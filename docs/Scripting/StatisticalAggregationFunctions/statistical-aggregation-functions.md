---
title: "Statistical aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/statistical-aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---

# Statistical aggregation functions

Expand/Collapse all

# Statistical aggregation functions

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Statistical aggregation functions in the data load script

The following statistical [aggregation](#glossary-0 "Glossary term") functions can be used in scripts.

Avg

Avg() finds the average value of the aggregated data in the expression over
a number of records as defined by a group by clause.

[**avg**](avg.htm) ([distinct] expression)

Correl

Correl() returns
the aggregated correlation coefficient for a series of coordinates represented
by paired numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**correl**](correl.htm)(x-expression, y-expression)

Fractile

Fractile()
finds the value that corresponds to the inclusive fractile (quantile) of the aggregated data in the expression over
a number of records as defined by a group by clause.

[**fractile**](fractile.htm)(expression, fractile)

FractileExc

FractileExc()
finds the value that corresponds to the exclusive fractile (quantile) of the aggregated data in the expression over
a number of records as defined by a group by clause.

[**fractileexc**](fractileexc.htm)(expression, fractile)

Kurtosis

Kurtosis() returns
the kurtosis of the data in the expression over
a number of records as defined by a group by clause.

[**kurtosis**](kurtosis.htm) ([distinct ] expression
)

LINEST\_B

LINEST\_B() returns
the aggregated b value (y-intercept) of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_b**](linest_b.htm)(y-expression, x-expression [, y0 [, x0 ]])

LINEST\_df

LINEST\_DF() returns
the aggregated degrees of freedom of a linear regression defined by the
equation y=mx+b for a series of coordinates represented by paired numbers
in x-expression and y-expression iterated over a number of records as defined by a
group by clause.

[**linest\_df**](linest_df.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_f

This script function returns
the aggregated F statistic (r2/(1-r2)) of a linear
regression defined by the equation y=mx+b for a series of coordinates
represented by paired numbers in x-expression and y-expression iterated
over a number of records as defined by a group
by clause.

[**linest\_f**](linest_f.htm)(y-expression, x-expression [, y0 [, x0 ]])

LINEST\_m

LINEST\_M() returns
the aggregated m value (slope) of a linear regression defined by the equation
y=mx+b for a series of coordinates represented by paired numbers in x-expression and y-expression
iterated over a number of records as defined by a group by clause.

[**linest\_m**](linest_m.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_r2

LINEST\_R2() returns
the aggregated r2
value (coefficient of determination) of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by clause.

[**linest\_r2**](linest_r2.htm)(y-expression, x-expression [, y0 [, x0 ]])

LINEST\_seb

LINEST\_SEB() returns
the aggregated standard error of the b value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_seb**](linest_seb.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_sem

LINEST\_SEM() returns
the aggregated standard error of the m value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_sem**](linest_sem.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_sey

LINEST\_SEY() returns
the aggregated standard error of the y estimate of a linear regression
defined by the equation y=mx+b for a series of coordinates represented
by paired numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_sey**](linest_sey.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_ssreg

LINEST\_SSREG() returns the
aggregated regression sum of squares of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_ssreg**](linest_ssreg.htm) (y-expression, x-expression [, y0 [, x0 ]])

Linest\_ssresid

LINEST\_SSRESID() returns
the aggregated residual sum of squares of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_ssresid**](linest_ssresid.htm) (y-expression, x-expression [, y0 [, x0 ]])

Median

Median() returns
the aggregated median of the values in the expression over a number of records as defined by a
group by clause.

[**median**](median.htm)(expression)

Skew

Skew() returns
the skewness of expression over
a number of records as defined by a group by clause.

[**skew**](skew.htm)([ distinct] expression)

Stdev

Stdev() returns
the standard deviation of the values given by the expression
over a number of records as defined by a group by clause.

[**stdev**](stdev.htm)([distinct] expression)

Sterr

Sterr() returns
the aggregated standard error (stdev/sqrt(n)) for a series of values represented
by the expression iterated over a
number of records as defined by a group by clause.

[**sterr**](sterr.htm) ([distinct] expression)

STEYX

STEYX() returns
the aggregated standard error of the predicted y-value for each x-value
in the regression for a series of coordinates represented by paired numbers
in x-expression and y-expression
iterated over a number of records as defined by a group by clause.

[**steyx**](steyx.htm) (y-expression, x-expression)

## Statistical aggregation functions in chart expressions

The following statistical aggregation functions can be used in [charts](#glossary-1 "Glossary term"):

Avg

Avg() returns the aggregated average of the expression or field iterated over the chart dimensions.

[**avg**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/avg.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} expr)

Correl

Correl() returns the aggregated correlation coefficient for two data sets. The correlation function is a measure of the relationship between the data sets and is aggregated for (x,y) value pairs iterated over the chart dimensions.

