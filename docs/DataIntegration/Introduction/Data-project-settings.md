---
title: "Data pipeline project settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-project-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects"]
---

# Data pipeline project settings

You can change the settings for a data pipeline project in Qlik Talend Data Integration. The properties are common to the project and all included data tasks. Some settings are only available for specific data platforms.

- Click Settings in the project.

## Settings for data warehouse data pipeline projects

### Data platform

You can change the following settings:

- Connection

  Connection for the project.
- Connection to staging area

  This option is not available when the data platform is Snowflake.

Information noteIt is not possible to change the platform type of a project, for example, from Snowflake to Google BigQuery.

### Metadata

You can set a suffix for internal artifacts and default suffixes for views that are created.

- Artifacts preferences

  - Prefix for all schemas: The prefix to add to data schemas that are created in the project. This is useful when an imported project is in the same cloud data warehouse as an exported project.
  - Suffix for internal schema: The suffix to be used for schemas used to store internal artifacts.
  - Default capitalization of schema name: The default capitalization for all schema names. If your database is configured to force capitalization, this option will not have effect.
- Suffixes for external views

  Set default suffixes for views that are created in data tasks included in the project.

### Default settings for new tasks

You can set default values for data tasks that are created in the project. When you create a data task you can change the value.

You can set the default database to create target artifacts for all types of data tasks.

#### Landing task defaults

Default database

You can use the default database of the project or specify another database.

Accessing the target via a proxy when using Data Movement gateway

Information noteThis option is only available when accessing targets via Data Movement gateway.

