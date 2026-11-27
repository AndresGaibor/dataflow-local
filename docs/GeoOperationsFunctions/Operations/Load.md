---
title: "Load"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Load

Load loads the dataset with no operations applied. This allows you to load all the different formats Qlik GeoOperations supports.

Tip note

Simplify can be a good alternative to Load if the geometries are detailed and slow to display.

You can load:

- A file
- A separated text file
- Standard areas and points from the location service
- A previously loaded table

## Loading from a file

You can use Load to load data from the following file types:

- DXF
- ESRIJSON
- GeoJSON
- GML2
- Shapefile (zipped)

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Load.
3. Under Type, select File based geo dataset.
4. Under URL, enter the location of the file.

   Only URLs with HTTPS or LIB protocols are allowed.

   You can use files from the data sources in the application's space using the following syntax: lib://DataFiles/<file name>. For example, lib://DataFiles/SalesGeographies.geojson.

   You can also specify a space storing the files using the following syntax: lib://<space name>:DataFiles/<file name>. For example, lib://EuropeSales:DataFiles/SalesGeographies.geojson.

   You can also specify a file from a Web Storage Provider Connector using the following syntax: lib://<Web Storage Provider>/<file name>. For example, lib://Dropbox/SalesGeographies.geojson.
5. Under Key field, select the field that contains identities for each geometry.

   If you select Autogenerate, a key field will be generated.

   If you select Specify, enter the field name.
6. Under File type, select the type of the file you are loading.
7. Under Character encoding, select the character encoding used in the file.

   If you select Auto, the connection attempts to automatically detect the encoding.

   If you select Specify, enter the encoding.
8. Under Expected geometry type, select the type of geometry contained in the geometry field. The following types are available:

   - Auto: Tries to detect type automatically.
   - Point : Looks for points in the specified file.
   - Line : :Looks for lines in the specified file.
   - Polygon : Looks for polygons in the specified file.
9. Under Tables, select the tables to load.
10. Under Fields select the fields from the tables to load.
11. Click Insert script.

## Loading data from a separated text file

Text files with table data, optionally with geometries. Instead of geometries, names of locations can be specified. All fields will be loaded as strings.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Load.
3. Under Type, select Separated text file.
4. Under URL, enter the location of the file.

   Only URLs with HTTPS or LIB protocols are allowed.

   You can use files from the data sources in the application's space using the following syntax: lib://DataFiles/<file name>. For example, lib://DataFiles/SalesGeographies.geojson.

   You can also specify a space storing the files using the following syntax: lib://<space name>:DataFiles/<file name>. For example, lib://EuropeSales:DataFiles/SalesGeographies.geojson.

   You can also specify a file from a Web Storage Provider Connector using the following syntax: lib://<Web Storage Provider>/<file name>. For example, lib://Dropbox/SalesGeographies.geojson.
5. Under Key field, select the field that contains identities for each geometry.

   If you select Autogenerate, a key field will be generated.

   If you select Specify, enter the field name.
6. Under Geometry field, enter the name of the geometry field.

   If point data is in two fields, then specify in the following format: latitude field,longitude field.
7. Under Geometry type, select the type of geometry contained in the geometry field. The following types are available:

   - Point : Point geometry in Qlik Sense point format: [longitude,latitude]
   - Point Latitude and longitude: Point geometry with latitude and longitude in separate fields.
   - Line : :Line geometry in Qlik Sense line format: [[longitude,latitude],[longitude,latitude],...]
   - Polygon : Polygon geometry.
   - LocationNamedPoint : Names of a geographic point such as a cities.
   - LocationNamedArea : Names of a geographic areas such as a countries.
   - WKT : Geometry in WKT format. Qlik GeoOperations supports Point, LineString, MultiLineString, Polygon, and MultiPolygon. For more information, see
      [Well-known text representation of geometry](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry).
