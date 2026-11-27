---
title: "Landing data to a lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/Lake-landing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Landing data to a lakehouse

You can land data to a Snowflake data lakehouse. This involves transferring the data from the data source to cloud file storage that is managed by the data platform.

Landing data to a lakehouse does not involve costly warehouse usage while landing the data, compared with regular landing to a data warehouse. This allows you to land in high frequency, and to consume in lower frequency on a need basis. You may also be able to share data with other platforms more easily. You can sync Iceberg tables with Snowflake Open Catalog to enable interoperability with other tools, such as Apache Spark.

Landing data to a lakehouse is only available in projects with Snowflake as data platform.

## Preparations

- If you want to sync Iceberg tables with Snowflake Open Catalog, you must set up a catalog integration in your Snowflake instance. The name of this integration is needed when creating the task. For more information, see [CREATE CATALOG INTEGRATION (Snowflake Open Catalog)](https://docs.snowflake.com/en/sql-reference/sql/create-catalog-integration-open-catalog).
- Although you can configure your source and target connection settings in the task setup wizard, to simplify the setup procedure, it is recommended to do this before you create the task.

## Creating a Lake landing task

1. Create a project, and select Data pipeline in Use case.
2. Select Snowflake in Data platform and set up a connection to the data warehouse.

   For more information about settings for the Snowflake target, see [*Snowflake*](../TargetConnections/snowflake-target.htm) .
3. Select Cloud storage in Landing target.
4. Set up a staging area in Cloud storage connection.

   You can use the following types of connections:

   - [*Amazon S3*](../TargetConnections/aws-s3-target.htm)
   - [*Azure Data Lake Storage*](../TargetConnections/adls-target.htm)
   - [*Google Cloud Storage*](../TargetConnections/google-storage-target.htm)
5. Set the name of the Snowflake storage integration. For more information, see Snowflake documentation for your selected storage area.
6. Select which table type to create by default for Storage, Transform, and Data mart tasks. This setting can be changed later in project settings. You can also set the table type for each individual task in the project.

   - Snowflake tables
   - Snowflake-managed Iceberg tables

     In this case, you must set the default name of the external volume in Default external volume.

     Information noteIceberg tables will inherit the storage serialization policy set at the schema, database, or account level. This can affect interoperability with other products reading tables directly through Snowflake.
7. Click Create to create the project.

When you onboard data or create a landing task in the project, a Lake landing task is created instead of a Landing task. Lake landing tasks operate and behave mostly like Landing tasks, except for the fact that they land data to cloud storage. For more information, see [*Landing data from data sources*](Landing-data-data-sources.htm).

All files are landed in the CSV format. The storage task that consumes the landing task will make sure that external tables are updated after landing data is updated.

## Deleting a task

You can delete the data task if it is not running, and there are no dependencies to downstream tasks in the same project.

- In Pipeline project view of the project, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Delete.

Artifacts (files) created by the task will not be deleted.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Settings

For more information about task settings, see [*Lake landing settings*](Lake-Landing-settings.htm).

## Limitations

- It is not possible to alter a table path after it has been created. This includes renaming the table.
- If landing tables are used as external tables, storage live views are disabled.
- When syncing tables with Snowflake Open Catalog, the internal schema tables are synced, and not the views generated in the data task schema. This limitation may be lifted in the future. For more information about internal schema tables, see [*Tables*](../Storage/dataset-tables.htm#Tables).
- Source columns of type CLOB and BLOB will be set as nullable by default, even if marked as non-nullable in the source. You can change it to be non-nullable, but then you need to add an expression to add a non-null value in case it arrives as null from the source. This can happen on deleted records.
