---
title: "Dataset"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Sense_GeoOperations/Content/Sense_GeoOperations/connector-geoanalytics_reference-Dataset.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Scripting with Qlik GeoOperations", "GeoOperations Reference"]
---

# Dataset

The following are data sources that can be used with operations in the Qlik GeoOperations server-side extension.

## CSV

Text files with table data, optionally with geometries. Instead of geometries, names of locations can be specified. All fields will be loaded as strings.

Parameters for CSV

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| url | string | *default: None.* | The URL of the file containing the data. Only URLs with HTTPS or LIB protocols are allowed.  You can use files from the data sources in the app's space using the following syntax: lib://DataFiles/<file name>. For example, lib://DataFiles/Offices.csv. You can also specify a space storing the files using the following syntax: lib://<space name>:DataFiles/<file name>. For example, lib://EuropeSales:DataFiles/Offices.csv. You can also specify a file from a Web Storage Provider Connector using the following syntax: lib://<Web Storage Provider>/<file name>. For example, lib://Dropbox/Offices.csv. |
| keyField | string | *default: None.* | The name of the field that contains identities for each geometry. If you leave the field empty a key field will be generated. |
| geometryField | string | *default: None.* | Name of the geometry field, if any. As an alternative to a geometry, a column with names of well-known points or areas may be specified as "Geometry Type" below. If point data is in two fields, then specify in the following format: name of latitude field comma name of longitude field. |
| geometryType | string | *default:POINT* | Type of geometry in the Geometry Field. Allowed values are:  - Point - a point geometry in Qlik Sense point format: "[longitude,latitude]" - PointLatLon - one field with latitudes and one with longitudes - Line - a line geometry in Qlik Sense line format: "[[longitude,latitude],[longitude,latitude],...]" - Polygon - a polygon geometry, that is, an array of closed lines or array of array of closed lines in case of multi-polygons - LocationNamedPoint - a name of a geographic point such as a city - LocationNamedArea - a name of a geographic area such as a country - WKT - a geometry on WKT format, supports POINT, LINESTRING, MULTILINESTRING, POLYGON and MULTIPOLYGON, see    [Well-known text representation of geometry](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)  In cases of named points or areas, the geometry is looked up in the location service and a column for the geometry is added. Columns for country, type, and administrative areas are added as in the Standard areas and Points dataset. |
| suffix | string | *default: None.* | For advanced users. The specified string is appended to all IDs. This is a convenient way to specify more information to server-based location services such as country code or type. The alternative is to append the extra data when loading the table into Qlik. With the following suffix all items are specified to be cities in Sweden: ,SE:city See the  [Geometry Service Specification](https://help.qlik.com/en-US/geoanalytics/Content/Qlik_GeoAnalytics/GeoAnalytics-Sense/Location-Service-Sense.htm) for more information on what syntax to use. |
| header | string | *default: None.* | The names of the columns separated by a comma. If blank, the first row contains the header. |
| fieldSeparator | string | *default:TAB* | The character that separates fields. In addition to ordinary characters, the key words TAB, NEWLINE, COMMA, and SEMICOLON are allowed. |
| recordSeparator | string | *default:NEWLINE* | The character that separates lines. In addition to ordinary characters, the key words TAB, NEWLINE, COMMA, and SEMICOLON are allowed. |
| encoding | string | *default:UTF-8* | The character set for the file. The same values are allowed as in Java. |
| stringQuotes | string | *default: None.* | The character that can be used for quoting strings. Field and record separators inside the quotes will not be parsed as such. The quotes will be removed in the imported data. In addition to ordinary characters the key words QUOTE("), DOUBLEQUOTE("), and SINGLEQUOTE(') are allowed. |
| crs | string | *default:Auto* | CRS (Coordinate Reference System) of the data to load. The data will be projected from this CRS to WGS84 (EPSG:4326) before being loaded into the app.  If set to  *Auto* then  *EPSG:4326* (WGS84) is used. |

## GEOFILE

Loads different kinds of geographical file formats like GeoJSON and ESRI Shapefile.This example loads a GeoJSON file via the Simplify operation:

Load \* Extension
GeoOperations.ScriptEval('
SELECT nuts.NUTS\_ID as NUTS\_ID, Simplified\_nuts\_Geometry FROM Simplify()
DATASOURCE nuts GEOFILE url="https://datahub.io/core/geo-nuts-administrative-boundaries/r/nuts\_rg\_60m\_2013\_lvl\_1.geojson"');

Parameters for GEOFILE

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| url | string | *default: None.* | The URL of the file containing the data. Only URLs with HTTPS or LIB protocols are allowed.  You can use files from the data sources in the app's space using the following syntax: lib://DataFiles/<file name>. For example, lib://DataFiles/SalesGeographies.geojson. You can also specify a space storing the files using the following syntax: lib://<space name>:DataFiles/<file name>. For example, lib://EuropeSales:DataFiles/SalesGeographies.geojson. You can also specify a file from a Web Storage Provider Connector using the following syntax: lib://<Web Storage Provider>/<file name>. For example, lib://Dropbox/SalesGeographies.geojson. |
| keyField | string | *default: None.* | The name of the field that contains identities for each geometry. If you leave the field empty a key field will be generated. |
| type | string | *default:Auto* | The type of file. Allowed values are:  - **Auto** - Tries to detect the file type from the name of the file. - **GeoJSON** - The GeoJSON format as specified by  [geojson.org](https://geojson.org). - **GML** - For reading GML files or connecting to WFS services. Reads  *featureCollection* files and makes one row of each  *featureMember* element. GeoOperations only supports GML2. - **Shape** - A zip file with at least a shp and a dbf file for the ESRI shape file format. It is important that the zip file is created with the same character encoding as the files it contains. - **ESRIJson** - JSON as returned by ESRI ArcGIS Server (see  [ESRI doc   of format](https://resources.arcgis.com/en/help/rest/apiref/feature.html)).   This makes it possible to connect to ArcGIS and import data from services it has published. - **DXF** - For reading geometries from an AutoCAD DXF file. A limited set of entity types for points and lines are supported:    `POINT, TEXT, MTEXT, ARC, CIRCLE, LINE, POLYLINE, LWPOLYLINE, SPLINE, and MLINE` |
| encoding | string | *default: None.* | For some formats (like ESRI Shapefile) the character encoding is not defined in the format. This gives a way to provide this information. For most formats this property is ignored. |
| expectedGeomType | string | *default:Auto* | Only a single geometric type is loaded at a time. If there are multiple types in the data, use this property to set which type is loaded. For formats that don't support multiple types, this parameter is ignored.  - **Auto** - Tries to detect type automatically. - **Point** - Looks for Points in the specified file. - **Line** - Looks for Lines in the specified file. - **Polygon** - Looks for Polygons in the specified file. |
| crs | string | *default:Auto* | Coordinate reference System (CRS) of the data to load. The data will be projected from this CRS to WGS84 (EPSG:4326) before being loaded into the app.  If set to  *Auto* or if empty it will try to parse it from the file. If no CRS is found in the file, then  *EPSG:4326* (WGS84) is used. Note that setting this to a CRS overrides the information in the file and should only be done for files lacking such information or where it is known that the information is wrong. Files with data with several CRSs are not supported. |

## INTABLE

A table that is passed as input to the Extension function can be declared to specify how it should be interpreted.
If it is not declared, the key field and geometry field can, in many cases, be automatically detected based on contents.
It is, however, recommended to declare tables so that the interpretation does not change after a reload with new data.If the table contains names instead of geometries or latitude and longitude columns, it must be declared.If the table is not declared it will count as the first table for default datasets in operations. If it is declared, it will be counted in the order it is declared.Normally the  [Qlik Sense geometry format](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/geospatial-functions.htm) is used but WKT format ( [Well-known text reprentation of geometry](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry))
is also supported.
This makes it possible to read geographic data from a database using one of the usual database connectors and then convert the geometries to Sense geometries using the  *Load* operation.
Note that when geometries are read from the database, a function that returns the column in WKT format should be applied. The standard SQL function is called  *ST\_AsText()* but some databases have their own function.Only one of the parameters that specify the location field may be used at a time, except  *latitudeField* and  *longitudeField* which always should be defined in pairs.Only one inline table can be specified per operation. If you need to use data in two or more inline tables, you can use  *STORE* to save the other inline tables as CSV files and then load from the CSV files.Example with latitude and longitude fields:

MyCities:
LOAD \*
inline "
cid;lat;long
1;57.7;12
2;45.42;-75.70
" (delimiter is ';');
Load \* Extension
GeoOperations.ScriptEval('
TravelAreas(costValue="10",costUnit="minutes")
DATASOURCE cities INTABLE keyField="cid", latitudeField="lat", longitudeField="long"', MyCities);

Example where the data contains named locations and because of that needs to declare the  *namedAreaField* parameter:

MyCountries:
LOAD \*
inline "
cid;Country
1;US
2;CA
" (delimiter is ';');
Load \* Extension
GeoOperations.ScriptEval('
Simplify()
DATASOURCE countries INTABLE keyField="Country", namedAreaField="Country"', MyCountries{Country});

Parameters for INTABLE

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| keyField | string | *optional* | The name of a field that contains unique identities for each row. If not specified, a key column named  *\_autoIndex\_* will be added with unique values for each row. |
| pointField | string | *optional* | Field containing point data in Qlik Sense point format, "[longitude, latitude]". WKT point data ("POINT(...)") is also supported. |
| lineField | string | *optional* | Field containing line data in Qlik Sense line format: "[[longitude,latitude],[longitude,latitude],...]". WKT line data ("LINESTRING(...)" or "MULTILINESTRING(...)") is also supported. |
| polygonField | string | *optional* | Field containing line data in Sense polygon format, i.e., an array of closed lines or array of array of closed lines in the case of multi-polygons. WKT polygon data ("POLYGON(...)" or "MULTIPOLYGON(...)") is also supported. |
| latitudeField | string | *optional* | Field containing latitude values. |
| longitudeField | string | *optional* | Field containing longitude values. |
| namedPointField | string | *optional* | Field containing names of geographic features that are looked up in the location database. The names will be represented with points. |
| namedAreaField | string | *optional* | Field containing names of geographic features that are looked up in the location database. The names will be represented with polygons. Not all names in the location database have associated polygons. |
| crs | string | *default:Auto* | CRS (Coordinate Reference System) of the data to load. The data will be projected from this CRS to WGS84 (EPSG:4326) before being loaded into the app.  If set to  *Auto* then  *EPSG:4326* (WGS84) is used. |

## LOCATIONSERVICE

Points and areas that are available in a Qlik GeoAnalytics Server location service. Type or country must be specified.

The fields in tables loaded from the location service are:

- LocationDbId - Unique id for each entity.
- LocationPoint/LocationArea - The geometry of the entity.
- CountryIso2 - The two-letter country code.
- Adm1Code - Nation-specific code of first order administrative area.
- Adm2Code - Nation-specific code of second order administrative area.
- LocationDbType - See the  [Geometry Service Specification](https://help.qlik.com/en-US/geoanalytics/Content/Qlik_GeoAnalytics/GeoAnalytics-Sense/Location-Service-Sense.htm) for more info on the types.

This example loads the states in the US:

MyAirports:
Load \*
Extension GeoOperations.ScriptEval('
Load()
DATASOURCE states LOCATIONSERVICE geometry="AREA", type="STATE", country="us"
');

Parameters for LOCATIONSERVICE

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| geometry | string | *default:Area* | Choose to access Points or Areas. |
| type | string | *default:Country* | Type of data that the names represents such as countries, administrative areas, postal codes etc. The following simplified type names can be used (case insensitive) in the native types in the location database:  - CONTINENT - Continent name. - COUNTRY - Country name. - COUNTRYISO2 - ISO 3166-1 alpha-2 code. - COUNTRYISO3 - ISO 3166-1 alpha-2 code. - ADMIN1 - First order administrative division. - STATE - Alias for ADMIN1. - ADMIN2 - Second order administrative division. - ADMIN3 - Third order administrative division. - ADMIN4 - Fourth order administrative division. - POSTALCODE - Postal code. - ZIP - Alias for POSTALCODE. - CITY - City name. - AIRPORTIATA - Airport IATA code. - AIRPORTICAO - Airport ICAO code.  See the  [Geometry Service Specification](https://help.qlik.com/en-US/geoanalytics/Content/Qlik_GeoAnalytics/GeoAnalytics-Sense/Location-Service-Sense.htm) for more information on the detailed types. |
| country | string | *default: None.* | Country code (2 or 3 letters) for the country to access. Several countries may be specified, separated by commas. The default value means not restricted to a country. |
