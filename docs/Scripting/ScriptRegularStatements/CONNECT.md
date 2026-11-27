---
title: "Connect"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/CONNECT.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Connect

The CONNECT
statement is used to define access to a data connection.

Information noteQlik Cloud only supports the LIB CONNECT TO variant. The ODBC CONNECT TO, OLEDB CONNECT TO, and CUSTOM CONNECT TO variants are not supported in Qlik Cloud. For documentation related to variants only supported in Qlik Sense Client-Managed, see [Connect](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/CONNECT.htm).

Syntax:

LIB CONNECT TO connection

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| connection | The name of a data connection.  The syntax for a data connection in a space is (space\_name):(connection\_name).  You can specify a data connection in the current space with the syntax :(connection\_name).  If no space is specified, it will look for the connection in the space the application is in. For more information on syntax for spaces, see [*Connect to data sources in load scripts*](../../LoadData/connect-data-sources-data-load-editor.htm). |

Example 1:

LIB CONNECT TO 'DataConnection';

The script looks for a connection named DataConnection in the user running the script's personal space.

Example 2:

LIB CONNECT TO 'Sales:DataConnection'

The script looks for a connection named DataConnection in a space called Sales.

## Learn more

- [*To*](../ScriptControlStatements/To.htm)
