---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/
last_updated: 2026-06-11T13:33:06+02:00
---

# Visualizations

Visualizations are used to present the data that is loaded into the app. The
selections you make in the app are reflected in all associated visualizations. If
you're new to creating visualizations,
review [Choosing the right visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/creating-visualization.htm)
on Qlik Help.

This section summaries the compatibility of these visualizations across embedding
frameworks. For support for Insight Advisor,
review [Insight Advisor compatibility](https://qlik.dev/embed/nebula/render/supported-charts/).

> **Note:** Fonts from a custom theme are not supported when embedding Qlik objects cross-domain unless you use
> `<qlik-embed iframe="true">`. Using the `iframe="true"` mode may impact performance.

## Chart types and properties

### Native charts

Native charts are those built into the core Qlik Sense experience, and are accessible
via the `Charts` menu in the Qlik Sense authoring experience.

| Chart                                                                                              | analytics/sheet1 & analytics/chart1 | classic/app1 | classic/chart1 | Viz on the fly ID / `analytics/chart` type2 | Nebula ID             | Qlik Help reference                                                                                                                               |
| -------------------------------------------------------------------------------------------------- | ----------------------------------- | ------------ | -------------- | ------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Bar chart](https://qlik.dev/embed/foundational-knowledge/visualizations/barchart)                 | ✔                                   | ✔            | ✔              | `barchart`                                  | `sn-bar-chart`        | [Bar chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Bar-Chart/bar-chart.htm)                   |
| [Box plot](https://qlik.dev/embed/foundational-knowledge/visualizations/boxplot)                   | ✔                                   | ✔            | ✔              | `boxplot`                                   | `sn-boxplot`          | [Box plot](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/BoxPlot/box-plot.htm)                       |
| Bullet chart                                                                                       | ✔                                   | ✔            | ✔              | `bulletchart`                               | `sn-bullet-chart`     | [Bullet chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/BulletChart/bullet-chart.htm)           |
| Button                                                                                             | ✔                                   | ✔            | ✔              | `action-button`                             | `sn-action-button`    | [Button](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Button/button.htm)                            |
| [Combo chart](https://qlik.dev/embed/foundational-knowledge/visualizations/combochart)             | ✔                                   | ✔            | ✔              | `combochart`                                | `sn-combo-chart`      | [Combo chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/ComboChart/combo-chart.htm)              |
| [Distribution plot](https://qlik.dev/embed/foundational-knowledge/visualizations/distributionplot) | ✔                                   | ✔            | ✔              | `distributionplot`                          | `sn-distplot`         | [Distribution plot](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DistPlot/distribution-plot.htm)    |
| Filter pane                                                                                        | ✔                                   | ✔            | ✔              | `filterpane`                                |                       | [Filter pane](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/FilterPane/filter-pane.htm)              |
| [Gauge](https://qlik.dev/embed/foundational-knowledge/visualizations/gauge)                        | ✔                                   | ✔            | ✔              | `gauge`                                     | `sn-gauge`            | [Gauge](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Gauge/gauge.htm)                               |
| [Histogram](https://qlik.dev/embed/foundational-knowledge/visualizations/histogram)                | ✔                                   | ✔            | ✔              | `histogram`                                 | `sn-histogram`        | [Histogram](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Histogram/histogram.htm)                   |
| [KPI](https://qlik.dev/embed/foundational-knowledge/visualizations/kpi)                            | ✔6                                  | ✔            | ✔              | `kpi`                                       | `sn-kpi`              | [KPI](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/KPI/KPI.htm)                                     |
| [Line chart](https://qlik.dev/embed/foundational-knowledge/visualizations/linechart)               | ✔                                   | ✔            | ✔              | `linechart`                                 | `sn-line-chart`       | [Line chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/LineChart/line-chart.htm)                 |
| Map chart                                                                                          | ✖️                                  | ✔            | ✔5             | `map`                                       | `sn-map`              | [Map](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Map/Map.htm)                                     |
| Mekko chart                                                                                        | ✔                                   | ✔            | ✔              | `mekkochart`                                | `sn-mekko-chart`      | [Mekko chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Mekko-Chart/mekko-chart.htm)             |
| [Navigation menu](https://qlik.dev/embed/foundational-knowledge/visualizations/navigationmenu)     | ✔                                   | ✔            | ✔              |                                             | `sn-navigation-menu`  | [Navigation menu](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Navigation-menu/navigation-menu.htm) |
| NL Insights                                                                                        | ✔                                   | ✔            | ✔              | `sn-nlg-chart`                              |                       | [NL Insights](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/NLInsights/nl-insights.htm)              |
| [Pie chart](https://qlik.dev/embed/foundational-knowledge/visualizations/piechart)                 | ✔                                   | ✔            | ✔              | `piechart`                                  | `sn-pie-chart`        | [Pie chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/PieChart/pie-chart.htm)                    |
| [Pivot table](https://qlik.dev/embed/foundational-knowledge/visualizations/pivottable)             | ✔                                   | ✔            | ✔              | `pivot-table`                               | N/A3                  | [Pivot table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/PivotTable/pivot-table.htm)              |
| [Scatter plot](https://qlik.dev/embed/foundational-knowledge/visualizations/scatterplot)           | ✔                                   | ✔            | ✔              | `scatterplot`                               | `sn-scatter-plot`     | [Scatter plot](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/ScatterPlot/scatter-plot.htm)           |
| [Straight table](embed/foundational-knowledge/visualizations/straight-table/)                      | ✔7                                  | ✔            | ✔7             | `sn-table`                                  | `sn-table`            | [Straight table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table.htm)  |
| Tab container                                                                                      | ✔                                   | ✔            | ✔              | `container`                                 | `sn-tabbed-container` | [Tab container](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Container/container-object.htm)        |
| [Table](https://qlik.dev/embed/foundational-knowledge/visualizations/table)                        | ✔                                   | ✔            | ✔              | `table`                                     | N/A4                  | [Table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Table/table.htm)                               |
| Text & image                                                                                       | ✖️                                  | ✔            | ✔5             | `text-image`                                |                       | [Text & image](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/TextAndImage/text-image.htm)            |
| [Treemap](https://qlik.dev/embed/foundational-knowledge/visualizations/treemap)                    | ✔                                   | ✔            | ✔              | `treemap`                                   | `sn-treemap`          | [Treemap](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/TreeMap/treemap.htm)                         |
| [Waterfall chart](https://qlik.dev/embed/foundational-knowledge/visualizations/waterfall)          | ✔                                   | ✔            | ✔              | `waterfallchart`                            | `sn-waterfall`        | [Waterfall chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WaterfallChart/waterfall-chart.htm)  |
| [Write table](https://qlik.dev/embed/foundational-knowledge/visualizations/write-table)            | ✖️                                  | ✖️           | ✖️             | `writetable`                                | `sn-writetable`       | [Write table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Analyze/write-table.htm)      |

1. These refer to [qlik-embed](https://qlik.dev/embed/qlik-embed/) UI types.
2. These IDs are used as the `type` attribute when creating charts on the fly—both with
   the capability APIs and with qlik-embed's `analytics/chart` UI. They are distinct from the
   Nebula ID column, which is used for nebula.js direct development. For a full walkthrough,
   see [Create charts on the fly with analytics/chart](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-charts-on-the-fly-tutorial/).
3. See `Pivot table` in Visualization bundle for a nebula alternative, note that
   features and capabilities are different to the native chart.
4. See `Straight table` for a nebula alternative, note that
   features and capabilities are different to the native chart.
5. Requires `iframe="true"` to be added to the `<qlik-embed ...>` tag of the
   `classic/chart` object. This is needed when the object requires additional resources
   on the tenant such as map tiles, or user-uploaded images, which cannot currently be
   authenticated outside of the iframe mode.
6. Native embedding of this component requires specific page encoding. See
   [UTF-8 character encoding requirement](#utf-8-character-encoding-requirement).
7. Chart exploration is not available by default for this chart when presented in this UI type.
   Enable it by adding `preview="true"` to the `<qlik-embed ...>` tag.

### Dashboard bundle and visualization bundle charts

These visualizations enhance navigation and selection in your Qlik Sense app, but haven't yet been promoted to standard
objects. This means they may have some limitations compared to the standard objects, such as missing localization,
right-to-left support, accessibility support, or may not be supported outside of the Qlik Sense
consumption experience.

| Chart              | analytics/sheet1 & analytics/chart1 | classic/app1 | classic/chart1 | Viz on the fly support2 | Nebula ID                 | Qlik Help reference                                                                                                                                         |
| ------------------ | ----------------------------------- | ------------ | -------------- | ----------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Animator           | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-animator`           | [Animator](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/animator.htm)                         |
| Date picker        | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-date-picker`        | [Date range picker](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/date-range-picker.htm)       |
| Funnel chart       | ✔                                   | ✔            | ✔              | ✔                       | `sn-funnel-chart`         | [Funnel chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/funnel-chart.htm)             |
| Grid chart         | ✔                                   | ✔            | ✔              | ✔                       | `sn-grid-chart`           | [Grid chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/grid-chart.htm)                 |
| Layout container   | ✔4                                  | ✔            | ✔              | ✔                       | `sn-layout-container`     | [Layout container](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/layout-container.htm)         |
| Line               | ✔                                   | ✔            | ✔              | ✔                       | `sn-shape`                | [Line](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/line.htm)                                 |
| Multi KPI chart    | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-multi-kpi`          | [Multi KPI chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/multi-KPI.htm)             |
| Network chart      | ✔3                                  | ✔            | ✖️             | ✔                       | `sn-network-chart`        | [Network chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/network-diagram.htm)         |
| Org chart          | ✔                                   | ✔            | ✔              | ✔                       | `sn-org-chart`            | [Org chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/org-chart.htm)                   |
| P\&L pivot chart   | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-smart-pivot`        | [P\&L pivot chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/pl-pivot-chart.htm)       |
| Pivot table        | ✔                                   | ✔            | ✔              | ✔                       | `sn-pivot-table`          | [Pivot table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/pivot-object.htm)              |
| Radar chart        | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-radar-chart`        | [Radar chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/radar-chart.htm)               |
| Sankey chart       | ✔                                   | ✔            | ✔              | ✔                       | `sn-sankey-chart`         | [Sankey chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/sankey-chart.htm)             |
| Text               | ✔                                   | ✔            | ✔              | ✔                       | `sn-text`                 | [Text](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/text-object.htm)                          |
| Trellis container  | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-trellis-container`  | [Trellis container](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/trellis-container.htm)   |
| Variable input     | ✖️                                  | ✔            | ✔              | ✔                       | `qlik-variable-input`     | [Variable input control](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/variable-input.htm)     |
| Variance waterfall | ✖️                                  | ✔            | ✖️             | ✔                       | `qlik-variance-waterfall` | [Variance waterfall](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/variance-waterfall.htm) |
| Video player       | ✖️                                  | ✔            | ✔              | ✔                       | `sn-video-player`         | [Video player](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/video-player.htm)                 |
| Word cloud chart   | ✔3                                  | ✔            | ✖️             | ✔                       | `sn-word-cloud`           | [Word cloud chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/word-cloud-chart.htm)     |

1. These refer to [qlik-embed](https://qlik.dev/embed/qlik-embed/) UI types.
2. Viz on the fly is supported by the capability APIs.
3. Works with analytics/sheet, but not with analytics/chart.
4. When embedding a layout container, all nested charts must support analytics/chart. Charts without analytics/chart
   support won't render inside the layout container.

### Visualization extensions

Visualization extensions are supported via:

- qlik-embed:
  - `classic/app`
  - `classic/chart`, when `iframe="true"` is added to the `<qlik-embed ...>`
    tag.
- Capability APIs
- iFrame embedding APIs.

### Monitoring deprecated charts

To track when users encounter deprecated chart types in your apps, use the
[Deprecated Charts Opened UI event](https://qlik.dev/apis/ui-event/analytics/#com-qlik-v1-analytics-analytics-app-client-deprecated-charts-opened).
This event is emitted when deprecated charts are detected as users open or navigate to sheets in the native Qlik
experience or when using qlik-embed with the `classic/app` UI.

This event is available via the [Audits API](https://qlik.dev/apis/rest/audits/). The event payload includes chart IDs, types, titles,
and sheet context, enabling you to:

- Monitor deprecated chart usage across your tenant
- Plan chart migration strategies
- Track deprecation adoption

> **Note:** The event is not emitted when switching between sheet modes (View to Edit) or in non-sheet UIs (Stories, Reporting).

For a list of the deprecated objects that are detected with the event, see [Find deprecated charts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/find-deprecated-charts.htm)
on Qlik Help.

### UTF-8 character encoding requirement

Certain visualizations require UTF-8 encoding to render correctly when embedded. If your host page doesn't
specify UTF-8 encoding, users see an error message.

This applies to:

- KPI objects with `analytics/chart` (default `iframe=false` mode) or `analytics/sheet` in qlik-embed
- Charts embedded via capability APIs

If users see the following error, the host page lacks proper charset configuration:

![UTF-8 charset requirement error in qlik-embed and capability APIs](https://qlik.dev/_astro/charset-error.tBuMQwuG.png)

To resolve this issue, add the following meta tag to the host page's `<head>` section:

```html
<meta charset="utf-8">
```

If you cannot set UTF-8 encoding, use one of these workarounds:

- **qlik-embed:** Use `classic/chart` with `iframe="true"`:

```html
<qlik-embed
  ui="classic/chart"
  app-id="{app-id}"
  object-id="{object-id}"
  iframe="true">
</qlik-embed>
```

- **Capability APIs:** Embed your mashup within an iframe on a page that specifies UTF-8 encoding.
  This isolates your mashup and fulfills the charset requirement.

> **Note:** Using `iframe="true"` mode in qlik-embed or wrapping Capability API mashups in iframes may impact
> performance. The charset requirement applies only to native embedding modes that don't use iframes.
