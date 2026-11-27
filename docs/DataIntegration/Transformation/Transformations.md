---
title: "Transforming data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Transformations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Transforming data

You can create reusable and rule-based data transformations as a part of your data pipeline. You can perform transformations as part of your data onboarding, or create reusable transformation data tasks. You can perform row-level transformations, include SQL transformations, and design complex transformation flows. The resulting datasets can either be materialized as tables, or created as views that perform transformations on the fly.

Information noteAdvanced transformations are available with a Qlik Talend Cloud Premium or Qlik Talend Cloud Enterprise subscription.

- You can perform explicit dataset transformations, or create global rules that transform multiple datasets. You can also filter a dataset to create a subset of rows.
- You can add SQL transformations. A SQL transformation allows you to input a SQL SELECT query into a pipeline to define complex or simple transformations.
- You can use SQL workbench to explore data across prepared tasks and validate SQL queries in the context of your project. For more information, see [*Exploring data with SQL Workbench*](SQL-workbench-data-exploration.htm).
- You can add visual transformation flows with sources, processors and targets to define complex or simple transformations.

Information noteData tasks operate in the context of the owner of the project they belong to. For more information about required roles and permissions, see [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).

A transformation data task contains three views:

- Transform

  This view displays all transformations to visualize the flow from source dataset to target dataset.
- Datasets

  This view displays all basic transformations on the datasets such as filtering data, or adding columns, as well as rules to perform global transformations.
- Model

  This view lets you create a data model with the relationships between the included datasets. For more information, see [*Creating a data model*](Create-data-model.htm).

In addition to storing tables in the data warehouse, you can also store tables as Iceberg tables that are managed by the data platform. This option is currently only available with Snowflake projects. This is possible by selecting Snowflake-managed Iceberg tables under Table type in the task settings.

## Creating a transformation data task

The easiest way to create a transformation data task is to click ... on a storage data task and then selecting Transform data.

You can also click Create in a project and select Transform data. In this case you need to define which source data task to use.

1. Define your source data and targets in Transform.

   You can either:

   - Perform dataset transformations

     Select source datasets and click Add to target to add them to Target.

     You can then perform basic transformations on the datasets such as filtering data, or adding columns, in Datasets.

     For more information, see [*Managing datasets*](../Introduction/Managing-datasets.htm).
   - Add a SQL transformation

     Select source datasets and click Add SQL transformation.

     A SQL transformation allows you to input a SQL SELECT query into a pipeline to define complex or simple transformations.

     For more information, see [*Adding SQL transformations*](Adding-SQL-based-tables.htm).
   - Add a transformation flow

     Select source datasets and click Add transformation flow.

     The flow designer allows you to create a transformation flow with sources, processors and targets to define complex or simple transformations.

     For more information, see [*Adding transformation flows*](Adding-transformation-flows.htm).
