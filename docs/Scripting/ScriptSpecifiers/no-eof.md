---
title: "No eof"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/no-eof.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
# No eof

The no eof specifier is used to disregard end-of-file character when loading delimited .txt
files.

Syntax:

no eof

If the no eof specifier is used, characters with code point 26,
which otherwise denotes end-of-file, are disregarded and can be part of a field value.

It is relevant only for delimited text files.

Example:

LOAD \* from a.txt (txt, utf8, embedded labels, delimiter is ' ', no eof);

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
