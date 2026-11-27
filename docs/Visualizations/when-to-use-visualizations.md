---
title: "Best practices for choosing visualization types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/when-to-use-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization"]
---

# Best practices for choosing visualization types

A good [visualization](#glossary-0 "Glossary term") clearly presents relationships among many values, and lets you analyze data at a glance. Qlik Cloud Analytics offers a range of Qlik Sense visualizations, [charts](#glossary-1 "Glossary term"), and analyses. Each chart and analysis excels at visualizing data in different ways for different purposes. You should select your charts and analyses by deciding what you want to see from the data in your charts.

If you are unsure of what visualizations to use, Qlik Sense can offer recommendations. You can use analyses to start with the type of analysis you want to make rather than starting with a chart. For more information, see [*Creating and editing analyses*](../Analyses/creating-analyses.htm). Insight Advisor can also help you create visualizations. For more information, see [*Creating visualizations with Insight Advisor*](../Insights/insight-advisor-create-visualizations.htm) and [*Creating visualizations using Insight Advisor chart suggestions*](creating-visualization-assistance.htm).

The following lists the purposes for viewing data and the chart and analysis type recommended to achieve that purpose:

## Viewing comparisons

Comparison charts are used to compare values against each other. They show the differences in values, such as the difference between categories, or how values are changing over time.

Questions that might be answered by comparison charts include:

- What product has the highest total sales this year?
- How have product sales risen or fallen over the last 24 months?

Chart types for viewing comparisons

| Chart type | Common purpose |
| --- | --- |
| [*Bar chart*](Bar-Chart/bar-chart.htm) | Comparing categories against the same [measure](#glossary-2 "Glossary term") or measures. |
| [*Combo chart*](ComboChart/combo-chart.htm) | Comparing measures that are different in scale. |
| [*Grid chart*](VisualizationBundle/grid-chart.htm) | Comparing measures to quickly see differences in measure values. |
| [*Line chart*](LineChart/line-chart.htm) | Comparing trends over time. |

The following analyses are useful for creating charts for viewing comparisons:

Analysis types for viewing comparisons

| Analysis type | Common purpose |
| --- | --- |
| [*Comparison analysis*](../Analyses/comparison.htm) | Showing multiple measures for a dimension. |
| [*Ranking analysis*](../Analyses/ranking.htm) | Showing dimensions in the order of their contribution to a measure. |
| [*Ranking (grouped) analysis*](../Analyses/ranking-grouped.htm) | Showing hierarchical dimensions in order of their contribution to a measure. |
| [*Trend over time analysis*](../Analyses/trend-over-time.htm) | Showing the performance of a measure over time, optionally broken down by a dimension. |

If you want to compare different values of the same dimension, you can use alternate states. For more information, see [*Using alternate states for comparative analysis*](alternate-states-comparative-analysis.htm).

## Viewing relationships

Relationship charts are used to explore how values relate to each other. A relationship chart allows you to find correlations, outliers, and clusters of data.

Questions that might be answered by relationship charts include:

- Is there a correlation between advertising spending and sales for our products?
- How do expenses and income vary per region?

Chart types for viewing relationships

| Chart type | Common purpose |
| --- | --- |
| [*Scatter plot*](ScatterPlot/scatter-plot.htm) | Viewing the relationship between two or three measures for a [dimension](#glossary-3 "Glossary term"). |

The following analyses are useful for creating charts for viewing relationships:

Analysis types for viewing relationships

| Analysis type | Common purpose |
| --- | --- |
| [*Clustering (k-means) analysis*](../Analyses/clustering-kmeans.htm) | Showing clusters of measures associated with a dimension using a statistical algorithm. |
| [*Correlation analysis*](../Analyses/correlation.htm) | Showing the strength of the relationship between two fields. |
| [*Mutual information analysis*](../Analyses/mutual-information.htm) | Detecting and show dependencies between the source and driver fields. |
| [*Relative importance analysis*](../Analyses/relative-importance.htm) | Showing the relative importance of dimensions contributing to a total. |

## Viewing compositions

Composition charts take a total value and discover what component values make up that total. Composition charts can be static, showing the current composition of a total value, or they can show how the composition of a total value changes over time. Composition charts can display compositions either by percentage of the total value or the fixed values in the total value.

Questions that might be answered by composition charts include:

- What percentages of our total sales come from which regions?
- What is each department's allotment of our total quarterly budget over the past year?

Chart types for viewing compositions

| Chart type | Common purpose |
| --- | --- |
| [*Bar chart*](Bar-Chart/bar-chart.htm) | Viewing the changing composition of a value over a short period of time. |
| [*Funnel chart*](VisualizationBundle/funnel-chart.htm) | Viewing the decreasing stages of a process. |
| [*Line chart*](LineChart/line-chart.htm) | Viewing the changing composition of a value over a long period of time. |
| [*Pie chart and donut chart*](PieChart/pie-chart.htm) | Viewing the static composition of a value. |
| [*Sankey chart*](VisualizationBundle/sankey-chart.htm) | Viewing contributions to the overall flow. |
| [*Treemap*](TreeMap/treemap.htm) | Viewing the static composition of a value's accumulation to the total. |
| [*Trellis container*](VisualizationBundle/trellis-container.htm) | Viewing comparisons of the same chart showing different dimension values. |
| [*Waterfall chart*](WaterfallChart/waterfall-chart.htm) | Viewing the static composition of a value with accumulation or subtraction to the total. |

The following analyses are useful for creating charts for viewing compositions:

Analysis types for viewing compositions

| Analysis type | Common purpose |
| --- | --- |
| [*Breakdown analysis*](../Analyses/breakdown.htm) | Showing multiple dimensions in order of contribution. |
| [*Time series decomposition analysis*](../Analyses/time-series-decomposition.htm) | Decomposing a time series into trend, seasonal, and residual components. |
| [*Trend over time analysis*](../Analyses/trend-over-time.htm) | Showing the performance of a measure over time, optionally broken down by a dimension. |
| [*Trend with forecast analysis*](../Analyses/trend-with-forecast.htm) | Showing measures along with forecast over the current and future time periods. |
| [*Year to date analysis*](../Analyses/year-to-date.htm) | Showing a comparison of dimensions for the same period in previous years. |

## Viewing distributions

Distribution charts are used to explore how the values within data are grouped. Distribution charts show you the shape of your data, the range of its values, and possible outliers.

Questions that might be answered by distribution charts include:

- What is the number of customers per age group?
- What cities have the highest use of our services?

Chart types for viewing distributions

| Chart type | Common purpose |
| --- | --- |
| [*Histogram*](Histogram/histogram.htm) | Viewing the how data is distributed over intervals. |
| [*Scatter plot*](ScatterPlot/scatter-plot.htm) | Viewing the distribution of two measures. |
| [*Distribution plot*](DistPlot/distribution-plot.htm) | Viewing the distribution of measure values in a dimension. |
| [*Box plot*](BoxPlot/box-plot.htm) | Viewing the range and distribution of numerical data. |

The following analyses are useful for creating charts for viewing distributions:

Analysis types for viewing distributions

| Analysis type | Common purpose |
| --- | --- |
| [*Overview analysis*](../Analyses/overview.htm) | Showing the distribution of measures for one or more dimensions. |

## Viewing performances

Performance charts provide a quick view of a performance measure. Looking at a performance chart, a user can quickly identify the measure value and whether the results are as expected or not.

Questions that might be answered by performance charts include:

- What are the current total sales for this quarter?
- Are current total sales for this quarter meeting the projected sales for the quarter?
- How is performance for this product line compared with other product lines?

Chart types for viewing performances

| Chart type | Common purpose |
| --- | --- |
| [*Bullet chart*](BulletChart/bullet-chart.htm) | Comparing performance of a measure for several dimensions. |
| [*Gauge*](Gauge/gauge.htm) | Viewing a performance value to understand performance immediately. |
| [*KPI*](KPI/KPI.htm) | Viewing one or two performance measures. |
| [*Text*](DashboardBundle/text-object.htm) | Viewing text or several measures. |
| [*Text & image*](TextAndImage/text-image.htm) | Viewing text or several measures with an image. Legacy visualization. |

The following analyses are useful for creating charts for viewing performances:

Analysis types for viewing performances

| Analysis type | Common purpose |
| --- | --- |
| [*Anomaly (spike) analysis*](../Analyses/anomaly-spike.htm) | Detecting and showing large data variations including spikes and dips in a time series. |
| [*Anomaly (trend) analysis*](../Analyses/anomaly-trend.htm) | Detecting and showing abrupt data variations including change points between time series segments. |
| [*Clustering (k-means) analysis*](../Analyses/clustering-kmeans.htm) | Showing clusters of measures associated with a dimension using a statistical algorithm. |
| [*Process control (mean) analysis*](../Analyses/process-control-mean.htm) | Showing measures over a time period compared with the overall mean of expected values. |
| [*Process control (rolling mean) analysis*](../Analyses/process-control-rolling-mean.htm) | Showing the performance of a measure over time between two calculated control limits. |

## Viewing data

Data charts present detailed data rather than a visualization of the data. Data charts are useful when you need to view precise values, and when you want to compare individual values.

Questions that might be answered by data charts include:

- What are the records for each transaction for this month?
- What are the quantity and sales for each item in each product group for each of our customers?

Chart types for viewing data

| Chart type | Common purpose |
| --- | --- |
| [*Pivot table*](PivotTable/pivot-table.htm) | Viewing precise value for several dimensions and measures. |
| [*Straight table*](StraightTable/sn-straight-table.htm) | Viewing precise values from your data without trends or patterns. |
| [*Table*](Table/table.htm) | Viewing precise values from your data without trends or patterns. Legacy visualization. |

## Viewing geography

Geographical charts let you visualize your data by geography, displaying your data on a map either as points or areas.

Common questions that might be answered by geographical charts include:

- What cities have the highest use of our services?
- Which countries have the most customers?

Chart types for viewing geography

| Chart type | Common purpose |
| --- | --- |
| [*Map chart*](Map/Map.htm) | Viewing data represented geographically by point or area. |

The following analyses are useful for creating charts for viewing geography:

Analysis types for viewing geography

| Analysis type | Common purpose |
| --- | --- |
| [*Breakdown (geospatial) analysis*](../Analyses/breakdown-geospatial.htm) | Showing geographical contributions to a measure. |

## Viewing organizational structure

Organization charts let you visualize the hierarchy of organizations with a tree structure.

Chart types for viewing organizational structure

| Chart type | Common purpose |
| --- | --- |
| [*Org chart*](VisualizationBundle/org-chart.htm) | Viewing and navigating the structure of an organization with a tree structure. |

## Building sheets and dashboards

Some visualizations and objects help you to layout dashboards and sheets. Others can add useful actions to sheets.

Objects for laying out dashboards and sheets

| Chart type | Common purpose |
| --- | --- |
| [*Animator*](DashboardBundle/animator.htm) | Animating changes in the visualizations over time. |
| [*Button*](Button/button.htm) | Adding actions to the sheet. |
| [*Date range picker*](DashboardBundle/date-range-picker.htm) | Selecting a single date or range of dates. |
| [*Filter pane*](FilterPane/filter-pane.htm) | Selecting values to explore your data. |
| [*Layout container*](DashboardBundle/layout-container.htm) | Storing multiple visualizations in a single object. |
| [*Line*](DashboardBundle/line.htm) | Adding lines to divide content on a sheet. |
| [*Navigation menu*](Navigation-menu/navigation-menu.htm) | Adding sheet navigation to the sheet. |
| [*NL insights*](NLInsights/nl-insights.htm) | Displaying natural language insights and information about selected dimensions and measures. |
| [*Tab container*](Container/container-object.htm) | Storing multiple visualizations in a single object. |
| [*Variable input control*](DashboardBundle/variable-input.htm) | Change the values in variables used in visualizations. |
| [*Video player*](DashboardBundle/video-player.htm) | Adding videos to sheets. |

## What if no standard chart suits my purpose?

You can create custom visualization objects if none of the standard charts provided fit your requirements for visualizing your data.

For more information, see [*Creating a visualization using a custom object*](create-visualization-extensions.htm).
