---
title: "alt Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/alt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Conditional functions"]
---
Expand/Collapse all

# alt Script and chart function

The alt function returns the
first of the parameters that has a valid number representation. If no
such match is found, the last parameter will be returned. Any number of
parameters can be used.

Syntax:

alt(expr1[ , expr2
, expr3 , ...]
, else)

Return data type: integer

Arguments

| Argument | Description |
| --- | --- |
| expr1 | The first expression to check for a valid number representation. |
| expr2 | The second expression to check for a valid number representation. |
| expr3 | The third expression to check for a valid number representation. |
| else | Value to return if none of the previous parameters has a valid number representation. |

The alt function is often used with number or date interpretation functions. This way, Qlik Sense can test different date formats in a prioritized order. It can also be used to handle NULL values in numerical expressions.

Example: Chart expressions

| Example | Result |
| --- | --- |
| alt( date#( dat , 'YYYY/MM/DD' ),  date#( dat , 'MM/DD/YYYY' ),  date#( dat , 'MM/DD/YY' ),  'No valid date' ) | This expression will test if the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/alt.htm#glossary-0 "Glossary term") date contains a date according to any of the three specified date formats. If so, it will return a dual value containing the original string and a valid number representation of a date. If no match is found, the text `No valid date` will be returned (without any valid number representation). |
| alt(Sales,0) + alt(Margin,0) | This expression adds the fields `Sales` and `Margin`, replacing any missing value (NULL) with a `0`. |

## Example - alt fundamentals

Chart expression

Overview

A dataset contains incomplete sales and forecast data. You want to replace missing values with valid alternate values to fill the gaps.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ID`
  - `Sales`
  - `Forecast`

Load script

```
Example:
LOAD * INLINE [
ID, Sales, Forecast
1, 500, 450
2, , 300
3, 200, 250
4, , 400
5, 350,
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `Sales`
- `Forecast`

Create the following measure:

- `=Sum(alt(Sales, Forecast))` to return a valid number representation by replacing missing values with valid alternate values.

Results table

| ID | Sales | Forecast | Sum(alt(Sales, Forecast)) |
| --- | --- | --- | --- |
| Totals |  |  | 1750 |
| 1 | 500 | 450 | 500 |
| 2 |  | 300 | 300 |
| 3 | 200 | 250 | 200 |
| 4 |  | 400 | 400 |
| 5 | 350 |  | 350 |

The `alt` function returns the `Forecast` value in the measure calculation for the `ID` rows with missing `Sales` values. By replacing missing values with valid alternate values you can generate a fully populated dataset.

## Example - Using alt to replace missing values

Chart expression

Overview

A company collects temperature data from multiple sensors. You want to replace missing data from one sensor with the data from the other sensor.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `Time`
  - `Temp_Sensor1`
  - `Temp_Sensor2`

Load script

```
Example:
LOAD * INLINE [
Time, Temp_Sensor1, Temp_Sensor2
08:00, 23.5, 24.0
09:00, , 23.8
10:00, 24.1,
11:00, , 24.5
12:00, 23.9, 24.1
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Time`
- `Temp_Sensor1`
- `Temp_Sensor2`

Create the following measure:

- `=Sum(alt(Temp_Sensor1, Temp_Sensor2))` to return a valid number representation.

Results table

| Time | Temp\_Sensor1 | Temp\_Sensor2 | Sum(alt(Temp\_Sensor1, Temp\_Sensor2)) |
| --- | --- | --- | --- |
| Totals |  |  | 119.8 |
| 08:00 | 23.5 | 24.0 | 23.5 |
| 09:00 |  | 23.8 | 23.8 |
| 10:00 | 24.1 |  | 24.1 |
| 11:00 |  | 24.5 | 24.5 |
| 12:00 | 23.9 | 24.1 | 23.9 |

Looking at the results, the `alt` function has replaced missing sensor data with valid alternate results from the other sensor. This completes the dataset by filling in gaps.

## Example - alt scenario

Chart expression

Overview

This scenario shows different ways you can use the `alt` function to replace missing or null values.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `ProductID`
  - `ProductName`
  - `SalesAmount`
  - `ReturnAmount`
  - `Profit`
  - `Discount`
  - `Category`
  - `Year`
  - `Region`
  - `CustomerRating`

Load script

```
Set NullInterpret = '';
Example:
LOAD * INLINE [
ProductID, ProductName, SalesAmount, ReturnAmount, Profit, Discount, Category, Year, Region, CustomerRating
101, "Laptop", 1200, 200, 500, , "Electronics", 2023, "North",
102, "Tablet", 800, , 300, 50, "Electronics", 2023, "South", 4
103, "Smartphone", 1500, , 600, 100, , 2022, "East", 5
104, "Printer", 400, , , 20, "Accessories", 2021, , 3
105, , 1000, 100, , 30, "Electronics", 2023, "West", 4
106, "Monitor", , 150, 250, , "Accessories", 2022, "North", 5
107, "Keyboard", 200, , 80, 5, , 2022, "South", 2
108, "Mouse", , 50, , , "Accessories", , "East",
109, , 600, , , , "Electronics", 2023, , 4
110, "Headphones", 300, 30, 100, , "Accessories", 2021, "West", 3
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `ProductID`

Create the following calculated dimension:

- `=Coalesce( ProductName, 'Unknown Product')`, to provide the description `Unknown Product` for all products that have no value for `ProductName`.

Create the following measures:

- `=Sum(alt(SalesAmount, ReturnAmount, Profit))`, to return a valid number if no `SalesAmount` is found.
- `=avg(alt(CustomerRating, 3))`, to return a valid standardized customer rating if none is originally supplied.
- `=Sum(alt(Discount, SalesAmount * 0.05))`, to return a valid discount.
- `=Sum(alt(Profit, SalesAmount * 0.1))`, to return a valid profit value.
- `=Sum(alt(SalesAmount, avg(TOTAL SalesAmount)))`, to return a valid sales value.
- `=Sum(alt(Discount, avg(TOTAL Discount)))`, to return a valid discount value.

Results table

| ProductID | Coalesce( ProductName, 'Unknown Product') | Sum(alt(SalesAmount, ReturnAmount, Profit)) | avg(alt(CustomerRating, 3)) | Sum(alt(Discount, SalesAmount \* 0.05)) | Sum(alt(Profit, SalesAmount \* 0.1)) | Sum(alt(SalesAmount, avg(TOTAL SalesAmount))) | Sum(alt(Discount, avg(TOTAL Discount))) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Totals |  | 6200 | 3.6 | 310 | 2030 | 7500 | 410 |
| 101 | Laptop | 1200 | 3 | 60 | 500 | 1200 | 41 |
| 102 | Tablet | 800 | 4 | 50 | 300 | 500 | 50 |
| 103 | Smartphone | 1500 | 5 | 100 | 600 | 800 | 100 |
| 104 | Printer | 400 | 3 | 20 | 40 | 400 | 20 |
| 105 | Unknown Product | 1000 | 4 | 30 | 100 | 1000 | 30 |
| 106 | Monitor | 150 | 5 | 0 | 250 | 750 | 41 |
| 107 | Keyboard | 200 | 2 | 5 | 80 | 200 | 5 |
| 108 | Mouse | 50 | 3 | 0 | 0 | 750 | 41 |
| 109 | Unknown Product | 600 | 4 | 30 | 60 | 600 | 41 |
| 110 | Headphones | 300 | 3 | 15 | 100 | 300 | 41 |

The `alt` function ensures that when values are missing, alternate values can be calculated and returned. Observe the following results:

- Column 2 uses the `Coalesce` function to return the value `Unknown Product` for all null values. The `Alt` function cannot be used as it applies to only numeric values.
- Column 3 returns the value for `SalesAmount`. If no value is found then it returns the `ReturnAmount` value. If no `ReturnAmount` value is found, it returns the `Profit` value. This helps to ensure that the column is populated with a value if `SalesAmount` has no value.
- Column 4 returns the `CustomerRating`. If no value is found then this defaults to a value of `3`. For example, the product `Laptop` has no customer rating so `3` is returned. The measure then calculates the average for the column.
- Column 5 returns the discount value. If no value is available, it is calculated as 5% of the `SalesAmount` value.
- Column 6 returns the `Profit` value. If no value is available, it returns 10% of the `SalesAmount`.
- Column 7 returns the `SalesAmount`. If no value is supplied then the average `SalesAmount` across the entire dataset is returned. For example, the products `Monitor` and `Mouse` have no value for `SalesAmount`, so both return `750`, which is the average of all `SalesAmount` values.
- Column 8 returns the `Discount` value. If no value is found, then the system calculates and returns the average discount across the entire dataset.
