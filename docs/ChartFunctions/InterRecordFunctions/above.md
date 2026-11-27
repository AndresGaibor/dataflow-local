---
title: "Above - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/InterRecordFunctions/above.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---

# Above - chart function

Expand/Collapse all

# Above - chart function

Above() evaluates an expression at a row above the current row within a column segment in a table. The row for which it is calculated depends on the value of offset, if present, the default being the row directly above. For charts other than tables, Above() evaluates for the row above the current row in the chart's straight table equivalent.

Syntax:

Above([TOTAL] expr
[ , offset [,count]])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. |
| offset | Specifying an offset n, greater than 0, moves the evaluation of the expression n rows further up from the current row. Specifying an offset of 0 will evaluate the expression on the current row.  Specifying a negative offset number makes the Above function work like the Below function with the corresponding positive offset number. |
| count | By specifying a third argument count greater than 1, the function will return a range of count values, one for each of count table rows counting upwards from the original cell. In this form, the function can be used as an argument to any of the special range functions. [*Range functions*](../RangeFunctions/RangeFunctionsInCharts.htm) |
| TOTAL | If the table is one-dimensional or if the qualifier TOTAL is used as argument, the current column segment is always equal to the entire column. [*Defining the aggregation scope*](../define-aggregation-scope.htm) |

On the first row of a column segment, a NULL value is returned, as
there is no row above it.

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
| Above( Sum(Sales) ) | Returns the value of Sales for the row above the current row. |

## Example - Above fundamentals

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
- =Above(Sum(Sales)), to find the sales value for the previous year.
- =Sum(Sales) - Above(Sum(Sales)), to calculate the variance between the Sales value of the current year and the value of the previous year.
- =RangeSum(Above(Sales, 1, 2)), to demonstrate a rolling two-year aggregation of the previous two years of sales.
- =(Sales - Above(Sales)) / Above(Sales), to return the change in Sales as a ratio / percentage. To show this value as a percentage, under Number formatting, select Number > Formatting Simple > 12.34%.

Results table

