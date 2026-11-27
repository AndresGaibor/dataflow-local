---
title: "Creating treemaps"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/TreeMap/create-treemaps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating treemaps

Treemaps display hierarchical data by using nested rectangles, that is, smaller rectangles within a larger rectangle.

You can create a treemap on the [sheet](#glossary-0 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Visualizations, drag an empty treemap to the sheet.
3. Click Add dimension and select a dimension or a field. This should be the highest level in the hierarchy. It will be displayed as the main group in the chart.
4. Click Add measure and select a measure or create a measure from a field. The measure will define the size of a rectangle.
5. Add more dimensions in the order of hierarchy level . The last dimension you add defines the rectangles. The other dimensions define the grouping of the rectangles.

In a treemap you need at least one [dimension](#glossary-1 "Glossary term") and one [measure](#glossary-2 "Glossary term"), but to make full use of the treemap it is preferable to have two or three dimensions. You can only have one measure, but up to 15 dimensions. We do not recommend using more than three dimensions as the treemap may become unmanageable.

When you have created the treemap, you may want to adjust its appearance and other settings in the [properties](#glossary-3 "Glossary term") panel. For information about styling, see [*Styling the treemap*](#Styling). For information about customizing other aspects of the chart's appearance, see [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

## Styling the treemap

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the different labels on the chart depends on chart-specific settings and label display options. These can be configured in the properties panel.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font, font size, and any other applicable properties for the following text elements:

   - Header labels: Style the header labels. You can customize the font, font size, and color.
   - Leaf labels: Style the labels for the leaf elements.
   - Legend title: Style the title of the legend. You can customize the font, font size, and color.
   - Legend labels: Style the labels of the individual legend items. You can customize the font, font size, and color.

### Customizing the background

You can customize the general background and the background of the header area. The general background can be set by color and image, while the background of the header area can be set to a single color.

In the styling panel, you can configure background options.

#### Setting the general background

The general background of the chart includes the title area, as well as the chart itself, which might be partially covered by the header.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-4 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

#### Setting the header background

The header area is a branch-like frame surrounding the hierarchy of rectangles when two or more dimensions are added to the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, select a background color under Header background color.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Learn more

- [*Treemap*](treemap.htm)
- [*Displaying hierarchical data with a treemap*](treemap-example.htm)
- [Interpreting Treemaps](/lnk/Interpreting_treemaps)

Related learning:

- [Interpreting Treemaps](/lnk/Interpreting_treemaps)