2. You can also add more datasets from other storage data tasks by clicking Select source data.

   You can add datasets from the current project, or from another project. To add datasets from another project:

   - You must have at least Can consume role in the space of the consumed project.
   - Both projects must be on the same data platform.

   If the selected project is under version control, you can select which branch to use as the source. For more information about cross-project pipelines, see [*Building cross-project pipelines*](../Introduction/Data-projects.htm#Building).
3. When you have added the transformations that you want, validate the datasets by clicking Validate datasets. If the validation finds errors, fix the errors before proceeding.

   For more information, see [*Validating and adjusting the datasets*](../Introduction/Managing-datasets.htm#Validati).
4. Create a data model

   Click Model to set the relationships between the included datasets.

   For more information, see [*Creating a data model*](Create-data-model.htm).
5. Click Prepare to prepare the data task and all required artifacts. This can take a little while.

   You can follow the progress under Preparation progress in the lower part of the screen.

   Information noteBefore you prepare a task, stop all tasks that are directly downstream.
6. When the status displays Prepared, you can run the data task .

   Click ... and then Run.

The data task will now start creating datasets to transform the data.

Information noteIt is not possible to change which datasets are included when you have started generating datasets.

## Using the Transform view

In Transform, all transformations are displayed to visualize the flow from source dataset to target dataset.

- Select a transformation to see which source datasets are used, and which target datasets are created.
- Select a source to see all transformations where it is used, and all resulting targets.
- Select a target to see which are the source datasets, and which transformation created this target dataset.

Transform view in a transformation

![Trandform view in Transformation ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qcdi_transform.png "Click to view full size")

You can change the following settings by clicking Display options:

- Filter by transformation type

  Display only transformations of one or two transformation types.
- Filter

  Display all transformations or just the selected transformation. You must select a transformation to enable this option.
- Density

  Select if you want to display transformations with a compact layout, or a wide layout using more space.

## Using the Datasets view

In Datasets you can view and edit all target datasets in the transformation task.

See also [*Managing datasets*](../Introduction/Managing-datasets.htm) for more information.

### Adding a target dataset

You can add more target datasets to the transformation task.

1. Click ![Add dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
2. Provide Name and optionally Description for the dataset.
3. Select a source dataset from the datasets available in the task in Source dataset.

   Tip noteYou can select No source dataset to create a empty dataset, not connected to any source. You can add columns to the dataset during design, but you must connect to a source dataset before you can prepare the task.

The target dataset is now added.

### Changing the source dataset

You can change the source dataset of a target dataset.

1. Click ![edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) after Source: [name of source dataset].
2. Select another source dataset from the datasets available in the task in Source dataset.

   Tip noteYou can select No source dataset to disconnect the target dataset from the source. You can edit the dataset during design, but you must connect to a source dataset before you can prepare the task.

### Adding new columns

You can add new columns to the target dataset.

- Adding a new column from scratch

  Click + Add.

  Provide a name for the column, and set an expression to define the column data.

  For more information, see [*Adding columns to a dataset*](Add-columns.htm).
- Adding a column from source

  Click ![down](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to Add and select Add column from source.

  Select a column from the source dataset.

### Reordering columns

You can change the ordinal position of a column.

1. Select a column.
2. Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then Reorder.
3. Use the arrows to move the column up or down.
4. Close Change ordinal when you are ready.

### Creating transformation rules

You can create re-usable transformation rules to perform global transformation on datasets.

For more information about creating rules, see [*Creating rules to transform datasets*](Transformation-rules.htm).

Tip noteYou can view the effects of rules by selecting Show rules effects. You cannot make changes to the datasets when Show rules effects is enabled.

### Filtering a dataset

You can filter data to create a subset of rows, if required.

- Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then Filter.

For more information about filtering, see [*Filtering a dataset*](Filter-data.htm).

## Scheduling a transformation task

You can schedule a transformation task to be updated periodically. You can set a time based schedule, or set the task to run when input data tasks have completed running.

Click ... on a data task and select Scheduling to create a schedule. The default scheduling setting is inherited from the settings in the project. For more information about default settings, see [*Transform defaults*](../Introduction/Data-project-settings.htm#Transfor).

You always need to set Scheduling to On to enable the schedule.

Information noteIf all datasets in the task are non-materialized, there is nothing to run as the transformation is performed on-the-fly with views. You can still create a schedule for a non-materialized transformation ask to run when the schedule condition is met. The task will complete immediately which can trigger a downstream task, for example a data mart. This allows you to build an event based pipeline schedule that includes non-materialized transformations without interrupting the pipeline flow.

### Time based schedules

You can use a time based schedule to run the task regardless of when the different input sources are updated.

- Select At specific time in Run the data task.

You can set an hourly, daily, weekly or monthly schedule.

### Event based schedules

You can use an event based schedule to run the task when input data tasks have completed running.

- Select On specific event in Run the data task.

You can select if you want to run the task when any of the input tasks have completed successfully, or when any of a selection of input tasks have completed successfully.

Information noteThe task will not run if any input task or downstream task is running when the schedule is triggered. The task is skipped until the next scheduled run.

## Monitoring a transformation task

You can monitor the status and progress of a transformation task by clicking on Monitor.

For more information, see [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm).

## Reloading data

You can perform a manual reload of tables if the data is materialized as physical tables. This is useful when there are issues with one or more tables.

Information noteIf datasets are non-materialized, you must reload the source datasets in the upstream data task to refresh data.

1. Open the data task and select the Monitor tab.
2. Select the tables that you want to reload.
3. Click Reload tables.

The reload will happen the next time the task is run. The reload process behaves differently depending on the history setting and transformation type of each dataset. This means that the reload process can differ between datasets in a data task.

- Dataset transformations are reloaded by truncating and loading.
- SQL transformations and transformation flows can be reloaded by truncating and loading, or by comparing and applying. It is best practice to compare and apply.

  [*Reloading a dataset based on SQL transformation or transformation flow*](#Reloadin)

You can cancel the reload for tables that are pending reload by clicking Cancel reload. This will not affect tables that are already reloaded, and reloads that are currently running will be completed.

Downstream tasks will be reloaded to apply changes, and to avoid backdating.

Downstream impact after reloading a Transform data task

![Transformation reload downstream effects](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qcdi_reload_downstream_transform.png "Click to view full size")

The impact downstream depends on the type of reload operation executed, and the type of immediate downstream dataset. Standard processing means that the dataset will react and process data using the configured method for the specific dataset.

Example: Reloading a dataset via truncate and load

- If the next dataset uses dataset transformations, it will be reloaded on next execution via a truncate and load.
- If the next dataset is a SQL transformation or transformation flow, it will be reloaded using compare and apply.

### Reloading a dataset with no history

In this case, there is no history to consider. To reduce processing on the target, the reload is performed by:

1. Truncating the tables.
2. Loading current data from the upstream data task.

Downstream tasks will be reloaded to apply changes.

### Reloading a dataset with history enabled

The reload is performed by:

1. Truncating current, prior, and changes tables.
2. Loading data from the upstream data task, including prior tables.

### Reloading a dataset based on SQL transformation or transformation flow

- Truncate and reload

  Information noteThis option may cause loss of history.

  1. Truncating the current and change tables.
  2. Running the query and loading it to the current tables.
- Reload and compare

  1. Running the query and comparing it with the current tables.
  2. Adding changes.

Information noteWhen a dataset based on SQL transformation or transformation flow is reloaded because of an upstream task reload, it is always reloaded by comparing and applying. If you want to truncate and reload it, you must issue a specific reload for these tables. In this case you must consider the effect on downstream tables as well.

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

## Transformation settings

You can set properties for the transformation data task .

- Click Settings.

Warning noteIf the task has already been run, changing a setting other than Runtime settings require that you recreate the datasets.

### General settings

- Database

  Database to use in the data source.
- Task schema

  You can change the name of the data task schema. Default name is the name of the task.
- Internal schema

  You can change the name of the internal storage schema. Default name is the name of the task appended with "\_\_internal".
- Default capitalization of schema name

  You can set the default capitalization for all schema names. If your database is configured to force capitalization, this option will not have effect.
- Prefix for all tables and views

  You can set a prefix for all tables and views created with this task.

  Information noteYou must use a unique prefix when you want to use a database schema in several data tasks.
- Materialized

  You can select to only create views that perform transformations on the fly (Non-materialized), or create both tables and views(Materialized).
- Historical Data Store (Type 2)

  You can keep historical change data to let you easily recreate data as it looked at a specific point in time. You can use history views and live history views to see historical data.
- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

  For more information about Catalog, see [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm).

### Runtime settings

- Parallel execution

  You can set the maximum number of connections for full loads to a number from 1 to 5.
- Warehouse

  The name of the cloud data warehouse.

### View type settings

The View type settings are only applicable for Snowflake.

- Standard views

  Use Standard views for most cases.
- Snowflake secure views

  Use Snowflake secure views for views designated for data privacy or sensitive information protection, such as views created to limit access to sensitive data that should not be exposed to all users of the underlying tables.

  Information note Snowflake secure views can execute more slowly than Standard views.

### Table type settings

These settings are only available in projects with Snowflake as data platform.

- Table type

  You can select which table type to use:

  - Snowflake tables
  - Snowflake-managed Iceberg tables

    You must set the default name of the external volume in Snowflake external volume.
- Cloud storage folder to use

  Select which folder to use when landing data to the staging area.

  - Default folder

    This creates a folder with the default name: <project name>/<data task name>.
  - Root folder

    Store data in the root folder of the storage.
  - Folder

    Specify a folder name to use.
- Sync with Snowflake Open Catalog

  Enable this to let Snowflake Open Catalog manage the files in cloud file storage.

## Best practices

- It is not possible to change source for a dataset in a data mart if facts and dimensions have been added. If you want to be flexible, you can add a preceding Transform task with non materialized views that can be used to change sources and also to have a model for all source tasks.

## Limitations and considerations

- It is not possible to change data types in a transformation data task when the Non-materialized option is selected.
- Field level lineage is not available for datasets created in SQL transformations or transformation flows.

  Information noteThis limitation applies to Qlik Cloud Government only. Using Add to target to read from a Qlik Open Lakehouse Mirror task set to Append only is not supported. As a workaround you can read data using a SQL transformation or a transformation flow.

Related learning:

- [Using Qlik Cloud Data Integration to onboard and transform data](/lnk/Qlik_cloud_data_integration_onboard_transform)