- When using Data Movement gateway, connect via proxy to

  When using Data Movement gateway, you can connect to the target platform and the staging platform (area) via a proxy.

  For more information about configuring Data Movement gateway to use a proxy server, see [*Setting the Qlik Cloud tenant and a proxy server*](../../Gateways/dm-gateway-setting-up.htm#Setting).

  - Target platform

    Information noteAvailable when using Snowflake, Google BigQuery, and Databricks.
  - Staging platform

    Information noteAvailable when using Azure Synapse Analytics, Amazon Redshift, and Databricks.

#### Storage task defaults

- Historical Data Store (Type 2)

  You can keep historical change data to let you easily recreate data as it looked at a specific point in time. You can use history views and live history views to see the historical data.
- Live views

  Live views show a view for each selected source table which merges the table with changes from the change table. This provides queries with a live view of the data without having to wait for the next apply cycle.

Default database

You can use the default database of the project or specify another database.

Catalog

- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

Default view type

Information noteAvailable when using the Snowflake data platform only.

- Standard views

  Use standard views to display the results of a query as if it were a table.
- Snowflake secure views

  Use Snowflake secure views for views designated for data privacy or sensitive information protection, such as views created to limit access to sensitive data that should not be exposed to all users of the underlying tables.
  Snowflake secure views can execute more slowly than Standard views.

#### Registered data task defaults

Default database

You can use the default database of the project or specify another database.

Catalog

- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

Incremental load settings

These settings are available when Incremental using high watermark is selected.

- Change tables

  If the changes are in the same table, select Changes are within the same table.

  If not, clear Changes are within the same table and specify a change table pattern.
- Watermark column

  Set the name of the watermark column in Name.
- "From date" column

  You can indicate the "From date" by the start time, or using a selected column.

  If you select Selected "From date" column, you must define a "From date" pattern.
- Soft deletions

  You can include soft deletions in changes by selecting Changes include soft deletions and defining an indication expression.

  The indication expression should evaluate to True if the change is a soft delete.

  Example: ${is\_deleted} = 1
- Before image

  You can filter out before image records in change tables changes by selecting Before image and defining an indication expression.

  The indication expression should evaluate to True if the row contains the image before the update.

  Example: ${header\_\_change\_oper} = 'B'

#### Transform task defaults

- Historical Data Store (Type 2)

  You can keep historical change data to let you easily recreate data as it looked at a specific point in time. You can use history views and live history views to see the historical data.

Materialization

- Non-materialized (Views only)

  Select this option to only create views that perform transformations on the fly.
- Materialized (Tables and Views)

  Select this option to create both tables and views.

Default database

You can use the default database of the project or specify another database.

Catalog

- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

Default view type

Information noteAvailable when using the Snowflake data platform only.

- Standard views

  Use standard views to display the results of a query as if it were a table.
- Snowflake secure views

  Use Snowflake secure views for views designated for data privacy or sensitive information protection, such as views created to limit access to sensitive data that should not be exposed to all users of the underlying tables.
  Snowflake secure views can execute more slowly than Standard views.

Default table type

Information noteAvailable when using the Snowflake data platform only.

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

#### Data mart task defaults

Default database

You can use the default database of the project or specify another database.

Catalog

- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

#### Runtime defaults

You can define default runtime performance settings for data assets that are included in the project.

Landing defaults

- You can set the maximum number of database connections in Parallel execution.

Storage defaults

- You can set default scheduling settings to a time based schedule. This will be the default value for each storage task created.
- You can set the default data warehouse if the project platform is Snowflake.

Transform defaults

- You can set default scheduling settings to a time based schedule or On successful completion of any input data task. This will be the default value for each transformation task created.
- You can set the default data warehouse if the project platform is Snowflake.

Data mart defaults

- You can set default scheduling settings to a time based schedule or On successful completion of any input data task. This will be the default value for each data mart task created.
- You can set the default data warehouse if the project platform is Snowflake.

Mirror defaults

- You can set the default data warehouse if the project platform is Snowflake.

## Settings for Qlik Open Lakehouse data pipeline projects

### Data platform

You can change the following settings:

- Data catalog connection: Select an existing connection or click Create new to add a new data catalog connection.
  You can also edit an existing connection and verify that the connection
  works by clicking Test connection.
- Landing target connection: Select the S3 bucket for landing the data or click Create new to add a new bucket location. You can also edit an existing connection and verify that the connection
  works by clicking Test connection.

Information noteIt is not possible to change the platform type of a project, for example, from Snowflake to Google BigQuery.

### Metadata

You can set a suffix for internal artifacts and default suffixes for views that are created.

- Artifacts preferences

  - Prefix for all schemas: The prefix to add to data schemas that are created in the project. This is useful when an imported project is in the same cloud data warehouse as an exported project.
  - Suffix for internal schema: The suffix to be used for schemas used to store internal artifacts.
  - Default capitalization of schema name: The default capitalization for all schema names. If your database is configured to force capitalization, this option will not have effect.
- Suffixes for external views

  Set default suffixes for views that are created in data tasks included in the project.

- Hash

  You can set a hash salt string to be used when hashing a column, for example to mask sensitive information. This will generate a SHA-256 hash of the input column after concatenating it with the hash salt string.

  You can either use the project ID as salt string, or set a custom salt string.

### Default settings for new tasks

You can set default values for data tasks that are created in the project. When you create a data task you can change the value.

You can set the default database to create target artifacts for all types of data tasks.

#### Lake landing task defaults

Folder to use

Select one of the following, according to which bucket folder you want the files to be written to:

- Default folder

  The default folder format is <your-project-name>/<your-task-name>
- Root folder

  The files will be written to the root bucket folder.
- Folder

  Specify a folder name. The folder will be created during the data task if it does not already exist.

  Information note The folder name cannot include special characters (for example, @, #, !, and so on).

#### Storage task defaults

- Historical Data Store (Type 2)

  You can keep historical change data to let you easily recreate data as it looked at a specific point in time. You can use history views and live history views to see the historical data.

Catalog

- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

Folder to use in staging area

Select one of the following, according to which bucket folder you want the files to be written to:

- Default folder

  The default folder format is <your-project-name>/<your-task-name>
- Root folder

  The files will be written to the root bucket folder.
- Folder

  Specify a folder name. The folder will be created during the data task if it does not already exist.

  Information note The folder name cannot include special characters (for example, @, #, !, and so on).

#### Streaming landing task defaults

You can set default values for Streaming landing tasks created in the project.

Folder to use

Select one of the following, according to which bucket folder you want the files to be written to:

- Default folder

  The default folder format is <your-project-name>/<your-task-name>
- Root folder

  The files will be written to the root bucket folder.
- Folder

  Specify a folder name. The folder will be created during the data task if it does not already exist.

  Information note The folder name cannot include special characters (for example, @, #, !, and so on).

Folder retention

Select how long to retain the data:

- Data and metadata are not deleted

  Neither the data nor the metadata are deleted.
- Delete data and metadata after the retention period

  Data and metadata are deleted after the retention period has elapsed.
- Delete metadata after the retention period. The data is deleted by external system.

  The metadata is purged after this period elapses. The underlying data, for example the S3 object, is not deleted by Qlik but is deleted by an external system.

#### Streaming transform task defaults

You can set default values for Streaming Transform tasks created in the project.

Catalog

- Publish to catalog

  Select this option to publish this version of the data to Catalog as a dataset. The Catalog content will be updated the next time you prepare this task.

Folder to use

Select one of the following, according to which bucket folder you want the files to be written to:

- Default folder

  The default folder format is <your-project-name>/<your-task-name>
- Root folder

  The files will be written to the root bucket folder.
- Folder

  Specify a folder name. The folder will be created during the data task if it does not already exist.

  Information note The folder name cannot include special characters (for example, @, #, !, and so on).

Table definitions

Configure the standard view header columns that appear by default in standard views for all Streaming Transform tasks in this project.

- hdr\_\_from\_timestamp

  When this option is enabled, the hdr\_\_from\_timestamp header column will appear in standard views. In addition, when Partition by event ingestion date is selected in the onboarding wizard, hdr\_\_from\_timestamp will be used as the default partition column. You can override this setting at the task or dataset level.

  Information noteHistory views always include all standard view header columns, regardless of this setting.

### Runtime

You can define default runtime performance settings for data tasks that are included in the project.

#### Lake landing task defaults

- You can set the maximum number of database connections in Parallel execution.

#### Storage task defaults

Lakehouse cluster

Optionally, choose a dedicated [Lakehouse cluster](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-cluster.htm) for storage tasks.

#### Streaming landing task defaults

Number of readers

Select the number of readers to use. The value must be between 1 and 1,000.

Lakehouse cluster

Optionally, choose a dedicated [Lakehouse cluster](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-cluster.htm) for storage tasks.

#### Streaming transform task defaults

Lakehouse cluster

Optionally, choose a dedicated [Lakehouse cluster](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-cluster.htm) for storage tasks.

Mirror defaults

- You can set the default data warehouse if the project platform is Snowflake.
