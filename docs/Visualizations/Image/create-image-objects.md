---
title: "Creating image objects"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Image/create-image-objects.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating image objects

You can add an Image object to the sheet you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag an Image to the sheet.
3. In the properties panel, expand Image.
4. Under Image source, select one of the following:
   - Media library: Click ![Select image](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_image_outline.svg) to select or upload an image from the media library.
   - URL: Specify the URL containing the image you want to use.

     Information note

     To add an image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-0 "Glossary term").

     For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

After creating the image object, you can further customize its appearance in the properties panel. See the sections below.

## Creating image objects from pasted images

While editing a sheet, you can also paste an image from your clipboard to create an Image object.

- Pasting text or formatted text into an empty area of a sheet creates a Text object.
- Pasting an image into an empty area of a sheet creates an Image object.
- If clipboard content contains both text and an image, the content is created as a Text object.
- If upload is not allowed for your role or the clipboard image format is not supported, the image is not added.
- Pasting images is not supported when using an iPad.

For more information about media library uploads and permissions, see [*Uploading image files to media library*](../../MediaLibrary/MediaLibrary-upload.htm).

## Modifying the image appearance

You can change how the image appears on the sheet.

Do the following:

1. In the properties panel, expand Image.
2. Configure the following properties:
   - Image fit: Set how the image is sized. For example, you can keep it at its original size, choose various fit options, or stretch it to fit the object size on the sheet.
   - Image position: Set where the image is placed in the sheet object.
   - Rotation: Specify a number of degrees to rotate the image.
   - Mirror image: Choose whether the image is flipped along its vertical axis.
   - Repeat image: Choose whether the image should be repeated within the object if, at its current size, it does not fill the entire frame.
   - Opacity: Set the degree to which the image appears opaque or transparent.
   - Image tooltip: Define text that will display as a tooltip when users hover their cursor over the image.

## Customizing styling

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the different labels on the chart depends on chart-specific settings and label display options. These can be configured in the properties panel.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
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

- [*Image object*](image-object.htm)
