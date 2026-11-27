---
title: "Qlik GeoOperations analytics sources"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/GeoOperations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Qlik GeoOperations analytics sources

Qlik GeoOperations connections allow you to easily use geographic calculations and functions. Qlik GeoOperations also allows you to load geographic data from a variety of data sources. With Qlik GeoOperations, you can solve problems such as:

- Determining how many customers are living within a 15 minute drive from a store location.
- Linking GPS positions to venues, regions, or road networks.
- Building custom sales areas from a list of municipalities.
- Finding the closest hospital for a list of patients.

Qlik GeoOperations helps to quickly create scripts to load or transform your geographic data. Qlik GeoOperations is available as three analytic connections:

- Qlik GeoOperations: Load and transform your geographic data through different operations.

  [*Qlik GeoOperations connection*](GeoOperations-QlikGeoOperations.htm)
- Qlik GeoOperations GeoJSON: Load GeoJSON files into your application.

  [*Qlik GeoOperations GeoJSON connection*](GeoOperationsGeoJSON.htm)
- Qlik GeoOperations Shapefile: Load shape files into your application.

  [*Qlik GeoOperations Shapefile analytics connection*](GeoOperationsShapefile.htm)

You can also add GeoOperations functions to the script yourself in Data load editor or Script.
Some GeoOperations are also available in chart expressions. For more information, see [*Scripting with Qlik GeoOperations*](GeoOperations-scripting.htm).

Tip note

For an example of how to use GeoOperations see, [GeoOperations example](https://community.qlik.com/t5/Qlik-Sense-Documents/GeoOperations-Examples-Qlik-GeoAnalytics/ta-p/1753980).

Additionally, you can add address data lookup functionality with the Qlik Geocoding subscription service. For more information, see [*Qlik Geocoding*](../GeoCoding/Qlik-GeoCoding.htm).

## Requirements

You must have one of the following user role permissions to use GeoOperations:

- Use GeoOperations: Allowed
- Use GeoOperations: No geocoding

## Supported file types

The following table shows which data types are supported with Qlik GeoOperations and the connection recommended to load them.

Supported file types

| File type | Recommended Qlik GeoOperations connection |
| --- | --- |
| CSV | Qlik GeoOperations using the Load operation |
| DXF | Qlik GeoOperations using the Load operation |
| ESRIJSON | Qlik GeoOperations using the Load operation |
| GeoJSON | Qlik GeoOperations GeoJSON |
| GML2 | Qlik GeoOperations using the Load operation |
| Shape (ZIP containing a SHP and DBF file) | Qlik GeoOperations Shapefile |

You can also use previously loaded tables with Qlik GeoOperations.

## Where to use GeoOperations

All Qlik GeoOperations connections are available in Data load editor, Script, and from the Create page in the Analytics [activity center](#glossary-0 "Glossary term"). You can only select and load data with them from Data load editor or Script.

Certain GeoOperations scripting operations can be used in expressions in chart scripts for maps as well to enable dynamic calculations. Each time the selection changes, the operation is run. Data does not go into the data model when GeoOperations are used in charts, preventing further analysis of that data. For more information, see [Operation](/en-US/geoanalytics/Content/Ref-GeoOperationsService/connector-geoanalytics_reference-Operation.htm).

## Limitations

The following limitations apply to the maximum size of datasets with Qlik GeoOperations operations:

- Max number of rows: 100,000
- Max dataset size in memory: 350 MB
- Max rows with routing: 400
- Max rows with name lookups: 20,000

Some operations support streaming data from Qlik Engine. Data streamed from Qlik Engine can be larger, but the size limit for routing still applies.

## Migrating from GeoAnalytics Connector to Qlik GeoOperations

For details on how to migrate from GeoAnalytics Connector to Qlik GeoOperations, see [Migrating from GeoAnalytics Connector to Qlik GeoOperations](/en-US/migration/Content/Migration/migrate-geo-analytics.htm).
