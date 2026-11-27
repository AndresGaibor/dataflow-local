---
title: "Bar chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Bar-Chart/bar-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Bar chart

The bar chart is suitable for comparing multiple values. The [dimension](#glossary-0 "Glossary term") axis shows the category items that are compared, and the [measure](#glossary-1 "Glossary term") axis shows the value for each category item.

In the image, the dimension values are different regions: Nordic, USA, Japan, UK, Spain, and Germany. Each region represents a dimension value, and has a corresponding bar. The bar height corresponds to the measure value (sales) for the different regions.

![Bar chart visualization.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChart.png)

You can make more complex comparisons of data by using grouped or stacked bars. This requires using two dimensions and one measure. The two example charts use the same two dimensions and the same measure:

Grouped bars: With grouped bars, you can easily compare two or more items in the same categorical group.

![Bar chart with grouped bars.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartGrouped.png)

Stacked bars: With stacked bars it is easier to compare the total quantity between different months. Stacked bars combine bars of different groups on top of each other and the total height of the resulting bar represents the combined result.

![Bar chart with stacked bars.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartStacked.png)

Using the butterfly chart configuration, you can compare two subsets of data in separate, mirrored views. The butterfly chart requires using one dimension and two measures. Data is shown along the same axis.

![Bar chart configured as a butterfly chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartButterfly.png)

The bar chart can be displayed horizontally or vertically, as in the example below:

![Two bar charts, one displayed horizontally and one vertically.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartHorVert.png)

## When to use the bar chart

Grouping and stacking bars makes it easy to visualize grouped data. The bar chart is also useful when you want to compare values side by side, for example sales compared to forecast for different years, and when the measures (in this case sales and forecast) are calculated using the same unit.

Advantages: The bar chart is easy to read and understand. You get a good overview of values when using bar charts.

Disadvantages: The bar chart does not work so well with many dimension values due to the limitation of the axis length. If the dimensions do not fit, you can scroll using the scroll bar, but then you might not get the full picture.

## Display limitations

### Displaying large numbers of dimension values

When the number of dimension values exceeds the width of the visualization, a mini chart with a scroll bar is displayed. You can scroll by using the scroll bar in the mini chart, or, depending on your device, by using the scroll wheel or by swiping with two fingers. When a large number of values are used, the mini chart no longer displays all the values. Instead, a condensed version of the mini chart (with the items in gray) displays an overview of the values, but the very low and the very high values are still visible.

![Bar chart with mini chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MiniBarChart.png)

Tip noteYou can exchange the mini chart with a regular scrollbar, or hide it, with the Scrollbar property.

### Displaying out of range values

In the [properties](#glossary-2 "Glossary term") panel, under Appearance, you can set a limit for the measure axis range. Without a limit, the range is automatically set to include the highest positive and lowest negative value, but if you set a limit you may have values that exceed that limit. A bar that exceeds the limit will be cut diagonally to show that it is out of range.

When a reference line is out of range, an arrow is displayed together with the number of reference lines that are out of range.

### Displaying large amounts of data in a stacked bar chart

When displaying large amounts of data in a stacked bar chart, there may be cases when not each dimension value within a bar is displayed with correct color and size. These remaining values will instead be displayed as a gray, striped area. The size and total value of the bar will still be correct, but not all dimension values in the bar will be explicit.

![A stacked bar chart with the remaining values displayed as a gray, striped area.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_BarChartLimited.png)

To remove the gray areas, you can either make a selection or use dimension limits in the properties panel.

The approximate limit for how many stacked bars that can be displayed without gray areas is 5000 bars, assuming that each bar consists of 10 inner dimension values and one dimension value and one measure value for the whole bar.

The initial data load is 500 dimension values or dimension stacks. (The value 500 refers to the outer dimension values, not each dimension value in a stack.) When you have scrolled past those 500 values, an incremental load is performed, where values are instead loaded based on the current view or scroll position.

### Displaying large amounts of data in a bar chart with continuous scale

If the chart uses a continuous scale, a maximum of 2000 data points can be displayed. The actual maximum number of data points in the chart is affected by the distribution of the data. Above that number, data points are neither displayed, nor included in [selections](#glossary-3 "Glossary term") made in the chart. Additionally, only twelve dimension values are displayed for the second dimension in a chart with two dimensions and continuous scale.

To avoid displaying limited data sets, you can either make a selection or use dimension limits in the properties panel.

### Colors and legend

When coloring by dimension is used in this chart, a maximum of 100 unique dimension values and 100 unique colors can be plotted on the legend.

### Stacked bar charts and number formatting by measure expression

Stacked bar charts ignore number formatting by measure expression and instead will always us the default formatting to make it consistent with the formatting of totals.

## Learn more

- [*Creating bar charts*](create-bar-charts.htm)
- [Interpreting Bar Charts](/lnk/Interpreting_bar_charts)

Related learning:

- [Interpreting Bar Charts](/lnk/Interpreting_bar_charts)
