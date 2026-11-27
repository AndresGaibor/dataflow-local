---
title: "Creating text & image objects"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/TextAndImage/create-text-image-objects.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating text & image objects

The text & image object complements other [visualizations](#glossary-0 "Glossary term") by offering options to add text, images, hyperlinks, and [measures](#glossary-1 "Glossary term").

You can format and color the text and align the paragraphs. The background image has sizing and positioning options. You can also set the responsive behavior for text and images.

Information note

The text & image visualization is only available in the advanced edit mode.

You can create a text & image visualization on the [sheet](#glossary-2 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts and under Legacy, drag a Text & image to the sheet.
2. Click the text & image [chart](#glossary-3 "Glossary term") to open the editing toolbar.
3. Add and format text, images, hyperlinks or measures to the text & image chart.

Tip noteIf you double-click a text & image chart in the assets panel, it is added to the sheet immediately.

## Styling the text & image object

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

### Customizing the background

You can customize the background of the chart. The background can be set by color and image.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the origin must be added to the allowlist in your tenant's Content Security Policy. Add the origin with the img-src directive. This is done in the Administration activity center by an administrator.

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

In a text & image object, you can also set a background image outside of the styling panel. Setting a background image in this way will not exclude or negate any background modifications you have made in the above procedure.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Background image, toggle on Use background image.
3. Add an image from your media library. You can select from a number of size and position options.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Creating a link

You can mark a text section and use it for a link.

If you do not add a prefix, http:// is added automatically, assuming that you are adding a web address.

Do the following:

1. Select the text section that you want to use for the link.
2. Click ![Create link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) in the editing toolbar to open the link dialog.
3. Enter the web address that you want to link to.
4. Click anywhere outside the URL editor.

## Removing a link

You can remove a link from a text section.

Do the following:

1. Click the link so that the cursor is somewhere inside it.
2. Click ![Create link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) in the editing toolbar to open the link dialog.
3. Click ![Trash bin](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).

The link is removed, but not the text.

## Adding an image

You can add an image through the editing toolbar. You can use one of the default images, or an image of your own.

Do the following:

1. Click ![media library](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) in the editing toolbar.

   The Media library opens.

   The following formats are supported: .png, .jpg, .jpeg, and .gif.When using Qlik Sense in Qlik Cloud, you upload images to the In app folder in the media library.
2. Select the image that you want to add.
3. Click Insert.

Information noteIn the [properties](#glossary-4 "Glossary term") panel, you can add a background image, which, for example, can be used when you want to insert text in the image. The images added through the editing toolbar are not background images.

## Adding a measure

You can add a measure in the following ways:

- By dragging a [field](#glossary-5 "Glossary term") from the assets panel and adding it as a measure.
- By dragging a measure from Master items.
- By adding a measure (existing or new) from the properties panel.

When you are editing the measure, it is displayed as a token, which can be styled and moved around in the visualization. You can also apply number formatting to it. When you leave the editor, the measure value is displayed . Values that cannot be aggregated are shown as a hyphen (-).

## Deleting a measure

You can delete a measure in the following ways:

- Place the cursor before the token and press Delete.
- Place the cursor after the token and press Backspace.
- In the properties panel, right-click the measure and select Delete in the dialog.
- In the properties panel, click the measure and click Delete![Trash bin](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).

## Learn more

- [*Text & image*](text-image.htm)
