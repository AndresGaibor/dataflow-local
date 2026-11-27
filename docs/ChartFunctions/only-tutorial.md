---
title: "The importance of Only()"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/only-tutorial.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Tutorial - Chart expressions"]
---

# The importance of Only()

Only() returns a value if there is only one possible value in the group. This value will be the result of the [aggregation](#glossary-0 "Glossary term"). Qlik Sense defaults to Only() if no aggregation function is specified.

If there is a one-to-one relationship between the [chart](#glossary-1 "Glossary term") [dimension](#glossary-2 "Glossary term") and the parameter, the Only() function returns the only possible value. If there are several values, it returns NULL. For example, searching for the only product where the unit price =12 will return NULL if more than one product has a unit price of 12.

The following images show the difference between one-to-one and one-to-many relationships:

A table showing one-to-one relationship between Manager Number and Manager.

![Two-column table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-only-table1.png)

A table showing one-to-many relationship of Sales Rep Name and Manager.

![Two-column table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-only-table2_382x482.png)

The Only() function is an aggregation function. It uses many records as input and returns one value only, similarly to Sum() or Count(). Qlik Sense uses aggregations in virtually all its calculations. The expression in a chart, in a sort expression, in a text box, in an advanced search, and in a calculated label are all aggregations and cannot be calculated without involving an aggregation function.

But what if a user enters an expression that lacks an explicit aggregation function? For example, if the sort expression is set to Date? Or if there is an advanced search for customers who have bought beer and wine products using the expression =[Product Type]='Beer and Wine'?

This is where the Only() function affects the calculation. If there is no explicit aggregation function in the expression, Qlik Sense uses the Only() function implicitly. In the above cases, Only(Date) is used as sort expression and Only([Product Type])='Beer and Wine' is used as the search criterion.

Sometimes the new expression returns a result that the user does not expect. Both of the examples above will work when there is only one possible value of Date or Product Type, but neither of them will work for cases when there is more than one value.

## Different expressions using Only()

We will create four KPIs with similar expressions. This way, we can compare how having naked [field](#glossary-3 "Glossary term") references, or having Only() in a different position in our expression can have a big impact on your selection results.

Inside the application on the Importance of Only()[sheet](#glossary-5 "Glossary term") you will find a filter pane with Invoice Date as the dimension.

Do the following:

1. Create a KPI.
2. Click Add measure. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following: Month([Invoice Date])
4. Create three more KPIs with measures: Month(Only([Invoice Date])), Month(Max([Invoice Date])), and Only(Month([Invoice Date])).
5. Click Apply.

Four KPIs and a filter pane showing three different but similar expressions.

![KPI results](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-only-table3.png)

Tip noteIn each KPI the Number formatting has been set to Measure expression.

When you have a naked field reference, the Only() function is inserted at the lowest level. That means that the first two KPIs, Month([Invoice Date]) and Month(Only([Invoice Date])), will be interpreted the same and will always give the same result.

As you can see three of the four KPIs return NULL. The third KPI, Month(Max([Invoice Date])), already returns a value, even though no selection has been made.

When you write expressions you should always ask yourself which aggregation you want to use, or which value you want to use if there are several values. If you want to use NULL to represent several values, you can leave the expression as is. For numbers, you probably want to use Sum(), Avg(), Min(), or Max() instead. For strings you may want to use Only() or MinString().

Do the following:

1. Stop editing the sheet.
2. In the filter pane, select date in the month of January.
3. Confirm the selection by clicking ![Checkmark ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg).

The KPI results change when a single selection is made.

![KPI results](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-only-table4.png)

When a single selection is made, all of the KPIs return the correct answer. Even if the expression contains a naked field reference, such as the expression in Month([Invoice Date]), the fact that we have made a unique selection allows it to return the proper value.

Do the following:

1. In the filter pane, select an additional date in the month of January.
2. Confirm the selection by clicking ![Checkmark ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg).

The KPI results change when two selections are made with both dates in the month of January.

![KPI results](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-only-table5.png)

The first two KPIs return NULL, and the other two KPIs return the proper value of January. Specifically, the fourth KPI returns a correct answer because both the date [selections](#glossary-6 "Glossary term") we made are for dates in January.

Do the following:

1. In the filter pane, select an additional date, in a month other than January.
2. Confirm the selection by clicking ![Checkmark ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg).

The KPI results change when multiple selections are made with dates in different months.

![KPI results](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-only-table6.png)

When multiple selections are made, using dates in different months, only the third KPI returns a value. It returns the value of the largest month from the selection made, according to the expression Month(Max([Invoice Date])). Since Only() is inserted automatically in expressions with naked field references you cannot always assume that the lowest level will be appropriate for your expression. The placement of Only() is important.

For more information, see [Only - chart function](BasicAggregationFunctions/only.htm).
