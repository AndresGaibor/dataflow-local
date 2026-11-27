---
title: "Correlating two measures with a scatter plot to find outliers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/ScatterPlot/scatter-plot-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating scatter plots"]
---

# Correlating two measures with a scatter plot to find outliers

This example shows how to make a scatter plot to correlate two [measures](#glossary-0 "Glossary term"). We want to compare how the average sales volume correlates with the average margin for a group of sales persons, and find the outliers.

![Scatter plot showing two measures](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_scatter-plot.png)

## Dataset

In this example, we'll use two data files available in the Qlik Sense Tutorial - Building an App. Download and expand the tutorial, and the files are available in the Tutorials source folder:

- Sales.xls
- Sales rep.csv

To download the files, go to [Tutorial - Building an App](/en-US/cloud-services/tutorials/Tutorial%20-%20Building%20an%20App.zip).

Add the two data files to an empty application and make sure that they are associated by Sales Rep ID - Sales Rep Number.

The [dataset](#glossary-2 "Glossary term") that is loaded contains sales data. The Sales rep table holds the information about the sales persons.

## Measures

We need two measures that we create in Master items:

- AverageSales with the expression Avg(Sales). This is the average of the sales value for all orders.
- AverageMargin with the expression Avg(Margin/Sales). This is the average of the sales margin for all orders.

## Visualization

We add a scatter plot to the [sheet](#glossary-3 "Glossary term") and set the following data [properties](#glossary-4 "Glossary term").

- Dimensions > Bubble: Sales Rep Name (sales person)
- Measures > X-axis: AverageSales
- Measures > Y-axis: AverageMargin

A scatter plot is created, with a bubble for each sales person.

But we also want to have information about the total sales for each sales person, by adding the third [measure](#glossary-5 "Glossary term") Avg(Sales). The size of each bubble reflects the total sales for each sales person.

![Scatterplot showing two measures](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_scatter-plot.png)

## Discovery

The scatter plot visualizes the average sales versus average margin for each sales person, and we can see which sales persons distinguish themselves in performance. You can hover the mouse pointer over a sales person and view the details.

In the [chart](#glossary-6 "Glossary term"), we can see that Lee Chin has the highest average sale value. Stewart Wind has the largest total sales volume, followed by Judy Thurman. Cheryle Sincock has a significantly smaller average margin than other sales persons, while outperforming most of them in average sales volume.
