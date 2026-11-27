---
title: "Time series decomposition analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/time-series-decomposition.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Time series decomposition analysis

Decompose a time series into trend, seasonal, and residual components.

Time series decomposition shows four decompositions for the measure in the selected time period:

- Observed: The measure values for the time series.
- Trend: The increasing or decreasing value as determined by the data model.
- Seasonality: The repeating short-term cycle in the series.
- Residual: Values not included in the trend. Residual shows where a model is missing more than it is finding.

You can optionally remove decompositions from the analysis.

Time series decomposition analysis

![Time series decomposition analysis showing gross profit over order date with the observed, trend, seasonal, and residual decompositions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-time-series-decomposition.png "Click to view full size")

## Creating time series decomposition analysis

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Time series decomposition into the sheet.
3. Click Add dimension and select a temporal dimension.
4. Click Add measure and a select a measure.
5. In the properties panel, under Analysis properties, optionally customize your analysis:

   - To change the number of period segments, after Period segments, adjust the slider.
   - To remove decompositions, after Decompositions, clear the decompositions you do not want in your analysis.
6. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
