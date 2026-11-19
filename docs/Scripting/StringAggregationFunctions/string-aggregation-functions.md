---
title: "String aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/string-aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---
Expand/Collapse all

# String aggregation functions

This section describes string-related [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/string-aggregation-functions.htm#glossary-0 "Glossary term") functions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## String aggregation functions in the data load script

Concat

Concat() is used to combine string values. The script function returns the
aggregated string concatenation of all values of the expression iterated over
a number of records as defined by a group by clause.

[**concat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/concat.htm)([ distinct
] expression [, delimiter [, sort-weight]])

FirstValue

FirstValue() returns the value that was loaded first from the
records defined by the expression, sorted by a group by clause.

> **Note:** This function is only available as a script function.

[**FirstValue**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/FirstValue.htm) (expression)

LastValue

LastValue() returns the value that was loaded last from the
records defined by the expression, sorted by a group by clause.

> **Note:** This function is only available as a script function.

[**LastValue**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/LastValue.htm) (expression)

MaxString

MaxString() finds string values in the expression and returns the last text value sorted
alphabetically over a number of records, as defined by a group
by clause.

[**MaxString**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/MaxString.htm)(expression
)

MinString

MinString() finds string values in the expression and returns the first text value sorted
alphabetically over a number of records, as defined by a group
by clause.

[**MinString**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/MinString.htm)(expression
)

## String aggregation functions in charts

The following [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/string-aggregation-functions.htm#glossary-1 "Glossary term")functions are available for aggregating strings in [charts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringAggregationFunctions/string-aggregation-functions.htm#glossary-2 "Glossary term")

Concat

Concat() is used to combine string values. The function returns the aggregated string concatenation of all the values of the expression evaluated over each dimension.

[**concat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StringAggregationFunctions/concat.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]] string[, delimiter[, sort\_weight]])

MaxString

MaxString() finds string values in the expression or field and returns the last text value in alphabetical sort order.

[**maxstring**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StringAggregationFunctions/maxstring.htm)({[SetExpression] [TOTAL [<fld{, fld}>]]} expr)

MinString

MinString() finds string values in the expression or field and returns the first text value in alphabetical sort order.

[**minstring**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StringAggregationFunctions/minstring.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} expr)
