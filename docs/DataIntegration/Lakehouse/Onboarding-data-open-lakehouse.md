---
title: "Onboarding data to Qlik Open Lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/Onboarding-data-open-lakehouse.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects"]
---

# Onboarding data to Qlik Open Lakehouse

Qlik Open Lakehouse facilitates data movement from any supported source to Apache Iceberg tables. The Iceberg open table format offers interoperability between apps and data platforms, enabling data to be read from a variety of tools, reducing the need to duplicate data. You can mirror tables in your Qlik Open Lakehouse projects to your cloud data warehouse, and users can query data directly your cloud data warehouse.

To onboard data to Qlik Open Lakehouse and store data in Iceberg format tables, you start by establishing a network integration to your AWS VPC. This integration enables Qlik to securely provision and manage resources within your cloud environment. Next, you create a lakehouse cluster to provide a compute environment for processing and storing your data. The final step of the preparation is to set up a data catalog connection to a centralized metadata repository.

You can create a data pipelines using Qlik Open Lakehouse projects when these components are configured. Data pipelines ingest your data and store it in Iceberg tables. You can access and query your Iceberg tables from a wide range of tools, including directly from your cloud data warehouse.

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## [*Qlik Open Lakehouse architecture*](lakehouse-pipeline-architecture.htm)

With Qlik Open Lakehouse you can create a scalable, high-performing lakehouse using the Iceberg open table format.

## [*Setting up Qlik Open Lakehouse*](Onboarding-open-lakehouse-setup.htm)

Configure your cloud environment with a network integration and lakehouse cluster to run Qlik Open Lakehouse projects.

## [Creating a Qlik Open Lakehouse project](creating-project.htm)

Create a project to onboard data to Iceberg open table format storage, and optionally mirror tables to your cloud data warehouse without data duplication.
