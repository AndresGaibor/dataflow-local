---
title: "Process control (rolling mean) analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/process-control-rolling-mean.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Process control (rolling mean) analysis

Show the performance of a measure over time between two calculated control limits.

Process control (rolling mean) monitors data against expected statistical ranges based on nearby values.

Process control (rolling mean) analysis

![Process control rolling mean analysis showing a control chart with average gross profit over the order date against a rolling mean.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-process-control-rolling-mean.png "Click to view full size")

## Creating process control (rolling mean) analyses

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Process control (rolling mean) into the sheet.
3. Click Add dimension and select a temporal dimension.
4. Click Add measure and a select a measure.
5. Optionally, in the properties panel, under Analysis properties, adjust the slider under Sigma.
6. Optionally, to add an analysis period, do the following:

   1. In the properties panel, under Analysis properties, turn on Analysis period.
   2. Under Calendar period, select the calendar period to use.
   3. Under Period, select a specific period to use.

   Information noteAnalysis periods requires calendar periods in the logical model. For more information, see [*Defining analysis periods with calendar periods in Insight Advisor*](../BusinessLogic/business-logic-calendar.htm).
7. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
