---
title: "MoneyDecimalSep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
Expand/Collapse all

# MoneyDecimalSep

The decimal separator defined replaces the decimal symbol for currency set by your regional settings.

> **Tip:** By default, Qlik Sense displays numbers and text differently in table charts. Numbers are right-aligned, and text is left-aligned. This makes it easy to find text-to-number conversion issues. Any tables on this page that show Qlik Sense results will use this formatting.

Syntax:

MoneyDecimalSep

Qlik Sense applications will interpret text [fields](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm#glossary-0 "Glossary term") that conform to this formatting as monetary values. The text field must contain the currency symbol that is defined in the `MoneyFormat` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm#glossary-1 "Glossary term"). `MoneyDecimalSep` is particularly helpful when handling data sources received from multiple different regional settings.

The following example shows a possible use of the `MoneyDecimalSep` system variable:

Set MoneyDecimalSep='.';

This function is often used together with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| `MoneyFormat` | In instances of text field interpretation, the `MoneyFormat` symbol will be used as part of the interpretation. For Number Formatting, the `MoneyFormat` formatting will be used by Qlik Sense in Chart Objects. |
| `MoneyThousandSep` | In instances of text field interpretation, the `MoneyThousandSep` function must also be adhered to. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 - MoneyDecimalSep dot (.) notation

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm#glossary-2 "Glossary term") that is loaded into a table named `Transactions`.
- Provided data that has its monetary field in text format with a dot ‘.’ used as the decimal separator. Each record is also prefixed by a ‘$’ symbol, except for the last record, which is prefixed by a ‘£’ symbol.

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
01/01/2022,1,'$14.41'
01/02/2022,2,'$2,814.32'
01/03/2022,3,'$249.36'
01/04/2022,4,'$24.37'
01/05/2022,5,'$7.54'
01/06/2022,6,'$243.63'
01/07/2022,7,'$545.36'
01/08/2022,8,'$3.55'
01/09/2022,9,'$3.436'
01/10/2022,10,'£345.66'
];					
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:`amount`.

Add the following [measures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm#glossary-3 "Glossary term"):

- `isNum(amount)`
- `sum(amount)`

Review the results below, demonstrating the correct interpretation of all dollar ‘$’ values only.

Results table

| amount | =isNum(amount) | =Sum(amount) |
| --- | --- | --- |
| Totals | 0 | $3905.98 |
| £345.66 | 0 | $0.00 |
| $3.436 | -1 | $3.44 |
| $3.55 | -1 | $3.55 |
| $7.54 | -1 | $7.54 |
| $14.41 | -1 | $14.41 |
| $24.37 | -1 | $24.37 |
| 243.63 | -1 | $243.63 |
| $249.36 | -1 | $249.36 |
| $545.36 | -1 | $545.36 |
| $2,814.32 | -1 | $2814.32 |

The results table above shows how the `amount` field has been interpreted correctly for all dollar ($) prefixed values, whilst the pound (£) prefixed `amount` has not been converted to a monetary value.

## Example 2 - MoneyDecimalSep comma (,) notation

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table named `Transactions`.
- Provided data that has its monetary field in text format with a comma ‘,’ used as the decimal separator. Each record is also prefixed by a ‘$’ symbol, except for the last record, which erroneously uses the dot decimal separator '.'.

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
01/01/2022,1,'$14,41'
01/02/2022,2,'$2.814,32'
01/03/2022,3,'$249,36'
01/04/2022,4,'$24,37'
01/05/2022,5,'$7,54'
01/06/2022,6,'$243,63'
01/07/2022,7,'$545,36'
01/08/2022,8,'$3,55'
01/09/2022,9,'$3,436'
01/10/2022,10,'$345.66'
];
```

Results

Paragraph text for Results.

Load the data and open a sheet. Create a new table and add this field as a dimension:`amount`.

Add the following measures:

- `isNum(amount)`
- `sum(amount)`

Review the results below, demonstrating the correct interpretation of all values, except for the amount in which the decimal separator uses dot '.' notation. In that case, a comma should have been used instead.

Results table

| amount | =isNum(amount) | =Sum(amount) |
| --- | --- | --- |
| Totals | 0 | $3905.98 |
| $345.66 | 0 | $0.00 |
| $3,436 | -1 | $3.44 |
| $3,55 | -1 | $3.55 |
| $7,54 | -1 | $7.54 |
| $14,41 | -1 | $14.41 |
| $24,37 | -1 | $24.37 |
| $243,63 | -1 | $243.63 |
| $249,36 | -1 | $249.36 |
| $545,36 | -1 | $545.36 |
| $2.814,32 | -1 | $2814.32 |
