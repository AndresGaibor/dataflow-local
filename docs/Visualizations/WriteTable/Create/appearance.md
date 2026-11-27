---
title: "Customizing the appearance of a write table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/appearance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Configuring write tables"]
---

# Customizing the appearance of a write table

Under Appearance in the properties panel, you can change the functional appearance of a write table. For example, you can add a hover menu and apply text wrapping.

Other aspects of the table's appearance can be customized with styling. For more information, see [*Styling a write table*](style.htm).

Information noteThis information does not apply to editable columns in the write table. For information about customizing editable columns, see [*Creating write tables*](create.htm#Editable).

## Turning on the hover menu

Under Appearance > General, use the toggle for Show hover menu to choose whether you want the hover menu to display in the visualization.

### Showing details

Under Appearance > General, set Show details to Show if you want to allow users to be able to choose to view details, such as descriptions, measures, and dimensions.

## Allowing users to view expressions in the chart

Under Appearance > General, set Show expressions to Show if you want to allow users to be able to choose to view expressions.

## Using text wrapping

When text is too long to be displayed given the provided space, some text is not shown and instead represented with an ellipsis. Under Appearance > Presentation, you can use the settings under Multiline text wrapping to wrap the text over multiple lines in the table. This setting can be controlled individually at the header and cell levels:

- Wrap text in headers (table headers only)
- Wrap text in cells (table cells only)

Information note

The Wrap text in cells setting is not supported for editable columns in a write table.

Tip noteUp to three lines of text can be wrapped using these settings. For longer text, set a higher Row height limit in the ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling panel. See [*Customizing the grid*](style.htm#GridSettings).

## Customizing representation of null values

You can change how null values are represented for measures in the write table. Enter static text to be used to replace null values. When you use numeric values, these values are interpreted as numbers rather than text. This allows you to fill in missing calculations with actual values, such as 0.

Do the following:

1. Click Appearance > Presentation in the properties panel.
2. Under Null value text, enter the text that will replace null measure values.
