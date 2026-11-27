---
title: "How I made this: Overlapping travel areas"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/GeoOperations-Travel-Area-Example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources"]
---

# How I made this: Overlapping travel areas

You can generate multiple travel areas in a single field and use them in an area layer. For example, you may want to view see incremental increases in travel areas for a single point.

In this example, a map has been added that has a 60 minute travel area in road distance for Canadian provincial and territorial capitals in 10 minute increments

Map containing 60-minute travel areas for Canadian provincial and territorial capitals

![Example map displaying only highlight points for each Canadian capital](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_travelarea-example.png "Click to view full size")

When you click on point for a city, the map zooms in, making it easier to see the travel areas for the city.

Zoomed in view of the travel areas of Fredericton

![Example zoomed-in view after a point has been selected, displaying more detailed road and travel data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_travelarea-example-zoom.png "Click to view full size")

The cost values for the area layer have been sorted so that the areas are overlaid on the map from greatest area to smallest area. This enables the smallest areas to be selected by users as otherwise they would be overlaid with the larger areas that overlap with them.

## Data

This example uses a single data set that is added inline in Data load editor.

[Cities]:

LOAD \* inline

[

City

Edmonton,Canada;

Victoria,Canada;

Winnipeg,Canada;

Fredericton,Canada;

St. John's,Canada;

Halifax,Canada;

Toronto,Canada;

Charlottetown,Canada;

Quebec City,Canada;

Regina,Canada;

Whitehorse,Canada;

Iqaluit,Canada;

Yellowknife,Canada;

]

(delimiter is ';');

## How I build this

Do the following:

1. Add the data into Data load editor.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select Qlik GeoOperations from the list of data connectors.
5. Click Create.
6. Under Data connections, click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
7. Under Operation, select Travel areas.
8. Under Cost, select Value and 60.
9. Under Cost units, select Minutes.
10. Under Transportation mode, select Car.
11. Under Dataset 1, select Loaded table.
12. Under Table name, enter Cities.
13. Under Key field, select Specify and enter City.
14. Under Geometry type and field, select Named point and enter City.
15. Select the table and select the following fields:

    - City
    - TravelArea
    - Cost
16. Click Insert script.
17. Rename the table TravelArea.

    Copy and paste the inserted script five times and edit the costValue to 50, 40, 30, 20, and 10.

    Your load script should now look like this:

    [TravelArea]:
    Load \* Extension GeoOperations.ScriptEval('
    SELECT City, TravelArea, Cost FROM
    TravelAreas(costValue="60", costUnit="minutes", transportation="car")
    DATASOURCE dataset INTABLE keyField="City", crs="EPSG:4326", namedPointField="City"
    ', Cities);
    Load \* Extension GeoOperations.ScriptEval('
    SELECT City, TravelArea, Cost FROM
    TravelAreas(costValue="50", costUnit="minutes", transportation="car")
    DATASOURCE dataset INTABLE keyField="City", crs="EPSG:4326", namedPointField="City"
    ', Cities);
    Load \* Extension GeoOperations.ScriptEval('
    SELECT City, TravelArea, Cost FROM
    TravelAreas(costValue="40", costUnit="minutes", transportation="car")
    DATASOURCE dataset INTABLE keyField="City", crs="EPSG:4326", namedPointField="City"
    ', Cities);
    Load \* Extension GeoOperations.ScriptEval('
    SELECT City, TravelArea, Cost FROM
    TravelAreas(costValue="30", costUnit="minutes", transportation="car")
    DATASOURCE dataset INTABLE keyField="City", crs="EPSG:4326", namedPointField="City"
    ', Cities);
    Load \* Extension GeoOperations.ScriptEval('
    SELECT City, TravelArea, Cost FROM
    TravelAreas(costValue="20", costUnit="minutes", transportation="car")
    DATASOURCE dataset INTABLE keyField="City", crs="EPSG:4326", namedPointField="City"
    ', Cities);
    Load \* Extension GeoOperations.ScriptEval('
    SELECT City, TravelArea, Cost FROM
    TravelAreas(costValue="10", costUnit="minutes", transportation="car")
    DATASOURCE dataset INTABLE keyField="City", crs="EPSG:4326", namedPointField="City"
    ', Cities);
18. Load the data.
19. In the sheet view, add the field Cost as a master dimension called Cost. Assign these colors to the following values:

    - 10: 0096ff
    - 20: 40ff0c
    - 30: faff09
    - 40: ee8a03
    - 50: ff020d
    - 60: c100ff
20. Add a map.
21. Add a point layer with City as the dimension. Set the following properties:

    - In Color, set the Color to #f8981d.
22. Add an area layer with TravelArea as the dimension. Set the following properties:

    - In Dimensions, change Label to Travel area.
    - In Colors, do the following:
      - Color By dimension using the master dimension Cost and enable Library colors.
      - Set the Outline color to 000000.
      - Set Opacity to 50%.
    - In Sorting, set Travel area to sort numerically and by descending value.
23. Center the region in the map and then set Limit pan navigation to Custom and click Set pan limit.
