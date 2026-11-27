---
title: "Qlik GeoOperations Shapefile analytics connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/GeoOperationsShapefile.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources"]
---

# Qlik GeoOperations Shapefile analytics connection

Qlik GeoOperations Shapefile analytic connections are added in Data load editor, Script, or from the Analytics [activity center](#glossary-0 "Glossary term").

Once you create a connection, you can load shape files (ZIP files containing SHP and DBF for ESRI format) through the connection. The script is then added to your load script.

## Creating a new connection

Do the following:

1. In Data load editor or Script, click Data sources.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Qlik GeoOperations Shapefile from the list of data connectors.
5. Optionally, add a new name for the connection.
6. Click Create.

Information note

You cannot create and manage connections to this connector in Data manager within an analytics application.

## Select and loading data through a Qlik GeoOperations Shapefile connection

When loading from shape files, only a single geometric type can be loaded at a time. If there are multiple types in the file, you must select which geometry to load.

Do the following:

1. Under Data connections, click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations Shapefile connection.
2. Under URL, enter the location of the GeoJSON file.

   Only URLs with HTTPS or LIB protocols are allowed.

   You can use files from the data sources in the application's space using the following syntax: lib://DataFiles/<file name>. For example, lib://DataFiles/SalesGeographies.geojson.

   You can also specify a space storing the files using the following syntax: lib://<space name>:DataFiles/<file name>. For example, lib://EuropeSales:DataFiles/SalesGeographies.geojson.

   You can also specify a file from a Web Storage Provider Connector using the following syntax: lib://<Web Storage Provider>/<file name>. For example, lib://Dropbox/SalesGeographies.geojson.
3. Under Key field, select the field that contains identities for each geometry.

   If you select Autogenerate, a key field will be generated.

   If you select Specify, enter the field name.
4. Under Character encoding, select the character encoding used in the GeoJSON file.

   If you select Auto, the connection attempts to automatically detect the encoding.

   If you select Specify, enter the encoding.
5. Optionally, under Expected geometry type, select the type of geometry to load.

   If you select Auto, the connection attempts to automatically detect the geometry type. If you file contains multiple geometry types ,you must select the geometry type you want to load.
6. Under Coordinate reference system, select the CRS of the data to load.

   The data is projected from the selected CRS to WGS84 (EPSG:4326) before being loaded into the application.

   If you select Auto, the connection attempts to automatically detect the CRS from the file. If no CRS is found in the file, then EPSG:4326 (WGS84) is used.

   Information note

   Setting a CRS value overrides the information in the file and should only be done for files lacking such information or where it is known that the information is wrong. Files with data with several CRSs are not supported.
7. Under Tables, select the tables to load.
8. Under Fields select the fields from the tables to load.
9. Click Insert script.
