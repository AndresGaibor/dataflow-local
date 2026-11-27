---
title: "Assigning colors to master dimension values"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Colors/assigning-colors-to-dimension-values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Editing visualizations", "Assigning colors to master items"]
---

# Assigning colors to master dimension values

You can assign colors to the distinct values contained in a master [dimension](#glossary-0 "Glossary term"). This ensures that the distinct values of your dimensions use the same colors in all [visualizations](#glossary-1 "Glossary term").

Colors assigned to values are used when you choose to color By dimension and have Library colors enabled. If you choose to color by Single color, the master dimension's color is used instead.

Assigning colors to master dimension values has the following limitations:

- A maximum of 100 colors can be assigned to a dimension's values.
- Dimension values cannot be longer than 1024 characters. Longer values are disabled in the list of values.
- Drill-down and cyclic dimensions do not support assigning colors to dimension values

Warning note

Do not assign colors to master dimension values if you use section access or work with sensitive data, because the values might be exposed by the color configuration.

The Value colors section of Edit dimensions contains the options for assigning colors to a dimension's distinct values. You can search the list of values with ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg).

Qlik Sense automatically applies an auto fill to your values to provide a default color. The auto fill is either a single color or a color scheme. Changing your auto-fill settings will not change colors you have assigned to values.

In addition to distinct values, you can set colors for the values classified as others in a visualization, that is, the collection of distinct values that fall outside the displayable values in a dimension. You can also set colors for null values.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click Master items.
3. Select a master dimension from your library.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
5. Click Value colors.
6. If you want to change the auto fill settings, set Auto fill to Custom , select the auto fill method, and either select a single color or color scheme.
7. Select a value and do one of the following:

   - Select a color in the color wheel, and optionally adjust the saturation slider.
   - Type a 6 character color code in the Hex input field: #.

   Values assigned colors display the ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) icon.
8. If you want to remove an assigned color, select the value and click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).
9. Optionally, to assign a color to Others or Null values, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) and do one of the following:

   - Click one of the colors in the palette.
   - Type a 6 character color code in the Hex input field: #.
   - Click ![Show options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) at the bottom of the dialog, select a color in the color wheel, and optionally adjust the saturation slider.
10. Click Save.
