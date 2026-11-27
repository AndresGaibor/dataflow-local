---
title: "SQLColumns"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLColumns.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# SQLColumns

The sqlcolumns statement returns
a set of fields describing the columns of an ODBC
or OLE DB data source, to which a connect
has been made.

Syntax:

SQLcolumns

The fields can be combined with the fields generated
by the sqltables
and sqltypes
commands in order to give a good overview of a given database. The twelve
standard fields are:

TABLE\_QUALIFIER

TABLE\_OWNER

TABLE\_NAME

COLUMN\_NAME

DATA\_TYPE

TYPE\_NAME

PRECISION

LENGTH

SCALE

RADIX

NULLABLE

REMARKS

For a detailed description of these fields, see an ODBC reference handbook.

Example:

Connect
to 'MS Access 7.0 Database; DBQ=C:\Course3\DataSrc\QWT.mbd';

SQLcolumns;

Information noteSome ODBC drivers may not support
this command. Some ODBC drivers may produce
additional fields.

## Learn more

- [*SQLTables*](SQLTables.htm)
- [*SQLTypes*](SQLTypes.htm)
