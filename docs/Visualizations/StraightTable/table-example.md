---
title: "Accumulating values over a dimension in a straight table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/table-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating straight tables"]
---

# Accumulating values over a dimension in a straight table

This example shows how to use a straight table to compare data which accumulate over a [dimension](#glossary-0 "Glossary term").

![Straight table comparing data accumulated over a dimension](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_sn_table-3.png)

## Dataset

In this example, we will use a data file available in the Qlik Sense Tutorial - Building an App. Download and expand the tutorial. The file is available in the Tutorials source folder: Sales.xlsx

To download the file, go to [Tutorial - Building an App](/en-US/cloud-services/tutorials/Tutorial%20-%20Building%20an%20App.zip).

Add the data file to an empty application. The [dataset](#glossary-2 "Glossary term") that is loaded contains sales data.

## Measure

We use the sales volume as the [measure](#glossary-3 "Glossary term") that we create in Master items:

- Sales with the expression Sum(Sales). This is the sum of the sales volume.

## Visualization

We add a Straight table to the [sheet](#glossary-4 "Glossary term") and set the following data [properties](#glossary-5 "Glossary term"):

- Dimension: Year (Date.Year).
- Dimension: Month (Date.Month).
- Measure: Sales; the measure that was previously created.

The following table is created, with columns showing the year, the month, and the sum of sales for each month.

![Table showing the year, the month, and the sum of sales for each month](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_sn_table-1.png)

Make sure to set the Sorting with Year > Month > Sales.

## Accumulation

To have our sales data accumulate over one dimension, we need to set an additional data property:

- Measure: Sales; the measure that was previously created.

We add this measure twice to reuse it for accumulation. To do this we need to apply a modifier to our Sales measure.

Do the following:

1. In the properties panel, under Data, expand the properties for the second Sales measure.
2. Set the Modifier to Accumulation. This will set the measure to accumulate over one dimension.
3. Set the Modifier>Dimension to Month. This sets the dimension over which the accumulation will take place.
4. Make sure Across all dimensions is turned off. We want the accumulation to restart at the beginning of each year.
5. Under Totals function, select None.

Information noteIn Accumulation there is the option to select Show excluded values. When turned on, your [visualization](#glossary-6 "Glossary term") includes any dimensional values that do not have data. This ensures that all values, including months with no sales data, are counted in the accumulation.

Our table becomes as follows, with the last column showing sales accumulating from one month to the next, for each year.

![table with sales accumulating from one month to the next, for each year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_sn_table-2.png)

It is good practice to have the title of your [charts](#glossary-7 "Glossary term") represent their content. So consider changing the titles of the columns of your table to reflect that the last column contains an accumulation of sales.

Our data for the year 2014 is insufficient as it stops at June. In order to achieve a better comparison between the accumulated sales of all three years we will choose a more appropriate range of months, from January to June.

Do the following:

1. Click Edit sheet to exit edit mode.
2. Select all months from January to June and confirm your selection.

Our table becomes as follows, with the sales accumulating from January to June, inside each year.

![Straight table comparing data accumulated over a dimension](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_acc_sn_table-3.png)

## Discovery

The table shows the sales volume of each month, grouped into years. By having the sales accumulate inside each year, we get a better understanding of the volume of sales for each year. We have made a selection of the months from January to June, to compare the same range of months between the three years. In the last column of the table we can see that the accumulated sales for 2014 so far have been higher than the accumulated sales for 2012, but not as high as the ones for 2013.
