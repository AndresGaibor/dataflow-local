---
title: "Creating and managing data marts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataMarts/DataMarts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Creating and managing data marts

Once you have onboarded your data, you can then create data marts using the data from the Storage or Transform tasks. You can create any number of data marts depending on your business needs. Ideally, your data marts should contain repositories of summarized data collected for analysis on a specific section or unit within an organization, for example, the Sales department.

Information noteData mart creation is available with a Qlik Talend Cloud Premium or Qlik Talend Cloud Enterprise subscription.

Information noteData tasks operate in the context of the owner of the project they belong to. For more information about required roles and permissions, see [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).

In addition to storing tables in the data warehouse, you can also store tables as Iceberg tables that are managed by the data platform. This option is currently only available with Snowflake projects. This is possible by selecting Snowflake-managed Iceberg tables under Table type in the task settings.

## Prerequisites

You can use data tasks of the following types as source for a data mart:

- Storage
- Transform

Before you can create a data mart, you need to do the following in the source data tasks:

- Populate the datasets with data that you want to use in your data mart. For more information, see [*Onboarding data to a data warehouse*](../Onboarding/Onboarding-data.htm).
- Create a dataset relational model to define the relationships between the source datasets. For more information, see [*Creating a data model*](../Transformation/Create-data-model.htm).

  Warning noteAll source datasets must have keys.

## Creating a data mart

To create a data mart:

1. Open your project.
2. Do one of the following:

   - Click Create in the top right and select Create data mart.
   - In the source data task, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) in the bottom right corner and then select Create data mart.

   The Create data mart dialog opens.

   ![Dialog for Create data mart](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/create-data-mart.png)
3. Provide a name for your data mart and, optionally, provide a description as well.
4. If you want to configure the data mart later, clear the Open check box and then click Create. Otherwise, just click Create.

   The Data mart opens on the Data mart tab.

   ![Data mart](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-mart-tab-1.png)
