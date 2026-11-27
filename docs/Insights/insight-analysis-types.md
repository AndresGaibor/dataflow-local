---
title: "Insight Advisor analysis types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insight-analysis-types.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating visualizations with Insight Advisor"]
---

# Insight Advisor analysis types

[Insight Advisor](#glossary-0 "Glossary term") provides results using a wide range of analysis types. These analysis types provide best practice [visualizations](#glossary-1 "Glossary term") for generated [charts](#glossary-2 "Glossary term").

Different analysis types are used depending on the inputs of the search and the characteristics of your data. The Qlik cognitive engine determines the best analysis type for your search depending on the available data. The following table describes the analysis types. Not all conditions for each analysis type are listed. The table also lists charts potentially available as alternatives when editing an Insight Advisor analysis.

Information noteThese analysis types are not to be confused with analysis types in the Discovery Agent. See [*Discovery Agent*](../DiscoveryAgent/discovery-agent.htm).

Analysis types

| Analysis type | Description | Dimensions | Measures |
| --- | --- | --- | --- |
| Anomaly (spike) | Identify spike anomalies by analyzing patterns in historic data. | 1 date/time dimension | 1 |
| Anomaly (trend) | Identify change points by analyzing patterns in historic data. Change point detection identifies moments in time when the underlying process generating the data experiences significant changes. These can include sudden changes in the baseline or trends in the data. It may also include shifts in the magnitude of noise distribution in the data.  The combo chart lines track the [measure](#glossary-3 "Glossary term") and bars display possible change point anomalies. | 1 date/time dimension | 1 |
| Breakdown | View nested [dimensions](#glossary-4 "Glossary term") of data that provide a breakdown of relative contributions to a measure. | 2-3 | 1 |
| Breakdown (geospatial) | Group data by simple and hierarchical geographic divisions. | 1-2 | 1-2 |
| Calculated measure (KPI) | Summarize performance in a given business segment or dimension using a key performance indicator (KPI). | 0 | 1-2 |
| Clustering (k-means) | Cluster data points aggregated by similarities from 2 measures over a dimension using a machine learning k-means algorithm. | 1 | 2 |
| Comparison | Compare two measures for a dimension. | 1 | 2 |
| Correlation | Identify complementary and inverse relationships between two data values. | 0-2 | 2 |
| Mutual information | Create a measure of certainty between pairs of values using a machine learning algorithm that applies random data distributions.  The dependency indicator ranges between 0 percent (no dependency) and 100 percent(strong dependency).  Mutual information selects one [field](#glossary-5 "Glossary term") (measure or dimension) as the target and then selects 1 to 10 dimensions or measures as drivers.  Results for this analysis type for the same fields or [selections](#glossary-6 "Glossary term") might vary due to the random data selection. | variable | variable |
| Overview | Describe how data ranges relate to each other in terms of an absolute measure. | 1-2 | 1 |
| Period changes | Build a [sheet](#glossary-7 "Glossary term") with measures, rank, and comparison analysis for dimensions across different time periods.  Requires a default calendar period set for the group containing the measure in the [logical model](#glossary-8 "Glossary term"). | 1-2 | 1 |
| Period changes (detailed) | Build a sheet with measures, rank, and comparison analysis for a hierarchy of dimensions across different time periods.  Requires a default calendar period set for the group containing the measure in the logical model. | 1 | 1 |
| Period over period | Compare dimensions across time periods.  Requires a default calendar period set for the group containing the measure in the logical model. | 1 | 1 |
| Period over period (selected) | Compare dimensions across time periods. It includes a filter pane for selecting dimension values.  Requires a temporal fields with autoCalendar-derived field selected as a part of the query. | 1-3 | 1 |
| Process control (mean) | Monitor data against expected statistical ranges based on mean values. | 1 date/time dimension | 1 |
| Process control (rolling mean) | Monitor data against expected statistical ranges based on nearby values. | 1 date/time dimension | 1 |
| Ranking | Rank dimension values by relative importance with a measure. | 1-2 | 1 |
| Ranking (grouped) | Rank hierarchical dimension values by relative importance with a measure. | 1-2 | 1 |
| Relative importance | Show the size of dimension values that contribute to the whole. Can also be used to perform Pareto or 80-20 contribution analysis. | 1 | 1 |
| Time series decomposition | Decompose a time series into trend, seasonal, and residual components. | 1 date/time dimension | 1 |
| Trend over time | Show data trends over time, optionally broken down by a dimension with low [cardinality](#glossary-9 "Glossary term"). | 1 date/time dimension and optionally 1 other dimension | 1-3 |
| Trend with forecast | Show data trends over time, along with forecast values for future time periods. | 1 date/time dimension | 1 |
| Values (table) | Show data organized in rows and columns that show measures and dimensions. | 0-10 | 0-10 |
| Year to date | Compare dimensions over the same period in a previous year. | 1 | 1 |

Related learning:

- [How do I evaluate relationships using Mutual information?](/lnk/How_evaluate_relationships_using_Mutual_information)
- [How do I evaluate Relative importance in a Pareto chart?](/lnk/How_evaluate_Relative_importance_Pareto)
- [How do I detect anomalies in a time series?](/lnk/How_detect_anomalies_time_series)
