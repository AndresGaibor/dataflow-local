---
title: "Relational functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RelationalFunctions/relational-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Relational functions

Expand/Collapse all

# Relational functions

This is a group of functions that calculate properties of individual dimensional values in a chart, using already aggregated numbers.

The functions are relational in the sense that the function output depends not only on the value of the data point itself, but also on the value’s relation to other data points. For example, a rank cannot be calculated without a comparison with other dimensional values.

These functions can only be used in chart expressions. They cannot be used in the load script.

A dimension is needed in the chart, since this defines the other data points needed for the comparison. Consequently, a relational function is not meaningful in a dimensionless chart (for example, a KPI object).

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

## Ranking functions

Information noteSuppression of zero values is automatically disabled when these functions are used. NULL values are disregarded.

Rank

Rank() evaluates the rows of the chart in the expression, and for each row, displays the relative position of the value of the dimension evaluated in the expression. When evaluating the expression, the function compares
the result with the result of the other rows containing the current column segment and returns the ranking of the current row within the segment.

[**rank**](rank.htm)([TOTAL [<fld {, fld}>]] expr[, mode[, fmt]])

HRank

HRank() evaluates the expression, and compares the result with the result of the other columns containing the current row segment of a pivot table. The function then returns the ranking of the current column
within the segment.

[**HRank**](HRank.htm)([TOTAL] expr[, mode[, fmt]])

## Clustering functions

KMeans2D

KMeans2D() evaluates the rows of the chart by applying k-means clustering, and for each chart row displays the cluster id of the cluster this data point has been assigned to. The columns that are used by the clustering algorithm are determined by the parameters coordinate\_1, and coordinate\_2, respectively. These are both aggregations. The number of clusters that are created is determined by the num\_clusters parameter. Data can be optionally normalized by the norm parameter.

[**KMeans2D**](KMeans2D.htm)(num\_clusters, coordinate\_1, coordinate\_2 [, norm])

KMeansND

KMeansND() evaluates the rows of the chart by applying k-means clustering, and for each chart row displays the cluster id of the cluster this data point has been assigned to. The columns that are used by the clustering algorithm are determined by the parameters coordinate\_1, and coordinate\_2, etc., up to n columns. These are all aggregations. The number of clusters that are created is determined by the num\_clusters parameter.

[**KMeansND**](KMeansND.htm)(num\_clusters, num\_iter, coordinate\_1, coordinate\_2 [,coordinate\_3 [, ...]])

KMeansCentroid2D

KMeansCentroid2D() evaluates the rows of the chart by applying k-means clustering, and for each chart row displays the desired coordinate of the cluster this data point has been assigned to. The columns that are used by the clustering algorithm are determined by the parameters coordinate\_1, and coordinate\_2, respectively. These are both aggregations. The number of clusters that are created is determined by the num\_clusters parameter. Data can be optionally normalized by the norm parameter.

[**KMeansCentroid2D**](KMeansCentroid2D.htm)(num\_clusters, coordinate\_no, coordinate\_1, coordinate\_2 [, norm])

KMeansCentroidND

KMeansCentroidND() evaluates the rows of the chart by applying k-means clustering, and for each chart row displays the desired coordinate of the cluster this data point has been assigned to. The columns that are used by the clustering algorithm are determined by the parameters coordinate\_1, coordinate\_2, etc., up to n columns. These are all aggregations. The number of clusters that are created is determined by the num\_clusters parameter.

[**KMeansCentroidND**](KMeansCentroidND.htm)(num\_clusters, num\_iter, coordinate\_no, coordinate\_1, coordinate\_2 [,coordinate\_3 [, ...]])

## Time series decomposition functions

STL\_Trend

STL\_Trend is a time series decomposition function. Along with STL\_Seasonal and STL\_Residual, this function is used to decompose a time series into seasonal, trend, and residual components. In the context of the STL algorithm, time series decomposition is used to identify both a recurring seasonal pattern and a general trend, given an input metric and other parameters. The STL\_Trend function will identify a general trend, independent of seasonal patterns or cycles, from time series data.

[**stl\_trend**](stl_trend.htm)(target\_measure, period\_int [,seasonal\_smoother [,trend\_smoother]])

STL\_Seasonal

STL\_Seasonal is a time series decomposition function. Along with STL\_Trend and STL\_Residual, this function is used to decompose a time series into seasonal, trend, and residual components. In the context of the STL algorithm, time series decomposition is used to identify both a recurring seasonal pattern and a general trend, given an input metric and other parameters. The STL\_Seasonal function can identify a seasonal pattern within a time series, separating this from the general trend displayed by the data.

[**stl\_seasonal**](stl_seasonal.htm)(target\_measure, period\_int [,seasonal\_smoother [,trend\_smoother]])

STL\_Residual

STL\_Residual is a time series decomposition function. Along with STL\_Seasonal and STL\_Trend, this function is used to decompose a time series into seasonal, trend, and residual components. In the context of the STL algorithm, time series decomposition is used to identify both a recurring seasonal pattern and a general trend, given an input metric and other parameters. In performing this operation, part of the variation in the input metric will neither fit within the seasonal nor the trend component, and will be defined as the residual component. The STL\_Residual chart function captures this portion of the calculation.

[**stl\_residual**](stl_residual.htm)(target\_measure, period\_int [,seasonal\_smoother [,trend\_smoother]])
