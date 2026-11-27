---
title: "Which aggregation functions?"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/which-aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Tutorial - Chart expressions"]
---

# Which aggregation functions?

[Aggregation](#glossary-0 "Glossary term") functions are many-to-one functions. They use the values from many records as input and collapse these into one single value that summarizes all records. Sum(), Count(), Avg(), Min(), and Only() are all aggregation functions.

In Qlik Sense, you need exactly one level of aggregation function in most formulas. This includes chart expressions, text boxes, and labels. If you do not include an aggregation function in your expression, Qlik Sense will automatically assign the Only() function.

- An aggregation function is a function that returns a single value describing some property of several records in your data.
- All expressions, except calculated [dimensions](#glossary-1 "Glossary term"), are evaluated as aggregations.
- All [field](#glossary-2 "Glossary term") references in expressions must be wrapped in an aggregation function.

Information noteYou can use the expression editor to create and change expressions in Qlik Sense. To learn more about expression editor features, see: [Expression editor](../Expressions/expression-editor.htm).

## Consolidating amounts using Sum()

Sum()
 calculates the total of the values given by the expression or field across the aggregated data.

Let us calculate the total sales that each manager has made, as well at the total sales of all managers.

Inside the application on the Which Aggregations? [sheet](#glossary-4 "Glossary term") you will find two tables, a table titled Sum(), Max(), Min(), and a table titled Count(). We will use each table to create aggregation functions.

Do the following:

1. Select the available Sum(), Max(), Min() table.
   The properties panel opens.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following: Sum(Sales)
5. Click Apply.

Table showing total sales per Manager

![Table showing total sales per Manager](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-aggregations-table1.png)

You can see the sales that each manager has made, as well as the total sales of all managers.

Information noteAs a best practice, make sure that your data is formatted appropriately. In this case, set the Number formatting to Money, and the Format pattern to $ #,##0;-$ #,##0.

For more information see [Sum](../ChartFunctions/BasicAggregationFunctions/sum.htm).

## Calculating highest sale value using Max()

Max() finds the highest value per row in the aggregated data.

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following : Max (Sales)
4. Click Apply.

Table showing total sales and highest sale per Manager

![Table showing total sales and highest sale per Manager](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-aggregations-table2.png)

You can see that the highest sales earnings for each manager, as well as the highest total number.

For more information, see [Max](../ChartFunctions/BasicAggregationFunctions/max.htm).

## Calculating lowest sale value using Min()

Min()
 finds the lowest value per row, in the aggregated data.

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following : Min (Sales)
4. Click Apply.

Table showing total sales, highest sale, and lowest sale per Manager

![Table showing total sales, highest sale, and lowest sale per Manager](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-aggregations-table3.png)

You can see the lowest sales earnings for each manager, as well as the lowest total number.

For more information see [Min](../ChartFunctions/BasicAggregationFunctions/min.htm).

## Counting the number of entities using Count()

Count()
 is used to count the number of values, text and numeric, in each [chart](#glossary-5 "Glossary term") dimension.

In our data, each manager is responsible for a number of sales representatives (Sales Rep Name). Let us calculate the number of sales representatives.

Do the following:

1. Select the available Count() table.
   The properties panel opens.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following : Count([Sales Rep Name])
5. Click Apply.

Table showing Sale Representatives, and total number of Sales Representatives.

![Table showing Sale Representatives, and total number of Sales Representatives.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-aggregations-table4.png)

You can see that the total number of sales representatives is 64.

### Difference between Count()and Count(distinct )

Let us calculate the number of managers.

Do the following:

1. Add a new dimension to your table: Manager.
   A single manager is handling more than one sales representative, so the same manager name appears more than once in the table.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following: Count(Manager)
5. Add another [measure](#glossary-6 "Glossary term") with the expression: Count(distinct Manager)
6. Click Apply.

Table showing Sales Representatives, total number of Sales Representatives, Manager responsible for each Sales Representative, incorrect total number of Managers, and correct total number of Managers.

![Table showing Sales Representatives, total number of Sales Representatives, Manager responsible for each Sales Representative, incorrect total number of Managers, and correct total number of Managers.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-aggregations-table6.png)

You can see that the total number of managers on the column using Count(Manager) as an expression was calculated as 64. That is not correct. The total number of managers is correctly calculated as 18 using the Count(distinct Manager) expression. Each manager is only counted once, regardless of how many times their name appears on the list.

For more information see [Count](../ChartFunctions/CounterAggregationFunctions/count.htm).
