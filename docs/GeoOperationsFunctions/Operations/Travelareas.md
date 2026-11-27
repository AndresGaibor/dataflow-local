---
title: "Travel areas"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/Operations/Travelareas.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources", "Qlik GeoOperations connection"]
---

# Travel areas

Travel areas calculates ISO travel areas based on time or distance. All locations within the returned area can be reached within a certain time or are closer than a certain distance along roads.

Example of Travel areas

![A map displaying reachable areas from two points.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_geo-travelareasfrompoints.png "Click to view full size")

You can calculate a travel area using one of the following units:

- Seconds
- Minutes
- Hours
- Meters
- Yards
- Kilometers
- Miles

When a time unit is used, Travel area calculates the area reached within that time. When a distance unit is used, Travel area calculates the area within a travel distance shorter than specified distance.

When calculating a travel area, you select a type of transportation to use. The following transportation types are available:

- Bird: Calculates the travel area for a flying bird traveling at 10 meters per second.
- Car: Creates travel area along roads with car restrictions.
- Bike: Creates travel areas along roads with bike restrictions.
- Pedestrian: Creates travel areas along roads with pedestrian restrictions.
- Truck: Creates travel areas along roads with truck restrictions.

Travel areas returns the following fields:

- <dataset key column>: The key column from the input dataset.
- TravelArea: The polygon geometry that defines the travel area.
- Cost: The cost as specified in Cost and Cost unit.
- CostUnit: The cost unit as specified in Cost unit.
- Status: The returned status is either OK or failed: followed by an error message.
- All columns except the key column from the input dataset, prefixed with the dataset name.

Do the following:

1. Under Data connections, click ![Select data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
2. Under Operation, select Travel areas.
3. Under Cost, enter how many of your selected unit should be used to calculate the travel area.

   To use a manually entered number, select Value and enter the cost.

   To use numbers from a field, select Field and enter the field name containing your travel area costs.
4. Under Cost unit, select the unit to use in the travel area.
5. Under Transportation mode, select the form of transportation to use to calculate the travel area.
6. Under Dataset 1, select the type of data source to use in the operation and its parameters.

   The data types and parameters are the same as those in the Load operation. For information on each of the dataset parameters, see:

   - [*Loading from a file*](Load.htm#Loading)
   - [*Loading data from a separated text file*](Load.htm#Loading2)
   - [*Loading standard areas and points*](Load.htm#Loading3)
   - [*Loading a previously loaded table*](Load.htm#Loading4)
7. Under Tables, select the table to load.
8. Under Fields, select the fields to load.
9. Click Insert script.
