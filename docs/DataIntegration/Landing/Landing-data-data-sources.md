---
title: "Landing data from data sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/Landing-data-data-sources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Landing data from data sources

The first step of transferring data when onboarding is landing the data. This involves transferring the data from the data source to a landing area.

You can land data from a number of data sources through source connections.

The landing area is defined when you create the project.

- Qlik Cloud (via Amazon S3)

  When you land data to Qlik Cloud (via Amazon S3), you can use it to generate QVD tables ready for analytics in Qlik Cloud.
- Cloud data warehouse

  When you land data to a cloud data warehouse, such as Snowflake or Azure Synapse Analytics, you can store tables in the same cloud data warehouse.
- Qlik Open Lakehouse

  When you land data to a Qlik Open Lakehouse, your data is stored in Iceberg open table format, and can be mirrored to your cloud data warehouse.

You can also land data to a lakehouse, where the data is landed to cloud file storage managed by Snowflake. For more information, see [*Landing data to a lakehouse*](Lake-landing.htm).

Information noteData tasks operate in the context of the owner of the project they belong to. For more information about required roles and permissions, see [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).

## Create and configure a landing data task

This describes how to create a landing data task. The quickest way to create a data pipeline is to onboard data which creates a landing data task and a storage data task, ready to prepare and run. For more information, see [*Onboarding data to a data warehouse*](../Onboarding/Onboarding-data.htm).

1. In your project, click Create and select Land data.
2. In the Land data dialog, enter a name and a description of the data task.

   Select Open to open the landing data task when it is created.

   Click Create.
3. Click Select source data.
4. Select a connection to the source data and click Next.

   You can use the filters in the left panel, to filter the list of connections on source type, space, and owner.

   If you don't have a connection to the source data yet, you need to create one first, by clicking Add connection.

   For more information about setting up a connection to the supported sources, see [*Setting up connections to data sources*](connecting-data-2.htm).

   Information noteWhen you have selected tables in the next step, it is not possible to change the source connection from an on-premises data source to a cloud data source, or vise versa. You can only change the connection to another data source of the same type.
5. Select datasets to include in the data task. The selection dialog is different depending on which type of source you have connected to.

   When you are done selecting tables, click Save.

   Datasets is displayed.
6. You can change settings for the landing. This is not required.

   - Click Settings.

   For more information about settings, see [*Landing settings*](Landing-settings.htm#Landing).
7. You can now preview the structure and metadata of the selected data asset tables. This includes all explicitly listed tables, and tables that match the selection rules.

   If you want to add more tables from the data source, click Select source data.
8. You can perform basic transformations on the datasets, such as filtering data, or adding columns. This is not required.

   For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
9. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation finds errors, fix the errors before proceeding.

   For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
10. When you are ready, click Prepare to catalog the data task and prepare it for execution.

    You can follow the progress under Preparation progress in the lower part of the screen.
11. When the data task is prepared, and you are ready to start onboarding data, click Run.

The data onboarding should now start, and you can see the progress in Monitor. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori).

### Selecting data from a database

You can select specific tables or views, or use selection rules to include or exclude groups of tables.

Information noteIf the selection includes views, CDC is not supported.

Use % as a wildcard to define a selection criteria for schemas and tables.

- %.% defines all tables in all schemas.
- Public.% defines all tables in the schema Public.

Selection criteria gives you a preview based on your selections.

You can now either:

- Create a rule to include or exclude a group of tables based on the selection criteria.

  Click Add rule from selection criteria to create a rule, and select either Include or Exclude.

  You can see the rule under Selection rules.
- Select one or more datasets, and click Add selected datasets.

  You can see the added datasets under Explicitly selected datasets.

Selection rules only apply to the current set of tables and views, not to tables and views that are added in the future.

## Running a landing task with Change data capture (CDC)

You can run the landing task when it is prepared. This starts the replication which transfers data from the on-premises data source to the landing area.

- Click Run to start landing data.

The replication should now start, and the data task will have status Running. First, the full data source is copied, then changes are tracked. This means that changes are continuously tracked and transferred when discovered. This keeps the landing data in the landing area up to date.

In Qlik Talend Data Integration home you can view status, date and time of when the landing data is updated, and the number of tables in error. You can also open the data task and select the Tables tab to view basic metadata information for the tables.

You can monitor progress in detail by opening the Monitor tab. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori).

When all tables are loaded and the first set of changes are processed, Data is updated to on the data task card indicates that source changes up to that time are available in the data task.

### Reloading tables

You can reload data from the source.

#### Reloading single tables

You can reload specific tables manually without interfering with change data capture. This is useful when there are CDC issues with one or more tables.

