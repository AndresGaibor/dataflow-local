---
title: "Creating pivot tables (Pivot)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-pivot-object.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating pivot tables (Pivot)

The pivot table (Pivot) in the Visualization bundle presents [dimensions](#glossary-0 "Glossary term") and [measures](#glossary-1 "Glossary term") as rows and columns in a table. In a pivot table you can analyze data by multiple measures and in multiple dimensions at the same time. For more information, see [*Visualization bundle*](visualization-bundle.htm).

Do the following:

1. In the assets panel, open Charts.
2. Under Visualization, drag Pivot to the sheet.
3. Add the row dimension. Do one of the following:

   1. Click Add dimension and select a [field](#glossary-2 "Glossary term") or master dimension.
   2. In the properties panel, expand Data and click ![Add custom expression](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to insert a custom expression as a row dimension.
4. Optionally, add more row dimensions in the properties panel:

   - In Data > Dimensions > Rows, click ![Add data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and select a [field](#glossary-3 "Glossary term") or master dimension.
   - In Data > Dimensions > Rows, click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to insert a custom expression as a row dimension.

   Tip note The pivot table drills down rows in the order they are added. You can click and drag the dimensions to reorder them.
5. Add one or more column dimensions as needed:

   - In Data > Dimensions > Columns, click ![Add data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and select a [field](#glossary-4 "Glossary term") or master dimension.
   - In Data > Dimensions > Columns, click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to insert a custom expression as a column dimension.
6. Add one or more measures:

   - In Data > Measures, click ![Add data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) and select a [field](#glossary-5 "Glossary term") aggregation or master measure.
   - In Data > Measures, click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to insert a custom expression as a measure.
7. Optionally, you can define filters to apply to the chart data. This is done in Data > Filters in the properties panel.

   For more information about filters, see [*Applying filters to visualizations*](../../Sheets/visualization-filters.htm).
8. As needed, further manage the pivot table data in the Data tab of the properties panel. You can:

   - Click the checkbox next to any item. Click ![Tools](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) or right-click an item to perform the following actions:

     - Move to top
     - Move to bottom
     - Hide
     - Show
     - Cut
     - Copy
     - Duplicate
     - Paste
     - Delete

     You can apply changes to multiple items by selecting them and then right-clicking on one of the selected items.

     Information noteHide and show actions are not available when both visible and alternative columns are selected.
   - Click ![Hide](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view_outline.svg) or ![Show](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view_disabled_outline.svg) on items to hide or show them—that is, to add and remove them from alternative columns. Hidden columns can be added when using [chart exploration](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/creating-pivot-object.htm#ChartExploration).
   - Click ![Draggable column](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_draggable.svg) next to items and drag them to reorder, or to move them between row and column dimensions.

After defining the data, you can adjust appearance and other settings in other sections of the properties panel.

## Pivoting your data in the properties panel

In the properties panel, you can add measures and dimensions to the pivot table, as well as pivot rows or columns.

### Data

In the Data pane, you can add Dimensions, Measures, and Filters. You can move items between rows and columns. You can also change item order inside rows or columns. When you use more than one measure, they are grouped and a Values item is created.

![Properties panel, Data section. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotObject_data_pane.png)

### Sorting

On the sorting pane in advanced properties, you can change the internal order of dimensions and measures.

![Properties panel, sorting pane.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotObject_sorting_pane.png)

Information noteWhen sorting pivot tables, NULL values are always displayed first.

#### Sort by first measure

If you have more than one measure, a measure group is created. Sort by first measure will sort dimension values by the numeric value of the first measure. This sort order will affect all dimensions and take precedence before any other sort order defined under the dimensions.

For example, you have two measures: Quantity and Sales. In the properties pane, under Data> Measures, Quantity is listed first. If you Sort by first measure in descending order, your table is sorted starting with the dimension with the highest Quantity.

If Sort by first measure is turned off, the table uses the sort order configured for the dimensions.

Pivot table in Edit mode. Sort by first measure has been toggled on.

![Pivot object with sorted by first measure.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotObject_Example4.png "Click to view full size")

Limitations:

- This option is only supported if subtotals are calculated. You can calculate subtotals by doing one of the following:
  - In the properties pane, go to Data, and click on a dimension. Under Field, toggle on Show totals.
  - In the properties pane, go to Appearance > Presentation. Toggle on Indent rows.
- This option is not supported for calculated dimensions.
- This option is only supported if all dimensions are in the Row section and all measures are in the Column section.

#### Dimension sorting

With Sort by first measure turned off, the table can be sorted by dimension values. Each dimension can have Auto or Custom sorting. With Auto sorting, field values are sorted alphabetically and numerically in ascending order. With Custom sorting, you can turn each of the following settings on or off:

- Sort by expression: Sorts by custom expression. Sort by expression overrides the Sort numerically and Sort alphabetically settings. This option should only be used with the first (outermost) dimension in the table.
- Sort numerically: Sorts field values starting with a number.
- Sort alphabetically: Sorts field values starting with a letter.

Ascending and Descending options are available for all three settings.

#### Sorting in search

The user can click a dimension name in the table to expand a listbox. In the listbox, the user can search and select individual dimension values. The Sorting in search setting controls the sort order of the values in a dimension listbox.

You have the following options for the listbox sort order:

- Auto: Uses the default sort order. Numbers are sorted numerically in ascending order. Text is sorted alphabetically in ascending order.
- Inherit from dimension: Uses the sort order defined for the individual dimension.

## Formatting dimension and measure columns

You can format your dimension and measure columns with additional options. You can:

- Limit displayed dimensions
- Format dimension representation
- Format measure representation
- Format measure numbers
- Group measures under headers
- Create conditional columns
- Set background color of cells using expressions
- Set text color with expressions
- Setting column width

### Limiting displayed dimensions

Limit the number of displayed values for a dimension. When you set a limitation, the only dimensions displayed are those where the measure value meets the limitation criterion.

Do the following:

1. Under Data, select a dimension and expand the properties.
2. Under Field > Limitation, select one of the following limitations:

   - No limitation: The default value.
   - Fixed number: Select to display the top or bottom values. Set the number of values. You can also use an expression to set the number. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Exact value: Use the operators and set the exact limit value. You can also use an expression to set the number. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Relative value: Use the operators and set the relative limit value in percent. You can also use an expression to set the number. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

### Formatting dimension representation

You can format dimension columns to show values, links, or images using Representation in the properties panel. You can select the following representations:

- Text: Displays the dimension values as text. This is the default value.
- Link: Displays values as clickable links. Either the dimension value is used or the URL or you can add other URLs to the displayed dimension values.
- Image: Displays values that contain an absolute URL to an image display as images.

#### Formatting links

Information note

The character ; is not supported as a query parameter separator in a URL.

Do the following:

1. Under Data, select a dimension and expand the properties.
2. Under Presentation > Representation, select Link.
3. Under Link setting, select one of the following:

   - Add label: The dimension contains the destination URL in either the dimension expression or the data table. The links are displayed and ordered by destination URL expression.

     Under Link label, enter a descriptive text label for the destination URL. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Add URL: The dimension values become selectable text links that are labels for the URLs.

     Under Link URL, enter the destination URL expression. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

#### Formatting images

Warning note

Images in pivot tables are only accessible from servers and domains that have been safe-listed. Administrators make these resources available in Administration by adding Content-Security-Policies (CSP) for each server or domain. CSP helps to prevent cross-site scripting attacks by controlling what resources a browser can request from a server.

Information note

The character ; is not supported as a query parameter separator in a URL.

Do the following:

1. Under Data, select a dimension and expand the properties.
2. Under Presentation > Representation, select Image.
3. Under Image setting, select one of the following:

   - Add label: The dimension contains the absolute URL to the image in either the dimension expression or the data table. The links are displayed and ordered by the URL expression.

     Under Image label, enter a descriptive text label for the image that displays as alternative text when the image is hovered over. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Add URL: The dimension values become labels for the alternative text that displays when the image is hovered over.

     Under Image URL, enter the destination URL expression. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
4. Under Sizing, select one of the following sizing options:

   - Always fit
   - Fit to width
   - Fit to height
   - Stretch to fit
   - Original size
5. Under Position, select the image position within the cell.

### Formatting measure representation

You can format measure columns using Representation in the properties panel. You can select the following representations:

- Text: Displays the dimension values as text. This is the default value.
- Image: Displays measure values as images.
- Indicator: Displays customizable indicator symbols in measure cells. Text representations for each value can be shown or hidden alongside these indicators, depending on preference.

#### Formatting images

Warning note

Images in pivot tables are only accessible from servers and domains that have been safe-listed. Administrators make these resources available in Administration by adding Content-Security-Policies (CSP) for each server or domain. CSP helps to prevent cross-site scripting attacks by controlling what resources a browser can request from a server.

Information note

The character ; is not supported as a query parameter separator in a URL.

Do the following:

1. Under Data, select a measure and expand the properties.
2. Under Presentation > Representation, select Image.
3. Under Image setting, select one of the following:

   - Add label: The measure contains the absolute URL to the image in either the measure expression or the data table. The links are displayed and ordered by the URL expression.

     Under Image label, enter a descriptive text label for the image that displays as alternative text when the image is hovered over. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Add URL: The measure values become labels for the alternative text that displays when the image is hovered over.

     Under Image URL, enter the destination URL expression. Click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
4. Under Sizing, select one of the following sizing options:

   - Always fit
   - Fit to width
   - Fit to height
   - Stretch to fit
   - Original size
5. Under Position, select the image position within the cell.

#### Adding a trend indicator to a measure

You can add a trend indicator to a measure column. This will show a symbol next to the measure value. You can define the ranges that determine which symbol is displayed and in which color it is displayed.

Do the following:

1. In the properties panel, expand Data and click a measure.

   The measure properties open.
2. Under Presentation, set Representation to Indicator.
3. Click the rectangle below the Add limit button, containing a color and symbol. You can set the color and symbol for the indicator.

   If you add one or more limits, you can adjust the color and symbol for each range by clicking the range in this rectangle.
4. Set additional properties for the indicators, which are detailed in the sections below.

Setting the indicator limits

You need to add the limits for the ranges you want to use for showing indicators with Add limit. You can set a limit value in three ways.

- Use the slider.
- Type a value in the text box.
- Set an expression that returns the limit value.

When you have added the limits, you can select the color and the symbol of the indicator for each defined range.

Styling the indicators

You can style the way the indicators are displayed.

- You can show both the indicator and the measure value by selecting Show values.
- You can set the value color to the same as the indicator color with Apply color to value.

  Information noteWith this setting on, the indicator color overrides the current cell value color if it is defined in other properties for the chart.
- You can display the indicator to the right or to the left of the value with Indicator position.
- When you have one or more limits, toggle on Gradient to color the indicators with gradients between the colors.

### Formatting measure numbers

You can format measure numbers under Number formatting in the properties panel.

If you want to change the number format at application level, and not just for a single measure, it is better to do that in the regional settings in the SET statements at the beginning of the script in the data load editor.

Do the following:

1. Under Data, select a measure and expand the properties.
2. Under Field > Number formatting, select the format:

   - Auto: Qlik Sense automatically sets a number formatting based on the source data.

     To represent numeric abbreviations, the international SI units are used, such as k (thousand), M (million), and G (billion).
   - Number: By default, the formatting is set to Simple, and you can select the formatting from the options in the list. Change to Custom to and enter the format pattern under Format pattern.

     Examples:

     - # ##0 describes the number
       as an integer with a thousands separator. In this example " " is used as a thousands separator.
     - ###0 describes the number as an integer without a thousands separator.
     - 0000 describes the number as an integer with at least four digits. For example, the number 123 will be shown as 0123.
     - 0.000 describes the number
       with three decimals. In this example "." is used as a decimal separator.

     If you add the percent sign (%) to the format pattern, the measure values are automatically multiplied by 100.
   - Money: By default, the format pattern used for money is set by the preferred region settings in your profile. Use Format pattern to change the format pattern.
   - Date: By default, the formatting is set to Simple, and you can select the formatting from the options in the list. Change to Custom to and enter the format pattern under Format pattern.
   - Duration: By default, the format pattern used for duration is set by the preferred region settings in your profile. Duration can be formatted as days, or as a combination of days, hours, minutes, seconds and fractions of seconds. Use Format pattern to change the format pattern.
   - Custom: By default, the format pattern used for custom is set by the preferred region settings in your profile. Use Format pattern to change the format pattern.

### Grouping measures under headers

You can group adjacent measures under a shared header that is displayed above the measure labels. Each measure group is shown as one header cell that spans the measures in the group.

Do the following:

1. Under Data, select a measure and expand the properties.
2. Under Group, enter a string or string expression in Group name. For example, =max(Year) or ='FY' & $(vYear).
3. Repeat for each measure that you want to include in the group.

#### Behavior

Adjacent measures that resolve to the same non-empty group name share one header cell. Measures without a group name have their own blank header cell. Measures with the same group name are not grouped if another measure separates them.

Styling and theme settings interact as follows:

- The group header inherits its color from the measures that it covers.
- If all measures in a group use the same header color expression, the group header uses this expression.
- If the group measures use different header color expressions, the group header does not use any of them and defaults to any settings defined manually in the Styling panel. If no styling is manually applied, the group header defaults to the application theme.

The group header also scrolls and resizes together with the other column headers.

Limitations:

- Measure groups are only displayed when all measures are in the Columns section and there are no dimensions in the Columns section.
- Measure groups are not supported when downloading the chart as data.

### Creating conditional columns

Columns can be conditional, so that they only appear when certain conditions are met.

Do the following:

1. Under Data, select a dimension or measure and expand the properties.
2. Under Presentation > Show column if, click ![Open Expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
3. Enter the expression to determine the conditions for the column to appear.
4. Click Apply.

#### Example

Suppose you have a Pivot table or Pivot object that contains the following:

- Dimensions are Product Type and Product Name.
- Measures are Sum(Sales) and Count (distinct InvoiceNumber).
- The items under Columns are Values (default) and the field Quarter.

Part 1: Conditional column based on user selections

You might have a large number of years of data in your application, so you do not want to add too much clutter to the visualization. At the same time, you want to encourage granular and interactive analysis.

For the Quarter column, you could add the following expression for Show column if:

```
GetSelectedCount(Year)=1
```

With this expression, if the user selects a single year in the application, the pivot table breaks down each measure by quarter. If not, the total measure values are shown.

Part 2: Conditional columns using variables

You can use variables to encourage interactive analysis. Suppose you also create a variable vUserInteraction with a blank definition. Then, you create two Button charts on your sheet, configured with the Set variable value action:

- Show more detail: Clicking this button sets vUserInteraction to a value of ='Yes'.
- Show less detail: Clicking this button sets vUserInteraction to a value of ='No'.

In your pivot table, you could add a number of additional measures to the chart, such as Count(Quantity) and Sum(Cost). Then, configure each measure column to have the following value for Show column if:

```
'$(Reference)'='Yes'
```

This allows the chart to adapt to whether or not the user wants additional information. If the user clicks the Show more detail button, additional measures are added to the table. If not, or if they click Show less detail, the additional measures are removed.

- Show more detail: Clicking this button sets vUserInteraction to a value of ='Yes'.
- Show less detail: Clicking this button sets vUserInteraction to a value of ='No'.

In your pivot table, you could add a number of additional measures to the chart, such as Count(Quantity) and Sum(Cost). Then, configure each measure column to have the following value for Show column if:

```
'$(Reference)'='Yes'
```

This allows the chart to adapt to whether or not the user wants additional information. If the user clicks the Show more detail button, additional measures are added to the table. If not, or if they click Show less detail, the additional measures are removed.

### Setting background color with expressions

You can use expressions to define the background color of both header and content cells of each item. For example, you can have cells in the column change background color depending on the values in the column cell.

For more information about applying colors using expressions, see [*Color by expression*](../../Colors/color-by-expression.htm).

Do the following:

1. Under Data, select an item and open Presentation in the properties.
2. To color the header cell background of an item, under Header, under Background color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
3. To color the content cell backgrounds of an item, under Content, under Background color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

### Setting text color with expressions

You can define the text color for a column using expressions. For example, you can have cells in the column change text color depending on the values in the column cell. If the cell background color is defined but text color is undefined, the text color defaults to a color that best contrasts with the background.

You can change the text color in both the item's header and content cells.

For more information about applying colors using expressions, see [*Color by expression*](../../Colors/color-by-expression.htm).

Do the following:

1. Under Data, select an item and open Presentation in the properties.
2. To color the header cell text, under Header, under Text color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
3. To color the content cell text, under Content, under Text color expression, enter the expression. Click ![Open expression editor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

### Setting column width

By default, column width is automatically set. You can manually set column width by:

- Content
- Pixels
- Percentage

You can also manually size the columns by dragging the header borders.

Do the following:

1. Under Data, select a dimension or measure and expand the properties.
2. Under Presentation > Column width, select how you want to set column width:

   - Fit to content: Columns are sized by the width of the content in the column.
   - Pixels: Set the width of the column in pixels.
   - Percentage: Set the width of the column by percent.
   - Auto: Automatically set the column width with Qlik Sense.

## Changing how data is presented

There are several options available for customizing the data presentation in the pivot table. These options are available in the properties panel under Appearance > Presentation.

### Fully expanded

When selected, all values in the pivot table are displayed, rather than some being collapsed. This setting is noticeable when more than one dimension is added.

### Indent rows

This setting is also noticeable when more than one dimension is added.

When the setting is turned on, dimensions are nested within each other and expandable. When you expand a top-level dimension row, nested dimensions are displayed with an indentation at the beginning of each row.

With the setting turned off, dimensions after the first dimension are displayed in separate columns in the table and become visible if you expand a top-level dimension row.

## Customizing styling

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

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
4. On the Chart tab, adjust styling — such as font, emphasis style, font size, and color — for the following text elements:

   - Header: Style the text of the headers for all dimensions.
   - Dimension values: Style the text dimension values.
   - Measure values: Style the text of the measure values.
   - Measure labels: Style the text of the measure headers.
   - Total values: Style the text of the totals.
   - Dimension null values (see [*Customizing null values*](#Nulls))
   - Measure null values (see [*Customizing null values*](#Nulls))

### Customizing the background

You can customize the background of the chart. You can also color individual dimensions or measures by expression.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-6 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.
4. On the Chart tab, customize the background color for the following elements:

   - Header- Dimension values
     - Measure values
     - Measure labels
     - Total values
     - Dimension null values (see [*Customizing null values*](#Nulls))
     - Measure null values (see [*Customizing null values*](#Nulls))

### Customizing the grid

You can customize the pivot table grid.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the Chart tab, customize the grid with the following elements:

   - Row height: Set the height of rows in lines.
   - Border: Set the color of the cell borders.
   - Divider: Set the color of the divider between that divides both dimensions and measures as well as header and rows.
   - Background: Set the color of the empty area created when you have dimensions in Column.

### Customizing null values

You can change how null values are represented in the pivot table.

For null table cells, the null value styling overrides any other styling that has been set at the row, column, and cell level.

Do the following:

1. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
2. Open the Chart tab of the styling panel.
3. In the Dimension null values and Measure null values sections, you can adjust the following:

   - Emphasis style, text color, and background color.
   - Null value text: Enter the text you want to replace null values with.

     Information note

     If you set the null value text for measures to a numeric value, these null values are also formatted and styled as numeric values. In this case, the measure null value text inherits the number format, as well as the styling and background color, set for measure values.

     For example, if the measure column is formatted as currency, percentage, date, or time, the null value is displayed using the same number format.

     This does not apply to dimension null values, which are always treated as text.

### Expanding the pivot table fully

You can set the pivot table to always be fully expanded.

Do the following:

1. Click Appearance > Presentation in the properties panel.
2. Select Fully expanded.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Configuring totals

You can choose to show numeric totals for dimensions in the pivot table. Consider the following:

- With Indent rows turned on in Appearance > Presentation, you can show totals for any dimension other than the automatically created Values dimension.
- With Indent rows turned off in Appearance > Presentation, you can show totals for the first Row dimension, and any Column dimension other than the automatically created Values dimension.

Do the following:

1. In the properties panel, expand the Data section.
2. Click the dimension to expand its properties.
3. Set Show totals to On.

## Working with chart exploration

Chart exploration allows users without edit access to the sheet to modify the Pivot object on the fly during analysis. Users can add, remove, and reorder data, effectively building their own tables if needed for custom analysis.

### Preparing for activating chart exploration

Prepare the Pivot object for chart exploration by adding all data assets that users will need. This is done under Data in the properties panel.

Do the following:

1. Configure the Pivot object as you normally would, giving it its default arrangement under Data in the properties.

   [Creating pivot tables](/en-US/cloud-servicves/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/pivot-object.htm)
2. Add additional row, column, and measure items that you want users to have access to, but that will not be in the table by default.
3. Hide these additional items from the default view by hovering over an item in the properties panel, and clicking ![Hide](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view_outline.svg).

   Hiding a data asset from the default view of the Pivot object. It will be available to use in chart exploration.

   ![Pivot object with sorted by first measure.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotObject_HideDataAsset.png "Click to view full size")

   Tip noteYou can choose to show hidden items again by default by clicking ![Show](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view_disabled_outline.svg) on them in the properties panel.

### Activating chart exploration

After you have prepared the data in the chart for chart exploration, you can activate it for users.

Do the following:

1. In the properties panel, expand Appearance > Chart exploration.
2. Toggle on Enable chart exploration.
3. Choose between the following under Visibility option:

   - Auto: Chart exploration panel is visible when users open the sheet.
   - Minimized: Chart exploration is turned on, but not visible when users open the sheet. Users can open it in the hover menu by clicking ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then ![Controls](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Chart exploration.

### Using chart exploration during analysis

When analyzing the chart, consumers can add, remove, and reorder data assets on the fly. This allows dynamic, flexible analysis that can help uncover additional insights from data. Users can also share, download, and bookmark the modified table state.

Information noteFor Pivot objects with chart exploration activated, chart exploration is either visible by default, or it can be opened in the ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu under ![Controls](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Chart exploration.

You use chart exploration in analysis mode. Add or remove rows, values, and columns from the Pivot object, re-sort data, change column width, and apply selections. You cannot change the size or layout of the entire chart on the sheet in chart exploration mode.

Tip note

The following actions are available in the panel header:

- ![Unselect all](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cleanse_outline.svg): Remove all currently selected items.
- ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reset_outline.svg): Reset all unsaved changes you made during analysis in the current session, including added or removed items, sorting, and more.
- ![Close exploration](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg): Close the panel.

If you customize a Pivot object using chart exploration mode, other users cannot see your changes, unless you save them as a public bookmark. This means that several users can alter the same chart, at the same time. Your changes will remain visible to you until your session ends. When this occurs, the chart will return to its default state, as set by the person who created it. If you want to save your layout, create a bookmark. For more information, see [*Creating bookmarks*](../../Bookmarks/create-bookmark.htm).

The chart exploration panel is not shown in the resulting chart that you have shared or downloaded.

Chart exploration of a Pivot object. In this image, the chart is in its default state—no data has been added, removed, or re-arranged.

![Pivot object in default configuration with chart exploration expanded.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotObject_ChartExploration_Default.png "Click to view full size")

Chart exploration of the same Pivot object as above, but with dimension row items changed (some added, some removed). Also, three new measures are added. Effectively, a new table has been constructed on the fly.

![Pivot object with chart exploration expanded and changes added on the fly to its configuration and data.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PivotObject_ChartExploration_Customized.png "Click to view full size")

## Selecting active fields from cyclic dimensions in pivot tables

If a pivot table uses a cyclic dimension, users can select the active fields from the cyclic dimension.

Do the following:

1. Click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) on a cyclic dimension column.
2. Click ![Cycle](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) <Dimension name> and select a dimension from the cyclic dimension.

## Expanding and collapsing dimensions during analysis

Depending on how it is configured, the Pivot table might allow you to expand and collapse items during analysis. Otherwise, all dimensions will already be expanded.

To expand a dimension, click ![Plus](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg). To collapse an expanded dimension, click ![Minus](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_minus_outline.svg).

You can also expand and collapse dimensions using the right-click and ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menus for the chart.

Do the following:

1. Right-click the chart, or open the options menu by selecting ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) from the hover menu.
2. Click Expand / collapse.
3. Use the available options:

   - ![Plus](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) Expand all: Expand all dimensions.
   - ![Minus](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_minus.svg) Collapse all: Collapse all dimensions.
   - ![Plus](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus.svg) Expand <Dimension name>: Expand a given dimension.
   - ![Minus](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_minus.svg) Collapse <Dimension name>: Collapse a given dimension.

## Learn more

- [*Pivot*](pivot-object.htm)
