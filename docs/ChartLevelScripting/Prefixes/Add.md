---
title: "Add"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/Prefixes/Add.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Prefixes"]
---

# Add

In a [chart](#glossary-0 "Glossary term") modifying context, the Add prefix is used with LOAD to append values to the HC1 table, representing the hypercube computed by the Qlik associative engine. You can specify one or several columns. Missing values are automatically filled by the Qlik associative engine.

Syntax:

Add loadstatement

Example:

This example adds two rows to the columns Dates and Sales from the inline statement

Add Load
x as Dates,
y as Sales
Inline
[
Dates,Sales
2001/09/1,1000
2001/09/10,-300
]

## Learn more

- [*Load*](../RegularStatements/Load.htm)
