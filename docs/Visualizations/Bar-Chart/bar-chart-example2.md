---
title: "Accumulating values over a dimension in a bar chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Bar-Chart/bar-chart-example2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating bar charts"]
---

# Accumulating values over a dimension in a bar chart

This example shows how to use a bar chart to visualize sales data which accumulate over a [dimension](#glossary-0 "Glossary term").

![Bar chart showing accumulated sales data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_bar-chart-three-dim_799x544.png)

## Dataset

In this example, we will use a data file available in the Qlik Sense Tutorial - Building an App. Download and expand the tutorial. The file is available in the Tutorials source folder: Sales.xls

To download the file, go to [Tutorial - Building an App](/en-US/cloud-services/tutorials/Tutorial%20-%20Building%20an%20App.zip).

Add the data file to an empty application. The [dataset](#glossary-2 "Glossary term") that is loaded contains sales data.

## Measure

We use the sales volume as the [measure](#glossary-3 "Glossary term") that we create in Master items:

- Sales with the expression Sum(Sales). This is the sum of the sales volume.

## Visualization

We add a bar chart to the [sheet](#glossary-4 "Glossary term") and set the following data [properties](#glossary-5 "Glossary term"):

- Dimension: Month (Date.Month).
- Measure: Sales; the measure that was previously created.

The following bar chart is created, with a bar showing the sum of sales for each month.

![ a bar showing the sum of sales for each month](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_bar-chart-one-dim_797x423.png)

## Accumulation

To have our sales data accumulate over one dimension, we need to apply a modifier to our Sales measure.

Do the following:

- Under Measure: Sales set the Modifier to Accumulation. This will set the measure to accumulate over one dimension.

Our bar chart becomes as follows, with the sales accumulating from one month to the next.

![Stacked chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_bar-chart-two-dim_762x516.png)

We want to achieve a visual separation of the periods of time, by adding the Quarter as a second dimension. The Quarter [field](#glossary-6 "Glossary term")groups the month bars into larger groups. By default, a grouped chart is selected when adding a second dimension.

Do the following:

1. Add Dimension: Quarter (Date.Quarter).
2. Under Measure: Sales set the Modifier>Dimension to Month. This sets the dimension over which the accumulation will take place.

If Across all dimensions is turned on, the accumulation continues across all quarters.

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_bar-chart-four-dim_802x547.png)

Notice how the bars of the previous two bar charts are the same.

If Across all dimensions is turned off, the accumulation starts again at the beginning of each quarter. Our bar chart becomes as follows, with the sales accumulating from one month to the next, inside each quarter.

![bar chart with sales accumulating from one month to the next, inside each quarter](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_bar-chart-three-dim_799x544.png)

It is good practice to have the title of your charts represent their content. So consider changing the title of your new bar chart to reflect that the bars are now an accumulation of sales.

## Discovery

The bar chart visualizes the sales volume of each month, grouped into quarters. By having the sales accumulate inside each quarter, we get a better understanding of the volume of sales for each quarter. You can hover the mouse pointer over a month and view the details.

In the bar chart we can see that Q1 has the highest sales volume. We can also see that even though Q4 had the lowest sales volume, the first two months of the quarter were better than the ones from Q3.
