---
title: "Trend with forecast analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/trend-with-forecast.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Trend with forecast analysis

Show measures along with forecast over the current and future time periods.

Trend with forecast analysis

![Trend with forecast analysis, showing the average cost of sale over order dates, with a forecast.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-trend-with-forecast.png "Click to view full size")

## Creating trend with forecast analyses

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Trend with forecast into the sheet.
3. Click Add dimension and select a temporal dimension.
4. Click Add measure and a select a measure.
5. In the properties panel, under Analysis properties, optionally customize your analysis:

   - To change the number of forecast steps, after Forecast steps, adjust the slider.
   - To change the step unit, after Step unit, select a different unit.
   - To change the forecast method, under Forecast method, select one of the following:

     - Singular spectrum analysis (SSA)
     - Ordinary least squares (OLS)
   - To remove decompositions, after Decompositions, clear the decompositions you do not want in your analysis.
   - To set an analysis period, do the following:

     1. turn on Analysis period.
     2. Under Calendar period, select the calendar period to use.
     3. Under Period, select a specific period to use.

     Information noteAnalysis periods requires calendar periods in the logical model. For more information, see [*Defining analysis periods with calendar periods in Insight Advisor*](../BusinessLogic/business-logic-calendar.htm).
6. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
