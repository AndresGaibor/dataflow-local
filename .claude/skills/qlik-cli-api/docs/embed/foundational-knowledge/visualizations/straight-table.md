---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/straight-table/
last_updated: 2025-12-10T10:53:56+01:00
---

# Straight table

The straight table (`sn-table`) is a tabular visualization that displays data in
rows and columns. It supports one or more dimensions and measures and allows for
sorting, selections, and optional totals.

The table is commonly used to show detailed records, especially when users want
to scan or export data, or compare values across multiple fields.

Use a straight table when you want to view detailed data and precise values rather
than visualizations of values. You can search and filter on dimensions
and sort the table by dimensions and measures.

## Chart exploration mode

When enabled by the app creator, chart exploration allows users to interactively
add or remove columns, sort, resize, and make selections - all without changing
the original table for others.

Changes are session-specific and personal, but can be saved as public bookmarks.
The exploration panel is not shown in downloaded or shared versions of the table.

In the `analytics/sheet` and `analytics/chart` UI types, chart exploration is
available as a preview feature. Enable it by adding `preview="true"`
to the `<qlik-embed ...>` tag.

## Additional references

For more information about the Straight Table, see
[Straight Table documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table.htm)
on the Qlik help site.
