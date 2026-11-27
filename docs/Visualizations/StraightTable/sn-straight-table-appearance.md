---
title: "Customizing straight table appearance and navigation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table-appearance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating straight tables", "Configuring straight table properties"]
---

# Customizing straight table appearance and navigation

Under Appearance in the properties panel, you can change the functional appearance of a straight table. For example, you can add a hover menu, apply text wrapping, and set accessibility options.

Other aspects of the straight table's appearance can be customized with styling. For more information, see [*Styling a straight table*](sn-straight-table-style.htm).

## Managing accessibility settings

The straight table has several accessibility enhancements, which you can turn on in the properties panel under Appearance > Presentation > Accessibility options. Consider turning both settings on for optimal accessibility.

### Use pagination

With the Use pagination setting, change how many rows are displayed in the chart at a time. With pagination, instead of displaying all rows at once, only a certain amount of rows are displayed. Users can use the arrow buttons at the bottom of the table to navigate.

### Increased accessibility

The Increased accessibility setting simplifies column header interaction so that clicking a header opens a menu with sorting, search, and selection options. This improves table accessibility and enhances screen reader support.

Increased accessibility is turned off by default in new straight tables. The table below outlines the differences between having the setting on or off.

Information noteKeyboard navigation and selections work the same whether or not this setting is turned on. For keyboard controls, see [*Keyboard navigation and shortcuts in apps*](../../UserInterface/keyboard-navigation-and-shortcuts.htm#Accessibility).

Comparison of Increased accessibility options in straight tables

| User action | How the action is done (Increased accessibility on) | How the action is done (Increased accessibility off) |
| --- | --- | --- |
| Sort column | User clicks a column header and selects a sort option. | User clicks a column header one or more times. |
| Search in column | User clicks column header and selects the search option. | User clicks Search icon in column header. |
| Change cyclic dimension values | User clicks column header and selects the option to change dimension value. | User clicks Cyclic group icon in column header. |

## Turning on the hover menu

Under Appearance > General, use the toggle for Show hover menu to choose whether you want the hover menu to display in the visualization.

### Showing details

Under Appearance > General, set Show details to Show if you want to allow users to be able to choose to view details, such as descriptions, measures, and dimensions.

## Allowing users to view expressions in the chart

Under Appearance > General, set Show expressions to Show if you want to allow users to be able to choose to view expressions.

## Using text wrapping

When text in the straight table is too long to be displayed given the provided space, some text is not shown and instead represented with an ellipsis. Under Appearance > Presentation, you can use the settings under Multiline text wrapping to wrap the text over multiple lines in the table. This setting can be controlled individually at the header and cell levels:

- Wrap text in headers (table headers only)
- Wrap text in cells (table cells only)

Tip noteUp to three lines of text can be wrapped using these settings. For longer text, set a higher Row height limit in the ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling panel. See [*Customizing the grid*](sn-straight-table-style.htm#GridSettings).

## Customizing representation of null values

Null values can be customized in the styling panel. See [*Customizing null values*](sn-straight-table-style.htm#Nulls).

## Hiding the column header

You can hide the header at the top of the straight table that displays column titles and allows user to change the sorting. Under Appearance > Presentation, activate the Hide header setting.

## Learn more

- [*Best practices for designing accessible applications*](../../Apps/accessibility-analytic-apps.htm)
