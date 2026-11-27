---
title: "Counter aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterAggregationFunctions/counter-aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---

# Counter aggregation functions

Expand/Collapse all

# Counter aggregation functions

Counter aggregation functions return various types of counts of an expression over a number of records in a data [load script](#glossary-0 "Glossary term") or a number of values in a [chart](#glossary-1 "Glossary term") [dimension](#glossary-2 "Glossary term").

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Counter aggregation functions in the data load script

Count

Count() returns the number of values aggregated in expression, as defined by a group by clause.

[**count**](count.htm)([distinct ] expression | \* )

MissingCount

MissingCount() returns the number of missing values aggregated in the expression, as defined by a group by clause.

[**MissingCount**](MissingCount.htm)([
distinct ] expression)

NullCount

NullCount() returns the number of NULL values aggregated in the expression, as defined by a group by clause.

[**NullCount**](NullCount.htm)([
distinct ] expression)

NumericCount

NumericCount() returns the number of numeric values found in the expression,
as defined by a group by clause.

[**NumericCount**](NumericCount.htm)([
distinct ] expression)

TextCount

TextCount() returns the number of field values that are non-numeric aggregated in the expression, as defined by a group by clause.

[**TextCount**](TextCount.htm)([
distinct ] expression)

## Counter aggregation functions in chart expressions

The following counter aggregation functions can be used in charts.

Count

Count()
 is used to aggregate the number of values, text and numeric, in each chart dimension.

[**count**](../../ChartFunctions/CounterAggregationFunctions/count.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

MissingCount

MissingCount()
 is used to aggregate the number of missing values in each chart dimension. Missing values are all non-numeric values.

[**missingcount**](../../ChartFunctions/CounterAggregationFunctions/missingcount.htm)({[SetExpression] [DISTINCT]
[TOTAL [<fld {,fld}>]] expr)

NullCount

NullCount()
 is used to aggregate the number of null values in each chart dimension.

[**nullcount**](../../ChartFunctions/CounterAggregationFunctions/nullcount.htm)({[SetExpression][DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

NumericCount

NumericCount()
 aggregates the number of numeric values in each chart dimension.

[**numericcount**](../../ChartFunctions/CounterAggregationFunctions/numericcount.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld {,fld}>]]} expr)

TextCount

TextCount()
 is used to aggregate the number of field values that are non-numeric in each chart dimension.

[**textcount**](../../ChartFunctions/CounterAggregationFunctions/textcount.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld {,fld}>]]} expr)
