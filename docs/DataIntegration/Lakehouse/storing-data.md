---
title: "Storing datasets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/storing-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "CDC data"]
---

# Storing datasets

In a Qlik Open Lakehouse project, the storage task writes landed data into Iceberg tables for efficient storage and querying. The storage data task consumes the data that was landed to the cloud landing area by a landing data task. You can use the tables in an analytics application, for example.

The following settings and behaviors apply to the storage task in a Qlik Open Lakehouse project that writes to Iceberg tables.

- The storage data task runs continuously and cannot be scheduled.
- Qlik automatically optimizes the data stored in Iceberg tables. For more information about the optimization process, see [*Qlik Open Lakehouse architecture*](lakehouse-pipeline-architecture.htm) .
- You can design a storage data task when the status of the landing data task is at least Ready to prepare.
- You can prepare a storage data task when the status of the landing data task is at least Ready to run.

The storage data task will use the same mode of operation (Full load or Full load & CDC) as the consumed landing data task. Configuration properties are different between the two modes of operation, as well as monitor and control options. In AWS, a cloud target landing data task with full load only creates views to the landing tables instead of physical tables. GCP projects do not generate storage views.

Information noteData tasks operate in the context of the owner of the project they belong to. For more information about required roles and permissions, see [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).

## Creating a storage data task

You can create a storage data task in three ways:

- Click ... on a landing data task and select Store data to create a storage data task based on this landing data asset.
- In a project, click Create and then Store data. In this case you will need to specify which landing data task to use.
- When you onboard data, a storage data task is created. It is connected to the landing data task, which is also created when onboarding data.

  For more information, see [*Onboarding data to Qlik Open Lakehouse*](Onboarding-data-open-lakehouse.htm).

When you have created the storage data task:

1. Open the storage data task by clicking ... and selecting Open.
   The storage data task is opened and you can preview the output datasets based on the tables from the landing data asset.
2. Make all required changes to the included datasets, such as transformations, filtering data, or adding columns.

   For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
3. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation finds errors, fix the errors before proceeding.

   For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
4. Click Prepare to prepare the data task and all required artifacts. This can take a little while.

   You can follow the progress under Preparation progress in the lower part of the screen.
5. When the status displays Ready to run, you can run the data task.

   Click Run.

   The data task will now start creating datasets to store the data.

## Keeping historical data

You can keep type 2 historical change data to easily recreate data as it looked at a specific point in time. This creates a full historical data store (HDS).

- Type 2 slowly changing dimensions are supported.
- When a changed record is merged, it creates a new record to store the changed data and leaves the old record intact.
- New HDS records are automatically time-stamped do you can create trend analysis and other time-oriented analytic data marts.

You can enable historical data by clicking:

- Replication with both current data and history of previous data in Settings when you onboard data.
- Keep historical change records and change record archive in the Settings dialog of a storage task.

## Scheduling a storage task

A storage task in a Qlik Open Lakehouse project runs continuously in one-minute mini batches and cannot be scheduled.

## Monitoring a storage task

You can monitor the status and progress of a storage task by clicking on Monitor.

For more information, see [*Monitoring a Qlik Open Lakehouse storage task*](../Introduction/Monitoring-qol-storage-tasks.htm).

## Troubleshooting a storage data task

When there are issues with one or more tables in a storage data task, you may need to reload or recreate the data. There are a few options available to perform this. Consider which option to use in the following order:

1. You can reload the dataset in landing. Reloading the dataset in landing will trigger the compare process in storage and correct data while retaining type 2 history. This option should also be considered when:

   - The full load was performed a long time ago, and there is a large number of changes.
   - If full load and change table records that have been processed have been deleted as part of maintenance of the landing area.

   [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm)
2. You can recreate tables. This recreates the datasets from the source.

   - Click ... and then click Recreate tables. When recreating a table, the downstream task will react as if a truncate and reload action occurred on the source datasets.

     Information noteIf there are problems with individual tables, it is recommended to first try reloading the tables instead of recreating them. Recreating tables may cause a loss of historical data. If there are breaking changes, you must also prepare downstream data tasks that consume the recreated data tasks to reload the data.

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
- Create table that matches the selection pattern

  If you used a Selection rule to add datasets that match a pattern, new tables that meet the pattern will be detected and added.

