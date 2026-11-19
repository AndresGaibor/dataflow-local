---
title: "Logical functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/LogicalFunctions/logical-functions.htm#IsNum?id=1421
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Logical functions

This section describes functions handling logical operations. All functions can be used in both the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/LogicalFunctions/logical-functions.htm#glossary-0 "Glossary term") and in chart expressions.

IsNum

Returns -1 (True) if the expression can be interpreted as a number,
otherwise 0 (False).

IsNum( expr )

IsText

Returns -1 (True) if the expression has a text representation, otherwise
0 (False).

IsText( expr )

> **Note:** Both IsNum and IsText return 0 if the expression is NULL.

Example:

The following example loads an inline table with mixed text and numerical values, and adds two fields to check if the value is a numerical value, respectively a text value.

Load \*, IsNum(Value), IsText(Value)
Inline [
Value
23
Green
Blue
12
33Red];

The resulting table looks like this:

Resulting table

| Value | IsNum(Value) | IsText(Value) |
| --- | --- | --- |
| 23 | -1 | 0 |
| Green | 0 | -1 |
| Blue | 0 | -1 |
| 12 | -1 | 0 |
| 33Red | 0 | -1 |