| Year | Sum(Sales) | Above(Sum(Sales)) | Sum(Sales) - Above(Sum(Sales)) | RangeSum(Above(Sales, 1, 2) | (Sales - Above(Sales)) / Above(Sales) |
| --- | --- | --- | --- | --- | --- |
| Totals | 7200 | - | - | 0 | - |
| 2019 | 1000 | - | - | 0 | - |
| 2020 | 1500 | 1000 | 500 | 1000 | 50.00% |
| 2021 | 1200 | 1500 | -300 | 2500 | -20.00% |
| 2022 | 1800 | 1200 | 600 | 2700 | 50.00% |
| 2023 | 1700 | 1800 | -100 | 3000 | -5.56% |

Looking at the results, you can compare the Sales values in the current period with the previous period.

- The Sum(Sales)- Above(Sum(Sales)) measure returns the change in Sales values, comparing the current period to the previous period.
- The RangeSum(Above(Sales, 1, 2)) measure returns the sum of the previous two Sales values.
- The (Sales - Above(Sales)) / Above(Sales) measure returns the change in Sales compared to the previous period as a percentage.

Tip noteThis function can also be used in charts other than tables, for example bar charts.

Do the following:

Create a bar chart, and then add this field as a dimension:

- Year

Create the following measure:

- =Sum(Sales) - Above(Sum(Sales)), to return the year-on-year variance.

Bar chart showing results for the Above function

![Bar chart showing year-on-year variance for the sum of sales](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-above-example.png "Click to view full size")

Using the Above function in a bar chart provides a visual comparison of the variance between the sales of the current period versus the previous period.

## Example - Above scenario

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - SalesYear
  - SalesAmount

Load script

```
Example:
LOAD * INLINE [
SalesYear, SalesAmount
2019, 500
2020, 800
2021, 400
2022, 700
2023, 600
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- SalesYear

Create the following measures:

- =Sum(SalesAmount), to aggregate the sales.
- =RangeSum(Above(SalesAmount, 0, RowNo())), to calculate a running total of the SalesAmount values.

Results table

| SalesYear | Sum(SalesAmount) | RangeSum(Above(SalesAmount, 0, RowNo())) |
| --- | --- | --- |
| Totals | 3000 | 0 |
| 2019 | 500 | 500 |
| 2020 | 800 | 1300 |
| 2021 | 400 | 1700 |
| 2022 | 700 | 2400 |
| 2023 | 600 | 3000 |

The results show how you can use a combination of the RangeSum function and the Above function to create a cumulative running total.

Tip noteThis function can also be used in charts other than tables, for example bar charts.

Do the following:

Create a bar chart, and then add this field as a dimension:

- SalesYear

Create the following measure:

- =RangeSum(Above(SalesAmount, 0, RowNo())), to return the cumulative sales value.

Bar chart showing the cumulative sales value by year

![Bar chart showing cumulative sales value by sales year.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-above-example2.png "Click to view full size")

## Example - Chart expression using Above

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
- =Above(Sum(Sales)), to show the sum of sales in the previous row.
- =Sum(Sales)+Above(Sum(Sales)), to sum the sum of sales value with the sum of sales for the customer row above the current row.
- =Sum(Sales)+Above(Sum(Sales), 3), to sum the Sum(Sales) value for the current Customer to the value for the Customer that is three rows above.
- =IF(Sum(Sales)>Above(Sum(Sales)), 'Higher'), to add the label "Higher" to customers whose Sum(Sales) results are greater than the Sum(Sales) of the customer in the row above.

Results table

| Customer | Sum(Sales) | Above(Sum(Sales)) | Sum(Sales)+Above(Sum(Sales)) | Sum(Sales)+Above(Sum(Sales), 3) | IF(Sum(Sales)>Above(Sum(Sales)), 'Higher') |
| --- | --- | --- | --- | --- | --- |
| Totals | 2566 | - | - | - | - |
| Astrida | 587 | - | - | - | - |
| Betacab | 539 | 587 | 1126 | - | - |
| Canutility | 683 | 539 | 1222 | - | Higher |
| Divadip | 757 | 683 | 1440 | 1344 | Higher |

The measure Above(Sum(Sales)) returns NULL for the customer Astrida, because there is no row above it. The result for the customer Betacab shows the value of Sum(Sales) for Astrida. The result for Canutility shows the value for Sum(Sales) for Betacab, and so on.

For the measure Sum(Sales)+Above(Sum(Sales)), the row for Betacab returns the result of adding the Sum(Sales) values for the rows Betacab + Astrida (539+587). The result for the row Canutility shows the result of the addition of Sum(Sales) values for Canutility + Betacab (683+539).

The measure Sum(Sales)+Above(Sum(Sales), 3) has the argument offset, set to 3. This takes the value in the row that is 3 rows above the current row. It adds the Sum(Sales) value for the current Customer to the value for the Customer three rows above. For example, the Sum(Sales) for Divadip, is added to the Sum(Sales) for Astrida, the customer that is three rows above Divadip. The values returned for the first 3 Customer rows are null because there is no data.

The measure IF(Sum(Sales)>Above(Sum(Sales)), 'Higher'), returns the value Higher for customers Canutility and Divadip because their sales results are both highter than the sum of sales of the customer in the row above, Betacab and Canutility respectively.

Tip noteThis function can also be used in charts other than tables, for example bar charts.

Tip noteFor other chart types, convert the chart to the straight table equivalent so you can easily interpret which row the function relates to.

## Example - Above scenario based on sort order

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Three data tables called Monthnames, Sales2013, and Product.

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

Product:
LOAD * inline [
Customer|Product|OrderNumber|UnitSales|UnitPrice
Astrida|AA|1|4|16
Astrida|AA|7|10|15
Astrida|BB|4|9|9
Betacab|CC|6|5|10
Betacab|AA|5|2|20
Betacab|BB||| 25
Canutility|AA|||15
Canutility|CC| ||19
Divadip|CC|2|4|16
Divadip|DD|3|1|25
] (delimiter is '|');
```

```

```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Customer
- Product
- Month

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =Above(Sum(Sales)), to show the sum of sales in the previous row.

Results table

| Customer | Product | Month | Sum(Sales) | Above(Sum(Sales)) |
| --- | --- | --- | --- | --- |
| Totals | - | - | 2566 | - |
| Astrida | AA | Jan | 46 | - |
| Astrida | AA | Feb | 60 | 46 |
| Astrida | AA | Mar | 70 | 60 |
| Astrida | AA | Apr | 13 | 70 |
| Astrida | AA | May | 78 | 13 |
| Astrida | AA | Jun | 20 | 78 |
| Astrida | AA | Jul | 45 | 20 |
| Astrida | AA | Aug | 65 | 45 |
| Astrida | AA | Sep | 78 | 65 |
| Astrida | AA | Oct | 12 | 78 |
| Astrida | AA | Nov | 78 | 12 |
| Astrida | AA | Dec | 22 | 78 |
| Astrida | BB | Jan | 46 | - |
| Astrida | BB | Feb | 60 | 46 |

For charts with more than one dimension, the results of expressions containing the Above, Below, Top, and Bottom functions depend on the order in which the column dimensions are sorted by Qlik Sense. Qlik Sense evaluates the functions based on the column segments that result from the dimension that is sorted last. The column sort order is controlled in the properties panel under Sorting and is not necessarily the order in which the columns appear in a table.

In the results table, the last-sorted dimension is Month, so the Above function evaluates based on months. There is a series of results for each Product value for each month (Jan to Dec) - a column segment. This is followed by a series for the next column segment for each Month for the next Product. There will be a column segment for each Customer value for each Product.

## Example - Above scenario using a different sort order

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Three data tables called Monthnames, Sales2013, and Product.

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

Product:
LOAD * inline [
Customer|Product|OrderNumber|UnitSales|UnitPrice
Astrida|AA|1|4|16
Astrida|AA|7|10|15
Astrida|BB|4|9|9
Betacab|CC|6|5|10
Betacab|AA|5|2|20
Betacab|BB||| 25
Canutility|AA|||15
Canutility|CC| ||19
Divadip|CC|2|4|16
Divadip|DD|3|1|25
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Customer
- Product
- Month

Create the following measures:

- =Sum(Sales), to calculate the sum of sales.
- =Above(Sum(Sales)), to show the sum of sales in the previous row.

Change the sort order of the table in the properties panel. Select  Sorting, and then drag the Product dimension to the third position in the sort order.

Results table

| Customer | Product | Month | Sum(Sales) | Above(Sum(Sales)) |
| --- | --- | --- | --- | --- |
| Totals | - | - | 2566 | - |
| Astrida | AA | Jan | 46 | - |
| Astrida | BB | Jan | 46 | 46 |
| Astrida | AA | Feb | 60 | - |
| Astrida | BB | Feb | 60 | 60 |
| Astrida | AA | Mar | 70 | - |
| Astrida | BB | Mar | 70 | 70 |
| Astrida | AA | Apr | 13 | - |
| Astrida | BB | Apr | 13 | 13 |
| Astrida | AA | May | 78 | - |
| Astrida | BB | May | 78 | 78 |
| Astrida | AA | Jun | 20 | - |
| Astrida | BB | Jun | 20 | 20 |
| Astrida | AA | Jul | 45 | - |
| Astrida | BB | Jul | 45 | 45 |

In table of results, the last sorted dimension is Product. The Above function is evaluated for each Product, and because there are only two products, AA and BB, there is only one non-null result in each series. In row BB for the month Jan, the value for Above(Sum(Sales)), is 46. For row AA, the value is null. The value in each row AA for any month will always be null, as there is no value of Product above AA. The second series is evaluated on AA and BB for the month Feb, for the Customer value, Astrida. When all the months have been evaluated for Astrida, the sequence is repeated for the second customer Betacab, and so on.

Information noteThe results in the table show only a partial list of the data. To see the complete results, try the example in an app.

## Example - Using the Above function with RangeAvg

Chart expression

Overview

The Above function can be used as input to the range functions. This example uses the function in a RangeAvg.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- Three data tables called Monthnames, Sales2013, and Product.

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

Product:
LOAD * inline [
Customer|Product|OrderNumber|UnitSales|UnitPrice
Astrida|AA|1|4|16
Astrida|AA|7|10|15
Astrida|BB|4|9|9
Betacab|CC|6|5|10
Betacab|AA|5|2|20
Betacab|BB||| 25
Canutility|AA|||15
Canutility|CC| ||19
Divadip|CC|2|4|16
Divadip|DD|3|1|25
] (delimiter is '|');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measure:

- =RangeAvg
  (Above(Sum(Sales),1,3))

Results table\*

| Customer | RangeAvg (Above(Sum(Sales),1,3)) |
| --- | --- |
| Totals | - |
| Astrida | - |
| Betacab | 587 |
| Canutility | 563 |
| Divadip | 603 |

In the arguments for the Above function, offset is set to 1 and count is set to 3. The function finds the results of
the expressionSum(Sales) on the three rows immediately above the
current row in the column segment (where there is a row). These three values are used as input to the RangeAvg function, which finds the average of the values in the supplied range of numbers.

## Learn more

- [*Below - chart function*](below.htm)
- [*Bottom - chart function*](bottom.htm)
- [*Top - chart function*](top.htm)
- [*RangeAvg Script and chart function*](../RangeFunctions/rangeavg.htm)
