---
title: "Creating a map with multiple background layers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/map-backgroundlayers-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating maps"]
---

# Creating a map with multiple background layers

You can use multiple background layers in a map chart. This enables you to create layered base maps for your map chart data.

Some WMS sources include layers with transparency. With these sources, you can overlay the WMS background layer on top of a base map or other layers. Images can also be placed over other background layers. This enables you to create more complex base maps for your data.

Information note

Whether or not an WMS transparency layer supports transparency is dependent on the WMS source.

In this map example, a custom TMS is used in a background layer. A WMS background layer is placed on top, using a WMS endpoint from the National Ocean and Atmospheric Administration. The WMS layer shows weather radar data.

Map chart with a point layer overlaid on TMS and WMS background layers

![Map chart with a point layer overlaid on TMS and WMS background layers](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_map-background-wms-tms_example.png "Click to view full size")

## Dataset

This example uses a single table for data, Cities, with an external TMS and WMS data from external sources.

Cities

Cities

| Cities |
| --- |
| Albany, New York |
| Annapolis, Maryland |
| Atlanta, Georgia |
| Augusta, Maine |
| Austin, Texas |
| Baton Rouge, Louisiana |
| Bismarck, North Dakota |
| Boise, Idaho |
| Boston, Massachusetts |
| Carson City, Nevada |
| Charleston, West Virginia |
| Cheyenne, Wyoming |
| Columbia, South Carolina |
| Columbus, Ohio |
| Concord, New Hampshire |
| Denver, Colorado |
| Des Moines, Iowa |
| Dover, Delaware |
| Frankfort, Kentucky |
| Harrisburg, Pennsylvania |
| Hartford, Connecticut |
| Helena, Montana |
| Honolulu, Hawaii |
| Indianapolis, Indiana |
| Jackson, Mississippi |
| Jefferson City, Missouri |
| Juneau, Alaska |
| Lansing, Michigan |
| Lincoln, Nebraska |
| Little Rock, Arkansas |
| Madison, Wisconsin |
| Montgomery, Alabama |
| Montpelier, Vermont |
| Nashville, Tennessee |
| Oklahoma City, Oklahoma |
| Olympia, Washington |
| Phoenix, Arizona |
| Pierre, South Dakota |
| Providence, Rhode Island |
| Raleigh, North Carolina |
| Richmond, Virginia |
| Sacramento, California |
| Saint Paul, Minnesota |
| Salem, Oregon |
| Salt Lake City, Utah |
| Santa Fe, New Mexico |
| Springfield, Illinois |
| Tallahassee, Florida |
| Topeka, Kansas |
| Trenton, New Jersey |

## How I built this

Tip note

This example adds layers so that they are layered on top of each other in the final order. If you add these layers in a different order, you click and drag layers into the correct order you want in Layers.

Information noteURLs that contain resource requests to external resources must have its origins allowlisted in the Content Security Policy, else the resource will not be loaded.
WMS resources must have both img-src and connect-src directives allowlisted.

See also: [Managing Content Security Policy](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)

### Before you start

The following origins must be added to the allowlist in your tenant’s Content Security Policy. This is done in the Administration activity center by an administrator.

Origins and required directives for the Content Security Policy.

| Origin | Directives |
| --- | --- |
| a.tile.openstreetmap.org | img-src |
| nowcoast.noaa.gov | connect-src, img-src |

For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

### Building the map

Do the following:

1. Add the table Cities to your application. You can copy and paste the table using manual entry.
2. In a sheet, add a map chart.
3. In Map settings, set Base map to None.
4. Add a background layer and do the following:

   - In Data, do the following:

     - For Format, select TMS.
     - For URL, enter https://a.tile.openstreetmap.org/${z}/${x}/${y}.png.
     - For Attribution, enter © OpenStreetMap contributors.
   - In Options > General, do the following:

     - Set Show legend to None.
   - In Options > Presentation, do the following:

     - Set Opacity to 0.5.
5. Add a background layer and do the following:

   - For Label, enter Weather Radar Base Reflectivity Mosaics.
   - For Format, select WMS and click WMS setup. Do the following:
     - For WMS server URL, enter https://nowcoast.noaa.gov/geoserver/observations/weather\_radar/ows.
     - For Version, select 1.3.0.
     - Click Load WMS.
     - In Step 2 (Settings), set the following settings:
       - Set CRS to EPSG:3857.
       - Turn on the Transparent setting.
       - Select all options under Weather Radar Base Reflectivity Mosaics.
     - Click Save.
   - For Attribution, enter NWS, DOD, NOAA, and nowCOAST.
6. Add a point layer and do the following:

   - In Data, add Cities as the dimension.
   - In Location, do the following:
     - Set Scope for locations to Custom.
     - Set Country to 'USA'.
   - In Colors, set Colors to Custom and set Color to f93f17.
   - In Size & Shape, set Bubble size to 9.
