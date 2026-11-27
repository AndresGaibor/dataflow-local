---
title: "Styling a write table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Create/style.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating write tables", "Configuring write tables"]
---

# Styling a write table

A number of styling properties are available for customizing the look and feel of your write table. Styling can help reflect your organization's color palette, assist analysis, and improve readability.

For information about adjusting other aspects of the write table's appearance, see [*Customizing the appearance of a write table*](appearance.htm).

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../../style-visualization.htm).

Information noteMuch of this information does not apply to editable columns in the write table. For information about customizing editable columns, see the separate sections [*Styling editable columns*](#StyleEditable) and [*Configuring editable columns*](editable-column.htm#ConfigureEditable).

## Styling the text

The write table is a text-based visualization, so text can be styled in many different ways:

- [*Chart-level text styling*](#ChartText)
- [*Column- and cell-level text styling*](#ColLevel)
- [*Row-level text styling*](#RowText)

### Chart-level text styling

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
4. On the Chart tab, set the font, emphasis style, font size, and color for the following text elements:

   - Header: Style the text of the headers for the dimensions and measures.
   - Dimension values: Style the text of the dimension values.
   - Measure values: Style the text of the measure values.
   - Totals: Style the text of the totals, if you have selected to show a Totals row under Appearance > Presentation.
   - Null values: Style the text of the null values. You can change emphasis style and color.

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
2. Under Text style expression, enter the expression. Click ![Open expression editor](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

#### Text color

You can change the text color for individual columns. You can change the text color in both the column's header and content cells.

Do the following:

1. Under Data, select a column and open Presentation in the properties.
2. To color the header cell text, under Header, under Text color expression, enter the expression. Click ![Open expression editor](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
3. To color the content cell text, under Content, under Text color expression, enter the expression. Click ![Open expression editor](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

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
2. Under Appearance > Presentation, click ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-0 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background. The chart header always displays with 100% opacity.

   When using a background image, you can adjust image sizing and position.
4. On the Chart tab, customize the background color for the following elements:

   - Header (100% opacity is used)
   - Dimension values
   - Measure values
   - Measure labels
   - Totals (100% opacity is used)
   - Null values

### Column- and cell-level background styling

You can use an expression to define the background color of each column. If you style a column's background with an expression, this expression overrides the application theme, and any custom styling applied to the visualization, for that column.

Do the following:

1. Under Data, select a column and open Presentation in the properties.
2. Under Background style expression, enter the expression. Click ![Open expression editor](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

### Row-level background styling

Row-level settings are available for defining the background color:

- [*Customizing the hover behavior*](#Customiz)

## Customizing the grid

You can customize the table grid.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab, customize the grid with the following elements:

   - Row height: Set the height of rows in lines.
   - Border: Set the color of the cell borders.
   - Divider: Set the color of the divider between that divides the header and body of the table.

## Customizing the hover behavior

You can set display options for when a user hovers over a row in the table.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab of the styling panel, under Row hover, adjust the following settings:

   - To highlight rows in the table when a user hovers over them, set the switch to On. Switch the behavior off according to preference.
   - Row hover color: Set the color to highlight the row when a user hovers over it.
   - Row hover font color: Set the color of the text in the highlighted row when a user hovers over it.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Styling editable columns

You can style editable columns in the write table.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, under Editable column values, adjust the following settings:

   - Select a font, font emphasis, text size, and text color.
   - Background: Set the background color for editable column cells.
   - Input field: Set the color of the background for the text input area.
   - Hover color: Set the color of the outside of the cell when a user hovers their cursor over it.
