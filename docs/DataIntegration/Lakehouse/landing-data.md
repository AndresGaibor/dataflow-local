---
title: "Landing data to Qlik Open Lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/landing-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "CDC data"]
---

# Landing data to Qlik Open Lakehouse

Data lands in Amazon S3 or Cloud Storage, ready for the storage data task to convert it into the Iceberg open table format. You can land data from any source supported by Qlik.

Landing data to a Qlik Open Lakehouse requires a pre-configured Amazon S3 or Cloud Storage bucket. Qlik Open Lakehouse is compatible with all Qlik-supported data sources. Data lands in CSV format. The Storage data task converts the data to Iceberg format and copies it to Parquet files. You can query Iceberg data using an engine that supports the Iceberg table format. You can also mirror tables to a supported cloud data warehouse without duplicating data.

Landing data to a Qlik Open Lakehouse is available in projects with an [AWS Glue Data Catalog](../TargetConnections/aws-glue-data-catalog.htm) or [Google Lakehouse runtime catalog](../TargetConnections/google-biglake-catalog.htm) target connection.

## Preparations

- To mirror data to your cloud data warehouse, you must first create a Qlik Open Lakehouse project to ingest your data and store it using the Iceberg open table format. You can add a Mirror data task after the Storage data task. To perform data transformations, create a Redshift or Snowflake project that uses the Qlik Open Lakehouse project as the source. For more information, see [*Mirroring data to a cloud data warehouse*](mirroring-data.htm).
- Although you can configure your source and target connection settings in the task setup wizard, to simplify the setup procedure, it is recommended to do this before you create the task.

## Creating a Lake landing task

To create a lake landing task, do the following:

1. Create a project, and select Data pipeline in Use case.
2. Select Qlik Open Lakehouse in Data platform and establish a connection to the data catalog.
3. Set up a storage area in Landing target connection.
4. Click Create to create the project.

When you onboard data or create a landing task in the project, a Lake landing task is created instead of a Landing task. Lake landing tasks operate and behave mostly like Landing tasks, except for the fact that they land data to cloud storage. For more information, see [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm).

All files are landed in CSV format. After landing data is updated, the storage task that consumes the landing task updates the external tables.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Settings

For more information about task settings, see [*Lake landing settings*](landing-data-settings.htm).

## Limitations

- Landed data is not partitioned in the bucket due to the storage task running every minute. Therefore the data partition frequency cannot be updated in the task settings.
- Although landing data from SaaS sources is scheduled, the storage task runs mini-batches every minute. This requires an active lakehouse cluster at minimal cost.
- If a Primary Key value changes, records with the original key are marked as Deleted, and the row containing the changed key value is marked as Insert.
