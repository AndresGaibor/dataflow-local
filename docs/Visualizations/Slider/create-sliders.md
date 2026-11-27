---
title: "Creating sliders"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Slider/create-sliders.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating sliders

You can add a slider on the sheet you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag a Slider to the sheet.
3. Under Data > Data type in the properties panel, choose whether the slider controls [selections](#glossary-0 "Glossary term") in a Field, or if it changes Variable values.
4. Under Slider type, select one of the following:

   - Single value: The slider sets a single value or selection at a time.
   - Multi value: The slider can set value ranges, or make multiple selections at a time.
5. Depending on your configuration, choose the Data, (field) or Variable, or Variables that the slider controls.
6. Optionally, set the Number formatting for the field or variables. There are options for number, money, date, duration, custom, and expression-based number formats.

After creating the slider, you can customize it by adjusting other settings in the properties panel.

## Setting ranges and step size

For variable sliders, you can set the minimum and maximum ranges between which the values of the variables can be changed. You can also adjust the step size to customize the number of intervals between the minimum and maximum values.

For sliders with one variable, the minimum and maximum values correspond to the variable being used. For sliders with two variables, the minimum value corresponds to the variable with the lower initial value. The maximum value corresponds to the variable with the higher initial value.

Do the following:

1. In the properties panel, under Appearance > Presentation, set the Min slider range using a value or expression.
2. Set the Max slider range using a value or expression.
3. Optionally, turn Snap to step off if you want the slider to be able to smoothly move between values.
4. Adjust the Step size using a value or expression to set the intermediate ticks on the slider.
5. Set the Value label interval using a value or expression to determine the intervals at which value labels appear on the slider scale.

## Allowing manual entry of values

You can allow users to enter text into input boxes on the slider, rather than selecting or changing values by dragging.

Do the following:

1. In the properties panel, under Appearance > Presentation, turn on Manual value entry.
2. Set the Text field position property to adjust the location of the input boxes on the slider. You can set this to Auto or select a specific location.

## Customizing the slider scale

The slider scale can be customized with several settings in the properties panel.

### Value distribution

For field sliders, you can change whether the axis is continuous or discrete. For variable sliders, this setting is always set to continuous.

Do the following:

- In the properties panel, under Appearance > Presentation, set Value distribution to one of the following:

  - Continuous: Data points are separated to accurately show the distance in magnitude between each data point. Any missing values will be interpolated and shown on the axis—however, for field sliders, missing values cannot be selected with the slider. Continuous axes are useful, for example, for a time-based dimension with data that might not be measured over equal time intervals.
  - Discrete: Data points are separated by even intervals. This is useful for text-based dimensions, or for numeric or date data that is measured at even intervals.

### Setting text visibility

Expand Appearance > Presentation > Scale in the properties panel. Here, you can set:

- Show values: Choose whether to show or hide values between the minimum and maximum.
- Show min/max: Choose whether to show or hide the minimum and maximum values.

### Scale orientation

You can change between a horizontal and vertical chart orientation. This is configured under Appearance > Presentation > Orientation.

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
4. On the Chart tab, set the font, font size, and color for the Value labels.

### Customizing the slider track

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab, expand Slider Track and customize the slider track appearance:

   - Selection color: Set the color of the selected portion of the slider track.
   - Background color: Set the background color of the slider track.
   - Border color: Set the border color of the slider track.

### Customizing the manual input entry boxes

When Manual value entry is enabled on the slider, you can customize the appearance of the input value and input field boxes.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab, expand Input value and set the font, font size, and color for the input value text.
4. Expand Input field and customize the input field appearance:

   - Border color: Set the border color of the input field.
   - Background color: Set the background color of the input field boxes.

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

## Configuring sorting

For variable sliders, the sorting of slider values cannot be changed because the slider defaults to a continuous dimension axis.

For field sliders, you can change whether you want a continuous or discrete distribution (see [*Value distribution*](#ValueDist)). Similar to variable sliders, continuous value distribution does not allow custom sorting. If you choose to use a discrete value distribution, you can customize the sorting as follows.

### Automatic sorting

Leave the Sorting setting to Auto to automatically sort values.

### Custom sorting

Turn the Sorting setting to Custom to allow configuration of the following options:

- Sort by expression: Select whether to sort in ascending or descending order, and specify the expression by which to sort.
- Sort numerically: Select whether to sort by numeric value, in ascending or descending order.
- Sort alphabetically: Select whether to sort in alphabetical order, in ascending or descending order.

## Learn more

- [*Slider*](slider.htm)
