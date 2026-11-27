---
title: "Settings for cloud storage targets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/landing-datalakes-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project", "Landing data in a data lake with a Standard, Premium, or Enterprise subscription"]
---

# Settings for cloud storage targets

You can change the default data lake landing settings according to your needs.

## General

### Update method

You can land data in two different modes. It is not possible to change mode once the data lake landing task is prepared.

- Change data capture (CDC) using Change Tables: Data lake landing tasks starts with a full load (during which all of the selected tables are loaded to the target). The target data is then kept up-to-date using CDC (Change Data Capture) technology.

  Information noteCDC (Change Data Capture) of DDL operations is not supported.

  When working with Data Movement gateway, except when using a SaaS application source, changes are captured from the source in near real-time. When working without Data Movement gateway or with SaaS application sources, changes are captured according to the scheduler settings. For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
- Reload: Performs a full load of the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually or scheduled to occur periodically as needed.

  Information noteThis setting is not available when using a SaaS application connector.

### Folder to use

Select one of the following, according to which bucket folder you want the files to be written to:

- Default folder

  The default folder format is <your-project-name>/<your-task-name>
- Root folder

  The files will be written to the root bucket folder.
- Folder

  Specify a folder name. The folder will be created during the data task if it does not already exist.

  Information note The folder name cannot include special characters (for example, @, #, !, and so on).

## Data uploading

### File attributes

#### Format

You can choose to create the target files in CSV or JSON, or Parquet format.

Information noteWhen using Parquet file format, LOB columns larger than 1 MB are not supported

In a JSON file, each record is represented by a single line, as in the following example:

{ "book\_id": 123, "title": "Alice in Wonderland", "price": 6.99, "is\_hardcover": false }

{ "book\_id": 456, "title": "Winnie the Pooh", "price": 6.49, "is\_hardcover": true }

{ "book\_id": 789, "title": "The Cat in the Hat", "price": 7.23, "is\_hardcover": true }

See also: [*Content-type and content-encoding properties*](content-encoding-datalakes.htm)

Information noteChanging the format (for example, from CSV to JSON or from JSON to CSV) while the task is in a stopped state and then resuming the task, is not supported.

Information note

- If you choose JSON or Parquet format , the following fields will be hidden as they are only relevant to CSV format: Field delimiter, Record delimiter, Null value, Quote character, Quote escape character, and Add metadata header.
- The following fields are relevant for Parquet format only: Parquet version, Parquet timestamp unit, and Parquet maximum LOB size (KB).

For information about data type mappings when using Parquet format and limitations, see [*Mapping from Qlik Cloud data types to Parquet*](landing-datalakes-datatypes.htm#Mapping)

#### Field delimiter

The delimiter that will be used to separate fields (columns) in the target files. The default is a comma.

Example using a comma as a delimiter:

"mike","male"

Delimiters can be standard characters or a hexadecimal (hex) value. Note that the "`0x`" prefix must be used to denote a hexadecimal delimiter (e.g. `0x01 = SOH`). In the Field delimiter, Record delimiter and Null value fields, the delimiter can consist of concatenated hex values (e.g. `0x0102` = `SOHSTX`), whereas in the Quote character and Quote escape character fields, it can only be a single hex value.

The hexadecimal number `0x00` is not supported (i.e. only `0x01`-`0xFF` are supported).

#### Null value

The string that will be used to indicate a null value in the target files.

Example (where \n is the record delimiter and @ is the null value):

"mike","male",295678\n

"sara","female",@\n

#### Record delimiter

The delimiter that will be used to separate records (rows) in the target files. The default is a newline (`\n`).

Example:

"mike","male"\n

"sara","female"\n

#### Quote character

The character that will be used at the beginning and end of a text column. The default is the double-quote character ("). When a column that contains column delimiters is enclosed in double-quotes, the column delimiter characters are interpreted as actual data, and not as column delimiters.

Example (where a @ is the quote character):

@mike@,@male@

#### Quote escape character

The character used to escape a quote character in the actual data. The default is the double-quote character (").

Example (where " is the quote character and \ is the escape character):

1955,"old, \"rare\", Chevrolet","$1000"

#### Parquet version

Select which version to use according to which version the target platform supports. Note that Parquet version 1.0 supports the MICRO
 timestamp unit
only, while Parquet version 2.6 supports both MICRO
and NANO timestamp units.

#### Parquet timestamp unit

When Parquet version is set to 2.6, choose MICRO
or NANO. When Parquet version is set to 1.0, only MICRO
is supported.

#### Parquet maximum LOB size (KB)

The default maximum LOB size is 64 KB and the maximum value you can enter in this field is 10,000 KB.
Handling LOB columns requires greater resources, which in turn impacts performance. Only increase this value is you are replicating LOB data larger than 64 KB and you require all the LOB data to be replicated to the target.

#### Maximum file size

The maximum size a file can reach before it is closed (and optionally compressed).

The maximum size a file can reach before it is closed. Smaller files might be uploaded faster (depending on the network) and improve performance when used in conjunction with the parallel execution option. However, it is generally considered bad practice to clutter the database with small files.

#### Compress files using

Choose one of the compression options to compress the target files or NONE (the default) to leave them uncompressed. Note that the available compressions options are determined by the selected file format.

#### Add metadata header

You can optionally add a header row to the data files. The header row can contain the source column names and/or the intermediate (i.e. Qlik Talend Data Integration) data types.

Example of a target file with a header row when both With column names and With data types are selected:

Position:DECIMAL(38,0),Color:VARCHAR(10)

1,"BLUE"

2,"BROWN"

3,"RED"

...

### Change processing

This section describes conditional settings in Change Processing.

#### Apply/store changes when

- File size reaches: Specify the maximum size of Change Data to accumulate before uploading the file to the target.
- Elapsed time reaches: Elapsed time reaches x.

### Metadata files

When the Create metadata files in the target folder option is selected, for each data file, a matching metadata file with a .dfm extension will be created under the specified target folder. The metadata files provide additional information about the task/data such as the source connector type, the source table name, the number of records in the data file, and so on.

For a full description of the metadata file as well as possible uses, see [*Metadata file description*](s3-metadata.htm)

## Metadata

### LOB columns

Information noteThese settings are not available for tasks using a SaaS application connector.

Include LOB columns and limit column size to (KB)

You can choose to include LOB columns in the task, and set the maximum LOB size. LOBs that are larger than the maximum size will be truncated.

### JSON column mapping

Map compatible source JSON columns to JSON columns on the target

Information note

- If you are using Data Movement gateway to access your data source, version 2024.11.70 or later is required.

When this option is selected, JSON columns on the source will automatically be mapped to JSON columns on the target.

The state and visibility of this option is determined by the following factors:

- New tasks: This option will be enabled by default if both the source and the target support the JSON data type.
- Existing tasks: This option will be disabled by default, even if both the source and the target support the JSON data type. This is in order to preserve backward compatibility with downstream processes - such as transformations - that expect the target data to be in STRING format (which is the legacy behavior). You can either leave the option disabled or you can edit the downstream processes to be compatible with JSON format, and then enable this option.
- New and existing tasks: If only the source supports the JSON data type, this option will not be visible. If JSON support is added to the target at a later stage, the option will become visible but remain disabled. This is in order to preserve backward compatibility with downstream processes - such as transformations - that expect the target data to be in STRING format (which is the legacy behavior).

### Control tables

Select which of the following Control tables you want to be created on the target platform:

- Replication Status: Provides details about the current landing task including task status, amount of memory consumed by the task, number of changes not yet applied to the data platform and the position in the data source from which the data is currently being read.
- Suspended Tables: Provides a list of suspended tables, and the reason they were suspended.
- Landing history: Provides information about the task history including the number and volume of records processed during a landing task, latency at the end of a CDC task, and more.
- Change data partitions: Provides records of partitions created on the target database due to [*Change data partitioning*](#Change). You can use this information to identify partitioned data that needs to be further processed.

For a detailed description of each of the Control Tables, see [*Control tables*](control_tables.htm)

## Full load

Information noteThese settings are not available for tasks using a SaaS application connector.

### Performance tuning

- Maximum number of tables to load in parallel: Enter the maximum number of tables to load into the target at one time. The default value is 5.
- Transaction consistency timeout (seconds): Enter the number of seconds to wait for open transactions to close, before beginning the Full Load operation. The default value is 600 (10 minutes). The full load will start after the timeout value is reached even if there are transactions that are still open.

  Information noteTo replicate transactions that were open when Full Load started but were only committed after the timeout value was reached, you need to reload the target tables.
- Commit rate during full load: The maximum number of events that can be transferred together. The default value is 10000.

### After full load completes

Create primary key or unique: Select this option if you want to delay creation of the primary key or unique index on the data platform until after full load completes.

### For initial load

Information note
If you are using Data Movement gateway to access your data source, these settings require version 2022.11.74 or later.

|  |  |
| --- | --- |
| Use cached data | This option lets you use cached data that was read when generating metadata with Full data scan selected.  This creates less overhead regarding API use and quotas, as the data is already read from the source. Any changes since the initial data scan can be picked up by Change data capture (CDC). |
| Load data from source | This option performs a new load from the data source. This option is useful if:   - The metadata scan was not performed recently. - The source dataset is small and frequently changing, and you do not want to maintain a full history of changes. |

## Store changes

When you select the Change Data Capture (CDC) update method, updates to the source data will be stored in Change Tables on the target platform. Change Tables capture all insert, update, and delete operations from the source, allowing downstream applications to process changes incrementally.

This section describes how to configure Change Table options: DDL handling, update image storage, and table creation behavior.

Information note

Store changes processing is only available when the update method is set to Change Data Capture (CDC).

Any changes to these settings will only take effect the next time a full load is run. If you modify these settings while the task is stopped, you must reload the target tables to apply the changes.

For in-depth information about Change Tables, see [*Using Change Tables*](use_change_tables.htm).

### Basic settings

#### DDL options

Information noteThese settings are not available when replicating from SaaS application sources.

DDL (Data Definition Language) options determine how schema changes from the source are handled in the Change Tables.

- Apply to change table: When you select this option, the system automatically applies DDL changes from the source tables (such as adding or removing columns) to the corresponding Change Tables. Use this option when your downstream applications need Change Tables to reflect all schema changes from the source.
- Ignore: The system ignores all DDL changes to the source. The Change Table structure remains unchanged. Use this option when DDL changes in the source should not affect the stored changes, or when your target system requires fixed table schemas.

### Advanced settings

#### On update

Information noteThis setting is not relevant for SaaS application sources as changes are applied as INSERT operations.

On UPDATE settings control what data is captured when a source record is updated.

Store before and after image: The system captures both the original data (before the update) and the modified data (after the update). This option requires more storage but provides complete audit information, allowing downstream systems to compare old and new values or perform complex change analysis. Use this when your applications need full change context.

When this option is disabled, the system captures only the modified data (after the update), not the original values. This option reduces storage requirements on the target. Use this when you only need the current state of changed records and do not require historical before-values.

#### Change table creation

Overriding the default change table suffix and header column prefix

- Suffix: Specify a string to use as the suffix for all Change Tables. The default value is \_\_ct. The Change Table names are the name of the target table with the suffix appended. So for example, using the default value, the name of the Change Table will be HR\_\_ct.
- Header column prefix: Specify a string to use as the prefix for all of the Change Table header columns. The default value is header\_\_. For example, when using the default value, the header column stream\_position will be called header\_\_stream\_position.

Determining how existing Change Tables are handled when full load starts

When a full load starts, these settings determine how existing Change Tables on the target are handled. Select the option that best fits your data recovery and storage requirements:

- DROP and CREATE: The system removes the existing Change Table entirely and creates a new empty one. All previously stored changes are deleted. Use this when you want a fresh start with each full load cycle.
- Delete old changes and store new changes in existing Change Table: The system removes all data from the existing Change Table without affecting its structure or metadata. New changes are stored in the same table. Use this when you want to keep the table structure but clear previous changes.
- Keep old changes and store new changes in existing Change Table: The system preserves all existing data and metadata in the Change Table. New changes are added to the existing data. Use this when you need to accumulate all changes across multiple full load cycles.

#### Change data partitioning

Information noteThis option is only available when the update method is Change data capture (CDC).

In a standard landing task (without Change Data Partitioning), changes are landed to the target in no particular order. Change Data Partitioning enables processing of Change Data from many tables in a consistent fashion. You can define the duration of partitions as well as the partitioning base time, thereby ensuring overall consistency of the partitioned data (i.e. no partial transactions, no order headers without order rows, and so on.)

Information about the partitions is recorded in the [attrep\_cdc\_partitions](CDC_Partition.htm) Control Table in the target database. This information can be used to identify partitioned data that needs to be further processed.

Understanding how partitioning works according to source type

- From database sources:

  In a standard landing task (without Change Data Partitioning), changes are landed to the target in no particular order. Change Data Partitioning enables processing of Change Data from many tables in a consistent fashion. You can define the duration of partitions as well as the partitioning base time, thereby ensuring overall consistency of the partitioned data (i.e. no partial transactions, no order headers without order rows, and so on.)

  - Scheduled CDC: Partitions are created when the scheduled task instance runs. So, for example, if a task is scheduled to run at midnight every day, and Partition every is set to 4 hours, then the number of partitions created will represent the time the commits occurred during the last 24 hours. If commits occurred 01:00-03:00 and 16:15-18:00 and the Partitioning base time is set to 0:00, then two partitions will be created: 0:00-04:00 and 16:00-20:00.
  - Continuous CDC: If Partition every is set to 4 hours, Replicate creates a partition every 4 hours containing all commits that occurred during that period. If there were no commits during 4 hours, then no partition will be created for that period.
- From SaaS application sources:

  Tasks that extract data from SaaS application sources are always scheduled. Partitions are based on data extraction time, as the notion of commits does not exist in SaaS application sources. Data extraction begins when the scheduled task instance runs. So, for example, if a task is scheduled to run at midnight every day, and Partition every is set to 4 hours, then the number of partitions created will represent the data extraction duration. If data extraction takes less than two hours, a single partition will be created. But if the extraction takes six hours (for example), two partitions will be created.

Partitioning options

- Partition every - Specify the length (in hours and minutes) of each partition.

  Information note

  It is recommended to specify a partition length in excess of one hour. Although specifying a partition length less than one hour may improve latency, creating many partitions on the target may also impact (target) performance (especially in systems with large volumes of changes).

  If you resume a task from BEFORE the time that the last partition was created, the data lake landing task will write to a partition that has already been closed.
- Partition base time - Partitions are created during a 24 hour time period, which is calculated according to the specified “Partitioning base time” on the source database (in UTC time). For example, a partition interval of 8 hours with a “Partitioning base time” time of 02:00 will create the following partitions: 02:00-10:00, 10:00-18:00, 18:00-02:00 - but not necessarily in that order. For instance, if a task started at 01:00, then the timeframe of the first partition will be 18:00-02:00. Additionally, if a task started in the middle of a partition (e.g. at 04:00), its Change Data will be inserted into the 02:00-10:00 partition (even though no changes were captured before 04:00).

#### Table header columns

Warning note

You cannot add or remove columns while a task is running. To modify your column selection, stop the task, update your preferences, and then reload the target tables.

The Change Table includes system metadata columns with a configurable prefix. By default, these columns are prefixed with `header__` (for example, `header__stream_position`, `header__operation`). These columns provide information about each change record, such as the operation type (INSERT, UPDATE, DELETE) and the order in which changes occurred.

You can exclude specific header columns from the Change Table if you do not need that metadata. This reduces storage requirements on the target platform.

Information note

When [*Change data partitioning*](#Change) is enabled, the system automatically adds an extra system column named `partition_name` to the Change Tables and automatically selects it in the UI. As this column is required for partition tracking, it cannot be excluded.

## Error handling

### Data errors

Information note

Data error handling is supported with the Change Data Capture (CDC) update method only.

#### Data truncation errors

For data truncation errors: Select what you want to happen when a truncation occurs in one or more specific records. You can select one of the following from the list:

- Ignore: The task continues and the error is ignored.
- Suspend table: The task continues, but data from the table with the error record is moved into an error state and its data is not replicated
- Stop task: The task is stopped and manual intervention is required.

#### Other data errors

For other data errors: Select what you want to happen when an error occurs in one or more specific records. You can select one of the following from the list:

- Ignore: The task continues and the error is ignored.
- Suspend table: The task continues, but data from the table with the error record is moved into an error state and its data is not replicated
- Stop task: The task is stopped and manual intervention is required.

#### Escalating data error handling

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

- Offload transactions in progress to disk if:

  Transaction data is usually kept in memory until it is fully committed to the source or target. However, transactions that are larger than the allocated memory or that are not committed within the specified time limit will be offloaded to disk.

  - Total memory size for all transactions exceeds (MB): The maximum size that all transactions can occupy in memory before being offloaded to disk. The default value is 1024.
  - Transaction duration exceeds (seconds): The maximum time that each transaction can stay in memory before being offloaded to disk. The duration is calculated from the time Qlik Talend Data Integration started capturing the transaction. The default value is 60.

#### Batch tuning

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

  - "Land data in data lake" tasks in a replication project, see [*Scheduling CDC for lake landing tasks*](#Scheduli2)

#### Miscellaneous tuning

- Statements cache size (number of statements): The maximum number of prepared statements to store on the server for later execution (when applying changes to the target). The default is 50. The maximum is 200.
- DELETE and INSERT when updating a primary key column: This option requires full supplemental logging to be turned on in the source database.

  Information noteThis setting is not available for tasks using a SaaS application connector, unless it is a [Lite connector](../Landing/connecting-web-applications.htm#Lite).

## Automatic schema evolution

Select how to handle the following types of DDL changes in the schema. When you have changed schema evolution settings, you must prepare the task again. The table below describes which actions are available for the supported DDL changes.

Information noteWhen using a SaaS application connector only Change column data type is supported.

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

## Loading dataset segments in parallel

Information noteThis setting is not available for SaaS application sources and only available for a specific subset of source and target databases.

During full load, you can accelerate the loading of large datasets by splitting the dataset into segments, which will be loaded in parallel. Tables can be split by data ranges, all partitions, all subpartitions, or specific partitions.

For more information, see [*Replicating dataset segments in parallel*](Table-settings-replication.htm).

## More options

These options are not exposed in the UI as they are only relevant to specific versions or environments. Consequently, do not set these options unless explicitly instructed to do so by Qlik Support or product documentation.

To set an option, simply copy the option into the Add feature name field and click Add. Then set the value or enable the option according to the instructions you received.

## Scheduling CDC for lake landing tasks

Information noteUsing the Scheduler requires the Can operate role or the Can edit role.

In the following use cases, you must define a scheduling interval to keep the target data up-to-date:

- Accessing a data source without Data Movement gateway
- Using a SaaS application connector that is not a [Lite connector](../Landing/connecting-web-applications.htm#Lite).
- When capturing changes from a SAP OData source using the As scheduled option.

The schedule determines how often the target datasets will be updated with changes to the source datasets. Whereas the schedule determines the update frequency, the dataset type determines the update method. If a dataset supports CDC, only the changes to that dataset will be retrieved and propagated to the corresponding target table. If a dataset does not support CDC, (for example, a View), changes will be propagated by reloading the entire dataset. With SaaS application connectors, a single task will be created with the ability to schedule CDC intervals and reload intervals during the onboarding, and later in the task's scheduling settings. When using other connectors types (for example, databases) with the CDC update method, if some of the selected datasets support CDC and some do not, two separate sub-tasks will be created: one for retrieving the changes to the datasets that support CDC, and the other for reloading the datasets that do not support CDC.

To change the scheduling:

1. Open your pipeline project and then do one of the following:

   - In tasks view, click ![Menu button consisting of 3 horizontal dots.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a data task and select Scheduling.
   - In pipeline view, click ![Menu button consisting of 3 vertical dots.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on a data task and select Scheduling.
   - Open the replication task and click the Scheduling toolbar button.
2. Change the scheduling settings as needed and then click OK.

Information noteIf a data task is still running when the next scheduled run is due to start, the next scheduled run(s) will be skipped until the task completes.

### Executing a missed run for a task based on Data Movement gateway

Sometimes a network issue might result in the connection to Data Movement gateway being lost. If the connection to Data Movement gateway is not restored before the next scheduled run, the data task will not be able to run as scheduled. In such cases, you can choose whether or not to execute a run immediately after the connection is restored.

The default settings for all Data Movement gateways are [defined in the Administration activity center](../../Gateways/dm-gateway-managing-console.htm#Executin). You can override these settings for individual tasks as described below.

To do this

1. Open your project and then do one of the following:

   - In tasks view, click ![Menu button consisting of 3 horizontal dots.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data task and select Scheduling.
   - In pipeline view, click ![Menu button consisting of 3 vertical dots.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the data task and select Scheduling.
   - Open the data task and click the Scheduling toolbar button.

   The Scheduling - <task> dialog opens.
2. Toggle on Use custom settings for this task.
3. At the bottom of the dialog, choose one of the following Run missed scheduled tasks options.

   - As soon as possible and then as scheduled if it's important to run a task before the next scheduled instance
   - As scheduled to run the task at the next scheduled instance
4. Save your settings.

See also: [*Executing a task run after a missed schedule*](../../Gateways/dm-gateway-managing-console.htm#Executin).
