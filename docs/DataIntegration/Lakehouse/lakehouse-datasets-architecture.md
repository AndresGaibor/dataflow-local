---
title: "Dataset architecture for CDC sources in a Qlik Open Lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-datasets-architecture.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "CDC data"]
---

# Dataset architecture for CDC sources in a Qlik Open Lakehouse

When you generate datasets in a Qlik Open Lakehouse, storage tables and change tables are generated automatically by Qlik Talend Data Integration. In AWS, views are also generated to access current and historical data. GCP projects do not generate storage views.

An intuitive and guided user interface helps you build, model, and execute data pipelines. You can automatically generate schemas for operational data stores (ODS) and historical data stores (HDS) without manual coding.

The following diagrams show the AWS and GCP architectures for a Qlik Open Lakehouse data pipeline using Qlik Data Gateway - Data Movement. Data lands in cloud storage and is stored in an Iceberg open lakehouse.

AWS architecture for a Qlik Open Lakehouse data pipeline. Optionally, tables can be mirrored to a data warehouse.

![AWS architecture for a Qlik Open Lakehouse data pipeline.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Upsolver/open_lakehouse_architecture.png "Click to view full size")

GCP architecture for a Qlik Open Lakehouse data pipeline. Tables are mirrored to BigQuery.

![GCP architecture for a Qlik Open Lakehouse data pipeline.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Upsolver/open_lakehouse_architecture-gcp.png "Click to view full size")

## Schemas

Artifacts are generated in an internal schema and a data task schema.

- The internal schema contains a physical table with multiple partitions.
- In AWS, the data task schema contains the views that you can use to consume the data.

  When an AWS schema is associated with more than one data task, each data task must use a unique prefix for tables and views. You can set the prefix in the data task settings.

Only internal schemas are checked for naming conflicts. For other schemas, you must ensure there are no naming conflicts in the table names. The best practice is to name the internal schema the same name as the data task schema with \_internal added. This ensures that every schema and prefix combination is unique.

Information noteAll tables and views are managed by Qlik Talend Data Integration. Do not alter the data using other tools.

## Tables

For each source table, a table is created in the internal schema with the suffix \_internal, using the format:

<INTERNAL\_SCHEMA>.<TABLE\_NAME>\_internal

This table contains five partitions, each serving a distinct purpose in how the data is processed and stored. Each partition leverages a subset of the table’s columns based on its role in the data lifecycle.

Information noteThe table in the internal schema is subject to change without notice. In AWS, use views to consume data where possible.

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

## Views in AWS

In AWS, views are updated in near real time. The following views are available to simplify querying and reporting:

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
