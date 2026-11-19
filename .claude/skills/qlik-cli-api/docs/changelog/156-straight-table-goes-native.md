---
source: https://qlik.dev/changelog/156-straight-table-goes-native/
last_updated: 2026-11-09T15:15:19+01:00
---

# The straight table replaces the table as the primary Qlik Sense table visualization

The straight table is now a native chart in Qlik Cloud, and is the replacement for
the [table](https://qlik.dev/embed/foundational-knowledge/visualizations/table/).

The straight table (`sn-table`) is a tabular visualization that displays data in
rows and columns. It supports one or more dimensions and measures and allows for
sorting, selections, and optional totals. You can customize styling at the dimension
and measure levels. You can also customize elements such as totals, null values,
grid, and the hover menu.

The straight table is identified as `sn-table` when in-app and embedding, and as
`straightTableV2` in theme properties.

Consider upgrading existing tables to straight tables for improved capabilities
and performance.

For more information, see:

- the [Visualization overview](https://qlik.dev/embed/foundational-knowledge/visualizations/) for embedded chart compatibility.
- the [straightTableV2 theme properties](https://qlik.dev/extend/create-custom-themes/custom-themes-properties/#straighttablev2)
  for an example of custom styling.
- the [straight table documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table.htm)
  on Qlik Help for details on usage and features.
