---
title: "Executing non-SELECT statements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/How-to-load-without-SELECT.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Executing non-SELECT statements

You can execute load scripts that do not start with an SQL SELECT statement, for example UPDATE, INSERT, EXEC, and WITH ... AS with the connectors in the Qlik ODBC Connector Package. This option needs to be enabled.

## Enabling non-SELECT queries on Qlik Cloud

If you want to execute scripts that contain non-SELECT statements, you need to enable the setting Allow non-SELECT queries in the data connection dialog.

## Executing statements that do not return data

If you want to execute a query that contains statements such as UPDATE or INSERT, that do not return data, you can use an !EXECUTE\_NON\_SELECT\_QUERY keyword at the end of the query. In this occasion the connector will execute the statement and then return an empty \_\_skip\_loading (string \_\_empty\_field) table instead.

Example:

SQL INSERT INTO [dbo].[Table\_1]
([val])
VALUES
(123) !EXECUTE\_NON\_SELECT\_QUERY;
