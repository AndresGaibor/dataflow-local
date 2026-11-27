---
title: "Simplify"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Simplify.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Simplify

Simplify simplifies line and area geometries in a dataset. Loading geographic data with Simplify instead of Load creates more efficient geometries that are faster to display.

Example of Simplify

![A map of states, simplified to load faster and look better.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-simplify.png "Click to view full size")

The degree of simplification is calculated automatically based on area, number of objects and size of objects. You can adjust this simplification to a higher or lower resolution. Area simplification is done with an algorithm that handles topologies and can remove gaps and join islands. Line simplification is done with a breakpoint reduction algorithm.

Information note

Overlaps of polygons are removed from the output.

Simplify returns the following fields:

- <dataset key field>: The key field from the dataset.
- Simplified\_<geometry field name>: Simplified versions of the original geometries.
- All fields except the key field from dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Simplify.
3. Under Resolution, select the resolution to simplify areas or lines to. The following resolutions are available:

   - AutoLow: A resolution that is half the resolution of Auto.
   - Auto: A simplified resolution calculated based on the data.
   - AutoHigh: A resolution that is double the resolution of Auto.
4. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
5. Under Tables, select the table to load.
6. Under Fields, select the fields to load.
7. Click Insert script.
