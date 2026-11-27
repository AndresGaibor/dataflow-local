---
title: "KMeansCentroidND - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RelationalFunctions/KMeansCentroidND.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Relational functions"]
---

# KMeansCentroidND - chart function

KMeansCentroidND() evaluates the rows of the chart by applying k-means clustering, and for each chart row displays the desired coordinate of the cluster this data point has been assigned to. The columns that are used by the clustering algorithm are determined by the parameters coordinate\_1, coordinate\_2, etc., up to n columns. These are all aggregations. The number of clusters that are created is determined by the num\_clusters parameter.

KMeansCentroidND returns one value per row. The returned value is a dual and is one of the coordinates of the position corresponding to the cluster center the data point has been assigned to.

Syntax:

KMeansCentroidND((num\_clusters, num\_iter, coordinate\_no, coordinate\_1, coordinate\_2 [,coordinate\_3 [, ...]])

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| num\_clusters | Integer that specifies the number of clusters. |
| num\_iter | The number of iterations of clustering with reinitialized cluster centers. |
| coordinate\_no | The desired coordinate number of the centroids (corresponding, for example, to the x, y, or z axis). |
| coordinate\_1 | The aggregation that calculates the first coordinate, usually the x-axis (of a scatter chart that can be made from the chart). The additional parameters calculate the second, third, and fourth coordinates, etc. |

## Auto-clustering

KMeans functions support auto-clustering using a method called depth difference (DeD). When a user sets 0 for the number of clusters, an optimal number of clusters for that dataset is determined. Note that while an integer for the number of clusters (k) is not explicitly returned, it is calculated within the KMeans algorithm. For example, if 0 is specified in the function for the value of KmeansPetalClusters or set through a variable input box, cluster assignments are automatically calculated for the dataset based on an optimal number of clusters.
