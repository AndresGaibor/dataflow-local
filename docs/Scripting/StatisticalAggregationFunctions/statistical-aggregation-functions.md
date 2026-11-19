---
title: "Statistical aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/statistical-aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions"]
---
Expand/Collapse all

# Statistical aggregation functions

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Statistical aggregation functions in the data load script

The following statistical [aggregation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/statistical-aggregation-functions.htm#glossary-0 "Glossary term") functions can be used in scripts.

Avg

Avg() finds the average value of the aggregated data in the expression over
a number of records as defined by a group by clause.

[**avg**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/avg.htm) ([distinct] expression)

Correl

Correl() returns
the aggregated correlation coefficient for a series of coordinates represented
by paired numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**correl**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/correl.htm)(x-expression, y-expression)

Fractile

Fractile()
finds the value that corresponds to the inclusive fractile (quantile) of the aggregated data in the expression over
a number of records as defined by a group by clause.

[**fractile**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractile.htm)(expression, fractile)

FractileExc

FractileExc()
finds the value that corresponds to the exclusive fractile (quantile) of the aggregated data in the expression over
a number of records as defined by a group by clause.

[**fractileexc**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/fractileexc.htm)(expression, fractile)

Kurtosis

Kurtosis() returns
the kurtosis of the data in the expression over
a number of records as defined by a group by clause.

[**kurtosis**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/kurtosis.htm) ([distinct ] expression
)

LINEST\_B

LINEST\_B() returns
the aggregated b value (y-intercept) of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_b**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_b.htm)(y-expression, x-expression [, y0 [, x0 ]])

LINEST\_df

LINEST\_DF() returns
the aggregated degrees of freedom of a linear regression defined by the
equation y=mx+b for a series of coordinates represented by paired numbers
in x-expression and y-expression iterated over a number of records as defined by a
group by clause.

[**linest\_df**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_df.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_f

This script function returns
the aggregated F statistic (r2/(1-r2)) of a linear
regression defined by the equation y=mx+b for a series of coordinates
represented by paired numbers in x-expression and y-expression iterated
over a number of records as defined by a group
by clause.

[**linest\_f**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_f.htm)(y-expression, x-expression [, y0 [, x0 ]])

LINEST\_m

LINEST\_M() returns
the aggregated m value (slope) of a linear regression defined by the equation
y=mx+b for a series of coordinates represented by paired numbers in x-expression and y-expression
iterated over a number of records as defined by a group by clause.

[**linest\_m**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_m.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_r2

LINEST\_R2() returns
the aggregated r2
value (coefficient of determination) of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by clause.

[**linest\_r2**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_r2.htm)(y-expression, x-expression [, y0 [, x0 ]])

LINEST\_seb

LINEST\_SEB() returns
the aggregated standard error of the b value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_seb**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_seb.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_sem

LINEST\_SEM() returns
the aggregated standard error of the m value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_sem**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_sem.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_sey

LINEST\_SEY() returns
the aggregated standard error of the y estimate of a linear regression
defined by the equation y=mx+b for a series of coordinates represented
by paired numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_sey**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_sey.htm) (y-expression, x-expression [, y0 [, x0 ]])

LINEST\_ssreg

LINEST\_SSREG() returns the
aggregated regression sum of squares of a linear regression defined by
the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_ssreg**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_ssreg.htm) (y-expression, x-expression [, y0 [, x0 ]])

Linest\_ssresid

LINEST\_SSRESID() returns
the aggregated residual sum of squares of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers in x-expression and y-expression iterated over a number
of records as defined by a group by
clause.

[**linest\_ssresid**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/linest_ssresid.htm) (y-expression, x-expression [, y0 [, x0 ]])

Median

Median() returns
the aggregated median of the values in the expression over a number of records as defined by a
group by clause.

[**median**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/median.htm)(expression)

Skew

Skew() returns
the skewness of expression over
a number of records as defined by a group by clause.

[**skew**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/skew.htm)([ distinct] expression)

Stdev

Stdev() returns
the standard deviation of the values given by the expression
over a number of records as defined by a group by clause.

[**stdev**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/stdev.htm)([distinct] expression)

Sterr

Sterr() returns
the aggregated standard error (stdev/sqrt(n)) for a series of values represented
by the expression iterated over a
number of records as defined by a group by clause.

[**sterr**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/sterr.htm) ([distinct] expression)

STEYX

STEYX() returns
the aggregated standard error of the predicted y-value for each x-value
in the regression for a series of coordinates represented by paired numbers
in x-expression and y-expression
iterated over a number of records as defined by a group by clause.

[**steyx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/steyx.htm) (y-expression, x-expression)

## Statistical aggregation functions in chart expressions

The following statistical aggregation functions can be used in [charts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StatisticalAggregationFunctions/statistical-aggregation-functions.htm#glossary-1 "Glossary term"):

Avg

Avg() returns the aggregated average of the expression or field iterated over the chart dimensions.

[**avg**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/avg.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} expr)

Correl

Correl() returns the aggregated correlation coefficient for two data sets. The correlation function is a measure of the relationship between the data sets and is aggregated for (x,y) value pairs iterated over the chart dimensions.

[**correl**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/correl.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} value1, value2 )

Fractile

