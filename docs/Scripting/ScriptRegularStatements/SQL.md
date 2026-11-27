---
title: "SQL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQL.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# SQL

The SQL statement allows you to send an arbitrary SQL command through an
ODBC or OLE DB connection.

Syntax:

SQL sql\_command

Sending SQL statements which update the database will return an error
if Qlik Sense has opened the ODBC [connection](#glossary-0 "Glossary term") in read-only mode.

The syntax:

SQL SELECT \* from tab1;

is allowed, and is the preferred syntax for SELECT,
for reasons of consistency. The SQL prefix will, however, remain optional
for SELECT statements.

Arguments:

| Argument | Description |
| --- | --- |
| sql\_command | A valid SQL command. |

Example 1:

SQL leave;

Example 2:

SQL Execute <storedProc>;

## Learn more

- [*Select*](Select.htm)
