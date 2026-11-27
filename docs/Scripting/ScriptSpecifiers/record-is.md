---
title: "Record is"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/record-is.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load", "Format specification items"]
---

# Record is

For fixed record length files, the record
length must be specified through the record
is specifier.

Syntax:

Record is n

Record is line

Record is n lines

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| n | Specifies the record length in bytes. |
| line | Specifies the record length as one line. |
| n lines | Specifies the record length in lines where n is a positive integer representing the record length. |

Limitations:

The record
is specifier is only relevant for fix
files.

## Learn more

- [*Load*](../ScriptRegularStatements/Load.htm)
