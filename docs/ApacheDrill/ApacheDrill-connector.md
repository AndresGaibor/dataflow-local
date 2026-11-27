---
title: "Apache Drill"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApacheDrill/ApacheDrill-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Apache Drill

The Apache Drill Connector provides access to non-relational data stores. Connections are made by selecting Apache Drill from the list of drivers in the list of connectors in the Qlik Sense Add data or Data load editor dialogs.

Apache Drill is a low-latency distributed query engine capable of querying large data sets from multiple data sources using SQL. Unlike a relational database, Apache Drill does not require centralized schema definitions. Apache Drill can query self-describing data as well as complex or multi-structured data. Apache Drill supports semi-structured or nested data types such as JSON.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported Apache Drill versions

The following versions are supported:

- Up to 1.16.0

## Supported Apache Drill data types

The following Apache Drill data types are supported by the Apache Drill Connector.

- Any
- Array
- BigInt
- Bit
- Char
- Date
- DateTime
- Float
- Decimal9
- Double
- Int
- Map
- SmallInt
- TinyInt
- Time
- Timetstamp
- Varchar

## Learn more

- [Data types in Qlik Sense](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/data-types.htm)