5. Select your source data as described in [*Selecting your source data*](#Selectin)
6. If you want the data mart to contain dimensions, add dimensions as described in [*Adding dimensions and a fact to the data mart*](#Adding2)
7. If you want the data mart to contain a fact, add a fact as described in [*Adding a fact*](#Adding)
8. If the data mart contains both dimensions and a fact, add the dimensions to your star schema as described in [*Building a star schema*](#Adding3)
9. Create the datasets in your data mart and populate them with data as described in [*Populating your data mart*](#Populati)

## Learn more

- [*Data mart view structure*](datamarts-structure.htm)

## Selecting your source data

You select your source data from the datasets in the source data task.

To do this:

1. Click the Select source data button in the middle of the tab or click the Select source data toolbar button.

   The Select source data dialog opens.
2. From the Pipeline projects drop-down list, select which project to get source data from.

   You can add datasets from the current project, or from another project. To add datasets from another project:

   - You must have at least Can consume role in the space of the consumed project.
   - Both projects must be on the same data platform.

   If the selected project is under version control, you can select which branch to use as the source. For more information about cross-project pipelines, see [*Building cross-project pipelines*](../Introduction/Data-projects.htm#Building).
3. From the Data tasks drop-down list, select a Storage task, or a Transform task if you created transformations.
4. Either leave the default % to search for all datasets or enter the name of a specific dataset to find. Then click Search.
5. Select the desired datasets and then click Add selected tables.
6. Click OK to close the dialog and then proceed to Add a fact and/or Add dimensions.

Information noteYou can repeat the process to add datasets from other data tasks.

## Adding dimensions and a fact to the data mart

Once you have selected you source data, you can then proceed to build your data mart. A data mart can have a fact dataset, dimensions datasets, or a combination of both (where the dimension datasets are logically related to the fact dataset).

### Adding dimensions

To add a dimension.

1. Click the Add dimension button.

   The Add dimension dialog opens.
2. The following settings are available:

   - Most granular dataset: Select a dataset.
   - Name: Specify a display name for the dimension. The default is the most granular dataset name.
   - Description: Optionally, provide a description.
   - History type: Select one of the following:
     - Type 1: The existing record in the dimension will be updated whenever the corresponding record in the Storage is updated.
     - Type 2: A new record will be added to the dimension whenever the corresponding record in the Storage is updated.
   - Related dataset to denormalize: Any datasets that can be denormalized in the dimension dataset (according to the relationships in the source data asset model) will be available for selection here.

     Example of a dimension that can be denormalized

     ![Example of a dimension with related dimensions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/denormalized-dims.png)
3. Click OK to save your settings.

   The dimension will be added to the Dimensions list on the left.

See also [*Role-playing dimensions*](#Role).

#### Viewing information about a dimension

When you select a dimension, the Source relational model tab will be shown in the center pane. This tab shows the source datasets that are consolidated in the dimension. Datasets that you chose to denormalize when you added the dimension will be shown selected (and grayed out).

Products dimension denormalized with the Categories and Suppliers dataset

![Example of a relational model with related dimensions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/denormalized-dim-model.png)

### Adding a fact

To add a fact:

1. Click the Add fact button.

   The Add fact dialog opens.
2. The following settings are available:

   - Fact: Select a dataset to be the fact. The dataset should define the granularity of the fact you are creating.
   - Name: Specify a display name for the fact. The default is the fact name.
   - Description: Optionally, provide a description.
   - Related datasets to denormalize: Any datasets that can be denormalized in your fact dataset will be available for selection here.
   - Advanced
     - Use current data: When selected (the default), the fact will not contain a transaction date column.
     - Choose transaction date: To locate data according to a specific transaction date, select this option and then select a date column. This is useful if your star schema contains type 2 dimensions and you need to find the correct data for a specific transaction. For example, if a customer has multiple addresses, it might be possible to find the correct address according to the order date.

       Example use case:

       A retailer needs to create a data mart to analyze the relationship between orders and customers. The data mart should be able to answer queries such as: Which US state had the highest sum of orders in Q4 2022?

       If the retailer selects the Use current data option, only the most current record version in the Customers table will be included in the calculation.

       Ignoring the transaction date will result in inaccurate data as illustrated below:

       ![Shows the relationship between the Orders fact table and the Customers dimension when Use current data is selected.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/transaction-date-example-1.png)

       If the retailer selects the Choose transaction date option, however, the customer's orders will be associated with the correct record version in the Customers table.

       This will allow the retailer to accurately calculate the total sum of orders per state in Q4 2022.

       ![Shows the relationship between the Orders fact table and the Customers dimension when Use transaction date  is selected.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/transaction-date-example-2.png)

       Tip noteNote that the transaction date can be leveraged differently in each data mart, according to business needs. For example, in one data mart it could be used to analyze order dates, while in another data mart it could be used to analyze shipping dates.
3. Click OK to save your settings.

   The fact will be added to the Facts list on the left.

#### Viewing information about the fact

When you select a fact, the following tabs are shown in the center pane:

- Star schema model (default): Shows a graphical representation of the dataset relationships within the data mart.
- Fact model: Shows any datasets related to the fact dataset. Datasets that you chose to denormalize when you added the fact will be shown selected (and grayed out).

  Orders Details fact with a denormalized Orders dataset

  ![Example of a fact with denormalized dataset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/fact-model-denormalized.png)
- Transaction date: The name of the transaction column if you selected the Choose transaction date option when adding the fact.

### Unknown and late-arriving dimension handling

Every dimension contains -1 and 0 rows, which are the dimension’s business key (object ID). Row -1 is reserved for late-arriving dimensions, while 0 is reserved for unknown dimensions.

#### Unknown dimensions

“Unknown” is data that was unavailable when the dimension was originally created. For example, let’s say you have an ORDER fact with a SHIPPER column that is the business key for the SHIPPER dimension. If the ORDER fact row has not been shipped yet - and thus has NULL for the SHIPPER column - it will become related to the 0 record (which denotes an Unknown for the dimension). When the ORDER fact is later updated with a SHIPPER value (for example, USPS), the related dimension ID (0) will be updated in turn.

Information note"Unknown" could also be missing or non-existing data, which might never be added.

#### Late-arriving dimensions

A late-arriving dimension has a key which exists in the new fact data, but which does not yet exist in the dimension. For example, if the SHIPPER in the ORDER fact has a value of "NEWSHIP" for a new shipper and that business key does not yet exist in the DIM\_SHIPPER dimension, the data mart processing will relate that fact to the -1 row. This denotes a missing dimension member in your dimension table. When the "NEWSHIP" business key arrives for the DIM\_SHIPPER dimension, its dimension row will be created, and the fact record updated to align with the previously missing dimension.

## Building a star schema

Once you have added dimensions to your data mart, you can then proceed to connect them to your fact dataset, thereby creating a star schema.

To do this:

1. Select your fact in the Facts list on the left.
2. Select which dimensions to add from the Recommended dimensions list on the right.

   Recommended dimensions are shown connected to the fact dataset with a dotted line.

   In the image below, some of the dimensions were added earlier and are therefore connected with a solid gray line.

   ![Example of a star schema with recommended dimensions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/recommended-dims.png)
3. Click Apply to add the dimensions.

   The dimensions will be shown connected to the fact dataset with a solid gray line.
4. To close the Recommended dimensions panel, click ![Associate](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_associate.svg).

## Populating your data mart

Once you have designed your data mart, you can then proceed to populate it.

To do this:

1. Click the Prepare toolbar button in the top right.

   The preparation process includes creating datasets and views in the data mart, and updating the Catalog.

   You can follow the progress under Preparation progress in the lower part of the screen.

   After the preparation is complete, the Prepare button changes to Run.
2. Optionally, validate the data mart as described in [*Validating and synchronizing your data mart*](#Validati) below.
3. Click the Run button.

   The window switches to Monitor view, showing the loading progress and status of the datasets in your data mart.

   ![Data mart monitor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/data-mart-monitor.png)

Every source record will be processed by the data mart, even deleted records. This is done to ensure that historical information is kept.

Information noteFor dimension datasets with type 2 history, the processed records count will include all version rows for a record and show a higher value than the number of actual records processed.

## Validating and synchronizing your data mart

Validating the data mart ensures that the data mart metadata is identical to the corresponding metadata in the Storage (or Transform if defined). Validating the data mart also compares the created metadata against the current star schema design. For example, if you run the validation after adding a dimension to an already created data mart, the validation will fail.

To validate the data mart:

1. Either select Validate datasets from the ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu to the right of the Run button or click the Validate datasets button at the bottom right of the window.

   A Validation is completed message will be shown.
2. If the metadata is not in sync or if there are star schema design conflicts, the Validate and adjust pane at the bottom of the window will automatically open with the validation report.

   Example of a data mart with a star schema design conflict:

   ![Data mart with a start schema design conflict](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validate-dm.png)

   Example of a data mart with validation errors:

   ![Data mart with validation errors](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/validation-error.png)
3. To resolve any Pending design changes issues, click the ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) button in the top right and select Prepare. If the value of the Can be altered without data loss column is Yes, an ALTER operation will be performed. Otherwise, the data mart tables will be recreated.

   Note that all Validation errors need to be resolved manually.

## Managing data marts

This section describes the various options available for managing your datasets and data marts.

### Refining facts or dimensions

In the Datasets tab, you can perform various operations to refine your facts and dimensions such as creating transformation rules (for instance, replacing columns values), and adding column-level expressions. The Datasets tab is located to the right of the Data mart tab:

Datasets tab

![Datasets tab for managing fact and dimension datasets](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/datasets-tab.png)

#### Adding rules

For an explanation of how to add global rules, see [*Creating rules to transform datasets*](../Transformation/Transformation-rules.htm)

Information noteFor more information about rules as well as other operations you can perform on your datasets, see [*Managing datasets*](../Introduction/Managing-datasets.htm). Note that some of the options such as filtering and renaming datasets are not available for Data Mart data tasks.

#### Adding new columns

You can add new columns to the target dataset.

- Adding a new column from scratch

  Click + Add.

  Provide a name for the column, and set an expression to define the column data.

  For more information, see [*Adding columns to a dataset*](../Transformation/Add-columns.htm).
- Adding a column from source

  Click ![down](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to Add and select Add column from source.

  Select a column from the source dataset.

#### Reordering columns

You can change the ordinal position of a column.

1. Select a column.
2. Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then Reorder.
3. Use the arrows to move the column up or down.
4. Close Change ordinal when you are ready.

### Role-playing dimensions

A role-playing dimension is the same dimension used multiple times within the same star schema, but with different meanings. This is commonly seen with the Date and Customer dimensions. For example, your star schema might have two Date entities, one representing the Order Date and the other representing the Received Date.

To add or edit a dimension's role name:

1. Click the ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) icon in the dimension node and select Edit dimension name in this star schema.
2. In the Edit dimension name in this star schema dialog, enter a name (or edit the existing name) in the Dimension name in this star schema field and click OK.

   The new name will appear below the original dimension name.

### Additional management options

The following table describes additional management options:

| To | Do this |
| --- | --- |
| Add additional source datasets | See [*Selecting your source data*](#Selectin). |
| Add additional facts | See [*Adding a fact*](#Adding) |
| Add additional dimensions | See [*Adding dimensions and a fact to the data mart*](#Adding2). |
| Delete a dimension | Select the dimension in the Dimensions pane, and then select Delete from the menu. |
| Delete a fact | Select the fact in the Facts pane, and then select Delete from the menu. |
| Recreate a data mart | Click the  button in the top right and select Recreate tables. Recreating a data mart might be necessary if, for example, there are changes in the Storage that cannot be automatically synced to the data mart.  Information noteIf there are problems with individual tables, it is recommended to first try reloading the tables instead of recreating them. Recreating tables may cause a loss of historical data. If there are breaking changes, you must also prepare downstream data tasks that consume the recreated data tasks to reload the data. |
| Stop a running data mart task | Click the Stop button in the top right. |
| Prepare a data mart task | Click the  button in the top right and select Prepare to sync the datasets with the Transform or Storage assets and resolve any design conflicts. This prepares a task for execution. This includes:   - Validating that the design is valid. - Creating or altering the physical tables and views to match the design. - Generating the SQL code for the data task. - Creating or altering the catalog entries for the task output datasets.   You can follow the progress under Preparation progress in the lower part of the screen.  Information noteBefore you prepare a task, stop all tasks that are directly downstream. |

## Scheduling a data mart task

You can schedule a data mart task to be updated periodically. You can set a time based schedule, or set the task to run when input data tasks have completed running.

Click ... on a data task and select Scheduling to create a schedule. The default scheduling setting is inherited from the settings in the project. For more information about default settings, see [*Data mart defaults*](../Introduction/Data-project-settings.htm#Data).

You need to set Scheduling to On to enable the schedule.

### Time based schedules

You can use a time based schedule to run the task regardless of when the different input sources are updated.

- Select At specific time in Run the data task.

You can set an hourly, daily, weekly or monthly schedule.

### Event based schedules

You can use an event based schedule to run the task when input data tasks have completed running.

- Select On specific event in Run the data task.

You can select if you want to run the task when any of the input tasks have completed successfully, or when any of a selection of input tasks have completed successfully.

Information noteThe task will not run if any input task or downstream task is running when the schedule is triggered. The task is skipped until the next scheduled run.

## Reloading data

You can perform a manual reload of data. This is useful when there are issues with one or more tables.

1. Open the data task and select the Monitor tab.
2. Select the tables that you want to reload.

   When a dimension is selected for reload, all facts that use that dimension will also be reloaded to maintain integrity.
3. Click Reload tables.

You can cancel the reload for tables that are pending reload by clicking Cancel reload. This will not affect tables that are already reloaded, and reloads that are currently running will be completed.

The reload is performed by:

1. Truncating the selected dimensions and facts.
2. Loading the selected dimension tables from the upstream data task.
3. Loading the fact tables from the upstream data task. This includes:

   - Explicitly selected fact tables.
   - Fact tables that are related to a dimension that is reloaded.

Information noteIf you reload dimension x and related fact a, and then create a new fact b using dimension x as well, fact b will not be reloaded automatically. You must reload the new fact b manually.

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

## Data mart settings

Click the Settings toolbar button to open the Settings: <data-mart-name> dialog.

Warning noteIf the task has already been run, changing a setting other than Runtime settings require that you recreate the datasets.

### General settings

In the General tab, the following settings are available:

- Database: The database in which the data mart will be created
- Data task schema: The schema in which the datasets will be created
- Internal schema: The schema in which the internal datasets will be created
- Default capitalization of schema name

  You can set the default capitalization for all schema names. If your database is configured to force capitalization, this option will not have effect.
- Prefix for all tables and views

  You can set a prefix for all tables and views created with this task.

  Information noteYou must use a unique prefix when you want to use a database schema in several data tasks.
- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

  For more information about Catalog, see [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm).

### Runtime settings

In the Runtime tab, the following settings are available:

- Parallel execution: Enter the maximum number of database connections that Qlik Cloud is allowed to open for the task. The default number is 10.
- Warehouse: Only relevant for Snowflake. The name of the Snowflake data warehouse.

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

- It is not possible to change source for a dataset if facts and dimensions have been added. If you want to be flexible, you can add a preceding Transform task with non materialized views that can be used to change sources and also to have a model for all source tasks.

## Limitations

There are limitations when you use source datasets matching all these conditions:

- Created by SQL transformation or a transformation flow
- Non-materialized
- Historical Data Store (Type 2) turned off

These datasets are considered updated on every run which may affect efficiency and cost. You can mitigate this by:

- Changing the source datasets to be materialized.
- Using explicit dataset transformations.
- Creating global rules that transform multiple datasets.

### Relationships

- It is not possible to relate data from two datasets. Create a transform task where you define the relationship in the data model, and use the transform task as source for the task.
- When two datasets are related in the data model, both datasets will be available in the task, even if you only selected one of the datasets.
