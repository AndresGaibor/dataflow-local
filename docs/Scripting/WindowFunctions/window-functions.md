---
title: "Window functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/window-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Window functions

Window functions perform calculations using values from multiple rows to produce a value for each row separately. Window functions can only be calculated once the entire table is read.

You can use window functions to perform operations such as:

- Comparing an individual number value in a row with the average, maximum, or minimum within the column.
- Calculating the rank of an individual value, either within the column or within the entire table.

Window functions do not change the number of records in the table but can perform similar tasks as aggregation functions or relational functions and range functions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Window

The **Window** function performs calculations from multiple rows, producing a value for each row separately.

[**Window**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/Window.htm)(main\_expr, [partition1, partition2, ...], [sort\_type, [sort\_expr],[filter\_expr], [start\_expr, end\_expr]])

WRank

The **WRank** function performs ranking calculations inside **Window**.

[**WRank**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/WRank.htm)([mode[, fmt]])
