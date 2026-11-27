---
title: "Money# Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/money_hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Interpretation functions"]
---

# Money# Script and chart function

Expand/Collapse all

# Money# Script and chart function

Money#() converts a text string to a money value, in the format set in the load script or the operating system, unless a format string is supplied. Custom decimal and thousand separator symbols are optional parameters.

Syntax:

Money#(text[, format[, dec\_sep
[, thou\_sep ] ] ])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| text | The text string to be evaluated. |
| format | String describing the expected input format to use when converting the string to a numeric interval. If omitted, the value set in the data load script for MoneyFormat is used.  The Money# function supports many format options for different money structures, for example:  ​$#,##0.00: Adds a dollar sign and two decimal places.  € #,##0: Adds a euro sign and no decimal places, with a space after the euro sign.  ​¥#,##0: Adds a Japanese yen sign with no decimal places.  ​$#,##0;($#,##0): Formats negative values in parentheses.  ​₣ #.##0,00:​ Adds a Swiss franc sign with periods as thousand separators and a comma for decimals (for example, ₣ 1.000,00).  ​R #,##0.00: South African rand sign with two decimal places and space after the rand symbol.  ​$ #,##0.000: Adds three decimal places to the dollar format. |
| dec\_sep | String specifying the decimal number separator. If omitted, the MoneyDecimalSep value set in the data load script is used. The Money# function supports many decimal number separator formats, for example:  Comma ​' , ': For example, $1,000,00 for one thousand dollars.  Period ' . ':​ For example, € 1,000.00.  Hyphen ' - ': When used instead of the traditional period or comma for the decimal separator, it shows values like ¥1,000-00. |
| thou\_sep | String specifying the thousands number separator. If omitted, the MoneyThousandSep value set in the data load script is used.  The Money# function supports many options for the thousands number separator:  Period ​' . ': Uses a period for the thousands separator (common in some European formats), displaying as $1.000,00 if combined with a comma decimal separator.  Space ​' ': Uses a space for the thousands separator, which is common in some European countries. Displays as € 1 000.00.  Underscore ​'\_':​ Uses an underscore for the thousands separator, which is sometimes used in technical or specific regional formats. Displays values like $1\_000.00. |

The Money# function generally
behaves like the Num# function but takes its default values for the decimal and thousand separators from the
script [variables](#glossary-0 "Glossary term") for money format or the system settings for currency.

Example: Chart expressions

| Example | Results |
| --- | --- |
| Money#('35 648,37 kr' , '# ##0,00 kr',',',' ' ) | Returns 35 648,37 kr when the MoneyFormat setting is # ##0,00 kr. The following need to be set in your load script for this to evaluate correctly as a number:   - SET MoneyDecimalSep=','; - SET MoneyThousandSep=' '; |
| Money#( '$35,648.37', ' $#', '.', ',' ) | Returns $35,648.37 when the following is set:   - MoneyFormat is $# - SET MoneyDecimalSep=','; - SET MoneyThousandSep=' '; |

## Example - Money# fundamentals

Load script

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called MoneyValue.
- A preceding load that uses the Money# function to convert the text values in the data into a value that Qlik Sense will recognize as a valid value.

Load script

```
SET MoneyFormat='$ #,##0.00';
SET MoneyThousandSep=',';
Example:
Load *, Money#(MoneyValue, '# ##0,00 kr',',',' ') as FormattedMoneyValue;
Load * inline [
MoneyValue
35 648,37 kr
56 735,56 kr
] (delimiter is ';');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- MoneyValue
- FormattedMoneyValue

Create the following measures:

- =Money( FormattedMoneyValue, 'kr #,##0', '.' , ',' ), to view the value as money, formatted using the arguments set in the Money function.
- =Num(FormattedMoneyValue) to return the numeric value after it has been processed by the Money# function.

Results table

| MoneyValue | FormattedMoneyValue | Money( FormattedMoneyValue, 'kr #,##0', '.' , ',' ) | Num(FormattedMoneyValue) |
| --- | --- | --- | --- |
| 56 735,56 kr | 56 735,56 kr | kr 56,736 | 56735.56 |
| 35 648,37 kr | 35 648,37 kr | kr 35,648 | 35648.37 |

The table of results shows how values can be displayed using the following functions and format: Money#, Money, and Num. The second column shows the dimension FormattedMoneyValue, which was calculated using the Money# function to change the value to money with the format '# ##0,00 kr',',',' '. The third column uses the Money function to change the currency format of FormattedMoneyValue to 'kr #,##0', '.' , ','. The fourth column uses the Num function to show the numeric value of the FormattedMoneyValue dimension using the format in the system variable.

## Example - Money# scenario

Load script

Overview

A dataset of sales orders contains fields that use different currencies. This example shows you how to separate and sum the sales values based on currency.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:
  - TransactionID
  - Currency
  - Amount
- The MoneyDecimalSep, MoneyFormat and MoneyThousandSep system variables set to use a different format than those used in the data for demonstration purposes.
- A preceding load which loads the fields TransactionID, Currency, and Amount, and creates the following field:

  - AmountValue, this field uses the Money# function to convert the text that it receives to a value that the system understands.

Load script

```
SET MoneyDecimalSep='-';
SET MoneyFormat='###0-00';
SET MoneyThousandSep=';';
Example:
LOAD
TransactionID,
Currency,
Amount,
IF(Currency = 'USD', Money#(Amount, '$#,##0.00','.',','),
IF(Currency = 'EUR', Money#(Amount, '€ #.##0,00',',','.'))) AS AmountValue
INLINE [
TransactionID, Currency, Amount
"TXN001", "USD", "$ 1,500.00"
"TXN002", "EUR", "€ 1.200,75"
"TXN003", "USD", "$ 1,750.50"
"TXN004", "EUR", "€ 950,00"
"TXN005", "USD", "$ 2,600.25"
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- TransactionID
- Currency
- Amount
- AmountValue

Create the following measure:

- Num(AmountValue)

Results table

| TransactionID | Currency | Amount | AmountValue | Num(AmountValue) |
| --- | --- | --- | --- | --- |
| TXN001 | USD | $1,500.00 | $ 1,500.00 | 1500 |
| TXN002 | EUR | € 1.200,75 | € 1.200,75 | 1200.75 |
| TXN003 | USD | $ 1,750.50 | $ 1,750.50 | 1750.5 |
| TXN004 | EUR | € 950,00 | € 950,00 | 950 |
| TXN005 | USD | $ 2,600.25 | $ 2,600.25 | 2600.25 |

The results show how the Money# function converts text values to monetary numeric values which can then be evaluated. For example, the values in the Amount field are text and appear left-aligned. However, once these are processed by the Money# function to create the new field, AmountValue, the system now recognizes these as monetary numeric values. The Num function, used in the right-most column, can now evaluate the monetary values in AmountValue and change the format from money to a number.
