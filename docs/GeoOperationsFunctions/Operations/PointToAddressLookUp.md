---
title: "Point to address lookup"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/PointToAddressLookUp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Point to address lookup

Point to address lookup returns the closest address for points in the list, also known as reverse geocoding. Point to address lookup requires a Qlik Geocoding license.

Information note

Point to address lookup requires a license for Qlik Geocoding. The functionality offered by Qlik Geocoding with Address to point lookup and Point to address lookup is distinct from other location lookup features. Qlik Geocoding allows lookups at the address level, whereas other Qlik location lookups are only as precise as the ZIP code level.

For more information, see [*Qlik Geocoding*](../../GeoCoding/Qlik-GeoCoding.htm).

Information noteYou must have the user role permission Use GeoOperations: Allowed to use Point to address lookup.

Points that are close to streets will return street level addresses. Otherwise, Point to address lookup returns postal area or city-level results. For points too far away from any known address, no data is returned.

Point to address lookup returns the following fields:

- <dataset key field>: The key field from the input dataset.
- Address: The found address, formatted to the address standards of the country.
- Geometry: The point for the found item.
- HouseNumber: The house number for the found item.
- Street: The street for the found item.
- PostalCode: The postal code for the found item.
- City: The name of the city-level administrative division for the found item.
- Adm1: The name or abbreviated name for the first order administrative division (state) for the found item.
- CountryIso2: The country code for the found item.
- Distance: Distance in meters to the found address.
- All fields except the key field from dataset, prefixed with the dataset name.

Information note

Returned fields might be empty where not applicable or where data is not available.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Point to address lookup.
3. Under Language, enter the two-letter language code for the language in which you want the address data returned.

   If no language is specified, it the address data is returned in the default language for the lookup location.
4. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
5. Under Tables, select the table to load.
6. Under Fields, select the fields to load.
7. Click Insert script.
