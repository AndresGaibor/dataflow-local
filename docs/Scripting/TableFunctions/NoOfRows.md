---
title: "NoOfRows Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TableFunctions/NoOfRows.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Table functions"]
---
# NoOfRows Script and chart function

The NoOfRows function returns the number of rows (records) in a previously loaded table.
If the function is used within a LOAD statement, it must not reference
the table currently being loaded.

Syntax:

NoOfRows(table\_name)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| table\_name | The name of the table. |

Example:

LET a =
NoOfRows('tab1');
