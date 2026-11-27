---
title: "Examples of using a variable in an expression"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/use-variables-expression.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations", "Using variables in expressions"]
---

# Examples of using a variable in an expression

A [variable](#glossary-0 "Glossary term") in Qlik Sense is a named entity, containing a data value. When a variable is used in an expression, it is substituted by its value or the variable's definition.

## Ways to use variables in an expression

A variable can be used in two different ways: in a direct reference or in a dollar-sign expansion. If you use a direct reference, the variable value will be used in the calculation. If you use a dollar-sign expansion, the entire dollar-sign expansion will be replaced by the variable value before the expression is parsed. Therefore, the two different methods may return different results.

### Example: Using a variable with dollar-sign expansion

The variable x contains the text string Sum(Sales).

In a chart, you define the expression $(x)/12. The effect is exactly the same as having the chart expression Sum(Sales)/12.

However, if you change the value of the variable x to for example Sum(Budget), the data in the chart are immediately recalculated with the expression interpreted as Sum(Budget)/12.

Tip noteWhen using variables in expressions, you can change the expression used in a range of charts simultaneously simply by editing the variable.

### Example: Variable with dollar-sign expansion in pivot table

Suppose you have a Pivot table or Pivot object that contains the following:

- Dimensions are Product Type and Product Name.
- Measures are Sum(Sales) and Count (distinct InvoiceNumber).
- The items under Columns are Values (default) and the field Quarter.

You can use variables to encourage interactive analysis. Suppose you also create a variable vUserInteraction with a blank definition. Then, you create two Button charts on your sheet, configured with the Set variable value action:

- Show more detail: Clicking this button sets vUserInteraction to a value of ='Yes'.
- Show less detail: Clicking this button sets vUserInteraction to a value of ='No'.

In your pivot table, you could add a number of additional measures to the chart, such as Count(Quantity) and Sum(Cost). Then, configure each measure column to have the following value for Show column if:

```
'$(Reference)'='Yes'
```

This allows the chart to adapt to whether or not the user wants additional information. If the user clicks the Show more detail button, additional measures are added to the table. If not, or if they click Show less detail, the additional measures are removed.

### More examples: Using variables in dollar-sign expansions

Dollar-sign expansions are a versatile and powerful tool in Qlik Sense, with many possible uses. For more examples, see [*Dollar-sign expansions*](../Scripting/dollar-sign-expansions.htm).

### Example: Directly referencing a variable in an expression

Using a variable as a direct reference is less common, but still useful. For example:

Suppose you have a field TransactionSummary in your data model that contains free text summaries of transactions. This field could contain supplemental information about transactions. For example, a transaction could have a summary to document that the customer purchased an item with a store credit, or to document any issues that came up during the sale.

In your application, you might want to use TransactionSummary but you want to put the data into context without affecting the data model or load script, and without storing it elsewhere in the chart.

You could do the following:

1. Create a variable named vIntroStatement in the variables dialog with the following definition:

   ```
   ='The following summary was provided by the vendor: '
   ```
2. Add the following measure to a Text & image chart:

   ```
   vIntroStatement & TransactionSummary
   ```

Storing the introductory statement as a variable allows you to centrally control the use of a value. For example, the variable vIntroStatement could be used in multiple charts, and within a number of different measures (for example, there could be a separate chart that sometimes contains text describing how many units were sold during the transaction). By using a variable, you can simplify the process of updating expressions in the application. To make a change to the wording, simply update the variable and the changes are reflected across the application.

## How names are interpreted

It is not recommended to name a variable identically to a field or a function in Qlik Sense. But if you do, you must know how to use them in an expression.

Example:

The string XXX represents a field, a variable, a function, or a measure. XXX will be interpreted as one of these depending on how you create the expression.

Examples of how names are interpreted

| Expression | XXX interpreted as |
| --- | --- |
| XXX | measure, variable, or field |
| $(XXX) | variable |
| Count(XXX) | field or variable |
| XXX() | function |

When naming an entity, avoid assigning the same name to more than one field, variable, or measure. There is a strict order of precedence for resolving conflicts between entities with identical names. This order is reflected in any objects or contexts in which these entities are used. This order of precedence is as follows:

- Inside an aggregation, a field has precedence over a variable. Measure labels are not relevant in aggregations and are not prioritized.
- Outside an aggregation, a measure label has precedence over a variable, which in turn has precedence over a field name.
- Additionally, outside an aggregation, a measure can be re-used by referencing its label, unless the label is in fact a calculated one. In that situation, the measure drops in significance in order to reduce risk of self-reference, and in this case the name will always be interpreted first as a measure label, second as a field name, and third as a variable name.

As a best practice, consider using a standardized naming convention for the variables you create in an application. For example, you could make sure all of your variable names start with v. For example: vUserText. This helps to ensure variables are recognized quickly as variables and differentiated from measures, fields, and functions.

## Variable calculation

There are several ways to use variables with calculated values in Qlik Sense, and the result depends on how you define it and how you call it in an expression.

This example requires the following data is loaded in the data load editor:

LOAD \* INLINE [
Dim, Sales
A, 150
A, 200
B, 240
B, 230
C, 410
C, 330
];

Let's define two variables, from the variables dialog:

- Name vSales Definition'Sum(Sales)'
- Name vSales2 Definition'=Sum(Sales)'

In the second variable, we add an equal sign before the expression. This will cause the variable to be calculated before it is expanded and the expression is evaluated.

If you use the vSales variable as it is, for example in a measure, the result will be the string Sum(Sales), that is, no calculation is performed.

If you add a dollar-sign expansion and call $(vSales) in the expression, the variable is expanded, and the sum of Sales is displayed.

Finally, if you call $(vSales2), the variable will be calculated before it is expanded. This means that the result displayed is the total sum of Sales. The difference between using =$(vSales) and =$(vSales2) as measure expressions is seen in this chart showing the results:

Results

| Dim | $(vSales) | $(vSales2) |
| --- | --- | --- |
| A | 350 | 1560 |
| B | 470 | 1560 |
| C | 740 | 1560 |

As you can see, $(vSales) results in the partial sum for a dimension value, while $(vSales2) results in the total sum.

## Learn more

- [*Variables dialog*](../Sheets/variables-dialog.htm)
- [*Using variables in expressions*](work-with-variables.htm)
- [*Working with variables in the data load editor*](../Scripting/work-with-variables-in-data-load-editor.htm)
- [*Working with the expression editor*](../Expressions/work-with-expression-editor.htm)
- [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm)
