---
title: "Num# Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/num_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Num# Script and chart function

Expand/Collapse all

# Num# Script and chart function

Num#() interprets a text string as a numerical value, that is it converts the input string to a number using the format specified in the second parameter. If the second parameter is omitted, it uses the decimal and thousand separators set in the data load script. Custom decimal and thousand separator symbols are optional parameters.

Syntax:

Num#(text[, format[, dec\_sep
[, thou\_sep ] ] ])

Return data type:  dual

The Num#() function returns a dual value with both the string and the numeric value. The function takes the textual representation of the input expression and generates a number. It does not change the format of the number; the output is formatted in the same way as the input.

Arguments

| Argument | Description |
| --- | --- |
| text | The text string to be evaluated. |
| format | String specifying the number format used in the first parameter. If omitted, the decimal and thousand separators that are set in the data load script are used. The Num# function supports many format options for different numeric structures, for example:  #,##0: ​Displays a number without decimal places.  #,##0.00: ​Displays a number with two decimal places.  ##0.00%: Displays a number as a percentage with two decimal places.  ​#,##0;(#,##0): Formats negative numbers to appear in parentheses.  $#,##0.00: Formats numbers as currency with a $ symbol.  ​0.00E+0: Displays numbers in scientific notation. |
| dec\_sep | String specifying the decimal number separator. If omitted, the value of the variable DecimalSep that is set in the data load script is used. The Num# function supports many decimal number separator formats, for example:  Comma ​' , ': For example, $1,000,00 for one thousand dollars.  Period ' . ':​ For example, € 1,000.00.  Hyphen ' - ': When used instead of the traditional period or comma for the decimal separator, it shows values like ¥1,000-00.  ​For more information, see [*DecimalSep*](../NumberInterpretationVariables/DecimalSep.htm). |
| thou\_sep | String specifying the thousands number separator. If omitted, the value of the variable ThousandSep that is set in the data load script is used. The Num# function supports many options for the thousands number separator:  Period ​' . ': Uses a period for the thousands separator (common in some European formats), displaying as $1.000,00 if combined with a comma decimal separator.  Space ​' ': Uses a space for the thousands separator, which is common in some European countries. Displays as € 1 000.00.  Underscore ​'\_':​ Uses an underscore for the thousands separator, which is sometimes used in technical or specific regional formats. Displays values like $1\_000.00.  ​For more information, see [*ThousandSep*](../NumberInterpretationVariables/ThousandSep.htm). |

Example: Chart expressions

| Example | Results (String value returned) |
| --- | --- |
| Num#( '35,648.31', '#', '.' , ',' ) | Returns string of 35,648.31 and numeric value of 35648.31. |
| Num#( ‘35 648.312’, '#', '.' , ',' ) | Returns string of35 648.312 and numeric value of 35648.312. |
| Num#( '35.648,3123', '#', '.' , ',' ) | Returns string of 35.648,3123 and numeric value of NULL (-). |
| Num#( '35 648,31234', '#', '.' , ',' ) | Returns string of 35 648,31234 and numeric value of NULL (-). |
| Num#('1,234.56', '#,##0.00') | Returns string of 1,234.56 and numeric value of 1230.45. |
| Num#('$1,230.45', '$#,##0.00') | Returns string of $1,230.45 and numeric value of 1234.56. |
| Num#('20220315', 'YYYYMMDD') | Returns string of 20220315 and numeric value of 20220315. |

## Example - Num# fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - ProductID
  - ProductName
  - SalesAmount
- The standard settings for ThousandSep and DecimalSep to illustrate this example.
- A preceding load that uses the Num# function. When executed, it creates an additional field called FormattedSalesAmount.

Load script

```
SET ThousandSep=',';
SET DecimalSep='.';
Example:
LOAD
ProductID,
ProductName,
SalesAmount,
Num#(SalesAmount, '#.##0,00',',','.') AS FormattedSalesAmount
INLINE [
ProductID, ProductName, SalesAmount
1, Product A, '1.234,56'
2, Product B, '2.456,78'
3, Product C, '345,67'
4, Product D, '987,12'
5, Product E, '1.200,45'
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ProductID
- ProductName
- SalesAmount
- FormattedSalesAmount

Create the following measure:

- =Num(FormattedSalesAmount), to view the numeric value of the field according to the system settings for the number format.

Results table

| ProductID | ProductName | SalesAmount | FormattedSalesAmount | Num(FormattedSalesAmount) |
| --- | --- | --- | --- | --- |
| 1 | Product A | 1.234,56 | 1.234,56 | 1234.56 |
| 2 | Product B | 2.456,78 | 2.456,78 | 2456.78 |
| 3 | Product C | 345,67 | 345,67 | 345.67 |
| 4 | Product D | 987,12 | 987,12 | 987.12 |
| 5 | Product E | 1.200,45 | 1.200,45 | 1200.45 |

In this example you can observe how the Num# function converts SalesAmount data from its original format of text into a numeric value.

## Example - Num# scenario

Load script

Overview

A dataset contains sales data from several countries in different text formats. We want to standardize the data and display it in a table.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Country
  - Product
  - Amount
- A preceding load that uses the Num# function to convert the values in the Amount field.

Load script

```
Example:
LOAD
Country,
Product,
IF(Country = 'Germany', Num#(Amount, '#.##0,00', ',', '.'), Num#(Amount, '#,##0.00')) AS Amount
INLINE [
Country, Product, Amount
Germany, Product A, '1.234,56'
USA, Product B, '2,345.78'
Germany, Product C, '987,12'
USA, Product D, '1,200.45'
Germany, Product E, '345,67'
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Product
- Country
- Amount

Create the following measure:

- Num(Amount), to view the numeric value of the Amount field as set in the system settings for the number format.

Results table

| Product | Country | Amount | Num(Amount) |
| --- | --- | --- | --- |
| Customer A | Germany | 1.234,56 | 1234.56 |
| Customer B | USA | 2,345.78 | 2345.78 |
| Customer C | Germany | 987,12 | 987.12 |
| Customer D | USA | 1,200.45 | 1200.45 |
| Customer E | Germany | 345,67 | 345.67 |

When comparing the Amount column with the Num(Amount) column, you see that the data presented using the Num# function changes the underlying numeric values but keeps the string format as-is. For example, all values for Germany in the Amount column use a comma for the decimal separator, but the underlying format in Num(Amount) uses a period for all values.
