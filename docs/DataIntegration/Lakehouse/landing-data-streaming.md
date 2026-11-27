---
title: "Landing streaming data to Qlik Open Lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/landing-data-streaming.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data", "Streaming data"]
---

# Landing streaming data to Qlik Open Lakehouse

You can land data from a streaming source in Amazon S3 or Google Cloud Storage, ready for the Streaming Transform task to convert it into the Iceberg open table format.

Landing streaming data to a Qlik Open Lakehouse requires a preconfigured bucket in the cloud storage service for your project. Qlik Open Lakehouse supports high-volume streaming sources. For more information, see [*Connecting to data streams*](../SourcesConnections/Connecting-Data-Streams.htm).

Raw data lands in Avro format in the configured bucket. In AWS, the bucket is in Amazon S3. In GCP, it is in Google Cloud Storage. The Streaming Transform task converts the data to Iceberg format. You can optionally mirror the tables to a cloud data warehouse, including BigQuery for GCP projects, without duplicating the data.

## Preparations

- Make sure that you have set up Qlik Open Lakehouse. This includes creating a network integration, a lakehouse cluster, and source and target connections. For more information, see [*Setting up Qlik Open Lakehouse*](Onboarding-open-lakehouse-setup.htm).
- To mirror data to your cloud data warehouse, you must first create a Qlik Open Lakehouse project to ingest your data and store it using the Iceberg open table format. You can add a Mirror data task after the Streaming Transformation task. For more information, see [*Mirroring data to a cloud data warehouse*](mirroring-data.htm).

## Creating a Streaming landing task

To create a Streaming landing task, do the following to first create the project:

1. Create a project, and select Data pipeline in Use case.
2. Select Qlik Open Lakehouse in Data platform and establish a connection to the data catalog.
3. Set up a storage area in Landing target connection. Select an Amazon S3 bucket for AWS or a Google Cloud Storage bucket for GCP.
4. Click Create to create the project.

When you onboard data or create a landing task in the project, a Streaming landing task is created instead of a Landing task. Streaming landing tasks operate and behave similar to a Landing task, except that they land data to cloud storage from streaming sources. For more information, see [*Connecting to data streams*](../SourcesConnections/Connecting-Data-Streams.htm).

All files are landed in Avro format. After landing data is updated, the Streaming Transformation task consumes the landing data and updates the external tables.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Operations

The following operations are available in a streaming landing task:

- Dropping a column

  Select the column and click Remove.

  This will add a transformation rule that removes the column from newly loaded data after the task is prepared and run. You can restore the column for new records by deleting the transformation rule.
- Hashing a column, for example to mask sensitive information.

  Select Hash in the column.

  This will generate a SHA-256 hash of the input column after concatenating it with a hash salt string. You set the hash salt string in the project settings under Metadata > Hash. This setting is only available in Qlik Open Lakehouse projects. For more information, see [*Metadata*](../Introduction/Data-project-settings.htm#Metadata)

  Data type is changed to String when a column is hashed. If you want to keep non-hashed data as well for privileged users, perform the hash later in a Transform task.
- Filtering data

  For more information, see [*Filtering a dataset*](../Transformation/Filter-data.htm).
- Renaming a dataset

  Click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the dataset and select Rename.

## Deleting a task

You can delete the data task if it is not running, and there are no dependencies to downstream tasks in the same project.

- In Pipeline project view of the project, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Delete.

Artifacts (tables and views) created by the task will also be deleted, unless you select to keep them.

Information noteKeep in mind that the artifacts you keep will no longer be updated by the task.

## Settings

For more information about task settings, see [*Streaming lake landing settings*](landing-data-settings-streaming.htm)
