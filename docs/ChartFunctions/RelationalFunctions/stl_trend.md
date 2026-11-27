---
title: "STL_Trend  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RelationalFunctions/stl_trend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Relational functions"]
---

# STL\_Trend - chart function

STL\_Trend is a time series decomposition function. Along with STL\_Seasonal and STL\_Residual, this function is used to decompose a time series into seasonal, trend, and residual components. In the context of the STL algorithm, time series decomposition is used to identify both a recurring seasonal pattern and a general trend, given an input metric and other parameters. The STL\_Trend function will identify a general trend, independent of seasonal patterns or cycles, from time series data.

The three STL functions are related to the input metric through a simple sum:

STL\_Trend + STL\_Seasonal + STL\_Residual = Input metric

STL (seasonal and trend decomposition using Loess) employs data smoothing techniques, and through its input parameters, allows the user to adjust the periodicity of the calculations it performs. This periodicity determines how the time dimension of the input metric (a measure) is segmented in the analysis.

At minimum, STL\_Trend takes an input metric (target\_measure) and an integer value for its period\_int, returning a floating-point value. The input metric will be in the form of an aggregation that varies along the time dimension. Optionally, you can include values for the seasonal\_smoother and trend\_smoother to adjust the smoothing algorithm.

You can work with this function by entering it directly into the expression editor for a chart, or by adding the Time series decomposition modifier to a measure. It is also available for use in Insight Advisor as an analysis type. For more information, see [*Time series decomposition*](../../Measures/modifiers.htm#Time) and [*Insight Advisor analysis types*](../../Insights/insight-analysis-types.htm).

Syntax:

STL\_Trend(target\_measure, period\_int [,seasonal\_smoother [,trend\_smoother]])

Return data type: dual

Arguments

| Argument | Description |
| --- | --- |
| target\_measure | The measure to decompose into Seasonal and Trend components. This should be a measure such as Sum(Sales) or Sum(Passengers) that varies along the time dimension.  This must not be a constant value. |
| period\_int | The periodicity of the dataset. This parameter is an integer value representing the number of discrete steps that make up one period, or seasonal cycle, of the signal.  For instance, if the time series is segmented into one section for each quarter of the year, you must set the period\_int to a value of 4 to define the periodicity as Year. |
| seasonal\_smoother | Length of the seasonal smoother. This must be an odd integer. The seasonal smoother uses data for a particular phase in the seasonal variation, over a number of periods. One discrete step of the time dimension is used from each period. The seasonal smoother indicates the number of periods used for smoothing.  For example, if the time dimension is segmented by month and the period is Year (12), the seasonal component will be computed so that each particular month of each year is calculated from data for the same month, both in that year and in adjacent years. The seasonal\_smoother value is the number of years used for smoothing. |
| trend\_smoother | Length of the trend smoother. This must be an odd integer. The trend smoother uses the same time scale as the period\_int parameter, and its value is the number of granules used for smoothing.  For example, if a time series is segmented by month, the trend smoother will be the number of months used for smoothing. |

The STL\_Trend chart function is often used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*STL\_Seasonal - chart function*](stl_seasonal.htm) | This is the function used to compute the seasonal component of a time series. |
| [*STL\_Residual - chart function*](stl_residual.htm) | When breaking down an input metric into seasonal and trend component, part of the [measures](#glossary-0 "Glossary term") variation will not fit within either of the two main components. The STL\_Residual function computes this portion of the decomposition. |

For a tutorial with a full example showing how to use this function, see [*Tutorial - Time series decomposition in Qlik Sense*](tutorial-time-series-decomposition.htm).
