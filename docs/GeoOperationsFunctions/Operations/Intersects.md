---
title: "Intersects"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Intersects.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Intersects

Intersects creates a table that maps all objects that intersect between key fields in two dataset. If both datasets contain polygons, the relative overlap area compared to the areas in the respective datasets are returned.

Example of Intersects

![A map displaying the intersections of states in two different areas.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-intersect.png "Click to view full size")

You can limit the number of intersecting geometries that should be mapped by specifying the number of geometries to map in Intersects count. Then the most intersecting geometries are returned in order. The operation is symmetric if Intersects count is not specified.

Returns the following fields:

- <dataset1 name>\_<dataset2 name>\_RelationId: A key generated for the relation between the two geometries.
- <dataset1 key field>: The key field from the first dataset.
- <dataset2 key field>: The key field from the second dataset.
- <dataset1 name>.RelativeOverlap: The overlap compared to the polygon in the first dataset. Only returned if both datasets contain polygons. There is a performance penalty for requesting this field.
- <dataset2 name>.RelativeOverlap: The overlap compared to the polygon in the second dataset. Only returned if both datasets contain polygons. There is a performance penalty for requesting this field.
- All fields except the key fields from the first dataset, prefixed with the dataset name.
- All fields except the key fields from the second dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Intersects.
3. Optionally under Intersects count, enter the maximum number of intersecting geometries in the second dataset to return per geometries in the first dataset. Only the geometries that intersect the most (largest overlapping area or length) are returned.

   The default value, 0,` returns all intersecting geometries.
4. Under Use two datasets, select to use two key field from two datasets or a key field from a single dataset.
5. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
6. If you are using a second dataset, under Dataset 2, select the type of data to load and the parameters.

   For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
7. Under Tables, select the table to load.
8. Under Fields, select the fields to load.
9. Click Insert script.
