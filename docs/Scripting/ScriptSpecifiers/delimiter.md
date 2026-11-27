---
title: "Delimiter is"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/delimiter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load", "Format specification items"]
---

# Delimiter is

For delimited table files, an arbitrary
delimiter can be specified through the delimiter
is specifier. This specifier is relevant only for delimited .txt
files.

Syntax:

delimiter is char

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| char | Specifies a single character from the 127 ASCII characters. |

Additionally, the following values can be used:

Optional values

| Value | Description |
| --- | --- |
| '\t' | representing a tab sign, with or without quotation marks. |
| '\\' | representing a backslash ( \ ) character. |
| 'spaces' | representing all combinations of one or more spaces. Non-printable characters with an ASCII-value below 32, with the exception of CR and LF, will be interpreted as spaces. |

If nothing is specified, delimiter
is ',' is assumed.

Example:

LOAD \* from a.txt (utf8, txt, delimiter is ',' , embedded labels);

## Learn more

- [*Load*](../ScriptRegularStatements/Load.htm)
