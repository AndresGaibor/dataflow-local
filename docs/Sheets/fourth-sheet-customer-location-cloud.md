---
title: "The fourth sheet: Customer Location"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/fourth-sheet-customer-location-cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# The fourth sheet: Customer Location

In the fourth [sheet](#glossary-0 "Glossary term"), you will make a map that shows where customers are located, and how much they buy. Then you will add filter panes so you can filter by city, region, and customer.

You can create a map by adding point layers and area layers to display your data. You need to select a base map to provide the context for the layer data. You can add a [measure](#glossary-1 "Glossary term") value or an expression to the [dimension](#glossary-2 "Glossary term") values, and use the size of the points or color by measure to reflect the size of the measure.

Customer Location sheet when done

![Customer Location sheet when done](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CustomerLocationSheetCloud.png "Click to view full size")

## Adding filter panes

You will make filter panes in edit mode.

Do the following:

1. In the assets panel, open Master items.
2. Add the Region filter pane to the sheet.
3. Open Charts.
4. Under Visualizations, drag two filter panes to the sheet.
5. Go to Fields and add the dimension City to the first and the dimension Customer to the second filter pane.

Use the filter pane to select a subset of data after you create the [charts](#glossary-3 "Glossary term") below.

## Creating a map in edit mode

In Qlik Cloud you can create two types of maps, point maps and area maps. You can create maps that display data in point layers and area layers. The map we are using in this tutorial contains a point layer. A point layer is created using point coordinates (latitude and longitude) or location names to mark places of interest, like cities.

Do the following:

1. Resize the filter panes so they are positioned to the left, and taking up as little space as possible.
2. In the assets panel, open Charts.
3. Under Visualizations, drag a map onto the sheet.
4. In the assets panel, click ![Fields](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_outline.svg) Fields and drag the field City onto the map.
5. Select Add as new layer.
6. Select Add as point layer.

   The properties panel changes to the City point layer,
7. In Location, after Location field, select Longitude\_Latitude.
8. Go to Size & Shape. In the Size by field, type in: Sum(Sales).
9. Adjust the Bubble size range slider, if needed.

   If there is too small a minimum, then the bubble representing sales for one location may not be visible when compared to a location with a large sales volume.
10. In Colors, set Colors from Auto to Custom.
11. Select By measure in the list and in Select measure, type in: Sum(Sales).
12. Set Color scheme to Red blue gradient.
13. Click ![Back](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) by City Point layer to return to the chart properties
14. Go to Appearance > Legend. Toggle off Show legend.
15. Add the title Location to the map.
16. Click Edit sheet to stop editing.

The map size adjusts according to the [selections](#glossary-4 "Glossary term") made in the filters. For example, selecting Nordic will zoom the map to the North European area showing the locations of sales in that area.

Specific areas of the map can be selected by holding down the shift key, while using the mouse to draw a lasso around the area to be viewed. The selections in the filter panes then reflect the selection made on the map.

Selecting a specific location on the map shows the customers at that location in the filter panes. Selections in other sheets also affect the data shown in the Customer Location sheet.

This sheet is complete. In the assets panel, click Sheets and select Insights to move to that sheet.

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
