---
title: "Correlation analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/correlation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Correlation analysis

Show the strength of the relationship between two or more fields.

Correlation compares the relationship of two measure fields, identifying complementary and inverse relationships.

Optionally, up to two dimensions can be added to the analysis.

Correlation analysis

![Correlation analysis showing the correlation between the fields Cost of Sale and Gross Profit at 90.94%.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-correlation.png "Click to view full size")

## Creating correlation analysis

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Correlation into the sheet.
3. Click Add dimension and select a field.
4. Click Add dimension and a select a second field.
5. Optionally, add one or two dimensions to the analysis. In the properties panel, under Data, click Add and select a dimension.
6. Optionally, to add an analysis period, do the following:

   1. In the properties panel, under Analysis properties, turn on Analysis period.
   2. Under Calendar period, select the calendar period to use.
   3. Under Period, select a specific period to use.

   Information noteAnalysis periods requires calendar periods in the logical model. For more information, see [*Defining analysis periods with calendar periods in Insight Advisor*](../BusinessLogic/business-logic-calendar.htm).
7. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
