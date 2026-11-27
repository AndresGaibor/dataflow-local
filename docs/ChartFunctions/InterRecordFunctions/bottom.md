---
title: "Bottom - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/bottom.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Bottom - chart function

Expand/Collapse all

# Bottom - chart function

Bottom() evaluates an expression at the last (bottom) row of a column segment in a table. The row for which it is calculated depends on the value of offset, if present, the default being the bottom row. For
charts other than tables, the evaluation is made on the last row of the current column in the chart's straight table equivalent.

Syntax:

Bottom([TOTAL] expr
[ , offset [,count
]])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| offset | Specifying an offset n greater than 1 moves the evaluation of the expression up n rows above the bottom row. Specifying a negative offset number makes the Bottom function work like the Top function with the corresponding positive offset number. |
| count | By specifying a third parameter count greater than 1, the function will return not one but a range of count values, one for each of the last count rows of the current column segment. In this form, the function can be used as an argument to any of the special range functions. [*Range functions*](../RangeFunctions/RangeFunctionsInCharts.htm) |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

Information noteA column segment is defined as a consecutive subset of cells having the same values for the dimensions in the current sort order. Inter-record chart functions are computed in the column segment excluding the right-most dimension in the equivalent straight table chart. If there is only one dimension in the chart, or if the TOTAL qualifier is specified, the expression evaluates across full table.

Information noteIf the table or table equivalent has multiple vertical dimensions, the
current column segment will include only rows with the same values as
the current row in all dimension columns, except for the column showing the last dimension in the inter-field sort order.

Limitations:

- Recursive calls will return NULL.
- Sorting on y-values in charts or sorting by expression columns in tables is not allowed when this chart function is used in any of the chart's expressions. These sort alternatives are therefore automatically disabled. When you use this chart function in a visualization or table, the sorting of the visualization will revert back to the sorted input to this function.

Example: Chart expressions

| Example | Result |
| --- | --- |
| Bottom( Sum(Sales) ) | Returns the value of Sales for the last (bottom) row of a column segment in a table. |

## Example - Bottom fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Year
  - Sales

Load script

