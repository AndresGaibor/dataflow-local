---
title: "Map chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/Map.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Map chart

Maps enable you to view your data geographically.

Maps have many ways to present your data. You can add multiple layers to your map to display different types of information on the same map. You can set a custom scope for locations so that if two locations have the same name, you display the locations and their data correctly. You can use drill-down [dimensions](#glossary-0 "Glossary term") to create a hierarchy of geographic areas for selection. You can limit the pan of a map to a specific view and scope of the map, such as a region of interest, out of which users cannot pan or zoom out. You can add custom base maps to your map and use non-WGS-84 coordinates.

Map with density layer displaying number of global volcanic eruptions.

![Map with density layer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DensityLayer.png "Click to view full size")

## When to use maps

You can use a map to show the geographical distribution of offices, stores, and other sites of business interest. You can visualize not only locations but also sales values and other [measures](#glossary-1 "Glossary term") and display the value differences by bubble size or color.

### Advantages

The map is a versatile [visualization](#glossary-2 "Glossary term") that efficiently presents the geographical distribution of key values related to location or area.

### Disadvantages

With a large number of values, it may be hard to get a good overview. Values may be placed on top of each other and not visible until zoomed in.

## Server connection requirements

In order for a Qlik Sense map chart to be able to perform location lookup and show a background map (base map and layers), your web browser needs to be able to establish a connection with both of the following servers on port 443 (HTTPS):

- maps.qlikcloud.com (required for location lookups and background map)
- ibasemaps-api.arcgis.com (required for Satellite base map)

For more information, refer to the Map service connection requirements on [Ports used by user web browser](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/QSEoW/Deploy_QSEoW/Ports.htm#anchor-3).

## Base map

The base map provides the background for the data contained in your layers. You can select your base map in Map settings. Qlik Sense has four default base maps:

- Default: An OpenStreetMap-based map.
- Pale: A paler version of Default.
- Dark: A darker version of Default.
- Satellite: A satellite image map.
- None: No base map.

Additionally, custom base maps can be added using background layers to add your own custom base maps. For example, you could add the floor plan of an airport or office as a custom base map.

## Layers

Layers contain visualized dimension and measure data that is displayed over your map. You can stack layers on top of each other. You can also control at what zoom levels different layers appear in or have layers that appear only if other values in a drill-down dimension are selected. This enables you to create different levels of detail as you make [selections](#glossary-3 "Glossary term") and zoom in and out of areas of interest on your map. The following layers are available:

- Point layer: A point layer overlays individual locations on a map, representing them with shapes.

  [*Point layers*](point-layer.htm)
- Area layer: An area layer presents areas on your map, such as countries or states. With polygon geometry loaded into a [field](#glossary-4 "Glossary term"), it can present any custom area.

  [*Area layers*](area-layer.htm)
- Line layer: A line layer enables you to display lines between points on your map.

  [*Line layers*](line-layer.htm)
- Density layer: A density layer enables you to visualize the density of points in an area using a color ramp.

  [*Density layers*](density-layer.htm)
- Chart layer: A chart layer enables you to display small pie charts or bar charts over locations in your map.

  [*Chart layers*](chart-layer.htm)
- Background layer: Background layers enable you to display a custom base map for your map visualization.

  [*Background layers*](background-layer.htm)

Layers that use drill-down dimensions can be used to create drill-down layers. Drill-down layers enable you to drill-down different hierarchical dimensions in a single layer or in multiple layers. You could, for example, switch between area and point layers as selections are made. For more information, see [*Drill-down layers*](drill-down-layer.htm). For an example map that uses drill-down dimensions and layers, see [*Controlling visible map data with drill-down layers*](MapChart-Drilldown.htm).

## Location data for map layers

Maps support several ways for determining locations in a layer. You can use the dimension added to the layer. You can alternatively specify fields containing location data for the layer, if the layer dimension does not contain geographic data. In the Location properties, you can specify additional parameters for the location field, such as adding additional fields that include country or administrative area information. For example, if you have a field containing custom area geometries and a field containing the names of the custom areas, you can set the name field as the dimension and then set the area geometry field as the location field in Location in the map properties.

Locations can be either geometries or names of locations such as names of countries, regions, cities, postal codes etc. Layer locations can be defined using fields that contain names and codes. Qlik Sense can identify the following types of locations:

- Continent names
- Country names
- ISO alpha 2 country codes
- ISO alpha 3 country codes
- First-order administrative area names, such as a state or province names
- Second-order administrative area names
- Third-order administrative area names
- Fourth-order administrative area names
- Postal codes or ZIP Codes
- City, village, or other populated place names
- IATA airport codes
- ICAO airport codes

Information note

Availability of locations may vary by country. If the named location is not available, use coordinate or area data for the location.

Qlik Sense uses map and location data obtained from recognized field leaders who use accepted methodologies and best practices in marking borders and naming countries within their mappings. Qlik Sense provides flexibility to enable users to integrate their own, separate background maps. If the standard maps do not fit, Qlik Sense offers the option to load customer provided background maps, borders, and areas.

Geometries can either be added at load time by the data preparation service or loaded from geographic sources such as KML. Point layers also support latitudes and longitudes in separate fields. For area layers, areas can be defined using geometries from a geographic data source such as KML files. For more information, see [*Loading your own map data*](load-map-data.htm). Line layers support the same point data as point layers. Line layers also support strings with line geometries in GeoJSONLineString or MultiLineString formats.

If you are using a custom map in a background layer that uses non-WGS-84 coordinates, you can use a field with locations defined in the coordinate system the map uses (either degrees or meters). For more information, see [*Map chart*](#nonWGS84).

## Loading geographic data with Qlik GeoOperations analytics sources

Qlik GeoOperations analytic sources allow you to load additional sources of geographic data into your application for use in your maps. With Qlik GeoOperations, you can also perform transformations and geometric, [aggregation](#glossary-6 "Glossary term"), and lookup operations with your data.

For more information, see [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm).

## Limitations

The map chart is not navigable with keyboard navigation. When creating accessible applications, consider using alternative ways of presenting your geographic data.

## Learn more

- [*Creating maps*](create-maps.htm)
- [*Loading your own map data*](load-map-data.htm)
- [*Creating a drill-down dimension*](../../Dimensions/create-drill-down-dimension.htm)
- [Interpreting Map Charts](/lnk/Interpreting_map_charts)

Related learning:

- [Interpreting Map Charts](/lnk/Interpreting_map_charts)
