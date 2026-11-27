---
title: "Scatter plot"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/ScatterPlot/scatter-plot.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Scatter plot

The scatter plot presents pairs of values from two or three [measures](#glossary-0 "Glossary term").

This is useful when you want to show data where each instance has two numbers, for example, the relationship between Sales and Quantity per Customer.

Scatter plot displaying the relationship between Sales and Quantity per Customer.

![Scatter plot showing customer sales and sales quantity](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ScatterPlot.png "Click to view full size")

The scatter plot presents values from different measures over one [dimension](#glossary-1 "Glossary term") as a collection of points. In most [charts](#glossary-2 "Glossary term") you find your dimension on one of the axes, but for a scatter plot, the dimension is represented by the points in the chart and the measures are found on each of the two axes. When a third, optional, measure is used, its value is reflected in the bubble size. If you are analyzing large data sets and view compressed data, the density of the data points is reflected by color.

## When to use the scatter plot

The scatter plot helps you find potential relationships between values, and to find outliers in data sets. The scatter plot is useful when you want to show data where each instance has at least two metrics, for example, average life expectancy and average gross domestic product per capita in different countries.

### Advantages

The scatter plot is a great way to visualize the correlation of two or more measures at the same time. The third measure is an efficient way of differentiating between values and simplifying the identification of, for example, large countries, large customers, large quantities, and so on.

### Disadvantages

The scatter plot may be difficult to understand for an inexperienced user, because it has measure value on both axes, and the third, optional, measure adds complexity to the interpretation. Make sure a novice can interpret the scatter plot correctly. Using descriptive labels is a good way to make the [visualization](#glossary-3 "Glossary term") easier to interpret.

Values may be placed on top of each other and are then not visible until you zoom in.

## Display limitations

### Large data sets in scatter plots

You can set the maximum number of visible bubbles in a scatter plot if you are using advanced edit mode. Go to Presentation > Max visible bubbles. The default is 2,500. The maximum is 50,000. If you set a number less than 1,000, the scatter plot will behave as if the maximum is 1,000 visible bubbles.

If the number of displayed data points is less than Max visible bubbles, the data will be shown as individual bubbles. If there are more data points than the number set in Max visible bubbles, you will see an overview of your [dataset](#glossary-4 "Glossary term") as a table with colored boxes. This switch between compressed view and bubble view is done automatically. If there are more than 5,000 visible bubbles, then bubble labels and out of bound bubbles will not be shown.

Scatter plot with compressed data in a bubble view.

![Scatter plot with compressed data in a bubble view.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_SmartDataCompression.png "Click to view full size")

### Zooming and panning

In a scatter plot, you can zoom and pan around in your data. The interaction differs depending on what device you are using. If you are zooming in you can see where in the data set you are located by looking at the mini chart in the bottom right corner. If you zoom in on large data sets you will be able to see the data shown as boxes with values inside. The values represent the number of points in each box.

You cannot make selections when the scatter plot is rendering during a pan or zoom.

Zooming and panning is not possible when you have made a selection in the compressed data view.

You can change the compression resolution in the visual exploration menu or in the properties panel.

Scatter plot with compressed data in a compressed view.

![Scatter plot with compressed data in a compressed view.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_SmartDataCompressionZoom_1294x650.png "Click to view full size")

### Colors and legends

The compressed data view of a scatter plot has its own coloring settings. That means that any custom color definition for the scatter plot bubbles set in Colors will not affect compressed data. The density of the data points is reflected by color. More dense data is by default displayed in a darker color, but this can be customized. See [*Setting colors*](create-scatter-plots.htm#Colors).

When coloring by dimension is used in this chart, a maximum of 100 unique dimension values and 100 unique colors can be plotted on the legend.

## Learn more

- [*Creating scatter plots*](create-scatter-plots.htm)
- [Interpreting Scatter Plots](/lnk/Interpreting_scatter_plots)

Related learning:

- [Interpreting Scatter Plots](/lnk/Interpreting_scatter_plots)
