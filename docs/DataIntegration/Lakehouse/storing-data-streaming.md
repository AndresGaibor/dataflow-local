---
title: "Storing streaming datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/storing-data-streaming.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "Streaming data"]
---

# Storing streaming datasets

The following Streaming Transformation task settings apply to Qlik Open Lakehouse projects using a streaming source.

You can store and transform streaming data using the Streaming Transform data task. Streaming data often contains nested structures and arrays that require flattening, and transformation capabilities are needed during the storage phase. These capabilities are available to the Streaming Transformation task, enabling you to apply transformations immediately after landing your streaming data.

## Managing dataset granularity

You can flatten nested structures and arrays to increase granularity. Granularity is displayed in the Dataset view. Click ![edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) to edit granularity:

- Selecting a field from an array will cause the target table to include one row per element. This will increase the number of rows in the target.
- You must select fields from the same array path. Selecting fields from different paths will raise a validation error.
- Displayed data types reflect the selected granularity. For example, an ARRAY<INT> becomes INT when it is flattened. For more information, see [*Data type mappings*](onboarding-data-streaming.htm#Data).

## Deleting a task

You can delete the data task if it is not running, and there are no dependencies to downstream tasks in the same project.

- In Pipeline project view of the project, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Delete.

Artifacts (tables and views) created by the task will also be deleted, unless you select to keep them.

Information noteKeep in mind that the artifacts you keep will no longer be updated by the task.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Streaming Transform settings

You can set properties for the Streaming Transform data task when the data platform is Qlik Open Lakehouse.

- Click Settings.

### General settings

- Task schema

  You can change the name of the Streaming Transform task schema. Default name is the name of the storage task.
- Internal schema

  You can change the name of the internal storage data asset schema. Default name is the name of the storage task with \_internal appended.
- Prefix for all tables and views

  You can set a prefix for all tables and views created with this task.

  Information noteYou must use a unique prefix when you want to use a database schema in several data tasks.
- Folder to use

  You can change the Streaming Transform task storage folder.
- Load settings for new datasets

  - Append only

    Adds new records without modifying existing data. Key constraints are not enforced if duplicate records arrive.
  - Apply changes

    Updates existing records and inserts new records based on key fields.

    If you select to merge changes, you can also select the following:

    - Soft delete records by providing deletion expression

      Define a deletion expression to mark records for deletion.
    - Keep historical records (Type 2)

      Keep previous versions of changed records.
- Column unnesting

  - Preserve nested columns

    Select to preserve nested data.
  - Unnest into separate columns

    The default behavior is to unnest data into separate columns.
- Target tables partition

  Information noteThis option is only available when Append only is selected in Load settings.

  - No partition

    New tables are created without partitions.
  - Partition by event date

    New tables are partitioned by the date events are ingested.
- Data change handling

  Information noteThis option is only available when Apply changes is selected in Load settings.

  - Include soft deletions: Enter an expression to define which records to mark for deletion.
  - Create a historical data store (Type 2): This will keep previous versions of changed records.
- Retention management
  - No partition pruning
  - Current snapshot partition pruning

### Table definitions

- hdr\_\_from\_timestamp

  When this option is enabled, the hdr\_\_from\_timestamp header column will appear in standard views. In addition, when Partition by event ingestion date is selected in the onboarding wizard, hdr\_\_from\_timestamp will be used as the default partition column.

  Information noteHistory views always include all standard view header columns, regardless of this setting.

### Runtime settings

- Lakehouse cluster

  You can change the lakehouse cluster, but this must support streaming workloads or mixed workloads.

### Schema evolution settings

- Add new datasets

  This setting applies when new datasets are added to the streaming landing task.

  Information noteOnly supported when streaming landing reads from Kafka.

  - Apply to target

    Automatically adds new datasets from the Streaming landing task to the Streaming Transform task. This is the default setting.
  - Ignore

    Does not add new datasets.
- Add columns on root level

  This setting applies when new columns are added to the streaming landing task at the root level.

  - Apply to target

    Automatically adds new root level columns from the Streaming landing task to the Streaming Transform task. This is the default setting.
  - Ignore

    Does not add new root level columns.
  - Stop task

    Stops the transform task if a new root level column is detected in the streaming landing task.
- Add columns to structures

  This setting applies when new fields are added inside an existing nested structure in the streaming landing task.

  - Apply to target

    Automatically adds new fields to existing structures in the Streaming Transform task if they are added to the landing structure.
  - Ignore

    Does not add new fields to existing structures.
  - Stop task

    Stops the transform task if a new field is added to a structure in the Streaming landing task.
- Change field data type

  - Ignore

    Does not change the data type.
  - Stop task

    Stops the transform task if a data type change is detected in the Streaming landing task.

## Dataset settings

The following settings are available for all datasets in Design view > Datasets.

Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) next to the dataset and select Settings.

- Data load handling

  Selects how data is loaded into the target table.

  - Append only

    Adds new records without modifying existing data. Key constraints are not enforced if duplicate records arrive.
  - Apply changes

    Updates existing records and inserts new records based on key fields.
- Data change handling

  Information noteThis option is only available when Apply changes is selected in Load settings.

  - Include soft deletions: Enter an expression to define which records to mark for deletion. This should be an expression that validates to True if the change is a soft delete.

    Example: operation = 'D'
  - Create a historical data store (Type 2): This will keep previous versions of changed records.
- Partition columns

  Information noteThis option is only available when Append only is selected in Load settings.

  Optionally, you can select partition columns to optimize performance.

  Click Add column to add a partition column, then select a Transform, and set a Parameter if required.
- Retention management

  Partition pruning removes partitions that are older from the retention period. This does not physically delete the data and does not impact older snapshots immediately. Older data may be available in older snapshots until they are expired.

  Information noteAppears only if the partition has at least one date or datetime column.

  - No partition pruning
  - Current snapshot partition pruning
- Sort columns

  Information noteThis option is only available when Append only is selected in Load settings.

  Optionally, you can specify the columns by which data will be sorted within each file of your Iceberg table. During data ingestion, Iceberg uses these columns to order records. Defining sort keys on columns frequently used in queries improves data locality, resulting in faster read performance and more efficient compression. Properly configured sort keys ensure that your data is optimally organized for query performance.

  Click Add column to add a sort column, and then set the sort order.
- Snapshot expiration duration

  This setting controls how long snapshots are retained, which significantly impacts table size and storage costs. For frequently updated tables, a shorter duration is recommended to help reduce storage costs.

  Information noteEnter 0 to disable snapshot expiration.
- Standard view headers

  - Inherit from data task settings

    This is the default. Disable if you want to set specific header columns for this dataset only.
  - hdr\_\_from\_timestamp

    When this option is enabled, the hdr\_\_from\_timestamp header column will appear in standard views. In addition, when Partition by event ingestion date is selected in the onboarding wizard, hdr\_\_from\_timestamp will be used as the default partition column.

    Information noteHistory views always include all standard view header columns, regardless of this setting.
