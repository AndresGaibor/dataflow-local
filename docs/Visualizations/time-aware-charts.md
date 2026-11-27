---
title: "Creating time-aware charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/time-aware-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating time-aware charts

Time-aware [charts](#glossary-0 "Glossary term") are [visualizations](#glossary-1 "Glossary term") that use a continuous scale to provide a complete and accurate view of time-based data. That is, when you enable continuous scaling on the x-axis in a chart with date fields, data points are separated from each other by a distance relative to their associated time. As well, the axis labels are evenly separated whether or not there is data for that point and the chart view is compressed to avoid scrolling.

Information noteContinuous scale is supported for line charts, bar charts, and combo charts.

A continuous scale is most commonly used with date fields such as:

- Second
- Minute
- Hour
- Week
- Month
- YearMonth
- Quarter
- YearQuarter
- Year
- Date
- Timestamp

## Adding a continuous scale

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click the chart that you want to edit.
3. In the properties panel, click the Appearance tab.
4. In the X-axis section, switch Continuous from Auto to Custom, and then check Use continuous scale. This explicitly sets the chart to use a continuous scale.

   The chart is compressed and the data points and labels are readjusted.
5. For bar charts, you can set additional properties to adjust the width of the bars. See [*Configuring a continuous or discrete scale*](Bar-Chart/create-bar-charts.htm#AxisSettings).

## Making selections in a time-aware chart

When navigating a time-aware chart, you can zoom into a smaller time span to take [snapshots](#glossary-2 "Glossary term") of the data displayed and select data values. [Selections](#glossary-3 "Glossary term") made on a time axis using range selection select all data values (even those that are not visible). Selections made on the [measure](#glossary-4 "Glossary term") axis or using lasso selections only select visible values.
