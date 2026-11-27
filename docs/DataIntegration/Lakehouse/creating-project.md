---
title: "Creating a Qlik Open Lakehouse project"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/creating-project.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse"]
---

# Creating a Qlik Open Lakehouse project

Create a Qlik Open Lakehouse pipeline project to ingest data from supported sources and store it in Iceberg open table format.

## Prerequisites

To create a Qlik Open Lakehouse project, you need:

- A network integration to enable Qlik to provision and manage compute resources on your behalf.
- A lakehouse cluster configured to run the data storage task within your Iceberg project.
- A connection to a data catalog to use as the data target for your project, or the necessary details so you can create a new connection.

## Supported tasks

The following tasks are supported in a Qlik Open Lakehouse project.

For GCP, the supported workflow is CDC ingestion through Lake landing and Storage data tasks, followed by a Mirror data task to BigQuery. The streaming workflow described below applies to existing AWS projects.

### CDC and SaaS application sources

- Lake landing data task

  Land data in CSV format in Amazon S3 or Cloud Storage, from any Qlik-supported source, including high-volume data streams.

  For more information, see [*Landing data to Qlik Open Lakehouse*](landing-data.htm).
- Storage data task

  The Storage data task consumes data landed in the cloud by the Lake landing task. The task writes data to Iceberg tables for efficient storage and querying.
- For more information, see [*Storing datasets*](storing-data.htm).
- Mirror data task

  Mirror Iceberg tables from your storage task to your cloud data warehouse. For GCP, mirror tables to BigQuery. Users can query data via external tables without migrating data to your cloud data warehouse.

### Streaming sources

In GCP, supported streaming sources are Apache Kafka and Google Cloud Storage. Streaming data lands in Cloud Storage before the Streaming Transform task writes it to Iceberg.

- Streaming landing data task

  Land data in Avro format in Amazon S3 in AWS or Google Cloud Storage in GCP.

  For more information, see [*Landing streaming data to Qlik Open Lakehouse*](landing-data-streaming.htm)
- Streaming Transform data task

  The Streaming Transform data task consumes events landed in the cloud by the Streaming landing task. The task writes data to Iceberg tables for efficient storage and querying and supports transformations.

  For more information, see [*Storing streaming datasets*](storing-data-streaming.htm).
- Mirror data task

  Mirror Iceberg tables from your Streaming Transform task to your cloud data warehouse. In GCP, you can mirror tables to BigQuery.

## Example of creating a Qlik Open Lakehouse project

The following example creates a Qlik Open Lakehouse pipeline project, onboards data from a CDC source, and stores it in Iceberg format tables. This example creates a simple pipeline that you could expand by onboarding more data sources. You could add a Mirror data task to mirror your tables in your data warehouse without duplicating data, or use this project as the source for a project that requires transformations in your cloud data warehouse.

To create a Qlik Open Lakehouse project, do the following:

1. In Data Integration home, click Create pipeline, and configure it:

   - Name: Enter the name for the project.
   - Space: Select the space the project will belong to.
   - Description: Optionally, enter a description for the project.
2. For Use case, select Data pipeline.
3. Configure the Data platform:

   - Data platform: Select Qlik Open Lakehouse from the list.
   - Data catalog connection: Select an existing connection, such as AWS Glue Data Catalog or Google Lakehouse runtime catalog, or click Create new.
   - Landing target connection: Select an Amazon S3 bucket for AWS or a Google Cloud Storage bucket for GCP, or click Create new.
   - Storage compute cluster: Select the lakehouse cluster that will run the storage task.
4. Create the project.
5. Follow the steps in the onboarding data wizard. For more information, see [*Onboarding data*](onboarding-data.htm), which provides instructions for CDC and streaming sources.

## Limitations

- If you recreate a task, you must also recreate all downstream tasks.

### Limitations in GCP

The following limitations apply to Qlik Open Lakehouse projects in GCP:

- Google Cloud does not support renaming tables. If you rename a table, the table is recreated with the new name when you click Prepare.
- Google Cloud does not support the `ARRAY<ARRAY<>>` and `ARRAY<MAP<>>` data types. If your data contains these data types, transform the data to a supported data type.

  If your data contains a `STRUCT` data type, make sure that the struct does not contain fields with unsupported data types or unsupported characters.
