---
title: "Best practices for designing accessible applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/accessibility-analytic-apps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Best practices for designing accessible applications

Analytics applications support several accessibility features. Application creators can also take extra steps to improve accessibility and make sure that all users can access the information in their analytics applications.

Analytics applications support the following accessibility features:

- Default color schemes with high contrast
- Keyboard navigation and keyboard shortcuts

  [*Keyboard navigation and shortcuts in apps*](../UserInterface/keyboard-navigation-and-shortcuts.htm)
- Screen reader support

  [*Using Qlik Sense with a screen reader*](../UserInterface/accessibility.htm#Using)

When designing applications for accessibility, there are design best practices you should follow. Additionally, there are specific applications settings you can use to help make your applications more accessible.

## Design best practices

When designing for accessibility, follow these best practices:

- Keep a flat sheet structure
- Provide an overview first
- Use accessible colors
- Select visualizations for accessibility
- Avoid storytelling

### Keep a flat sheet structure

When adding visualizations to your sheets, use a flat structure with few columns and rows. A flat structure improves readability for your users. Additionally, it also makes keyboard navigation easier, as keyboard navigation moves from the top left to bottom right.

Complex sheet layouts with many columns and rows are both harder to understand and harder to navigate with a keyboard. When designing a sheet, try to navigate it with your keyboard to see how users may perceive your application.

A flat sheet layout

![A flat sheet layout with charts divided in two even rows. A bar chart and line chart are in the top row, and a pivot table is in the bottom row.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible_flat.png "Click to view full size")

A complex sheet layout

![A complext sheet layout, with irregularly placed visualizations.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible_complex.png "Click to view full size")

### Provide an overview first

When creating sheets, provide an overview first and then provide details. This makes it easier for users to consume information in your sheets. For example, start by providing summaries and KPIs in your sheets, and then provide more detail-heavy tables or other visualizations. You can also place details on another sheet. Alternatively, you could resize the sheet so that it is scrollable and put additional details further down the sheet.

For more information about changing sheet size, see [*Changing sheet layouts*](../Sheets/changing-sheet-layout.htm).

### Select the right visualizations

Analytic applications provide a range of visualizations for use in analytics. Some visualizations are better choices that other when designing accessible applications. Keep the following in mind when selecting visualizations:

- Use charts with data view
- Use the Straight table visualization
- Avoid using map charts
- Avoid using custom objects

#### Use charts with data view

When designing your application, use charts with data view. Data view lets users change the chart to a table, helping them to inspect and select values.

A pie chart with the same pie chart in data view

![An image of a pie chart with the data view of the pie chart beside it.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible-data-view.png "Click to view full size")

Data view is available in the following charts:

- Bar chart
- Box plot (with one or more dimensions)
- Combo chart
- Distribution plot
- Histogram
- Line chart
- Pie chart
- Pivot table
- Scatter plot
- Treemap

For more information, [*Viewing data of visualizations*](../Visualizations/viewing-data-visualizations.htm).

#### Use the straight table

The Straight table has an improved navigation experience compared to the Table visualization, the former default table visualization. When adding tables to an accessible application, use the straight table instead of the table.

For optimal accessibility, turn on the Use pagination and Increased accessibility settings in your straight table. These settings are available in the properties panel under Appearance > Presentation > Accessibility options. For more information, see [*Managing accessibility settings*](../Visualizations/StraightTable/sn-straight-table-appearance.htm#Accessibility).

For more information, see [*Straight table*](../Visualizations/StraightTable/sn-straight-table.htm).

#### Avoid using map charts

The map chart is not navigable with keyboard navigation. When creating accessible applications, consider using alternative ways of presenting your geographic data.

#### Avoid using custom objects

The charts in the Dashboard or Visualization bundles may not be as accessible as other charts. They are not recommended for use in accessible applications. Additionally, if you do use extensions, test them to confirm they are accessible for your users.

### Use accessible colors

The spectrum of colors is narrower for people with color-based visual impairment. They may interpret your visualizations differently than you intended. For example, some users may have difficulty with reds and greens in your visualizations. Lines, bars, and pie slices can also be difficult to distinguish when the colors do not have enough contrast.

It is best to use a simple color scheme in your application. The default application color schemes each have 12 colors that contrast with each other. It is better to use three to five colors if possible, or even a color scheme based on a single color. You can create your own custom color schemes and use them in all your accessible applications. For more information, see [Create custom themes](https://qlik.dev/extend/create-custom-themes/).

You can also set some colors manually, separately from themes. For dimensions, you can set assign colors to values in master dimensions. For more information, see [*Assigning colors to master dimension values*](../Colors/assigning-colors-to-dimension-values.htm). You can also color by expressions to set colors. For more information, see [*Color by expression*](../Colors/color-by-expression.htm). To learn more about coloring options for visualizations, see [*Coloring a visualization*](../Colors/color-a-visualization.htm).

#### Adding shapes as performance indicators in KPIs

Consider adding shapes as performance indicators in your KPIs. These add context and make your KPIs more accessible. For example, you could use a red empty circle to denote bad results, a green full circle for good results, and a triangle as a warning symbol that only appears when a KPI status is at an unacceptable level. For more information, see [*Adding shapes to KPIs*](#Adding).

KPI using performance indicator shapes

![KPI using a downwards pointing triangle for a negative result and an upward triangle for a positive result.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible-KPI-ex.png "Click to view full size")

### Avoid storytelling

While stories are useful for presenting discoveries, sheets are more accessible for keyboard navigation and screen readers. In applications designed for accessibility, it is better to use sheets to present your discoveries.

## Accessible application settings

Analytics applications have a range of settings that can help improve the accessibility of your applications.

### Sheet settings

There are several settings you can change in your sheets to improve accessibility:

- Improve sheet title contrast
- Turn off the hover menu

#### Improving sheet title contrast

You can improve the visibility of sheet titles by styling them to contrast with your sheets.

Do the following:

1. In the application navigation bar, click your application title.
2. Click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) to open settings.
3. Under Sheet title styling, adjust your color settings to improve contrast.
4. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
5. In the menu, switch to the Sheet header styling tab.
6. Adjust your color settings to improve contrast.

#### Turning off the hover menu

Turning off the hover menu allows for a smoother navigation experience. There is no loss of functionality as the options are also available through the context menu and keyboard shortcuts.

Do the following:

1. In the application navigation bar, click your application title.
2. Click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) to open settings.
3. Under Appearance, turn off Show hover menu for visualizations.
4. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
5. In the menu, switch to the Appearance tab.
6. Turn off Hover menu for visualizations.

### Chart settings

Some charts have options that can help make them more accessible to users. You can:

- Provide text descriptions
- Limit dimension values in visualizations
- Add shapes to KPIs

#### Providing text descriptions

Visualizations come with fields for titles, subtitles, and footnotes. Providing accurate text descriptions can help your users navigate your visualizations and provide context to your sheets. Without context, it can take users longer to find the information that interests them in your sheets. Titles, subtitles, and footnotes are all read by screen readers as well.

You can find titles, subtitles, and footnotes in the properties panel, under Appearance > General.

#### Limit dimension values in visualizations

When working with nominal data in dimensions, try to find hierarchies or make aggregations if the number of categories is greater than 10. For example, displaying the top 10 values, with the rest categorized as others, makes your data easier to understand and read aloud. If you need to include full details, you can include them at the end of the sheet or other sheets.

Do the following:

1. Select a visualization.
2. In the properties panel, under Data, select your dimension.
3. Under Limitation, select one of the following:

   - Fixed number: Select to display the top or bottom values. Set the number of values. You can also use an expression to set the number. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Exact value: Use the operators and set the exact limit value. You can also use an expression to set the number. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
   - Relative value: Use the operators and set the relative limit value in percent. You can also use an expression to set the number. Click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.

#### Abbreviate numbers

Reading, listening to, and understanding long numbers can be a challenge. Where possible, abbreviate your numbers to keep the number of digits and decimals low.

You can use functions such as Ceil and Round to round numbers. For example, if you wanted to round measure values to the millions with one decimal place, you could use =Round(Sum(Sales)/1000000, 0.1).

For more information, see:

- [*Ceil Script and chart function*](../ChartFunctions/GeneralNumericFunctions/ceil.htm)
- [*Round Script and chart function*](../ChartFunctions/GeneralNumericFunctions/round.htm)

#### Adding shapes to KPIs

If you are using conditional coloring for your KPIs, you can add symbols in addition to the color. Symbols can be used to provide additional performance indicators.

Do the following:

1. Select a KPI visualization, and switch to the properties panel in the advanced edit mode.
2. Select Appearance and expand Color.
3. If necessary, turn off Library colors and turn on Conditional colors.
4. Click Add limit to create a new limit. Multiple limits can be added to a single KPI chart.
5. Specify a value for the limit, or enter an expression using the expression editor.
6. On the Value color bar, click the range area of the KPI you would like to modify.
7. Under Colors, select a preset color or use a custom color.
8. Select Symbols and choose the symbol displayed when your KPI falls within the specified limit.

#### Use dynamic titles

When making visualizations, use dynamic titles to capture the essence of the chart. Rather than just a generic title, consider building an expression for the title that provides information dynamically based on user selections.

By using set analysis combined with max(), min(), rank(), and correl() to build the titles, you can present more dynamically descriptive charts.

For example, this visualization has a static title.

Static title

![A line chart with a static title of Sales per Year, showing a increasing trend of sales between 2018 and 2021.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible_static-title.png "Click to view full size")

If dynamic expressions were added to the title and subtitle, the chart would express information more dynamically and provide users with more information.

Dynamic title and subtitles

![A line chart with a dynamic title of 'Sales up 3.2% in the last period'. This highlights the changes in the last period. The chart shows an increasing trend of sales between 2018 and 2021. The subtitle is '+668.3% from 2018 to 2021', showing the overall increase.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible_dynamic-title.png "Click to view full size")

The advantage of the dynamic titles is that it changes based on user selections. In the visualization below, the three top countries for sales have been selected, changing the title and subtitle of the visualization.

Dynamic title and subtitles after selections

![The line chart's dynamic title has changed to 'Sales down 6.4% in the last period'. The chart shows an overall increasing trend of sales, with a decline between between 2020 and 2021. The subtitle is '+818.6.3% from 2018 to 2021', showing the overall increase for the top 3 countries for sales.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_accessible_dynamic-title-changed.png "Click to view full size")
