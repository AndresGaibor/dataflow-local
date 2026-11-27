---
title: "Creating trellis containers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-trellis-container.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating trellis containers

You can use the Trellis container to show a trellis chart based on a master [visualization](#glossary-0 "Glossary term"). The trellis chart shows a grid of the same chart for different [dimension](#glossary-1 "Glossary term") values. You can use the trellis chart to compare metrics for different groups of data. The Trellis container is included in the Visualization bundle. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You can create a trellis chart on the [sheet](#glossary-2 "Glossary term") you are editing. The chart that you want to repeat for different dimension values must be a master visualization.

Do the following:

1. Create the chart that you want to repeat for different dimension values and save it as a master visualization.

   [*Reusing visualizations with a master visualization*](../create-master-visualization.htm)
2. In the assets panel, open Charts.
3. Under Dashboard objects, drag a Trellis container object to the sheet.
4. Select which master visualization to show in Appearance > Trellis options > Base visualization in the property panel.
5. Select the dimension that you want to use as the first grid dimension in Data > Dimensions.
6. Optionally, add a second grid dimension to create a grid with one dimension in each axis.

Tip noteIf any of the grid dimensions are calculated dimensions, toggle on Calculated Dimension in the settings for the dimension.

You will now see a grid of [charts](#glossary-3 "Glossary term") each based on the grid dimensions you selected.

### Troubleshooting

I do not see a grid of charts, and receive this message: Too many dimension values!

Possible cause

There are more dimension values than the maximum number of charts allowed in the grid.

Proposed action

You can increase the number of charts allowed in Appearance > Trellis options > Maximum number of charts.

## Changing the appearance of the chart

You can customize your chart with one or more features.

### Setting the number of columns

You can set the number of columns in the chart grid with Appearance > Trellis options > Number of columns.

### Setting the y-axis range of charts

You can select which y-axis range to show for the charts in the trellis chart with Appearance > Trellis options > Auto range.

- On will show the same range for all charts. This is the best option if you want to compare values between different charts.
- Off will show an optimized range for each chart.

### Show border

You can show a border for the trellis chart with Appearance > Trellis options > Border. You can adjust width, color and style. It is also possible to define a custom border.

### Slide mode

You can view the charts in slide mode instead of a grid by setting Appearance > Trellis options > Slide mode to On. In slide mode, you view one chart at a time. You can scroll between the charts.

## Using the styling panel to further customize the appearance

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

## Configuring how null values are represented

### Null measure values

To configure the representation of null measure values for a dimension value, use Appearance > Trellis options > Show all possible dimensions. With Show all possible dimensions, you have the following options:

- On: The container shows a measure value of 0 for a dimension value where no measure data is present. Suppose that the master visualization aggregates sales by month and there are no sales in October. Here, the Trellis container will still list October as a dimension in the charts (with a value of 0 as applicable).
- Off: The container does not show dimension values where no measure data is present. Suppose that the master visualization aggregates sales by month and there are sales in all months except October. Here, the Trellis container will list each month except October in the charts.

### Null values in the grid dimensions

It could happen that there are null values in the grid dimension. If you want the Trellis container to visualize these null values, toggle on the Include null values setting.

Do the following:

1. In the properties panel, expand Data.
2. Expand the dimension for which you want to show null values.
3. Turn on Include null values.

## Best practices for creating the master visualization

Here are some tips for creating a master visualization that will work well in a trellis chart:

- Show the title in the master visualization. In the trellis chart, the title is replaced with the grid dimension value of each chart.
- If you use expressions: create a label to hide the set expression.
- If you are using a combo chart: use only one axis, and set the minimum and maximum of the y-axis.
- If you are using a box plot: set the minimum and maximum of the y-axis.
- If you are using a scatter plot: set the x-axis.
- If you are using a map: use advanced mode, and set the layer color and title. For an example, see [*Example 2: Coloring on a map chart*](trellis-advanced-mode.htm#TrellisExample2).

## Using advanced mode

Use advanced mode to customize the [set expressions](#glossary-4 "Glossary term") and dimension values that will be shown in the Trellis container. Advanced mode allows you to use placeholder values to allow dynamic output tailored to the dimension being shown in each chart in the container.

Activate advanced mode by setting Appearance > Trellis options > Advanced mode to On. Advanced mode allows you to:

- Use advanced expressions for labels, titles, subtitles, and footnotes.
- Use advanced expressions to define the data shown in the visualization. For example:

  - if expression as chart measure
  - Coloring by measure
  - Joining the Trellis set expression with other set expressions

Do the following:

1. In the properties panel for the master visualization, go to Appearance > Trellis options, and set Advanced mode to On.
2. Use the placeholders in the table below in expressions for measures, coloring, chart text, and other properties. They will be replaced in the Trellis container by the corresponding values.

Advanced mode value replacements in a trellis chart

| Placeholder | Replaced by value |
| --- | --- |
| $(vDim) | Dimension Name |
| $(vDimValue) | Dimension Value |
| $(vDimSet) | ,[Dimension Name]={'Dimension Value'} |
| $(vDimSetFull) | {<[Dimension Name]={'Dimension Value'}>} |

### Use cases and examples

#### $(vDim)

$(vDim) is useful as an expression for labels, titles, subtitles, or footnotes in the master visualization. For example, in a subtitle:

='This chart presents the aggregation by ' & $(vDim)

#### $(vDimValue)

$(vDimValue) is useful in many scenarios:

- Expressions for measure data in the master visualization. For example, as a measure in a Text & image or Text object:

  =if(GetSelectedCount([Product Category])=1, Sum({<Region={$(vDimValue)}>} Sales), 'Please select a product category.')
- Expressions for label, titles, subtitles, or footnotes in the master visualization. For example, as a footnote:

  ='This chart presents sales data for' & $(vDimValue) & '.'

#### $(vDimSet)

$(vDimset) is useful when you need to join multiple set expressions together. This can be used in an expression for measure data in the master visualization. For example:

=sum({<ProductName={'Bike Helmet'} $(vDimSet)>} Sales)

For the example above, the Trellis container would restrict the data to ProductName values of Bike Helmet. A separate chart would be shown for each unique value in the dimension used in the Trellis container.

#### $(vDimSetFull)

$(vDimSetFull) is useful for setting chart coloring by measure in the master visualization. For example:

=Sum($(vDimSetFull) Sales)

### Long-form examples

For step-by-step examples showing how to use advanced mode, see [*Trellis container advanced mode examples*](trellis-advanced-mode.htm).

## Limitations

For information about general limitations, see [*Limitations*](visualization-bundle.htm#Limitati).

### Unsupported visualizations

You cannot use the following visualizations in a trellis chart:

- Filter pane
- Histogram
- Container
- Layout container

### Multi KPI visualizations with embedded master visualizations

It is not possible to use a Multi KPI chart that contains an embedded master visualization.

### Selecting by dimension

If you make a selection on the dimension that is used as grid dimension in the trellis chart, the selection is not reflected in the trellis chart.

Example:

You have a filter pane with countries, and a trellis chart with country as the first grid dimension. When you select a country in the filter pane, the trellis chart will still show a chart for each country and ignore the selection.

### Coloring by master measure color

Colors assigned to master measures in a trellis container do not appear unless the trellis container is using the advanced mode.

## Learn more

- [*Trellis container advanced mode examples*](trellis-advanced-mode.htm)
- [How do I configure a Visualization Bundle Trellis container chart?](/lnk/How_configure_Visualization_Bundle_Trellis_container_chart)

Related learning:

- [How do I configure a Visualization Bundle Trellis container chart?](/lnk/How_configure_Visualization_Bundle_Trellis_container_chart)
