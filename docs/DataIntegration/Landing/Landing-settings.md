---
title: "Landing settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/Landing-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Landing data from data sources"]
---

# Landing settings

You can configure settings for the landing data task.

- Open the landing task and click Settings in the toolbar.

The Settings: <Task-Name> dialog opens. The available settings are described below.

## General

- Database

  Database to use in the target.

  Information noteThis option is not available when landing data to Qlik Cloud (via Amazon S3).
- Task schema

  You can change the name of the landing data task schema. Default name is landing.

  Information noteThis option is not available when landing data to Qlik Cloud (via Amazon S3).
- Default capitalization of schema name

  You can set the default capitalization for all schema names. If your database is configured to force capitalization, this option will not have effect.
- Prefix for all tables and views

  You can set a prefix for all tables and views created with this task.

  Information noteThis option is not available when landing data to Qlik Cloud (via Amazon S3).

  Information noteYou must use a unique prefix when you want to use a database schema in several data tasks.

  - Update method

    The landing task always starts with a Full Load. After the Full Load completes, you can keep the landed data up-to-date using one of the following methods:

    Information noteIt is not possible to change the update method once the landing data task prepare operation has completed.

  Information noteWhen using a SaaS application source, only the Change data capture (CDC) update method is supported.

  - - Change data capture (CDC)

      The landed data is kept up-to-date using CDC (Change Data Capture) technology. CDC may not be supported by all data sources. CDC does not capture DDL operations, such as renaming columns, or changes in metadata.

      Information note

      When Change data capture (CDC) is the update method, and your data source:

      - Is not a SaaS application
      - Contains datasets that support CDC and datasets that support Full load only (such as views)

      Two data pipelines will be created. One pipeline will be created for tables that support CDC, and another pipeline will be created for datasets that support Reload and compare only.
    - Reload and compare

      All of the landed data is reloaded from the source. This is useful if your source does not support CDC, but can be used with any supported data source.

      You can schedule the reloads periodically.
