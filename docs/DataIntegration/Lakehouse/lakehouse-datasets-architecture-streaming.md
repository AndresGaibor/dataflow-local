---
title: "Dataset architecture for streaming sources in a Qlik Open Lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-datasets-architecture-streaming.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "Streaming data"]
---

# Dataset architecture for streaming sources in a Qlik Open Lakehouse

Streaming sources have their own architecture in Qlik Open Lakehouse as they do not require the Data Movement gateway to load data into the landing bucket, but are powered by the lakehouse cluster.

When you ingest files with a date pattern in the file name from Amazon S3 or Google Cloud Storage, the lakehouse cluster can use targeted list operations to reduce the number of files it checks. The Streaming landing task can request files within a specific date range instead of listing the entire bucket. The optional Delete after load setting can help maintain a small file count. There is no full load; the first records are considered inserted changes.

In a Qlik Open Lakehouse, the Streaming Transform task replaces the storage task. This task is used to transform and store landed data as Iceberg tables. A Streaming Transform task can only be added after a Streaming landing task. The Streaming Transform task supports two modes for updating records:

- Append only: Adds new records without modifying existing data, and key constraints are not enforced if duplicate records arrive.
- Apply changes (Merge): Updates existing records and inserts new records based on key fields. This mode gives you the option of using a soft delete, or retain historical data (Type 2).

The Streaming Transform task is a target based task, that maps between source and target and includes schema evolution capabilities. It provides extended transformation capabilities including unnesting of nested structures and flattening of arrays. For more information on the functions you can use in the Steaming Transform task, see [*Transformation functions*](transformation-functions.htm).

When you ingest from a streaming source, you have the ability to configure Iceberg partitioning, retention management, sort columns, snapshot expiration to control storage costs, and optimize for query performance.

The following diagrams show the AWS architecture in Append only and Merge modes. Both modes provide a current view and optional mirroring to a data warehouse. Merge mode also provides a history view.

Architecture for a streaming Qlik Open Lakehouse data pipeline on AWS in Append only mode

![Streaming data flows through landing and transformation to the current partition and current view on AWS, with optional mirroring to a data warehouse.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/open_lakehouse_streaming_append.png "Click to view full size")

Architecture for a streaming Qlik Open Lakehouse data pipeline on AWS in Merge mode

![Streaming data flows through landing and the change partition to current and prior partitions on AWS, with current and history views and optional mirroring to a data warehouse.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/open_lakehouse_streaming_merge.png "Click to view full size")

On Google Cloud, both modes use a Mirror task to make partitions and views available in Google BigQuery. Append only mode provides a current view, while Merge mode provides current and history views, as shown in the following diagrams.

Architecture for a streaming Qlik Open Lakehouse data pipeline on Google Cloud in Append only mode

![Streaming data flows through landing and transformation to the current partition, with a Mirror task providing the current partition and current view in Google BigQuery.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/open_lakehouse_streaming_append-gcp.png "Click to view full size")

Architecture for a streaming Qlik Open Lakehouse data pipeline on Google Cloud in Merge mode

![Streaming data flows through landing and the change partition to current and prior partitions, with a Mirror task providing partitions and current and history views in Google BigQuery.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/open_lakehouse_streaming_merge-gcp.png "Click to view full size")

## Landing tables

The following header columns are added to the landing tables. These columns always exist in landing data, but are not included in the downstream Streaming Transform task by default. You can add them to the Streaming Transform task using Add column from source, or reference them in the expression builder when adding or editing a column.

Header columns added for Kafka sources

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_kafka\_partition | Long | Kafka partition |
| hdr\_\_kafka\_topic | String | Kafka topic |
| hdr\_\_kafka\_offset | Long | Running value in partition |
| hdr\_\_kafka\_key | String | Base64 encoded key. Set to NULL string if not available. |
| hdr\_\_kafka\_headers | String | JSON with all message headers. Set to NULL string if not available. |

Header columns added for Amazon Kinesis sources

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_kinesis\_stream | String | Amazon Kinesis stream |
| hdr\_\_kinesis\_shard | String | Amazon Kinesis shard |
| hdr\_\_kinesis\_offset | String | Amazon Kinesis offset |

Header columns added for Amazon S3 and Google Cloud Storage sources

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_file\_name | String | File name |
| hdr\_\_file\_size | Long | File size in bytes. |

## Schemas

Artifacts are generated in an internal schema and a data task schema.

