---
title: "Creating filter panes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/FilterPane/create-filter-panes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating filter panes

You can add a filter pane to control what data that is shown in the [visualizations](#glossary-0 "Glossary term") on a [sheet](#glossary-1 "Glossary term"). A filter pane can filter the data of several [dimensions](#glossary-2 "Glossary term") at once.

You can create a filter pane on the sheet you are editing.

In a filter pane you can use up to 1000 dimensions.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty filter pane to the sheet.
3. Click Add dimension and select a dimension or a field.
4. If you want to add more dimensions, click Add dimension again.

When you have created the filter pane, you may want to adjust its appearance and other settings in the [properties](#glossary-3 "Glossary term") panel:

- [*Styling the filter pane*](#Styling)
- [*Customizing individual listboxes in a filter pane*](#Configuring)

Tip noteIf you double-click or drag a [field](#glossary-4 "Glossary term") or a dimension from the assets panel, a filter pane is added to the sheet using the dimension. If you then double-click more dimensions, they are automatically added to the new filter pane.

## Styling the filter pane

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the Filter pane and Listboxes tabs. Settings on the Filter pane tab applies styling for the filter pane and settings on the Listboxes tab applies styling for all listboxes inside the filter pane.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles in both Filter pane and Listboxes.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the different labels on the chart depends on chart-specific settings and label display options. These can be configured in the properties panel.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Filter pane tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Listboxes tab, set the font, emphasis style, font size and color for the following text elements:

   - Header: Style the text of the headers for the listboxes.
   - Content: Style the text of the listbox values.

     Click the checkbox for Auto contrast color to automatically override the selected color with colors that have higher contrast with the selection state of the listbox value.

### Customizing the background

You can customize the filter pane background, the background of the header area, as well as the background of the listboxes. The filter pane and the listbox background can be set by color and image, while the background of the header area can be set to a single color.

In the styling panel, you can configure background options.

#### Setting the filter pane background

The filter pane background of the chart includes the title area, as well as the filter pane itself, which is partially covered by the listboxes.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palettee](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Filter pane tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-5 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

#### Setting the listbox background

You can style the background of the listboxes. This styling applies to all listboxes in the filter pane.

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Listboxes tab of the styling panel, you can select a background color (single color or expression), and also set the background to an image from your media library.

   When using a background image, you can adjust image sizing and position.

#### Setting grid cell backgrounds (image representation only)

If you are using images rather than text to show field values in listboxes, you can also customize the background of the individual grid cells. For more information, see [*Representing field values as images*](#Representation).

### Coloring the selection states

Each selection state of a listbox value can be assigned a specific color. This coloring is applied to the background of the listbox value.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Listboxes tab of the styling panel, under Selection state, set colors for each of the selection states:

   - Selected
   - Alternative
   - Excluded
   - Selected excluded
   - Possible

### Customizing the borders and shadow

You can customize the borders and shadow around the entire filter pane, as well as the borders around the listboxes within it.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Filter pane tab of the styling panel, you can customize the border and shadow around the entire chart:

   1. Under Border, adjust the Outline size to increase or decrease the border lines around the chart.
   2. Select a color for the border.
   3. Adjust the Corner radius to control the roundness of the border.
   4. Under Shadow, select a shadow size and color. Select None to remove the shadow.
4. On the Listboxes tab of the styling panel, you can customize the borders around the listboxes:

   1. Under Listbox border, click the color picker for Border color.
   2. Use the sliders to set border color and opacity.

## Customizing individual listboxes in a filter pane

A filter pane can contain one or more listboxes to filter dimension values over specified fields. Add fields to the filter pane, then re-arrange them in the properties panel in an order that meets your preferences.

Each field in the filter pane has its own listbox, which shows the individual field values. Each listbox in a filter pane can be customized with its own unique properties.

Do the following:

1. Create a filter pane on a sheet.
2. Add a field to the filter pane to create a new listbox for that field.
3. In the properties panel, under Data, click the field you just added.

This expands the Listbox properties panel, where you can customize the design of the listbox.

Listbox properties panel for a single listbox in a filter pane.

![Listbox properties for a single listbox in a filter pane.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_filter_pane_listbox_properties.png "Click to view full size")

### Configuring search options

In Listbox properties, you can choose whether or not users can search for individual field values in each listbox within the filter pane. You can also switch the default Search mode from Normal to Wildcard. Wildcard adds default wildcard symbols (\*) to the search field.

### Condensing information in the filter pane

There are multiple settings available in Listbox properties to help you customize how much space each listbox occupies in the filter pane.

#### Enabling compact view

To remove space between each dimension value, select the Compact view checkbox under Presentation.

#### Adjusting the collapse behavior

You can adjust whether the listbox is shown as expanded or collapsed in the filter pane. When a listbox is collapsed, you can click to expand it temporarily to view and apply selections.

Regardless of the collapse behavior selected, the exact behavior of each listbox within a filter pane depends on a number of factors. These include its configuration in relation to other listboxes in the filter pane, and available space. For more information, see [*Display limitations*](filter-pane.htm#Display).

To adjust the collapse behavior, select an option in the Collapse listbox drop down menu. This is located under Presentation.The following options are available:

- Auto: The listbox automatically adjusts to be expanded or collapsed, based on available space and configuration in relation to other listboxes in the filter pane. The listbox defaults to this option.
- Always: The listbox always collapses. It might be placed inside the drop down menu for additional dimensions.
- Never: The listbox never collapses. It might still be placed inside the drop down menu for additional dimensions.

### Changing selection behavior

You can adjust several different settings in Listbox properties to customize how selections are made in the listbox.

#### Enabling checkbox mode

If you select Checkbox mode under Presentation in Listbox properties, the listbox switches to a view where each dimension value is represented by a checkbox. In this mode, [selections](#glossary-6 "Glossary term") are made by clicking the checkbox next to each item, rather than the default behavior allowing clicking and dragging to select multiple values at once.

If you have applied Always one selected value for the field within the assets panel, radio buttons are used instead of checkboxes. The functionality is the same.

#### Toggling selection toolbar

By default, a selection toolbar appears when you make selections in a listbox. This toolbar allows you to explore other options for selections, as well as clear, cancel, or confirm the selections.

In Listbox properties, the Show selection toolbar checkbox is checked by default. Clear this checkbox if you want the toolbar not to appear above the listbox when you make selections.

If you toggle this setting off, selections are confirmed when you press Enter or click outside the listbox.

### Displaying dimension value frequencies

Under Presentation in Listbox properties, click the checkbox next to Histogram to display bars underneath each dimension value to represent how frequently each value appears in the data.

### Switching to grid layout

By default, a listbox for a field in a filter pane is set to show data in a single column. Alternatively, you can show data in a grid layout. Under Presentation, in Listbox properties, switch the parameter for Show data in from Single column to Grid.

In the grid layout, you can also configure how the data is ordered (by Row or Column), and customize the maximum visible rows or columns in the grid.

Information noteWhen representing fields as images rather than text, it is not possible to switch between single-column and grid modes. However, the filter pane does display images in a grid, with a different set of properties available to set.  See [*Representing field values as images*](#Representation).

### Representing field values as images

By default, the listbox shows field values as text. You can alternatively show field values as images instead. To represent field values as images, expand Presentation in the Listbox properties, and set Representation from Text to Image.

Information note

For filter panes that show field values as images, the Qlik Analytics mobile app displays the image URLs only, rather than the images themselves.

When configured to show values as images, listbox presentation properties are different than the default Text properties. Details are described below:

- Filter pane images come from URLs. With Image setting, you can decide where the URL comes from:

  - Dimension value: Uses the Field for the listbox as the source of the image URLs. You can also define an Image label separately.
  - Add URL: Specifies image URLs in a separate property, Image URL. You can enter a field or custom expression to define the URL.

    Information noteThis property also is used as the label if you decide to show text alongside the images.

  Information note

  To use an image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-7 "Glossary term").

  For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).
- Set custom subtitles and tooltips with Image subtitle and Image tooltip.
- Turn Show selected values on to only show image values that have been selected in the application. If left off, all images are shwon but non-selected image values are grayed out.
- You can set how images are displayed within the listbox grid with:

  - Sizing
  - Position
  - Max visible columns and Max visible rows (similar to grid setting for default text values. See [*Switching to grid layout*](#Grid).)
  - Grid gap in percentage
- Turn Show text on or off to show or hide text labels for each image. When turned on, you can adjust the text labels by:

  - Setting their position.
  - Setting whether or not they have a white Text background distinct from the cell background.
- Further manage the look and feel of grid cells that contain the images. You can set:

  - Cell background color: Set a background color for the cell (not including the outline). You can color cells with a single color, or define color using an expression or selection state.
  - Outline: Optionally choose to show an outline around the cell, and choose its width, color, and corner radius.
  - Outline color: Set a background color for the outline. You can color cells with a single color, or define color using an expression or selection state.

### Showing the frequency of values

You can show the frequency next to each value, either as an absolute number or as a percentage. You select this by opening Listbox properties, expanding the Presentation section, and selecting an option in Show frequency.

Information noteIn some cases the frequency cannot be calculated and is displayed as -. One example of this is for key fields.

## Showing the hover menu

By default, the hover menu is not displayed on filter panes. You can enable the hover menu if needed.

Do the following:

1. In edit mode, select the filter pane.
2. In the properties panel, go to Appearance > General.
3. Turn on Show hover menu.

## Learn more

- [*Filter pane*](filter-pane.htm)
- [*Exploring with selections*](../../Selections/SelectionsToolbar/work-with-selections.htm)
- [Interpreting Filter Panes](/lnk/Interpreting_filter_panes)

Related learning:

- [Interpreting Filter Panes](/lnk/Interpreting_filter_panes)
