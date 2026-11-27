---
title: "Creating Text objects"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/creating-text-object.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating Text objects

Text objects complements other visualizations by offering options to add text, images, hyperlinks, and [measures](#glossary-0 "Glossary term"). Text is included as a part of the Dashboard bundle. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

You can create a Text on the [sheet](#glossary-1 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag a Text to the sheet,
3. Click Text to open the editing toolbar.
4. Add and format text, tables, hyperlinks or measures to Text.

Tip noteIf you double-click a Text in the assets panel, it is added to the sheet immediately.

### Creating Text from pasted clipboard content

While editing a sheet, you can paste clipboard content directly into an empty area to create a Text object.

- Plain text and formatted text can be pasted into a new Text object.
- Hyperlinks in pasted formatted text are kept when available.

Consider the following additional details:

- Pasting text or formatted text into an empty area of a sheet creates a Text object.
- Pasting an image into an empty area of a sheet creates an Image object.
- If clipboard content contains both text and an image, the content is created as a Text object.
- If upload is not allowed for your role or the clipboard image format is not supported, the image is not added.
- Pasting images is not supported when using an iPad.

### Styling and formatting text in Text

Text offers several editing and formatting options for text. You can format your text using several styles:

- Paragraph
- Quote
- Heading 1
- Heading 2
- Heading 3
- Unordered list
- Ordered list

You can also select font families and size. You can apply emphases to your text and change text color. You can also add hyperlinks.

### Styling and formatting tables in the Text

You can insert tables into Text from the toolbar. You can resize column and rows and hide borders. You can insert additional tables inside table cells.

### Styling Text

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs. You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

#### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote

#### Customizing the background

You can customize the background of the chart. The background can be set by color and image.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-2 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

#### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

### Configuring layout behavior

You can customize how content in the Text object is scaled based on factors such as browser and chart width.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, under Layout behavior, select one of the following settings:

   - Fluid: Content is scaled based on the width of the Text object.
   - Responsive: Content is scaled based on browser size.
   - Fixed: Content is not scaled.

### Creating a link

You can mark a text section and use it for a link.

Do the following:

1. Select the text section that you want to use for the link.
2. Click ![Create link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) in the editing toolbar to open the link dialog.
3. Enter the web address that you want to link to.
4. Click ![Check mark](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg).

### Removing a link

You can remove a link from a text section.

Do the following:

1. Click the link so that the cursor is somewhere inside it.
2. Click ![Create link](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg).

The link is removed, but not the text.

### Adding an image

You can add an image through the editing toolbar.

Do the following:

1. Double-click the text object to open the editing toolbar.
2. Click ![media library](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg).
3. The Media library opens.

The following formats are supported: .png, .jpg, .jpeg, and .gif.When using Qlik Sense in Qlik Cloud, you upload images to the In app folder in the media library.

4. Select the image that you want to add.
5. Click Insert.

### Adding a measure

You can add a measure in the following ways:

- By dragging a [field](#glossary-3 "Glossary term") from the assets panel and adding it as a measure.
- By dragging a measure from Master items.
- By adding a measure (existing or new) from the properties panel.

When you are editing the measure, it is displayed as a value with a grey background, which can be styled and moved around in the visualization. You can also apply number formatting to it. When you leave the editor, the measure value is displayed . Values that cannot be aggregated are shown as a hyphen (-).

### Deleting a measure

You can delete a measure in the following ways:

- Place the cursor before the token and press Delete.
- Place the cursor after the token and press Backspace.
- In the properties panel, right-click the measure and select Delete in the dialog.
- In the properties panel, click the measure and click Delete ![Trash bin](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).
