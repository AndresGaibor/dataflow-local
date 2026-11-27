---
title: "Chart level scripting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/modifier-statements-keywords.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions"]
---

# Chart level scripting

When modifying [chart](#glossary-0 "Glossary term") data, you use a sub-set of the Qlik Sense script which consists of a number of statements. A statement
can be either a regular script statement or a script control statement. Certain statements can be preceded by prefixes.

Regular statements are typically used for manipulating data in one way
or another. These statements may be written over any number of lines in
the script and must always
be terminated by a semicolon, ";".

Control statements are typically used for controlling the flow of the script execution. Each clause of a control statement must be kept inside one script line and may be terminated by a semicolon or the end-of-line.

Prefixes may be applied to applicable regular statements but never to control statements.

All script keywords can be typed with any combination of lower case and upper case characters. Field and variable names used in the statements are however case sensitive.

In this section you can find an alphabetical listing of all script statements, control statements and prefixes available in the sub-set of the script used when modifying chart data.
