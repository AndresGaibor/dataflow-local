---
title: "Dataset architecture in a cloud data warehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Storage/dataset-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Dataset architecture in a cloud data warehouse

Qlik Talend Data Integration lets you create, manage, and control an analytics data pipeline, delivering data all the way to consumers. When you generate datasets in a cloud data warehouse with Qlik Talend Data Integration, storage tables, change tables and views are generated.

An intuitive and guided user interface helps you build, model and execute data pipelines. Automatically generate schemas for operational data stores (ODS) and historical data stores (HDS) without manual coding.

Architecture for a Qlik Talend Data Integration data pipeline using Qlik Data Gateway - Data Movement and CDC

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_DIArchitecture_v1.svg "Click to view full size")

- Landing

  The landing task in Qlik Talend Data Integration controls the continuous landing of data from the data sources to the landing zone. The example in the diagram describes using Qlik Data Gateway - Data Movement to access data sources using CDC to keep the data up-to-date. You can also use Qlik Cloud source connections to perform full loads that can be scheduled to reload periodically.

  For information about when you need to use Data Movement gateway, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top)

  Information noteTables in the landing zone are generated for internal use by Qlik Talend Data Integration Storage data tasks. Do not use the landing tables in any other downstream processes.
- Storage

  The storage task controls when data is applied to the storage tables, and creates and manages the tables and external views.
- External views

  When consuming data, the best practice is to use views. Views provide several benefits over tables including improved data concurrency.

## Using live views

You can access both current data (ODS) and historical data (HDS) using live views. Live views include data from changes tables that is not yet applied to the current or prior tables. This lets you see data with lower latency without having to apply changed data frequently. The ability to delay the merge allows for reduced costs and processing requirements in the target platform.

Another benefit with live views is that the compute tier does not need to run all the time.

- Landing can point to an explicit warehouse that can be small, as it just performs INSERT operations for fast execution.
- The storage process, running once a day for example, can wake up a large compute layer for processing.
- Latency can be improved, as we no longer need to apply changes throughout the day. When inserted new records are available in the changes table, they are available right away in the live views.

## Schemas

Artifacts are generated in an internal schema and a data task schema.

- The internal schema contains the physical data tables.
- The data task schema contains the views that you can use to consume the data.

  When a schema is associated with more than one data task, each data task must use a unique prefix for tables and views. You can set the prefix in the data task settings.

Only internal schemas are checked for naming conflicts. For other schemas, you must make sure there are no naming conflicts in the table names. The best practice is to name the internal schema the same name as the data task schema with \_internal added. This will effectively make sure that every schema and prefix combination is unique.

Schemas created by Qlik Talend Data Integration will not be deleted when you delete tasks or projects.

Information noteAll tables and views are managed by Qlik Talend Data Integration. Do not alter the data using other tools.

## Tables

The following tables are created in the internal schema.

Information noteTables in the internal schema are subject to change without notice. You should primarily use views to consume data where possible.

- Current table (ODS)

  This table contains the replica of the data source updated with changes during the latest apply interval.
