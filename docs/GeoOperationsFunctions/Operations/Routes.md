---
title: "Routes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Routes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Routes

Routes calculates routes between two locations in a dataset, including length and duration.

Example of Routes

![A map displaying routes between points.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-routes.png "Click to view full size")

Routes supports the following transportation modes:

- Bird: Generates arcs between origins and destinations.
- Car: Creates routes along roads with car restrictions. Only supported for point datasets.
- Bike: Creates routes along roads with bike restrictions. Only supported for point datasets.
- Pedestrian: Creates routes along roads with pedestrian restrictions. Only supported for point datasets.
- Truck: Creates routes along roads with truck restrictions. Only supported for point datasets.

Routes returns the following fields:

- <dataset key field>: The key field from the input dataset.
- Distance: The route distance in meters.
- Duration: The estimated route travel time in seconds.
- Status: The returned status is either ok or failed: followed by an error message.
- LowResLine: A low resolution version of the route line.
- All fields except the key field from the input dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Routes.
3. Under Criteria, select Fastest route or Shortest route.
4. Under Transportation mode, select the mode used to calculate the route.
5. Under Destination field, select the destinations used when calculating routes.
6. Under Destination field type, select the type of data in the destination field.
7. If you selected Named point as the Destination field type, under Location suffix, optionally add a suffix to append to the field values.

   This is useful to specify more information to server-based location services such as country code or type. For example, with the following suffix all items are specified to be cities in Sweden: ,SE:city.

   For more information on what syntax to use, see [Location service](https://help.qlik.com/en-US/geoanalytics/Content/Qlik_GeoAnalytics/GeoAnalytics-Sense/Location-Service-Sense.htm).
8. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   You must specify the origin as the geometry field in the dataset.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
9. Under Tables, select the table to load.
10. Under Fields, select the fields to load.
11. Click Insert script.

Related learning:

- [How do I add route information to a Qlik Sense map that shows the fastest or shortest distance between points?](/lnk/How_route_Qlik_Sense_map)
