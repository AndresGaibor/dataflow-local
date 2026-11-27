---
title: "Adding trend and reference lines to visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/add-trend-and-reference-lines.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Adding trend and reference lines to visualizations

Use trend lines to visualize changes in [measure](#glossary-0 "Glossary term") values over time. Use reference lines to mark specific measure and dimension values on a chart.

## Adding trend lines to visualizations

Trend lines are available for bar charts and line charts. Trend lines are added when you configure a [measure](#glossary-1 "Glossary term") in the chart.

For more information about trend lines, see [*Trend lines*](../Measures/trend-lines.htm).

Do the following:

1. Click on an existing bar or line chart.
2. In the properties panel, expand the Data section.
3. Under Measures, expand the measure for which you are adding trend lines.
4. Under Trend lines, click Add trend line.
5. Define the Label and Type for the trend line.
6. Use the Colors slider to define Custom or Auto coloring.
7. Use the Dashed checkbox to give the line a dashed or solid appearance.

## Adding reference lines to visualizations

Reference lines can help users interpret a visualization, providing guidance on what to look for during analysis. Reference lines are separately defined for measures and dimensions.

For more information about reference lines, see [*Reference lines*](reference-lines.htm).

### Adding reference lines for chart measures

Do the following:

1. Click on an existing chart that supports reference lines.
2. In the properties panel, expand the Add-ons section.
3. Expand one the following sections depending on your chart type and data:

   - Reference lines: Applicable to most chart types that support reference lines.
   - Primary axis reference lines and Secondary axis reference lines: Applicable to combo chart with data on multiple axes.
   - X-axis reference lines and Y-axis reference lines: Applicable to scatter plot. For more information about configuring scatter plot reference lines, see [*Adding reference lines*](ScatterPlot/create-scatter-plots.htm#RefLines).
4. Click Add reference line.
5. Optionally, define a Show condition and Label.
6. Under Reference line expression ,enter the expression to define the measure value for which the reference line is shown.
7. Style the reference line with the Color, Line type, and Colored background settings.

To remove an existing reference line, expand the reference line and click Delete.

### Adding dimensional reference lines

Do the following:

1. Click on an existing chart that supports dimensional reference lines.
2. In the properties panel, expand the Add-ons section.
3. Expand Dimension reference lines.
4. Click Add reference line.
5. Optionally, define a Show condition and Label.
6. Under Dimension value, enter the expression to define the dimension value for which the reference line is shown.
7. Style the reference line with the Alignment, Color, Line type, and Colored background settings.

To remove an existing dimensional reference line, expand the reference line and click Delete.
