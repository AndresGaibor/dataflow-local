---
title: "SQLTables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLTables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# SQLTables

The sqltables statement returns
a set of fields describing the tables of an ODBC or OLE DB data source, to which a connect
has been made.

Syntax:

SQLTables

The fields can be combined with the fields generated
by the sqlcolumns
and sqltypes
commands in order to give a good overview of a given database. The five
standard fields are:

TABLE\_QUALIFIER

TABLE\_OWNER

TABLE\_NAME

TABLE\_TYPE

REMARKS

For a detailed description of these fields, see an ODBC reference handbook.

Example:

Connect
to 'MS Access 7.0 Database; DBQ=C:\Course3\DataSrc\QWT.mbd';

SQLTables;

> **Note:** Some ODBC drivers may not support
> this command. Some ODBC drivers may produce
> additional fields.

## Learn more

- [*SQLColumns*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLColumns.htm)
- [*SQLTypes*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLTypes.htm)
