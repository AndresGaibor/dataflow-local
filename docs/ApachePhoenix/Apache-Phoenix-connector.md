---
title: "Apache Phoenix"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ApachePhoenix/Apache-Phoenix-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Apache Phoenix

Connections to an Apache Phoenix database are made by selecting Apache Phoenix from the list of connectors in the Qlik Sense Add data or Data load editor dialogs.

Apache Phoenix is a relational database layer that is build on top of Apache HBase. Apache Phoenix compiles an SQL query into a series of HBase scans and executes those scans to produce result sets.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported Apache Phoenix database versions

The followings database versions are supported:

- CDH 4.4.0 to 4.7.0

## Supported Apache Phoenix data types

The following Apache Phoenix data types are supported by the Apache Phoenix Connector.

- Array
- BigInt
- Binary
- Boolean
- Char
- Date
- Decimal
- Double
- Float
- Integer
- SmallInt
- Time
- Timestamp
- TinyInt
- Unsigned\_Date
- Unsigned\_Double
- Unsigned\_Float
- Unsigned\_Int
- Unsigned\_Long
- Unsigned\_SmallInt
- Unsigned\_Time
- Unsigned\_TimeStamp
- Unsigned\_TinyInt
- Varchar
