---
title: "Animator"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/animator.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects"]
---

# Animator

The animator control (Animator) animates the changes in values in your [visualizations](#glossary-0 "Glossary term") over a range of values. For example, you could view changes in your visualizations over a period of time.

Information noteAnimator is included as a part of the Dashboard bundle Dashboard bundle objects have additional limitations and may not have the same supports as other visualizations. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

The animator control adds a button and progress slider to the [sheet](#glossary-1 "Glossary term"). When pressed, animator cycles through the values of its [dimension](#glossary-2 "Glossary term"). Users can use the slider to manually pick values from the dimension to display.

Animator

![Animator extension](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_animator_rev.png "Click to view full size")

## When to use the animator

The animator is useful when you want to see your visualizations change over a specified range, such as over a period of time. For example, you could use the animator control to view how visualizations in your sheet change month to month over a period of a year. Animator can be used to animate any dimension values. You could, for example, animate how your sales visualizations change city to city by selecting a dimension containing city vales to use with animator.

The [selections](#glossary-3 "Glossary term") animator makes while running through values are applied to your current selections.

## Creating animators

You can create an animator on the sheet you are editing. The dimension you select to use with animator contains the range of values you want animated. By default, every value in the dimension will be used as a step. You can customize the number of steps used in the animation as well as how quickly animator moves between steps. Animator runs through dimension values by the order in Sorting.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag a Animator object to the sheet.
3. Select a field to add as the dimension.

Once you have created the animator, you may want to adjust its animation options and other settings.

## Setting animator options

Animator options are set in Animator Options in the Properties pane.

You can control how fast an animator transitions between values in the selected dimension in Time Between Steps. Time Between Steps requires values be set in milliseconds.

Information note

It is not recommended to set Time Between Steps lower than 300 milliseconds.

You can set the total steps the animator runs through in Total Steps. The animator will divide the total steps evenly across the dimension values. For example, if there are 10 values in the time dimension selected and Total Steps is set to 5, animator will go to values 2, 4, 6, 8, 10). If Total Steps is set to 0, the animator will use every value.

If you want the animation to show the total building over time for your selected values, select Aggregate. When Aggregate is selected, each step is aggregated to the previous step.

By default, the animator will run through steps in a loop. You can control this with the Loop option.

You can control whether or not the dimension and current value displays in the animator as it runs with Show Dimension Label and Show Dimension Value.

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

Animator has the following limitations:

- Animator does not support drill-down dimensions as the dimension.
- Animator does not support animating trellis charts.
- An animator can have a maximum of 1000 steps.

Related learning:

- [How do I configure a Dashboard Bundle Animator object?](/lnk/How_configure_Dashboard_Bundle_Animator_object)
