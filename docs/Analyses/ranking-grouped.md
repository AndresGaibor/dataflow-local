---
title: "Ranking (grouped) analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/ranking-grouped.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Ranking (grouped) analysis

Show hierarchical dimensions in order of their contribution to a measure.

Grouped ranking analyses group three dimensions in a hierarchy and view their contributions to the selected measure.

Ranking (grouped) analysis

![Ranking (grouped) analysis showing a pivot table ranking average gross sales by product line, product group, and product subgroup.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-ranking-grouped.png "Click to view full size")

## Creating grouped ranking analyses

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Ranking (grouped) into the sheet.
3. Click Add dimension and select the first dimension in the hierarchy.
4. Click Add dimension and select the second dimension in the hierarchy.
5. Click Add dimension and select the third dimension in the hierarchy.
6. Click Add measure and a select a measure.
7. Optionally, to add an analysis period, do the following:

   1. In the properties panel, under Analysis properties, turn on Analysis period.
   2. Under Calendar period, select the calendar period to use.
   3. Under Period, select a specific period to use.

   Information noteAnalysis periods requires calendar periods in the logical model. For more information, see [*Defining analysis periods with calendar periods in Insight Advisor*](../BusinessLogic/business-logic-calendar.htm).
8. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