- The internal schema contains a physical table with multiple partitions.
- The data task schema contains the views that you can use to consume the data.

  When a schema is associated with more than one data task, each data task must use a unique prefix for tables and views. You can set the prefix in the data task settings.

Only internal schemas are checked for naming conflicts. For other schemas, you must ensure there are no naming conflicts in the table names. The best practice is to name the internal schema the same name as the data task schema with \_internal added. This ensures that every schema and prefix combination is unique.

Information noteAll tables and views are managed by Qlik Talend Data Integration. Do not alter the data using other tools.

## Tables

For each source table, a table is created in the internal schema with the suffix \_internal, using the format:

<INTERNAL\_SCHEMA>.<TABLE\_NAME>\_internal

This table contains five partitions in Apply changes (Merge) mode, each serving a distinct purpose in how the data is processed and stored. Each partition leverages a subset of the table’s columns based on its role in the data lifecycle. In Append only mode the table has no partitions and behaves like the Current partition (ODS).

Information noteThe table in the internal schema is subject to change without notice. You should primarily use views to consume data where possible.

The internal dataset is structured to efficiently manage incoming data from your source system, supporting real-time ingestion and historical tracking.
The flow of data is managed through several specialized partitions, each described below:

- Changes partition – Real-time ingestion

  All changes from the source system—inserts, updates, and deletes—are first appended to the Changes partition.

  - Acting as a raw changelog, the partition provides a complete feed of source activity before any transformations occur.
  - Each change is tagged with a type (I, U, or D), indicating how it is processed.
  - Events are captured from the source as they occur. The partition is updated in near real-time.
  - The Changes partition is available when the following settings are applied in the Lake landing data task.

    - In the General tab, the Update method is set to CDC.
    - Full load is enabled.
- Asset\_state partition - Tracking progress

  As changes are ingested, the Asset\_state partition logs two key timestamps:

  - When changes were last appended to the Changes partition.
  - When changes were last applied to the Current partition.

  This provides full visibility into the synchronization pipeline and helps with monitoring or troubleshooting delays.
- Current partition (ODS) – Latest replica of the source

  Changes from the Changes partition are periodically applied to the Current partition to maintain an up-to-date, query-optimized copy of the source data.

  - A background task runs automatically to apply those updates. This is based on the volume of accumulated changes, rather than a fixed schedule.
  - The initial full load is written directly to the Current partition.
  - This partition reflects the current state of the data and is designed for efficient querying.
- Prior partition (HDS) – Historical data

  When an a record is updated or deleted in the Current partition, a copy of the previous version is written to the Prior partition.

  - Records contain metadata, including change history and the date range when the data is valid.
  - This supports Type 2 slowly changing dimension (SCD2).
  - The Prior partition is available when Keep historical records and archive of change records is enabled in the General tab of the Storage data task settings.
  - When an updated version of a record enters the Current partition, the previous record is moved to the Prior partition for historical tracking.
- Reload partition

  The Reload partition acts as a temporary staging area during manual or scheduled full reloads:

  - New data is first written to the Reload partition.
  - Regular maintenance tasks clear any pending changes before they are paused.
  - Data is compared with the Current partition, and only the differences are moved to the Current partition.
  - The Reload partition is cleared when the operation completes.

  This process ensure minimal disruption to the main dataset during full reload operations.

### Current partition

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | VARBINARY (20) | Hash of all record primary keys. Hash format is SHA1. Columns are separated by a backspace character. |
| hdr\_\_from\_timestamp | TIMESTAMP | Timestamp in UTC:   - For data taken from a full load, this is the full load start time. - For a change coming from the Changes partition, this is the timestamp field of the record. |
| hdr\_\_operation | VARCHAR (1) | Latest operation of this record.   - D - deleted from Changes partition. - U - updated from Changes partition. - I - inserted from the Changes partition. - L - inserted by the full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_inserted\_timestamp | TIMESTAMP | UTC timestamp of the first time the key was added. When using full load, the start time of the full load. |
| hdr\_\_modified\_timestamp | TIMESTAMP | UTC timestamp of when the last update was made. |

