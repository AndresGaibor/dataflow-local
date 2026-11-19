---
title: "Median Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/median.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Statistical aggregation functions"]
---
# Median Script function

Median() returns
the aggregated median of the values in the expression over a number of records as defined by a
group by clause.

Syntax:

Median (expr)

Return data type: numeric

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |

## Example: Script expression using Median

Example - script expression

### Load script

Load the following inline data and script expression in the data load editor for this example.

```
Table 1:
Load RecNo() as RowNo, Letter, Number Inline
[Letter, Number
A,1
A,3
A,4
A,9
B,2
B,8
B,9];
					
Median:
LOAD Letter,
Median(Number) as MyMedian
Resident Table1 Group By Letter;
										
```

For more information about using inline loads, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

### Create a visualization

Create a table [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/median.htm#glossary-0 "Glossary term") in a Qlik Sense [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/median.htm#glossary-1 "Glossary term") with Letter and MyMedian as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/median.htm#glossary-2 "Glossary term").

### Result

![](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Median_script.png)

### Explanation

The median is considered the "middle" number when the numbers have been sorted in order from smallest to greatest. If the data set has an even number of values, the function returns the average of the two middle values. In this example, the median is calculated for each set of values of A and B, which is 3.5 and 8, respectively.
