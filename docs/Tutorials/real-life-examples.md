---
title: "Examples from real life"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/real-life-examples.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Tutorial - Chart expressions"]
---

# Examples from real life

Visualizations in Qlik Sense can give you insight in your data. Using expressions in your [charts](#glossary-0 "Glossary term") can bring results that specifically apply to your work. The range of functions in Qlik Sense allow you to customize your expressions to fit your needs, even if the option is not readily available.

## Calculating the gross margin percentage

We define the margin as the difference between our sales and the cost of making these sales. We will calculate the margin for each month, as well as what percentage of the monthly sales is our margin.

To calculate the margin percentage we can use the following expression:

(Sum(Sales)-Sum(Cost))/Sum(Sales)

The expression can be simplified further

1-Sum(Cost)/Sum(Sales)

Inside the application, on the Examples from real life [sheet](#glossary-2 "Glossary term"), you will find a table titled Margin.

Do the following:

1. Select the available table titled Margin.
   The properties panel opens.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following: Sum(Sales)
5. Add three more [measures](#glossary-3 "Glossary term") with the expressions: Sum(Cost), Sum(Sales) - Sum(Cost), and 1 - Sum(Cost)/Sum(Sales).
6. Click Apply.

Table showing sum of sales, and sum of cost per month, as well as calculated margin per month in both amount and percentage forms

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table1.png)

Information noteAs a best practice, make sure that your data is formatted appropriately. In this case, in each column we will change the Label to represent the calculation. In columns with monetary values we will change the Number formatting to Money, and the Format pattern to $ #,##0;-$ #,##0. Set the Number formatting of the margin percentage to Number, and the Formatting to Simple and 12%.

You can see the calculated margin for each month based on the sales and the cost. You can also see what percentage of the sales makes up our margin.

In the application data, we already have data for the monthly margin. This is a good opportunity to make a comparison between our original data and our calculation.

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following : Sum(Margin)
4. Add another measure with the expression: (Sum(Sales) - Sum(Cost)) - Sum(Margin)
5. Click Apply.

The margin table with additional columns for monthly margin coming from the data set, and its difference to the calculated margin.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table2.png)

Some values in the calculated margin column differ from the values from the margin column coming directly from our data. The margin discrepancy column clearly shows that this takes place in a months during 2014. The difference between the calculated margin and the margin coming from the data set is small, but the fact that it takes place in a specific year creates some questions. What changed during that year? Looking into the data and asking the right questions might prove to be important for your business.

## Invoicing delays

For this example we will be using data based on a company that collects dates both for the creation of invoices and the promised delivery of the goods they produce. The two dates are not always the same. Additionally some invoices might have two promised delivery dates. The shortest date is always the same as the invoice date, as it is automatically created by the invoicing system used by the company. The largest promised delivery date is the date when a delivery was agreed to be made between the company and the client.

Let us start by adding these dates on a table.

On the Examples from real life sheet you will find a table titled Invoicing delays.

Do the following:

1. Select the available table titled Invoicing delays.
   The properties panel opens.
2. Click Add column and select Measure.
3. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
4. Enter the following : Only([Invoice Date])
5. Add another measure with the expression: Max([Promised Delivery Date])
6. Click Apply.

Table showing promised delivery date and invoice date for each invoice

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table3.png)

Information noteAs a best practice, make sure that your data is formatted appropriately. In columns that show dates, set the Number formatting to Date, and set the Formatting to Simple and 17 Feb 2014.

You can see that the invoice date and the promised delivery date are not always the same. When there are two promised delivery dates we need to use the largest one for our calculation.

Let us calculate the difference between the invoice date and the promised delivery date. We will use the following expression:

Max([Promised Delivery Date])-[Invoice Date]

There are three scenarios:

- The two dates are the same, and the result of the expression is 0.
- The products were promised after the invoice was created, and the result is a positive integer.
- The invoice was created after the products were promised to be delivered, and the result is a negative integer.

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following : Max([Promised Delivery Date])-[Invoice Date]
4. Click Apply.

Table showing promised delivery date and invoice date for each invoice, as well as the number of days from invoicing to promised delivery

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table4.png)

Information noteSort the table based on the last column, named Days from invoicing to delivery.

There is a range of differences between the dates. Negative values indicate that the invoice was delayed. Positive numbers indicate that the promised delivery was done after the invoice was created.

Let us calculate the number of invoices that were made after the promised delivery date.

Do the following:

1. Click Add column and select Measure.
2. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following: Count(Distinct If(Aggr(Max([Promised Delivery Date])<[Invoice Date],[Invoice Number]),[Invoice Number]))
4. Click Apply.

Information noteAlternatively we could use Sum(Aggr(If(Max([Promised Delivery Date])-[Invoice Date]< 0, 1, 0), [Invoice Number])).

The invoicing delays table with additional column showing the number of delayed invoices.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table5.png)

The last column makes more sense as a KPI as a percentage of the total number of invoices.

Do the following:

1. Create a KPI.
2. Click Add measure. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following: Count(Distinct If(Aggr(Max([Promised Delivery Date])<[Invoice Date],[Invoice Number]),[Invoice Number]))/Count([Invoice Number])
4. Click Apply.

A KPI showing the percentage of delayed invoices.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table6.png)

Let us calculate the average delay in invoicing.

Do the following:

1. Create a new KPI.
2. Click Add measure. Click on the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) symbol.
   The expression editor opens.
3. Enter the following: Avg(Aggr(If(Max([Promised Delivery Date])<[Invoice Date],(Max([Promised Delivery Date])-[Invoice Date])), [Invoice Number]))
4. Click Apply.

A KPI showing the average delay in invoicing

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_examples_table7.png)

## Thank you!

Now you have finished this tutorial, and hopefully you have gained some basic knowledge about chart expressions in Qlik Sense. Please visit our website for more inspiration for your applications.
