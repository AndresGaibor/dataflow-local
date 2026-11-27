---
title: "Dissolve"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Dissolve.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Dissolve

Dissolve combines and simplifies areas to create new areas. This is typically used for building custom areas that are built up by smaller well-defined areas, such as postal areas or administrative areas.

Example of Dissolve

![A map displaying various states dissolved into simplified areas.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-dissolve.png "Click to view full size")

When you use Dissolve, you specify a dissolve field that contains the new areas to create custom geometries for. Dissolve compares that field to the key field in your selected dataset. The dissolve field and key fields can be in separate datasets.

Dissolve returns the following fields:

- <dissolveField>: The field specified as the dissolve field.
- DissolvedPolygon: The geometries of the new dissolved areas.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Dissolve.
3. Under Dissolved field, enter the field to use to combine values from the key field

   Under Resolution, select the resolution to use for the geometries created by Dissolve.

   The following resolutions are available:

   - AutoLow: A resolution that is half that of Auto.
   - Auto: A standard resolution that calculated based on the data.
   - AutoHigh: A resolution twice that of Auto.
   - Source: A resolution with no simplification of geometries.

     Information note

     Overlaps of polygons are removed in all resolutions except Source. If your dissolved field contains overlapping areas, select Source.
4. Under Sources of area to dissolve, select Dataset 1 or Dataset 2.

   If you select Dataset 2, enter the key field containing the areas to dissolve.
5. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   If you are only using one dataset, the key field must be the field containing the areas to dissolve.

   If you are using two datasets, the key field must be the same as the dissolved field.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
6. Optionally, if you are using a second dataset, under Dataset 2, select the type of data to load and the parameters.

   The key field must contain the areas to dissolve.
7. Under Tables, select the table to load.
8. Under Fields, select the fields to load.
9. Click Insert script.