### Prior partition

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | VARBINARY (20) | Hash of all record primary keys. |
| hdr\_\_from\_timestamp | TIMESTAMP | Timestamp in UTC. |
| hdr\_\_to\_timestamp | TIMESTAMP | Timestamp in UTC. |
| hdr\_\_operation | STRING (1) | Latest operation of this record.   - D - deleted from Changes partition. - U - updated from Changes partition. - I - inserted from the Changes partition. - L - inserted by the full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_was\_current\_from\_timestamp | TIMESTAMP | Timestamp in UTC for the first time record was current. |
| hdr\_\_was\_current\_to\_timestamp | TIMESTAMP | Timestamp in UTC for the last time record was current. |

### Changes partition

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_change\_identifier | VARCHAR (50) | The change identifier is a string with two parts:   - Batch run start timestamp in milliseconds since 1/1/1970 (10 digit string). - Change sequence from the replication gateway (35 characters). |
| hdr\_\_operation | VARCHAR (1) | Latest operation of this record.   - D - deleted from the Changes partition. - U - updated from the Changes partition. - I - inserted from the Changes partition. - L - inserted by the full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_timestamp | TIMESTAMP | Timestamp in UTC. |
| hdr\_\_key\_hash | BINARY (20) | Hash of all record primary keys. |
| hdr\_\_inserted\_timestamp | TIMESTAMP | UTC timestamp of the time when the change was processed by Qlik. |

### Asset\_state partition

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_apply\_change\_identifier | VARCHAR (50) | The change identifier of the latest change applied to the Current partition. |
| hdr\_\_copy\_change\_identifier | VARCHAR (50) | The change identifier of the latest change appended to the Changes partition. |

### Reload partition

The columns used by the Reload partition are identical to the Current partition.

## Views

All views created are updated in near real time. The following views are available to simplify querying and reporting:

### Current

The Current view reflects the most recent state of the data. This view represents a replica of the source table, updated in near-real time. It merges data from the Current and Changes partitions.

Name: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>

No header columns are added to the table structure.

### History

A History view is generated in the data asset schema for each selected source table when History is enabled in the data task settings. The History view merges data from the Prior and Changes partitions. It provides a complete timeline of changes, ideal for audit or historical analysis.

Name: <EXTERNAL\_SCHEMA>.[<PREFIX>]<TABLE\_NAME>\_<Suffix for history views>

The following header fields are added to the History view:

| Field | Type | Description |
| --- | --- | --- |
| hdr\_\_key\_hash | BINARY (20) | Hash of all record primary keys. |
| hdr\_\_from\_timestamp | TIMESTAMP | The timestamp when the change occurred in the source system. This reflects when the user originally made the change. |
| hdr\_\_to\_timestamp | TIMESTAMP | The timestamp when the change was reversed or updated in the source system. |
| hdr\_\_store | VARCHAR (10) | This indicates where the record resides:   - CURRENT - if the record resides in the Current partition. - PRIOR - if the record resides in the Prior partition with historical data. |
| hdr\_\_operation | STRING (1) | Latest operation of this record.   - D - deleted from the Changes partition. - U - updated from the Changes partition. - I - inserted from the Changes partition. - L - inserted by the full load task. - d - deleted from compare and apply. - u - updated from compare and apply. - i - inserted from compare and apply. |
| hdr\_\_deleted | BIT | Indicates if the record is soft deleted, based on if hdr\_\_operation is D or d. |
| hdr\_\_was\_current\_from\_timestamp | TIMESTAMP | The time (UTC) when this row entered the Current partition. This is typically when the storage job ran and the change was applied. |
| hdr\_\_was\_current\_to\_timestamp | TIMESTAMP | The time (UTC) when the row was removed from the Current table, for example, due to a newer version. |

Information noteThe Current and History views rely on the Changes partition and are always near real-time.
However, if you experience slow query performance, it may be due to a large number of changes that have not yet been applied into the Current or Prior partitions. Unmerged deltas require more processing at query time, making access slower.

### Showing header columns in views

You can control whether to show or hide the header columns. The options differ according to task type.

Information noteHeader columns are auto-populated with data and read-only.

#### Streaming landing task

To show the header columns, toggle on Show header columns to the right of the Search box.

#### Streaming transform task

A drop-down list with the following options is available to the right of the Search box.

- Hide header columns: The default.
- Show header columns

  - Standard: Select to show header columns for standard views.
  - History: Select to show header columns for history views. Note that this option will only be available if Create a historical data store (Type 2) is enabled in the task or dataset settings.

For a description of the available header columns, see [*Landing tables*](#Landing) and [*Views*](#Views).

Govnote-not-inNot supported in Qlik Cloud Government.
