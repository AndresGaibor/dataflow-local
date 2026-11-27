---
title: "Prefixes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/modifier-prefixes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting"]
---

# Prefixes

Expand/Collapse all

# Prefixes

Prefixes may be applied to applicable regular statements but never to control statements.

All script keywords can be typed with any combination of lower case and upper case characters. Field and variable names used in the statements are however case sensitive.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Add

The Add prefix can be added to any LOAD or SELECT statement in the script to specify that it should add records to another table. It also specifies that this statement should be run in a partial reload. The Add prefix can also be used in a Map statement.

[**Add**](Prefixes/Add.htm) [only] [Concatenate[(tablename )]] (loadstatement |
selectstatement)

[**Add**](Prefixes/Add.htm) [ Only ] mapstatement

Replace

The Replace prefix
can be added to any LOAD or SELECT statement in the script to specify that the loaded table should replace another table. It also specifies that this statement should be run in a partial reload. The Replace prefix can also be used in a Map statement.

[**Replace**](Prefixes/Replace.htm) [only] [Concatenate[(tablename) ]] (loadstatement |
selectstatement)

[**Replace**](Prefixes/Replace.htm) [only] mapstatement
