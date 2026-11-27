---
title: "Dollar-sign expansion using an expression"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/dollar-sign-expansion-using-expression.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Dollar-sign expansions"]
---

# Dollar-sign expansion using an expression

Expand/Collapse all

# Dollar-sign expansion using an expression

Expressions
can be used in dollar-sign expansions.

The content between the brackets
must start with an equal sign:

$(=expression)

The
expression will be evaluated and the value will be used in the expansion. For example:

```
// returns a string with the current year
$(=Year(Today()));
```

```
// returns the year before the selected one
$(=Only(Year)-1);
```

## Example: Select a measure by referencing the measure in a chart expression

Example: Load script

Load script

Load the following data as an inline load in the data load editor:

```
// Load string “=MinString(Measure)” into variable VSelectMeasure
Let vSelectMeasure = '=MinString(Measure)';
MyTable1: // Create table and load values for Dim and Sales
Load * inline [
Dim, Sales
A, 150
A, 200
B, 240
B, 230
C, 410
C, 330 ];

MyTable2: // Create table and load aggregations as field values for Measure
Load * Inline [
Measure
avg(Sales)
sum(Sales)
count(distinct Dim)];
```

For more information about using inline loads, see [*Using inline loads to load data*](inline-loads-qs.htm).

Explanation

The script allows you to select a [measure](#glossary-0 "Glossary term") by referencing the measure in a chart expression. The chart expression contains the variable expansion $(=MinString(Measure)). MinString() finds string values in the expression and returns the first text value sorted alphabetically, in this case avg(Sales). This makes it possible to interactively decide (and select) which expression to use in a [visualization](#glossary-1 "Glossary term") without accessing and manipulating the [properties](#glossary-2 "Glossary term") of the object.

Output

Create the following table in Qlik Sense by using:

- Dimension: Dim
- Measures:

  - ='$(vSelectMeasure)'
  - =$(=MinString(Measure))
  - Avg(Sales)

Table - Dollar-sign expansion using an expression

| Dim | ='$(vSelectMeasure)' | =$(=MinString(Measure)) | Avg(Sales) |
| --- | --- | --- | --- |
| Totals | - | 260 | 260 |
| A | avg(Sales) | 175 | 175 |
| B | avg(Sales) | 235 | 235 |
| C | avg(Sales) | 370 | 370 |

## Example: Calculate the quota between two dimensions

Example: Load script

Load script

Load the following data as an inline load in the data load editor:

```
Let vDivision = '=MinString(Numerator) / MinString(Denominator)';
Load recno() as Numerator autogenerate 100;
Load recno() as Denominator autogenerate 100;
```

Explanation

This script generates a pair of fields, containing 100 values each, that function as Numerators and Denominators in a calculation of the quota between the two. The chart measure contains the variable expansion ='$( vDivision )' , making it possible to interactively decide (and select) which quota to be calculated.

Output

Create the following table in Qlik Sense by using:

- Dimensions:

  - Numerator
  - Denominator
- Measure: ='$(vDivision)'

The resultant quota (Totals) is affected by the selected values in the fields. Numerator (=5) and Denominator (=3) and will be recalculated with each new selection in either field.

Table - Dollar-sign expansion as expression

| Numerator | Denominator | ='$(vDivision)' |
| --- | --- | --- |
| Totals | - | 1,6666666666667 |
| --- | --- | --- |
| 5 | 3 | 1,6666666666667 |

## File inclusion

File
inclusions are made using dollar-sign expansions. The syntax is:

$(include=filename)

The above text will be replaced by the content
of the file specified after the equal sign. This feature is useful when storing scripts or parts of scripts in text files.

For more information, see [*Include*](SystemVariables/Include.htm).

## Dollar expansions and alternate states

A dollar expansion is normally not sensitive to alternate states. However, if the dollar expansion has an expression, this is evaluated in the state relevant to the object where the dollar expansion is made.

For example:

```
$(=Sum(Amount))
```

The calculation will return the sum of amount based on the selection in the state of the object.

## Interaction between dollar-sign expansions and outer set expressions

When you combine dollar-sign expansions with outer set expressions, a specific order of evaluation applies. For details, see [*Outer set expressions and dollar-sign expansions*](../ChartFunctions/SetAnalysis/outer-set-expression-dollar-sign-expansion.htm).
