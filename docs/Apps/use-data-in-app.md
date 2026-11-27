---
title: "Using data in an application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/use-data-in-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Using data in an application

To finish off this tutorial, it is time for you to put your loaded data into a [visualization](#glossary-0 "Glossary term") in your application.

## Adding a chart

Now that your data is loaded, you can create some [charts](#glossary-2 "Glossary term") with the data. Charts are often also called visualizations. It is not until you have also added the required [dimensions](#glossary-3 "Glossary term") and [measures](#glossary-4 "Glossary term") that a [chart](#glossary-5 "Glossary term") is complete. You will start by adding the charts and then continue by adding dimensions and measures.

Do the following:

1. Create a new sheet in your Scripting Tutorial application.
2. In the properties panel, give the sheet the title Product sales.
3. Drag a filter pane from the Charts tab to the sheet and use the handles to resize it so that it is 3 cells wide and 4 cells tall. Place it in the top left corner of the sheet.
4. Drag a bar chart to the top right corner, make it 5 cells tall and wide enough to stretch until the side of the sheet.
5. Drag a line chart to the remaining space.

The icons on the [sheet](#glossary-6 "Glossary term") show what sort of chart you have added. Now you can add dimensions and measures to your charts to complete them as visualizations.

Application sheet with empty charts

![Application sheet with empty charts](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_add-app-charts_saas_rev2.png "Click to view full size")

## Adding dimensions and measures

The next step is to add dimensions and measures. Begin by adding time dimensions to the top left filter pane. The benefit of a filter pane is that you save space. Instead of having one filter pane each for Year, Quarter, Month, and Week, you will use only one filter pane for the same purpose.

### Creating and adding dimensions

Do the following:

1. In the assets panel, click ![Repository](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_outline.svg) Fields. Here you find all the fields in all the tables that you have loaded in the data load editor.
2. Scroll down to the bottom of the list, and click the field Year. Drag it to the center of the top left filter pane.
3. In the same way, add Quarter, Month and Week to the filter pane.

You have now created a filter pane with four dimensions: Year, Quarter, Month, and Week.

### Creating and adding measures

Most visualizations need both dimensions and measures. A measure is the result of an [aggregation](#glossary-7 "Glossary term") expression, which is, in many cases, a common function, such as Sum, Max, Min, Avg (average), or Count.

In the bar chart you will show the sales by region.

Do the following:

1. In Fields, click the field Region and drag it to the center of the bar chart area.
2. Click Add "Region".
3. Click the field Sales and drag it to the center of the bar chart area.
4. Click Add as measure > Sum(Sales).
5. In the properties panel on the right-hand side, click Appearance and then Presentation. Select Horizontal.

   The bars are now displayed horizontally.
6. In the properties panel on the right-hand side, click Sorting.

   The sorting order is displayed.
7. Drag Sum([Sales]) above Region so that the dimensions are sorted by Sum([Sales]) (measure value) instead of Region (dimension value, alphabetically).

The bar chart is complete, showing the sales results for the different regions. This is a basic bar chart. There are many options to enhance it in the properties panel (to the right). Just to show you one of the possibilities, let us use the title area for something more than just a title.

8. Paste the following into the title field of the bar chart:

```
='Total sales: $'& Round(Sum(Sales)/1000000, 0.1) & 'M'
```

9. Press Enter.

The final visualization on this sheet is a line chart.

Do the following:

1. In Fields, click the field Month and drag it to the center of the line chart area.
2. Click Add "Month".
3. Click the field Year and drag it to the center of the line chart area.
4. Click Add "Year".
5. Click the field Margin and drag it to the center of the line chart area.
6. Click Add as measure > Sum(Margin).
7. Add the title Profit margin on top of the line chart.

Charts with data

![Completed charts in the sheet with data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_app-edit-rev2.png "Click to view full size")8. Stop editing the sheet.

The sheet is now complete and you can begin to click around and interact with the contents of the sheet.

Completed sheet

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/SenseTutorials/tutorial_app-done-rev.png "Click to view full size")

Because we limited the amount of monthly sales data in our original Sales.xlsx file, there is little data available for our chart after the end of March for each year. You can make [selections](#glossary-8 "Glossary term") in your filter pane so that you are only comparing the first three months of each year.

9. Click the Month field in the filter box, and then select Jan, Feb, and Mar.

Filter box

![Filter box.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-app-filter-pane.png "Click to view full size")10. Close the filter pane. The Profit margin chart shows the data for the first three months of each year.

Profit margin chart updated based on selections

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/SenseTutorials/tutorial-app_done_filter_data-rev.png "Click to view full size")

## Thank you!

Now you have finished this tutorial, and hopefully you have gained some basic knowledge about scripting in applications. Please visit our website for more inspiration for your applications.
