---
title: "GetObjectMeasure  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/FieldFunctions/getobjectmeasure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Field functions"]
---

# GetObjectMeasure - chart function

GetObjectMeasure() returns the name of the measure. Index is an optional integer denoting the measure that should be returned.

Information note

You cannot use this function in a chart in the following locations: title, subtitle, footer, reference line expression and min/max expression.

Information note

You cannot reference the name of a dimension or measure in another object using the Object ID.

Syntax:

GetObjectMeasure ([index])

Return data type: String

Example: Chart expressions

| Example | Result |
| --- | --- |
| GetObjectMeasure () GetObjectMeasure (0) | Returns the name of the first measure in the chart. |
| GetObjectMeasure (1) | Returns the name of the second measure in the chart. |

## Example - GetObjectMeasure fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - CustomerID
  - TransactionQuantity

Load script

```
Example:
LOAD * INLINE [
CustomerID, TransactionQuantity
049681, 13
203521, 6
203521, 21
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CustomerID

Create the following measures:

- Sum(TransactionQuantity) - first measure.
- Avg(TransactionQuantity) - second measure
- =GetObjectMeasure(), to find the first measure in the table.
- =GetObjectMeasure(0), to find the first measure in the table.
- =GetObjectMeasure(1), to find the second measure in the table.

Results table

| CustomerID | Sum(TransactionQuantity) | Avg(TransactionQuantity) | GetObjectMeasure () | GetObjectMeasure (0) | GetObjectMeasure (1) |
| --- | --- | --- | --- | --- | --- |
| Totals | 40 | 13.333333 | Sum(TransactionQuantity) | Sum(TransactionQuantity) | Avg(TransactionQuantity) |
| 049681 | 13 | 13 | =Sum(TransactionQuantity) | =Sum(TransactionQuantity) | =Avg(TransactionQuantity) |
| 203521 | 27 | 13.5 | =Sum(TransactionQuantity) | =Sum(TransactionQuantity) | =Avg(TransactionQuantity) |

Looking at the results, you can see how the GetObjectMeasure function returns the measure indicated by the function parameters.
