---
title: "Binning"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Binning.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Binning

Binning generates rectangular or hexagonal bins for a point dataset. This allows you to efficiently display an overview of aggregated point data.

Example of Binning

![A map divided up into color-coded hexagonal bins.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-binning.png "Click to view full size")

Binning returns the following fields:

- <dataset key field>: The key field from the input dataset.
- BinId: Identity for the bin.
- BinTable.BinPolygon: The polygon for the bin.
- BinTable.CenterPoint: Point in center of the bin.
- All fields except the key field from dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Binning.
3. Under Type, select the bin shape.
4. Under Grid size, enter the height of an individual bin in degrees.

   One degree is approximately 10,000 m
5. Optionally, under Grid width / Grid height ratio, enter the ratio of the bins.

   By default, the value is 1.5.
6. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
7. Under Tables, select the table to load.
8. Under Fields, select the fields to load.
9. Click Insert script.
