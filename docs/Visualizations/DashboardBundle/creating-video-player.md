---
title: "Creating video players"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/creating-video-player.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating video players

The video player lets you play videos in different formats from external sources. It is included in the Dashboard bundle. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

You can add video player object to a [sheet](#glossary-0 "Glossary term") that you are editing. Add or paste a video link into the video object. The video is streamed from a source; it is not uploaded to Qlik Sense. By default, the video format of the link will be auto-detected, the video will not auto-play, and video controls will be available to application consumers.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag a Video player object to the sheet.
3. Add a video as a URL in the video player object field Add URL, or in the properties panel under Video > URL. You can format the URL field as an expression.
4. Autodetect format is default setting and it will adjust accordingly based on the URL. You can also turn off Autodetect, and then select the correct supported video format.

Once you have added the video, you may want to adjust its options.

## Setting video options

Video options are set in the Properties pane.

Click Auto play if you want the video to automatically start when viewed in analyzer mode. Auto play is turned off by default. When Auto play is selected, the video starts but it is muted. The application user has to select Unmute to turn the sound on.

Click Hide Controls to turn off video controls in analyzer mode. By default, video controls are visible.

You can add a Poster image. By default, the poster image is turned off. For Source, select an external URL that directs to an image, or add an image from your media library.

If a poster image is selected, the selected image is displayed before the video starts playing. Poster alignment specifies how the poster image will align inside the video player.

You cannot play the video in edit mode. The video restarts when you switch between analyzer mode and edit mode.

In analyzer mode, you start the video with the play button. You can pause, switch between mute and unmute, and view the video in full screen. You can also share the video player object, and Take snapshot.

In edit mode, the right-click context menu provides options for Qlik Sense. In analyzer mode, the context menu provides options for YouTube.

The application developer (edit mode) or application consumer (analyzer mode) must allow YouTube videos to play in Qlik Sense.

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

## Limitations

The video player has the following limitations:

- Safari does not support OGG and WEBM formats.
- iPhone adds native video controls. It does not use video player controls, therefore Hide Controls will not turn off controls.
- Android does not support OGG format.
- When exporting or printing a sheet that includes a video player object, the video player object will not be included.

## Video player allowlist examples

The following table provides allowlist examples for the video player. For more information, see [*Managing Content Security Policy (CSP)*](../../Admin/mc-administer-content-security-policy.htm).

Video player allowlist examples

| Name | Origin | Directive |
| --- | --- | --- |
| video-play-test-mp4 | file-examples-com.github.io | media-src |
| wiki img src | upload.wikimedia.org | img-src, media-src |
| YouTube - No cookies | www.youtube-nocookie.com | child-src, font-src, frame-ancestors, frame-src, img-src, media-src, script-src, worker-src |
| YouTube | www.youtube.com | child-src, font-src, frame-ancestors, frame-src, img-src, media-src, script-src, worker-src |
| YouTube - img | img.youtube.com | img-src |
| webm | dl5.webmfiles.org | img-src, media-src |

Related learning:

- [How do I configure a Dashboard Bundle Video Player?](/lnk/How_configure_dashbundle_video)
