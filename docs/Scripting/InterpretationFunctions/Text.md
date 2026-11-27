---
title: "Text Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/Text.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Text Script and chart function

Expand/Collapse all

# Text Script and chart function

Text() forces the
expression to be treated as text, even if a numeric interpretation is possible.

Syntax:

Text (expr)

Return data type: string

Arguments

| Argument | Description |
| --- | --- |
| expr | An expression to be treated as text. |

Example: Chart expressions

| Example | Results |
| --- | --- |
| Text( 1234 ) | Returns 1234 as a string. There is no numeric value. |
| Text( pi( ) ) | Returns 3.1415926535898 as a string. There is no numeric value. |

## Example - Text fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ID
  - PostalCode
- A preceding load that uses the Text function to create a new field named PostalCode\_Text to ensure that the postal codes remain as text and do not get converted to numbers.

Load script

```
Example:
LOAD
ID,
PostalCode,
Text(PostalCode) AS PostalCode_Text;
LOAD * INLINE [
ID, PostalCode
1, 12345
2, 54321
3, 67890
4, 11223
5, 33445
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ID
- PostalCode
- PostalCode\_Text

Results table

| ID | PostalCode | PostalCode\_Text |
| --- | --- | --- |
| 1 | 12345 | 12345 |
| 2 | 54321 | 54321 |
| 3 | 67890 | 67890 |
| 4 | 11223 | 11223 |
| 5 | 33445 | 33445 |

The output of the preceding load uses the Text function to ensure that any numeric values are treated as text. You can see that the values in the PostalCode\_Text column are processed as text and appear left-aligned by default, whereas the values in the PostalCode column are numbers and appear right-aligned by default.

## Example - Text scenario

Load script

Overview

A dataset contains customer invoice data that are entered as numeric values, but you want to retain these values as text.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - InvoiceNumber
  - CustomerName
- A preceding load that uses the Text function to create a new field named InvoiceNumber\_Text to ensure that the invoice numbers are treated as text.

Load script

```
Example:
LOAD
InvoiceNumber,
CustomerName,
Text(InvoiceNumber) AS InvoiceNumber_Text;
LOAD * INLINE [
InvoiceNumber, CustomerName
10001, John Doe
10002, Jane Smith
10003, Bob Johnson
10004, Alice Brown
10005, Michael Green
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InvoiceNumber
- CustomerName
- InvoiceNumber\_Text

Results table

| InvoiceNumber | CustomerName | InvoiceNumber\_Text |
| --- | --- | --- |
| 10001 | John Doe | 10001 |
| 10002 | Jane Smith | 10002 |
| 10003 | Bob Johnson | 10003 |
| 10004 | Alice Brown | 10004 |
| 10005 | Michael Green | 10005 |

The results show that the numeric values in the InvoiceNumber column have now been converted to text values in the InvoiceNumber\_Text column and appear left-aligned.
