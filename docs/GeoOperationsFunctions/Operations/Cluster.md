---
title: "Cluster"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Cluster.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Cluster

Cluster produces clusters from a point dataset based on geographic closeness between points. The cluster generation is controlled by the distance parameter, which defines how far away a point may be from the cluster it belongs to.

Example of Cluster

![A map displaying various points, with grouped points condensed into a single, larger point that displays the total number of points it contains.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-cluster.png "Click to view full size")

Cluster adds the following fields:

- <dataset key field>: The key field from the input dataset.
- ClusterID: ID of the cluster the point belongs to.
- Clusters.ClusterPoint: Center point for cluster.
- Clusters.PointCount: Number of original points belonging to the cluster.
- All fields except the key field from the input dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Cluster.
3. Under Distance, enter the maximum distance items can be apart from each other in the distance unit.
4. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
5. Under Tables, select the table to load.
6. Under Fields, select the fields to load.
7. Click Insert script.
