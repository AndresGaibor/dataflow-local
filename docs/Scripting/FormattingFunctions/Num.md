---
title: "Num Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Num.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---

# Num Script and chart function

Expand/Collapse all

# Num Script and chart function

Num() formats a number, that is it converts the numeric value of the input to display text using the format specified in the second parameter. If the second parameter is omitted, it uses the decimal and thousand separators set in the data load script. Custom decimal and thousand separator symbols are optional parameters.

Syntax:

Num(number[, format[, dec\_sep [, thou\_sep]]])

Return data type:  dual

The Num function returns a dual value with both the string and the numeric value. The function takes the numeric value of the input expression and generates a string representing the number.

Arguments

| Argument | Description |
| --- | --- |
| number | The text string to be evaluated. |
| format | String specifying how the resulting string is to be formatted. If omitted, the decimal and thousand separators that are set in the data load script are used. The Num function supports many format options for different numeric structures, for example:  #,##0: ​Displays a number without decimal places.  #,##0.00: ​Displays a number with two decimal places.  ##0.00%: Displays a number as a percentage with two decimal places.  ​#,##0;(#,##0): Formats negative numbers to appear in parentheses.  $#,##0.00: Formats numbers as currency with a $ symbol.  ​0.00E+0: Displays numbers in scientific notation. |
| dec\_sep | String specifying the decimal number separator. If omitted, the value of the variable DecimalSep that is set in the data load script is used. The Num function supports many decimal number separator formats, for example:  Comma ​' , ': For example, $1,000,00 for one thousand dollars.  Period ' . ':​ For example, € 1,000.00.  Hyphen ' - ': When used instead of the traditional period or comma for the decimal separator, it shows values like ¥1,000-00.  ​For more information, see [*DecimalSep*](../NumberInterpretationVariables/DecimalSep.htm). |
| thou\_sep | String specifying the thousands number separator. If omitted, the value of the variable ThousandSep that is set in the data load script is used. The Num function supports many options for the thousands number separator:  Period ​' . ': Uses a period for the thousands separator (common in some European formats), displaying as $1.000,00 if combined with a comma decimal separator.  Space ​' ': Uses a space for the thousands separator, which is common in some European countries. Displays as € 1 000.00.  Underscore ​'\_':​ Uses an underscore for the thousands separator, which is sometimes used in technical or specific regional formats. Displays values like $1\_000.00.  ​For more information, see [*ThousandSep*](../NumberInterpretationVariables/ThousandSep.htm). |

For more information on number formatting see [Conventions for number and time formats](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/conventions-number-time-formats.htm).

Example: Chart expressions

| Example | Results (String value returned) |
| --- | --- |
| Num(35648.312) | Returns 35648.312 (depends on the environment variables in the script) |
| Num(35648.312, '0.0', '.') | Returns 35648.3 |
| Num(35648.312, '0,00', ',') | Returns 3,56,48 |
| Num(35648.312, '#,##0.0', '.', ',') | Returns 35,648.3 |
| Num(35648.312, '# ##0', ',', ' ') | Returns 35 648 |

## Example - Num fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following field in a data table:

  - InputValue

Load script

