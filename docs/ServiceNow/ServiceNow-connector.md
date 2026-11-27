---
title: "ServiceNow"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/ServiceNow/ServiceNow-connector.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# ServiceNow

You can connect to a ServiceNow database in the Qlik Sense Add data or Data load editor dialogs.

The ServiceNow Connector connects to ServiceNow Workspace clusters and SQL Analytics SQL endpoints to query data in tables.

Information noteIndustry-accepted best practices must be followed when using or allowing access through the ODBC Connector. Administrators must follow The Principle of Least Privilege when setting up source database privileges and permissions.

## Supported ServiceNow versions

The followings database versions are supported:

- ServiceNow Orlando and later

## Supported ServiceNow data types

The following ServiceNow data types are supported:

Supported data types

| SourceType (ServiceNow ODBC) | QvxField Type (Qlik Sense) |
| --- | --- |
| BIGINT | Int64 |
| BIT | Bit |
| CHAR | String |
| DECIMAL | Real |
| DOUBLE | Real |
| FLOAT | Real |
| INTEGER | Int32 |
| LONGVARCHAR | String |
| NUMERIC | Real |
| REAL | Real |
| SMALLINT | Int16 |
| TINYINT | Int16 |
| TYPE\_DATE | Date |
| TYPE\_TIME | Time |
| TYPE\_TIMESTAMP | DateTime |
| UBIGINT | Int64 |
| UINTEGER | Int32 |
| USMALLINT | Int16 |
| UTINYINT | Int16 |
| VARCHAR | String |
| WCHAR | String |
| WLONGVARCHAR | String |
| WVARCHAR | String |
