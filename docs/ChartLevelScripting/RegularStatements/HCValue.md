---
title: "HCValue"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/RegularStatements/HCValue.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Regular statements"]
---

# HCValue

The HCValue function it is used to retrieve values in a row of a specified column.

Syntax:

HCValue(column,position)

Example 1:

This example returns the value at the first position of the column with label ‘Sales’.

HCValue(Sales,1)

Example 2:

This example returns the value at the tenth position of the sorted hypercube.

HCValue(#hc1.[measure](#glossary-0 "Glossary term")2,10)

Example 3:

This example returns the value at the fifth row in the third [dimension](#glossary-1 "Glossary term").

HCValue(#hc1.dimension.3,5)

Information noteIf there are no such dimensions or expressions, in value or labels, an error is returned indicating that the column was not found. If the index for the column is out of bounds, NULL is returned.

## Learn more

- [*Put*](Put.htm)
