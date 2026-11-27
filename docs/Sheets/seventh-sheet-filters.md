---
title: "The seventh sheet: Filters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/seventh-sheet-filters.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# The seventh sheet: Filters

In the seventh [sheet](#glossary-0 "Glossary term") you will add filters to limit the data used in a [visualization](#glossary-1 "Glossary term") to a specific subset of that data.

Filters sheet when finished

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-seventh-sheet-rev.png "Click to view full size")

You can filter by:

- Values: Filter using selected values from a [field](#glossary-2 "Glossary term"). For example, filter results to only include those values you select from a field.
- Searches: Filter using matches from a search. For example, filter results to only include those that start with a specific code prefix.
- Condition: Filter matching specified conditions. For example, filter results to only include those that meet a numeric threshold.
- Clear selection: Filter to exclude [selections](#glossary-3 "Glossary term") made in other [visualizations](#glossary-4 "Glossary term") from this visualization for the chosen field.

For this sheet, you will create four visualizations and apply a filter to each one. Create a new sheet and name it Filters.

## Filtering by values

For your first filtered visualization, you will create a donut chart that shows sales by city and filter it by the value Nordic from the field Region.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, select a pie chart and drag it to the sheet.
3. In the properties panel, under Appearance > Presentation select the ![Donut chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pie_chart_donut_outline.svg) Donut.
4. In the assets panel, open Fields and drag and drop the field City onto the chart and add it as a dimension.
5. Open Master items and drag and drop the measure Sales onto the chart.
6. In the properties panel, under Filters, click Add and select the field Region.
7. Click Region under Filters and select Values.
8. Select Nordic.
9. Click the ![Donut chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) at the top of the donut chart and enter Sales by city (Nordic) as the title.

## Filtering by search

For the next visualization, you will make a KPI chart and filter it to display only the sales results for juice.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, select the ![KPI](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_kpi_outline.svg) KPI and place it to the right of Sales by city (Nordic).
3. In Master items, drag and drop the measure Sales onto the chart.
4. In the properties panel, under Filters, click Add and select Product Sub Group.
5. Click Product Sub Group under Filters and select Search.
6. Select Matches exactly.
7. Enter Juice.
8. Under Appearance > General, turn on Show titles and add the title Sales (Juice).

## Filtering by condition

Next, you will create a vertical grouped bar chart and filter it so it only includes sales values greater than 40,000.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a bar chart to the sheet, placing it beneath the donut chart.
3. Under Data, click Add under Dimensions and select the field Product Type.
4. Click Add under Measures and select the master measure Sales.
5. Under Filters, click Add and select the field Sales.
6. Click Sales under Filters.
7. Select Condition.
8. Select Compare.
9. Under Greater than, enter 40000.
10. Click the ![Donut chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) icon on the bar chart and enter Sum of sales greater than 40K by product as the title.

## Filtering by clearing the selection

Finally, you will create a donut chart and add a clear selection filter so that selections in other [charts](#glossary-5 "Glossary term") from Region do not impact this chart.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag a pie chart to the sheet, placing it to the right of Sum of sales greater than 40K by product.
3. In the properties panel, under Appearance > Presentation, select the ![Donut chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pie_chart_donut_outline.svg) Donut.
4. In the assets panel, go to Fields and drag and drop the field Region onto the chart as a dimension.
5. In Master items, drag and drop the measure Sales onto the chart.
6. Under Filters, click Add and select the field Region.
7. Click Region under Filters.
8. Select Clear selection.
9. Click the ![Donut chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) icon at the top of the donut chart and enter Sales by region as the title.

You can now make selection in Region in other charts without changing this chart. Selections made in this chart impact other charts, however.

You are done making visualizations. Now you will complement your application with data storytelling.

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
