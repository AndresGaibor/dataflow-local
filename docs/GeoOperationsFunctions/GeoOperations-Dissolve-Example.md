---
title: "How I made this: Dissolving regions and subregions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/GeoOperations-Dissolve-Example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources"]
---

# How I made this: Dissolving regions and subregions

You can create custom regions using the dissolve operation. Using drill-down dimensions, you can create a hierarchical relationship between the multiple dissolved areas.

In this example, a map has been added that has USA states dissolved into regions and subregions. The maps use a drill-down dimension to create the hierarchy between region, subregion, and state.

Map with dissolved regions of the USA

![Example map of the United States dissolved into regions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_dissolve-example.png "Click to view full size")

When you select a region, it drills down to the component subregions.

Map with a dissolved region selected, showing dissolved subregions

![Map with a region selected, now displaying dissolved subregions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_dissolve-example-subregion.png "Click to view full size")

Selecting a subregion then displays the component states.

Map with a subregion selected showing component states

![Map of a selected subregion, now displaying individual component states](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/GeoAnalytics/ui_dissolve-example-state.png "Click to view full size")

Two drill-down dimensions are used to make this map. One contains the names of the regions and states. The second contains the geometry and is used as the location field.

## Data

This example uses a single data set that is added inline in data load editor.

Region data

Regions:

LOAD \* inline

"

State;RegionName;SubregionName

Alabama,US;South;East South Central

Alaska,US;West;Pacific

Arizona,US;West;Mountain

Arkansas,US;South;West South Central

California,US;West;Pacific

Colorado,US;West;Mountain

Connecticut,US;Northeast;New England

Delaware,US;South;South Atlantic

Florida,US;South;South Atlantic

Georgia,US;South;South Atlantic

Hawaii,US;West;Pacific

Idaho,US;West;Mountain

Illinois,US;Midwest;East North Central

Indiana,US;Midwest;East North Central

Iowa,US;Midwest;West North Central

Kansas,US;Midwest;West North Central

Kentucky,US;South;East South Central

Louisiana,US;South;West South Central

Maine,US;Northeast;New England

Maryland,US;South;South Atlantic

Massachusetts,US;Northeast;New England

Michigan,US;Midwest;East North Central

Minnesota,US;Midwest;West North Central

Mississippi,US;South;East South Central

Missouri,US;Midwest;West North Central

Montana,US;West;Mountain

Nebraska,US;Midwest;West North Central

Nevada,US;West;Mountain

New Hampshire,US;Northeast;New England

New Jersey,US;Northeast;Mid-Atlantic

New Mexico,US;West;Mountain

New York,US;Northeast;Mid-Atlantic

North Carolina,US;South;South Atlantic

North Dakota,US;Midwest;West North Central

Ohio,US;Midwest;East North Central

Oklahoma,US;South;West South Central

Oregon,US;West;Pacific

Pennsylvania,US;Northeast;Mid-Atlantic

Rhode Island,US;Northeast;New England

South Carolina,US;South;South Atlantic

South Dakota,US;Midwest;West North Central

Tennessee,US;South;East South Central

Texas,US;South;West South Central

Utah,US;West;Mountain

Vermont,US;Northeast;New England

Virginia,US;South;South Atlantic

Washington,US;West;Pacific

West Virginia,US;South;South Atlantic

Wisconsin,US;Midwest;East North Central

Wyoming,US;West;Mountain

District of Columbia;South;South Atlantic

"

(delimiter is ';');

## How I built this

1. Add the data into Data load editor.
2. Click Create new connection and select Qlik GeoOperations.
3. Click Create new connection.
4. Under Space, select the space where the connection will be located.
5. Select Qlik GeoOperations from the list of data connectors.
6. Click Create.
7. Under Data connections, click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
8. Under Operation, select Dissolve.
9. Set the following parameters:

   - Dissolve field: SubregionName
   - Resolution: Source.
10. Under Dataset 1, set the following parameters:
    - Type: Loaded table
    - Table name: Regions
    - Key field: State
    - Geometry type and field: Named area and State.
11. Select the table and select the following fields:
    - SubregionName
    - DissolvedPolygon
12. Click Insert script.
13. In the script, replace DissolvedPolygon with DissolvedPolygon as SubregionPolygon.

    Tip note

    When you are using multiple operations, it is important to rename default field names used by Qlik GeoOperations to avoid creating unwanted concatenations and loops in your load script.
14. Under Data connections, click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on your Qlik GeoOperations connection.
15. Under Operation, select Dissolve.
16. Set the following parameters:

    - Dissolve field: RegionName
    - Resolution: Source.
17. Under Dataset 1, set the following parameters:
    - Type: Loaded table
    - Table name: Regions
    - Key field: State
    - Geometry type and field: Named area and State.
18. Select the table and select the following fields:
    - RegionName
    - DissolvedPolygon
19. Click Insert script.
20. In the script, replace DissolvedPolygon with DissolvedPolygon as RegionPolygon.
21. Load the data.
22. In the sheet view, create a drill-down dimension called Regions. Add the following fields to it, in order:

    - RegionName
    - SubregionName
    - State
23. Create a drill-down dimension called RegionPolygons. Add the following fields to it, in order:

    - RegionPolygon
    - SubregionPolygon
    - State
24. Add a map.
25. Add an area layer using Regions as the dimension. Set the following properties:

    - In Location, set the Location field to RegionPolygons.
    - In Colors, set Colors to Custom and do the following:
      - Select Persistent colors
      - Select 100 colors.
      - Set Opacity to 50%.
      - Set Outline color to 000000.
26. Center the region in the map and then set Limit pan navigation to Custom and click Set pan limit.
