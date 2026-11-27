---
title: "Creating and editing analyses"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/creating-analyses.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations"]
---

# Creating and editing analyses

Select the type of analysis you would like to make and build visualizations from that choice.

As an alternative to creating visualizations from chart types, you can instead start with the kind of analysis you want to build. Analyses build charts based on your fields and selected analysis type. You can customize the generated analysis.

Analyses in the sheet edit mode

![Analyses in sheet edit mode.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analyses.png "Click to view full size")

Analyses are useful when you know the kind of analysis you want to perform on your data, but not how to build it in a visualization.

Compared to charts, analyses have fewer options for customization and do not have all the properties available to a chart. You can convert analyses to charts, however, if you want additional customization options.

## Available analyses

The following analyses are available:

- Anomaly (spike): Detect and show large data variations including spikes and dips in a time series.
- Anomaly (trend): Detect and show abrupt data variations including change points between time series segments.
- Breakdown: Show multiple dimensions in order of contribution.
- Breakdown (geospatial): Show geographical contributions to a measure.
- Calculated measure (KPI): Show a calculated measure.
- Clustering (k-means): Show clusters of measures associated with a dimension using a statistical algorithm.
- Comparison: Show multiple measures for a dimension.
- Correlation: Show the strength of the relationship between two fields.
- Mutual information: Detect and show dependencies between the source and driver fields.
- Overview: Show the distribution of measures for one or more dimensions.
- Process control (mean): Show measures over a period of time compared with the overall mean of expected values.
- Process control (rolling mean): Show the performance of a measure over time between two calculated control limits.
- Ranking: Show dimensions in the order of their contribution to a measure.
- Ranking (grouped): Show hierarchical dimensions in order of their contribution to a measure.
- Relative importance: Show the relative importance of dimensions contributing to a total.
- Time series decomposition: Decompose a time series into trend, seasonal, and residual components.
- Trend over time: Show the performance of a measure over time, optionally broken down by a dimension.
- Trend with forecast: Show measures along with forecast over the current and future time periods.
- Year to date: Show a comparison of dimensions for the same period in previous years.

## Recommendations in analyses

When you add data sources to analyses, you can pick from recommended fields or pick any field from your data sources. Recommended fields are determined based on an analysis of your data model and the logical model, looking at properties such as:

- The classification of data in the field. Some analyses require certain kinds of specific data, such as dimension fields with temporal or geographic data.
- The number of distinct values. For example, a dimension with a small number of distinct values may be more suitable to one kind of analysis and visualization than a dimension with a large number of distinct values.
- The default aggregation for the field. For example, some analyses prefer measures that are averages or sums.
- Fields that are in the same hierarchy. For example, some forms of the comparison analysis require fields belong to a single hierarchy.

Additionally, when recommending fields, analyses look at the relationships between fields in the data model and which fields are suitable to be combined in analysis.

You can manage your logical model with business logic. For more information, see [*Building logical models for Insight Advisor with Business logic*](../BusinessLogic/business-logic-logical-models.htm).

## Creating analyses

Analyses are available in the advanced edit mode.

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. In the assets panel, click Analyses.
3. Drag and drop an analyses into the sheet.

   You can drop it in an empty location on the sheet, split the area of an existing visualization into two, or replace an existing visualization.
4. Add dimensions and measure, and then make adjustments in the properties panel. For more information, see the specific analysis type:

   - [*Anomaly (spike) analysis*](anomaly-spike.htm)
   - [*Anomaly (trend) analysis*](anomaly-trend.htm)
   - [*Breakdown analysis*](breakdown.htm)
   - [*Breakdown (geospatial) analysis*](breakdown-geospatial.htm)
   - [*Calculated measure (KPI) analysis*](calculated-measure.htm)
   - [*Clustering (k-means) analysis*](clustering-kmeans.htm)
   - [*Comparison analysis*](comparison.htm)
   - [*Correlation analysis*](correlation.htm)
   - [*Mutual information analysis*](mutual-information.htm)
   - [*Overview analysis*](overview.htm)
   - [*Process control (mean) analysis*](process-control-mean.htm)
   - [*Process control (rolling mean) analysis*](process-control-rolling-mean.htm)
   - [*Ranking analysis*](ranking.htm)
   - [*Ranking (grouped) analysis*](ranking-grouped.htm)
   - [*Relative importance analysis*](relative-importance.htm)
   - [*Time series decomposition analysis*](time-series-decomposition.htm)
   - [*Trend over time analysis*](trend-over-time.htm)
   - [*Trend with forecast analysis*](trend-with-forecast.htm)
   - [*Year to date analysis*](year-to-date.htm)

## Converting analyses to charts

You can convert analyses into charts. This gives you more options for customizing the charts created by your analyses, but you will no longer have access to the analysis properties.

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Select the analysis in the sheet.
3. In the properties panel, click ![Convert analysis to chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_default.svg).
4. Click Apply.

## Analyses and Insight Advisor Analysis Types

The analyses available in Analyses overlap with the analyses offered in Insight Advisor Analysis Types.

Analyses added from Analyses have different properties than the chart properties, allowing for easier customization of the analysis parameters. Insight Advisor Analysis Types adds analyses as charts. If you want to modify the chart, you must use chart properties rather than analysis properties.

Insight Advisor Analysis Types offers the following additional analyses:

- Period over period
- Period changes
- Period changes (detailed)
- Period over period (selected)

For more information on Insight Advisor Analysis Types, see [*Creating analyses by selecting analysis types*](../Insights/insight-advisor-create-visualizations.htm#Creating).

## Limitations

Analyses have the following limitations:

- Exploration menu and View data options are not available for analyses.
- Analyses cannot be individually added to reports in Qlik Automate using Add chart to report. Sheets with analyses can be added to reports with Add sheet to report or Add selection to report.
- An Analysis object can only be added to an Excel report template as a chart image. To add an Analysis to the template as tabular data, convert it to a chart in the application.
- For process control (rolling mean) and time series decomposition analysis types, if you convert to a chart, you need to click twice on Undo to undo the action.
- You cannot redo changing an analysis type to a chart after clicking Undo. In the properties panel, click ![Convert analysis to chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_default.svg) instead.
- Undo and redo are not supported if you select a bar, line, or sankey chart from the alternate charts in an analysis. Users can change charts by selecting other charts from the alternate charts, however.
- Geospatial breakdown is not supported for download or being added to notes.
