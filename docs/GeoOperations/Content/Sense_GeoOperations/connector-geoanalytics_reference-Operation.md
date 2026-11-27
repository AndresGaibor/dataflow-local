---
title: "Operation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Sense_GeoOperations/Content/Sense_GeoOperations/connector-geoanalytics_reference-Operation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Scripting with Qlik GeoOperations", "GeoOperations Reference"]
---

# Operation

## AddressPointLookup

Returns point geometries for addresses in a table, that is, geocoding.
Specify either an address string in the  *Search Text* property or structured parts in the corresponding properties, such as  *Country*,  *Street* etc.
Combinations are also allowed. This operation requires a special license. Addresses that could not be found for any reason are not returned in the result.

The functionality offered by Qlik Geocoding (via AddressPointLookup and PointToAddressLookup) is distinct from other location lookup features. Qlik Geocoding allows lookups at the address level, whereas regular location lookups can only be as precise as the ZIP code level.

When getting started with Qlik Geocoding, use the template referenced at  [Configuring Qlik Geocoding](https://help.qlik.com/en-US/geoanalytics/Content/Global_Common/GeoCoding/Qlik-GeoCoding-setup.htm).

Information note For best results, favor specific data and omit broad data whenever possible. For instance, if you have both a postal code and postal city, and you trust that the postal code is correct, then it is best to not specify the postal city.

Most parameters come in two versions, one that specifies the actual value, such as  `country="SWE"`, and one that specifies a field name where the actual value should be retrieved from,
such as  `countryField="CountryIso2"`.

Information note
You must have the user role permission Use : to use AddressPointLookup.

Information note
To geocode English or Pinyin addresses in China, the Country parameter must be set to "CHN".

Returns the following columns:

- <dataset key column> - The key column from the input dataset.
- Address - The found address, formatted to address standards of the country.
- Geometry - The point for the found item.
- HouseNumber - The house number for the found item.
- Street - The street for the found item.
- PostalCode - The postal code for the found item.
- City - The name of the city-level administrative division for the found item.
- Adm1 - The name or abbreviated name for the first-order administrative division (state) for the found item.
- CountryIso2 - The country code for the found item.
- Match - A value between 0 and 1 that shows how good the match was. A value of 1 means a perfect match.
- All columns except the key column from  *dataset*, prefixed with the dataset name.

The returned fields might be empty where not applicable or where data is not available.

Supports:

- ScriptEval in load scripts.

Example that geocodes some Swedish addresses where each item is in each own field:

[Addresses]:
Load \* inline [
Id,Country,City,Street,HouseNumber,Postal
1,SE,Gothenburg,Odinsgatan,13,41103
2,SE,,Alfhemsgatan,5,41310
];
Load \* Extension GeoOperations.ScriptEval('
Select Id, Address, AddressPoint From
AddressPointLookup(countryField="Country", cityField="City", streetField="Street", houseNumberField="HouseNumber", postalCodeField="Postal")
', Addresses);

This example shows geocoding in a free text style:

[Addresses2]:
Load \* inline [
Id;Address
1;1600 Pennsylvania Avenue NW, Washington, D.C. 20500
2;767 5th Ave, New York, NY 10153
]
(delimiter is ';');
Load \* Extension GeoOperations.ScriptEval('
AddressPointLookup(searchTextField="Address", country="USA")
', Addresses2);

Parameters for AddressPointLookup

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| searchText | string | *optional* | A string of text to search for. Can be addresses like: "1600 Pennsylvania Ave, Washington DC, USA" or incomplete addresses that are combined with data in other fields, such as "1117 Washington Ave" with  *City* set to "Philadelphia" and  *Country* set to "USA". |
| searchTextField | string | *optional* | If  *searchText* is not specified, this parameter can be used to specify a field where the information should be retrieved from. |
| country | string | *optional* | A string with three-letter ISO codes. Multiple countries may be specified, separated by commas: "SWE,NOR,FIN". To geocode English or Pinyin addresses in China specifically, this parameter must be set to "CHN". |
| countryField | string | *optional* | If  *country* is not specified, this parameter can be used to specify a field that contains the country name or two- or three-letter ISO codes. Note that in contrast to the other parameters, the expected format of the data specified by  *country* and  *countryField* is not identical. The  *country* parameter allows multiple countries, but only in three letter ISO format, while  *countryField* allows different country formats. |
| state | string | *optional* | State name or code. For most countries, the state is not part of the address. |
| stateField | string | *optional* | If  *state* is not specified, this parameter can be used to specify a field where the information should be retrieved from. |
| city | string | *optional* | City name, municipality, or postal city. |
| cityField | string | *optional* | If  *city* is not specified, this parameter can be used to specify a field where the information should be retrieved from. |
| postalCode | string | *optional* | Postal code. |
| postalCodeField | string | *optional* | If  *postalCode* is not specified, this parameter can be used to specify a field where the information should be retrieved from. |
| street | string | *optional* | Street name. Instead of specifying street and house number in separate parameters or fields, both can be specified together, separated by a space. |
| streetField | string | *optional* | If  *street* is not specified, this parameter can be used to specify a field where the information should be retrieved from. |
| houseNumber | string | *optional* | House number. |
| houseNumberField | string | *optional* | If  *houseNumber* is not specified, this parameter can be used to specify a field where the information should be retrieved from. |
| matchThreshold | real | *default:0.5* | Return only result with a better match than this. Increase this value if too many false hits are returned. |
| language | string | *default: None.* | A two-letter language code for the preferred language for the address in the reply. If the address is not available in the requested language it is returned in a default language for the location. |
| dataset | Dataset | *default: None.* | A dataset with addresses that will be looked up in the geocoder. Supports streaming of this dataset when sent from the load script, which means that larger tables are allowed. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Binning

Generates rectangular or hexagonal bins for a point dataset. This is a way to aggregate point data so that an overview of the data can be displayed efficiently.

Returns the following columns:

- <dataset key column> - The key column from the input dataset.
- BinId - Identity for the bin.
- BinTable.BinPolygon - The polygon for the bin.
- BinTable.CenterPoint - Point in center of the bin.
- All columns except the key column from  *dataset*, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.

Example that loads hexagonal bins from US airports:

Load \* Extension GeoOperations.ScriptEval('
Binning(type="hexagonal", gridSize="1")
DATASOURCE airports LOCATIONSERVICE geometry="POINT", type="AirportIATA", country="us"
');

Parameters for Binning

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| type | string | *default:rectangular* | Defines whether  *rectangular* or  *hexagonal* bins should be generated. |
| gridSize | real | *default: None.* | The height of an individual bin in degrees. One degree is approximately 10000m. |
| gridWidthHeightRatio | real | *default:1.5* | The width height ratio of bins. Square bins are often optimal, but that varies by latitude. The formula for the optimal width height ratio is 1/cos(latitude), for example 1 at the equator, 1.15 at latitude +-30 deg and 2 at latitude +-60 deg. It often looks better to display binned data in the adaptive projection than in the Mercator projection. |
| dataset | Dataset | *default: None.* | The dataset with point geometries to generate bins for. Supports streaming of this dataset when sent from the load script, which means that larger tables are allowed. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Closest

Returns relations and distances between objects in one dataset and the closest objects in another, if any is closer than the maximum distance.
The cost may also be calculated along roads, and in that case optionally use travel time.
This operation is useful in many cases, not only for getting the relations to the closest objects, but also for getting distance matrices between a set of points.

Returns the following columns:

- <dataset1 name>\_<dataset2 name>\_RelationId - A key generated for the relation between the two geometries.
- <dataset1 key column> - The key column from the input dataset1.
- <dataset2 key column> - The key column from the input dataset2.
- Distance - The distance in the unit specified in  *costUnit*.
- Status - The returned status is either "ok" or "failed:" followed by an error message.
- LowResLine - A low resolution version of the route line, only available for non  *bird* distance types.
- All columns except the key column from the input  *dataset1* dataset, prefixed with the dataset name.
- All columns except the key column from the input  *dataset2* dataset, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.

This example finds the closest airports to points in a table:

MyPoints:
LOAD \* inline "
id;point
1;[12,57.7]
2;[12.1,57.7]
" (delimiter is ';');
MyClosestAirports:
Load \* Extension GeoOperations.ScriptEval('
Closest(distance="100000", closestCount="3")
DATASOURCE pts INTABLE keyField="id", pointField="point"
DATASOURCE airports LOCATIONSERVICE geometry="POINT", type="AirportIATA", country="se"
', MyPoints);

Parameters for Closest

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| distance | real | *default: None.* | Maximum distance from the unit specified in Cost unit. Items further apart than this are ignored. |
| costUnit | string | *default:meters* | Should be one of meters, yards, kilometers, miles, seconds, minutes, or hours. Using time units imply that the travel time is used as the cost and length units that the distance is used. The time units are not allowed for Distance type Bird. |
| distanceType | real | *default:Bird* | Decides how distances are measured. The following values are allowed:  - Bird - measure direct distances (as the crow flies) between objects. - Car - measure along roads with car restrictions. Only supported for point datasets. - Bike - measure along roads with bike restrictions. Only supported for point datasets. - Pedestrian - measure along roads with pedestrian restrictions. Only supported for point datasets. - Truck - measure along roads with truck restrictions. Only supported for point datasets. |
| closestCount | real | *default:1* | Number of objects in the second dataset to associate with an object in the first dataset. A value of 1 means only the closest, 2 means the two closest, and so on. |
| dataset1 | Dataset | *default:<first dataset>* | Objects to check for closeness to objects in dataset2 if specified, otherwise to objects in itself. When checking closeness between objects in a single dataset, relations are never added from an object to itself. Supports streaming of this dataset when sent from the load script and  *dataset2* is defined, which means that larger tables are allowed. |
| dataset2 | Dataset | *default:<second dataset if any>* | Objects to relate to objects in dataset1. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Cluster

Produces clusters from a point dataset based on geographic closeness between points. The cluster generation is controlled by the  *distance*
parameter, which defines how far away a point may be from the cluster it belongs to.
Returns a table with relations between points and clusters.
Also returns a joined in table named Clusters with cluster geometries.
It contains the fields ClusterID, ClusterCenter (point geometry) and PointCount.
The count field contains the number of points in the cluster.

Returns the following columns:

- <dataset key column> - The key column from the input dataset.
- ClusterID - Id of the cluster the point belongs to.
- Clusters.ClusterPoint - Center point for cluster.
- Clusters.PointCount - Number of original points belonging to the cluster.
- All columns except the key column from the input dataset, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.

This example clusters airports in the US so that airports closer than 50 km belongs to one cluster:

MyClusteredAirports:
Load \*
Extension GeoOperations.ScriptEval('
Cluster(distance="50000")
DATASOURCE airports LOCATIONSERVICE geometry="POINT", type="AirportIATA", country="us"
');

Parameters for Cluster

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| distance | real | *default: None.* | The distance between a point and its cluster can not be longer than this distance in meters. |
| dataset | Dataset | *default: None.* | A dataset with points to cluster. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Dissolve

Dissolves and simplifies areas to form larger areas based on the mapping between old area identities (or geometries) and new area identities.
This is typically used for building custom areas that are build up by smaller well-defined areas, such as postal areas or administrative areas.

Returns the following columns:

- <dissolveField> - The field specified as  *dissolveField* in indata.
- DissolvedPolygon - The geometries of the new dissolved areas.

Supports:

- ScriptEval in load scripts.

The geometry dataset is optional. If not provided, geometries are supposed to be available in the dissolve definition dataset.

Note that overlaps of polygons are removed in all resolutions except  *Source*.

This example creates two regions, one consisting of CA and AZ and one consisting of WA and OR:

MySalesRegions:
LOAD \* inline "
Adm1Code;RegionName
California;SouthWest
Arizona;SouthWest
Washington;NorthWest
Oregon;NorthWest
" (delimiter is ';');
MySalesRegionGeometries:
Load \* Extension GeoOperations.ScriptEval('
Dissolve(dissolveField="RegionName", areaDatasetKeyField="Name")
DATASOURCE states LOCATIONSERVICE type="State", country="us"
', MySalesRegions);

Parameters for Dissolve

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| dissolveField | string | *default:<same name as the key field in dissolveDataset>* | The name of the field with identities of the new areas in  *dissolveDataset*. |
| resolution | string | *default:Auto* | The resulting dataset is simplified and the degree of simplification is controlled by this property. Available values are:  - **auto** - The operation calculates a resolution based on the data. - **autolow** - A resolution that is lower than (half of) the Auto-resolution. - **autohigh** - A resolution that is higher than (double of) the Auto-resolution. - **source** - No simplification is performed.   Note that if  *dissolveDataset* contains the same old areas twice in two different new areas,  *source* must be used. |
| areaDatasetKeyField | string | *default:<key field in areaDataset>* | The identities of the original areas in  *areaDataset*. This is only used if  *areaDataset* is specified. |
| dissolveDataset | Dataset | *default:<first dataset>* | The definition of which new area each old area belongs to, i.e., a mapping between old area and new area identities. The key field should map to the keys in  *areaDataset* if specified. If no  *areaDataset* is provided, the geometries should be available in this dataset. |
| areaDataset | Dataset | *default:<second dataset if any>* | The dataset with area geometries to dissolve. May be none, which means the geometries should be available in  *dissolveDataset*. The  *areaDatasetKeyField* in this dataset must be linked to the key field in  *dissolveDataset*. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Intersects

Returns a table that maps between the key in dataset1 and the key in dataset2 for all objects that intersect.
If both datasets contain polygons, the relative overlap area compared to the areas in respective dataset are returned.

It is possible to limit the number of intersecting geometries in the second dataset that should be mapped to each geometry in the first dataset by specifying  *intersectsCount*.
Then the most intersecting geometries are returned in order. The operation is symmetric if  *intersectsCount* is not specified.

Returns the following columns:

- <dataset1 name>\_<dataset2 name>\_RelationId - A key generated for the relation between the two geometries.
- <dataset1 key column> - The key column from the input dataset1.
- <dataset2 key column> - The key column from the input dataset2.
- <dataset1 name>.RelativeOverlap - The overlap compared to the polygon in dataset1. Only returned if both datasets contain polygons. There is a performance penalty for requesting this field.
- <dataset2 name>.RelativeOverlap - The overlap compared to the polygon in dataset2. Only returned if both datasets contain polygons. There is a performance penalty for requesting this field.
- All columns except the key column from the input  *dataset1* dataset, prefixed with the dataset name.
- All columns except the key column from the input  *dataset2* dataset, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.

This example calculates which states some lines intersects:

MyLines:
LOAD \*
inline "
id;line
1;[[-108.1,45.4],[-107.4,44.9]]
2;[[-98.9,40.1],[-100.4,40.9]]
" (delimiter is ';');
LinesInStates:
Load \*
Extension GeoOperations.ScriptEval('
SELECT id, states.Name FROM Intersects()
DATASOURCE states LOCATIONSERVICE geometry="AREA", type="Admin1", country="us"
', MyLines);

Parameters for Intersects

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| dataset1 | Dataset | *default:<first dataset>* | A dataset with geometries to test for which intersect the geometries in the other dataset if specified, or between objects in this dataset if not. When checking intersection between objects in a single dataset, relations are never added from an object to itself. Supports streaming of this dataset when sent from the load script and when  *dataset2* is defined, which means that larger tables are allowed. |
| dataset2 | Dataset | *default:<second dataset if any>* | A dataset with geometries to test for which intersect the geometries in the other dataset. If not specified, intersection between objects in  *dataset1* is calculated. |
| intersectsCount | integer | *default:0* | If larger than 0, at most this number of intersecting geometries in  *dataset2* is returned per  *dataset1* geometry. Only the ones that intersect the most (largest overlapping area or length) are returned. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## IpLookup

Returns location information and point geometries for IP-addresses in a table.
This is useful when you are analyzing access data to web services.
The returned table contains the following fields:

- Key field - The same as the key field for the name table.
- <Address Table Ip Field> - The same as the IP field that was looked up. Only available if not the same as the key field.
- IpPoint - The point for the found item.
- CountryIso2 - The country code for the found item.
- Adm1Code - The code for the first order administrative area for the found item. Note that this code is not always compatible with the code returned by the location service.
- City - The city for the found item.
- All columns except the key column from the input dataset, prefixed with the dataset name.

IP geolocation is inherently imprecise. For many IP-addresses it is possible to pinpoint a city, but for others only country can be resolved.

Best practice is to only send the Ip-column to the  *IpLookup* operation. Example that looks up some IP addresses:

MyIpData:
LOAD \* inline "
User;Ip
Alice;188.12.2.2
Bob;176.77.23.14
" (delimiter is ';');
MyIpPoints:
Load \* Extension GeoOperations.ScriptEval('
IpLookup(ipField="Ip")
', MyIpData{Ip});

It is common that the same IP is repeated in many rows. It then improves performance to first filter out only the unique IPs like in this example:

MyIpData:
LOAD \* inline "
User;Ip
Alice;176.77.23.14
Bob;188.12.2.2
Carol;176.77.23.14
Dave;188.12.2.2
Bob;188.12.2.2
Bob;188.12.2.2
" (delimiter is ';');
MyDistinctIpData:
Load distinct Ip resident MyIpData;
MyIpPoints:
Load \* Extension GeoOperations.ScriptEval('
IpLookup(ipField="Ip")
', MyDistinctIpData);
Drop Table MyDistinctIpData;

This product includes GeoLite2 data created by MaxMind, available from  [MaxMind](https://www.maxmind.com).

Parameters for IpLookup

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| ipField | string | *optional* | The field with the IP-address to look up. Uses the key field of the dataset if not specified. |
| dataset | Dataset | *default: None.* | A dataset with IP-addresses that will be looked up in the geocoder. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Load

Loads the dataset with no operation applied. This makes it possible to load all the formats that GeoOperations supports.
Note that  *Simplify* can be a good alternative to  *Load* if geometries are detailed and slow to display.

Returns the following columns:

- All columns from  *dataset*.

Supports:

- ScriptEval in load scripts.

Example that loads postal codes from Sweden:

Load \* Extension GeoOperations.ScriptEval('Load() DATASOURCE PostalCodes LOCATIONSERVICE type="PostalCode", country="se"');

Since WKT is supported as geometry format for data in  *INTABLE*, the  *Load* operation is excellent for converting geographic geometries loaded from a database into the Sense geometry format so that it can be displayed.
The following example shows how to convert WKT data, in this case from the  *MyWKTData* table:

MyWKTData:
LOAD \*inline "
id;wkt
1;POINT(-80.204 25.791)
2;POINT(-81.381 28.538)"
(delimiter is ';');
Load \*
Extension GeoOperations.ScriptEval('
Select id, wkt as point From Load()
', MyWKTData);

Parameters for Load

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| dataset | Dataset | *default:<first dataset>* | Dataset to load. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## PointToAddressLookup

Returns the closest address for points in the list, also known as reverse geocoding.
This operation requires a special license.
Points that are close to streets will get street level addresses, otherwise it will fall back to returning postal area or city-level hits. For points too far away, no data is returned.

Information note
You must have the user role permission Use : to use PointToAddressLookup.

Returns the following columns:

- <dataset key column> - The key column from the input dataset.
- Address - The found address, formatted to the address standards of the country.
- Geometry - The point for the found item.
- HouseNumber - The house number for the found item.
- Street - The street for the found item.
- PostalCode - The postal code for the found item.
- City - The name of the city-level administrative division for the found item.
- Adm1 - The name or abbreviated name for the first order administrative division (state) for the found item.
- CountryIso2 - The country code for the found item.
- Distance - Distance in meters to the found address.
- All columns except the key column from  *dataset*, prefixed with the dataset name.

Note that the returned fields might be empty where not applicable or where data is not available.

Example that gets the addresses for some points:

MyAddressPoints:
LOAD \*
inline "
id;point
1;[-108.1,45.4]
2;[-98.9,40.1]
3;[12.1,57.7]
" (delimiter is ';');
Load \* Extension GeoOperations.ScriptEval('
PointToAddressLookup()
', MyAddressPoints);

Parameters for PointToAddressLookup

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| language | string | *default:* | A two-letter language code for the preferred language for the address in the reply. If the address is not available in the requested language it is returned in a default language for the location. |
| dataset | Dataset | *default: None.* | A dataset with points that will be looked up in the geocoder. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Routes

Calculates routes, including length and duration, between two locations in a table.

Note that the origin is the geometry column in the dataset.
The destination column is specified in operation parameters since datasets only know of one geometry column.

If you use  **bird** as transportation type it generates great circle arcs between origins and destinations.

Returns the following columns:

- <dataset key column> - The key column from the input dataset.
- Distance - The route distance in meters.
- Duration - The estimated route travel time in seconds.
- Status - The returned status is either "ok" or "failed:" followed by an error message.
- LowResLine - A low resolution version of the route line.
- All columns except the key column from the input dataset, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.
- ScriptEvalStr in chart scripts for getting the route.
- ScriptEval in chart scripts for getting the distance or duration.

This is an example that calculates routes between points in a dataset:

MyRoutePoints:
LOAD \* inline "
routeid;origin;dest
1;[12,57.7];[12,57.8]
2;[12.1,57.7];[12.2,57.7]
" (delimiter is ';');
MyRoutes:
Load \* Extension
GeoOperations.ScriptEval('Routes(destField="dest")', MyRoutePoints);

This is an example that calculates routes directly in a Line Layer. The operation is called for the selection every time the selection changes.
Normally there should be a calculation condition that is true if only a few points are selected (otherwise it is better to calculate the routes in the load script).
This should be put in the load script to load the data. For example:

Load \* Extension GeoOperations.ScriptEval(
'Load() DATASOURCE Cities LOCATIONSERVICE geometry="POINT", type="City", country="dk"');

Use the following dimension in the Line Layer:

LocationDbId

Use a calculation condition in the Line Layer:

Count(LocationDbId)<10

In the Location property, which should be set to  *Line geometry*, put this to calculate the routes from a fixed position to the selected points:

=GeoOperations.ScriptEvalStr('SELECT LowResLine from Routes(originField="Me", destField="LocationPoint")',
'[11.2,54.8]' as Me, LocationPoint)

Parameters for Routes

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| dataset | Dataset | *default: None.* | A dataset with origins and destinations for the routes to calculate. The origins should be in the geometry of the dataset. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| criteria | string | *default:fastest* | Choose between  *fastest* or  *shortest* route to be calculated. |
| transportation | string | *default:car* | The transportation mode, one of  *car*,  *truck*,  *bike*,  *pedestrian* or  *bird* (which flies at 10 m/s). |
| destField | string | *default: None.* | The field in the dataset that specifies the destination. Note that the origin is the geometry field specified in the dataset. |
| geometryType | string | *default:POINT* | Type of geometry in  *destField*. Allowed values are  *Point*,  *NamedPoint* and  *LatLon*. In case of named points, the geometry is looked up in the location service and a column for the geometry is added. |
| suffix | string | *default: None.* | For advanced users. The specified string is appended to all IDs. This is a convenient way to specify more information to server based location services such as country code or type. The alternative is to append the extra data when loading the table into Qlik. With the following suffix all items are specified to be cities in Sweden: ,SE:city See the  *Location Service Guide* for more information on syntax to use. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Simplify

Simplifies line and area geometries in a dataset.
It is often useful to load geographic data with the  *Simplify* operation instead of the  *Load* operation to get more efficient geometries that are faster to display.

The degree of simplification is calculated automatically based on area, number of objects and size of objects.
It is then possible to adjust that to a higher or lower resolution with the  *resolution* parameter.

Area simplification is done with an algorithm that handles topologies and can remove gaps and join islands.

Line simplification is done with a breakpoint reduction algorithm.

Note that overlaps of polygons are removed. There will be no overlapping polygons in the output.

Returns the following columns:

- <dataset key column> - The key column from the input  *dataset1*.
- Simplified\_<geometry column name> - Simplified versions of the original geometries.
- All columns except the key column from  *dataset*, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.

Example that loads simplified versions of US states:

Load \* Extension GeoOperations.ScriptEval('
SELECT LocationDbId, Simplified\_LocationPolygon FROM Simplify()
DATASOURCE states LOCATIONSERVICE type="State", country="us"
');

Parameters for Simplify

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| resolution | string | *default:Auto* | The resulting dataset is simplified and the degree of simplification is controlled by this property. Available values are:  - **Auto** - The operation calculates a resolution based on the data. - **AutoLow** - A resolution that is lower than (half of) the Auto-resolution. - **AutoHigh** - A resolution that is higher than (double of) the Auto-resolution. |
| dataset | Dataset | *default:<first dataset>* | The dataset with geometries to simplify. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## TravelAreas

Calculates travel time ISO areas.
All locations within the returned area can be reached within a certain time or is closer than a certain distance along roads.
Returns a table with id, travel area geometry, center point, cost, cost unit and status (OK or failed).

If you use "bird" as transportation type it generates geographically correct circles around the origins.

Returns the following columns:

- <dataset key column> - The key column from the input dataset.
- TravelArea - The polygon geometry that defines the travel area.
- Cost - The cost as specified in the costValue or costField.
- CostUnit - The cost unit as specified in costUnit.
- Status - The returned status is either "OK" or "failed:" followed by an error message.
- All columns except the key column from the input dataset, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.
- ScriptEvalStr in chart scripts for getting the travel area geometry.
- ScriptEval in chart scripts for getting cost.

This load script example generates 10-minute travel areas in Miami and Orlando from coordinates:

MyPoints:
LOAD \*
inline "
id;point
1;[-80.204,25.791]
2;[-81.381,28.538]
" (delimiter is ';');
MyTravelAreas:
Load \*
Extension GeoOperations.ScriptEval(
'SELECT id, TravelArea from TravelAreas(costValue="10", costUnit="Minutes")', MyPoints);

This load script example generates 10-minute travel areas in Miami and Orlando using named points:

MyCities:
LOAD \*
inline "
cid;City
1;Miami,US
2;Orlando,FL,US
" (delimiter is ';');
Load \* Extension
GeoOperations.ScriptEval('TravelAreas(costValue="10",costUnit="minutes")
DATASOURCE cities INTABLE keyField="City", namedPointField="City"', MyCities {City});

This is an example that calculates Travel Areas around points directly in an Area Layer. The operation is called for the selection every time the selection changes.
This should be put in the load script to load the data for the example:

MyAirports:
Load \*
Extension GeoOperations.ScriptEval('
Load()
DATASOURCE airports LOCATIONSERVICE geometry="POINT", type="AirportIATA", country="se"
');

Use the following dimension in the Area Layer:

LocationDbId

Use a calculation condition in the Area Layer:

Count(LocationDbId)<10

In the Location property put this:

=GeoOperations.ScriptEvalStr('Select TravelArea from TravelAreas(costValue="10", costUnit="minutes")', LocationPoint)

Parameters for TravelAreas

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| dataset | Dataset | *default:<first dataset>* | A dataset with origins and optionally costs for the travel area calculations. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| costValue | number | *default: None.* | The cost at the border of the returned area. The cost can be either a length or a time. (See costUnit below.) An alternative that allows individual costs for each area is to specify costField instead. |
| costField | string | *default: None.* | A field in the dataset that specifies the cost. This is only used if costValue is empty. |
| costUnit | string | *default:seconds* | Should be one of seconds, minutes, hours, meters, yards, kilometers, or miles. When a time unit is used, the area reached within that time is calculated, and when a length unit is used, the area with a travel distance shorter than specified is calculated. |
| transportation | string | *default:car* | The transportation mode, one of car, truck, bike, pedestrian, or bird (which flies at 10 m/s). |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |

## Within

Returns the relations between two datasets where a geometry in one dataset (enclosed) is completely inside the area in the other dataset (enclosing).
Returns a table that maps between the key in enclosed and the key in enclosing for all found relations.

Use within typically for finding which areas the data is in;
for example, to test GPS position for which administrative area they are in.
This is a kind of reverse geocoding.

Returns the following columns:

- <enclosed name>\_<enclosing name>\_RelationId - A key generated for the relation between the two geometries.
- <enclosed key column> - The key column from the input dataset1.
- <enclosing key column> - The key column from the input dataset2.
- All columns except the key column from the  *enclosed* dataset, prefixed with the dataset name.
- All columns except the key column from the  *enclosing* dataset, prefixed with the dataset name.

Supports:

- ScriptEval in load scripts.

To compensate for inaccuracies in data, it is sometimes better to use  *Closest* instead of  *Within*. For instance, if you have point data in coastal
areas which you want to relate to administrative areas, small inaccuracies can make points fall slightly outside of the areas.

This is a load script example that calculates which points are within which states:

MyPoints:
LOAD \*
inline "
id;point
1;[-108.1,45.4]
2;[-98.9,40.1]
3;[12.1,57.7]
" (delimiter is ';');
PointsInStates:
Load \* Extension GeoOperations.ScriptEval('
Within()
DATASOURCE states LOCATIONSERVICE geometry="AREA", type="Admin1", country="us"
', MyPoints);

Parameters for Within

| Parameter | Type | Use | Description |
| --- | --- | --- | --- |
| enclosed | Dataset | *default:<first dataset>* | A dataset with geometries to test for which areas they are enclosed by. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| enclosing | Dataset | *default:<second dataset>* | A dataset with area geometries to test for which geometries they enclose. Supports streaming of this dataset when sent from the load script which means that larger tables are allowed. |
| precision | integer | *default:6* | Sets the number of decimals to round to in coordinates. The default value is 6 decimals, which is precise to around 10 cm. If you do not want coordinates rounded, set the value to a negative number. |
