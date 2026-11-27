---
title: "Creating and editing sheets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/sheets-creating.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with sheets"]
---

# Creating and editing sheets

Quickly build [sheets](#glossary-0 "Glossary term") and [visualizations](#glossary-1 "Glossary term") in edit mode.

When you create a new sheet, it opens in edit mode. You can also edit an existing sheet by clicking Edit sheet. The edit mode interface helps you quickly create [charts](#glossary-2 "Glossary term") and lay them out in a sheet. You can also select prebuilt templates with charts already arranged on the sheet, and then define the data for these charts.

With edit mode's smart grid, you can quickly place new visualizations beside or below a chart and click and drag them into their final positions. You can easily create filters in your visualizations, limiting the data that displays in the charts.

Your sheets are private until you make them public. For more information, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

## Creating sheets

Do the following:

- In your application, do one of the following:

  - If you are in the application overview, click Create new sheet.
  - If you are in a sheet in analysis mode, open Sheets in the assets panel, and then click Create new sheet.
  - If you are in a sheet in edit mode, in the assets panel, select Sheets, and then click Create new sheet.

After you have created the sheet, you can:

- Choose from a number of sheet templates to arrange charts on your sheet. Sheet templates are prebuilt arrangements of charts that can help you build high-quality sheets quickly and with ease.

  For more information, see [*Building sheets using templates*](sheet-templates.htm).
- Create and arrange visualizations manually on your sheet, according to your preferences and use case.

  For more information, see [*Creating visualizations*](#CreateViz).

## Editing sheets

Do the following:

- In a sheet in your application, click Edit sheet.

## Creating visualizations

You can create visualizations in a few different ways:

- Drag and drop visualizations from Charts in that assets panel.
- Using analyses to create visualizations from analysis types.
- Create visualizations using chart suggestions

### Creating visualizations from the assets panel

Do the following:

1. In edit mode, drag the visualization from the assets panel onto the sheet or double-click the visualization.
2. Add dimensions and measures to the visualization.

   You can add dimensions and measures using the buttons on the visualization. You can also drag a [field](#glossary-3 "Glossary term") from the Fields tab of the assets panel and then select it to use it as a [dimension](#glossary-4 "Glossary term") or [measure](#glossary-5 "Glossary term"). The number of dimensions and measures that are required depends on which visualization you select.

   If you want to add expressions as dimensions or measures, click in the properties panel, under Data, click add and then click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg).
3. Adjust the presentation: for example: sorting, coloring, or labeling.

   For more information, see [*Changing the appearance of a visualization*](../Visualizations/change-appearance-of-visualization.htm).

Tip noteYou can also add a visualization by copying visualizations. This is useful if you want to use existing visualization settings in another visualization type. For more information, see [*Copying a visualization from an existing visualization*](../Visualizations/copy-visualization.htm)

Custom objects are added in a similar manner. You start creating a visualization by dragging a visualization extension onto the sheet. For more information, see [*Creating a visualization using a custom object*](../Visualizations/create-visualization-extensions.htm).

You can use tab containers to save space on your dashboard, by quickly switching between tabs with different visualizations. For more information, see [*Tab container*](../Visualizations/Container/container-object.htm).

The types of data you have in your tables and fields impacts whether they can be used as dimensions or measures.

- Dimensions determine how the data in a visualization is grouped. For example: total sales per country or number of products per supplier. For more information, see [*Data grouping with dimensions*](../Dimensions/dimensions.htm).
- Measures are calculations used in visualizations, typically represented on the y-axis of a bar chart or a column in a table. Measures are created from an expression composed of aggregation functions, such as Sum or Max, combined with one or several fields. For more information, see [*Measures*](../Measures/measures.htm).

### Creating visualizations with analyses

Analyses allow you to build visualizations by starting with a type of analysis. You then select data for the analysis to use and then the analysis generates a chart. You can then adjust analysis-specific properties and style the visualization.

In analysis mode, analyses are identical to other visualizations.

Analyses are available from Analyses in the assets panel. For more information, see [*Creating and editing analyses*](../Analyses/creating-analyses.htm).

### Creating visualizations with chart suggestions

You can turn on chart suggestions in the properties panel. When turned on, as you add or remove fields, the suggested visualization adjusts itself based on your changes. You can customize a suggested visualization with a focused set of properties.

For more information, see [*Creating visualizations using Insight Advisor chart suggestions*](../Visualizations/creating-visualization-assistance.htm).

### Defining data for visualizations added using a template

If you are using a sheet template, visualizations have already been added for you. Click Add dimension and Add measure, as needed, to populate your charts with data.

## Moving visualizations on a sheet

Do the following:

- Click and drag visualizations to reposition them on the grid.

## Resizing visualizations

You can resize visualizations in their row.

Do the following:

- Click and drag the borders of a visualization to resize it in the grid.

## Copying visualizations

You can copy and paste visualizations in the following ways:

- Using the edit bar on the sheet (![Cut](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cut.svg), ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg), and ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg)).
- By right-clicking and selecting Cut, Copy and Paste.
- With the keyboard shortcuts Ctrl+C, Ctrl+X and Ctrl+V.

Depending on what situation you are in, different things will happen when you paste a copied visualization on a sheet:

- If a visualization is selected, then the selected visualization will be replaced.
- If no visualization is selected, then the pasted visualization will be placed in the largest empty space.
- If there is no empty space, then the largest visualization on the sheet will be split in half to make space for the pasted visualization.

In edit mode, pasting content from your system clipboard can also create new objects on a sheet:

- Pasting text or formatted text into an empty area of a sheet creates a Text object.
- Pasting an image into an empty area of a sheet creates an Image object.
- If clipboard content contains both text and an image, the content is created as a Text object.
- If upload is not allowed for your role or the clipboard image format is not supported, the image is not added.
- Pasting images is not supported when using an iPad.

For more information about copying and pasting visualizations, see [*Copying a visualization from an existing visualization*](../Visualizations/copy-visualization.htm).

## Copying and pasting visualization styling

If you have applied custom styling to a visualization, you can copy its styling properties and paste them onto another visualization. For more information, see [*Copying and pasting visualization styling*](../Visualizations/style-visualization.htm#Copying).

## Converting visualizations

You can convert visualizations by clicking and dragging them onto another visualization.

Do the following:

1. While editing a sheet, drag a new chart from the assets panel onto the visualization that you want to convert.

   The shortcut menu opens.
2. Select the conversion option.

## Deleting visualizations

Do the following:

- Right-click a visualization and select Delete.

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
