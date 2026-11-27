---
title: "The first sheet: Dashboard"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/first-sheet-dashboard-cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# The first sheet: Dashboard

In this first [sheet](#glossary-0 "Glossary term"), you will make a dashboard with different [visualizations](#glossary-1 "Glossary term").

## Overview

Open the Dashboard sheet you created earlier. Right now the sheet is empty, but it will not be for long.

### Edit mode

Going from left to right, edit mode has the following layout:

1. Assets
2. Sheet area
3. Properties

Dashboard sheet with no visualizations in edit mode

![A sheet without charts in edit mode.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen-tutorial-sheet_nocharts.png "Click to view full size")

### Fields, dimensions, and measures

Visualizations are built using fields, dimensions, and measures.

#### Field

A field is a data asset containing values, loaded from a data source. At a basic level, a field corresponds to a column in a table. Fields are used to create dimensions and measures in visualizations.

For more information, see [*Fields*](../DataSource/fields.htm).

#### Dimension

A dimension is an entity used to categorize data in a chart. For example, the slices in a pie chart or the bars of a bar chart represent individual values in a dimension. Dimensions are often a single field with discrete values, but can also be calculated in an expression.

For more information, see [*Data grouping with dimensions*](../Dimensions/dimensions.htm).

#### Measure

A measure is a calculation based on one or more aggregations. For example, the sum of sales is a single [aggregation](#glossary-2 "Glossary term") while the sum of sales divided by the count of customers is a measure based on two aggregations.

For more information, see [*Measures*](../Measures/measures.htm).

### Master items

A master item is a reusable dimension, measure, or visualization that you define once and can add to multiple visualizations and sheets across your app. Using master items ensures consistency in how fields are used and values are calculated and makes it easier to update shared assets in one place when requirements change.

## Purpose of this sheet

The purpose of a dashboard is to give a quick overview of the current state of affairs. The focus here is on sales trends and figures. The dashboard is not primarily designed for data exploration, but you can make [selections](#glossary-3 "Glossary term") and analyze the results.

Dashboard sheet when finished

![Dashboard sheet when tutorial is finished](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_DashboardSheetCloud.png "Click to view full size")

## Adding the donut chart

The first visualization that you will create is a Sales per Region donut chart. Pie charts and donut charts display the relation between values as well as the relation of a single value to the total. You can use a pie chart when you have a single data series with only positive values. You should use a donut chart when you have a single data series that includes negative values.

You will create this using chart suggestions. Chart suggestions allows you to create charts by dragging fields or master items onto the sheet and then the application suggests an appropriate chart. Once you have the chart you want, you can turn off chart suggestions to customize the visualization. To learn more information about chart suggestions, see [*Creating visualizations using Insight Advisor chart suggestions*](../Visualizations/creating-visualization-assistance.htm).

As a part of creating the donut chart, you will create a master measure, Sales, that will calculate the sum of the field Sales. The master measure Sales will be used in a number of other visualizations in this tutorial.

For more information, see [*Pie chart and donut chart*](../Visualizations/PieChart/pie-chart.htm).

Do the following:

1. In the assets panel, click Fields and right-click on Sales and select Create measure.
2. In the Create new measure dialog, under Expression, enter Sum(Sales).
3. Click Create.

   The measure is added as a master item.
4. In the assets panel, click Master items, and drag Sales to the sheet and drop it onto the sheet.
5. In the assets panel, click Fields and drag the Region field to the sheet and drop it onto the suggested chart.
6. Select the chart and in the properties panel, click Auto and select Pie chart.
7. Turn off Chart suggestions.
8. Under Appearance > General, select Show titles and add the title: Sales per Region.
9. Under Appearance > Presentation, select Donut.
10. Under Appearance > Colors and legend, turn off Auto.
11. Under Custom, click the drop-down and select By measure.

The donut chart is complete. The colors in the donut chart are set by measure, which means the higher the value, the darker the color.

You have many options when it comes to coloring the values. Remember that the colors should serve a purpose and not be used only to make the visualization more colorful.

## Adding the KPI chart

The second visualization is the Total Sales and Margin KPI chart. A KPI visualization can show one or two measure values, and is used to track performance. Color coding and symbols indicate how the figures relate to the expected results. This KPI will use conditional coloring to change the colors depending on the displayed values in the measures.

For more information, see [*KPI*](../Visualizations/KPI/KPI.htm).

Do the following:

1. In the assets panel, click Charts.
2. Under Visualizations, drag and drop a KPI onto the sheet to the right of the donut chart.
3. Click Add measure > Sales.

   The sum of sales is added to the KPI.
4. In the assets panel, click Master items and after Measures, click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
5. Under Expression, enter Sum(Margin).
6. Enter the name Margin and click Create.
7. In Master items, drag and drop Margin onto the KPI and select Add Margin.
8. Under Appearance > Color, making sure First is selected, turn on Conditional colors and turn off Library colors.
9. Click Add limit.
10. Under Value, select the left side and then select a shade of red from the color palette.
11. Under Value, select the right side and then select a shade of green from the color palette.
12. Drag the value limit to the left to display the sales value as red in the KPI.
13. Select Second and turn on Conditional colors and turn off Library colors.
14. Click Add limit.
15. Under Value, select the left side and then select a shade of red from the color palette.
16. Under Value, select the right side and then select a shade of green from the color palette.
17. Drag the value limit to the right to display the margin value as green in the KPI.
18. Under Appearance > General, turn on Show titles and add the title: Total Sales and Margin.

## Adding the gauge chart

The third visualization we want to create is the Profit Margin gauge chart. A gauge is used to visualize a single measure. A gauge is easy to read and understand and gives an instant indication of the performance within an area.

For more information, see [*Gauge*](../Visualizations/Gauge/gauge.htm) .

This time, we are going to add an expression to calculate the profit margin.

Do the following:

1. In the assets panel, click Charts.
2. Under Visualizations, drag and drop a Gauge onto the sheet to the right of the KPI.
3. Click Add measure. Click on ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg).

   The expression editor opens.
4. Enter:

   ```
   (sum(Sales) - sum(Cost)) / Sum (Sales)
   ```
5. Click Apply.
6. Under Presentation > Range limits, set the minimum value to -0.5 and the max value to 0.5.
7. Select the Bar option.
8. Toggle on Use segments and toggle off Use library.
9. Click the Add Limit button. Enter  0.12 in the field.
10. Click the Value bar. Select red for the values below the limit, and green for the values above the limit
11. Select Data. Click on the expression to see more options. Under Number formatting select Number from the drop-down menu. Under Simple, select 12%.

    This will display a percentage without decimals.
12. Select Appearance > Measure axis. In the Labels and title drop-down menu, select Labels only.
13. Click the chart and add a title: Profit Margin.

## Adding the bar chart

The next visualization is a bar chart showing the Top 5 Customers. A bar chart is suitable for comparing multiple values. The dimension axis shows the category items that are compared, and the measure axis shows the value for each category item. Grouping and stacking bars makes it easy to visualize grouped data.

For more information, see [*Bar chart*](../Visualizations/Bar-Chart/bar-chart.htm).

Do the following:

1. In the assets panel, click Charts.
2. Under Visualizations, add a bar chart below the donut chart.
3. Under Fields, drag and drop Customer on the chart and add it as the dimension.
4. Under Master items, drag and drop Sales on the chart and add it as the measure.
5. In the properties panel for the bar chart, under Appearance > Presentation, select Horizontal.
6. Under Data, click the Customer dimension.
7. In the Limitation drop-down menu, select Fixed number. In the expression field, type in: 5.

   The chart will only show the top 5 customers.
8. Clear the Show others check box.
9. Click Click to add title on the chart and add Top 5 Customers.

The bar chart is complete, showing the top five customers. When you make selections in other visualizations, these customers will change, accordingly.

If you had not cleared the selection Show others, the fifth bar would have been gray, summarizing all the sales values where the company name is missing. This value can be useful to get an understanding of how much of the sales that cannot be referred to a specific company.

## Adding the line chart

The fifth visualization is the Quarterly Trend line chart. A line chart is used to show trends over time. The dimension is always on the x-axis, and the measures are always on the y-axis.

For more information, see [*Line chart*](../Visualizations/LineChart/line-chart.htm).

This line chart will be used to show the quarterly sales trend for the years 2024-2026. The figures for 2026 are for the first half of the year.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag and drop a line chart next to the bar chart.
3. Under Fields, select Date >Derived fields, and add Quarter and Year as dimensions.
4. Under Master items, add Sales as a measure.
5. In the properties panel, under Data, update the labels for Date.autoCalendar.Quarter and Date.autoCalendar.Year to Quarter and Year .
6. Under Appearance > Presentation, select Show data points.
7. Click Click to add title on the chart and add Quarterly Trend.

## Adding the combo chart

The last visualization we want to create here is the Sales Trend combo chart. The combo chart combines a bar chart and a line chart and is useful when you want to combine values that are normally hard to combine because of their different scales. A typical example is when you have a bar chart with sales figures and want to combine these figures with the margin values (in percent).

For more information, see [*Combo chart*](../Visualizations/ComboChart/combo-chart.htm).

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, add a combo chart to the sheet, placing it below the line chart.
3. Under Master items, add Sales as a bar measure.
4. Add Margin as a line measure.
5. Under Fields, click Date > Derived fields. Add YearMonth as a dimension.
6. Update the label for Date.autoCalendar.YearMonth to YearMonth.
7. In the properties panel, under Appearance > Colors and legend, toggle off Show legend.
8. Under X-axis, toggle off Continuous and clear the Use continuous scale check box.
9. Under Sorting, drag YearMonth to the top of the sort order.
10. Click the chart and add a title: Sales Trend.

## Adding the filter panes

The purpose of the filter panes is to filter out a limited data set,
which you can analyze and explore.

For more information, see [*Filter pane*](../Visualizations/FilterPane/filter-pane.htm).

Do the following:

1. In the assets panel to the left, click ![Sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_object.svg) to open Charts.
2. Under Visualizations, drag a filter pane onto the sheet.
3. In the assets panel, click ![Fields ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_outline.svg) to open Fields.
4. Click Date in the list to expand it.
5. Drag the field Year to the center of the filter pane, then click it in the properties panel on the right-hand side to expand the dimension and change its Title to Year.
6. Drag the field Quarter to the filter pane, then click it in the properties panel and change its Title to Quarter.
7. Drag the field Month to the filter pane, then click it in the properties panel and change its Title to Month.
8. Drag the field Week to the filter pane, then click it in the properties panel and change its Title to Week.
9. You can use the handles to resize the filter pane.
10. Right-click each filter pane and select Add to master items.
11. Type the name Period and click Add.

You have created a filter pane and saved it as a [master item](#glossary-4 "Glossary term"). This makes it easy to reuse in other sheets.

The second filter pane only contains one dimension, Region.

Do the following:

1. In the assets panel to the left, click ![Sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_object.svg) to open Charts.
2. Under Visualizations, drag a filter pane onto the sheet.
3. Click Add dimension and scroll down and select the field Region.
4. You can use the handles to resize the filter pane.
5. Right-click the filter pane and select Add to master items.
6. Type the name Region and click Add.

The two filter panes are complete.

Feel free to adjust the positioning and size of the visualizations in your sheet.

Dashboard sheet after customizing

![Dashboard sheet after customizing](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_DashboardSheetEdit_AfterCustomizingCloud.png "Click to view full size")

You have completed the first sheet. In the assets panel, click Sheets and select Product Details to move to that sheet.

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
