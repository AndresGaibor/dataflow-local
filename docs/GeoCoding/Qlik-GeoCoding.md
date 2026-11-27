---
title: "Qlik Geocoding"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoCoding/Qlik-GeoCoding.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources"]
---

# Qlik Geocoding

Qlik Cloud Government noteQlik Cloud Government does not support Qlik Geocoding.

Qlik Geocoding® is a subscription service that adds address data lookup functionality to Qlik GeoOperations for Qlik Cloud.

Qlik Geocoding is remotely hosted by Qlik. It provides geographical (GPS) coordinates corresponding to a location, such as a street address and vice versa. Each address or individual coordinate set sent to the Qlik Geocoding server constitutes a lookup request, regardless of the extent to which resulting data is returned (e.g. an invalid or incomplete street address or GPS coordinates may result in non-discrete data or no data at all being returned). Up to five thousand (5,000) lookup requests may be sent in a single call to the Qlik Geocoding server. Geocoding is sold as a fixed quantity of lookup requests, where such quantity of lookups must be used within one (1) year from the date of purchase. Unused lookup requests remaining as of the date of expiration are forfeited.

Qlik Geocoding is accessed through QlikGeoOperations using the operations Address to point lookup and Point to address lookup. The service features both Forward Geocoding (address to point conversion) with the result including information about match level and location structure, and Reverse Geocoding (point to address conversion) which can be used for converting GPS coordinates to a location.

[*Address to point lookup*](../GeoOperationsFunctions/Operations/AddressPointLookup.htm)

[*Point to address lookup*](../GeoOperationsFunctions/Operations/PointToAddressLookUp.htm)

To get started,

1. Please contact your Qlik sales representative for pricing and license information.
2. Follow the [*Using Qlik Geocoding*](Qlik-GeoCoding-setup.htm) setup instructions.
3. Start converting and implementing addresses and lookup into your application workflow.

Please visit the [Qlik Community](https://community.qlik.com/t5/Qlik-GeoAnalytics/ct-p/qlik-geoanalytics) for more information, tutorials and support for Qlik GeoAnalytics.
