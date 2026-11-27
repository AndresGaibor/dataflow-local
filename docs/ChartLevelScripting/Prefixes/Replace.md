---
title: "Replace"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/Prefixes/Replace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Prefixes"]
---

# Replace

In a [chart](#glossary-0 "Glossary term") modifying context, the Replace prefix changes all values of the HC1 table with a computed value defined by the script.

Syntax:

Replace loadstatement

Example:

This example overwrites all values in column z with the sum of x and y.

Replace Load
x+y as z
Resident HC1;

## Learn more

- [*Load*](../RegularStatements/Load.htm)