```
Example:
LOAD * INLINE [
Year, Sales
2019, 1000
2020, 1500
2021, 1200
2022, 1800
2023, 1700
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Year

Create the following measures:

- =Sum(Sales), to find the annual sales.
- =Bottom(Sum(Sales)), to find the sales value for the last year.
- =Sum(Sales) - Bottom(Sum(Sales)), to calculate the variance between the Sales value of the current year and the value of the last year.
- =Sum(Sales)+Bottom(Sum(Sales), 3), to calculate the sum of the sales value of the current year and the value of the third last year.
- =(Sales - Bottom(Sales)) / Bottom(Sales), to return the change in Sales as a ratio / percentage as compared to the last year. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Sort the table on the dimension Year in ascending order.

Results table

| Year | Sum(Sales) | Bottom(Sum(Sales)) | Sum(Sales) - Bottom(Sum(Sales)) | Sum(Sales)+Bottom(Sum(Sales), 3) | (Sales - Bottom(Sales)) / Bottom(Sales) |
| --- | --- | --- | --- | --- | --- |
| Totals | 7200 | 1700 | 5500 | 8400 | - |
| 2019 | 1000 | 1700 | -700 | 2200 | -41.18% |
| 2020 | 1500 | 1700 | -200 | 2700 | -11.76% |
| 2021 | 1200 | 1700 | -500 | 2400 | -29.41% |
| 2022 | 1800 | 1700 | 100 | 3000 | 5.88% |
| 2023 | 1700 | 1700 | 0 | 2900 | 0.00% |

Looking at the results, you can compare the Sales values in the current period with the last, or most recent, period.

- The Sum(Sales) - Bottom(Sum(Sales)) measure returns the change in Sales values, comparing the current period to the most recent period.
- The Sum(Sales)+Bottom(Sum(Sales), 3) measure returns the sum of Sales for the current row and the third most recent period.
- The (Sales - Bottom(Sales)) / Bottom(Sales) measure returns the change in Sales compared to the most recent period as a percentage.

Tip noteThis function can also be used in charts other than tables, for example bar charts.

Do the following:

Create a bar chart, and then add this field as a dimension:

- Year

Create the following measure:

- =Sum(Sales) - Bottom(Sum(Sales)), to return the variance in sales between the current period and the most recent period.

Bar chart showing results for the Bottom function

![Bar chart showing the variance in sales between the current period and the last period.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-bottom-example.png "Click to view full size")

Using the Bottom function in a bar chart provides a visual comparison of the variance between the sales of the current period versus the most recent period.

## Example - Bottom scenario

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - OrderID
  - Product
  - SalesValue
  - OrderDate

Load script

```
Example:
LOAD * INLINE [
OrderID, Product, SalesValue, OrderDate
1, "Product A", 500, '2023-01-10'
2, "Product B", 300, '2023-01-15'
3, "Product C", 450, '2023-02-01'
4, "Product D", 700, '2023-02-20'
5, "Product E", 350, '2023-03-05'
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Product

Create the following measures:

- =RangeAvg (Bottom(Sum(SalesValue),1,3)), to return the average of the 3 most recent rows.
- =Sum(SalesValue) - RangeAvg (Bottom(Sum(SalesValue),1,3)), to calculate the variance between the current row and the average of the 3 most recent rows.
- =Sum(SalesValue) to calculate the total SalesValue for the current row.

Results table

| Product | RangeAvg (Bottom(Sum(SalesValue),1,3)) | Sum(SalesValue) - RangeAvg (Bottom(Sum(SalesValue),1,3)) | Sum(SalesValue) |
| --- | --- | --- | --- |
| Totals | 500 | 1800 | 2300 |
| 2019 | 500 | 0 | 500 |
| 2020 | 500 | -200 | 300 |
| 2021 | 500 | -50 | 450 |
| 2022 | 500 | 200 | 700 |
| 2023 | 500 | -150 | 350 |

The results show how you can use the combination of the RangeSum function and the Bottom function to analyze and compare sales values.

## Example - Chart expression using Bottom

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Two data tables called Monthnames and Sales2013.

Load script

```
Monthnames:
LOAD *, Dual(MonthText,MonthNumber) as Month INLINE [
MonthText, MonthNumber
Jan, 1
Feb, 2
Mar, 3
Apr, 4
May, 5
Jun, 6
Jul, 7
Aug, 8
Sep, 9
Oct, 10
Nov, 11
Dec, 12
];

Sales2013:
Crosstable (MonthText, Sales) LOAD * inline [
Customer|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec
Astrida|46|60|70|13|78|20|45|65|78|12|78|22
Betacab|65|56|22|79|12|56|45|24|32|78|55|15
Canutility|77|68|34|91|24|68|57|36|44|90|67|27
Divadip|57|36|44|90|67|27|57|68|47|90|80|94
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =Bottom(Sum(Sales)), to show the sum of sales of the Customer in the bottom row.
- =Sum(Sales)+Bottom(Sum(Sales)), to add the Sum(Sales) value of the current Customer with the Customer in the bottom row.
- =Sum(Sales)+Bottom(Sum(Sales), 3), to add the Sum(Sales) value of the current Customer with the value for the Customer that is third from the bottom row.

Results table

| Customer | Sum(Sales) | Bottom(Sum(Sales)) | Sum(Sales)+Bottom(Sum(Sales)) | Sum(Sales)+Bottom(Sum(Sales), 3) |
| --- | --- | --- | --- | --- |
| Totals | 2566 | 757 | 3323 | 3105 |
| Astrida | 587 | 757 | 1344 | 1126 |
| Betacab | 539 | 757 | 1296 | 1078 |
| Canutilty | 683 | 757 | 1440 | 1222 |
| Divadip | 757 | 757 | 1514 | 1296 |

The measure Bottom(Sum(Sales)) returns 757 for all rows because this is the value of the bottom row: Divadip.

For the measure Sum(Sales)+Bottom(Sum(Sales)), the row Astrida returns 1344, which is the result of adding the Sum(Sales) value for Astrida and Divadip, the Customer in the bottom row.

For the measure Sum(Sales)+Bottom(Sum(Sales), 3), the argument offset is set to 3. The expression adds the Sum(Sales) value for the current row and the third row from the bottom, Betacab. For example, the value 1126 is returned for customer Astrida. This is the result of adding the Sum(Sales) value for Astrida and the SumSales for Betacab (587+539).

## Learn more

- [*Top - chart function*](top.htm)