For more information about task settings, see [*Schema evolution*](#Schema)

Information noteIf there are schema evolution changes that have not been automatically applied to storage, you must validate and prepare the storage task.

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

## Storage settings

You can set properties for the storage data task when the data platform is a Qlik Open Lakehouse.

- Click Settings.

## General settings

- Database

  Database to use in the data source.
- Task schema

  You can change the name of the storage data task schema. Default name is the name of the storage task.
- Internal schema

  You can change the name of the internal storage data asset schema. Default name is the name of the storage task with \_internal appended.
- Default capitalization of schema name

  You can set the default capitalization for all schema names. If your database is configured to force capitalization, this option will not have effect.
- Prefix for all tables and views

  You can set a prefix for all tables and views created with this task.

  Information noteYou must use a unique prefix when you want to use a database schema in several data tasks.
- History

  You can keep historical change data to let you easily recreate data as it looked at a specific point in time. In AWS, you can use history views and live history views to see historical data. GCP projects do not generate storage views. Select Keep historical records and archive of change records to enable historical change data.
- When comparing storage with landing, you can choose how to manage records that do not exist in the landing.

  - Mark as deleted

    This will perform a soft delete of records that do not exist in the landing.
  - Keep

    This will keep all records that do not exist in the landing.

  Information noteDatasets in Storage data task must have a primary key set. If not, each time landing data is reloaded an initial load will be performed on the Storage data task.
- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

  For more information about Catalog, see [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm).

### Runtime settings

- Parallel execution

  You can set the maximum number of connections for full loads to a number from 1 to 5.
- Warehouse

  The name of the cloud data warehouse. This setting is only applicable for Snowflake.

### Schema evolution

Select how to handle the following types of DDL changes in the schema. When you have changed schema evolution settings, you must prepare the task again. The table below describes which actions are available for the supported DDL changes.

| DDL change | Apply to target | Ignore | Stop task |
| --- | --- | --- | --- |
| Add column | Yes | Yes | Yes |
| Create table If you used a Selection rule to add datasets that match a pattern, new tables that meet the pattern will be detected and added. | Yes | Yes | Yes |

## Operations on the storage data task

You can perform the following operations on a storage data task from the task menu.

- Open

  This opens the storage data task . You can view the table structure and details about the data task and monitor the status for the full load and batches of changes.
- Edit

  You can edit the name and the description of the task, and add tags.
- Delete

  You can delete the data task.
- Prepare

  This prepares a task for execution. This includes:

  - Validating that the design is valid.
  - Creating or altering the physical tables and, in AWS, views to match the design.
  - Generating the SQL code for the data task
  - Creating or altering the catalog entries for the task output datasets.

  You can follow the progress under Preparation progress in the lower part of the screen.

Information noteBefore you prepare a task, stop all tasks that are directly downstream.

- Validate datasets

  This validates all datasets that are included in the data task.

  Expand Validate and adjust to see all validation errors and design changes.
- Recreate tables

  This recreates the datasets from the source. When recreating a table, the downstream task will react as if a truncate and reload action occurred on the source datasets. For more information, see [*Troubleshooting a storage data task*](#Troubles).
- Stop

  You can stop operation of the data task. The data task will not continue to update the tables.

  Information noteThis option is available when the data task is running.
- Resume

  You can resume the operation of a data task from the point that it was stopped.

  Information noteThis option is available when the data task is stopped.
- Mirror data

  Mirror Qlik Open Lakehouse tables to other data platforms. This creates a Mirror data task.

  [*Mirroring data to a cloud data warehouse*](mirroring-data.htm)

## Limitations

- If the data task contains datasets and you change any parameters in the connection, for example username, database, or schema, the assumption is that the data exists in the new location. If this is not the case, you can either:

  - Move the data in the source to the new location.
  - Create a new data task with the same settings.
