---
title: "Closest"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Closest.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Closest

Closest returns relations and distances between objects in one dataset and the closest objects in another dataset, if any is closer than the maximum distance. This operation is useful both for getting the relations to the closest objects as well as getting distance matrices between a set of points.

Example of Closest

![A map displaying the closest objects to a set of other objects.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-closest.png "Click to view full size")

When you use Closest, you must specify the unit of measurement as well as how the distance is measured. Closest supports the following units for measuring distance:

- Meters
- Kilometers
- Yards
- Miles
- Seconds
- Minutes
- Hours

Closest supports the following methods for measuring distance:

- Bird: Measures direct distances between objects.
- Car: Measures along roads with car restrictions. Only supported for point datasets.
- Bike: Measures along roads with bike restrictions. Only supported for point datasets.
- Pedestrian: Measures along roads with pedestrian restrictions. Only supported for point datasets.
- Truck: Measures along roads with truck restrictions. Only supported for point datasets.

Closest can be used to compare closeness between objects in the same dataset or between two datasets. When comparing distances in a single dataset, distances are never calculated from an object to itself.

Closest returns the following fields:

- <dataset1 name>\_<dataset2 name>\_RelationId : A key generated for the relation between the two geometries.
- <dataset1 key column>: The key column from the first dataset.
- <dataset2 key column>: The key column from the second dataset.
- Distance: The distance in the unit specified in Distance unit.
- Status: The returned status is either ok or failed: followed by an error message.
- LowResLine: A low resolution version of the route line, only available for non-bird distance types.
- All fields except the key column from the first dataset, prefixed with the dataset name.
- All fields except the key column from the second dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Closest.
3. Under Distance, enter the maximum distance items can be apart from each other in the distance unit.
4. Under Distance unit, select the unit to use.
5. Under Distance type, select how distances are to be measured.
6. Under Closest count, select how many objects in the second dataset to associate with an object in the first dataset.

   A value of 1 means only the closest object, a value of 2 means the two closest objects, and so on.
7. Under Use two datasets, select to use two key field from two datasets or a key field from a single dataset.
8. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
9. If you are using a second dataset, under Dataset 2, select the type of data to load and the parameters.

   For more information on loading data in Qlik GeoOperations, see [*Load*](Load.htm).
10. Under Tables, select the table to load.
11. Under Fields, select the fields to load.
12. Click Insert script.
