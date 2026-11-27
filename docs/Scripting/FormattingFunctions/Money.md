---
title: "Money Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Money.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Formatting functions"]
---

# Money Script and chart function

Expand/Collapse all

# Money Script and chart function

Money() formats an
expression numerically as a money value, in the format set in the system variables set in the data load script, or in the operating system, unless a format string is supplied, and optional decimal and thousands separators.

Syntax:

Money(number[, format[, dec\_sep[, thou\_sep]]])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| number | The number to be formatted. |
| format | String describing how the resulting money string is to be formatted. If omitted, the value set in the data load script for MoneyFormat is used. The Money function supports many format options for different date structures, for example:  ​$#,##0.00: Adds a dollar sign and two decimal places.  € #,##0: Adds a euro sign and no decimal places, with a space after the euro sign.  ​¥#,##0: Adds a Japanese yen sign with no decimal places.  ​$#,##0;($#,##0): Formats negative values in parentheses.  ​₣ #.##0,00:​ Adds a Swiss franc sign with periods as thousand separators and a comma for decimals (for example, ₣ 1.000,00).  ​R #,##0.00: South African rand sign with two decimal places and space after the rand sign.  ​$ #,##0.000: Adds three decimal places to the dollar format. |
| dec\_sep | String specifying the decimal number separator. If omitted, the MoneyDecimalSep value set in the data load script is used. The Money function supports many decimal number separator formats, for example:  Comma ​' , ': For example, $1,000,00 for one thousand dollars.  Period ' . ':​ For example, € 1,000.00.  Hyphen ' - ': When used instead of the traditional period or comma for the decimal separator, it shows values like ¥1,000-00. |
| thou\_sep | String specifying the thousands number separator. If omitted, the MoneyThousandSep value set in the data load script is used. The Money function supports many options for the thousands number separator:  Period ​' . ': Uses a period for the thousands separator (common in some European formats), displaying as $1.000,00 if combined with a comma decimal separator.  Space ​' ': Uses a space for the thousands separator, which is common in some European countries. Displays as € 1 000.00.  Underscore ​'\_':​ Uses an underscore for the thousands separator, which is sometimes used in technical or specific regional formats. Displays values like $1\_000.00. |

If the format, dec\_sep, and thou\_sep arguments are omitted, the currency format set in the operating system is used when formatting each specific part of the output. The operating system settings are automatically included as system variables upon creation of the script, thus making sure that these are consistent throughout the entire application.

These system variables are MoneyFormat, MoneyDecimalSep, and MoneyThousandSep, and map to the format, dec\_sep, and thou\_sep function arguments respectively.

Example: Chart expressions

| Example | Results |
| --- | --- |
| Money( 35648 ) | Returns kr 35 648,00 when the MoneyFormat setting is kr ##0,00 and the MoneyThousandSep is a period ' ' . |
| Money( 35648, '#,##0 ¥', '.' , ',' ) | Returns 3,564,800 ¥ by ignoring the MoneyFormat setting and the MoneyThousandSep setting since the optional parameters Format, dec\_sep and thou\_sep are supplied in the function. |
| Money(35648) | Returns $ 35,648.00 when the MoneyFormat setting is $ #,##0.00 and the MoneyThousandSep is a comma ','. |

## Example - Money fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called InputValue.
- The following variable formats:

  - MoneyFormat variable, which uses the format: kr ##0,00
  - MoneyThousandSep variable set to use a space ' '

Load script

```
SET MoneyFormat='kr ##0,00';
SET MoneyThousandSep=' ';
Example:
Load * inline [
InputValue
35648
3564800
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputValue

Create the following measures:

- =Money(InputValue), to view the value as a money that is formatted using the system setting.
- =Money(InputValue, '#,##0 ¥', '.' , ','), to view the value as money that is formatted using the format supplied in the function.
- =Num(InputValue), to return the numeric value.

Results table

| InputValue | Money(InputValue) | Money(InputValue, '#,##0 ¥', '.' , ',') | Num(InputValue) |
| --- | --- | --- | --- |
| 35648 | kr35 648,00 | 35,648 ¥ | 35648 |
| 3564800 | kr3 564 800,00 | 3,564,800 ¥ | 3564800 |

In this example, you can see how the Money function displays values and how the values in the format parameter can change the output.

## Example - Money fundamentals using a different format setting

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called InputValue.
- The following variable formats:

  - MoneyFormat variable, which uses the format: $ #,##0.00
  - MoneyThousandSep variable set to use a comma ','

Load script

```
SET MoneyFormat='$ #,##0.00';
SET MoneyThousandSep=',';
Example:
Load * inline [
InputValue
35648
3564800
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputValue

Create the following measures:

- =Money(InputValue), to view the value as a money that is formatted using the system setting.
- =Money(InputValue, '#,##0 ¥', '.' , ', ), to view the value as money that is formatted using the format supplied in the function.
- =Num(InputValue), to return the numeric value.

Results table

| InputValue | Money(InputValue) | Money(InputValue, '#,##0 ¥', '.' , ',') | Num(InputValue) |
| --- | --- | --- | --- |
| 35648 | $ 35,648.00 | 35,648 ¥ | 35648 |
| 3564800 | $ 3,564,800.00 | 3,564,800 ¥ | 3564800 |

In this example, you can see how the Money function displays values and how the values in the format parameter can change the output.

## Example - Money scenario

Chart expression

Overview

Customer sales data is received in various currencies. You want to display the data in a table using the relevant currency format.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:
  - Customer
  - CurrencyCode
  - Sales
- The following variable formats:

  - MoneyFormat variable, which uses the format: $ ###0.00;-$ ###0.00
  - MoneyThousandSep variable set to use a comma ','
  - MoneyDecimalSep variable set to use a period '.'

Load script

```
SET MoneyThousandSep=',';
SET MoneyDecimalSep='.';
SET MoneyFormat='$ ###0.00;-$ ###0.00';
Example:
Load * inline [
Customer, CurrencyCode, Sales
Customer A, USD, 100008
Customer B, EUR, 12500
Customer C, YEN, 15000
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Customer

Create the following measure:

- =Money(Sales, If(CurrencyCode = 'USD', '$#,##0.00', If(CurrencyCode = 'EUR', '€ #,##0.00', '¥#,##0'))), to display the currency in the correct currency format.

Results table

| Customer | Money(Sales, If(CurrencyCode = 'USD', '$#,##0.00', If(CurrencyCode = 'EUR', '€ #,##0.00', '¥#,##0'))) |
| --- | --- |
| Customer A | $100,008.00 |
| Customer B | € 12,500.00 |
| Customer C | ¥15,000 |

The sales data now uses the currency format defined in the measure expression. The decimal and thousand parameters use the settings in the load script.
