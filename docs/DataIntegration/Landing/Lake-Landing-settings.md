---
title: "Lake landing settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/Lake-Landing-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Landing data to a lakehouse"]
---

# Lake landing settings

You can configure settings for the Lake landing data task.

- Open the landing task and click Settings in the toolbar.

The Settings: <Task-Name> dialog opens. The available settings are described below.

## General

- Update method

  The landing task always starts with a Full Load. After the Full Load completes, you can keep the landed data up-to-date using one of the following methods:

  Information noteIt is not possible to change the update method once the landing data task prepare operation has completed.

  - Change data capture (CDC)

    The landed data is kept up-to-date using CDC (Change Data Capture) technology. CDC may not be supported by all data sources. CDC does not capture DDL operations, such as renaming columns, or changes in metadata.

    If your data also contains views or tables that do not support CDC, two data pipelines will be created. One pipeline with all tables supporting CDC, and another pipeline with all other tables and views using Reload as the update method.
  - Reload

    All of the landed data is reloaded from the source. This is useful if your source does not support CDC, but can be used with any supported data source.

    You can schedule the reloads periodically.
- Folder to use

  Select which folder to use when landing data to the staging area.

  - Default folder

    This creates a folder with the default name: <project name>/<data task name>.
  - Root folder

    Store data in the root folder of the storage.
  - Folder

    Specify a folder name to use.

## Data uploading

- Maximum files size (MB)

  The maximum size a file can reach before it is closed. Smaller files might be uploaded faster (depending on the network) and improve performance when used in conjunction with the parallel execution option. However, it is generally considered bad practice to clutter the database with small files.

  Information noteThis setting is relevant for all data platforms except Qlik Cloud.
- Use compression

  When selected, the CSV files will be compressed (using gzip) before being uploaded to Google BigQuery.

  Information note
  - This setting is relevant for Google BigQuery only.
  - Requires Data Movement gateway 2023.5.16 or later.

## Metadata

### LOB columns

