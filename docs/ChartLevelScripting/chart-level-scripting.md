---
title: "Using chart level scripting in visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/chart-level-scripting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Using chart level scripting in visualizations

With [chart](#glossary-0 "Glossary term") level scripting, you can add script-like functionality to the results of a [visualization](#glossary-1 "Glossary term"). It complements chart expressions, as chart level scripting include control statements, such as loops and recursive actions, for more complex mathematical calculations. You can also modify multiple columns, as long as a placeholder exists in the chart, and add new rows to a result.

You can use chart level scripting on most visualization types and you access it from the [properties](#glossary-2 "Glossary term") panel. Some visualizations or specific configurations, do not support chart level scripting. In those cases, you cannot access chart level scripting from the properties panel, or you will receive an error message.

When modifying chart data, you use a sub-set of the Qlik Sense script which consists of a number of statements. See [Chart level scripting](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/modifier-statements-keywords.htm).

You enable chart level scripting in the application settings. When enabled, a Scripts control is available on the Data section of the properties panel for a visualization. See [Turning on chart level scripting](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/enable-chart-level-scripting.htm).

Even when disabled, existing chart scripts will be processed. Disabling once authored content has been developed is a useful way of preventing new chart scripts being created by other users.

## Adding a chart script to a visualization

You can add chart scripts to existing visualizations, or when you create new visualizations.

Chart level scripting must be enabled in the application before you can add a chart script to a visualization, see [Turning on chart level scripting](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/enable-chart-level-scripting.htm).

### Adding chart scripts to a new visualization

Do the following:

1. Drag the visualization from the assets panel onto the sheet, or double-click the visualization.
2. On the Data tab, add [dimensions](#glossary-3 "Glossary term") and [measures](#glossary-4 "Glossary term") to the visualization.
3. Also on the Data tab, add a chart script in the Scripts section.

   You can add maximum five chart scripts per visualization.

### Adding chart scripts to an existing visualization

Do the following:

1. When in ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg)Edit sheet mode, select the visualization.
2. On the Data tab, add a chart script in the Scripts section.

   You can add maximum five chart scripts per visualization.

## Example

This example assumes that you have created a visualization, for example a bar chart, and that you have added a dimension and a measure.

This example takes the values of the first dimension and puts them in the first measure in reverse order.

```
Let P = HCNoRows();
For J = 1 to P
Put #hc1.measure.1(J) = HCValue(#hc1.dimension.1, P - J + 1);
Next
```

## Limitations of chart level scripting

Chart level scripting cannot be used in the standard edit mode.

Chart level scripting does not work for visualizations with Chart suggestions enabled.

You can add maximum five chart scripts per visualization.

Chart level scripting is not available for the following visualizations:

- Bar charts in stacked mode

  If you have created a chart script in grouped mode and switch to stacked mode, an invalid hypercube error will be shown.
- Box plot
- Button
- Distribution plot
- Filter pane
- Line charts with two dimensions
- Pivot table
- Text & image
- Treemap
- Grid Chart (Visualization bundle)
- Trellis Container (Visualization bundle)
