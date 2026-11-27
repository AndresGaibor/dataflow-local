---
title: "Creating tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Table/create-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating tables

The table shows several fields simultaneously, where the content of each row is logically connected. Typically, a table consists of one [dimension](#glossary-0 "Glossary term") and several [measures](#glossary-1 "Glossary term").

Information note

The Straight table has replaced the Table as the default table visualization. Consider upgrading existing tables to straight tables for improved functionality and performance. For information about creating straight tables, see [*Creating straight tables*](../StraightTable/create-sn-straight-tables.htm).

You can create a new table on the [sheet](#glossary-2 "Glossary term") you are editing.

Do the following:

1. From the assets panel, in Charts under Legacy, drag a Table to the sheet.
2. Click Add dimension and select a dimension or a field.
3. Click Add measure and select a measure or create a measure from a field.

When you have created the table, you may want to adjust its appearance and other settings in the [properties](#glossary-3 "Glossary term") panel. For information about styling, see [*Styling the table*](#Styling). For information about customizing other aspects of the chart's appearance, refer to the current topic and [*Changing the appearance of a visualization*](../change-appearance-of-visualization.htm).

Tip noteColumn width is automatically set to keep columns together for improved readability. You can adjust the width of a column by dragging the header divider. Double-click the header divider to reset to the default width.

## Styling the table

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
4. On the Chart tab, set the font size and color for the following text elements:

   - Header: Style the text of the column headers.
   - Content: Style the text of the table content. If you have selected to show a Totals row, it will be styled using these settings, in addition to its text being bold.

Additionally, you can customize how the text appears when a user hovers over a row. See [*Customizing the hover behavior and scrollbar*](#Customiz).

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

### Setting the row height

You can adjust the height of the rows in the table.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab, under Row height (in lines), enter a positive integer value representing how many originally sized rows should fit into one newly sized row, height-wise.

### Customizing the hover behavior and scrollbar

You can set display options for when a user hovers over a row in the table. You can also set the scrollbar size.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, under Row hover, adjust the following settings:

   - To highlight rows in the table when a user hovers over them, set the switch to On. Switch the behavior off according to preference.
   - Row hover color: Set the color to highlight the row when a user hovers over it.
   - Row hover font color: Set the color of the text in the highlighted row when a user hovers over it.
4. Under Scrollbar size, set the size of the scrollbar in the chart (you can select Small, Medium, or Large).

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Aligning data

If Text alignment is set to Auto, column data is aligned according to data type: text values are left-aligned and number values, including date related values, are right-aligned.
If you set it to Custom, you can align the data to the left, center, or right.

## Sorting the table

You can adjust the sorting of the table in several ways:

- Column sorting: adjust the order of the dimensions and measures from left to right
- Row sorting: adjust the sorting priority order of the rows
- Internal sorting: use the internal sorting order of dimensions and measures
- Interactive sorting: during analysis you can click on a column header to sort the table

### Column sorting

By default, the order in which columns are sorted is set by the order in which dimensions and measures are added to the table. If you add the measure Sales first, it is presented first (leftmost) in the table. The next dimension or measure that is added is presented in the second column, and so on. The column sorting order can be changed in the properties panel, under Columns.

### Row sorting

By default, rows are sorted by the first added dimension or measure, numeric values ascending, text values ascending. A small arrow under the column header shows by which column the table is sorted.

You can change the row sorting in the properties panel, under Sorting.
Drag the dimensions and measures to change the sorting priority order. In many cases, sorting is not only affected by the first dimension or measure in Sorting, but also the following ones.

Example:

In the following screenshot, the rows are first sorted by Customer, then by Month, and then by Product Type. As you can see, the columns Customer and Month have several rows with the same values (A-2-Z Solutions and Month). The rows in Product Type are ordered alphabetically, but only those that were sold in January to the customer A-2-Z Solutions are displayed.

![Table with sorting order: Customer, Month, Product type.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_TableSorting.png)

By changing the sorting order, so that secondary sorting is by Product Type, followed by Month, all Product Type items sold to the customer A-2-Z Solutions are presented in alphabetical order, whereas only the months when they were sold are displayed under Month.

![Table with sorting order: Customer, Product type, Month.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_TableSorting2.png)

### Internal sorting

Each dimension and measure has a default (Auto) internal sorting order, which can be changed. Under Sorting, click the item you want to change and click the button to switch to Custom sorting. Changes made to the internal sorting of an item may not have any effect if the sorting is in conflict with an item with higher priority.

### Interactive sorting

During analysis, you can set which column to sort on by clicking the column header. The first click sorts the table according to the default sorting of the selected item. A second click reverses the sorting order. Interactive sorting is session based and is not saved. If you want your changes to the sorting to be persistent, you need to make the changes in the properties panel.

## Displaying totals

By default, the totals of numeric values are displayed under the column names. In the properties panel, you can hide the totals row and customize its calculations. You can also choose to display the totals at the bottom of a column, or not at all.

### Showing totals

Do the following:

1. In the properties panel, expand the Appearance section.
2. Change the Totals setting. With a Custom value, you can choose whether to place the totals at the top or bottom of the chart. Select None to hide the totals.
3. You can set a Totals label, either plain text or an expression.

### Configuring totals calculations

If you have selected to show a totals row, you can set a custom aggregation to use for a numeric measure total. This aggregation overrides the calculation used by the measure.

Do the following:

1. In the properties panel, expand the Data section.
2. Expand a numeric measure.
3. Under Totals function, use the drop down menu to select one of the following:

   - Auto
   - Avg
   - Count
   - Max
   - Min
   - Sum
   - None (totals for the measure are shown with -)

   Information noteThese settings are column-level, so they can be overridden if the totals row is hidden entirely in the chart. See [*Showing totals*](#Showing).

## Displaying more data

The chart can be configured to display more data, or to show it in different ways. Under Appearance > Presentation in the properties panel, you can:

- Freeze the first column from scrolling.

  For application consumers who have Touch screen mode activated in the navigation menu, you need to turn on Enable on touchscreen to support the freezing of the first column for these consumers.
- Select to wrap multiline text in headers and cells separately.

  Tip noteUp to three lines of text can be wrapped using these settings. For longer text, set a higher Row height limit in the ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling panel. See [*Setting the row height*](#RowHeight).
- Turn off horizontal scrolling and turn on the column picker feature. This lets application consumers change table column order.

## Adding a trend indicator to a measure

You can add a trend indicator to a measure column. This will show a symbol next to the measure value. You can define the ranges that determine which symbol is displayed and in which color it is displayed. You enable the indicator by setting Representation to Indicator in the measure properties.

### Setting the indicator limits

You need to add the limits for the ranges you want to use for showing indicators with Add limit. You can set a limit value in three ways.

- Use the slider.
- Type a value in the text box.
- Set an expression that returns the limit value.

When you have added the limits, you can select the color and the symbol of the indicator for each defined range.

### Styling the indicator

You can style the way the indicator is displayed.

- You can show both the indicator and the measure value by selecting Show values.
- You can set the value color to the same as the indicator color with Apply color to value.
- You can display the indicator to the right or to the left of the value with Indicator position.

### Example

In this example, we added a trend indicator to the Sales measure to indicate which values are below the target value. The indicator limits are:

- For values below 3000000 a red flag is displayed.
- For values in the range of 3000000 to 3500000 a yellow flag is displayed.
- For values above 3500000 a green check-mark is displayed.

![Table with trend indicators](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_table_trend_indicator.png "Table with trend indicators")

## Adding a mini chart to a measure

You can add a mini [chart](#glossary-4 "Glossary term") to a measure column. This will show a small chart [visualization](#glossary-5 "Glossary term") instead of the measure value. You can define the dimension that determines what data is displayed and in which color it is displayed. You enable the indicator by setting Representation to Mini chart in the measure properties.

Information noteThe mini chart popup only shows the value of the measure, and is not broken down by individual dimension point values.

### Setting the mini chart type

After specifying which dimension the mini chart will be based on, you must select a Mode.

- Bars creates a bar chart.
- Dots creates a dot chart.
- Sparkline creates a sparkline chart. You can show dots at each data point along the sparkline chart by selecting Show dots.
- Positive/negative creates a chart with each value represented by a dot above or below the zero.

When you have selected the mode, you can specify the Y-axis of the Mini chart at the bottom of the mini chart options.

### Styling the mini chart

You can set the color of bars or lines for Bars, Dots, and Sparkline.

- You can optionally set the Max value color and Min value color, which will highlight the highest and lowest visible chart values.
- You can optionally set the Highlight first and Highlight last colors, which will highlight the first and last visible chart values.

You can set the positive and negative color for a Positive/negative mini chart.

## Learn more

- [*Table*](table.htm)
- [*Accumulating values over a dimension in a table*](table-example.htm)
- [*Using relative numbers in a table to calculate contribution*](table-example2.htm)
- [Interpreting Tables](/lnk/Interpreting_tables)

Related learning:

- [Interpreting Tables](/lnk/Interpreting_tables)