8. Optionally, under Location suffix, add a suffix to append to all values.

   This is useful to specify more information to server-based location services such as country code or type. For example, with the following suffix all items are specified to be cities in Sweden: ,SE:city. For more information on what syntax to use, see [Location service](https://help.qlik.com/en-US/geoanalytics/Content/Qlik_GeoAnalytics/GeoAnalytics-Sense/Location-Service-Sense.htm).
9. Under Character encoding, select the character encoding used in the file.

   If you select Auto, the connection attempts to automatically detect the encoding.

   If you select Specify, enter the encoding.
10. Under Header, select First row in file if the header is the first row.

    Otherwise, select Specify and enter the names of the columns, separated by commas.
11. Under Field separator, enter the character that separates fields.

    In addition to characters, the keywords TAB, NEWLINE, COMMA, and SEMICOLON are supported.
12. Under Record separator, enter the character that separates lines.

    In addition to characters, the keywords TAB, NEWLINE, COMMA, and SEMICOLON are supported.
13. Optionally, under Quote character, enter the character used for quoting strings.

    Field and record separators inside the quotes will not be parsed as such. The quotes will be removed in the loaded data. The key words QUOTE ("), DOUBLEQUOTE ("), and SINGLEQUOTE (') are supported.
14. Under Coordinate reference system, select the CRS of the data to load.

    The data is projected from the selected CRS to WGS84 (EPSG:4326) before being loaded into the application.

    If you select Auto, the connection attempts to automatically detect the CRS from the file. If no CRS is found in the file, then EPSG:4326 (WGS84) is used.

    Information note

    Setting a CRS value overrides the information in the file and should only be done for files lacking such information or where it is known that the information is wrong. Files with data with several CRSs are not supported.
15. Under Tables, select the tables to load.
16. Under Fields select the fields from the tables to load.
17. Click Insert script.

## Loading standard areas and points

You can load default points and areas from the Qlik GeoAnalytics Server locations service. These can be associated to fields containing corresponding names in other tables to provide points and areas.

The following location types are available:

Location support

| Location | Description | Point | Area |
| --- | --- | --- | --- |
| Adm 1 area | First order administrative division. | Yes | Yes |
| Adm 2 area | Second order administrative division. | Yes | Yes |
| Adm 3 area | Third order administrative division. | Yes | Yes |
| Adm 4 area | Fourth order administrative division. | Yes | Yes |
| Airport code IATA | IATA airport codes. | Yes | No |
| Airport code ICAO | ICAO airport codes. | Yes | No |
| Capital | National capitals. | Yes | No |
| City | Major cities and places. | Yes | No |
| Continent | Continents. | Yes | No |
| Country | Country names. | Yes | Yes |
| Country Code ISO 2 | ISO 2 codes for countries. | Yes | Yes |
| Country Code ISO 3 | ISO 3 codes for countries. | Yes | Yes |
| Postal Code | Postal or ZIP codes. | Yes | Yes |

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Load.
3. Under Type, select Separated text file.
4. Under Geometry type, select Area or Point.
5. Under Location type, select the location to load.
6. Under Country codes, optionally enter country codes (2 or 3 letters) for the countries to load locations from.

   You can separate country codes by with commas. Entering no values means all locations of the type selected will be loaded.

   Information note

   Only 50,000 entries can be loaded. If more are loaded, the load will fail.
7. Under Tables, select the tables to load.
8. Under Fields select the fields from the tables to load.
9. Click Insert script.

## Loading a previously loaded table

You can pass a previously loaded table to Qlik GeoOperations to declare how its geographic data should be interpreted.

In many cases, the key field and geometry field can be automatically detected based on contents. It is recommended to declare tables so that the interpretation does not change after a reload with new data.

Normally the [Qlik Sense geometry format](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/GeospatialFunctions/geospatial-functions.htm) is used but well-known text representation of geometry (WKT) format is also supported.
This makes it possible to read geographic data from a database and then convert the geometries using the *Load* operation.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Load.
3. Under Type, select Loaded Table.
4. Under Table name, enter the table.
5. Under Key field, select the field that contains identities for each geometry.

   If you select Autogenerate, a key field will be generated.

   If you select Specify, enter the field name.
6. Under Geometry type and field, select the geometry type, and then enter the field containing that data.

   For data that goes not contain geometry, select None.
7. Under Coordinate reference system, select the CRS of the data to load.

   The data is projected from the selected CRS to WGS84 (EPSG:4326) before being loaded into the application.

   If you select Auto, the connection attempts to automatically detect the CRS from the file. If no CRS is found in the file, then EPSG:4326 (WGS84) is used.

   Information note

   Setting a CRS value overrides the information in the file and should only be done for files lacking such information or where it is known that the information is wrong. Files with data with several CRSs are not supported.
8. Under Tables, select the tables to load.
9. Under Fields select the fields from the tables to load.
10. Click Insert script.

### Loading data from previously loaded inline tables

Only one inline table can be specified per operation. If you need to use data in two or more inline tables, you can use STORE to save the other inline tables as CSV files and then load from the CSV files.

For example, you have two inline tables in your load script:

pts:
LOAD \* inline "
p1id;p1point
1;[12.3,57.8]
2;[12.2,57.9]
3;[12.0,57.6]
4;[12.8,57.5]
" (delimiter is ';');
pts2:
LOAD \* inline "
p2id;p2point
1;[12.3,57.8]
2;[12.3,57.8]
3;[12.3,57.8]
4;[12.3,57.8]
" (delimiter is ';');

You want to use data from both tables in a Closest operation. To do so, you store the data from the second table as a CSV file with STORE. For example:

store pts2 into
[lib://DataFiles/temppoints.csv]
(txt, delimiter is ';');

Now when loading in your Closest operation, you can load the data from the pts2 table from the temppoints CSV file.
