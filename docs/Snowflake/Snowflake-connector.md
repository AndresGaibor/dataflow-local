---
title: "Snowflake"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Snowflake/Snowflake-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Snowflake

Connections to a Snowflake database are made by selecting Snowflake from the list of drivers in the list of connectors in the QlikView ODBC Connection dialog or the Qlik Sense Add data or Data load editor dialogs.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported Snowflake data types

The following Snowflake data types are supported by the Snowflake Connector.

- Array
- BigInt
- Binary
- Boolean
- ByteInt
- Character
- Date
- Datetime
- Decimal
- Double precision
- Float
- Float4
- Float8
- Integer
- Number
- Object
- Real
- SmallInt
- Text
- Time
- TimeStamp
- TimeStamp\_NTZ
- TimeStamp\_LTZ
- TimeStamp\_TZ
- TinyInt
- Varbinary
- Varchar
- Variant

Information noteTime-zone related data types, such as TIMESTAMP\_LTZ and TIMESTAMP\_TZ, may show different results between Qlik Sense Enterprise and Qlik Cloud, due to time-zone differences between Qlik Sense Enterprise servers and Qlik Cloud containers.