1. Open the landing data task and select the Monitor tab.
2. Select the tables that you want to reload.
3. Click Reload tables.

Information noteThis option will become available after that landing task has run at least once.
If clicked while the landing task is not running, the tables will be reloaded the next time the task runs.

If you cannot resolve the issues by reloading tables, or if they affect the entire task, you can reload all tables to the target instead. This will restart change data capture.

#### Reloading all tables to the target

You can reload all tables to the target if you experience CDC issues that cannot be resolved by reloading specific tables. Examples of issues are missing events, issues caused by source database reorganization, or failure when reading source database events.

Information noteThis operation is only available for tasks with the update method Change data capture (CDC), and that have run at least once.

1. Stop the data task and all tasks that consume it.
2. Open the data task and select the Monitor tab.
3. Click ..., and then Reload target.

This will reload all tables to the target using Drop-Create, and will restart all change data capture from now.

- Storage tasks that consume the landing data task will be reloaded via compare and apply at their next run to get in sync. Existing history will be kept. Type 2 history will be updated to reflect changes after the reload and compare process is executed.

  The timestamp for the from date in the type 2 history will reflect the reload date, and not necessarily the date the change occurred in the source.
- Storage live views will not be reliable during the reload target operation, and until the storage is in sync. Storage will be fully synced when:

  - All tables are reloaded using compare and apply,
  - One cycle of changes is performed for each table.

Information noteMetadata changes are not supported. If there are metadata changes in the source they are propagated to landing when reloading data but they will not be handled properly. This may cause the consuming storage to fail.

## Running a landing data task with Reload and compare

You can copy data using the landing data task when it is prepared.

- Click Run to start the full load.

Data will now start being copied, and the data task will have status Running. When the full data source is copied, the status is Completed.

In Qlik Talend Data Integration home you can view status, date and time of when the landing data is updated, and the number of tables in error. You can also open the data task and select the Tables tab to view basic meta data information for the tables.

You can monitor progress in detail by opening the Monitor tab. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori).

When all tables are loaded, Data is updated to on the data task card indicates that source changes up to that time are available in the data asset. However, some tables of the data task can be updated to a later time, depending on when they started loading. This means that data consistency is not guaranteed. For example, if the load started at 08:00 and took 4 hours, Data is updated to will show 08:00 when the load is completed. However, a table that started reloading at 11.30 will include source changes that occurred between 08:00 and 11:30.

Data is updated to reflects only tables that loaded successfully. It does not indicate anything regarding tables that their reloads have failed. In cloud targets, the field will be empty if a reload completed with all tables in error.

### Reloading data when using Reload and compare

When you use Reload and compare as update method, you need to reload data to keep it up-to-date with the data source.

- Click Reload to perform a manual reload of all tables.
- Set up a scheduled reload.

  For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).

#### Reloading single tables

You can reload specific tables manually. This is useful when there are issues with one or more tables.

1. Open the landing data task and select the Monitor tab.
2. Select the tables that you want to reload.
3. Click Reload tables.

Information note

- This option will be available after the landing task has run at least once, and only when the task is not running.
- Metadata changes are not supported. If there are metadata changes in the source they are propagated to landing when reloading data but they will not be handled properly. This may cause the consuming storage to fail.

### Scheduling a Reload and compare landing data task

You can schedule periodical reloads for the landing data task if you have the Can operate role or the Can edit role in the space of the data task . Data task status must be at least Prepared for the schedule to be active.

