---
title: "Using relative numbers in a straight table to calculate contribution"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/table-example2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating straight tables"]
---

# Using relative numbers in a straight table to calculate contribution

This example shows how to use the relative numbers modifier to calculate contribution in a one-dimensional Straight table.

![Table created by using relative numbers to calculate financial contributions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_relnum_sn-table_5.png)

## Dataset

In this example, we will use a data file available in the Qlik Sense Tutorial - Building an App. Download and expand the tutorial. The file is available in the Tutorials source folder: Sales.xlsx

To download the file, go to [Tutorial - Building an App](/en-US/cloud-services/tutorials/Tutorial%20-%20Building%20an%20App.zip).

Add the data file to an empty application. The [dataset](#glossary-1 "Glossary term") that is loaded contains sales data.

## Measure

We use the sales volume as the [measure](#glossary-2 "Glossary term") that we create in Master items:

- Sales with the expression Sum(Sales). This is the sum of the sales volume.

## Visualization

We start by adding a filter pane to the [sheet](#glossary-3 "Glossary term") and set the following data [properties](#glossary-4 "Glossary term"):

- Dimension: Product Group.

We also add a Straight table to the sheet and set the following data properties:

- Dimension: Year (Date.Year).
- Measure: Sales; the measure that was previously created.

The following table is created, with columns showing the year, and the sum of sales for each year.

![Table with columns showing year and sum of sales](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_relnum_sn-table_1.png)

Make sure to set the Number formatting to Money, and the Format pattern to $ #,##0;-$ #,##0.

It is good practice to have the title of your [charts](#glossary-5 "Glossary term") represent their content. Additionally, consider changing the title of each column to reflect what it represents. The first column that we added is the Year, and the second column contains the Sales per year.

## Relative numbers

We could use the filter pane to select specific product groups and see their yearly sales and their total sales. That would not provide a good comparison to their contribution. Instead we will use relative numbers to get percentages as an indication of the product group contribution. By changing the parameters upon which the relative numbers calculation is based, we will get different contributions and gain more insight.

### Contribution of a year to the sales of product group

To see how much each year has contributed to the total sales of a specific product group when we make a selection, we need to add a third column:

Do the following:

1. In the properties panel, expand the Data section.
2. Click the checkbox for Sales per year.
3. Click ![Tools](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Duplicate.

To use this duplicate measure as a relative number we will apply a modifier.

Do the following:

1. In the properties panel, under Data, expand the properties for the second Sales measure.
2. Set the Modifier to Relative numbers. This will set the measure to act as a relative number.
3. Set the Modifier>Selection scope to Current selection. This sets the modifier to be calculated relative to any selection made.
4. The Modifier>Dimensional scope is set to Disregard dimension by default. This sets the modifier to be calculated relative to the total.
5. Set the Number formatting to Custom, and the Format pattern to #,##0%.
6. Change the Label to something meaningful such as Contribution to total sales of current selection.

Our table becomes as follows, with the last column showing the contribution of each year to the total sales of the selected product group.

![Table showing contributions for each year](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_relnum_sn-table_2.png)

### Contribution of a product group to total sales

To see how much each year's sales of a specific product group have contributed to the total sales of all product groups, we need to add a fourth column:

Do the following:

1. In the properties panel, expand the Data section.
2. Click the checkbox for Contribution to total sales of current selection.
3. Click ![Tools](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Duplicate.

We will apply the Relative numbers modifier again, but with different properties this time.

Do the following:

1. Set the Modifier>Selection scope to Disregard selection. This sets the modifier to be calculated disregarding any selection made.
2. The Modifier>Dimensional scope is already set to Disregard dimension. This sets the modifier to be calculated relative to the total.
3. Change the Label to something meaningful such as Contribution to total sales from all years.

The Number formatting and the Format pattern are already set, since we duplicated the previous measure.

Our table becomes as follows, with the last column showing the contribution of the selected product group to the total sales from all three years.

![Table showing contributions for all three years.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_relnum_sn-table_3.png)

Since we have not made any [selections](#glossary-6 "Glossary term") yet, the last two columns have the same values.

### Contribution of a product group to yearly sales

To see how much the sales of a specific product group have contributed to that year's sales compared to all the other product groups, we need to add a fifth column:

Do the following:

1. In the properties panel, expand the Data section.
2. Click the checkbox for Contribution to total sales from all years.
3. Click ![Tools](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Duplicate.

We will apply the Relative numbers modifier again, but with different properties this time.

Do the following:

1. The Modifier>Selection scope is already set to Disregard selection. This sets the modifier to be calculated disregarding any selection made.
2. Set the Modifier>Dimensional scope to Respect dimension. This sets the modifier to be calculated relative to each dimensional value.
3. Change the Label to something meaningful such as Contribution to sales of each year.

Our table becomes as follows, with the last column showing the contribution of the selected product group to the total sales from all three years.

![Table with the contribution of the selected product group to the total sales from all three years.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_relnum_sn-table_4.png)

Since we have not made any selections yet, the last column shows the yearly contribution of all product groups for each year.

## Making a selection

We can now start making selections to change our relative numbers to something that provides more insight.

Do the following:

1. Click Edit sheet to exit edit mode.
2. Select Canned Products from the product group filter pane.

Our table becomes as follows.

![Table created by using relative numbers to calculate financial contributions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_relnum_sn-table_5.png)

## Discovery

The table shows the relative sales for each year. By having the different contribution columns, using the relative numbers as a measure modifier, we get a better understanding of the contribution of each product group to the total sales. From the Contribution to total sales of current selection column we can see that 40% of the Canned Product sales happened in 2012, with a dramatic drop in 2014. The Contribution to total sales from all years column shows that 8% of the total sales from all three years came from the 2012 sales of Canned Product. The Contribution to sales of each year column also tells us that for 2012 the Canned Product sales contributed 21% of the sales of that year, and the same applies to the sales of 2014.
