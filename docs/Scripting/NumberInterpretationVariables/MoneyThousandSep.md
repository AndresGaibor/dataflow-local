---
title: "MoneyThousandSep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
Expand/Collapse all

# MoneyThousandSep

The thousands separator defined replaces the digit grouping symbol for
currency set by your regional settings.

> **Tip:** By default, Qlik Sense displays numbers and text differently in table charts. Numbers are right-aligned, and text is left-aligned. This makes it easy to find text-to-number conversion issues. Any tables on this page that show Qlik Sense results will use this formatting.

Syntax:

MoneyThousandSep

Qlik Sense applications will interpret text [fields](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm#glossary-0 "Glossary term") that conform to this formatting as monetary values. The text field must contain the currency symbol that is defined in the `MoneyFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm#glossary-1 "Glossary term"). `MoneyThousandSep` is particularly helpful when handling data sources received from multiple different regional settings.

The following example shows a possible use of the `MoneyThousandSep` system variable:

Set MoneyDecimalSep=',';

This function is often used together with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| `MoneyFormat` | In instances of text field interpretation, the `MoneyFormat` symbol will be used as part of the interpretation. For Number Formatting, the `MoneyFormat` formatting will be used by Qlik Sense in [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm#glossary-2 "Glossary term") objects. |
| `MoneyDecimalSep` | In instances of text field interpretation, the `MoneyDecimalSep` function must also be adhered to. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 - MoneyThousandSep comma (,) notation

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm#glossary-3 "Glossary term") which is loaded into a table named `Transactions`.
- Provided data that has its monetary field in text format with a comma used as the thousands separator. Each record is also prefixed by a ‘$’ symbol.

Keep in mind that the `MoneyFormat` system variable defines dollar ‘$’ as the default currency.

Load script

```
SET MoneyThousandSep=',';
SET MoneyDecimalSep='.';
SET MoneyFormat='$###0.00;-$###0.00';

Transactions:
Load
date,
id,
amount
Inline 
[
date,id,amount
01/01/2022,1,'$10,000,000,441'
01/02/2022,2,'$21,237,492,432'
01/03/2022,3,'$249,475,336'
01/04/2022,4,'$24,313,369,837'
01/05/2022,5,'$7,873,578,754'
01/06/2022,6,'$24,313,884,663'
01/07/2022,7,'$545,883,436'
01/08/2022,8,'$35,545,828,255'
01/09/2022,9,'$37,565,817,436'
01/10/2022,10,'$3.454.343.566'
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:`amount`.

Add the following [measures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm#glossary-4 "Glossary term"):

- `isNum(amount)`
- `sum(amount)`

Review the results below. The table demonstrates the correct interpretation of all values using comma ‘,’ notation as the thousands separator.

The `amount` field has been interpreted correctly for all values, with the exception of one value which used a dot '.' as the thousands separator.

Results table

| amount | =isNum(amount) | =Sum(amount) |
| --- | --- | --- |
| Totals | 0 | $161645330590.00 |
| $3.454.343.566 | 0 | $0.00 |
| $249,475,336 | -1 | $249475336.00 |
| $545,883,436 | -1 | $545883436.00 |
| $7,873,578,754 | -1 | $7873578754.00 |
| $10,000,000,441 | -1 | $10000000441.00 |
| $21,237,492,432 | -1 | $21237492432.00 |
| $24,313,369,837 | -1 | $24313369837.00 |
| $24,33,884,663 | -1 | $24313884663.00 |
| $35,545,828,255 | -1 | $35545828255.00 |
| $37,565,817,436 | -1 | $37565817436.00 |

## Example 2 - MoneyThousandSep dot (.) notation

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table named `Transactions`.
- Provided data that has its monetary field in text format with a dot '.' used as the thousands separator. Each record is also prefixed by a ‘$’ symbol.

Keep in mind that the `MoneyFormat` system variable defines dollar ‘$’ as the default currency.

Load script

```
SET MoneyThousandSep='.';
SET MoneyDecimalSep=',';
SET MoneyFormat='$###0.00;-$###0.00';

Transactions:
Load
date,
id,
amount
Inline 
[
date,id,amount
01/01/2022,1,'$10.000.000.441'
01/02/2022,2,'$21.237.492.432'
01/03/2022,3,'$249.475.336'
01/04/2022,4,'$24.313.369.837'
01/05/2022,5,'$7.873.578.754'
01/06/2022,6,'$24.313.884.663'
01/07/2022,7,'$545.883.436'
01/08/2022,8,'$35.545.828.255'
01/09/2022,9,'$37.565.817.436'
01/10/2022,10,'$3,454,343,566'
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:`amount`.

Add the following measures:

- `isNum(amount)`
- `sum(amount)`

Review the results below, demonstrating the correct interpretation of all values using dot ‘.’ notation as the thousand separator.

The `amount` field has been interpreted correctly for all values, with the exception of one value which used a comma ',' as the thousands separator.

Results table

| amount | =isNum(amount) | =Sum(amount) |
| --- | --- | --- |
| Totals | 0 | $161645330590.00 |
| $3,545,343,566 | 0 | $0.00 |
| $249.475.336 | -1 | $249475336.00 |
| $545.883.436 | -1 | 545883436.00 |
| $7.873.578.754 | -1 | $7873578754.00 |
| $10.000.000.441 | -1 | $10000000441.00 |
| $21.237.492.432 | -1 | $21237492432.00 |
| $24.313.884.663 | -1 | $24313884663.00 |
| $24.313.884.663 | -1 | $24313884663.00 |
| $35.545.828.255 | -1 | $35545828255.00 |
| $37.565.817.436 | -1 | $37565817436.00 |
