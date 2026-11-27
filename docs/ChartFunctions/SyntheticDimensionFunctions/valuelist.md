---
title: "ValueList - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SyntheticDimensionFunctions/valuelist.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Synthetic dimension functions"]
---

# ValueList - chart function

ValueList() returns a set
of listed values, which, when used in a calculated dimension, will form a synthetic dimension.

Information noteIn [charts](#glossary-0 "Glossary term") with a synthetic dimension created with the ValueList function it is possible to reference the [dimension](#glossary-1 "Glossary term") value corresponding to a specific expression cell by restating the ValueList
function with the same parameters in the chart expression. The function may of course be used anywhere in the layout, but apart from when used
for synthetic dimensions it will only be meaningful inside an aggregation function.

Information noteSynthetic dimensions are not affected by selections.

Syntax:

ValueList(v1 {,...})

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| v1 | Static value (usually a string, but can be a number). |
| {,...} | Optional list of static values. |

Examples and results:

Function examples

| Example | Result |
| --- | --- |
| ValueList('Number of Orders', 'Average Order Size', 'Total Amount') | When used to create a dimension in a table, for example, this results in the three string values as row labels in the table. These can then be referenced in an expression. |
| =IF( ValueList('Number of Orders', 'Average Order Size', 'Total Amount') = 'Number of Orders', count(SaleID), IF( ValueList('Number of Orders', 'Average Order Size', 'Total Amount') = 'Average Order Size', avg(Amount), sum(Amount) )) | This expression takes the values from the created dimension and references them in a nested IF statement as input to three [aggregation](#glossary-2 "Glossary term") functions: |

Data used in examples:

SalesPeople:

LOAD \* INLINE [

SaleID|SalesPerson|Amount|Year

1|1|12|2013

2|1|23|2013

3|1|17|2013

4|2|9|2013

5|2|14|2013

6|2|29|2013

7|2|4|2013

8|1|15|2012

9|1|16|2012

10|2|11|2012

11|2|17|2012

12|2|7|2012

] (delimiter is '|');
