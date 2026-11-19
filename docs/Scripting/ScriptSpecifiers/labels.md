---
title: "Labels"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/labels.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
# Labels

Labels is a file specifier for the LOAD statement that defines where in a file the field names can be found.

Syntax:

embedded
labels|explicit
labels|no labels

The [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/labels.htm#glossary-0 "Glossary term") names can be found in different
places of the file. If the first record contains the field names, embedded labels should be used. If there
are no field names to be found, no labels
should be used. In dif files,
a separate header section with explicit field names is sometimes used.
In such a case, explicit labels
should be used. If nothing is specified, embedded labels is assumed, also for dif
files.

Example 1:

LOAD \* from a.txt (unicode, txt, delimiter is ',' , embedded labels

Example 2:

LOAD \* from a.txt (codePage is 1252, txt, delimiter is ',' , no labels)

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
