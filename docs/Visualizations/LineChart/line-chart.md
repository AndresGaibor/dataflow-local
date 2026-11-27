---
title: "Line chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/LineChart/line-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Line chart

The line chart is used to show trends over time. The [dimension](#glossary-0 "Glossary term") is always on the x-axis, and the [measures](#glossary-1 "Glossary term") are always on the y-axis.

![Line chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_LineChart-rev.png)

Your data set must consist of at least two data points to draw a line. A data set with a single value is displayed as a point. You can fill in the space beneath the lines by using an area line chart [visualization](#glossary-2 "Glossary term").

If you have a data set where data is missing for a certain month, you have the following options for showing the missing values:

- As gaps
- As connections
- As zeros

When a month is not present at all in the data source, it is also excluded from the presentation.

## When to use the line chart

The line chart is primarily suitable when you want to visualize trends and movements over time, where the dimension values are evenly spaced, such as months, quarters, or fiscal years.

### Advantages

The line chart is easy to understand and gives an instant perception of trends.

### Disadvantages

Using more than a few lines in a line chart makes the line chart cluttered and hard to interpret. For this reason, avoid using more than two or three measures.

## Display limitations

### Displaying large numbers of dimension values

When the number of dimension values exceeds the width of the visualization, a mini chart with a scroll bar is displayed. You can scroll by using the scroll bar in the mini chart, or, depending on your device, by using the scroll wheel or by swiping with two fingers. When a large number of values are used, the mini chart no longer displays all the values. Instead, a condensed version of the mini chart (with the items in gray) displays an overview of the values, but the very low and the very high values are still visible. 
Note that for line charts with two dimensions, the mini chart is only available in stacked area mode.

Line chart with a mini chart, since the dimension values exceeds the width of the visualization.

![Line chart with mini chart.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_MiniLineChart.png "Click to view full size")

### Displaying out of range values

In the properties panel, under Appearance, you can set a limit for the measure axis range. Without a limit, the range is automatically set to include the highest positive and lowest negative value, but if you set a limit you may have values that exceed that limit. When a data point value cannot be displayed, due to the range limits, an arrow indicates the direction of the value.

When a reference line is out of range, an arrow is displayed together with the number of reference lines that are out of range.

### Displaying large amounts of data in a line chart

If the chart uses a continuous scale, you can set the maximum number of visible points and lines.
In the properties panel, go to Presentation. Then adjust the following:

- Max visible points: Set the maximum number of points that will be displayed. The default is 2,000. The maximum is 50,000. If you set a number less than 1,000, the line chart will behave as if the maximum is 1,000 visible points. The actual maximum number of data points in the chart is affected by the distribution of the data, and could be lower than the value you configure with this setting. When there are more data points than the value you have set, data points are neither displayed, nor included in selections made in the chart.
- Max visible lines: Set the maximum number of lines that will be displayed. The default is 12. The maximum is 1,000.

If there are more data points than the number set in Max visible points, you will not see any points, only lines. If there are more than 5,000 visible points, then labels will not be shown. If you have a large number of lines, not all lines will be displayed, or lines may overlap.

If you have a large number of points or lines, it may take your chart longer to render when you zoom or pan. You cannot make selections when the line chart is rendering.

A line chart with a large data set. This chart is set to display 50 lines, and 20,000 data points.

![A line chart with many lines. Lines are overlapping, and not labels are displayed.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_linechart_displayinglargedata.png "Click to view full size")

To avoid displaying limited data sets, you can either make a selection or use dimension limits in the properties panel.

### Colors and legend

When coloring by dimension is used in this chart, a maximum of 100 unique dimension values and 100 unique colors can be plotted on the legend.

## Learn more

- [*Creating line charts*](create-line-charts.htm)
- [Interpreting Line Charts](/lnk/Interpreting_line_charts)
- [How do I forecast based upon time series data in Qlik Cloud?](/lnk/How_forecast_timeseries_data_qlikcloud)

Related learning:

- [Interpreting Line Charts](/lnk/Interpreting_line_charts)
- [How do I forecast based upon time series data in Qlik Cloud?](/lnk/How_forecast_timeseries_data_qlikcloud)
