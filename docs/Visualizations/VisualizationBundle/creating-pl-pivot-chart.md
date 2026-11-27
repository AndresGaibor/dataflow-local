---
title: "Creating P&L pivot charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-pl-pivot-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating P&L pivot charts

You can use the P&L pivot chart to create a pivot table with a layout for profit and loss reporting. You can color cells according to performance and style the chart with custom fonts and alternating row colors. You can also download the chart to Excel including formatting. The P&L pivot chart is included in the Visualization bundle.

Do the following:

1. In the assets panel, open Charts.
2. Under Legacy, drag a P&L pivot object to the sheet.
3. Click Add dimension and select a dimension or a field.
4. Click Add measure and select a measure or create a measure from a field.

## Coloring cells to show performance

You can color cells to show performance according to a scale of Poor, Fair and Good. All rows and columns are colored by default, but you can choose which columns and rows to color if you want to.

Do the following:

1. Make sure that Enabled is set to On under Appearance > Color by condition.
2. Select which rows to color by performance.

   Set Color all rows by condition to Specified rows.

   Add rows to color by name (dimension value) with Add row to color.
3. Select which measures to color by performance.

   Set Color all measures to Specified measures.

   Add a list of measures by number in Measure indices with the first measure of the chart numbered zero. Separate the measures with a comma.

   Example: Color the first, third, and fifth measure.

   0,2,4
4. Set performance limits and colors.

   You can set the range limits for Poor and Fair.

   - All cells with a value lower than the Poor range limit are displayed with the background color and text color set for Poor.
   - All cells with a value lower than the Fair range limit, but higher than Poor, are displayed with the background color and text color set for Fair. You should set the Fair range limit higher than Poor.
   - All other cells are displayed with the background color and text color set for Good.

## Styling the chart using a style template

You can create a layout for the chart, for example to show a profit and loss report, using a style template.

Information noteYou need to be able to add and load a CSV file to the application.

Do the following:

1. Create a style template as a CSV file. Use the style template format described below.
2. Load the style template to your application as one field. When you add the file, do not use semicolon as field separator, each row should be loaded as one field.
3. Set Style template field under Appearance > Table format to the name of the template field you added.

You can load several style templates in your application, and change the layout with Style template field.

### Style template format

The style template is created as a comma separated text file (CSV) using UTF-8 encoding.

The style template rows need to align to the data in your first dimension. You need to refer to a dimension value in the template. The dimension value should be first in every row. You do not need to specify all rows/dimension values in the template. The style template can contain maximum 5000 rows.

Each row in the template should be in the following format. It is not required to use a header row.

DimensionValue;Bold;Background;FontStyle;TextColor;Align;FontSize;Comment

- DimensionValue

  The dimension value of the row that you want to style.
- Bold

  Set to <bold> if you want bold text.
- Background

  Set a background color. You can use <dark>, <night>, <soft>, <red>, <orange>, <violete>, <blue>, <green> or a color code in RGB format, for example rgb(183,219,255). The default background color is white.
- FontStyle

  You can set the font style to <italic> or <oblique>.
- TextColor

  You can set the color of the text to <white>. The default background color is black.
- Align

  You can center align the text with <center>. The default alignment is left for text and right for numeric values.
- FontSize

  You can set the font size to <large>, <medium> (default) or <small>.
- Comment

  You can use the <comment> tag to replace all zero values with a space. This is useful when you want to include a sub header row. without values.

You can also use the style tags in any order, and exclude tags that are not used. These rows will give the same result:

Operating expenses;<bold>;;<italic>;;;;

Operating expenses;<italic>;<bold>

### Style template example for profit and loss reporting

Cost of goods sold;<bold>;RGB(225,226,226);;;;;
Extraordinary items after tax;<bold>;RGB(193,216,47);;;<center>;<large>;
Extraordinary items;<bold>;;<italic>;;<center>;;<comment>
Financial revenue & expenses;<bold>;;<italic>;;<center>;;<comment>
General & administrative expenses;<bold>;;<italic>;;<center>;;<comment>
Gross profit;<bold>;RGB(193,216,47);;;<center>;<large>;
Income before tax & extraordinary items;<bold>;RGB(193,216,47);;;;<large>;
Manufacturing overhead;<bold>;;<italic>;;<center>;;<comment>
Net costs of goods sold;<bold>;RGB(225,226,226);;;;;
Net gain on sale of land;<bold>;RGB(193,216,47);;;<center>;<large>;
Net Income (Profit);<bold>;#191970;;<white>;<center>;<large>;
Net mfr overhead;<bold>;RGB(225,226,226);;;;;
Net sales revenues;<bold>;RGB(225,226,226);;;;;
Operating expenses;<bold>;;<italic>;;;;
Operating income before taxes;<bold>;RGB(193,216,47);;;;<large>;
Other general & admin expenses;<bold>;rgb(128, 191, 255);<white>;;<center>;<large>;
Revenues;<bold>;;<italic>;;<center>;;<comment>
total general & admin expenses;<bold>;#efefef;;;;;
total operating expenses;<bold>;rgb(128, 191, 255);<white>;;;;
Total selling expenses;<bold>;RGB(225,226,226);;;;;

To use this template, you need a data file where the first dimension contains values that correspond to the first item of each row, for example Cost of goods sold.

P&L pivot chart styled with the layout template in the example

![A P&L pivot chart showing many dimensions and measures.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_pl_pivot.png "Click to view full size")

## Using the styling panel to further customize the appearance

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

## Downloading the chart in Excel format

You can download the P&L pivot chart as an Excel file. When you download the chart using the Export as XLS option, the exported .xls file includes custom formatting applied to the chart.

Do the following:

1. Right-click a P&L pivot chart, or hover over the chart and click ![Three-dot menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
2. Select ![Export](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_export.svg)Export as XLS.

   Information noteAlternatively, select Download, and use the Data option to download the chart as a .xlsx file. When using the Download > Data option, custom formatting applied to the P&L pivot chart is not included in the Excel file.
3. Select a location on your computer where you want to store the file.

Related learning:

- [How do I configure a Visualization Bundle P and L pivot chart?](/lnk/How_configure_Visualization_Bundle_P_L_pivot_chart)
