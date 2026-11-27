---
title: "Presto"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Presto/Presto-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Presto

Presto provides simultaneous SQL queries across multiple data sources. The Presto Connector enables you to create connections that query all the data sources in an environment that have been configured with Presto. Connections made by selecting Presto from the list of connectors in the Qlik SenseAdd data or Data load editor dialogs.

Presto supports MySQL and PostgreSQL. It also integrates with the Hive metastore to complement existing Hive environments with low latency queries. Unlike a relational database, Presto does not require centralized schema definitions. Presto can query self-describing data as well as complex or multi-structured data. Presto supports semi-structured or nested data types such as JSON.

Presto processes data in record batches and discovers the schema during the processing of each record batch. This enables Presto to support changing schemas during a query.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported Presto versions

The Presto ODBC Driver supports the following versions of Presto Server:

- Open-source Presto Server versions 0.296 and earlier

## Supported Presto data types

The following Presto data types are supported by the PrestoDB Connector:

- BigInt
- Boolean
- Char
- Date
- Decimal
- Double
- Float
- Integer
- SmallInt
- Time
- Time\_WTZ
- Timestamp
- Timestamp With Time Zone
- TinyInt
- Varbinary
- Varchar
- Array
- Json
- Map
- Row
