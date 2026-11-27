---
title: "SQLTypes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLTypes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# SQLTypes

The sqltypes statement returns
a set of fields describing the types of an ODBC or OLE DB data source, to which a connect
has been made.

Syntax:

SQLTypes

The fields can be combined with the fields generated
by the sqlcolumns
and sqltables
commands in order to give a good overview of a given database. The fifteen
standard fields are:

TYPE\_NAME

DATA\_TYPE

PRECISION

LITERAL\_PREFIX

LITERAL\_SUFFIX

CREATE\_PARAMS

NULLABLE

CASE\_SENSITIVE

SEARCHABLE

UNSIGNED\_ATTRIBUTE

MONEY

AUTO\_INCREMENT

LOCAL\_TYPE\_NAME

MINIMUM\_SCALE

MAXIMUM\_SCALE

For a detailed description of these fields, see an ODBC reference handbook.

Example:

Connect
to 'MS Access 7.0 Database; DBQ=C:\Course3\DataSrc\QWT.mbd';

SQLTypes;

Information noteSome ODBC drivers may not support
this command. Some ODBC drivers may produce
additional fields.

## Learn more

- [*SQLColumns*](SQLColumns.htm)
- [*SQLTables*](SQLTables.htm)
