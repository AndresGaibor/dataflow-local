---
title: "Streaming data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/onboarding-data-streaming.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data"]
---

# Streaming data

The onboarding process transfers data from the source and stores it in Iceberg tables. Changes from the streaming data sources are continuously applied to the storage tables in near real time.

## Onboard data

Data is onboarded within a pipeline project and datasets are stored in the S3 location defined in the project settings.

1. In your project, click Create and then Onboard data.
2. Add a Task name and optional Description for the onboarding.

   Click Next.
3. Select the source connection.

   You can select an existing streaming source connection or create a new connection to the source.

   For more information, see [*Connecting to data streams*](../SourcesConnections/Connecting-Data-Streams.htm)

   Click Next and follow the instructions below for your data source.

### Selecting data

#### Apache Kafka

The list displays the available Kafka topics from the cluster defined in the source connection.

When selecting your topics, you can select specific datasets. You can also use selection rules to include or exclude groups of datasets:

- Use % as a wildcard to define a selection criteria for the datasets.

If topics are selected using selection rules, you can choose whether to load all datasets into the same target table or to create a separate target table for each source topic:

- By default, the target Iceberg table name is derived from the topic name, formatted to comply with naming conventions, for example, lowercase, spaces removed, dashes replaced with underscores. In Define target dataset name, you can edit the name of the target table
- When selection rules are used to load multiple topics into a single table, you must provide the target name.
- When selection rules are used and the data is loaded into a separate tables (one dataset per topic), the default target names are the topic names. At this stage, you cannot edit the names in the wizard, but this can be done later in the landing task.
- If a rule is configured to select topics for ingestion, any new topics that meet the rule criteria are also landed if the New topic  > Add to target option under schema evolution in the landing task settings is checked.

Select one or more datasets, or use a selection rule, and click Add. Click Next.

#### Amazon Kinesis

The list displays the available Kinesis streams defined in the source connection.

Select one or more datasets, and click Add. You can see the added datasets under Selected streams. Click Next.

#### Amazon S3

The directory browser displays a list of all the directories located in the S3 bucket of your source connection.

Information noteUsing a data pattern to select directories can improve performance.

- Select the directories to include when landing data:

  - For each directory, in Add path, enter the path and file name pattern:

    - Use \* as a wildcard to match any character.
    - To enter a date pattern, use <yyyy> as the four-digit year placeholder, <MM> as the two-digit month placeholder, <dd> as the two-digit day placeholder, and <HH> as the two-digit hour placeholder. For example:

      - MyDir3/<yyyy>\_<MM>\_<dd>\_<HH>\_orders.csv
      - MyDir3/<yyyy>/<MM>/<dd>/<HH>\_orders.csv
- Click Preview to open the Preview data dialog. A list of included and excluded files is displayed.
- Click Validate to check that the paths and the file name patterns are correct and functional.
- In Define target dataset name, provide a name to map the topic to the target Iceberg table. Click Next.

### Selecting the content type

Choose the source events content type.

- Select the type of events you are ingesting in Choose the type of data events.
- For more information, see [*Connecting to data streams*](../SourcesConnections/Connecting-Data-Streams.htm).

  The content type selected applies to all topics, datasets, or data events. You must create a new task for each content type you want to ingest.
- Expand Verify the events are correctly loaded to confirm the data can be parsed. It's a good idea to ensure data is correct at this stage, otherwise you need to recreate the pipeline and load the data again. Use Select dataset to examine specific datasets and check any warnings that may affect the loading of the data. Click the eye icon next to any struct columns to view the data.
- Click Next.

Information noteIf no events were detected for the dataset, a message is displayed in landing. You will need to run the task when there are events to read, and the columns will be added automatically.

### Setting ingestion properties

Configure the settings for your pipeline:

- Read data from

  - Start from the earliest event: ingest all historical data.
  - Start from now: ingest new data arriving from the time the pipeline starts.
- Column unnesting

  - Preserve nested columns: no transformations are applied.
  - Unnest into separate columns: data is split into separate columns.
- Load settings for new data sets

  - Append only: generally the best option for event data as it usually has a short life-span and is not updated, for example, Orders.
  - Apply changes: this is best suited to data that is updated over time, for example, Customers. Updates existing records and inserts new records based on key fields. You will need to specify the key fields later when defining the task.
