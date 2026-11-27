---
title: "KMeansCentroid2D - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RelationalFunctions/KMeansCentroid2D.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Relational functions"]
---

# KMeansCentroid2D - chart function

KMeansCentroid2D() evaluates the rows of the chart by applying k-means clustering, and for each chart row displays the desired coordinate of the cluster this data point has been assigned to. The columns that are used by the clustering algorithm are determined by the parameters coordinate\_1, and coordinate\_2, respectively. These are both aggregations. The number of clusters that are created is determined by the num\_clusters parameter. Data can be optionally normalized by the norm parameter.

KMeansCentroid2D returns one value per data point. The returned value is a dual and is one of the coordinates of the position corresponding to the cluster center the data point has been assigned to.

Syntax:

KMeansCentroid2D(num\_clusters, coordinate\_no, coordinate\_1, coordinate\_2 [, norm])

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| num\_clusters | Integer that specifies the number of clusters. |
| coordinate\_no | The desired coordinate number of the centroids (corresponding, for example, to the x, y, or z axis). |
| coordinate\_1 | The aggregation that calculates the first coordinate, usually the x-axis of the scatter chart that can be made from the chart. The additional parameter, coordinate\_2, calculates the second coordinate. |
| norm | The optional normalization method applied to datasets before KMeans clustering.  Possible values:  0 or ‘none’ for no normalization  1 or ‘zscore’ for z-score normalization  2 or ‘minmax’ for min-max normalization  If no parameter is supplied or if the supplied parameter is incorrect, no normalization is applied.  Z-score normalizes data based on feature mean and standard deviation. Z-score does not ensure each feature has the same scale but it is a better approach than min-max when dealing with outliers.  Min-max normalization ensures that the features have the same scale by taking the minimum and maximum values of each and recalculating each datapoint. |

## Auto-clustering

KMeans functions support auto-clustering using a method called depth difference (DeD). When a user sets 0 for the number of clusters, an optimal number of clusters for that dataset is determined. Note that while an integer for the number of clusters (k) is not explicitly returned, it is calculated within the KMeans algorithm. For example, if 0 is specified in the function for the value of KmeansPetalClusters or set through a variable input box, cluster assignments are automatically calculated for the dataset based on an optimal number of clusters.
