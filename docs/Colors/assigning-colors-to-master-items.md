---
title: "Assigning colors to master items"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Colors/assigning-colors-to-master-items.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations"]
---

# Assigning colors to master items

You can assign colors to your [master items](#glossary-0 "Glossary term"). Colors assigned to master [dimensions](#glossary-1 "Glossary term") and master [measures](#glossary-2 "Glossary term") persist across all instances of those master items in all [visualizations](#glossary-3 "Glossary term").

If you change the color used for the master item, the color will be updated across all instances of that master item. Optionally, master item colors can be disabled for individual visualizations.

Visualizations use master dimension colors when Single color is selected in the Colors and legend section of the visualization [properties](#glossary-4 "Glossary term") panel. Master measure colors are used when Single color or Multicolored are selected in the Colors and legend section of the visualization properties panel.

By default, if a visualization's default Auto settings use the Single or Multicolored, master item colors will be applied automatically. If they do not, you must switch to Custom and select a supported setting. Master item colors can be disabled in individual visualizations.

In a visualization with colors specified for both master dimension and master measure, Qlik Sense defaults to the master dimension color. Master measure colors can be applied using the Use library colors drop-down and selecting Measure in the Colors and legend section of the visualization properties panel. In visualization with a mix of master measures with assigned colors and measures without assigned colors, the other measures will use the default palette colors.

Master dimensions can have colors assigned to their distinct values. For more information, see [*Assigning colors to master dimension values*](assigning-colors-to-dimension-values.htm).

Master measures can have custom color gradients applied to their values in visualizations. For more information, see [*Assigning colors to master measure values*](assigning-colors-to-measure-values.htm).

When assigning colors to your master items, you have the following options:

- Choose a color from the default palette
- Type a hexadecimal color code
- Choose a color using advanced color options

## Assigning a color from the default color palette

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click Master items.
3. Select a master item from your library.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
5. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop-down.
6. Select one of the colors in the palette.
7. Click outside the dialog.
8. Click Save.

The color dialog with the default color palette and a blue color selected.

![Default color palette.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_DefaultColorPalette.png "Click to view full size")

## Assigning a color using a hexadecimal color code

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click Master items.
3. Select a master item from your library.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
5. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop-down.
6. Type a 6 character color code in the input field: #.
7. Click outside the dialog or press Enter.
8. Click Save.

## Assigning a color using advanced color options

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click Master items.
3. Select a master item from your library.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
5. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) in the color drop-down.
6. Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog.

   The dialog displays the advanced options.
7. Select a color in the color wheel.

   The selected color changes and the Hex color code updates accordingly.
8. Optionally, adjust the color saturation using the slider.

   The saturation changes and the Hex color code updates accordingly.
9. Click outside the dialog.
10. Click Save.

The color dialog with the color wheel in the advanced options and a blue color selected.

![Color wheel.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_AdvancedColorOptions.png "Click to view full size")

## Learn more

- [*Coloring a visualization*](color-a-visualization.htm)
