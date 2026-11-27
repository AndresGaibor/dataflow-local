---
title: "CalcDim - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/calcdim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "System functions"]
---

# CalcDim - chart function

Expand/Collapse all

# CalcDim - chart function

When used in a [dimension](#glossary-0 "Glossary term") expression, CalcDim() overrides the engine's automatic interpretation of how to internally handle the expression. Specifically, the function prevents a new internal field from being created in the data model. Instead, [selections](#glossary-1 "Glossary term") made in the application are treated as selections in applicable fields from the original data model.

This function cannot be used in the [load script](#glossary-3 "Glossary term"). Additionally, a best practice for system performance is to load the fields that are used in the calculated dimension as logical fields via the load script when possible. CalcDim() offers a way to control engine behavior in scenarios where loading the calculated field from the script is not possible.

In Qlik Sense, the dimension expression is by default realized as a field-on-the-fly—that is, as an actual field, apparent in the current selection bar, built on demand. Selections are applied and inferred to this field, similar to any logical field from the script.

An expression wrapped in CalcDim() will behave the same way as all calculated dimension expressions work in QlikView, which is an ad-hoc mapping of the calculated values to the underlying source field values.
All field-on-the-fly calculations can be transferred into calculated dimensions using the CalcDim() function since the calculated dimension has to meet fewer requirements based on the data model than the corresponding field-on-the-fly calculation. This transformation may be desirable in order to guarantee a similar behavior for all calculated dimensions where the data model may prevent the use of a field-on-the-fly calculation in some cases, but not in others.

[Calculated Fields](https://community.qlik.com/t5/Design/Calculated-Fields/ba-p/1694383)

Syntax:

CalcDim(expr)

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| expr | An expression being used as a dimension, or as a segment within a dimension expression. |

## When to use CalcDim

CalcDim() is useful when you need more control over how the Qlik engine handles the fields you invoke in a dimension expression.

By default, Qlik Sense automatically decides whether to create and reference internal fields in the data model when you use a custom dimension expression. Qlik Sense creates and uses these internal fields whenever it is possible. When not possible, the expression is handled with reference to the existing data model fields on which it relies.

Depending on your use case, this automatic processing might not always be desirable. For example, if you are using a variable in a dimension expression, the automatic creation of new fields can become problematic. In this case, use CalcDim() to force the expression to be handled without this method.

Here are some common use cases:

- You have migrated QlikView content into Qlik Sense and you want to preserve the QlikView processing method for calculated dimensions.
- You want to simplify the selection behavior in your application. For example, you prefer to show field selections as selections in fields from the original data model, rather than selections in new fields.
- Your use case requires an ad-hoc expression for consistency and performance. For example, if your dimension expression contains user-controllable dynamic visualization parameters, such as controllable formatting, cut-off values, or periods.

Function examples

| Example | Result |
| --- | --- |
| =CalcDim(if(Year < 2023, 'Older', Year)) | Making a selection in a [visualization](#glossary-4 "Glossary term") that uses this dimension will be processed and displayed as a selection in the associated Year field value from the data model.  Conversely, let's say you do not wrap the expression in CalcDim(). In this case, it would look like this:  =if(Year < 2023, 'Older', Year)  Making a selection in the above expression would be processed and displayed as a selection in the internal field =if(Year < 2023, 'Older', Year), which is not in the data model. |

## Example 1 – Simple comparison

Chart expressions and results

Overview

In this example, you will:

- Add an inline table and load data into an application.
- Create a table to visualize the data and perform calculations.
- Make selections in the table to observe the difference in behavior.

Open the Data load editor and add the following load script to a new section.

The load script loads an inline table. This table includes two fields: a field for the individual's first name, and a field for the individual's last name.

Load script

```
Names:

Load * inline [
FirstName,LastName
John,Doe
Amanda,Honda
Amalia,Craig
Cart,Lynch
];
```

Table creation

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- FirstName
- LastName

Next, add each of the following expressions as dimensions in the table:

- =FirstName & ' ' & LastName
- =CalcDim(FirstName & ' ' & LastName)

The table should look like the following.

Qlik Sense table with example results

| FirstName | LastName | =FirstName & ' ' & LastName | =CalcDim(FirstName & ' ' & LastName) |
| --- | --- | --- | --- |
| John | Doe | John Doe | John Doe |
| Amanda | Honda | Amanda Honda | Amanda Honda |
| Amalia | Craig | Amalia Craig | Amalia Craig |
| Cart | Lynch | Cart Lynch | Cart Lynch |

Comparison: Making selections

In the =FirstName & ' ' & LastName column of the table, select the value John Doe. Notice that in the selection toolbar, the value is selected as a value from a field named =FirstName&' '&LastName.

Clear the selection.

In the =CalcDim(FirstName & ' ' & LastName) column of the table, select the value John Doe. In the selection toolbar, the value is selected as values from two different fields: FirstName and LastName.

These two expressions present the same information: a concatenation of the FirstName and LastName fields. The difference is that without CalcDim(), a synthetic field is created to store the calculation. With CalcDim(), the original fields from the data model are used as the basis for the calculated dimension.

## Example 2 – Practical use case to modify the default behavior

Chart expressions and results

Overview

In this example, we create dynamic dimension expressions referencing a variable, rather than references to static values.

In this example, you will:

- Add an inline table and load data into application.
- Create a variable to dynamically store a value.
- Create a table to visualize the data and perform calculations.
- Make selections in the table to observe the difference in behavior.

Open the Data load editor and add the following load script to a new section.

The load script loads an inline table. This table includes a date field and a calculated field, Year, which is derived from the raw dates.

Load script

```
SET DateFormat='MM/DD/YYYY';

Transactions:

Load *,

RowNo() as ID,
Year(date) as Year
;

Load * Inline
[
date,amount
'1/19/2022',37.23
'2/28/2022',88.27
'3/16/2022',53.80
'4/1/2022',82.06
'5/16/2022',87.21
'6/26/2022',45.89
'7/9/2022',36.23
'8/2/2022',76.11
'9/26/2022',84.21
'10/29/2022',67.67
'1/1/2023',100.49
'2/24/2023',99.47
'3/6/2023',50.02
'4/10/2023',2.05
'5/20/2023',75.64
'6/25/2023',98.11
'7/19/2023',30.00
'9/27/2023',76.11
'10/26/2023',43.21
'11/12/2023',135.41
'1/15/2024',67.24
];
```

Variable creation

Load the data and open a sheet. Create a variable named vCutoffYear, and give it the following Definition: 2023

Table creation

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- Year
- amount

Next, add each of the following expressions as dimensions in the table:

- =if(Year < $(vCutoffYear), 'Older', Year)
- =CalcDim(if(Year < $(vCutoffYear), 'Older', Year))

The table should look like the following.

Qlik Sense table with example results

| date | Year | amount | if(Year < $(vCutoffYear), 'Older', Year) | =CalcDim(if(Year < $(vCutoffYear), 'Older', Year)) |
| --- | --- | --- | --- | --- |
| 1/19/2022 | 2022 | 37.23 | Older | Older |
| 2/28/2022 | 2022 | 88.27 | Older | Older |
| 3/16/2022 | 2022 | 53.80 | Older | Older |
| 4/1/2022 | 2022 | 82.06 | Older | Older |
| 5/16/2022 | 2022 | 87.21 | Older | Older |
| 6/26/2022 | 2022 | 45.89 | Older | Older |
| 7/9/2022 | 2022 | 36.23 | Older | Older |
| 8/2/2022 | 2022 | 76.11 | Older | Older |
| 9/26/2022 | 2022 | 84.21 | Older | Older |
| 10/29/2022 | 2022 | 67.67 | Older | Older |
| 1/1/2023 | 2023 | 100.49 | 2023 | 2023 |
| 2/24/2023 | 2023 | 99.47 | 2023 | 2023 |
| 3/6/2023 | 2023 | 50.02 | 2023 | 2023 |
| 4/10/2023 | 2023 | 2.05 | 2023 | 2023 |
| 5/20/2023 | 2023 | 75.64 | 2023 | 2023 |
| 6/25/2023 | 2023 | 98.11 | 2023 | 2023 |
| 7/19/2023 | 2023 | 30.00 | 2023 | 2023 |
| 9/27/2023 | 2023 | 76.11 | 2023 | 2023 |
| 10/26/2023 | 2023 | 43.21 | 2023 | 2023 |
| 11/12/2023 | 2023 | 135.41 | 2023 | 2023 |
| 1/15/2024 | 2024 | 67.24 | 2024 | 2024 |

Comparisons, part 1: Behavior without CalcDim()

In the above table, there is no difference between the two calculated dimension columns.

In the  if(Year < $(vCutoffYear), 'Older', Year) column of the table, select the value 2023. Notice that in the selection toolbar, the value is selected as a value from a field named =if(Year<2023,'Older',Year).

Next, change the Definition of the vCutoffYear variable to 2024. Notice that while the selection field =if(Year<2023,'Older',Year) is the same and retains the selected value 2023, the data in the table has changed. The value 2023 has changed to the value Older. If you select Older in the  if(Year < $(vCutoffYear), 'Older', Year) column, the selection Older is made in a new field: =if(Year<2024,'Older',Year).

In essence, a new field is internally created for each value of the vCutoffYear variable. When working with concurrent and changing selections, this behavior might not be desirable and can add complexity to data interpretation.

Comparisons, part 2: Behavior with CalcDim()

Now that you have seen the behavior of the expression when not wrapped in CalcDim(), clear all selections in the application. Reset the vCutoffYear variable to the value 2023.

In the =CalcDim(if(Year < $(vCutoffYear), 'Older', Year)) column of the table, select the value 2023. Notice that in the selection toolbar, the value is selected as a value from the underlying field, Year.

Next, change the Definition of the vCutoffYear variable to 2024. The selection field Year is the same, it retains the selected value 2023, and the data in the table has changed, as seen without CalcDim(). However, if you now select Older in the =CalcDim(if(Year < $(vCutoffYear), 'Older', Year)) column, the value 2024 is selected in Year.

All selections you make in a calculated dimension wrapped with CalcDim() will be reflected as selections in the underlying fields referenced from the original data model. This can simplify data interpretation and prevents cluttered, complex expressions from appearing in the selection toolbar when users consume the analytics content.

## Learn more

- [Calculated Fields](https://community.qlik.com/t5/Design/Calculated-Fields/ba-p/1694383)
- [*Calculated dimensions*](../../Dimensions/calculated-dimensions.htm)