- Click ... on a data task and select Scheduling.

  You can set a time based schedule.

  For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).

  For information about minimum scheduling intervals according to data source type and subscription tier, see [*Minimum allowed scheduling intervals*](../../Admin/subscription-options-QTC.htm#Minimum).

Information noteIf a data task is still reloading when a scheduled reload is about to start, the scheduled reload is skipped until the next scheduled reload event.

## Setting load priority for datasets

You can control the load order of datasets in your data task by assigning a load priority to each dataset. This can be useful, for example, if you want to load smaller datasets before large datasets.

1. Click Load priority.
2. Select a load priority for each dataset.

   The default load priority is Normal. Datasets will be loaded in the following order of priority:

   - Highest
   - Higher
   - High
   - Normal
   - Low
   - Lower
   - Lowest

   Datasets with the same priority are loaded in no particular order.
3. Click OK.

Information noteDatasets from SaaS application sources may contain dependencies in load order. Consider this when setting the load priority.

## Operations on the landing data task

You can perform the following operations on a landing data task from the task menu.

- Open

  This opens the landing data task. You can view the table structure and details about the data task.
- Edit

  You can edit the name and the description of the task.
- Delete

  You can delete the data task.

  The following objects are not deleted:

  - The data in the landing area
  - Schemas in the target platform
- Run

  You can run the data task to start copying data.

  [*Running a landing task with Change data capture (CDC)*](#Running)

  [*Running a landing data task with Reload and compare*](#Running2)
- Stop

  You can stop operation of a data task that is running. The landing area is not updated with changed data.

  When you stop a full load data task with a reload schedule, only the current reload is stopped. If the data task status is Stopped and there is an active reload schedule, it will reload again at the next scheduled time. You must turn off the reload schedule in Schedule reload.
- Reload

  You can perform a manual reload of a data task in Reload and compare update mode.
- Prepare

  This prepares a task for execution. This includes:

  - Validating that the design is valid.
  - Creating or altering the physical tables and views to match the design.
  - Generating the SQL code for the data task.
  - Creating or altering the catalog entries for the task output datasets.

  You can follow the progress under Preparation progress in the lower part of the screen.

  Information noteBefore you prepare a task, stop all tasks that are directly downstream.
- Recreate tables

  This recreates the datasets from the source.

  Information noteIf there are problems with individual tables, it is recommended to first try reloading the tables instead of recreating them. Recreating tables may cause a loss of historical data. If there are breaking changes, you must also prepare downstream data tasks that consume the recreated data tasks to reload the data.
- Scheduling

  You can setup a scheduled reload for landing data tasks in Full load mode. You can set a time based schedule that can be customized.

  You can also turn on or off scheduled reloads.

  You must have the Can operate role on the space of the data task to schedule reloads.

  For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
- Store data

  You can create a storage data task that uses data from this landing data task.

## Schema evolution

Schema evolution allows you to easily detect structural changes to multiple data sources and then control how those changes will be applied to your task. Schema evolution can be used to detect DDL changes that were made to the source data schema. You can also apply some changes automatically.

Information noteSchema evolution is not available with a Qlik Talend Cloud Starter subscription. When working with SaaS application connectors, only data type changes are supported.

For each change type, you can select how to handle the changes in the Schema evolution section of the task settings. You can either apply the change, ignore the change, suspend the table, or stop task processing.

You can set which action to use to handle the DDL change for every change type. Some actions are not available for all change types.

- Apply to target

  Apply changes automatically.
- Ignore

  Ignore changes.
- Suspend table

  Suspend the table. The table will be displayed as in error in Monitor.
- Stop task

  Stop processing of the task. This is useful if you want to handle all schema changes manually. This will also stop scheduling, that is, scheduled runs will not be performed.

The following changes are supported:

- Add column
- Rename column
- Change column data type
- Create table that matches the selection pattern

  If you used a Selection rule to add datasets that match a pattern, new tables that meet the pattern will be detected and added.

For more information about task settings, see [*Automatic schema evolution*](Landing-settings.htm#Schema)

You can also get notifications about changes that are handled with schema evolution. For more information, see [*Setting notifications for changes in operation*](../Introduction/Notifications.htm).

### Limitations for schema evolution

The following limitations apply to schema evolution:

- Schema evolution is only supported when using CDC as update method.
- When you have changed schema evolution settings, you must prepare the task again.
- If you rename tables, schema evolution is not supported. In this case you must refresh metadata before preparing the task.
- If you are designing a task, you must refresh the browser to receive schema evolution changes. You can set notifications to be alerted on changes.
- In Landing tasks, dropping a column is not supported. Dropping a column and adding it will result in a table error.
- In Landing tasks, a drop table operation will not drop the table. Dropping a table and then adding a table will only truncate the old table, and a new table will not be added.
- Changing the length of a column is not possible for all targets depending on support in the target database.
- If a column name is changed, explicit transformations defined using that column will not take affect as they are based on column name.
- Limitations to Refresh metadata also apply for schema evolution.
- If a task contains design changes that have not yet been prepared and source schema evolution changes are detected when the task is run, the task will be stopped to avoid conflicts. Prepare the pending design changes and run the task again.

When capturing DDL changes, the following limitations apply:

- When a rapid sequence of operations occurs in the source database (for instance, DDL>DML>DDL), Qlik Talend Data Integration might parse the log in the wrong order, resulting in missing data or unpredictable behavior. To minimize the chances of this happening, best practice is to wait for the changes to be applied to the target before performing the next operation.

  As an example of this, during change capture, if a source table is renamed multiple times in quick succession (and the second operation renames it back to its original name), an error that the table already exists in the target database might be encountered.
- If you change the name of a table used in a task and then stop the task, Qlik Talend Data Integration will not capture any changes made to that table after the task is resumed.
- Renaming a source table while a task is stopped is not supported.
- Reallocation of a table's Primary Key columns is not supported (and will therefore not be written to the DDL History Control table).
- When a column's data type is changed and the (same) column is then renamed *while* the task is stopped, the DDL change will appear in the DDL History Control table as “Drop Column” and then “Add Column” when the task is resumed. Note that the same behavior can also occur as a result of prolonged latency.
- CREATE TABLE operations performed on the source while a task is stopped will be applied to the target when the task is resumed, but will not be recorded as a DDL in the DDL History Control table.
- Operations associated with metadata changes (such as ALTER TABLE, reorg, rebuilding a clustered index, and so on) may cause unpredictable behavior if they were performed either:

  - During Full Load

    -OR-
  - Between the Start processing changes from timestamp and the current time (i.e. the moment the user clicks OK in the Advanced Run Options dialog).

    Example:

    IF:

    The specified Start processing changes from time is 10:00 am.

    AND:

    A column named Age was added to the Employees table at 10:10 am.

    AND:

    The user clicks OK in the Advanced Run Options dialog at 10:15 am.

    THEN:

    Changes that occurred between 10:00 and 10:10 might result in CDC errors.

  Information note

  In any of the above cases, the affected table(s) must be reloaded in order for the data to be properly moved to the target.

- The DDL statement `ALTER TABLE ADD/MODIFY <column> <data_type> DEFAULT <>` does not replicate the default value to the target and the new/modified column is set to NULL. Note that this may happen even if the DDL that added/modified the column was executed in the past. If the new/modified column is nullable, the source endpoint updates all the table rows before logging the DDL itself. As a result, Qlik Talend Data Integration captures the changes but does not update the target. As the new/modified column is set to NULL, if the target table has no Primary Key/Unique Index, subsequent updates will generate a "zero rows affected" message.
- Modifications to TIMESTAMP and DATE precision columns will not be captured.

### Handling changes that are not automatically applied

This describes how to handle changes that cannot be applied to target, that is, the action is Ignore, Suspend, or Stop Task.

| DDL change | To implement the change | To preserve the current state |
| --- | --- | --- |
| Add column | Refresh metadata, prepare the task, and then run the task. | No action required |
| Create table | Refresh metadata, prepare the task, and then run the task. | No action required |
| Change column data type | Check limitations. if no limitation applies:  Refresh metadata, prepare the task, and then run the task. | Preserving the current state is not always supported. Possible workarounds:   - Change the column data type manually. This needs to be repeated in downstream tasks. - Create a new column and direct the old column to the new one, then create a view manually that combine the two columns. |
| Rename table | Check limitations. if no limitation applies:  Prepare the task, and then run the task. | Define an explicit rename rule to the old name. |
| Rename column | Check limitations. if no limitation applies:  Refresh metadata, prepare the task, and then run the task. | Refresh metadata, then define an explicit rename rule to the old name. |

## Removing columns

If you drop a column which is consumed by a storage data task with history enabled, you need to follow these steps to preserve history and avoid possible data loss.

1. Stop the landing data task.
2. Run the storage data task to ensure that all landing data is read.
3. Drop the column in the landing.
4. Run the landing data task.
5. In storage, add the column with a default expression (Null or default value), or drop the column.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Changing source connections or data gateway

If you change the source connection, or the source data gateway, you must recreate all tables.

## Maintenance of the landing area

Automatic cleanup of the landing area is not supported. This can affect performance.
We recommend that you perform manual cleanups of old full load data in the landing area.

- Qlik Cloud (via Amazon S3)

  If there are several folders of full load data, you can delete all but the most recent folder. You can also delete change data partitions that have been processed.
- Cloud data warehouse

  You can delete full load and change table records that have been processed.

## Recommendations

- If a primary key in a source table can be updated, enable DELETE and INSERT when updating a primary key column option in Change Processing Tuning.

## Limitations

- Replicating varchar data longer than 8000 bytes, or Nvarchar longer than 4000 bytes, is not supported.
- Changing nullability is not supported on columns that are moved, either changing it directly or using a transformation rule. However, new columns created in the task are nullable by default.
- Source columns of type CLOB and BLOB will be set as nullable by default, even if marked as non-nullable in the source. You can change it to be non-nullable, but then you need to add an expression to add a non-null value in case it arrives as null from the source. This can happen on deleted records.

Transformations are subject to the following limitations:

- Transformations are not supported for columns with right-to-left languages.
- Transformations cannot be performed on columns that contain special characters (e.g.
  #, \, /, -) in their name.
- The only supported transformation for LOB/CLOB data types is to drop the column on the target.
- Using a transformation to rename a column and then add a new column with the same name is not supported.
