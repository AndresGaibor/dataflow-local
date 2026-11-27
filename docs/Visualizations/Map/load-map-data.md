---
title: "Loading your own map data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/load-map-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Loading your own map data

To be able to create a map [visualization](#glossary-0 "Glossary term"), you need access to geographical data that connects to the data in your application

Qlik Sense can use:

- Name data in fields to place locations in map layers.
- Fields containing geopoints (latitude and longitude) in WGS-84.
- Fields containing geopoints, polygons, or lines from a geographic data source such as a KML file.
- Fields containing geodata in GeoJSON, LineString, or MultiLineString formats.
- Fields containing non-WGS-84 coordinates (when using a custom map as the base map).

When loading map data in Data manager with data profiling enabled, the data profiling service will identify country names, city names, and latitude and longitude fields and load the corresponding geometries into new fields. In Data load editor, you can optionally combine coordinate fields into a single field for convenience. For more information about using your map data to create a map, see [*Map chart*](Map.htm).

## Supported name data for fields in a map visualization

The map visualization can use name data in fields to place locations in map layers. The following location types can be used:

- Continent names
- Country names
- ISO alpha 2 country codes
- ISO alpha 3 country codes
- First-level administrative area names. such as a state or province names
- Second-level administrative area names
- Third order administrative area names
- Fourth order administrative area names
- City, village, or other populated place names
- Postal codes or ZIP Codes
- IATA airport codes
- ICAO airport codes

Information note

Availability of locations may vary by country. If the named location is not available, use coordinate or area data for the location.

Qlik Sense uses map and location data obtained from recognized field leaders who use accepted methodologies and best practices in marking borders and naming countries within their mappings. Qlik Sense provides flexibility to enable users to integrate their own, separate background maps. If the standard maps do not fit, Qlik Sense offers the option to load customer provided background maps, borders, and areas.

## Loading point and area data from a KML file

You can add data from a KML file into your map in [Data manager](#glossary-2 "Glossary term") and [Data load editor](#glossary-3 "Glossary term"). By default, all [fields](#glossary-4 "Glossary term") are selected in the data selection dialog, even if they do not contain any data. A KML file could contain, for example, area data but no point data. When adding data from a KML file that contains an empty point or area field to Qlik Sense, you can exclude the empty field without running the risk of creating map [dimensions](#glossary-5 "Glossary term") without any data.

When adding a field from a KML field to a map layer, if the name field contains meaningful name data, it should be added as the dimension of the layer. The area or point field should then be added as the Location field. There will be no difference in how the data is visualized in the layer and the text in the name field will be shown as a tooltip.

Information noteIf the KML file does not contain point data, line data, or area data, you cannot load data from that file. If the KML file is corrupt, an error message is displayed, and you will not be able to load the data.

## Loading map data with data profiling

When you load geographical data using Add data in Data manager with data profiling enabled, Qlik Sense will try to recognize if your data contains:

- Country and city names from your data
- Geopoint data (latitude, longitude) for a single location, such as a city
- Area data (polygons of geopoints) to represent regions or countries

If successful, a new field containing geographical information is created automatically.

Warning noteWhen using Add data, data profiling must be enabled. This is the default selection. If you disable data profiling, the geographical data is not detected and the new field containing geographical information is not created.

If cities are recognized during data preparation, the new field contains geopoints, and if countries are recognized the new field contains area polygon data. This field is named <data field>\_GeoInfo. For example, if your data contains a field named Office containing city names, a field with geopoints named Office\_GeoInfo is created.

Information note

Qlik Sense analyzes a subset of your data to recognize fields containing cities or countries. If the matching is less than 75 percent, a field with geographical information will not be created. If a field is not recognized as geographical data, you can manually change the field type to geographical data.

For more information, see [*Changing field types*](../../LoadData/changing-date-time-format.htm).

Fields with geographical information do not display the geopoint or polygon data in the Associations preview panel or in the Tables view. Instead, the data is indicated generically as [GEO DATA]. This improves the speed with which the Associations and Tables views are displayed. The data is available, however, when you create [visualizations](#glossary-6 "Glossary term") in the Sheet view.

## Loading and formatting point data

You can create a map by using point data (coordinates). Two formats are supported:

- The point data is stored in two fields, one for latitude and one for longitude. You can add the fields to a point layer in the Latitude and Longitude fields in the point layer. Optionally, you can combine them into a single field. To combine them into a single field:

  - If you used Add data with data profiled enabled to load the table, the latitude and longitude fields are recognized, and a geopoint field is created automatically.
  - If you loaded the data using the data [load script](#glossary-7 "Glossary term") you can create a single field with point data in [x, y] format, using the function GeoMakePoint().

    For more information, see [*Example: Loading point data from separate latitude and longitude columns with the data load script*](#Loading2).
- The point data is stored in one field. Each point is specified as an array of x and y coordinates: [x, y]. With geospatial coordinates, this would correspond to [longitude, latitude].

  When using this format and loading the data in Data load editor, it is recommended that you to tag the point data field with $geopoint;.

  For more information: [*Example: Loading point data from a single column with the data load script*](#Loading).

In the following examples we assume that the files contain the same data about the location of a company's offices, but in two different formats.

#### Example: Loading point data from separate latitude and longitude columns with the data load script

The Excel file has the following content for each office:

- Office
- Latitude
- Longitude
- Number of employees

The load script could look as follows:

LOAD

Office,

Latitude,

Longitude,

Employees

FROM 'lib://Maps/Offices.xls'

(biff, embedded labels, table is (Sheet1$));

Combine the data in the fields Latitude and Longitude to define a new field for the points.

Run the script and create a map visualization. Add the point dimension to your map.

You can choose to create the dimension Location in the script by adding the following string above the LOAD command:

LOAD \*, GeoMakePoint(Latitude, Longitude) as Location;

The function GeoMakePoint() joins the longitude and latitude data together.

It is recommended that you tag the field Office with $geoname so that it is recognized as the name of a geopoint. Add the following lines after the last string in the LOAD command:

TAG FIELDS Office WITH $geoname;

The complete script then is as follows:

LOAD \*, GeoMakePoint(Latitude, Longitude) as Location;

LOAD

Office,

Latitude,

Longitude,

Employees

FROM 'lib://Maps/Offices.xls'

(biff, embedded labels, table is (Sheet1$));

TAG FIELDS Office WITH $geoname;

Run the script and create a map visualization. Add the point dimension to your map.

#### Example: Loading point data from a single column with the data load script

The Excel file has the following content for each office:

- Office
- Location
- Number of employees

The load script could look as follows:

LOAD

Office,

Location,

Employees

FROM 'lib://Maps/Offices.xls'

(biff, embedded labels, table is (Sheet1$));

The field Location contains the point data and it is recommended to tag the field with $geopoint so that it is recognized as a point data field. It is recommended that you tag the field Office with $geoname so that it is recognized as the name of a geopoint. Add the following lines after the last string in the LOAD command:

TAG FIELDS Location WITH $geopoint;

TAG FIELDS Office WITH $geoname;

The complete script then looks as follows:

LOAD

Office,

Location,

Employees

FROM 'lib://Maps/Offices.xls'

(biff, embedded labels, table is (Sheet1$));

TAG FIELDS Location WITH $geopoint;

TAG FIELDS Office WITH $geoname;

Run the script and create a map visualization. Add the point dimension to your map.

## Learn more

- [*Map chart*](Map.htm)
