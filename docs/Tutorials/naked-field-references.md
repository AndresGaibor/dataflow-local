---
title: "Naked field references"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/naked-field-references.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Tutorial - Chart expressions"]
---

# Naked field references

A [field](#glossary-0 "Glossary term") is considered naked when it is not enclosed in an [aggregation](#glossary-1 "Glossary term") function.

A naked field reference is an array, possibly containing several values. If so Qlik Sense will evaluate it as NULL, not knowing which of these values you want.

## Always use an aggregation function in your expression

If you find that your expression does not evaluate correctly, there is a high chance that it does not have an aggregation function.

A field reference in an expression is an array of values. For example:

Two tables, one showing that Max(Invoice Date) is a single value, and one showing that Invoice Date is an array of values.

![ Two tables, one showing that Max(Invoice Date) is a single value, and one showing that Invoice Date is an array of values.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-nakedfield-table1.png)

You must enclose the field Invoice Date in an aggregation function to make it collapse into a single value.

If you do not use an aggregation function on your expression, Qlik Sense will use the Only() function by default. If the field reference returns several values, Qlik Sense will interpret it as NULL.

### Splitting invoice dates using the If() function

The If() function is often used for conditional aggregations. It returns a value depending on whether the condition provided within the function evaluates as True or False.

Inside the application on the Naked field references[sheet](#glossary-3 "Glossary term") you will find a table titled Using If() on Invoice dates.

Do the following:

1. Select the available table titled Using If() on Invoice dates.
   The properties panel opens.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following: If( [Invoice Date]>= Date(41323), 'After', 'Before' )
5. Click Apply.

Table showing invoice dates being split by a reference date.

![ Table showing invoice dates being split by a reference date.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-nakedfield-table2.png)

This expression tests if the Invoice Date is before the reference date 2/18/2013 and returns 'Before' if it is. If the date is after or equal to the reference date 2/18/2013, 'After' is returned. The reference date is expressed as the integer number 41323.

For more information, see [if - script and chart function](../Scripting/ConditionalFunctions/if.htm)

## Avoiding naked field references

At first glance, this expression looks correct:

If([Invoice Date]>= Date(41323) 'After', 'Before')

It should evaluate invoice dates after the reference date, return 'After' or else return 'Before'. However, Invoice Date is a naked field reference, it does not have an aggregation function, and as such is an array with several values and will evaluate to NULL. In the previous example, there was only one Invoice Date per Date value in our table, so the expression calculated correctly.

Let's see how a similar expression calculates under a different dimensional value, and how to solve the naked field reference issue:

### Avoiding naked field references in an If() function

We will be using a similar expression as before:

If([Invoice Date]>= Date(41323), Sum(Sales))

This time the function sums the sales after the reference date.

Inside the application, on the Naked field references sheet you will find a table titled Sum(Amount).

Do the following:

1. Select the available Sum(Amount) table.
   The properties panel opens.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following: If( [Invoice Date]>= 41323, Sum(Sales) )
5. Click Apply.

Table showing year, sum of sales for each year, and the results of the expression using the If() function.

![ Table showing year, sum of sales for each year, and the results of the expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-nakedfield-table3.png)

Tip noteKeep the Label intact on the [measures](#glossary-4 "Glossary term") to show the differences between each expression. In columns with monetary values, change the Number formatting to Money, and the Format pattern to $ #,##0;-$ #,##0.

For each year there is an array of invoice dates that come after the reference date. Since our expression lacks an aggregation function it evaluates to NULL. A correct expression should use an aggregation function such as Min() or Max() in the first parameter of the If() function:

If(Max([Invoice Date])>= Date(41323), Sum(Sales))

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following: If( [Invoice Date]>= Date(41323), Sum(Sales) )
4. Click Apply.

Table showing year, sum of sales for each year, and the results of the different expressions using the If() function.

![Table showing year, sum of sales for each year, and the results of the different expressions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-nakedfield-table4.png)

Alternatively, the If() function can be put inside the Sum() function:

Sum(If([Invoice Date]>= Date(41323), Sales) )

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following: Sum( If([Invoice Date]>= Date(41323), Sales ) )
4. Click Apply.

Table showing year, sum of sales for each year, and the results of the different expressions using the If() function.

![Table showing year, sum of sales for each year, and the results of the different expressions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-nakedfield-table5.png)

In the second to last expression, the If() function was evaluated once per dimensional value. In the last expression, it is evaluated once per row in the raw data. The difference in how the function is evaluated causes the results to be different, but both return an answer. The first expression simply evaluates to NULL. The picture above shows the difference between the expressions, using 2/18/2013 as the reference date.
