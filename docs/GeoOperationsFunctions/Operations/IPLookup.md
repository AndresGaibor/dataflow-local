---
title: "IP lookup"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/IPLookup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# IP lookup

IP lookup returns location information and point geometries for IP addresses in a table.

IP lookup is useful when you are analyzing access data to web services. The returned table contains the following fields:

- <key field>: The same as the key field for the name table.
- <address table IP field>: The same as the IP field that was looked up. Only available if it is not the same as the key field.
- IpPoint: The point for the found item.
- CountryIso2: The country code for the found item.
- Adm1Code: The code for the first order administrative area for the found item. Note that this code is not always compatible with the code returned by the location service.
- City: The city for the found item.
- All fields except the key field from the input dataset, prefixed with the dataset name.

IP geolocation is inherently imprecise. For many IP-addresses it is possible to pinpoint a city, but for others only country can be resolved.

It is common that the same IP is repeated in many rows in a table. As a best practice, performance is improved if you filter out only the unique IP addresses. For example:

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
[IplookupResultTable]:
Load \* Extension GeoOperations.ScriptEval('
SELECT Ip, IpPoint, CountryIso2, Adm1Code, City FROM
IpLookup(ipField="Ip")
DATASOURCE ipDataset INTABLE keyField="Ip", crs="EPSG:4326"
', MyDistinctIpData);
Drop Table MyDistinctIpData;

In this example, the table MyDistinctIpData is used to filter distinct IP data from MyIpData. IplookupResultTable is added by Qlik GeoOperations IP lookup. Then MyDistinctIpData is dropped from the load script.

Information note

Qlik GeoOperations includes GeoLite2 data created by MaxMind, available from MaxMind.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select IP lookup.
3. Under IP address field, enter the field containing IP addresses.
4. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
5. Under Tables, select the table to load.
6. Under Fields, select the fields to load.
7. Click Insert script.
