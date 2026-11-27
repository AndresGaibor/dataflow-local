---
title: "Evaluate Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Evaluate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Evaluate Script function

Expand/Collapse all

# Evaluate Script function

Evaluate() finds if the input text string can be evaluated as a valid Qlik Sense expression, and if so, returns the value of the expression as a string. If the input string
is not a valid expression, NULL is returned.

Syntax:

Evaluate(expression\_text)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Information noteThis string function cannot be used in chart expressions.

Function example and results

| Function example | Result |
| --- | --- |
| Evaluate( 5 \* 8 ) | Returns 40 |

## Example - Evaluate fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called ExpressionText.
- A preceding load that uses the Evaluate function to evaluate the field ExpressionText and return two new fields: Evaluated and Evaluatedx4.

Load script

```
Example:
Load
ExpressionText
, Evaluate(ExpressionText) as Evaluated
, Evaluate(ExpressionText)*4 as Evaluatedx4
;
Load * Inline
[ExpressionText
4
5+3
100/5
123*2
329-9
0123456789012345678
1234567890123456789
0123456.5512
0123456.5512479994578952364859346469
Today()
Bob
];
```

Results

The following fields are loaded in the data table:

- ExpressionText
- Evaluated
- Evaluatedx4

Results table

| ExpressionText | Evaluated | Evaluatedx4 |
| --- | --- | --- |
| 4 | 4 | 16 |
| 5+3 | 8 | 32 |
| 100/5 | 20 | 80 |
| 123\*2 | 246 | 984 |
| 329-9 | 320 | 1280 |
| 0123456789012345678 | 0123456789012345678 | 4.9382715604938e+17 |
| 1234567890123456789 | 1234567890123456789 | 4.9382715604938e+18 |
| 0123456.5512 | 0123456.5512 | 493826.2048 |
| 0123456.5512479994578952364859346469 | 0123456.5512479994578952364859346469 | 493826.204992 |
| Today() | 11/5/2024 | 182404 |
| Bob | - | - |

The output of the Evaluate function returns values for all ExpressionText strings except the last row. The string Bob cannot be evaluated, so the function returns no value - NULL. All rows have been evaluated, for example the second row adds 5 and 3 to return 8. Some of the ExpressionText strings return the string as-is because the string already evaluates to a number. For example, the string 0123456789012345678 evaluates to the same number.

Although Qlik Sense has a 14-digit precision limit for numeric values, the Evaluate function evaluated 18-digit strings as a number and applied multiplication within the script. This is useful for handling very large numbers within the script.

## Example - Evaluate scenario

Load script

Overview

A dataset of sales data contains products, prices, and discounts. This example derives the discounted price for the products.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Product
  - Price
  - Discount %
- A preceding load which takes the Price and Discount % values and calculates an additional field called DiscountedPrice. This new field uses the Evaluate function to calculate the price minus the discount.

Load script

```
Example:
LOAD
Product,
Price,
[Discount (%)],
Price * (1 - ​​Evaluate([Discount (%)] / 100)) AS DiscountedPrice
INLINE [
Product, Price, Discount (%)
Laptop, 1000, 15
Smartphone, 800, 10
Tablet, 600, 20
Headphones, 200, 5
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Product
- Price
- Discount %
- DiscountedPrice

Results table

| Product | Price | Discount % | DiscountedPrice |
| --- | --- | --- | --- |
| Headphones | 200 | 5 | 190 |
| Tablet | 600 | 20 | 480 |
| Smartphone | 800 | 10 | 720 |
| Laptop | 1000 | 15 | 850 |

The output of the Evaluate function demonstrates how you can use the function to compute values.
