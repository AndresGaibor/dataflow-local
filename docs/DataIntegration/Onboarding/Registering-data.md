---
title: "Registering data that is already on the data platform"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Onboarding/Registering-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Registering data that is already on the data platform

You can register data that already exists on the data platform to curate and transform data, and create data marts. This lets you use data that is onboarded with other tools than Qlik Talend Data Integration, for example, Qlik Replicate.

When you register data, two data tasks are created.

- Registered data

  Registering the data involves creating views to prepare the data to be ready for creating datasets.
- Storage

  This involves generating and storing datasets based on the registered data.

  [*Storing datasets*](../Storage/generating-datasets.htm)

When you have registered the data, you can use the generated datasets in several ways.

- You can use the datasets in an analytics application.
- You can create transformations.
- You can create a data mart.

## Register data

You can register data that exists in the cloud data warehouse defined in the project. The generated datasets will be stored in the same cloud data warehouse.

For more information about projects, see [*Creating and managing data pipeline projects*](../Introduction/Data-projects.htm).

1. Click Create and then Register data in a project.
2. Add Name and Description for the data task.

   Click Next.
3. Select data to register.

   [*Selecting data to include*](#Selectin)

   Click Next.

   Settings is displayed.
4. Select how the data is updated in Update method.

   Select Incremental using high watermark if the data is replicated by Qlik Replicate.

   - Use Incremental using high watermark to process data changes incrementally using a high watermark pattern. This is the suggested method if the data is replicated by Qlik Replicate (with Full load and store changes enabled).

     For more information, see [*Update method*](#Loading).
   - Use Compare with current storage when the data was only loaded once, or if it is updated using full reloads.
5. Preview the two data tasks that are created in Summary, and rename them if you prefer.

   Tip noteThe names are used when naming database schemas in the storage data task. As a schema can only be associated with one task, consider using names that are unique to avoid conflicts with data tasks in other projects using the same data platform.
6. Select if you want to open the registered data task, or return to the project.

   When you are ready, Click Finish.

The two data tasks are now created. To start replicating data you need to:

- Prepare the registered data task.

  Click Prepare in the data task.

  When artifacts have been created, the data task status is Registered.
- Prepare and run the storage data task.

  For more information, see [*Storing datasets*](../Storage/generating-datasets.htm)

## Selecting data to include

When you select data to include, you can select specific tables or views, or use selection rules to include or exclude groups of tables.

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

## Registered data settings

You can set properties for the registered data task.

- Click Settings.

### General settings

- Database

  Database to use in the target.
- Task schema

  You can change the name of the schema of the data task.
- Prefix for all tables and views

  You can set a prefix for all tables and views created with this task.

  Information noteYou must use a unique prefix when you want to use a database schema in several data tasks.
- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

  For more information about Catalog, see [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm).

### Update method

#### Change detection

- Use Compare with current storage when the data was only loaded once, or if it is updated using full reloads.
- Use Incremental using high watermark to process data changes incrementally using the high watermark method.

  This option requires that all tables have a primary key defined. You can define a primary key manually in the Datasets view for tables that are missing a primary key.

#### Incremental load settings

These settings are available when Incremental using high watermark is selected.

- If the data is replicated by a Qlik Replicate task with Full load and store changes, set Incremental load settings to Qlik Replicate settings.
- Otherwise, set Incremental load settings to Custom and define the settings yourself.

Incremental load settings

| Setting | Custom | Qlik Replicate settings |
| --- | --- | --- |
| Change tables | If the changes are in the same table, select Changes are within the same table.  If not, deselect Changes are within the same table and specify a change table pattern in Change table pattern. | ${SOURCE\_TABLE\_NAME}\_\_ct table |
| Watermark column | Set the name of the watermark column in Name. | header\_\_change\_seq |
| "From date" column | You can indicate the "From date" by the batch start time, or using a selected column.  If you select Selected "From date" column, you must define a "From date" pattern. | header\_\_timestamp |
| Soft deletions | You can include soft deletions in changes by selecting Changes include soft deletions and defining an indication expression.  The indication expression should evaluate to True if the change is a soft delete.  Example: ${is\_deleted} = 1 | ${header\_\_change\_oper} = 'D' |
| Before image | You can filter out before image records in change tables changes by selecting Before image and defining an indication expression.  The indication expression should evaluate to True if the row contains the image before the update.  Example: ${header\_\_change\_oper} = 'B' | ${header\_\_change\_oper} = 'B' |

## Recommended Qlik Replicate configuration

These Qlik Replicate task settings are recommended when registering data that is replicated using a Qlik Replicate task storing changes.

- The Qlik Replicate task should be configured with options Full Load and Store Changes.
- In Store Changes Settings > Change Tables, make sure that the following change table columns are included, using their default names:

  - [header\_\_]change\_seq
  - [header\_\_]change\_oper
  - [header\_\_] timestamp
- In Store Changes Settings > Change Tables, set On UPDATE to Store after image only.

  This reduces the space for each update as the before image is not included. Use this option if you do not plan to use the before image.
- In Store Changes Settings > Change Tables, set Suffix to the default value \_\_ct.
- Do not apply the following global transformations:

  - Rename Change Table
  - Rename Change Table Schema
- If a primary key in a source table can be updated, enable DELETE and INSERT when updating a primary key column option in Change Processing Tuning.

  History of the old record will not be preserved in the new record.

  Information noteThis option is supported from Qlik Replicate November 2022 .

## Operations on the registered data task

You can perform the following operations on a registered data task from the task menu.

- Open

  This opens the data task. You can view the table structure and details about the data task.
- Edit

  You can edit the name and the description of the task, and add tags.
- Delete

  You can delete the data task.

  The source data is not deleted.
- Sync datasets

  This syncs design changes that cannot be automatically adjusted.
- Recreate tables

  This recreates the datasets from the source.

  Information noteIf there are problems with individual tables, it is recommended to first try reloading the tables instead of recreating them. Recreating tables may cause a loss of historical data. If there are breaking changes, you must also prepare downstream data tasks that consume the recreated data tasks to reload the data.
- Store data

  You can create a storage data task that uses data from this landing data task.

## History considerations when setting a "From date" column

If historical data is enabled in a downstream task, and you use a "From date" column, backdating is not supported. This means that if a change batch contains an older version of a record that does not exist in storage, the change batch must also include all newer versions of the record. If the newer versions are not included, they will be deleted.

In these examples, storage contains these records from the start:

| From date | Name | City |
| --- | --- | --- |
| 2/Oct/2023 | Joe | New York |
| 3/Oct/2023 | Joe | London |

Example 1:

If you insert the following change batch:

| From date | Name | City |
| --- | --- | --- |
| 4/Oct/2023 | Joe | Paris |

The result in storage is, as expected:

| From date | Name | City |
| --- | --- | --- |
| 2/Oct/2023 | Joe | New York |
| 3/Oct/2023 | Joe | London |
| 4/Oct/2023 | Joe | Paris |

Example 2:

But if you insert the following older record in a change batch:

| From date | Name | City |
| --- | --- | --- |
| 1/Oct/2023 | Joe | Berlin |

This results in the newer records being removed in storage:

| From date | Name | City |
| --- | --- | --- |
| 1/Oct/2023 | Joe | Berlin |

Example 3:

To maintain the history, the change batch must include the newer records:

| From date | Name | City |
| --- | --- | --- |
| 1/Oct/2023 | Joe | Berlin |
| 2/Oct/2023 | Joe | New York |
| 3/Oct/2023 | Joe | London |

This will ensure the history is maintained in storage as well:

| From date | Name | City |
| --- | --- | --- |
| 1/Oct/2023 | Joe | Berlin |
| 2/Oct/2023 | Joe | New York |
| 3/Oct/2023 | Joe | London |

## Considerations

- Use the options to keep historical data in Qlik Talend Data Integration.
- Columns using any of the data types VARIANT, JSON, and SUPER will be converted to JSON.
- Data Movement gateway 2024.11.78 or higher is required to discover JSON data type if you are using a client-managed gateway.

## Data capacity considerations

- If a registered table has no primary key, a full reload will be executed for every run. This will be counted towards your monthly registered data capacity quota. This is because the storage will need to compare all records to find changes.
- Data capacity for registered data is counted in the storage. This means a delete in the registered data is translated to an insert or update of the storage (a soft delete) and counted in the data capacity.
- Soft deletes, inserts, and updates will be counted twice towards data capacity if a table from registered data is used in two storage data tasks.
