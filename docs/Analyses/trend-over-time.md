---
title: "Trend over time analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/trend-over-time.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Trend over time analysis

Show the performance of a measure over time, optionally broken down by a dimension with low [cardinality](#glossary-0 "Glossary term").

Trend over time analysis

![Trend over time analysis showing the average cost of sale over order date](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-trend-over-time.png "Click to view full size")

## Creating trend over time analyses

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Trend over time into the sheet.
3. Click Add dimension and select a temporal dimension.
4. Click Add measure and a select a measure.
5. Optionally, to add an analysis period, do the following:

   1. In the properties panel, under Analysis properties, turn on Analysis period.
   2. Under Calendar period, select the calendar period to use.
   3. Under Period, select a specific period to use.

   Information noteAnalysis periods requires calendar periods in the logical model. For more information, see [*Defining analysis periods with calendar periods in Insight Advisor*](../BusinessLogic/business-logic-calendar.htm).
6. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
