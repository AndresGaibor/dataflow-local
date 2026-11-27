---
title: "Setting up connections to targets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/TargetConnections/data-project-connections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections"]
---

# Setting up connections to targets

You can connect to targets to facilitate data delivery and various ELT operations, including data registration, data storage, transformations, and data mart creation. Target platforms can be supported as replication targets, data pipeline targets, and in some cases, both.

Information noteWhen you connect to targets you may need to add underlying Qlik Cloud IP addresses to your allowlist. For more information, see [*Allowlisting domains and IP addresses*](../../Introduction/qlik-cloud-dns-ip.htm).

## Target platform use cases and supported versions

The table below summarizes which platforms are supported according to use case and, where applicable, lists the supported versions for each target.

Target platform use cases and supported versions

| Target platform | Supported as a replication target | Supported as a data pipeline target platform | Supported as a data warehouse staging area | Supports access via a private connection | Version |
| --- | --- | --- | --- | --- | --- |
| [Azure Data Lake Storage](adls-target.htm) | Yes | No | Supported with the following targets:   - Databricks - Azure Synapse Analytics - Microsoft Fabric | Yes | Not applicable |
| [Amazon Redshift](redshift-target.htm) | Yes | Yes | No | Yes | Not applicable |
| [Amazon S3](aws-s3-target.htm) | Yes | No | Supported with the following targets:   - Databricks - Amazon Redshift | Yes | Not applicable |
| [Databricks](databricks-target.htm) | Yes | Yes | No | On Azure: Yes  On Google: Yes  On AWS: Not when moving data. Only when registering data and running ELT tasks. | - All-purposes (Interactive) cluster:    - 12.2 LTS   - 13.3 LTS   - 14.3 LTS   - 15.4 LTS - SQL Warehouse cluster - Databricks SQL Serverless |
| [Google BigQuery](bigquery-target.htm) | Yes | Yes | No | Yes | Not applicable |
| [Google Cloud Storage](google-storage-target.htm) | Yes | No | Supported with the Databricks target. | Yes |  |
| [Microsoft Azure Synapse Analytics](azure-target.htm) | No | Yes, except when SaaS connectors are used as sources in data pipeline projects. | No | Yes | Not applicable |
| [Microsoft Fabric](fabric-target.htm) | Yes | Yes | No | Yes | Not applicable |
| [Microsoft SQL Server](sqlserver-target.htm)  In addition to on-premises support, the following cloud platforms are also supported:   - Amazon RDS for SQL Server - Google Cloud for SQL Server - Microsoft Azure SQL (Supports both Microsoft Azure Managed Instance and Microsoft Azure Database) | Yes | Yes | No | Yes | 2016, 2017, 2019, 2022 |
| [MySQL and MariaDB](mysql-target.htm)  In addition to on-premises support, the following cloud platforms are also supported:   - Amazon Aurora - Microsoft Azure Database for MySQL - Flexible Server. - Amazon RDS for MariaDB - Amazon RDS for MySQL - Google Cloud SQL for MySQL. | Yes | No | No | Yes | 8.0, 8.4  Information noteWhen MariaDB (on-premises or Amazon RDS) is the target, the supported versions are 10.6 to 10.11, 11.4, and 11.8 |
| [Oracle](oracle-target.htm) | Yes | No | No | Yes | 19.x, 21c, 23ai  Information note Oracle 23ai is certified with Oracle Standard Edition only.  Warning noteIf you set the Oracle compatibility parameter, make sure you specify a version supported by Data Movement gateway. For example, if you are working with version 21c, you cannot set an earlier version as the compatibility version. |
| [PostgreSQL](postgresql-target.htm)  In addition to on-premises support, the following cloud platforms are also supported:   - Amazon Aurora - Azure Database for PostgreSQL - Flexible Server - Amazon RDS for PostgreSQL - Google Cloud SQL for PostgreSQL - Google Cloud AlloyDB for PostgreSQL | Yes | No | No | Yes | 14.x, 15.x, 16.x, 17.x |
| [Teradata](teradata-target.htm) | Yes | No | No | Yes | 17.x, 20.x |
| [Qlik Cloud](aws-target.htm) | No | Yes | No | Not applicable | Not applicable |
| [Snowflake](snowflake-target.htm) | Yes | Yes | No | Yes | Not applicable |
| [Kafka](kafka-target.htm)  In addition to on-premises support, Amazon MSK is also supported.  Schema registry servers:  Certified with Confluent Schema Registry 6.x, and 7.x. | Yes | No | No | Yes | 3.x and 4.0.x |

For more information on the data pipeline use case, see [*Creating and managing data pipeline projects*](../Introduction/Data-projects.htm).

For more information on the replication use case, see [*Creating a replication project*](../Replicating/data-replication-task.htm).

For more information on private connections, see [*Supporting private connections in Qlik Talend Data Integration*](../../Gateways/replication-gateway.htm#Supporti).
