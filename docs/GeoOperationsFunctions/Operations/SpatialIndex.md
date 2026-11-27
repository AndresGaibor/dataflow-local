---
title: "Spatial index"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/SpatialIndex.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Spatial index

Spatial index generates a spatial index for a dataset for use with the Auto select visible feature in map charts. Field selections are updated based on the data displayed in map charts. For more information, see [*Setting the zoom and selection behavior for maps*](../../../Sense_Hub/Visualizations/Map/create-maps.htm#Zoom).

Spatial index returns these fields:

- <dataset key field>: A key field linking the values from SpatialIndex with the source field from the dataset.
- SpatialIndex: Contains grid coordinates for the items in the key field.
- SpatialIndexLevel<num>: Contains grid coordinates for the items in the key field for use with Auto select visible for each level. A field is created for each of the levels set in Number of levels.
- All fields except the key field from dataset are prefixed with the dataset name.

If you have multiple spatial indexes, rename the fields created by Spatial index. For example:

[CountrySpatialindexResultTable]:
Load \* Extension GeoOperations.ScriptEval('
SELECT Country, SpatialIndex as CountrySpatialIndex, SpatialIndexLevel2 as CountrySpatialIndexLevel2, SpatialIndexLevel3 as CountrySpatialIndexLevel3, SpatialIndexLevel4 as CountrySpatialIndexLevel4, SpatialIndexLevel5 as CountrySpatialIndexLevel5, SpatialIndexLevel6 as CountrySpatialIndexLevel6 FROM SpatialIndex(gridSize="0.04", gridWidthHeightRatio="1.5", nLevels="6", levelFactor="4") DATASOURCE dataset INTABLE keyField="Country", crs="auto", namedPointField="Country"
', Sales);

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Spatial Index.
3. Under Operation, adjust the parameters as needed.

   - Grid size (degrees): Specifies the height (in degrees) of an individual spatial index cell at the most detailed level. An appropriate value is the side length of the map view that users commonly zoom into.

     The default value is 0.04.
   - Grid width / height ratio: Specifies the ratio that determines the shape of grid cells used for spatial indexing. The formula for the optimal width/height ratio is 1/cos(latitude), for example 1 at the equator, 1.15 at latitude ±30 deg and 2 at latitude ±60 deg.

     The default value is 1.5.
   - Number of levels: Specifies the number of spatial index levels to generate. Each level has cells with side lengths scaled by the level factor compared to the level below.

     The default value is 6.
   - Level factor: Specifies the factor by which to multiply the spatial index cell dimensions for each level.

     The default value is 4.
4. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)[*Loading a previously loaded table*](Load.htm#Loading4)

   You must specify a key field.
5. Under Tables, select the table to load.
6. Under Fields, select the fields to load.
7. Click Insert script.
