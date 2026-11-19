---
title: "Header is"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/header-is.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
# Header is

Specifies the header size in table files. An arbitrary header length can be specified
through the header is specifier. A header is a text section not used by Qlik Sense.

Syntax:

header is n

header is line

header is n lines

The header length can
be given in bytes (header is n),
or in lines (header is line or
header is n
lines). n must be a positive
integer, representing the header length. If not specified, header
is 0 is assumed. The header is
specifier is only relevant for table files.

Example:

This is an example of a data source table containing a header text line that should not be interpreted as data by Qlik Sense.

\*Header line
Col1,Col2
a,B
c,D

Using the header is 1
lines specifier, the first line will not be loaded as data. In the example, the embedded labels specifier tells Qlik Sense to interpret the first non-excluded line as containing [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/header-is.htm#glossary-0 "Glossary term") labels.

LOAD Col1, Col2
FROM 'lib://files/header.txt'
(txt, embedded labels, delimiter is ',', msq, header is 1 lines);

The result is a table with two fields, Col1 and Col2.

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
