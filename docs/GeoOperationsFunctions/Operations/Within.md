---
title: "Within"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Within.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Within

Within returns the relations between two datasets where a geometry in one dataset (enclosed) is completely inside the area in the other dataset (enclosing). This creates a table that maps between the key in enclosed and the key in enclosing for all found relations.

Example of Within

![A map displaying points that are within a set of specified areas.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-within.png "Click to view full size")

You can use Within for finding which areas the other data is in as a kind of reverse geocoding. For example, you could use GPS position with Within to discover which administrative area they are in.

Tip note

To compensate for inaccuracies in data, it is sometimes better to use Closest instead of Within. For example, if you have point data in coastal areas which you want to relate to administrative areas, small inaccuracies can make points fall slightly outside of the areas.

Returns the following fields:

- <enclosed name>\_<enclosing name>\_RelationId: A key generated for the relation between the two geometries.
- <enclosed key field>: The key field from the first dataset.
- <enclosing key field>: The key field from the second dataset.
- All fields except the key field from the enclosed dataset, prefixed with the dataset name.
- All fields except the key field from the enclosing dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Within.
3. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The key field in Dataset 1 must be the data that is enclosed within the other data.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
4. Under Dataset 2, select the type of data source to use in the operation and its parameters.

   The key field in Dataset 2 must be the data that encloses the other data.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
5. Under Tables, select the table to load.
6. Under Fields, select the fields to load.
7. Click Insert script.
