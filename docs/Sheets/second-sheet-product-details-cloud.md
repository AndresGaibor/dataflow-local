---
title: "The second sheet: Product Details"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/second-sheet-product-details-cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# The second sheet: Product Details

In the second [sheet](#glossary-0 "Glossary term") you will make a bar chart and treemap that focus on products. Then you will add filter panes so you can filter by date and region.

Product Details sheet when finished

![Product Details sheet when finished.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ProductDetailsCloud.png "Click to view full size")

You will complete all work in editing mode.

## Adding the bar chart

The next visualization is a bar chart showing the Top Sales. You will add an expression to the chart title so that it will include the total sales.

Tip note

The order you add fields and master items can determine the sort order in the visualization. In this visualization, you want it ordered by Sales, then Margin, and then Product Group.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a bar chart to the sheet.
3. Go to Master items and add Sales  as a [measure](#glossary-1 "Glossary term") to the chart.
4. Add Margin as a measure to the chart.
5. Go to Fields and add Product Group as the dimension to the chart.
6. In the properties panel, under Appearance > Presentation >turn on Values labels.
7. Go to Appearance > General. Find Title, and click on ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg).

   The expression editor opens.
8. This expression will resolve to show total sales:

   ```
   ='Total Sales: $'& Round(Sum(Sales)/1000000, 0.1) & 'M'
   ```
9. Click Apply.

## Adding the treemap

Treemaps display hierarchical data by using nested rectangles. Use a treemap when space is constrained and you have a large amount of hierarchical data that you need to get an overview of. Treemaps should primarily be used with values that can be aggregated.

For more information, see [*Treemap*](../Visualizations/TreeMap/treemap.htm).

In this treemap you will create a product hierarchy.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a treemap to the area below the bar chart.
3. Go to Fields and add Product Group, Product Type, and Item Desc as dimensions to the treemap.
4. Go to Master items and add Sales as a measure. The treemap will be created.
5. Click Click to add title on the chart and add the title: Product Treemap.
6. Under Appearance > Colors and legend, set Colors from Auto to Custom.
7. Select By measure in the list.
8. Select the master measure Sales.

## Adding the filter panes

The purpose of the filter panes is to filter out a limited data set,
which you can analyze and explore.

For more information, see [*Filter pane*](../Visualizations/FilterPane/filter-pane.htm).

You will now reuse the Period filter pane and the Region filter pane that you saved as master items.

Do the following:

1. Resize the bar chart and treemap so that there is space on the left for two filter panes.
2. In the assets panel, click ![Linked Object](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) to open Master items.
3. Click Visualizations.
4. Drag the filter pane Period to the sheet and resize it.
5. Drag the filter pane Region to the area below Period and resize it.

This sheet is complete. In the assets panel, click Sheets and select Customer Details to move to that sheet.

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