- Loading method

  When replicating to a Snowflake target, you can choose one of the following loading methods:

  - Bulk loading (the default)

    If you select Bulk Loading, you will be able to tune the loading parameters in the Data uploading tab.
  - Snowpipe Streaming

    Information note

    Snowpipe Streaming will only be available for selection if the following conditions are met:

    - The Change data capture (CDC) update method is enabled.
    - The Authentication Mechanism in the Snowflake connector is set to Key Pair.
    - If you are using Data Movement gateway, version 2024.11.45 or later is required.

    If you select Snowpipe Streaming, make sure you are familiar with the [limitations and considerations](../TargetConnections/snowflake-target.htm#Limitati2) when using this method. Additionally, if you select Snowpipe Streaming and then switch to the Reload and compare update method, the loading method will automatically switch back to Bulk loading.

  The main reasons to choose Snowpipe Streaming over Bulk loading are:

  - Less costly: As Snowpipe Streaming does not use the Snowflake warehouse, operating costs should be significantly cheaper, although this will depend on your specific use case.
  - Reduced latency: As the data is streamed directly to the target tables (as opposed to via staging), replication from the data source to the target should be faster.

  Tip noteWhen using Snowpipe Streaming, the initial full load might be significantly slower than Bulk loading. To optimize the loading performance, especially when loading large datasets, best practice is to use Snowpipe Streaming together with the [parallel load feature](Table-settings-landing.htm).

- Folder to use in staging area

  For data platforms that require a staging area (for example, Databricks and Azure Synapse Analytics), you can select which folder to use when landing data.

  - Default folder

    This creates a folder with the default name: <project name>/<data task name>.
  - Root folder

    Store data in the root folder of the storage.

    Information noteThis option is only available when landing data to Qlik Cloud (via Amazon S3).
  - Folder

    Specify a folder name to use.
- Change processing interval

  You can set the interval between processing changes from the source.

  Information noteThis option is only available when landing data to Qlik Cloud (via Amazon S3).
- Proxy server when using Data Movement gateway

  Information noteThis option is only available when accessing targets via Data Movement gateway.

  You can select to use a proxy server when the Data Movement gateway connects to the cloud data warehouse and the storage area.

  For more information about configuring the Data Movement gateway to use a proxy server, see [*Setting the Qlik Cloud tenant and a proxy server*](../../Gateways/dm-gateway-setting-up.htm#Setting).

  - Use proxy to connect to cloud data warehouse

    Information noteAvailable when using Snowflake, Google BigQuery, and Databricks.
  - Use proxy to connect to storage

    Information noteAvailable when using Azure Synapse Analytics, Amazon Redshift, and Databricks.

## Data uploading

Some of the settings in this tab are only relevant to specific target platforms.

### Relevant for all data platforms except Qlik Cloud and Snowflake

Maximum files size (MB)

The maximum size a file can reach before it is closed. Smaller files might be uploaded faster (depending on the network) and improve performance when used in conjunction with the parallel execution option. However, it is generally considered bad practice to clutter the database with small files.

### Relevant for Google BigQuery only

Use compression

When selected, the CSV files will be compressed (using gzip) before being uploaded to Google BigQuery.

Information note

Requires Data Movement gateway 2023.5.16 or later.

### Relevant for Snowflake only

In the General tab, you can choose whether to load the data to Snowflake using Bulk Loading or Snowpipe Streaming. When Snowpipe Streaming is selected, the Data uploading tab will not be shown. When Bulk Loading is selected, the following settings will be available:

- Maximum file size (MB): Relevant for the initial Full Load and CDC. The maximum size a file can reach before it is loaded to the target. If you encounter performance issues, try adjusting this parameter.
- Number of file to load in a batch: Relevant for the initial Full Load only. The number of files to load in a single batch. If you encounter performance issues, try adjusting this parameter.

For a description of the Bulk Loading and Snowpipe Streaming loading methods, see [*General*](#General).

## Metadata

### LOB columns

Information noteThis setting is not available for tasks using a SaaS application connector, unless it is a [Lite connector](connecting-web-applications.htm#Lite).

Include LOB columns and limit column size to (KB):

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

### Transactional offload tuning

- Offload transactions in progress to disk if:

  Transaction data is usually kept in memory until it is fully committed to the source or target. However, transactions that are larger than the allocated memory or that are not committed within the specified time limit will be offloaded to disk.

  - Total memory size for all transactions exceeds (MB): The maximum size that all transactions can occupy in memory before being offloaded to disk. The default value is 1024.
  - Transaction duration exceeds (seconds): The maximum time that each transaction can stay in memory before being offloaded to disk. The duration is calculated from the time Qlik Talend Data Integration started capturing the transaction. The default value is 60.

### Batch tuning

Some of the settings in this tab might not be applicable to all targets or target loading methods.

#### Settings that are applicable to all targets except Qlik Cloud and Snowflake when the "Loading method" is "Snowpipe Streaming"

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

#### Settings that are only applicable to Qlik Cloud and Snowflake when the "Loading method" is "Snowpipe Streaming"

- Minimum number of changes per transaction: The minimum number of changes to include in each transaction. The default value is 1000.

  Information note

  The changes will be applied to the target either when the number of changes is equal to or greater than the Minimum number of changes per transaction value OR when the Maximum time to batch transactions before applying (seconds) value described below is reached - whichever occurs first. Because the frequency of changes applied to the target is controlled by these two parameters, changes to the source records may not immediately be reflected in the target records.
- Maximum time to batch transactions before applying (seconds): The maximum time to collect transactions in batches before declaring a timeout. The default value is 1.

### Interval

Information noteThese settings are only available for the SAP ODP connector.

- Read changes every (Minutes)

  The interval between reading changes from the source in minutes. The valid range is 1 to 1440.

  Information note

  This option is only for tasks using:

  - Data Movement gateway
  - The Change data capture (CDC) update method

Check for changes

- According to the delta extraction interval: When this option is selected, the data task checks for changes according to the Delta extraction interval.

  Information noteThe interval will start after each "round". A round can be defined as the time it takes for the data task to read the changes from the source tables, and send them to the target (as a single transaction). The length of a round varies according to the number of tables and changes. So if you specify an interval of 10 minutes and a round takes 4 minutes, then the actual time between checking for changes will be 14 minutes.

  - Delta extraction interval: The frequency with which deltas will be extracted from your system. The default is every 60 seconds.
- As scheduled: When this option is selected, the data task will extract the delta once and then stop. It will then continue to run as scheduled.

  Information noteThis option is only relevant if the interval between the CDC cycles is 24 hours or more.

  For information on scheduling:

  - Landing tasks in a data pipeline project, see [*Scheduling tasks*](#Scheduli2)

### Miscellaneous tuning

- Statements cache size (number of statements): The maximum number of prepared statements to store on the server for later execution (when applying changes to the target). The default is 50. The maximum is 200.
- DELETE and INSERT when updating a primary key column: This option requires full supplemental logging to be turned on in the source database.

  Information noteThis setting is not available for tasks using a SaaS application connector, unless it is a [Lite connector](connecting-web-applications.htm#Lite).

## Automatic schema evolution

Information noteWhen using a SaaS application connector only Change column data type is supported.

Select how to handle the following types of DDL changes in the schema. When you have changed schema evolution settings, you must prepare the task again. The table below describes which actions are available for the supported DDL changes.

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
