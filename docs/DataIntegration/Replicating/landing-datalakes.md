---
title: "Landing data in a data lake with a Standard, Premium, or Enterprise subscription"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/landing-datalakes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project"]
---

# Landing data in a data lake with a Standard, Premium, or Enterprise subscription

You can set up a Land data in data lake task to land data to the following targets:

- Amazon S3

  For information on configuring a connection to your Amazon S3, see [*Amazon S3*](../TargetConnections/aws-s3-target.htm#Using2).
- Azure Data Lake Storage

  For information on configuring a connection to your Azure Data Lake Storage, see [*Azure Data Lake Storage*](../TargetConnections/adls-target.htm#top).
- Google Cloud Storage

  For information on configuring a connection to your Google Cloud Storage, see [*Google Cloud Storage*](../TargetConnections/google-storage-target.htm#Using).

Tip noteAlthough you can configure your source and target connection Land data in data lake settings in the task setup wizard, to simplify the setup procedure, it is recommended to do this before you create the task.

For information on configuring connections to your data sources, see [*Setting up connections to data sources*](../Landing/connecting-data-2.htm)

To set up a data lake landing task:

1. In Data Integration > Projects, click Create new > Project.
2. In the New project dialog, do the following:

   1. Provide a Name for your project.
   2. Select the Space in which you want the project to be created.
   3. Optionally, provide a Description.
   4. Select Replication as the Use case.
   5. Optionally, clear the Open check box if you want to create an empty project without configuring any settings.
   6. Click Create.

      One of the following will occur:

      - If the Open check box in the New project dialog was selected (the default), the project will open.
      - If you cleared the Open check box in the New project dialog, the project will be added to your list of projects. You can open the project later by selecting Open from the project's ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu.
3. After the project opens, click Land data in data lake.

   The Land data in data lake wizard opens.
4. In the General tab, specify a name and description for the data lake landing task. Then click Next.

   Information noteNames containing slash (/) or backslash (\) characters are not supported.
5. In the Select source connection tab, select a connection to the source data. You can optionally edit the connection settings by selecting Edit from the menu in the Actions column.

   Information noteIf you change the source connection or the source data gateway after the task has already been prepared, you must [recreate all the datasets](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Managing-datasets.htm#:~:text=the%20storage%20task.-,Recreating%20datasets,-You%20can%20recreate).

   If you don't have a connection to the source data yet, you need to create one first, by clicking Create connection in the top right of the tab.

   You can filter the list of connections using the filters on the left. Connections can be filtered according to source type, gateway, space, and owner. The All filters button above the connections list shows the number of current filters. You can use this button to close or open the Filters panel on the left. Currently active filters are also shown above the list of available connections.

   You can also sort the list by selecting Last modified, Last created, or Alphabetical from the drop-down list on the right. Click the arrow to the right of the list to change the sorting order.

   After you have selected a data source connection, optionally click Test connection in the top right of the tab(recommended), and then click Next.
6. In the Select datasets tab, select tables and/or views to include in the data lake landing task. You can also use wildcards and create selection rules as described in [*Selecting data from a database*](../Landing/Landing-data-data-sources.htm#Selectin).

   Information noteSchema names, or table names containing slash (/) or backslash (\) characters are not supported.
7. In the Select target connection tab, select a target from the list of available connections and then click Next. In terms of functionality, the tab is the same as the Select source connection tab described earlier.

   Information noteIf you change the target connection after the task has already been prepared, you must [recreate all the datasets](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Managing-datasets.htm#:~:text=the%20storage%20task.-,Recreating%20datasets,-You%20can%20recreate).
8. In the Settings tab, optionally change the following settings and then click Next.

   Update method:

   - Change data capture (CDC) using Change Tables: Data lake landing tasks starts with a full load (during which all of the selected tables are loaded to the target). The target data is then kept up-to-date using CDC (Change Data Capture) technology.

     Information noteCDC (Change Data Capture) of DDL operations is not supported.

     When working with Data Movement gateway, except when using a SaaS application source, changes are captured from the source in near real-time. When working without Data Movement gateway or with SaaS application sources, changes are captured according to the scheduler settings. For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
   - Reload: Performs a full load of the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually or scheduled to occur periodically as needed.

     Information noteThis setting is not available when using a SaaS application connector.

   Information note

   When Change data capture (CDC) is the update method, and your data source:

   - Is not a SaaS application
   - Contains datasets that support CDC and datasets that support Reload only (such as views)

   Two data pipelines will be created. One pipeline will be created for tables that support CDC, and another pipeline will be created for datasets that support Reload only.

   Folder to use

   Select one of the following, according to which bucket folder you want the files to be written to:

   - Default folder

     The default folder format is <your-project-name>/<your-task-name>
   - Root folder

     The files will be written to the root bucket folder.
   - Folder

     Specify a folder name. The folder will be created during the data task if it does not already exist.

     Information note The folder name cannot include special characters (for example, @, #, !, and so on).

   Replication scheduler

   You can schedule how often to capture changes from the data source and set a start date and time. The task setup wizard allows you to set a basic scheduling frequency. After you have completed setting up the task, additional scheduling options are available.

   For a description of all the scheduling options, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
9. In the Summary tab, a visual of the data pipeline is displayed. Choose whether to Open the <name> task or Do nothing. Then click Create.

   Depending on your choice, either the task will be opened or a list of projects will be displayed.
10. If you chose to open the task, the Datasets tab will show the structure and metadata of the selected data asset tables. This includes all explicitly listed tables as well as tables that match the selection rules.

    If you want to add more tables from the data source, click Select source data.
11. Optional, change the task setting as described in [*Settings for cloud storage targets*](landing-datalakes-settings.htm).
12. You can perform transformations on the datasets, filter data, or add columns.

    For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
13. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation fails, resolve the errors before proceeding.

    For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
14. When you are ready, click Prepare to catalog the landing task and prepare it for execution.
15. When the data task has been prepared, click Run.
16. The data lake landing task should now start. You can monitor its progress in Monitor view. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori)

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
- Add table that matches the selection pattern

  If you used a Selection rule to add datasets that match a pattern, new tables that meet the pattern will be detected and added.

For more information about task settings, see [*Automatic schema evolution*](landing-datalakes-settings.htm#Schema)

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

## Changing gateway or connections

When changing target or source connection, or source gateway, you must recreate tables.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Limitations and considerations when landing data in a data lake

Transformations are subject to the following limitations:

- Transformations are not supported for columns with right-to-left languages.
- Transformations cannot be performed on columns that contain special characters (e.g.
  #, \, /, -) in their name.
- The only supported transformation for LOB/CLOB data types is to drop the column on the target.
- Using a transformation to rename a column and then add a new column with the same name is not supported.

Changing nullability is not supported on columns that are moved, either changing it directly or using a transformation rule. However, new columns created in the task are nullable by default.
