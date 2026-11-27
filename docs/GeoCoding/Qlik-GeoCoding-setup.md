---
title: "Using Qlik Geocoding"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoCoding/Qlik-GeoCoding-setup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik Geocoding"]
---

# Using Qlik Geocoding

Once you have purchased Qlik Geocoding, you can use the Qlik GeoOperations connection with Address to point lookup and Point to address lookup. While you can use these functions in any application, it is recommended to build your datasets using the template application available for Qlik Geocoding.

The template application uses an optimal workflow and will help you avoid overusing the limited number of address lookups available with Qlik Geocoding. It stores the points in a QVD file and uses the addresses and points in the QVD file to make sure that addresses that have already been geocoded are not geocoded again.

Information noteYou must have the user role permission Use GeoOperations: Allowed to use Qlik Geocoding.

## Download the template application

Download the template application from [Qlik Community](https://community.qlik.com/t5/Qlik-GeoAnalytics-Documents/Qlik-Geocoding-Geocoding-Template-Data-and-presentation/ta-p/1548595).

## Load the addresses

Replace the example addresses in the Load Addresses section of the load script.

Start with a small list, loading only 10-20 test addresses, making sure to use the same names for fields, remapping if necessary.

For example (test\_addresses\_400.xlsx):

addresses:
First 10
LOAD
id,
street,
city,
state,
zip,
country
FROM [lib://DataFiles/test\_addresses\_400.xlsx]
(ooxml, embedded labels, table is addresses);

## Modify paths (if needed)

Optionally, modify the paths Qlik Geocoding uses for the space the application is in and the space to which AddressPointLookupResult.qvd will be output. By default, AddressPointLookupResult.qvd is output to your personal space. For guidelines on referrencing specific spaces in the script, see [*Referring to a data connection in the script*](../../Sense_Hub/LoadData/connect-data-sources-data-load-editor.htm#Referrin).

## Run the load script

Run the script. The results will be saved to AddressPointLookupResult.qvd in the specified space.

The QVD file can be imported into other applications, using the “id” field as the key.

## Further documentation

For more information on using Address to point lookup in a Qlik GeoOperations connection, see [*Address to point lookup*](../GeoOperationsFunctions/Operations/AddressPointLookup.htm). For information on scripting using AddressPointLookup, see [AddressPointLookup](/en-US/cloud-services/Subsystems/Sense_GeoOperations/Content/Sense_GeoOperations/connector-geoanalytics_reference-Operation.htm#anchor-1).

For more information on using Point to address lookup in a Qlik GeoOperations connection, see [*Point to address lookup*](../GeoOperationsFunctions/Operations/PointToAddressLookUp.htm). For information on scripting using PointToAddressLookup, see [PointToAddressLookup](/en-US/cloud-services/Subsystems/Sense_GeoOperations/Content/Sense_GeoOperations/connector-geoanalytics_reference-Operation.htm#anchor-9).
