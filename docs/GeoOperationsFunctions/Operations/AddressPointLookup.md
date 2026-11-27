---
title: "Address to point lookup"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/AddressPointLookup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Address to point lookup

Address to point lookup creates point geometries for addresses in a table, also known as geocoding. You can specify an address using a text string, use fields to structure the lookup, or use a combination of both.

Information note

Address to point lookup requires a license for Qlik Geocoding. The functionality offered by Qlik Geocoding with Address to point lookup and Point to address lookup is distinct from other location lookup features. Qlik Geocoding allows lookups at the address level, whereas other Qlik location lookups are only as precise as the ZIP code level.

For more information, see [*Qlik Geocoding*](../../GeoCoding/Qlik-GeoCoding.htm).

Information noteYou must have the user role permission Use GeoOperations: Allowed to use Address to point lookup.

Addresses that cannot be found for any reason are not returned in the result.

Address to point lookup can use the following parameters for looking up locations, either entered as text strings or included in fields:

- Search string: A string of text to search for containing addresses. This can be addresses, such as 1600 Pennsylvania Ave, Washington DC, USA. It can also be incomplete addresses that are combined with data in other fields. For example, 1117 Washington Ave with City set to Philadelphia and Country set to USA.
- Country: A string or field containing three-letter ISO codes. Multiple countries can be specified, separated by commas. For example, SWE,NOR,FIN.

  Information note

  To geocode English or Pinyin addresses in China, the Country parameter must be set to "CHN".
- State: First-level administrative areas, either their name or code.
- City: City name, municipality, or postal city.
- Postal code: The postal code of the address.
- Street: The street name. Instead of specifying street and house number in separate parameters or fields, both can be specified together, separated by a space.
- House numbers: House numbers.

Tip note

For best results, favor specific data and omit broad data whenever possible. For instance, if you have both a postal code and postal city, and you trust that the postal code is correct, then it is best to not specify the postal city.

Address to point lookup returns the following fields:

- <dataset key field>: The key field from the input dataset.
- Address: The found address, formatted to address standards of the country.
- <geometry>: The point for the found item.
- HouseNumber: The house number for the found item.
- Street: The street for the found item.
- PostalCode: The postal code for the found item.
- City: The name of the city-level administrative division for the found item.
- Adm1: The name or abbreviated name for the first-order administrative division (state) for the found item.
- CountryIso2: The country code for the found item.
- Match: A value between 0 and 1 that shows how good the match was. A value of 1 means a perfect match.
- All fields except the key field from dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Address to point lookup.
3. Under Operation parameters, enter your address data to the corresponding parameters.

   To enter a text string, select Value and enter your text.

   To enter a field, select Field and enter the name of the corresponding field.
4. Under Match threshold, set the threshold to return results.

   By default, the value if 0.5. If you are receiving false hits, increase this value. A value of 1 means a perfect match.
5. Under Language, enter the two-letter language code for the language in which you want the address data returned.

   If no language is specified, it the address data is returned in the default language for the lookup location.
6. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
7. Under Tables, select the table to load.
8. Under Fields, select the fields to load.
9. Click Insert script.
