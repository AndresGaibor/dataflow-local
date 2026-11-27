---
title: "NoOfFields Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/NoOfFields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Table functions"]
---

# NoOfFields Script function

The NoOfFields script function returns the number of fields in a previously loaded table. If
the function is used within a LOAD statement, it must not reference the
table currently being loaded.

Syntax:

NoOfFields(table\_name)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| table\_name | The name of the table. |

Example:

LET a =
NoOfFields('tab1');
