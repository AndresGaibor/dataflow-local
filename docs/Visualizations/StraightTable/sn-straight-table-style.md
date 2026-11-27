---
title: "Styling a straight table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table-style.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating straight tables", "Configuring straight table properties"]
---

# Styling a straight table

A number of styling properties are available for customizing the look and feel of your straight table. Styling can help reflect your organization's color palette, assist analysis, and improve readability.

For information about adjusting other aspects of the straight table's appearance, see [*Customizing straight table appearance and navigation*](sn-straight-table-appearance.htm).

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

## Styling the text

The straight table is a text-based visualization, so text can be styled in many different ways:

- [*Chart-level text styling*](#ChartText)
- [*Column- and cell-level text styling*](#ColLevel)
- [*Row-level text styling*](#RowText)

### Chart-level text styling

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font, emphasis style, font size, and color for the following text elements:

   - Header: Style the text of the headers for the dimensions and measures.
   - Dimension values: Style the text of the dimension values.
   - Measure values: Style the text of the measure values.
   - Totals: Style the text of the totals, if you have selected to show a Totals row under Appearance > Presentation.
   - Subtotals: Style the text of subtotal rows.
   - Dimension null values (see [*Customizing null values*](#Nulls))
   - Measure null values (see [*Customizing null values*](#Nulls))
   - Zebra stripes: With this setting turned on, you can set alternating text color for rows. See [*Applying zebra stripes*](#ZebraStripes).

### Column- and cell-level text styling

#### Text emphasis

You can use an expression to define how the text in each column is styled. If you style a column's text with an expression, this expression overrides the application theme, and any custom styling applied to the visualization, for that column.

You can use the following syntax in your expression to define the styling (the letter in the tag is not case sensitive):

- <B>: Bold
- <I>: Italics
- <U>: Underlined
- <S>: Strikethrough

More than one of the options above can be applied at a time.

Examples:

if(avg(Sales) > 300, '<B>')

if(count(OrderID) = 0, '<S>')

if(sum(Sales) > 100000, '<B><U>', '<I>')

Do the following:

1. Under Data, select a column and open Presentation in the properties.
2. Under Text style expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

#### Text color

You can change the text color for individual columns. You can change the text color in both the column's header and content cells.

Do the following:

1. Under Data, select a column and open Presentation in the properties.
2. To color the header cell text, under Header, under Text color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
3. To color the content cell text, under Content, under Text color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

#### Text alignment and column width

Do the following:

1. Under Data, select a column and open Presentation in the properties.
2. Use the slider to select an option for Text alignment. With Custom text alignment, you can select left, center, or right alignment.

   Information noteIf Text alignment is set to Auto, column data is aligned according to data type: text values are left-aligned and number values, including date related values, are right-aligned. If you set it to Custom, you can align the data to the left, center, or right.
3. Make a selection for Column width. You can select one of the following:

- Auto
- Fit to content
- Pixels
- Percentage

### Row-level text styling

Row-level settings are available for styling text:

- [*Applying zebra stripes*](#ZebraStripes)
- [*Customizing the hover behavior*](#Customiz)

## Customizing the background

Background can be styled at various levels:

- [*Chart-level background styling*](#ChartBckgrd)
- [*Column- and cell-level background styling*](#ColBckgrd)
- [*Row-level background styling*](#RowBckgrd)

### Chart-level background styling

You can customize the background of the chart. The background can be set by color and image.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-0 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background. The chart header always displays with 100% opacity.

   When using a background image, you can adjust image sizing and position.
4. On the Chart tab, customize the background color for the following elements:

   - Header (100% opacity is used)
   - Dimension values
   - Measure values
   - Measure labels
   - Totals (100% opacity is used)
   - Subtotals (100% opacity is used)
   - Dimension null values (see [*Customizing null values*](#Nulls))
   - Measure null values (see [*Customizing null values*](#Nulls))
   - Zebra stripes (see [*Applying zebra stripes*](#ZebraStripes))

### Column- and cell-level background styling

You can use expressions to define the background color of both header and content cells of each column.  If you style a column's background with an expression, this expression overrides the application theme, and any custom styling applied to the visualization, for that column. If you have not set a text color, the text will automatically be a high contrast color for your selected background color.

Do the following:

1. Under Data, select a column and open Presentation in the properties.
2. To color the header cell background of a column, under Header, under Background color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
3. To color the content cell backgrounds of a column, under Content, under Background color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

### Row-level background styling

Row-level settings are available for defining the background color:

- [*Applying zebra stripes*](#ZebraStripes)
- [*Customizing the hover behavior*](#Customiz)

## Customizing null values

You can change how null values are represented in the straight table.

You can change how null values are represented for dimensions and measures. Enter static text to replace null values for each. When you enter a numeric value for the measure null value text, it is interpreted as a number rather than text. This lets you fill in missing calculations with actual values, such as 0. Dimension null value text is always interpreted as text.

For null table cells, the null value styling overrides any other styling that has been set at the row, column, and cell level.

Do the following:

1. Click Appearance > Presentation in the properties panel.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. Open the Chart tab of the styling panel.
4. In the Dimension null values and Measure null values sections, you can adjust the following:

   - Emphasis style, text color, and background color.
   - Null value text: Enter the text you want to replace null values with.

     Information note

     If you set the null value text for measures to a numeric value, these null values are also formatted and styled as numeric values. In this case, the measure null value text inherits the number format, as well as the styling and background color, set for measure values.

     For example, if the measure column is formatted as currency, percentage, date, or time, the null value is displayed using the same number format.

     This does not apply to dimension null values, which are always treated as text.

## Customizing the grid

You can customize the table grid.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab, customize the grid with the following elements:

   - Row height: Set the height of rows in lines.
   - Border: Set the color of the cell borders.
   - Divider: Set the color of the divider between that divides the header and body of the table.

## Customizing the hover behavior

You can set display options for when a user hovers over a row in the table.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, under Row hover, adjust the following settings:

   - To highlight rows in the table when a user hovers over them, set the switch to On. Switch the behavior off according to preference.
   - Row hover color: Set the color to highlight the row when a user hovers over it.
   - Row hover font color: Set the color of the text in the highlighted row when a user hovers over it.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Applying zebra stripes

With zebra stripes, you can add alternating rows of color to the straight table. Zebra stripes improve readability by increasing contrast between odd and even rows.

You can set the text and background color for odd and even rows.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab of the styling panel, set Zebra stripes to On.
4. Adjust the following settings:

   - Color (odd row): Set the text color of the odd rows.
   - Background (odd row): Set the background color of the odd rows.
   - Color (even row): Set the text color of the even rows.
   - Background (even row): Set the background color of the even rows.
