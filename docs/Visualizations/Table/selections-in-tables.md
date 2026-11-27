---
title: "Selections in tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Table/selections-in-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Legacy", "Table"]
---

# Selections in tables

You can make [selections](#glossary-0 "Glossary term") in a table by clicking or drawing in the [dimension](#glossary-1 "Glossary term") columns.

Information note

The Straight table has replaced the Table as the default table visualization. Consider upgrading existing tables to straight tables for improved functionality and performance. For information about the straight table, see [*Straight table*](../StraightTable/sn-straight-table.htm).

Measure values cannot be selected. When you make a selection, it is always the dimension values that you select. You can only make selections in one column at a time.

Table with three selected fields in the dimension Customer.

![Table with selected fields in a dimension.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_TableSelection.png "Click to view full size")

To deselect a row, click it. To confirm a selection, click ![Checkmark ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) or click outside the visualization. You can also press Enter. To cancel, click ![Cancel selection](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) or press Esc. If you confirm, the selection is reflected in all visualizations associated with the table.

You cannot select dimension values that are null. Null values in a table are presented as dashes (-). Rows without valid dimension values will not be included in the selection.

## Learn more

- [*Exploring data with visualizations*](../../Selections/make-selection.htm)