- Prior table (HDS)

  This table contains type 2 historical data. It is only generated if History is enabled in the data task settings.

  When a source table record is updated, a new record is added to the prior table each time. The history record is a copy of the previous current record, which also includes what was updated, and when it was valid.

  Use a history view or a history live view to view historical data. For more information see [*History view*](#History) and [*History live view*](#History2).
- Change table

  This table contains all changes to the corresponding source table from the start of the task, and is never truncated. It is only generated if the landing mode is Full load and CDC.

  Tip noteIf your system handles a high volume of changes, consider periodically truncating applied changes from the Change Tables. This should reduce resource consumption and improve performance.

Information note

When you re-insert a record that was previously deleted, and the records have the same primary key value. hdr\_\_operation will have the value U - updated.

Column names starting with hdr\_\_ are reserved for use in header columns by Qlik Talend Data Integration. For more information, see [*Ambiguous column names*](../Deploying/Troubleshooting-data-assets.htm#Ambiguou).

### Current table

Naming: <INTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>\_current

The following header columns are added to the table structure.

Current table header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | varbinary(20) | Hash of all record primary keys. Hash format is SHA1. Columns are separated by a backspace character.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |
| hdr\_\_from\_timestamp | timestamp | Timestamp in UTC   - For data taken from full load, it will be the full load start time. - For a change coming through change tables, it will be the timestamp field of the record. |
| hdr\_\_operation | string(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - L - inserted by full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_inserted\_timestamp | timestamp | UTC timestamp of the first time the key was added. When using full load, the start time of the full load. |
| hdr\_\_modified\_timestamp | timestamp | UTC timestamp of when the last update was applied. |

### Prior table

The following header fields are added.

Naming: <INTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>\_prior

Prior table header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | varbinary(20) | Hash of all record primary keys.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |
| hdr\_\_from\_timestamp | timestamp | Timestamp in UTC |
| hdr\_\_to\_timestamp | timestamp | Timestamp in UTC |
| hdr\_\_operation | string(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - L - inserted by initial load. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_was\_current\_from\_timestamp | timestamp | Timestamp in UTC for first time record was current. |
| hdr\_\_was\_current\_to\_timestamp | timestamp | Timestamp in UTC for last time record was current. |

### Changes table

Naming: <INTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>\_ct

The following header fields are added to the table structure.

Change table header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_change\_identifier | varchar(50) | The change identifier is a string with two parts:   - Batch run start timestamp in milliseconds since 1/1/1970 (10 digit string) - Change sequence from the replication gateway (35 characters) |
| hdr\_\_operation | varchar(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_timestamp | timestamp | Timestamp in UTC . |
| hdr\_\_key\_hash | binary(20) | Hash of all record primary keys.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |

## Views

The following views are created in the data task target schema. Which views are created depends on if you have enabled live views and history, and if you use change handling.

- Standard view
- Live view
- Changes view
- History view
- History live view

Information noteAll header column names, starting with hdr\_\_, are reserved. If you consume a view in a storage task, you must rename the consumed header columns in the storage task to avoid a naming conflict, as the storage task will generate views with the same header columns.

### Standard view

Naming: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>

No header columns are added to the table structure.

### Live view

Live views show a view for each selected source table which merges the table with changes from the change table. This provides queries with a live view of the data without having to wait for the next apply cycle. The changes merged from the change table view are not transaction consistent between tables.

Live views are only created if you enable Live views in the settings of the data task.

Naming: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>< Suffix for live views>

Table header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | varbinary(20) | Hash of all record primary keys. Hash format is SHA1. Columns are separated by a backspace character.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |
| hdr\_\_from\_timestamp | timestamp | Timestamp in UTC   - For data taken from full load, it will be the full load start time. - For a change coming through change tables, it will be the timestamp field of the record. |
| hdr\_\_operation | string(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - L - inserted by full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_inserted\_timestamp | timestamp | UTC timestamp of the first time the key was added. When using full load, the start time of the full load. |
| hdr\_\_modified\_timestamp | timestamp | UTC timestamp of when the last update was applied. |
| hdr\_\_store | varchar(10) | This indicates where the record resides.   - CURRENT - if the record resides in the current physical table. - CHANGES - if the record resides in the change table. |

### Changes view

This is a view of the change table in the landing schema for each selected source table.

Naming: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>\_changes

The following header fields are added to the table structure.

Changes view header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_change\_identifier | string(50) | The change identifier is a string with two parts:   - Batch run start timestamp in milliseconds since 1/1/1970 (10 digit string) - Change sequence from the replication gateway (35 characters) |
| hdr\_\_from\_timestamp | timestamp | Timestamp in UTC   - For data taken from full load, it will be the full load start time. - For a change coming through change tables, it will be the timestamp field of the record. |
| hdr\_\_to\_timestamp | timestamp | Timestamp in UTC   - For data taken from full load, it will be the full load start time. - For a change coming through change tables, it will be the timestamp field of the record. |
| hdr\_\_operation | string(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - L - inserted by full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_timestamp | timestamp | Timestamp in UTC . |
| hdr\_\_key\_hash | binary(20) | Hash of all record primary keys.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |

### History view

A history view is generated in the data asset schema for each selected source table if History is enabled in the data task settings. The following header fields are added.

Naming: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>< Suffix for history views>

History view header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | binary(20) | Hash of all record primary keys.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |
| hdr\_\_from\_timestamp | timestamp | Timestamp in UTC   - For data taken from full load, it will be the full load start time. - For a change coming through change tables, it will be the timestamp field of the record. |
| hdr\_\_to\_timestamp | timestamp | Timestamp in UTC   - For data taken from full load, it will be the full load start time. - For a change coming through change tables, it will be the timestamp field of the record. |
| hdr\_\_was\_current\_from\_timestamp | timestamp | Timestamp in UTC for first time record was current. |
| hdr\_\_was\_current\_to\_timestamp | timestamp | Timestamp in UTC for last time record was current. |
| hdr\_\_store | varchar(7) | This indicates where the record resides.   - CURRENT - if the record resides in the current physical table. - PRIORS - if the record resides in the priors table with historical data. |
| hdr\_\_operation | string(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - L - inserted by full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_deleted | bit | Indicates if the record is soft deleted, based on if hdr\_\_operation is D or d. |

### History live view

A history live view is generated in the data asset schema for each selected source table for each selected source table merged with changes from the change table. The following header fields are added.

Naming: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>< Suffix for live history views>

Live history view header fields

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | binary(20) | Hash of all record primary keys.  This column is not generated in Data mart data tasks. |
| hdr\_\_key\_id | int64 | Sequence incremented per record.  This column is only generated in Data mart data tasks. |
| hdr\_\_store | varchar(10) | This indicates where the record resides.   - CURRENT - if the record resides in the current physical table. - PRIORS - if the record resides in the priors table with historical data. - CHANGES - if the record resides in the change table. |
| hdr\_\_operation | string(1) | Latest operation of this record.   - D - deleted from change table. - U - updated from change table. - I - inserted from change table. - L - inserted by full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_deleted | bit | Indicates if the record is soft deleted, based on if hdr\_\_operation is D or d. |
