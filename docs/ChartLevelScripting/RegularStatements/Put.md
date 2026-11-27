---
title: "Put"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/RegularStatements/Put.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Regular statements"]
---

# Put

The put statement is used to set some numeric value in the hypercube.

Access to the columns can be done by labels. You can also access columns and rows by declaration order. See the examples below for more details.

Information noteYou cannot modify chart dimensions with the put statement.

Syntax:

put column(position)=value

Example 1:

Access to the columns can be done by labels.

This example will set a value of 1 in the first position of the column labeled Sales.

Put Sales(1) = 1;

Example 2:

You can access [measure](#glossary-0 "Glossary term") columns by declaration order using the #hc1.measure format for measures.

This example will set the value 1000 in the tenth position of the final sorted hypercube.

Put #hc1.measure.2(10) = 1000;

## Learn more

- [*HCValue*](HCValue.htm)
