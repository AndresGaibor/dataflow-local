---
title: "System requirements and limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Deploying/System-requirements-data-services.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Getting started with Qlik Talend Data Integration"]
---

# System requirements and limitations

This section describes requirements and limitations for Qlik Talend Cloud.

Before you start, you should review the requirements to make sure that you have everything needed to get started.

You can read more about the workflow and system components in [*Integrating data*](../Introduction/Data-services.htm)

## General requirements for Qlik Talend Cloud

- Tenant on Qlik Cloud with access to Qlik Talend Data Integration. This requires either of these subscriptions:

  - Qlik Talend Cloud for managing data integration projects.

    Qlik Talend Cloud is available in subscription options from four tiers: Starter, Standard, Premium, and Enterprise. The higher editions provide more advanced data sources and transformations. This includes capabilities hosted on Qlik Cloud and Talend Cloud. All subscriptions include [*Qlik Cloud Analytics Standard*](../../Admin/subscription-options-analytics.htm#_bm2).
  - Qlik Cloud Analytics subscription allows access to Qlik Talend Data Integration for creating QVD files in a Qlik Cloud data platform. The QVD files can be used in analytics applications.

    For more information, see [*Qlik Cloud Analytics subscription options*](../../Admin/subscription-options-analytics.htm).
- Users must have the Data Services Contributor role to create, manage, and run data tasks in Qlik Talend Data Integration. For user-based subscriptions, the user must also have Professional user entitlement.
- Qlik Cloud Government noteAlthough the Qlik Talend Data Integration interface and tooling is available in Qlik Cloud Government, it is not functional without a license except for the ability to create data pipelines.
- Talend Studio 8.0.1 R2024-05 or higher is required to use Talend Studio capabilities with a Qlik Talend Cloud Premium or Qlik Talend Cloud Enterprise license.
- When you connect to data sources you may need to add underlying Qlik Cloud IP addresses to your allowlist.

  For more information, see [*Allowlisting domains and IP addresses*](../../Introduction/qlik-cloud-dns-ip.htm).
- Connections are used to connect to cloud data platforms for data delivery and push-down transformations. For more information, see [*Setting up connections to targets*](../TargetConnections/data-project-connections.htm#Data).
- If you are using Data Movement gateway, the drivers required to access your data source and your target platform need to be installed on the Data Movement gateway machine. If you are using one Data Movement gateway to access the source and another to access the target, then install the driver(s) needed to access the target on the target Data Movement gateway and the driver needed to access your data source on the source Data Movement gateway.

  For more information, see [*Setting up connections to targets*](../TargetConnections/data-project-connections.htm#top).

## Requirements for storing data

- If you land data to an Amazon S3 bucket, you can generate QVD tables in Qlik Cloud managed storage, or in Amazon S3 storage managed by you.
- If you land data to a cloud data warehouse, such as Snowflake or Azure Synapse Analytics, you can generate tables in the same cloud data warehouse.
- If you land data from a cloud data source to a cloud data warehouse, you can generate tables in the same cloud data warehouse.

### Requirements for staging areas

You need a staging area for moving data to some data warehouse targets:

- Azure Synapse Analytics

  You need an Azure Data Lake Storage staging area.
- Google BigQuery

  You need a Google Cloud Storage staging area.
- Databricks

  You need a staging area in Azure Data Lake Storage, Google Cloud Storage, or Amazon S3.

### Requirements for generating QVD tables

- Amazon S3 bucket for staging data with write access from the Data Movement gateway server machine and read access from the Qlik Cloud tenant.

  Warning noteYou need to make sure that the landing zone is secure. You can use server-side encryption with Amazon S3-managed keys or AWS KMS-managed keys.
- If you want to store Storage (QVD) data in your own managed storage rather than in Qlik managed storage you need an Amazon S3 bucket. You can use the same Amazon S3 bucket that you use for landing data, but this also requires write access from the Qlik Cloud tenant. You also need to use separate folders for landing data and storage.

  Warning noteYou need to make sure that the managed storage is secure. You can use server-side encryption with Amazon S3-managed keys or AWS KMS-managed keys.

## Limitations

There are some limitations to how you use Qlik Talend Data Integration.

### Common limitations

- It is not possible to change the owner of a data task, or move a data task to another project.
- Automatic cleanup of the landing area is not supported. This can affect performance. We recommend that you perform manual cleanups.
- While applying changes to tables in a Storage data asset, there is no transactional consistency between the different tables in the task.
- When a database schema is associated with more than one data task, each data task must use a unique prefix for tables and views. You can set the prefix in the data task settings.
- Two Data Movement gateway tasks should not write to the same table in the landing area. Best practice is to use a separate landing area for each Data Movement gateway task.
- Change handling is not supported for source tables that do not have a primary key. This applies to both onboarded and registered data.

### Limitations when generating QVD tables

- The maximum size of a generated QVD table is 5 GB.

  Data spaces always work with standard capacity which limits the Storage data task capacity. Each table processed by the Storage data task should be with an overall size, including changes, that is up to the supported application size (in-memory) for standard applications.

  For more information about capacity, see [*Large application support*](../../Admin/large-app-support.htm).
- Make sure that two applications do not generate QVD tables with the same name. Best practice is to keep a separate output folder for each application.

### Limitations for cloud data warehouses

#### General limitations

- All datasets are written in the same internal schema and all views are written in the same data asset schema in the storage. Therefore, it is not allowed to have two datasets with the same name in different schemas in a single landing data task.

#### Snowflake limitations

- OAuth authentication is not supported when connecting to Snowflake.

#### Google BigQuery limitations

- It is not possible to use spaces in column names.
- If you rename or delete columns, the tables will need to be recreated and data will be lost.
- Parametrized data types will be set with default values:

  - String

    Length: 8192
  - Bytes

    Length: 8192
  - Numeric

    Precision: 38

    Scale: 9
  - bigDecimal

    Precision: 76

    Scale: 38
- Google BigQuery connections are by default configured with a US location. If you want to use a different location you need to set this in the connection properties.

  1. Edit the connection.
  2. Add a property named location under Advanced.
  3. Set the value of the property to the location that you want to use.
  4. Click Save.

#### Databricks limitations

- Renaming tables and columns is not supported. When syncing after renaming, data will be lost.
- Enable SSL must be enabled.
