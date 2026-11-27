---
title: "Displaying different charts based on selections with a tab container"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Container/container-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating tab containers"]
---

# Displaying different charts based on selections with a tab container

This example shows how to display different [chart](#glossary-0 "Glossary term") content based on user [selections](#glossary-1 "Glossary term") using a tab container.

- When a single product group is selected a chart for product sub groups is displayed.
- When more than one product group is selected a chart for product groups is displayed.

## Dataset

In this example, we will use two data files from the Qlik Sense Tutorial - Building an App. To download the files, go to [Tutorial - Building an App](/en-US/cloud-services/tutorials/Tutorial%20-%20Building%20an%20App.zip). Download and unzip the tutorial, and find the files in the Tutorials source folder:

- Sales.xls
- Item master.xls

Create a new application and add the two data files. Make sure that they are associated by Item Number.

The [dataset](#glossary-3 "Glossary term") that is loaded contains sales data. The Item master table holds the information about the items ordered, such as product groups.

## Measures

We need to create two [measures](#glossary-4 "Glossary term") in Master items:

- Sales volume: with the name Sales, and the expression Sum(Sales).
- Sales margin in percent: with the name Margin %, and the expression Avg(Margin/Sales)\*100.

## Visualizations

We need two different master [visualizations](#glossary-5 "Glossary term") based on product group selections. One of them with product group as [dimension](#glossary-6 "Glossary term"), the other with product sub group as dimension.

### Product group visualization

This is the visualization we want to show when more than one product group is selected.

We add a combo chart to the [sheet](#glossary-7 "Glossary term") and set the following data [properties](#glossary-8 "Glossary term"):

- Dimension: Product Group (product group).
- Measure: Sales (the master measure you created).

The following chart is created, with a bar showing the sales for each product group. It is a bar chart at this stage.

![Combo chart with bars](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_combo_chart_1.png)

But we also want to show the sales margin, which has a different scale than the sales volume. Sales volume is in the scale of millions, while the margin is a percentage between 0 and 100. If we add margin as a bar next to sales volume, it would be too small to distinguish.

In the properties pane, go to Measures > Height of line. Use the drop down to add Margin % as a measure.

![Combo chart with bars and a line](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_combo_chart_2.png)

### Product sub group visualization

This is the visualization we want to show when a single product group is selected.

Make a copy of the product group visualization, and change the dimension to Product Sub Group.

### Master visualizations

You need to create two master visualizations to use in the tab container.

- Add the product group visualization as a master visualization with name Product Group - sales and margin.
- Add the product sub group visualization as a master visualization with name Product Sub Group - sales and margin

You can now delete the two visualizations you created earlier, they are saved as master visualizations.

### Tab container

You need to add a tab container to the sheet. Add the two visualizations to the tab container.

- Product Group - sales and margin

  Set Show condition to =GetPossibleCount([Product Group])>1
- Product Sub Group - sales and margin

  Set Show condition to =GetPossibleCount([Product Group])=1

You can also hide the selection tabs of the tab container under Appearance>Container>Tabs.

To demonstrate how it works, you can add a filter pane with Product Group.

## Discovery

You can now make selections in Product Group. When a single product group is selected, the chart displays data for product sub groups of that product group. Otherwise, the chart displays data for product groups.
