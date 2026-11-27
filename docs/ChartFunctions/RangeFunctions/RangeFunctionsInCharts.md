---
title: "Range functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RangeFunctions/RangeFunctionsInCharts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Range functions

Expand/Collapse all

# Range functions

The range functions are functions that take an array of values and produce a single value as a result. All range functions can be used in both the data [load script](#glossary-0 "Glossary term") and in chart expressions.

For example, in a [visualization](#glossary-1 "Glossary term"), a range function can calculate a single value from an inter-record array. In the data load script, a range function can calculate a single value from an array of values in an internal table.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Information noteRange functions replace the following general
numeric functions: numsum,
numavg, numcount,
nummin and nummax, which should now be regarded as obsolete.

## Basic range functions

RangeMax

RangeMax() returns the highest numeric values found within the expression or field.

[**rangemax**](rangemax.htm)(first\_expr[, Expression])

RangeMaxString

RangeMaxString() returns the last value in the text sort order that it finds in the expression or field.

[**rangemaxstring**](rangemaxstring.htm)(first\_expr[, Expression])

RangeMin

RangeMin() returns the lowest numeric values found within the expression or field.

[**rangemin**](rangemin.htm)(first\_expr[, Expression])

RangeMinString

RangeMinString() returns the first value in the text sort order that it finds in the expression or field.

[**rangeminstring**](rangeminstring.htm)(first\_expr[, Expression])

RangeMode

RangeMode() finds the most commonly occurring value (mode value) in the expression or field.

[**rangemode**](rangemode.htm)(first\_expr[, Expression])

RangeOnly

RangeOnly() is a dual function that returns a value if the expression evaluates to one unique value. If this is not the case then NULL is returned.

[**rangeonly**](rangeonly.htm)(first\_expr[, Expression])

RangeSum

RangeSum() returns the sum of a range of values. All non-numeric
values are treated as 0.

[**rangesum**](rangesum.htm)(first\_expr[, Expression])

## Counter range functions

RangeCount

RangeCount() returns the number of values, both text and numeric, in the expression or field.

[**rangecount**](rangecount.htm)(first\_expr[, Expression])

RangeMissingCount

RangeMissingCount() returns the number of non-numeric values (including NULL) in the expression or field.

[**rangemissingcount**](rangemissingcount.htm)(first\_expr[, Expression])

RangeNullCount

RangeNullCount() finds the number of NULL values in the expression or field.

[**rangenullcount**](rangenullcount.htm)(first\_expr[, Expression])

RangeNumericCount

RangeNumericCount() finds the number of numeric values in an expression or field.

[**rangenumericcount**](rangenumericcount.htm)(first\_expr[, Expression])

RangeTextCount

RangeTextCount() returns the number of text values in an expression or field.

[**rangetextcount**](rangetextcount.htm)(first\_expr[, Expression])

## Statistical range functions

RangeAvg

RangeAvg() returns the average of a range. Input to the function can be either a range of values or an expression.

[**rangeavg**](rangeavg.htm)(first\_expr[, Expression])

RangeCorrel

RangeCorrel() returns the correlation coefficient for two sets of data. The correlation coefficient is a measure of the relationship between the data sets.

[**rangecorrel**](rangecorrel.htm)(x\_values
, y\_values[, Expression])

RangeFractile

RangeFractile() returns the value that corresponds to the n-th fractile (quantile) of a range of numbers.

[**rangefractile**](rangefractile.htm)(fractile, first\_expr[ ,Expression])

RangeKurtosis

RangeKurtosis() returns the value that corresponds to the kurtosis of a range of numbers.

[**rangekurtosis**](rangekurtosis.htm)(first\_expr[, Expression])

RangeSkew

RangeSkew() returns the value corresponding to the skewness of a range of numbers.

[**rangeskew**](rangeskew.htm)(first\_expr[, Expression])

RangeStdev

RangeStdev() finds the standard deviation of a range of numbers.

[**rangestdev**](rangestdev.htm)(expr1[, Expression])

## Financial range functions

RangeIRR

RangeIRR() returns the internal rate of return for a
series of cash flows represented by the input values.

[**RangeIRR**](../../Scripting/RangeFunctions/RangeIRR.htm)(value[, value][, Expression])

RangeNPV

RangeNPV() returns the net present value of an investment
based on a discount rate and
a series of future periodic payments (negative values) and incomes (positive values).
The result has a default number format of money.

[**RangeNPV**](../../Scripting/RangeFunctions/RangeNPV.htm)(discount\_rate,
value[, value][, Expression])

RangeXIRR

RangeXIRR() returns the internal rate of return (yearly) for a
schedule of cash flows that is not necessarily periodic. To calculate
the internal rate of return for a series of periodic cash flows, use the
RangeIRR
function.

[**RangeXIRR**](../../Scripting/RangeFunctions/RangeXIRR.htm)(values,
dates[, Expression])

RangeXNPV

RangeXNPV() returns the net present value for a schedule of cash flows (not necessarily periodic) represented by paired numbers in the expressions given by pmt and date. All payments are discounted based on a 365-day year.

[**RangeXNPV**](../../Scripting/RangeFunctions/RangeXNPV.htm)(discount\_rate,
values, dates[, Expression])

## Learn more

- [*Inter-record functions*](../InterRecordFunctions/inter-record-functions-charts.htm)
