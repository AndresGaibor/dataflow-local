---
title: "Qlik Geocoding best practices"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoCoding/Qlik-GeoCoding-guidelines.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik Geocoding"]
---

# Qlik Geocoding best practices

Follow these guidelines to improve your results and avoid redundant queries.

- Properly configure and use the template application, as described in [*Using Qlik Geocoding*](Qlik-GeoCoding-setup.htm).
- Try with a small number of addresses first.
- Always store the result in QVD (as the template application does).
- Only perform lookups of new addresses (as the template application does).
- Do not insert sensitive data in index or address fields, which would violate the Qlik Geocoding terms of service.
- Split larger tables in consecutive calls (as the template application does).
- Use specific address fields, to yield better and faster results.
- Fill in all indata fields with proper info. Quality of lookup is highly dependent on the quality of the indata.
- Make sure that the address fields only contain address information. Company names, phone numbers, c/o, apartment number, etc. may alter the result.
- If an location field's info is missing or corrupt, it is better to leave that field blank.
- Write out abbreviations if ambiguous, e.g. "C." could be “Corso”, “Calle” or “Contrado”.
- Zip/postal code data has very high priority, so omit it if you are at all unsure about the accuracy of the data.
- Every lookup on the service counts as a transaction, independent of the response.
