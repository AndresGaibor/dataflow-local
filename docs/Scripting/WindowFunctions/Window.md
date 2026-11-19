---
title: "Window Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/Window.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Window functions"]
---
Expand/Collapse all

# Window Script function

**Window()** performs calculations from multiple rows of a section (or "window") of a complete table, and produces a single value for each row.

You can use the **Window** functions to perform operations such as:

- Comparing an individual number value in a row with the average, maximum, or minimum within a window of the table.
- Calculating the rank of an individual value, either within the window or within the entire table.

[Video: https://share.vidyard.com/watch/KddMeUa2GDAvFQ3vFFroPy]

The **Window** function does not change the number of records in the table, but it can still perform similar tasks as aggregation, relational, and range functions.

The **Window** function must be included within the LOAD statement of the table you are working with, or reference the table such as with a Resident LOAD. For example, see [*Example - Adding a field containing an aggregation*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/Window.htm#Example2).

The name can be omitted, but this results in the field name being set to the entirety of the **Window** function expression. For example, AvgDepSalary in the example below:

[AvgSalary]:
Load
\*,
Window(avg(Salary), Department) as AvgDepSalary
Resident Employees;

> **Note:** It is recommended to give the **Window** function a field name.

**Window** supports general functions, such as rounding or basic numerical operations. For example:

Load \*, Round(Window(Sum(Salary),Department)) as SumDepSalary

Load \*, Window(Sum(Salary),Department) + 5 as SumDepSalary

> **Note:** The **Window** function scans the full table. In terms of memory consumption, the cost of this scanning is proportional to the number of fields in the table. A table with a few fields, besides the ones over which the **Window** function is operating, is always to be preferred over a table with many fields.
>
> Typically, a **Window** function consumes 2-4 times the memory, and takes 2-4 times longer in reload time when compared to a similar script operation containing the same aggregation, a `Where` clause (filter), a `Group by` clause (partition) and an `Order by` clause (sort).

Syntax:

Window (main\_expr, [partition1, partition2, ...], [sort\_type, [sort\_expr],[filter\_expr], [start\_expr, end\_expr]])

Return data type: One value per row, which can be combined with or used in another expression, or added directly to the resulting table created by the LOAD statement.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| main\_expr | The main input expression calculated and returned by the function. It must be any expression based on an aggregation, such as `Median(Salary)`. For example:  Window(Median(Salary)) as MedianSalary  The expression can also be a field name with no aggregation applied. In this case, **Window** treats it like the **Only()** function is applied to that field. For example:  Window(Salary) as WSalary  Expressions that include nested aggregations or nested window functions, such as `Window(Sum(Avg(Salary)))` or `Window(Sum(Window(Salary)))` are not permitted. |
| partition1, partition2 | After main\_expr, you can define any number of partitions. Partitions are fields that define which combinations to apply the aggregations with. For example:  Window(Avg(Salary), Department) as AvgDepSalary  This calculates the average salary for each department.  When several partition parameters are provided, the aggregation will be applied to each row with a unique combination of partition fields. For example:  Window(Avg(Salary), Department, Country) as AvgDepSalaryPerCountry  This calculates the average salary for each department in each country. Duplicate departments in different countries, such as Marketing in Sweden and Marketing in Canada, will be treated as different partitions.  Partitioning is similar to the grouping achieved by the **group by** clause. Partitioning does not reduce the number of records compared to the input table, however. |
| sort\_type, [sort\_expr] | Optionally, specify the sort type and the sort expression. This defines the order in which the aggregation is performed. sort\_type is a constant string and can have one of three values:   - ASC: Ascending sort. - DESC: Descending sort. - NONE   If you define sort\_type ASC or DESC, then you need to define a sorting expression. With sort\_type NONE, no sorting expression should be provided. The sorting expression decides the order of the rows within a partition.  For example:  Window(RecNo(), Department, 'ASC', Year)  In the above example, the aggregation within the partition is performed ascendingly by the Year field.  The sorting parameters also affect the order in which a sliding window processes a table. For an example, see [*Example - Adding a field with a sorted sliding window*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/WindowFunctions/Window.htm#Example3). |
| filter\_expr | Optionally, add a filter expression. This is a Boolean expression that decides whether the record should be included in the calculation or not.  If filter\_expr is provided then a sort type should be included. If no sort type is defined, then argument may be interpreted as a partition parameter rather than a filter expression. The filter\_expr parameter can be omitted completely or a truthy value can be included. Both of these result in no filters being used so no rows are excluded.  For example:  Window(avg(Salary), Department, 'ASC', Age, Country='US' Or Country='Canada') as AvgDepSalaryInUsOrCanada  The above **Window** statement will filter away any row where the Country field is not US or Canada, excluding those rows from the aggregation. There will still be output values for the rows that were filtered out, but like all the other output rows they will only contain aggregated results from rows that are not excluded by the filter. |
| start\_expr,end\_expr | Optionally, set the arguments for sliding window functionality. This further limits the number of rows to be aggregated together. Each output row will only include (aggregated) results from a number of rows preceding and succedent to the current row. A sliding window requires two arguments (start\_expr,end\_expr). If these arguments are provided, then sort type should not be skipped. Otherwise, the arguments may be interpreted as a partition parameter instead of sliding window. The parameter start\_expr,end\_expr comprise:   - Start expression: The number of rows prior to the current row to include in the window. - End expression: The number of rows after the current row to include in the window.   For example, if you wanted to include the 3 preceding rows, the current row, and the following row:  Window(concat(Text(Salary),'-'), Department, 'NONE', 1, -3, 1) as WSlidingSalaryDepartment  To indicate all preceding rows or all subsequent rows, you can use the **Unbounded()** function. For example, to include all preceding rows, the current row, and the following row:  Window(concat(Text(Salary),'-'), Department, 'NONE', 1, UNBOUNDED(), 1) as WSlidingSalaryDepartment  For example, to include the third row from the current row and all subsequent rows:  Window(concat(Text(Salary),'-'), Department, 'NONE', 1, 3, UNBOUNDED()) as WSlidingSalaryDepartment  In the examples above, the sort type NONE is provided so that the script can distinguish between partition arguments and the parameters that come after sort type. |

## Example - Adding a field containing an aggregation

Example: Adding a field containing an aggregation

Load script

Create a new tab in the data load editor, and then load the following data as an inline load. Create the table below in Qlik Sense to see the results.

```
[Employees]:
Load 
	*,
	Window(avg(Salary), Department) as AvgDepSalary
Inline [
	Name, Department, Salary, Age, Year, Country
	David, Sales, 11, 32, 2019, Canada
	Sara, Sales, 22, 25, 2022, Sweden
	Nils, Marketing, 33, 18, 2022, Sweden
	Patrick, Marketing, 44, 43, 2022, Canada
	Anna, Sales, 55, 33, 2023, Canada
	Johan, Sales, 66, 26, 2025, Sweden
	Olle, Marketing, 77, 19, 2023, Sweden
	Bonnie, Marketing, 88, 44, 2023, US
];
```

Results

Results for adding a field containing an aggregation

| Name | Department | Salary | Age | Year | Country | AvgDepSalary |
| --- | --- | --- | --- | --- | --- | --- |
| David | Sales | 11 | 32 | 2019 | Canada | 39 |
| Sara | Sales | 22 | 25 | 2022 | Sweden | 39 |
| Nils | Marketing | 33 | 18 | 2022 | Sweden | 61 |
| Patrick | Marketing | 44 | 43 | 2022 | Canada | 61 |
| Anna | Sales | 55 | 33 | 2023 | Canada | 39 |
| Johan | Sales | 66 | 26 | 2025 | Sweden | 39 |
| Olle | Marketing | 77 | 19 | 2023 | Sweden | 61 |
| Bonnie | Marketing | 88 | 44 | 2023 | US | 61 |

## Example - Adding a field containing an aggregation filtered for specific values

Example: Adding a field containing an aggregation filtered for specific values

Load script

Create a new tab in the data load editor, and then load the following data as an inline load. Create the table below in Qlik Sense to see the results.

```
[Employees]:
Load 
*,
Window(avg(Salary), Department, 'NONE', Country = 'Sweden') as AvgDepSalarySweden
Inline [
	Name, Department, Salary, Age, Year, Country
	David, Sales, 11, 32, 2019, Canada
	Sara, Sales, 22, 25, 2022, Sweden
	Nils, Marketing, 33, 18, 2022, Sweden
	Patrick, Marketing, 44, 43, 2022, Canada
	Anna, Sales, 55, 33, 2023, Canada
	Johan, Sales, 66, 26, 2025, Sweden
	Olle, Marketing, 77, 19, 2023, Sweden
	Bonnie, Marketing, 88, 44, 2023, US
];
```

Results

Results for adding a field containing an aggregation filtered for specific values

| Name | Department | Salary | Age | Year | Country | AvgDepSalarySweden |
| --- | --- | --- | --- | --- | --- | --- |
| David | Sales | 11 | 32 | 2019 | Canada | 44 |
| Sara | Sales | 22 | 25 | 2022 | Sweden | 44 |
| Nils | Marketing | 33 | 18 | 2022 | Sweden | 55 |
| Patrick | Marketing | 44 | 43 | 2022 | Canada | 55 |
| Anna | Sales | 55 | 33 | 2023 | Canada | 44 |
| Johan | Sales | 66 | 26 | 2025 | Sweden | 44 |
| Olle | Marketing | 77 | 19 | 2023 | Sweden | 55 |
| Bonnie | Marketing | 88 | 44 | 2023 | US | 55 |

## Example - Adding a field with a sliding window

Example: Adding a field with a sliding window

Load script

Create a new tab in the data load editor, and then load the following data as an inline load. Create the table below in Qlik Sense to see the results.

```
[Employees]:
Load 
	*,
	Window(concat(Text(Salary),'-'), Department, 'NONE', -1, 1) as SlidingWindow
Inline [
	Name, Department, Salary, Age, Year, Country
	David, Sales, 11, 32, 2019, Canada
	Sara, Sales, 22, 25, 2022, Sweden
	Nils, Marketing, 33, 18, 2022, Sweden
	Patrick, Marketing, 44, 43, 2022, Canada
	Anna, Sales, 55, 33, 2023, Canada
	Johan, Sales, 66, 26, 2025, Sweden
	Olle, Marketing, 77, 19, 2023, Sweden
	Bonnie, Marketing, 88, 44, 2023, US
];
```

Results

Results for adding a field containing an aggregation filtered for specific values

| Name | Department | Salary | Age | Year | Country | SlidingWindow |
| --- | --- | --- | --- | --- | --- | --- |
| David | Sales | 11 | 32 | 2019 | Canada | 11-22 |
| Sara | Sales | 22 | 25 | 2022 | Sweden | 11-22-55 |
| Nils | Marketing | 33 | 18 | 2022 | Sweden | 33-44 |
| Patrick | Marketing | 44 | 43 | 2022 | Canada | 33-44-77 |
| Anna | Sales | 55 | 33 | 2023 | Canada | 22-55-66 |
| Johan | Sales | 66 | 26 | 2025 | Sweden | 55-66 |
| Olle | Marketing | 77 | 19 | 2023 | Sweden | 44-77-88 |
| Bonnie | Marketing | 88 | 44 | 2023 | US | 77-88 |

## Example - Adding a field with a sorted sliding window

Example: Adding a field with a sliding window

Load script

Create a new tab in the data load editor, and then load the following data as an inline load. Create the table below in Qlik Sense to see the results.

```
[Employees]:
Load 
	*,
	Window(concat(Text(Salary),'-'), Department, 'ASC', Age, -1, 1) as SortedSlidingWindow
Inline [
	Name, Department, Salary, Age, Year, Country
	David, Sales, 11, 32, 2019, Canada
	Sara, Sales, 22, 25, 2022, Sweden
	Nils, Marketing, 33, 18, 2022, Sweden
	Patrick, Marketing, 44, 43, 2022, Canada
	Anna, Sales, 55, 33, 2023, Canada
	Johan, Sales, 66, 26, 2025, Sweden
	Olle, Marketing, 77, 19, 2023, Sweden
	Bonnie, Marketing, 88, 44, 2023, US
];
```

Results

Results for adding a field containing an aggregation filtered for specific values

| Name | Department | Salary | Age | Year | Country | SortedSlidingWindow |
| --- | --- | --- | --- | --- | --- | --- |
| David | Sales | 11 | 32 | 2019 | Canada | 11-55-66 |
| Sara | Sales | 22 | 25 | 2022 | Sweden | 22-66 |
| Nils | Marketing | 33 | 18 | 2022 | Sweden | 33-77-88 |
| Patrick | Marketing | 44 | 43 | 2022 | Canada | 44-77 |
| Anna | Sales | 55 | 33 | 2023 | Canada | 11-55 |
| Johan | Sales | 66 | 26 | 2025 | Sweden | 11-22-66 |
| Olle | Marketing | 77 | 19 | 2023 | Sweden | 33-44-77 |
| Bonnie | Marketing | 88 | 44 | 2023 | US | 33-88 |

To better understand how the partitions and sort order affect the aggregations in a sliding window, sort the table ascendingly by name.

Results for adding ad field containing an aggregation filtered for specific values

| Name | Department | Salary | Age | Year | Country | SortedSlidingWindow |
| --- | --- | --- | --- | --- | --- | --- |
| Anna | Sales | 55 | 33 | 2023 | Canada | 11-55 |
| Bonnie | Marketing | 88 | 44 | 2023 | US | 33-88 |
| David | Sales | 11 | 32 | 2019 | Canada | 11-55-66 |
| Johan | Sales | 66 | 26 | 2025 | Sweden | 11-22-66 |
| Nils | Marketing | 33 | 18 | 2022 | Sweden | 33-77-88 |
| Olle | Marketing | 77 | 19 | 2023 | Sweden | 33-44-77 |
| Patrick | Marketing | 44 | 43 | 2022 | Canada | 44-77 |
| Sara | Sales | 22 | 25 | 2022 | Sweden | 22-66 |

In the row for Johan, the aggregation has included the salary values for David as well as Sara. These are the preceding and following rows within the Sales department partition when sorted by age.

For another example showing which rows are included, change the **Windows** expression from `Window(concat(Text(Salary),'-'), Department, 'ASC', Age, -1, 1)` to `Window(concat(Text(Name),'-'), Department, 'ASC', Age, -1, 1)` and reload. The values in SortedSlidingWindow in the table below give the name from the preceding and following rows within the partition Sales.

Results for adding a field containing an aggregation filtered for specific values

| Name | Department | Salary | Age | Year | Country | SortedSlidingWindow |
| --- | --- | --- | --- | --- | --- | --- |
| Anna | Sales | 55 | 33 | 2023 | Canada | Anna-David |
| Bonnie | Marketing | 88 | 44 | 2023 | US | Bonnie-Nils |
| David | Sales | 11 | 32 | 2019 | Canada | Anna-David-Johan |
| Johan | Sales | 66 | 26 | 2025 | Sweden | David-Johan-Sara |
| Nils | Marketing | 33 | 18 | 2022 | Sweden | Bonnie-Nils-Olle |
| Olle | Marketing | 77 | 19 | 2023 | Sweden | Nils-Olle-Patrick |
| Patrick | Marketing | 44 | 43 | 2022 | Canada | Olle-Patrick |
| Sara | Sales | 22 | 25 | 2022 | Sweden | Johan-Sara |

## Limitations

**Window** has the following limitations:

- **Window** is a resource intensive function, particularly in terms of memory consumption.
- **Window** is not supported in Qlik Sense Mobile.
- Chart expressions do not support **Window**.
- You cannot nest **Window** functions inside other **Window** functions.
- **Window** cannot be used inside an aggregation function.
- **Window** cannot be used in a load statement with a group by clause.
- **Window** needs to be able to scan the whole table.
- **WRank()**, **RecNo()**, and **RowNo()** cannot be used with **Window** when using the sliding window functionality.
- When the sliding window functionality is used, the calculation time increases with the size of the window. Large tables combined with large window sizes should generally be avoided.
