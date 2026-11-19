---
title: "STEYX Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/steyx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---
# STEYX Script function

STEYX() returns
the aggregated standard error of the predicted y-value for each x-value
in the regression for a series of coordinates represented by paired numbers
in x-expression and y-expression
iterated over a number of records as defined by a group by clause.

Syntax:

STEYX (y\_value, x\_value)

Return data type:  numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| y\_value | The expression or field containing the range of y-values to be measured. |
| x\_value | The expression or field containing the range of x-values to be measured. |

Limitations:

Text values, NULL values and missing values in any or both pieces of a data-pair result in the entire data-pair being disregarded.

Examples and results:

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

Resulting data

| Example | Result |
| --- | --- |
| Trend:  Load \*, 1 as Grp;  LOAD \* inline [  Month|KnownY|KnownX  Jan|2|6  Feb|3|5  Mar|9|11  Apr|6|7  May|8|5  Jun|7|4  Jul|5|5  Aug|10|8  Sep|9|10  Oct|12|14  Nov|15|17  Dec|14|16  ] (delimiter is '|');  STEYX1:  LOAD Grp,  STEYX(KnownY, KnownX) as MySTEYX  Resident Trend Group By Grp; | In a table with the [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/steyx.htm#glossary-0 "Glossary term") `MySTEYX`, the result of the STEYX() calculation in the data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/steyx.htm#glossary-1 "Glossary term") is 2.0714764. |
