---
title: "Microsoft SQL Server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/SQLServer/SQL-Server-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Microsoft SQL Server

Connections to a Microsoft SQL Server database are made by selecting Microsoft SQL Server from the list of drivers in the list of connectors in the Qlik Sense Add data or Data load editor dialogs.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported Microsoft SQL Server versions

The followings data versions are supported:

- 2014 to 2022

Information noteWhen using the connector for Microsoft SQL Server, ensure that your environment is on a supported Microsoft SQL Server version.

## Supported Microsoft SQL Server data types

The following Microsoft SQL Server data types are supported by the Microsoft SQL Server Connector.

- BigInt
- BigInt Identity
- Binary
- Bit
- Char
- Date
- DateTime
- DateTime2
- Decimal
- Decimal Identity
- Float
- GUID
- Int
- Int Identity
- Money
- NChar
- NText
- Numeric
- Numeric Identity
- NVarChar
- NVarChar(max)
- Real
- SmallDateTime
- SmallInt
- SmallInt Identity
- SmallMoney
- SysName
- Text
- Time
- TinyInt
- TinyInt Identity
- Varbinary
- VarChar
- VarChar(max)
- XML

Information noteYou might be able to retrieve data types that are not noted in the Supported list. However, these unlisted data types might not work in future updates. In addition, Qlik cannot provide support for items not included in the Supported list.
