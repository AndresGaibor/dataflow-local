---
title: "Visualization bundle"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/visualization-bundle.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization"]
---

# Visualization bundle

Visualizations are an important means of conveying information from massive data. The Visualization bundle is a set of charts that can be used to enhance and increase your Qlik Sense application's charting capacity.

## Visualization bundle charts

Visualization bundle charts are in the asset panel under Custom objects.

The following charts are included:

- [*Funnel chart*](funnel-chart.htm)

  A funnel chart is a visual representation of the connected stages of a linear process.

  [*Creating funnel charts*](creating-funnel-chart.htm)
- [*Grid chart*](grid-chart.htm)

  A chart that displays comparative data and with the values represented as colors.

  [*Creating grid charts*](creating-grid-chart.htm)
- [*Network chart*](network-diagram.htm)

  Creates a cluster diagram representing a graphical chart of a computer network.

  [*Creating network charts*](creating-network-diagram.htm)
- [*Org chart*](org-chart.htm)

  Creates an organization chart with a tree structure.

  [*Creating org charts*](creating-org-chart.htm)
- [*P&L pivot chart*](pl-pivot-chart.htm)

  Creates a pivot table that you can style, for example for profit and loss reporting.

  [*Creating P&L pivot charts*](creating-pl-pivot-chart.htm)
- [*Pivot*](pivot-object.htm)

  Creates a pivot table with additional styling options not available in the pivot table visualization.

  [*Creating pivot tables (Pivot)*](creating-pivot-object.htm)
- [*Radar chart*](radar-chart.htm)

  Creates a two-dimensional chart using radial axes to show the scoring of a [measure](#glossary-1 "Glossary term") in one dimension or another.

  [*Creating radar charts*](creating-radar-chart.htm)
- [*Sankey chart*](sankey-chart.htm#Sankey)

  A flow chart diagram chart visually emphasizing major transfers or flows within defined system boundaries.

  [*Creating sankey charts*](creating-sankey-chart.htm)
- [*Trellis container*](trellis-container.htm)

  Creates a trellis chart based on a master [visualization](#glossary-2 "Glossary term").

  [*Creating trellis containers*](creating-trellis-container.htm)
- [*Variance waterfall chart*](variance-waterfall.htm)

  Shows the variance between two measures over the different values of a dimension.

  [*Creating variance waterfall charts*](creating-variance-waterfall.htm)
- [*Word cloud chart*](word-cloud-chart.htm#Word)

  A cloud chart of words with their size based on measure value.

  [*Creating word cloud charts*](creating-word-cloud-chart.htm)

## Deprecated charts

These charts have been deprecated. New instances cannot be added. Existing instances will be removed from your applications in May 2027.

Tenant administrators can find deprecated Visualization bundle controls with the Deprecated charts opened in sheet system event. This event is triggered whenever a user opens an application sheet containing a deprecated chart.

For more information, see [*Finding deprecated charts*](../find-deprecated-charts.htm).

Information note

More information about deprecated charts can be found on [Qlik Community](https://community.qlik.com/t5/Official-Support-Articles/About-the-deprecation-of-Qlik-Analytics-charts/ta-p/2543997).

### Bar & area chart

New bar & area charts are no longer supported as of May 2021. If you need to configure existing instances of this chart, please refer to the last version of the documentation before support ended: [Bar & area chart - February 2021](/en-US/sense/February2021/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/bar-area-chart.htm).

### Bullet chart

Deprecated by addition of native Bullet chart. For new charts, we recommend that you use the native [Bullet chart](../BulletChart/bullet-chart.htm) instead of this object. If you need to configure existing instances of this chart, please refer to the last version of the documentation before the introduction of the native chart: [Bullet chart - August 2021](/en-US/sense/August2021/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/bullet-chart.htm).

### Heatmap chart

As of February 2022, the Heatmap extension is no longer supported. Applications that use the Heatmap extension will continue to function. If you need to configure existing instances of this chart, please refer to the last version of the documentation before support ended: [Heatmap chart - November 2021](/en-US/sense/November2021/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/heatmap-chart.htm).

### Multi KPI

The Multi KPI will no longer be available in the assets panel for creation of new charts as of April 5, 2025 on Qlik Cloud and the May 2025 version of Qlik Sense Client-Managed. It will still function on dashboards where it was previously added, but will be fully removed in May 2027 for Qlik Cloud and the May 2027 version of Qlik Sense Client-Managed.

Information note

Use instead

The old Multi KPI will be retired. Consider replacing the object with other charts and functionality. If you have not already, please explore all the new application, sheet, and chart styling settings. Do also make use of the [Layout container](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/layout-container.htm) and the [Navigation menu](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Navigation-menu/navigation-menu.htm) when replacing the functionality. If you used CSS in the past, here is a [list of native settings](https://community.qlik.com/t5/App-Development/Obsolete-CSS-modifications/td-p/2511714) you can use instead. Note also that CSS can be [applied through a theme](https://qlik.dev/extend/create-custom-themes/) or through the [sheet setting for CSS input](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/styling-sheets.htm#Customiz).

### Straight table

The straight table has become a native chart.

For information about the native straight table, see [*Straight table*](../StraightTable/sn-straight-table.htm).

## Limitations

Visualization bundle visualizations have more limitations than built-in visualizations, such as bar charts. The following limitations are valid for all visualizations from Visualization bundle:

- The user interface of the visualization is not localized to the language that Qlik Sense is using.
- Right-to-left reading order is not currently supported.
- It is not possible to edit objects from an object bundle supplied by Qlik with Dev Hub.

The following table shows which additional features are supported, or not supported, for all bundled objects.

- Printing

  Printing a visualization made in an object.
- Download

  Download as image, PDF, or Excel.
- Storytelling

  Using a [snapshot](#glossary-3 "Glossary term") of a visualization created with an object in a [story](#glossary-4 "Glossary term").
- Alternate states

  Making different [selections](#glossary-5 "Glossary term") on the same dimension, and comparing the selections in a single visualization or in two or more visualizations side by side.

Information noteExported radar charts will not include the chart legend.

Visualization bundle capability support

| Chart | Printing | Download | Storytelling | Alternate states |
| --- | --- | --- | --- | --- |
| Funnel | Yes | Yes | Yes | Yes |
| Grid chart | Yes | Yes | Yes | Yes |
| Multi KPI | No | Yes | Yes | Yes |
| Network | Yes | Yes | Yes | Yes |
| Org chart | Yes | Yes | Yes | Yes |
| P&L pivot | Yes | Yes | Yes | Yes |
| Pivot object | Yes | Yes | Yes | Yes |
| Radar | Yes | Yes | Yes | Yes |
| Sankey | Yes | Yes | Yes | Yes |
| Trellis container | No | No | No | No |
| Variance waterfall | Yes | Yes | Yes | Yes |
| Wordcloud | Yes | Yes | Yes | Yes |