- Target table partition

  The target table partition option applies to all tables in the pipeline. You can override this later at the table level to define custom partitioning.

  Information noteThis option is only available when Append only is selected in Load settings.

  - No partition: tables are created without any partitioning.
  - Partition by event ingestion date: tables are partitioned by the date events are ingested.

    Information noteWhen this option is selected together with the hdr\_\_from\_timestamp header column option, hdr\_\_from\_timestamp will be used as the default partition column. For information on adding the hdr\_\_from\_timestamp header column to standard views, see [*Table definitions*](storing-data-streaming.htm#Table).
- Data change handling

  Information noteThis option is only available when Apply changes is selected in Load settings.

  - Include soft deletions: Enter an expression to define which records to mark for deletion.
  - Create a historical data store (Type 2): This will keep previous versions of changed records.
- Click Next.

### Summary

The summary screen provides a visual display of your pipeline:

- Optionally, for the Streaming landing and Streaming Transform task, you can click Edit name and description to provide new values.
- Select the option for what you want to happen After the pipeline is created.
- When you have configured all the settings, click Create to create the streaming pipeline.
- When the project is displayed, you can prepare and run each task to begin ingesting the data.

  - Prepare and run the Streaming landing task.

    For more information, see [*Landing streaming data to Qlik Open Lakehouse*](landing-data-streaming.htm).
  - Prepare and run the Streaming Transform task.

    For more information, see [*Storing streaming datasets*](storing-data-streaming.htm).

## Data type mappings

The initial source schema is based on a sample of the data taken prior to the PREPARE phase when creating your pipeline project, and schema evolution is handled at read time. Mirror tasks and other downstream tasks that do not support STRUCT and ARRAY use a JSON type. Data can be parsed using SQL.

The following data type mappings apply to all the supported data sources, but vary according to the source file type, and the following should be noted:

- Data types are inferred from a sample of the data being onboarded. For example, if a field contains only integer values in the sample, it is created as INT8 in the streaming landing and transform tasks. If subsequent data includes double-precision fractional values, the landing files contain those values; however, in the Streaming transform task, if the Change field data type setting is set to Ignore, the column remains INT8 and the fractional values are truncated. To avoid unintended truncation, ensure the sample data includes the full range of expected values before onboarding, or configure Change field data type to Stop task during early stages and adjust data types as needed.
- If a field is added to a struct in the source, it is always added to the landing target. For streaming transformation, the behavior is applied according to the option chosen in Streaming transform task settings > Schema evolution > Add fields to struct (Apply to target, Ignore, Stop task).
- If a field is missing in a specific record, or an array is empty, they are treated as null.
- If a dataset is flattened by an array, and a record arrives where that array is empty or null, the system creates one row and the flattened field is null. It is not excluded automatically. If you want to exclude these rows, manually add a filter, for example, array\_element IS NOT NULL.
- The data types displayed in the UI reflect the selected dataset granularity. For flattened arrays, the data type of the individual element is shown rather than the array structure itself.
- A new attribute cannot be added inside a struct within a nested JSON field, only at the root level.
- In streaming transform tasks, flattening is supported for only a single level of an array. When flatten is applied to a multi-level array, for example, ARRAY<ARRAY<STRUCT>>, only the outer array is flattened, resulting in ARRAY<STRUCT> rather than a fully flattened STRUCT. Additionally, the current UI allows flattening to be configured only at the column level. As a result, selecting a multi-level array implicitly applies flattening to the first array level only.
- When you refer to an array of primitives, the data type of the element is used if the granularity is the array. Otherwise the array data type is used.

  In this example, OrderDetails has an array of CustomerID of data type INT. OrderDetails.CustomerID means INT if the granularity is OrderDetails.CustomerID and ARRAY<INT> if the granularity is OrderDetails.

### JSON

In JSON files, the numeric value in the source determines the target data type:

- INT8 is used for integer values that fit within the supported integer range and do not include a fractional component.
- REAL8 (DOUBLE) is used when the value contains a fractional component (floating-point number).
- STRING is used when the numeric value exceeds the maximum supported integer range.

Data types are mapped as follows:

| Source data types | Qlik Talend Data Integration data types |
| --- | --- |
| STRING | STRING |
| NUMBER | INT8 |
| NUMBER | REAL8 |
| NUMBER | STRING |
| BOOLEAN | BOOLEAN |
| ARRAY | ARRAY |
| OBJECT | STRUCT |

### CSV, TSV, REGEX, and SPLIT

By default, all source data types are ingested to a string. Use the option, Automatically infer types, to map source and target types as follows:

| Source data types | Qlik data types |
| --- | --- |
| NUMERIC | INT8/REAL8 |
| True/TRUE/true/False/FALSE/false | BOOLEAN |
| TIMESTAMP | Timestamps in the format yyyy-MM-dd HH:mm:ss or yyyy-MM-ddTHH:mm:ssz are parsed to a datetime type. If a timezone is included, the value is parsed as a string. |

### Parquet

Parquet files support physical and logical data types. Physical data types define how values are stored on disk, such as INT32, DOUBLE, or BYTE\_ARRAY. Logical data types provide semantic meaning on top of the physical representation, for example, identifying whether an integer value represents a date. When a logical type is attached to a Parquet column and is supported in Qlik Open Lakehouse (as listed below), the Streaming landing task uses the logical type when defining the target schema, rather than the underlying physical type. This ensures that data is interpreted correctly, preserves intended semantics such as precision, scale, and temporal meaning, and results in more accurate schemas when data is written to downstream formats.

Data sourced from Parquet files is mapped as follows:

| Source data types | Logical types | Qlik Talend Data Integration data types |
| --- | --- | --- |
| BOOLEAN |  | BOOLEAN |
| INT32 |  | INT8 |
| INT64 |  | INT8 |
| INT96 |  | DATETIME |
| FLOAT |  | REAL8 |
| DOUBLE |  | REAL8 |
| BYTE\_ARRAY |  | STRING (Encoded as Base64) |
| FIXED\_LEN\_BYTE\_ARRAY |  | STRING (Encoded as Base64) |
| BYTE\_ARRAY | STRING | STRING |
| BYTE\_ARRAY | ENUM | STRING |
| INT32 | DECIMAL | INT8 |
| INT64 | DECIMAL | INT8 |
| FIXED\_LEN\_BYTE\_ARRAY | DECIMAL | INT8/REAL8 (Encoded as Base64) |
| BYTE\_ARRAY | DECIMAL | INT8/REAL8 (Encoded as Base64) |
| INT32 | DATE | DATE |
| INT32 | TIME(MILLIS,true) | INT8 |
| INT64 | TIME(MICROS,true) | TIME |
| INT64 | TIMESTAMP(MICROS,true) | DATETIME |
| INT64 | TIMESTAMP(MILLIS,true) | DATETIME |
| NESTED TYPES |  | STRUCT |
| LIST |  | ARRAY |
| MAP |  | ARRAY<STRUCT>. Array of structs representing key-value pairs. |

### Avro

The following mappings apply to Avro files with schema registry.

| Source data types | Logical types | Qlik Talend Data Integration data types |
| --- | --- | --- |
| BOOLEAN |  | BOOLEAN |
| INT |  | INT8 |
| LONG |  | INT8 |
| FLOAT |  | REAL8 |
| DOUBLE |  | REAL8 |
| BYTES |  | STRING |
| STRING |  | STRING |
| RECORD |  | STRUCT |
| ENUM |  | STRING |
| ARRAY |  | ARRAY |
| MAP |  | ARRAY<STRUCT> |
| UNION |  |  |
| FIXED |  | STRING |
| BYTES | DECIMAL | DECIMAL |
| FIXED | DECIMAL | DECIMAL |
| INT | DATE | DATE |
| INT | TIME-MILLIS | INT8 |
| INT | TIME-MICROS | TIME |
| LONG | TIMESTAMP-MILLIS | DATETIME |
| LONG | TIMESTAMP-MICROS | DATETIME |

### ORC

The following mappings apply to ORC files.

| Source data types | Qlik Talend Data Integration data types |
| --- | --- |
| BOOLEAN | BOOLEAN |
| BYTE | INT8 |
| SHORT | INT8 |
| INT | INT8 |
| LONG | INT8 |
| DATE | DATE |
| FLOAT | REAL8 |
| DOUBLE | REAL8 |
| TIMESTAMP | DATETIME |
| BINARY | STRING |
| DECIMAL | REAL8 |
| STRING | STRING |
| VARCHAR | STRING |
| CHAR | STRING |
| LIST | ARRAY |
| MAP | ARRAY<STRUCT>. Array of structs representing key-value pairs. |
| STRUCT | STRUCT |
| UNION |  |

## Limitations and considerations

- If a structure or array is modified by automatic schema evolution in the landing, downstream views that were not created by a Qlik Talend Cloud streaming task may need to be updated in order not to be stale.
- If a task has parsing errors, it will not get to an error state, and will not be marked as attention required. As parsing errors are an always increasing metric, there is no exit criterion for an error state.
- Removing a cluster capability is only allowed if there are no tasks using that capability.
- Updates and deletes to a record with the same primary key must not cross partition boundary, that is, they need to be mapped to the same partition.
- If a source contains a large number of columns, only the top 500 columns by frequency are displayed in tasks and in the catalog. All columns are saved to the Avro files in S3 landing, but only the top 500 columns are stored in Iceberg tables. In schema evolution, if a new column is added, it will not be added to the top columns even if it is frequent.

  Information noteWhen ingesting sparse columns from SQL Server, the 500 count includes Qlik header columns.