Fractile() finds the value that corresponds to the inclusive fractile (quantile) of the aggregated data in the range given by the expression
iterated over the chart dimensions.

[**fractile**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/fractile.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} expr, fraction)

FractileExc

FractileExc() finds the value that corresponds to the exclusive fractile (quantile) of the aggregated data in the range given by the expression
iterated over the chart dimensions.

[**fractileexc**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/fractileexc.htm)({[SetExpression] [TOTAL [<fld {, fld}>]]} expr, fraction)

Kurtosis

Kurtosis() finds the kurtosis of the range of data aggregated in the expression or field iterated over the chart dimensions.

[**kurtosis**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/kurtosis.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} expr)

LINEST\_b

LINEST\_B() returns the
aggregated b value (y-intercept) of a linear regression defined by the equation y=mx+b for a series of coordinates represented by paired numbers in the expressions given by the expressions x\_value and y\_value, iterated over the chart dimensions.

[**linest\_r2**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_r2.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_df

LINEST\_DF() returns the
aggregated degrees of freedom of a linear regression defined by the equation
y=mx+b for a series of coordinates represented by paired numbers in the expressions given by x\_value and
y\_value, iterated over the chart dimensions.

[**linest\_df**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_df.htm)({[SetExpression] [TOTAL [<fld{, fld}>]]} y\_value, x\_value [, y0\_const [, x0\_const]])

LINEST\_f

LINEST\_F() returns the
aggregated F statistic (r2/(1-r2)) of a linear regression defined by the
equation y=mx+b for a series of coordinates represented by paired numbers in the expressions given by x\_value and
the y\_value, iterated over the chart dimensions.

[**linest\_f**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_f.htm)({[SetExpression] [TOTAL[<fld{, fld}>]]} y\_value, x\_value [, y0\_const [, x0\_const]])

LINEST\_m

LINEST\_M() returns the
aggregated m value (slope) of a linear regression defined by the equation 
y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart dimensions.

[**linest\_m**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_m.htm)({[SetExpression] [TOTAL[<fld{, fld}>]]} y\_value, x\_value [, y0\_const [, x0\_const]])

LINEST\_r2

LINEST\_R2() returns the
aggregated r2 value (coefficient of determination) of a linear regression
defined by the equation y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart dimensions.

[**linest\_r2**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_r2.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_seb

LINEST\_SEB() returns the
aggregated standard error of the b value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_seb**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_seb.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_sem

LINEST\_SEM() returns the
aggregated standard error of the m value of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_sem**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_sem.htm)([{set\_expression}][ distinct ] [total [<fld {,fld}>] ] y-expression,
x-expression [, y0 [, x0 ]] )

LINEST\_sey

LINEST\_SEY() returns the
aggregated standard error of the y estimate of a linear regression defined
by the equation y=mx+b for a series of coordinates represented by paired
numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_sey**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_sey.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_ssreg

LINEST\_SSREG() returns the
aggregated regression sum of squares of a linear regression defined by the equation y=mx+b for a series of coordinates represented by paired
numbers given by the expressions x\_value and y\_value, iterated over the chart
dimensions.

[**linest\_ssreg**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_ssreg.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

LINEST\_ssresid

LINEST\_SSRESID() returns the
aggregated residual sum of squares of a linear regression defined by the
equation y=mx+b for a series of coordinates represented by paired numbers in the expressions given by x\_value and y\_value, iterated over the chart dimensions.

[**linest\_ssresid**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/linest_ssresid.htm)({[SetExpression] [TOTAL [<fld{ ,fld}>]] }y\_value, x\_value[, y0\_const[, x0\_const]])

Median

Median() returns the median value of the range of values aggregated in the expression iterated over the chart dimensions.

[**median**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/median.htm)({[SetExpression] [TOTAL [<fld{, fld}>]]} expr)

MutualInfo

MutualInfo calculates the mutual information (MI) between two fields or between aggregated values in Aggr().

[**MutualInfo**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/MutualInfo.htm){[SetExpression] [DISTINCT] [TOTAL target, driver [, datatype [, breakdownbyvalue [, samplesize ]]])

Skew

Skew() returns the aggregated skewness
of the expression or field iterated over the chart dimensions.

[**skew**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/skew.htm){[SetExpression] [DISTINCT] [TOTAL [<fld{ ,fld}>]]} expr)

Stdev

Stdev() finds the standard deviation of the range of data aggregated in the expression or field iterated over the chart dimensions.

[**stdev**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/stdev.htm)({[SetExpression] [DISTINCT] [TOTAL [<fld{, fld}>]]} expr)

Sterr

Sterr() finds the value of the standard error of the mean, (stdev/sqrt(n)), for the series of values aggregated in the expression iterated over the chart dimensions.

[**sterr**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/sterr.htm)({[SetExpression] [DISTINCT] [TOTAL[<fld{, fld}>]]} expr)

STEYX

STEYX() returns the
aggregated standard error when predicting y-values for each x-value in a linear regression given by a series of coordinates represented by paired numbers in the expressions given by y\_value and x\_value.

[**steyx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/StatisticalAggregationFunctionsinCharts/steyx.htm){[SetExpression] [TOTAL [<fld{, fld}>]]} y\_value, x\_value)