Information noteThis setting is not available for tasks using a SaaS application connector, unless it is a [Lite connector](connecting-web-applications.htm#Lite).

- Include LOB columns and limit column size to (KB):

  You can choose to include LOB columns in the task, and set the maximum LOB size. LOBs that are larger than the maximum size will be truncated.

  Information noteWhen using Azure Synapse Analytics as a target, maximum LOB size cannot exceed 7 MB.

### Control tables

Select which of the following control tables you want to be created on the target platform:

- Landing Status: Provides details about the current landing task including task status, amount of memory consumed by the task, number of changes not yet applied to the data platform and the position in the source endpoint from which Data Movement gateway is currently reading.
- Suspended Tables: Provides a list of suspended tables, and the reason they were suspended.
- Landing History: Provides information about the task history including the number and volume of records processed during a landing task, latency at the end of a CDC task, and more.
- DDL History: Contains a history of all supported DDL changes that
  occurred during a task.

  The DDL History table is supported with the following target platforms only:

  - Databricks
  - Microsoft Fabric
  - Amazon Redshift
  - If you are using Data Movement gateway, the following targets need version 2024.11.14 or later:
    - Amazon S3
    - Google Cloud Storage
    - Snowflake
  - Kafka - If you are using Data Movement gateway, version 2025.5.42 or later is required.
  - If you are using Data Movement gateway, the following targets need version 2025.11.1 or later:
    - Google BigQuery
    - Google Cloud Alloy DB for PostgreSQL
      (via the PostgreSQL connector)
    - Google Cloud SQL for PostgreSQL
      (via the PostgreSQL connector)
    - Microsoft Azure Database for PostgreSQL
      (via the PostgreSQL connector)
    - PostgreSQL

For a detailed description of each of the control tables, see [*Control tables*](../Replicating/control_tables.htm)

## Full load

Information noteThese settings are not available for tasks using a SaaS application connector.

### Performance tuning

- Maximum number of tables to load in parallel: Enter the maximum number of tables to load into the target at one time. The default value is 5.
- Transaction consistency timeout (seconds): Enter the number of seconds to wait for open transactions to close, before beginning the Full Load operation. The default value is 600 (10 minutes). The full load will start after the timeout value is reached even if there are transactions that are still open.

  Information noteTo replicate transactions that were open when Full Load started but were only committed after the timeout value was reached, you need to reload the target tables.
- Commit rate during full load: The maximum number of events that can be transferred together. The default value is 10000.

### After full load completes

Create primary key or unique: Select this option if you want to delay creation of the primary key or unique index on the data platform until after full load completes.

- ### For initial load

Information note
If you are using Data Movement gateway to access your data source, these settings require version 2022.11.74 or later.

|  |  |
| --- | --- |
| Use cached data | This option lets you use cached data that was read when generating metadata with Full data scan selected.  This creates less overhead regarding API use and quotas, as the data is already read from the source. Any changes since the initial data scan can be picked up by Change data capture (CDC). |
| Load data from source | This option performs a new load from the data source. This option is useful if:   - The metadata scan was not performed recently. - The source dataset is small and frequently changing, and you do not want to maintain a full history of changes. |

## Error handling

### Data errors

Information note

Data error handling is supported with the Change Data Capture (CDC) update method only.

For data truncation errors: Select what you want to happen when a truncation occurs in one or more specific records. You can select one of the following from the list:

- Ignore: The task continues and the error is ignored.
- Suspend table: The task continues, but data from the table with the error record is moved into an error state and its data is not replicated
- Stop task: The task is stopped and manual intervention is required.

For other data errors: Select what you want to happen when an error occurs in one or more specific records. You can select one of the following from the list:

- Ignore: The task continues and the error is ignored.
- Suspend table: The task continues, but data from the table with the error record is moved into an error state and its data is not replicated
- Stop task: The task is stopped and manual intervention is required.

Escalate error handling when other data errors reach (per table): Select this check box to escalate error handling when the number of non-truncation data errors (per table) reaches the specified amount. Valid values are 1-10,000.

Escalation action: Choose what should happen when error handling is escalated. Note that the available actions are dependent on the action selected from the For other data errors drop-down list described above.

- Suspend table (default): The task continues, but data from the table with the error record is moved into an error state and its data is not landed.
- Stop task: The task is stopped and manual intervention is required.

### Table errors

When encountering a table error: Select one of the following from the drop-down list:

- Suspend table (default): The task continues but data from the table with the error record is moved into an error state and its data is not replicated
- Stop task: The task is stopped and manual intervention is required.

Escalate error handling when table errors reach (per table): Select this check box to escalate error handling when the number of table errors (per table) reaches the specified amount. Valid values are 1-10,000.

Escalation action: The escalation policy for table errors is set to Stop task and cannot be changed.

### Environmental

- Maximum retry count: Select this option and then specify the maximum number of attempts to retry a task when a recoverable environmental error occurs. After the task has been retried the specified number of times, the task is stopped and manual intervention is required.

  To never retry a task, clear the check box or specify "0".

  To retry a task an infinite number of times, specify "-1"

  - Interval between retry attempts (seconds): Use the counter to select or type the number of seconds that the system waits between attempts to retry a task.

    Valid values are 0-2,000.
- Increase retry interval for long outages: Select this check box to increase the retry interval for long outages. When this option is enabled, the interval between each retry attempt is doubled, until the Maximum retry interval is reached (and continues retrying according to the specified maximum interval).
  - Maximum retry interval (seconds): Use the counter to select or type the number of seconds to wait between attempts to retry a task when the Increase retry interval for long outages option is enabled. Valid values are 0-2,000.

## Change processing tuning

Information noteThis tab is only available when the update method is Change data capture (CDC).

#### Transactional offload tuning

Offload transactions in progress to disk if:

Transaction data is usually kept in memory until it is fully committed to the source or target. However, transactions that are larger than the allocated memory or that are not committed within the specified time limit will be offloaded to disk.

- Total memory size for all transactions exceeds (MB): The maximum size that all transactions can occupy in memory before being offloaded to disk. The default value is 1024.
- Transaction duration exceeds (seconds): The maximum time that each transaction can stay in memory before being offloaded to disk. The duration is calculated from the time Qlik Talend Data Integration started capturing the transaction. The default value is 60.

#### Batch tuning

Some of the settings in this tab

Settings that are relevant for all targets except Qlik Cloud:

- Apply batched changes in intervals:

- More than: The minimum amount of time to wait between each application of batch changes. The default value is 1.

  Increasing the More than value decreases the frequency with which changes are applied to the target while increasing the size of the batches. This can improve performance when applying changes to target databases that are optimized for processing large batches.
- Less than: The maximum amount of time to wait between each application of batch changes (before declaring a timeout). In other words, the maximum acceptable latency. The default value is 30. This value determines the maximum amount of time to wait before applying the changes, after the Larger than value has been reached.

- Force apply a batch when processing memory exceeds (MB): The maximum amount of memory to use for pre-processing. The default value is 500 MB.

  For maximum batch size, set this value to the highest amount of memory you can allocate to the data task. This can improve performance when applying changes to target databases that are optimized for processing large batches.
- Apply batched changes to multiple tables concurrently: Selecting this option should improve performance when applying changes from multiple source tables.

  - Maximum number of tables: The maximum number of tables to apply batched changes to concurrently. The default is five.

  Information noteThis option is not supported when using Google BigQuery as your data platform.
- Limit the number of changes applied per change processing statement to: Select this option to limit the number of changes applied in a single change processing statement. The default value is 10,000.

  Information noteThis option is only supported when using Google BigQuery as your data platform.

Settings that are relevant for Qlik Cloud only:

- Minimum number of changes per transaction: The minimum number of changes to include in each transaction. The default value is 1000.

  Information note

  The changes will be applied to the target either when the number of changes is equal to or greater than the Minimum number of changes per transaction value OR when the Maximum time to batch transactions before applying (seconds) value described below is reached - whichever occurs first. Because the frequency of changes applied to the target is controlled by these two parameters, changes to the source records may not immediately be reflected in the target records.
- Maximum time to batch transactions before applying (seconds): The maximum time to collect transactions in batches before declaring a timeout. The default value is 1.

### Interval

- Read changes every (Minutes)

  Set the interval between reading changes from the source in minutes. The valid range is 1 to 1440.

  Information note

  This option is only available for tasks using:

  - A SaaS application [Lite connector](connecting-web-applications.htm#Lite).
  - Data Movement gateway
  - The Change data capture (CDC) update method

#### Miscellaneous tuning

- Statements cache size (number of statements): The maximum number of prepared statements to store on the server for later execution (when applying changes to the target). The default is 50. The maximum is 200.
- DELETE and INSERT when updating a primary key column: This option requires full supplemental logging to be turned on in the source database.

## Automatic schema evolution

Select how to handle the following types of DDL changes in the schema. When you have changed schema evolution settings, you must prepare the task again. The table below describes which actions are available for the supported DDL changes.

Information noteThese settings are not available for tasks using a SaaS application connector [Lite connector](connecting-web-applications.htm#Lite). When using a regular SaaS application connector only Change column data type is supported.

| DDL change | Apply to target | Ignore | Suspend table | Stop task |
| --- | --- | --- | --- | --- |
| Add column | Yes | Yes | Yes | Yes |
| Rename column | No | No | Yes | Yes |
| Rename table | No | No | Yes | Yes |
| Change column data type | No | Yes | Yes | Yes |
| Create table If you used a Selection rule to add datasets that match a pattern, new tables that meet the pattern will be detected and added. | Yes | Yes | No | No |

## Character substitution

You can substitute or delete source characters in the target database and/or you can substitute or delete source characters that are not supported by a selected character set.

Information note

- All characters must be specified as Unicode code points.
- Character substitution will also be performed on the Control tables.

- Invalid values will be indicated by a red triangle in the top right of the table cell. Hovering your mouse cursor over the triangle will show the error message.

- Any table-level or global transformations defined for the task will be performed after the character substitution has been completed.
- Substitutions actions defined in the Substitute or Delete Source Characters table are performed before the substitution action defined in the Substitute or Delete Source Characters Unsupported by the Selected Character Set table.
- Character substitution does not support LOB data types.

### Substituting or deleting source characters

Use the Substitute or delete source characters table to define replacements for specific source characters. This may be useful, for example, when the Unicode representation of a character is different on the source and target platforms. For example, on Linux, the minus character in the Shift\_JIS character set is represented as U+2212, but on Windows it is represented as U+FF0D.

Substitution actions

| To | Do This |
| --- | --- |
| Define substitution actions. | 1. Click the Add character button above the table. 2. Specify a source character and a target character in the Source character and Substitute character fields respectively.  For example to replace the letter "a" with the letter "e", specify 0061 and 0065 respectively.  Information note To delete the specified source character, enter 0 in the Substitute character column. 3. Repeat steps 1-2 to replace or delete additional characters. |
| Edit the specified source or target character | Click  at the end of the row and selected Edit. |
| Delete entries from the table | Click  at the end of the row and selected Delete. |

### Substituting or deleting source characters unsupported by the selected character set

Use the Unsupported source characters by character set table to define a single replacement character for all characters not supported by the selected character set.

Unsupported character substitution actions

| To | Do This |
| --- | --- |
| Define or edit a substitution action. | 1. Select a character set from the Character set drop-down list in the table.  Any characters not supported by the selected character set will be replaced on the target by the character specified in step 2 below. 2. In the Substitute character column, click anywhere in the column and specify the replacement character. For example, to replace all unsupported characters with the letter "a", enter 0061.  Information note To delete all unsupported characters, enter 0. |
| Disable the substitution action. | Select the blank entry from the Character Set drop-down list. |

## More options

These options are not exposed in the UI as they are only relevant to specific versions or environments. Consequently, do not set these options unless explicitly instructed to do so by Qlik Support or product documentation.

To set an option, simply copy the option into the Add feature name field and click Add. Then set the value or enable the option according to the instructions you received.

## Loading dataset segments in parallel

Information noteThis setting is not available for SaaS application sources and only available for a specific subset of source and target databases.

During full load, you can accelerate the loading of large datasets by splitting the dataset into segments, which will be loaded in parallel. Tables can be split by data ranges, all partitions, all subpartitions, or specific partitions.

For more information, see [*Landing dataset segments in parallel*](Table-settings-landing.htm).

## Scheduling tasks

In some cases, you might need to schedule your task to propagate changes from the data source to the target platform.

For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