[**correl**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/correl.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} value1, value2 )

Fractile

Fractile() finds the value that corresponds to the inclusive fractile (quantile) of the aggregated data in the range given by the expression
iterated over the chart dimensions.

[**fractile**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/fractile.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} expr, fraction)

FractileExc

FractileExc() finds the value that corresponds to the exclusive fractile (quantile) of the aggregated data in the range given by the expression
iterated over the chart dimensions.

[**fractileexc**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/fractileexc.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} expr, fraction)

Kurtosis

Kurtosis() finds the kurtosis of the range of data aggregated in the expression or field iterated over the chart dimensions.

[**kurtosis**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/kurtosis.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} expr)

LINEST\_b

LINEST\_B() returns the
aggregated b value (y-intercept) of a linear regression defined by the equation y=mx+b for a series of coordinates represented by paired numbers in the expressions given by the expressions x\_value and y\_value, iterated over the chart dimensions.

[**linest\_r2**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_r2.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_df

LINEST\_DF() returns the
aggregated degrees of freedom of a linear regression defined by the equation
y=mx+b for a series of coordinates represented by paired numbers in the expressions given by x\_value and
y\_value, iterated over the chart dimensions.

[**linest\_df**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_df.htm)({[SetExpression] [TOTAL [<fld{, fld}>]]} y\_value, x\_value [, y0\_const [, x0\_const]])

LINEST\_f

LINEST\_F() returns the
aggregated F statistic (r2/(1-r2)) of a linear regression defined by the
equation y=mx+b for a series of coordinates represented by paired numbers in the expressions given by x\_value and
the y\_value, iterated over the chart dimensions.

[**linest\_f**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_f.htm)({[SetExpression] [TOTAL[<fld{, fld}>]]} y\_value, x\_value [, y0\_const [, x0\_const]])

LINEST\_m

LINEST\_M() returns the
aggregated m value (slope) of a linear regression defined by the equation
y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart dimensions.

[**linest\_m**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_m.htm)({[SetExpression] [TOTAL[<fld{, fld}>]]} y\_value, x\_value [, y0\_const [, x0\_const]])

LINEST\_r2

LINEST\_R2() returns the
aggregated r2 value (coefficient of determination) of a linear regression
defined by the equation y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart dimensions.

[**linest\_r2**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_r2.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_seb

LINEST\_SEB() returns the
aggregated standard error of the b value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_seb**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_seb.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_sem

LINEST\_SEM() returns the
aggregated standard error of the m value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_sem**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_sem.htm)([{set\_expression}][ distinct ] [total [<fld {,fld}>] ] y-expression,
x-expression [, y0 [, x0 ]] )

LINEST\_sey

LINEST\_SEY() returns the
aggregated standard error of the y estimate of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_sey**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_sey.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_ssreg

LINEST\_SSREG() returns the
aggregated regression sum of squares of a linear regression defined by the equation y=mx+b for a series of coordinates represented by paired
numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_ssreg**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_ssreg.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_ssresid

LINEST\_SSRESID() returns the
aggregated residual sum of squares of a linear regression defined by the
equation y=mx+b for a series of coordinates represented by paired numbers in the expressions given by x\_value and y\_value, iterated over the chart dimensions.

[**linest\_ssresid**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_ssresid.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

Median

Median() returns the median value of the range of values aggregated in the expression iterated over the chart dimensions.

[**median**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/median.htm)({[SetExpression] [TOTAL [<fld{, fld}>]]} expr)

MutualInfo

MutualInfo calculates the mutual information (MI) between two fields or between aggregated values in Aggr().

[**MutualInfo**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/MutualInfo.htm){[SetExpression] [DISTINCT] [TOTAL target, driver [, datatype [, breakdownbyvalue [, samplesize ]]])

Skew

Skew() returns the aggregated skewness
of the expression or field iterated over the chart dimensions.

[**skew**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/skew.htm){[SetExpression] [DISTINCT] [TOTAL [<fld{ ,fld}>]]} expr)

Stdev

Stdev() finds the standard deviation of the range of data aggregated in the expression or field iterated over the chart dimensions.

[**stdev**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/stdev.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} expr)

Sterr

Sterr() finds the value of the standard error of the mean, (stdev/sqrt(n)), for the series of values aggregated in the expression iterated over the chart dimensions.

[**sterr**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/sterr.htm)({[SetExpression] [DISTINCT] [TOTAL[<fld{, fld}>]]} expr)

STEYX

STEYX() returns the
aggregated standard error when predicting y-values for each x-value in a linear regression given by a series of coordinates represented by paired numbers in the expressions given by y\_value and x\_value.

[**steyx**](../../ChartFunctions/StatisticalAggregationFunctionsinCharts/steyx.htm){[SetExpression] [TOTAL [<fld{, fld}>]]} y\_value, x\_value)
