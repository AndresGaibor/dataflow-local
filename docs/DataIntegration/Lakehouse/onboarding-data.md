---
title: "Onboarding data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/onboarding-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project"]
---

# Onboarding data

The first step of creating a data pipeline in a Qlik Open Lakehouse project is onboarding the data. This process involves transferring data from the source and storing datasets in optimized Iceberg tables.

Onboarding is created in a single operation, but performed in two steps. The data source type, either CDC or streaming, determines the tasks in your project:

### CDC sources

- Landing the data

  This involves transferring the data in continuous mini-batches from the on-premises data source to a landing area, using a Landing data task.

  [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm)

  You can also land data to a lakehouse, where the data is landed to S3 file storage.

  [*Landing data to Qlik Open Lakehouse*](landing-data.htm)
- Storing datasets

  This involves reading the initial load of landing data or incremental loads, and applying the data in read-optimized format using a Storage data task.

  [*Storing datasets*](storing-data.htm)

### Streaming sources

- Landing the data

  This involves continuously streaming the data from the source to a landing area, using a Streaming landing data task.

  [*Landing streaming data to Qlik Open Lakehouse*](landing-data-streaming.htm)
- Storing datasets

  This involves reading the initial load of landing data, and applying the data in read-optimized format using a Storage Transform data task.

  [*Storing streaming datasets*](storing-data-streaming.htm)

## Using onboarded data

When you have onboarded the data, you can use the stored datasets in several ways, including:

- You can use the datasets in an analytics application.
- You can mirror data to one or more cloud data warehouses, including Amazon Redshift and Snowflake, by adding a Mirror data task directly to the Storage data task for CDC sources, or the Streaming Transform task for streaming sources.

  For more information, see [*Mirroring data to a cloud data warehouse*](mirroring-data.htm).
- You can transform data in your cloud data warehouse by creating a cross-project pipeline that consumes data from your onboarding project.
