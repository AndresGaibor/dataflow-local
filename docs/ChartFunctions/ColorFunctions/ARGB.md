---
title: "ARGB Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/ColorFunctions/ARGB.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Color functions"]
---

# ARGB Script and chart function

Expand/Collapse all

# ARGB Script and chart function

ARGB() is used in expressions to set or evaluate the color properties of a chart object, where the color is defined by a red component r, a green
component g, and a blue component
b, with an alpha factor (opacity)
of alpha.

Syntax:

ARGB(alpha,
r, g,
b)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| alpha | Transparency value in the range 0 - 255. A 0 corresponds to full transparency and 255 corresponds to full opacity. |
| r, g, b | Red, green, and blue component values. A color component of 0 corresponds to no contribution and one of 255 to full contribution. |

Information noteAll arguments must be expressions that resolve to integers
in the range 0 to 255.

If interpreting the numeric component and formatting it in hexadecimal notation, the values of the color components are easier to see. For example, light green has the number 4 278 255 360, which in hexadecimal notation is FF00FF00. The first two positions ‘FF’ (255) denote the alpha channel. The next two positions ‘00’ denote the amount of red, the next two positions ‘FF’ denote the amount of green, and the final two positions ‘00’ denote the amount of blue.

Refer to [*Coloring a visualization*](../../Colors/color-a-visualization.htm) to find examples of how to use the color functions in visualizations, as well as details on the visualizations that support color by expression.

Example: Chart expression

| Example | Results |
| --- | --- |
| ARGB(128, 0, 128, 0) | Returns the color green with semitransparency. |

## Example - ARGB fundamentals

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

- =If(Sales > 400, ARGB(128, 0, 128, 0), If(Sales >= 200 and Sales <= 400, ARGB(128, 255, 255, 0), ARGB(128, 255, 0, 0)) )

Results table

| Product | Sum(Sales) |
| --- | --- |
| Product A | 200 |
| Product B | 500 |
| Product C | 100 |
| Product D | 300 |
| Product E | 700 |

In this example, observe the following:

- Sales values over 400 are highlighted with a green background.
- Sales values between 200 and 400 are highlighted with a yellow background.
- All other sales values are highlighted with a red background.

## Example - Highlighting profit data in a chart

Chart expression

Overview

A dataset contains sales figures by customer. We want to analyze the data and highlight profit margins according to whether they are low, moderate, or high.

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
If(ProfitMargin > 0.3, ARGB(128, 0, 128, 0),   // Green for high-profit customers
  If(ProfitMargin >= 0.1 and ProfitMargin <= 0.3, ARGB(128, 255, 165, 0), // Orange for moderate-profit customers
    ARGB(128, 255, 0, 0) // Red for low-profit customers
  )
)
```

In the Appearance panel, under Presentation, turn off Totals.

Results table

| Customer | Sum(SalesValue) | Sum(Cost) | Sum(Profit Margin) |
| --- | --- | --- | --- |
| Customer A | 500 | 300 | 40.00% |
| Customer B | 800 | 750 | 6.25% |
| Customer C | 400 | 300 | 25.00% |
| Customer D | 600 | 550 | 8.33% |
| Customer E | 900 | 700 | 22.22% |

The output from the ARGB function renders the following colors according to the customer's profit margin:

- Green, ARGB(128, 0, 128, 0), for customers with profit margins higher than 30%.
- Orange, ARGB(128, 255, 165, 0), for customers with moderate profit margins between 10% and 30%.
- Red, ARGB(128, 255, 0, 0), for customers with a profit margin below 10%.

## Example - ARGB chart scenario

Chart expression

Overview

A dataset contains actual and projected sales data by country. A sales manager wants to display the data in a bar chart and highlight the sales figures that are higher than the projected value for the period .

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

- =If(Sum(ActualSales)>Sum(ProjectedSales),ARGB(128,0,128,0),ARGB(128,128,0,0)), to highlight in green the occurrences where actual sales exceeds projected sales and in red where projected sales exceeds actual sales.

Results: Bar chart of sales by country

![Bar chart showing sum of sales by country. Sales columns appear green for countries where actual sales is higher than projected sales and red where actual sales is less than projected sales.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/argb-barchart.png "Click to view full size")

We can see that the bar color is green for those countries with sales that exceed the projected value, whereas those with sales below the projected value appear red. For example, Sweden is green because its sales value of 98,000 is greater than the projected value of 50,000.
