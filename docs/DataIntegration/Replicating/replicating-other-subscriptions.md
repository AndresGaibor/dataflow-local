---
title: "Replicating data with a Standard, Premium, or Enterprise subscription"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/replicating-other-subscriptions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project"]
---

# Replicating data with a Standard, Premium, or Enterprise subscription

To set up a replication task:

1. In Data Integration > Pipeline projects, click Create new > Project.
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
3. After the project opens, click Replicate data.

   The Replicate data wizard opens.
4. In the General tab, specify a name and description for the replication task. Then click Next.
5. In the Select source connection tab, select a connection to the source data. You can optionally edit the connection settings by selecting Edit from the menu in the Actions column.

   Information noteIf you change the source connection or the source data gateway after the task has already been prepared, you must [recreate all the datasets](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Managing-datasets.htm#:~:text=the%20storage%20task.-,Recreating%20datasets,-You%20can%20recreate).

   If you have not yet created a connection to your data source, you need to create one by clicking Create connection in the top right of the tab.

   You can filter the list of connections using the filters on the left. Connections can be filtered according to source type, gateway, space, and owner. The All filters button above the connections list shows the number of current filters. You can use this button to close or open the Filters panel on the left. Currently active filters are also shown above the list of available connections.

   You can also sort the list by selecting Last modified, Last created, or Alphabetical from the drop-down list on the right. Click the arrow to the right of the list to change the sorting order.

   After you have selected a data source connection, optionally click Test connection in the top right of the tab(recommended), and then click Next.
6. In the Select datasets tab, select tables and/or views to include in the replication task. You can also use wildcards and create selection rules as described in [*Selecting data from a database*](../Landing/Landing-data-data-sources.htm#Selectin).
7. In the Select target connection tab, select the target from the list of available connections and then click Next. In terms of functionality, the tab is the same as the Select source connection tab described earlier.

   Information noteIf you change the target connection after the task has already been prepared, you must [recreate all the datasets](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Managing-datasets.htm#:~:text=the%20storage%20task.-,Recreating%20datasets,-You%20can%20recreate).
8. In the Settings tab, optionally change the following settings and then click Next.

   Replication mode

   Information noteWhen replicating from SaaS application sources, the Full load replication mode is enabled by default and cannot be disabled.

   - Full load: Loads the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually should the need arise.

     Information noteThis setting is not available when using a SaaS application connector.
   - Apply changes: Keeps the target tables up-to-date with any changes made to the source tables.
   - Store changes: Stores the changes to the source tables in Change Tables (one per source table).

     For more information, see [*Store changes*](replicating-settings.htm#Store).

   When working with Data Movement gateway, changes are captured from the source in near real-time. When working without Data Movement gateway (by setting Data gateway to None in the connector settings), changes are captured according to the scheduler settings. The default change capture interval is every six hours. For more information, see [*Replication settings*](replicating-settings.htm#Scheduli).

   Apply changes mode

   Information noteWhen replicating to data warehouse targets or when working with a Qlik Talend Cloud Starter subscription, you cannot select which Apply changes mode to use. Changes will always be applied in Batch optimized mode for maximum efficiency. The exception to this is when replicating to Snowflake target and the Loading method is set to Snowpipe streaming. In such a case, while you still cannot select which Apply changes mode to use, changes will always be applied in Transactional mode.

   Changes are applied to the target tables using one of the following methods:

   - Batch optimized: This is the default. When this option is selected, changes are applied in batches. A preprocessing action occurs to group the transactions into batches in the most efficient way.
   - Transactional: Select this option to apply each transaction individually, in the order it is committed. In this case, strict referential integrity is ensured for all tables.

   Connection to a staging area

   When replicating to the data warehouses listed below, you need to set a staging area. Data is processed and prepared in the staging area before being transferred to the warehouse.

   - [Amazon Redshift](../TargetConnections/redshift-target.htm)
   - [Microsoft Fabric](../TargetConnections/fabric-target.htm)
   - [Databricks](../TargetConnections/databricks-target.htm)

   Either select an existing staging area or click Create new to define a new staging area and follow the instructions in [*Connecting to cloud storage*](../TargetConnections/cloud-storage-connections.htm).

   To edit the connection settings, click Edit. To test the connection (recommended), click Test connection.

   For information on which staging areas are supported with which data warehouses, see the Supported as a staging area column in[*Target platform use cases and supported versions*](../TargetConnections/data-project-connections.htm#ar_app_supported_dbversions_993761142_cjaehbcc).

   Replication scheduler

   Information note

   This setting is only available in the following use cases:

   - When using a SaaS application connector.
   - When accessing data sources without Data Movement gateway.

   For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm).

   - Replicate data every: You can schedule how often to capture changes from the data source and set a start date and time. The task setup wizard allows you to set a basic scheduling frequency. After you have completed setting up the task, additional scheduling options are available.

     For a description of all the scheduling options, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).

   For information about minimum scheduling intervals according to data source type and subscription tier, see [*Minimum allowed scheduling intervals*](../../Admin/subscription-options-QTC.htm#Minimum).
9. In the Summary tab, a visual of the data pipeline is displayed. If some of the selected datasets do not support CDC, two pipelines will be displayed: one for the CDC task and the other for the Reload task. Choose whether to Open the <name> data task or Do nothing, and then click Create.

   Depending on your choice, either the task will be opened or a list of projects will be displayed.
10. If you chose to open the task, the Datasets tab will show the structure and metadata of the selected source tables. This includes all explicitly listed tables as well as tables that match the selection rules.

    If you want to add more tables from the data source, click Select source data.
11. Optional, change the task setting as described in[*Replication settings*](replicating-settings.htm).
12. You can perform transformations on the datasets, filter data, or add columns.

    For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
13. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation fails, resolve the errors before proceeding.

    For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
14. When you are ready, click Prepare to catalog the data task and prepare it for execution.

    Information note
    - When you prepare a data task configured with the Full Load replication mode, the settings defined in the [task setting's Full load tab](replicating-settings.htm) will be applied.
    - By default, the initial prepare operation will drop and recreate any existing target tables. You can override the default by following the steps in [*Retaining existing target tables during initial prepare*](#Retainin)below.
15. When the data task has been prepared, click Run.

    For information on recovering tasks and other methods of running tasks, see [*Advanced run options*](replicating_advanced_run.htm).
16. The replication task should now start, and you can see the progress in Monitor. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori)

## Retaining existing target tables during initial prepare

By default, the initial prepare operation drops and recreates any existing target tables. However, in some cases, you might wish to retain the existing target tables.
For example, if you import a project with data tasks that already ran, you can start (resume) the data tasks from just after the last timestamp or position of the existing target records.

Information noteNot supported when replicating from SaaS application sources.

To do this:

1. In the [Full Load task settings](replicating-settings.htm#Basic), set If target table already exists to Ignore.

   Information noteIn addition to being applied during the data task preparation stage, this setting will also be applied any time a table is reloaded.
2. Prepare the task.
3. After the task has been prepared, open the [Advanced run options dialog](replicating_advanced_run.htm) and select Tables are already loaded. Start processing changes from:. To prevent duplicate target records, enter a date and time or source position (depending on the data source) just after the last timestamp or position of the existing target records.
4. Run the task.

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
- Drop table
- Drop column
- Add table that matches the selection pattern

  If you used a Selection rule to add datasets that match a pattern, new tables that meet the pattern will be detected and added.

For more information about task settings, see [*Automatic schema evolution*](replicating-settings.htm#Schema)

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

## Changing gateway or connections

When changing target or source connection, or source gateway, you must recreate tables.

## Viewing project information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view project information, such as:

- Owner
- Space
- Data platform
- Project ID

## Limitations and considerations when replicating data

Transformations are subject to the following limitations:

- Transformations are not supported for columns with right-to-left languages.
- Transformations cannot be performed on columns that contain special characters (e.g.
  #, \, /, -) in their name.
- The only supported transformation for LOB/CLOB data types is to drop the column on the target.
- Using a transformation to rename a column and then add a new column with the same name is not supported.

Changing nullability is not supported on columns that are moved, either changing it directly or using a transformation rule. However, new columns created in the task are nullable by default.
