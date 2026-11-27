---
title: "Comparing categories against a measure with a bar chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Bar-Chart/bar-chart-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating bar charts"]
---

# Comparing categories against a measure with a bar chart

This example shows how to make a bar chart to visualize sales data and how to compare different product groups against the same [measure](#glossary-0 "Glossary term").

![Stacked chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_bar-chart-two-dim.png)

## Dataset

In this example, we'll use two data files available in the Qlik Sense Tutorial - Building an App. Download and expand the tutorial, and the files are available in the Tutorials source folder:

- Sales.xls
- Item master.xls

To download the files, go to [Tutorial - Building an App](/en-US/cloud-services/tutorials/Tutorial%20-%20Building%20an%20App.zip).

Add the two data files to an empty application and make sure that they are associated by Item Number.

The [dataset](#glossary-2 "Glossary term") that is loaded contains sales data. The Item master table holds the information about the items ordered, such as product groups.

## Measure

We use the sales volume as the measure, by creating a measure in Master items with the name Sales, and the expression Sum(Sales).

## Visualization

We add a bar chart to the [sheet](#glossary-3 "Glossary term") and set the following data [properties](#glossary-4 "Glossary term"):

- Dimension: Product Group (product group).
- Measure: Sales; the measure that was created as a master item.

The following bar chart is created, with a bar showing the sales for each product group:

![Bar chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_bar-chart-one-dim.png)

But we want to have some more detailed information about the product sales, by adding the Product Sub Group as a [dimension](#glossary-5 "Glossary term"). The Product Sub Group [field](#glossary-6 "Glossary term") divides the product groups into sub groups. By default, a grouped chart is selected when adding the second dimension. We want to display a stacked chart instead, that is changed under Appearances in the properties panel.

![Stacked chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_bar-chart-two-dim.png)

## Discovery

The bar chart visualizes the sales volume of different product groups, divided into product sub groups. The [visualization](#glossary-7 "Glossary term") is sorted in order of sales volume per product. You can hover the mouse pointer over a product sub group and view the details.

In the bar chart we can see that Produce has the highest sales volume. One of the sub products contribute to most of the Produce sales, if we hover over that part of the bar we can see it is Fresh Vegetables.
