---
title: "Replicating data with a Qlik Talend Cloud Starter subscription"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/replicating-starter-subscription.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project"]
---

# Replicating data with a Qlik Talend Cloud Starter subscription

Using the task setup wizard, you can easily set up a replication task with just a few clicks.

The settings shown in the wizard reflect the selected target type. For example, when replicating to storage targets such as Amazon S3, you will be prompted for a storage location. However, when replicating to targets such as Amazon Redshift that require a staging area, you will be prompted to define or select a staging area.

The following table will help you navigate this topic according to your intended target.

## [*Replicating to databases and to data warehouses without staging*](#Replicat)

Set up a replication task to databases or to data warehouses that do not require to external staging, which are as follows:

- Google BigQuery
- Snowflake

## [*Replicating to data warehouses with staging*](#Replicat2)

Set up a replication task to data warehouses that require access to external staging, which are as follows:

- Amazon Redshift
- Microsoft Fabric
- Databricks

## [*Replicating to cloud storage*](#Replicat3)

Set up a replication task to cloud storage.

## Replicating to databases and to data warehouses without staging

This section explains how to set up a replication task to databases and to data warehouses that do not require a separate staging area.

To do this:

1. In Data Integration > Home, click Replicate data.

   The Replicate data wizard opens.
2. In the General tab, do the following:

   - Task name

     Specify a name for your task.
   - Description

     Optionally, enter a description for your task.
   - Project

     Do one of the following:

     - Select an existing project
     - Specify a name for a new project and then click Add new project: <your-project-name> below the Project field.

       The project name will be added to the Project field.
   - Space

     Select a data space for you replication project. If you have not created any data spaces, do one of the following:

     - Select Data-Space (the default tenant data space)

       Information noteData-Space has full permissions for all members. You can edit the roles and permissions each member has later, as described in [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).
     - Cancel the wizard, create your own data space as described in [Creating a data space](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/manage-data-space.htm#anchor-1), and then run the wizard again.

     For more information on data spaces, see [*Working in spaces in Data Integration*](../DataSpaces/working-spaces.htm).
3. Click Next. In the Select source connection tab, select a connection to the source data. You can optionally edit the connection settings by selecting Edit from the menu in the Actions column.

   If you have not yet created a connection to your data source, you need to create one by clicking Create connection in the top right of the tab.

   You can filter the list of connections using the filters on the left. Connections can be filtered according to source type, gateway, space, and owner. The All filters button above the connections list shows the number of current filters. You can use this button to close or open the Filters panel on the left. Currently active filters are also shown above the list of available connections.

   You can also sort the list by selecting Last modified, Last created, or Alphabetical from the drop-down list on the right. Click the arrow to the right of the list to change the sorting order.

   After you have selected a data source connection, optionally click Test connection in the top right of the tab(recommended), and then click Next.
4. In the Select datasets tab, select tables and/or views to include in the replication task. You can also use wildcards and create selection rules as described in [*Selecting data from a database*](../Landing/Landing-data-data-sources.htm#Selectin).
5. In the Select target connection tab, select the target from the list of available connections and then click Next. In terms of functionality, the tab is the same as the Select source connection tab described earlier.
6. In the Settings tab, optionally change the following settings and then click Next.

   Replication mode

   - Full load: Loads the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually should the need arise.

     Information noteWhen using a SaaS application connector, this option will be enabled and read-only as full load is required.
   - Apply changes: Keeps the target tables up-to-date with any changes made to the source tables.
   - Store changes: Stores the changes to the source tables in Change Tables (one per source table).

     For more information, see [*Store changes*](replicating-settings.htm#Store).

   The change data capture frequency is determined by the scheduler settings. The default change capture interval is every six hours. For more information, see [*Replication settings*](replicating-settings.htm#Scheduli).

   Custom schemas

   - Target dataset schema: Optionally, select the schema in which you want the datasets to be created on the target.
   - Control table schema: Optionally, select the schema in which you want the control tables to be created on the target.

   Replication scheduler

   - Replicate data every: You can schedule how often to capture changes from the data source and set a Start time and Start date.

     The task setup wizard allows you to schedule an hourly interval. After you have completed setting up the task, you can explore different scheduling options, as described in [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).

   For information about minimum scheduling intervals according to data source type and subscription tier, see [*Minimum allowed scheduling intervals*](../../Admin/subscription-options-QTC.htm#Minimum).

   You can change the settings later, as described in [*Replication settings*](replicating-settings.htm).
7. In the Summary tab, a visual of the data pipeline is displayed. Choose one of the following After the pipeline is created actions:

   - Open the <name> project (the default)
   - Open the <name> data task

     Information noteIf some of the selected datasets do not support CDC, two pipelines will be displayed: one for the CDC task and the other for the Reload task.

   Then click Create and run (the default) or Create to create the task without running it.

   If you clicked Create and run, the task will be created and start to run (which may take a few moments).
8. If you clicked Create, one of the following will happen according to the After the pipeline is created action you selected earlier:

   - The project will open showing the newly created task.
   - The task will open on the Datasets tab. The Datasets tab shows the structure and metadata of the selected source tables. This includes all explicitly listed tables as well as tables that match the selection rules.

     If you want to add more tables from the data source, click Select source data.
9. You can perform transformations on the datasets, filter data, or add columns.

   For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
10. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation fails, resolve the errors before proceeding.

    For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
11. When you are ready, click Prepare and run to prepare and run the data task.

    For information on recovering tasks and other methods of running tasks, see [*Advanced run options*](replicating_advanced_run.htm).
12. The replication task should now start, and you can see the progress in Monitor. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori)

## Replicating to data warehouses with staging

This section explains how to set up a replication task to data warehouses that require a separate staging area.

To do this:

1. In Data Integration> Home, click Replicate data.

   The Replicate data wizard opens.
2. In the General tab, do the following:

   - Task name

     Specify a name for your task.
   - Description

     Optionally, enter a description for your task.
   - Project

     Do one of the following:

     - Select an existing project
     - Specify a name for a new project and then click Add new project: <your-project-name> below the Project field.

       The project name will be added to the Project field.
   - Space

     Select a data space for you replication project. If you have not created any data spaces, do one of the following:

     - Select Data-Space (the default tenant data space)

       Information noteData-Space has full permissions for all members. You can edit the roles and permissions each member has later, as described in [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).
     - Cancel the wizard, create your own data space as described in [Creating a data space](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/manage-data-space.htm#anchor-1), and run the wizard again.

     For more information on data spaces, see [*Working in spaces in Data Integration*](../DataSpaces/working-spaces.htm).
3. Click Next. In the Select source connection tab, select a connection to the source data. You can optionally edit the connection settings by selecting Edit from the menu in the Actions column.

   If you have not yet created a connection to your data source, you need to create one by clicking Create connection in the top right of the tab.

   You can filter the list of connections using the filters on the left. Connections can be filtered according to source type, gateway, space, and owner. The All filters button above the connections list shows the number of current filters. You can use this button to close or open the Filters panel on the left. Currently active filters are also shown above the list of available connections.

   You can also sort the list by selecting Last modified, Last created, or Alphabetical from the drop-down list on the right. Click the arrow to the right of the list to change the sorting order.

   After you have selected a data source connection, optionally click Test connection in the top right of the tab(recommended), and then click Next.
4. In the Select datasets tab, select tables and/or views to include in the replication task. You can also use wildcards and create selection rules as described in [*Selecting data from a database*](../Landing/Landing-data-data-sources.htm#Selectin).
5. In the Select target connection tab, select the target from the list of available connections and then click Next. In terms of functionality, the tab is the same as the Select source connection tab described earlier.
6. In the Settings tab, optionally change the following settings and then click Next.

   Replication mode

   - Full load: Loads the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually should the need arise.

     Information noteWhen using a SaaS application connector, this option will be enabled and read-only as full load is required.
   - Apply changes: Keeps the target tables up-to-date with any changes made to the source tables.
   - Store changes: Stores the changes to the source tables in Change Tables (one per source table).

     For more information, see [*Store changes*](replicating-settings.htm#Store).

   The change data capture frequency is determined by the scheduler settings. The default change capture interval is every six hours. For more information, see [*Replication settings*](replicating-settings.htm#Scheduli).

   Connection to staging area

   When replicating to the data warehouses listed below, you need to set a staging area. Data is processed and prepared in the staging area before being transferred to the warehouse.

   - [Amazon Redshift](../TargetConnections/redshift-target.htm)
   - [Microsoft Fabric](../TargetConnections/fabric-target.htm)
   - [Databricks](../TargetConnections/databricks-target.htm)

   Either select an existing staging area or click Create new to define a new staging area and follow the instructions in [*Connecting to cloud storage*](../TargetConnections/cloud-storage-connections.htm).

   To edit the connection settings, click Edit. To test the connection (recommended), click Test connection.

   For information on which staging areas are supported with which data warehouses, see the Supported as a staging area column in[*Target platform use cases and supported versions*](../TargetConnections/data-project-connections.htm#ar_app_supported_dbversions_993761142_cjaehbcc).

   Custom schemas

   - Target dataset schema: Optionally, select the schema in which you want the datasets to be created on the target.
   - Control table schema: Optionally, select the schema in which you want the control tables to be created on the target.

   Replication scheduler

   - Replicate data every: You can schedule how often to capture changes from the data source and set a Start time and Start date. If a dataset supports CDC, only the changes to that dataset will be retrieved and propagated to the corresponding target table. If a dataset does not support CDC, (for example, a View), changes will be propagated by reloading the entire dataset. With SaaS application connectors, a single task will be created with the ability to schedule CDC intervals and reload intervals during the onboarding, and later in the task's scheduling settings. When using other connectors types (for example, databases) with the CDC update method, if some of the selected datasets support CDC and some do not, two separate sub-tasks will be created: one for retrieving the changes to the datasets that support CDC, and the other for reloading the datasets that do not support CDC.

     The task setup wizard allows you to schedule an hourly interval. After you have completed setting up the task, you can explore different scheduling options, as described in [*Replication settings*](replicating-settings.htm#Scheduli).

   You can change the settings later, as described in [*Replication settings*](replicating-settings.htm).
7. In the Summary tab, a visual of the data pipeline is displayed. Choose one of the following After the pipeline is created actions:

   - Open the <name> project (the default)
   - Open the <name> data task

     Information noteIf some of the selected datasets do not support CDC, two pipelines will be displayed: one for the CDC task and the other for the Reload task.

   Then click Create and run (the default) or Create to create the task without running it.

   If you clicked Create and run, the task will be created and start to run (which may take a few moments).
8. If you clicked Create, one of the following will happen according to the After the pipeline is created action you selected earlier:

   - The project will open showing the newly created task.
   - The task will open on the Datasets tab. The Datasets tab shows the structure and metadata of the selected source tables. This includes all explicitly listed tables as well as tables that match the selection rules.

     If you want to add more tables from the data source, click Select source data.
9. You can perform transformations on the datasets, filter data, or add columns.

   For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
10. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation fails, resolve the errors before proceeding.

    For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
11. When you are ready, click Prepare and run to prepare and run the data task.

    For information on recovering tasks and other methods of running tasks, see [*Advanced run options*](replicating_advanced_run.htm).
12. The replication task should now start, and you can see the progress in Monitor. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori)

## Replicating to cloud storage

This section explains how to set up a replication task to cloud storage.

To do this:

1. In Data Integration> Home, click Replicate data.

   The Replicate data wizard opens.
2. In the General tab, do the following:

   - Task name

     Specify a name for your task.
   - Description

     Optionally, enter a description for your task.
   - Project

     Do one of the following:

     - Select an existing project
     - Specify a name for a new project and then click Add new project: <your-project-name> below the Project field.

       The project name will be added to the Project field.
   - Space

     Select a data space for you replication project. If you have not created any data spaces, do one of the following:

     - Select Data-Space (the default tenant data space)

       Information noteData-Space has full permissions for all members. You can edit the roles and permissions each member has later, as described in [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).
     - Cancel the wizard, create your own data space as described in [Creating a data space](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/manage-data-space.htm#anchor-1), and run the wizard again.

     For more information on data spaces, see [*Working in spaces in Data Integration*](../DataSpaces/working-spaces.htm).
3. Click Next. In the Select source connection tab, select a connection to the source data. You can optionally edit the connection settings by selecting Edit from the menu in the Actions column.

   If you have not yet created a connection to your data source, you need to create one by clicking Create connection in the top right of the tab.

   You can filter the list of connections using the filters on the left. Connections can be filtered according to source type, gateway, space, and owner. The All filters button above the connections list shows the number of current filters. You can use this button to close or open the Filters panel on the left. Currently active filters are also shown above the list of available connections.

   You can also sort the list by selecting Last modified, Last created, or Alphabetical from the drop-down list on the right. Click the arrow to the right of the list to change the sorting order.

   After you have selected a data source connection, optionally click Test connection in the top right of the tab(recommended), and then click Next.
4. In the Select datasets tab, select tables and/or views to include in the replication task. You can also use wildcards and create selection rules as described in [*Selecting data from a database*](../Landing/Landing-data-data-sources.htm#Selectin).
5. In the Select target connection tab, select the target from the list of available connections and then click Next. In terms of functionality, the tab is the same as the Select source connection tab described earlier.
6. In the Settings tab, optionally change the following settings and then click Next.

   Update method

   - Change data capture (CDC): The data lake landing tasks starts with a full load (during which all of the selected tables are landed). The landed data is then kept up-to-date using CDC (Change Data Capture) technology.

     Information noteCDC (Change Data Capture) of DDL operations is not supported.

     The change data capture frequency is determined by the scheduler settings. The default change capture interval is every six hours. For more information, see [*Replication settings*](replicating-settings.htm#Scheduli).
   - Reload: Performs a full load of the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually or scheduled to occur periodically as needed.

   If you select Change data capture (CDC), and your data also contains tables that do not support CDC, or views, two data pipelines will be created. One pipeline with all tables supporting CDC, and another pipeline with all other tables and views using Reload.

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

   - Replicate data every: You can schedule how often to capture changes from the data source and set a Start time and Start date. If a dataset supports CDC, only the changes to that dataset will be retrieved and propagated to the corresponding target table. If a dataset does not support CDC, (for example, a View), changes will be propagated by reloading the entire dataset. With SaaS application connectors, a single task will be created with the ability to schedule CDC intervals and reload intervals during the onboarding, and later in the task's scheduling settings. When using other connectors types (for example, databases) with the CDC update method, if some of the selected datasets support CDC and some do not, two separate sub-tasks will be created: one for retrieving the changes to the datasets that support CDC, and the other for reloading the datasets that do not support CDC.

     The task setup wizard allows you to schedule an hourly interval. After you have completed setting up the task, you can explore different scheduling options, as described in [*Settings for cloud storage targets*](landing-datalakes-settings.htm#Scheduli).

   You can change the task settings later as described in [*Settings for cloud storage targets*](landing-datalakes-settings.htm).
7. In the Summary tab, a visual of the data pipeline is displayed. Choose one of the following After the pipeline is created actions:

   - Open the <name> project (the default)
   - Open the <name> data task

     Information noteIf some of the selected datasets do not support CDC, two pipelines will be displayed: one for the CDC task and the other for the Reload task.

   Then click Create and run (the default) or Create to create the task without running it.

   If you clicked Create and run, the task will be created and start to run (which may take a few moments).
8. If you clicked Create, one of the following will happen according to the After the pipeline is created action you selected earlier:

   - The project will open showing the newly created task.
   - The task will open on the Datasets tab. The Datasets tab shows the structure and metadata of the selected source tables. This includes all explicitly listed tables as well as tables that match the selection rules.

     If you want to add more tables from the data source, click Select source data.
9. You can perform transformations on the datasets, filter data, or add columns.

   For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
10. When you have added the transformations that you want, you can validate the datasets by clicking Validate datasets. If the validation fails, resolve the errors before proceeding.

    For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
11. When you are ready, click Prepare and run to prepare and run the data task.

    For information on recovering tasks and other methods of running tasks, see [*Advanced run options*](replicating_advanced_run.htm).
12. The replication task should now start, and you can see the progress in Monitor. For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm#Monitori)

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

You can refresh the metadata in the task to align with changes in the metadata of the source in the Design view of a task. For SaaS applications using Metadata manager, Metadata manager must be refreshed before you can refresh metadata in the data task.

Information noteThis operation only affects tables in the Design view of a task.

1. You can either:

   - Click ..., and then Refresh metadata to refresh metadata for all datasets in the task.
   - Click ... on a dataset in Datasets, and then Refresh metadata to refresh metadata for a single dataset.

   You can view the status of the metadata refresh under Refresh metadata in the lower part of the screen. You can see when metadata was last refreshed by hovering the cursor on ![info button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg).
2. Prepare the data task to apply the changes.

   When you have prepared the data task and the changes are applied, the changes are removed from Refresh metadata.

You must prepare storage tasks that consume this task to propagate the changes.

If a column is removed, a transformation with Null values is added to ensure that storage will not lose historical data.

### Limitations for refreshing metadata

- A rename with a dropped column before that, in the same time slot, will be translated into the dropped column rename if they have the same data type and data length.

  Example:

  Before: a b c d

  After: a c1 d

  In this example, b was dropped and c was renamed to c1, and b and c have same data type and data length.

  This will be identified as a rename of b to c1 and a drop of c.
- Last column rename is not recognized, even if the last column was dropped,and the one before it was renamed.

  Example:

  Before: a b c d

  After: a b c1

  In this example, d was dropped and c was renamed to c1.

  This will be identified as a drop of c and d, and an add of c1.
- New columns are assumed to be added at the end. If columns are added in the middle with the same data type as the next column, they may be interpreted as a drop and rename.

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
