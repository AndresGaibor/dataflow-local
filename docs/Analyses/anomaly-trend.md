---
title: "Anomaly (trend) analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/anomaly-trend.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Anomaly (trend) analysis

Detect and show abrupt data variations, including change points between time series segments.

Change point detection identifies moments in time when the underlying process generating the data experiences significant changes. These can include sudden changes in the baseline or trends in the data. It may also include shifts in the magnitude of noise distribution in the data.

The combo chart created by Anomaly (trend) tracks the measure with lines. The bars display possible change point anomalies.

Anomaly (trend) analysis

![Anomaly (trend) analysis showing change points detected for Gross Profit values over the field OrderDate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-anomaly-trend.png "Click to view full size")

## Creating anomaly (trend) analyses

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Anomaly (trend) into the sheet.
3. Click Add dimension and select a temporal dimension.
4. Click Add measure and select a measure.
5. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