```
Example:
Load * inline [
InputValue
35648
3564800
356.48
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputValue

Create the following measures:

- =Num(InputDate), to view the value as a number that is formatted using the system settings.
- =Num(InputValue, '0.0', '.'), to view the value as a number that is formatted using the format supplied in the function.
- =Num(InputValue, '0,00', ','), to view the value as a number that is formatted using the format supplied in the function.
- =Num(InputValue, '#,##0.0', '.', ','), to view the value as a number that is formatted using the format supplied in the function.
- =Num(InputValue, '# ##0', ',', ' '), to view the value as a number that is formatted using the format supplied in the function.

Results table

| InputValue | Num(InputDate) | Num(InputValue, '0.0', '.') | Num(InputValue, '0,00', ',') | Num(InputValue, '#,##0.0', '.', ',') | Num(InputValue, '# ##0', ',', ' ') |
| --- | --- | --- | --- | --- | --- |
| 356.48 | 356.48 | 356.5 | 3,56 | 356.5 | 356 |
| 35648 | 35648 | 35648.0 | 3,56,48 | 35,648.0 | 35 648 |
| 3564800 | 3564800 | 3564800.0 | 3,56,48,00 | 3,564,800.0 | 3 564 800 |

The results show how the Num function can display the values for the InputValue field based on the format supplied in the function expression.

Load script

The Num function can be used in a load script to format a number, even if the thousand and decimal separators are already set in the script. The load script below includes specific thousand and decimal separators but then uses Num to format data in different ways.

Load script

In the Data load editor, create a new section, and then add the example script and run it. Then add, at least, the fields listed in the results table to a [sheet](#glossary-0 "Glossary term") in your application to see the result.

```
SET ThousandSep=',';
SET DecimalSep='.';
Transactions:
Load
*,
Num(transaction_amount) as [No formatting],
Num(transaction_amount,'0') as [0],
Num(transaction_amount,'#,##0') as [#,##0],
Num(transaction_amount,'# ###,00') as [# ###,00],
Num(transaction_amount,'# ###,00',',',' ') as [# ###,00 , ',' , ' '],
Num(transaction_amount,'#,###.00','.',',') as [#,###.00 , '.' , ','],
Num(transaction_amount,'$#,###.00') as [$#,###.00],
;
Load * Inline [
transaction_id, transaction_date, transaction_amount, transaction_quantity, discount, customer_id, size, color_code
3750, 20180830, 12423.56, 23, 0,2038593, L, Red
3751, 20180907, 5356.31, 6, 0.1, 203521, m, orange
3752, 20180916, 15.75, 1, 0.22, 5646471, S, blue
3753, 20180922, 1251, 7, 0, 3036491, l, Black
3754, 20180922, 21484.21, 1356, 75, 049681, xs, Red
3756, 20180922, -59.18, 2, 0.333333333333333, 2038593, M, Blue
3757, 20180923, 3177.4, 21, .14, 203521, XL, Black
];
```

Results

Qlik Sense table showing the results from different uses of the Num function in the load script. The fourth column of the table contains incorrect formatting for example purposes.

| No formatting | 0 | #,##0 | # ###,00 | # ###,00 , ',' , ' ' | #,###.00 , '.' , ',' | $#,###.00 |
| --- | --- | --- | --- | --- | --- | --- |
| -59.18 | -59 | -59 | -59###,00 | -59,18 | -59.18 | $-59,18 |
| 15.75 | 16 | 16 | 16###,00 | 15,75 | 15.75 | $15,75 |
| 1251 | 1251 | 1,251 | 1251###,00 | 1 251,00 | 1,251.00 | $1,251.00 |
| 3177.4 | 3177 | 3,177 | 3177###,00 | 3 177,40 | 3,177.40 | $3,177.40 |
| 5356.31 | 5356 | 5,356 | 5356###,00 | 5 356,31 | 5,356.31 | $5,356.31 |
| 12423.56 | 12424 | 12,424 | 12424###,00 | 12 423,56 | 12,423.56 | $12,423.56 |
| 21484.21 | 21484 | 21,484 | 21484###,00 | 21 484,21 | 21,484.21 | $21,484.21 |

## Example - Num scenario

Chart expression

Overview

A dataset contains sales data that you want to present using a simpler numeric format.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - Sales

Load script

```
Example:
Load * inline [
Customer, Sales
Customer A, 2550000
Customer B, 12500
Customer C, 15000
Customer D, 250
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measure:

- =If(Sales > 1000000, Num(Sales/1000000, '#,##0.00M'), If(Sales > 1000, Num(Sales/1000, '#,##0.00K'), Num(Sales, '#,##0.00'))), to set the numeric representation of the values.

Results table

| Customer | If(Sales > 1000000, Num(Sales/1000000, '#,##0.00M'), If(Sales > 1000, Num(Sales/1000, '#,##0.00K'), Num(Sales, '#,##0.00'))) |
| --- | --- |
| Customer A | 2.55M |
| Customer B | 12.50K |
| Customer C | 15.00K |
| Customer D | 250.00 |

The measure expression in column 2 uses the Num function to present the data in a simplified numeric format.

Load script

The Num function can be used in a load script to format a number as a percentage.

Load script

In the Data load editor, create a new section, and then add the example script and run it. Then add the fields listed in the results column to a sheet in your application to see the result.

SET ThousandSep=',';
SET DecimalSep='.';
Transactions:
Load
\*,
Num(discount,'#,##0%') as [Discount #,##0%]
;
Load \* Inline [
transaction\_id, transaction\_date, transaction\_amount, transaction\_quantity, discount, customer\_id, size, color\_code
3750, 20180830, 12423.56, 23, 0,2038593, L, Red
3751, 20180907, 5356.31, 6, 0.1, 203521, m, orange
3752, 20180916, 15.75, 1, 0.22, 5646471, S, blue
3753, 20180922, 1251, 7, 0, 3036491, l, Black
3754, 20180922, 21484.21, 1356, 75, 049681, xs, Red
3756, 20180922, -59.18, 2, 0.333333333333333, 2038593, M, Blue
3757, 20180923, 3177.4, 21, .14, 203521, XL, Black
];

Qlik Sense table showing the results of the Num function being used in the load script to format percentages.

| Discount | Discount #,##0% |
| --- | --- |
| 0 | 0% |
| 0.1 | 10% |
| 0.22 | 22% |
| 0 | 0% |
| 75 | 7,500% |
| 0.333333333333333 | 33% |
| .14 | 14% |
