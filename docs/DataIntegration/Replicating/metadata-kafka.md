---
title: "Metadata and data messages"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/metadata-kafka.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to targets", "Connecting to streaming targets", "Kafka target"]
---

# Metadata and data messages

This topic describes the structure and content of the metadata and data messages produced by the Kafka target connector.

## Metadata message

Metadata message

| Field | Type | Description |
| --- | --- | --- |
| schemaId | String | The unique identifier of the Avro schema. |
| lineage | Structure | Information about the origin of the data (Qlik Talend Data Integration server, task, table, and so on) |
| server | String | The name of the Qlik Talend Data Integration server. |
| task | String | The name of the task. |
| schema (Schema Name) | String | The name of the database schema. |
| table (Table Name) | String | The name of the table. |
| tableVersion | Integer | Qlik Talend Data Integration maintains a version number of the structure of source table. Upon DDL change on the source, the version is increased and a new metadata message is produced. |
| timestamp | String | The date and time of the metadata message. |
| tableStructure | Structure | Describes the structure of the table. |
| tableColumns | Structure | Contains the list of columns and their properties. |
| {columns} | Structure | For each column, a record with the below properties. |
| ordinal | Integer | The position of the column in the record. |
| type | String | The column data type. |
| length | Integer | The maximum size of the data (in bytes) permitted for the column. |
| precision | Integer | For NUMERIC data type, the maximum number of digits required to represent the value. |
| scale | Integer | For NUMERIC data type, the maximum number of digits to the right of the decimal point permitted for a number. |
| primaryKeyPosition | Integer | The position of the column in the table’s Primary Key. or Unique Index. The value is zero if the column is not part of the table’s Primary Key. |
| dataSchema | String | The Avro schema for deserializing the Data messages. |

## Data message

Data message

| Field | Type | Description |
| --- | --- | --- |
| schema (name) | String | The name of the source database schema containing the replicated source table(s). |
| table (name) | String | The name of the source table. |
| headers | Structure | Information about the current record. |
| operation (Operation) | Enum | The operation type. Full Load - Initial load of the source data to the target topic(s)  REFRESH – Insertion of a record to the target during Full Load  CDC - Applies source table changes to the relevant topic  INSERT – Insertion of new target record  UPDATE – Update of an existing target record  DELETE – Deletion of a target record |
| changeSequence (Change Sequence) | String | A monotonically increasing change sequencer that is common to all change tables of a task.  Use this field to order the records in chronological order.  Applicable to CDC operations only. |
| timestamp (Timestamp) | String | The original change UTC timestamp.  Applicable to CDC operations only. |
| streamPosition | String | The source CDC stream position.  Applicable to CDC operations only. |
| transactionId (Transaction ID) | String | The ID of the transaction that the change record belongs to.  Use this field to gather all changes of a specific transaction.  Applicable to CDC operations only. |
| changeMask (Change Mask) | String | Indicates which data columns were changed in the source table.  The change mask is a string of hexadecimal digits, representing a bitmask of data columns in little-endian order. The bit position in the change mask is based on the ordinal of the column in the metadata message of that table.  This means that if there are 10 data columns, they occupy bits 0 to 9 in the bitmask.  If UPDATE mask is 0B hexadecimal, which is 1011 binary – it means that the columns at ordinals 1, 2 and 4 were changed.  The following describes the bit semantics:   - For INSERT records, all the inserted columns have the associated bits set. - For DELETE records, only primary-key (or unique index) columns have the associated bits set. This allows an applier to construct a DELETE statement without having to find the primary key fields from another source. - For UPDATE records, each column with a changed value will have the associated bit set.   Information note LOB columns are not included in the changeMask bit. |
| columnMask (Column Mask) | String | Indicates which data columns are present in the message. Usually, this will include all of the table columns.  Information note When moving from an Oracle source without full supplemental logging, some columns might not be present in the data, since they could not be moved.  The column mask is a string of hexadecimal digits, representing a bitmask of data columns in little-endian order. The bit position in the column mask is based on the ordinal of the column in the metadata message for that table.  This allows the applier to distinguish a null value that is the *actual* value of the column, from a null value that represents a column which could not be moved from the source database. |
| externalSchemaId | String | The Schema ID. This will only be displayed if the Include external Schema ID header check box is selected.  As the Schema ID changes whenever a DDL is performed on the source table, consumer applications can use this information to determine if the message schema has changed. |
| transactionEventCounter (Transaction Event Counter) | Long | The sequence number of the current operation in the transaction.  This can be used to determine the order of operations within a transaction. |
| transactionLastEvent (Transaction Last Event) | Boolean | "True" indicates that it is the final record in the transaction whereas "False" indicates that not all of the records have been processed. |
| data | Structure | The data of the table record |
| {columns} |  | The column names and values in the current record. |
| beforeData | Structure | The data of the table record, before the change |
| {columns} |  | The column names and values, before the change.  Applicable to UPDATE operation. |
