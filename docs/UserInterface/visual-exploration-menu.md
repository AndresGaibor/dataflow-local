---
title: "Visual exploration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/visual-exploration-menu.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring data with visualizations"]
---

# Visual exploration

The visual exploration menu lets you change certain [visualization](#glossary-0 "Glossary term") [properties](#glossary-1 "Glossary term"), without making [selections](#glossary-2 "Glossary term") or editing the [sheet](#glossary-3 "Glossary term"). For example, you can change data, sort data, color by [dimension](#glossary-4 "Glossary term") or [measure](#glossary-5 "Glossary term"), and change how labels are displayed.

For a visual demo about how to use the visual exploration menu, see [Visual explorations](https://share.vidyard.com/watch/VkAXeNA9iYZo96d4xCnCKH?).

Information noteThe visual exploration menu is available for the following visualizations: bar chart, line chart, pie chart, scatter plot, treemap, box plot, distribution plot, map, and combo chart.

Example of visual exploration menu for a scatter plot visualization.

![Visual exploration menu with Presentation tab open.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_VisualExplorationMenuScatter.png "Click to view full size")

## Using the visual exploration menu to change properties

Do the following:

1. When analyzing, hover over the visualization you want to change.
2. Click ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) at the top right of the visualization or right-click on the visualization and select Exploration menu.
3. Update the properties you want to change.
4. To close the menu and save your changes, click ![Controls](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg). The changes are saved during this session.

   To save your changes for future sessions (and have them updated in the properties panel), click Apply. This button is only available for visualizations that are not master items or linked to master items, and for users with rights to edit the sheet.

   Information noteIf you do not click Apply to save the changes or Discard to discard the changes and later click Edit to edit the sheet, you will be prompted to select whether to apply or discard the changes you made when analyzing the sheet.

## Using the visual exploration menu to change data

The visual exploration menu can change visualization data, if you have alternative dimensions or measures. Simply click on the dimension or measure you want the visualization to display. The selection is marked with a ![Tick](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg).

Information noteAlternative dimensions and measures are dimensions and measures that are added to a visualization, but are not displayed until a user chooses to switch which dimensions and measures are being displayed during visual exploration.

Example of visual exploration menu when changing data

![Visual exploration menu with data tab open.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_VisualExplorationMenuChangeData.png "Click to view full size")

## Using the visual exploration menu to explore time series forecasting

You can change the time series forecasting properties of line charts with the visual exploration menu.

Example of visual exploration when changing time series forecasting

![Visual exploration menu with data tab open for a line chart with forecasting.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_VisualExplorationMenuForecasting.png "Click to view full size")

For Dimensions, you can adjust the following properties:

- Forecast steps: Enter the number of steps to forecast.
- Step size: Enter a number to multiply each step by.
- Step unit: Select a time or number interval.

For Measures, you can adjust the following properties:

- Forecast: Turn forecasting on or off in the line chart..
- Method: Select the forecasting method:

  - SSA: Singular Spectrum Analysis (SSA) identifies noise and seasonality as well as trend. SSA is the best option to forecast trends with cyclical or oscillatory behavior.
  - OLS: Ordinary Least Square (QLS) calculates a trend line by minimizing the sums of the squares of the differences between the observed dependent [variable](#glossary-6 "Glossary term") and the predicted dependent variable. OLS is the best option when you want to see a linear trend of the data.

  For more information about forecasting methods, see [*OLS and SSA methods*](../Visualizations/LineChart/timeseries-forecast.htm#OLS).

## Limitations

The exploration menu has the following limitations:

- You cannot use the exploration menu with analyses. For more information on analyses, see [*Creating and editing analyses*](../Analyses/creating-analyses.htm).
- The visualization exploration menu is not available for charts that are located inside a tab container, layout container, or legacy container object.
