---
title: "Example: Building a sheet"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/example-sheet.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with sheets"]
---

# Example: Building a sheet

This example shows you how to quickly build a sheet. If you want to follow along to replicate the example, the base application and data used are available from the business logic tutorial. For the business logic tutorial, see [*Tutorial – Customizing how Insight Advisor interprets data*](../BusinessLogic/Tutorial/tutorial-customizing-insight-advisor.htm).

The [sheet](#glossary-0 "Glossary term") edit mode allows you to quickly develop useful [visualizations](#glossary-1 "Glossary term"). When you create a sheet, you should have an idea of the kinds of information you want to see. In this case, from the Tutorial - Business logic application we want to create a sheet that lets us exploration sales by different points of time. This sheet should let us see:

- A geographic representation of sales by country and city.
- Gross profits by sales office.
- Employee sales figures.
- The breakdown of specific products and categories.
- A filter so users can filter data by year, quarter, month, and week.

Example sheet

![An image of the completed sheet, with a top row containing a bar chart, map, and filter pane, and a bottom row containing a table and tree map.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-example-rev.png "Click to view full size")

## Creating the first visualization

For the first visualization, we will make a bar chart.

Do the following:

1. In the  Tutorial - Business logic application, create a new sheet.

   Information note

   The sheet templates picker might open when you create a new sheet. Sheet templates are not used for this example, so you can close the window or click Create without template.

   To learn more about how you can use sheet templates, see [*Building sheets using templates*](sheet-templates.htm).
2. In Assets, open Charts.
3. Under Visualizations, drag and drop a bar chart into the sheet.
4. From Assets, in Fields, drag and drop SalesOffice on the bar chart and select Add "SalesOffice".
5. From Assets, in Fields, drag and drop Gross Profit on the bar chart and select Add as measure > Sum([Gross Profit]).
6. In the properties panel, click Sorting.
7. Drag Sum([Gross Profit]) to the top of the sorting list.
8. Click Appearance > Presentation.
9. Select Horizontal.
10. In the properties panel, click Appearance > Colors and legend.
11. Under Colors, select to Custom.
12. Select By dimension.

    First visualization

    ![Completed bar chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-example1rev.png "Click to view full size")

## Adding a map

With the bar chart made, we can next make a map that visualizes both countries and cities.

Do the following:

1. In Assets, open Charts.
2. Under Visualizations, drag and drop a map into the sheet.
3. In the properties panel, click Layers > Add layer.
4. Select Area layer.
5. Under Dimensions, click Add and a select Country.
6. Under Colors, select Custom, select By measure, and color by Avg(Sales).
7. Click ![Back](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) to return to Layers.
8. Click Add layer and select Point layer.
9. Under Dimensions, click Add and select City.
10. Under Colors, select Custom, select By measure, and color by Sum(Sales).
11. Under Color scheme, select Diverging classes.

    Sheet with map

    ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-example3rev2.png "Click to view full size")

## Adding a filter pane and rearranging the row

Next, we will add a filter pane so we can explore the data in our visualizations by specific periods of time. We will also rearrange our row of visualizations.

Do the following:

1. In Assets, open Charts.
2. Under Visualizations, drag and drop a filter pane to the right of the map.
3. Click Add dimension > click OrderDate > Year.
4. Click OrderDate.autoCalendar.Year and under Title, enter Year.
5. In the properties panel, click Add field > OrderDate > Quarter.
6. Click OrderDate.autoCalendar.Quarter and under Title, enter Quarter.
7. Click Add field > OrderDate > Month.
8. Click OrderDate.autoCalendar.Month and under Title, enter Month.
9. Click Add field > OrderDate > Week.
10. Click OrderDate.autoCalendar.Week and under Title, enter Week.
11. Click and drag the borders of the map and filter pane to resize them.

    Adding a filter pane

    ![Sheet with resized map and filter pane.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-example3rev3.png "Click to view full size")

## Adding a new row with a table

We will add a new row of visualizations beneath the current row, starting with a table.

Filtered table

![The sheet, with completed table.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-example4rev2.png "Click to view full size")

Do the following:

1. In Assets, open Charts.
2. Under Visualizations, drag and drop a Straight table into the sheet.
3. Click Add columns > Fields & master items.
4. Under Dimensions, select EmployeeName.
5. From Assets, drag and drop SalesOffice onto the table and select Add "SalesOffice".
6. From Assets, drag and drop Sales onto the table and select Add as measure > Avg(Sales).
7. Select Avg(Sales) and under Number formatting, select Money.
8. Under Format pattern, enter $ #,##0.00;-$ #,##0.00.
9. From Assets, drag and drop Sales onto the table and select Add as measure > Sum(Sales).
10. Select Sum Sales and under Number formatting, select Money.
11. Under Number formatting, select Money.
12. Under Format pattern, enter $ #,##0.00;-$ #,##0.00.
13. In the properties panel, in Data, under Filters, click ![Open Add data asset menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) > Fields.
14. In the properties panel, in Data, under Filters, click ![Open Add data asset menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) > Fields.
15. Select Sales and click Add.
16. Click the new filter to expand its properties.
17. Select Condition as the filter type.
18. Select Compare.
19. Under condition, select > and Fixed value.
20. Under Greater than, enter 0.

## Adding a treemap

Now, we will add a treemap, so we can explore both our product categories but also the products within those categories.

New treemap

![The completed sheet, with treemap](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-example5rev.png "Click to view full size")

Do the following:

1. In Assets, open Charts.
2. Under Visualizations, drag and drop a treemap into the sheet.
3. In the properties panel, in Data, under Dimensions click Add > CategoryName.
4. Click Add > ProductName
5. Under Measures, click Add as measure  > Sum([Gross Profit]).
6. Click and drag the on the borders of the table and treemap.
