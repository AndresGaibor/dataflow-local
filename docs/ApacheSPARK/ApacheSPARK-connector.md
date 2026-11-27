---
title: "Apache Spark"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApacheSPARK/ApacheSPARK-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Apache Spark

Connections to an Apache Spark database are made by selecting Apache Spark from the list of drivers in the Qlik Sense Add data or Data load editor dialogs.

The Apache Spark Connector is used for direct SQL and HiveQL access to Apache Hadoop/Spark distributions. The connector transforms an SQL query into the equivalent form in HiveQL and passes the query through to the database for processing.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported Apache Spark versions

The followings database versions are supported:

- 1.6
- 2.1 through 2.4
- 3.0

## Supported Apache Spark data types

The following Apache SPARK data types are supported by the Apache Spark Connector.

- BigInt
- Binary
- Boolean
- Date
- Decimal
- Double
- Float
- Integer
- SmallInt
- String
- Timestamp
- TinyInt
- Varchar
