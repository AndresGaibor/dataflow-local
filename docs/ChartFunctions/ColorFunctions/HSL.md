---
title: "HSL Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/ColorFunctions/HSL.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Color functions"]
---

# HSL Script and chart function

Expand/Collapse all

# HSL Script and chart function

HSL() is used in expressions to set or evaluate the color properties of a chart object, where the color is defined by
values of hue, saturation, and luminosity between 0
and 1.

Syntax:

HSL (hue,
saturation, luminosity)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| hue, saturation, luminosity | Hue, saturation, and luminosity component values ranging between 0 and 1. |

Information noteAll arguments must be expressions that resolve to integers
in the range 0 to 1.

If interpreting the numeric component and formatting it in hexadecimal notation, the RGB values of the color components are easier to see. For example, light green has the number 4 278 255 360, which in hexadecimal notation is FF00FF00 and RGB (0,255,0). This is equivalent to HSL (80/240, 240/240, 120/240) - a HSL value of (0.33, 1, 0.5).

Refer to [*Coloring a visualization*](../../Colors/color-a-visualization.htm) to find examples of how to use the color functions in visualizations, as well as details on the visualizations that support color by expression.

Example: Chart expression

| Example | Results |
| --- | --- |
| If(Sum(Sales)>Sum(Budget),HSL( 0.33, 1, 0.25),HSL(0, 1, 0.5)) | Returns purple or red depending on the value of the comparison between Sales and Budget. |

## Example - HSL fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Product
  - Sales

Load script

```
Example:
LOAD * Inline [
Product, Sales
Product A, 200
Product B, 500
Product C, 100
Product D, 300
Product E, 700
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Product

Create the following measure:

- =Sum(Sales), to calculate the sum of sales.

In the Properties panel of the Sum(Sales) measure, enter the following expression as the Background color expression. This will apply cell color according to the sales calculation for the product.

- =If(Sales > 400, HSL(.33, 1, 0.25), If(Sales >= 200 and Sales <= 400, HSL(.167, 1, 0.5), HSL(0, 1, 0.5)) )

Results table

| Product | Sum(Sales) |
| --- | --- |
| Product A | 200 |
| Product B | 500 |
| Product C | 100 |
| Product D | 300 |
| Product E | 700 |

In this example, observe the following:

- Sales values over 400, such as Product B and E, are highlighted with a green background.
- Sales values between 200 and 400, such as Product A and D, are highlighted with a yellow background.
- All other sales values are highlighted with a red background.

## Example - Highlighting profit data in a chart

Chart expression

Overview

A dataset contains sales figures. We want to analyze the data and highlight profit margins according to whether they are low, moderate, or high.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - SalesValue
  - Cost
  - ProfitMargin

Load script

```
Example:
LOAD * Inline [
Customer, SalesValue, Cost, ProfitMargin
Customer A, 500, 300, 40%
Customer B, 800, 750, 6.25%
Customer C, 400, 300, 25%
Customer D, 600, 550, 8.33%
Customer E, 900, 700, 22.22%
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =Sum(SalesValue), to calculate the sum of sales.
- =Sum(Cost), to calculate the total value of the cost of sales.
- =Sum(ProfitMargin), to sum the profit margin. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

In the Properties panel of the Sum(ProfitMargin) measure, enter the following expression as the Background color expression.

```
If(ProfitMargin > 0.3, HSL( 0.33, 1, 0.25),   // Green for high-profit customers
  If(ProfitMargin >= 0.1 and ProfitMargin <= 0.3, HSL( 0.11, 1, 0.5),   // Orange for moderate-profit customers
    HSL(0, 1, 0.5)   // Red for low-profit customers
  )
)
```

In the Appearance panel, under Presentation, turn off Totals.

Results table

| Customer | Sum(SalesValue) | Sum(Cost) | Sum([Profit Margin]) |
| --- | --- | --- | --- |
| Customer A | 500 | 300 | 40.00% |
| Customer B | 800 | 750 | 6.25% |
| Customer C | 400 | 300 | 25.00% |
| Customer D | 600 | 550 | 8.33% |
| Customer E | 900 | 700 | 22.22% |

The output from the HSL function renders the following colors according to the customer's profit margin:

- Green, HSL( 0.33, 1, 0.25), for customers with profit margins higher than 30%.
- Orange, HSL( 0.11, 1, 0.5), for customers with moderate profit margins between 10% and 30%.
- Red, HSL(0, 1, 0.5), for customers with a profit margin below 10%.

## Example - HSL chart scenario

Chart expression

Overview

A dataset contains actual and projected sales data by country. A sales manager wants to display the data in a bar chart and highlight those sales figures that are higher than the projected value for the period.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Country
  - ActualSales
  - ProjectedSales

Load script

```
Example:
Load * Inline
[Country, ActualSales, ProjectedSales
Sweden, 100000, 50000
Germany, 125000, 175000
Norway, 74850, 68500
Ireland, 45000, 48000
Sweden, 98000, 50000
Germany, 115000, 175000
Norway, 71850, 68500
Ireland, 31000, 48000
];
```

Results

Load the data and open a sheet. Create a new bar chart and add this field as dimension:

- Country

Create the following measure:

- =Sum(ActualSales), to calculate the total value of sales for the country.

Add a color expression to compare actual sales with projected sales. In the properties panel, under Appearance > Colors and legend, turn off Colors: Auto to switch to Custom, and then select By expression from the list. Enter the following expression:

- =If(Sum(ActualSales)>Sum(ProjectedSales),HSL(1.2,1.0,0.25),HSL(0, 1.0, 0.25)), to highlight in green the occurrences where actual sales exceeds projected sales and in red where projected sales exceeds actual sales.

Results: Bar chart of sales by country

![Bar chart showing sum of sales by country. Sales columns appear green for countries where actual sales is higher than projected sales and red where actual sales is less than projected sales.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/hsl-barchart.png "Click to view full size")

We can see that the bar color is green for those countries with sales that exceed the projected value, whereas those with sales below the projected value appear red. For example, Sweden is green because its sales value of 98,000 is greater than the projected value of 50,000.
