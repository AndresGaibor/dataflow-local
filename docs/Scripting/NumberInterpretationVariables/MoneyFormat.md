---
title: "MoneyFormat"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyFormat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# MoneyFormat

Expand/Collapse all

# MoneyFormat

This system [variable](#glossary-0 "Glossary term") defines the format pattern used by Qlik for automatic translation of text to number where the number is prefixed by a monetary symbol. It also defines how [measures](#glossary-1 "Glossary term") whose Number Formatting [properties](#glossary-2 "Glossary term") are set to ‘Money’ will be displayed in [chart](#glossary-3 "Glossary term") objects.

The symbol defined as part of the format pattern in the MoneyFormat system variable replaces the currency symbol set by your regional settings.

Tip note

By default, Qlik Sense displays numbers and text differently in table charts. Numbers are right-aligned, and text is left-aligned. This makes it easy to find text-to-number conversion issues. Any tables on this page that show Qlik Sense results will use this formatting.

Syntax:

MoneyFormat

Set MoneyFormat='$ #,##0.00; ($ #,##0.00)';

This formatting will be displayed in chart objects when a numerical [field's](#glossary-4 "Glossary term") Number Formatting property is set to Money. Further, when numerical text fields are interpreted by Qlik Sense, if the currency symbol of the text field matches that of the symbol defined in the MoneyFormat variable, Qlik Sense will interpret this field as a monetary value.

This function is often used together with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*MoneyDecimalSep*](MoneyDecimalSep.htm) | For Number Formatting, MoneyDecimalSep will be used in field formatting of objects. |
| [*MoneyThousandSep*](MoneyThousandSep.htm) | For Number Formatting, MoneyThousandSep will be used in field formatting of objects. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 - MoneyFormat

Load script and results

Overview

Open the [Data load editor](#glossary-5 "Glossary term") and add the [load script](#glossary-6 "Glossary term") below to a new tab.

The load script contains a [dataset](#glossary-7 "Glossary term") which is loaded into a table named Transactions. The default MoneyFormat variable definition is used.

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
01/01/2022,1,$10000000441
01/02/2022,2,$21237492432
01/03/2022,3,$249475336
01/04/2022,4,$24313369837
01/05/2022,5,$7873578754
01/06/2022,6,$24313884663
01/07/2022,7,$545883436
01/08/2022,8,$35545828255
01/09/2022,9,$37565817436
01/10/2022,10,$3454343566
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- amount

Add this [measure](#glossary-8 "Glossary term"):

=Sum(amount)

Under Number formatting, select Money to configure Sum(amount) as a monetary value.

Results table

| date | Amount | =Sum(amount) |
| --- | --- | --- |
| Totals |  | $165099674156.00 |
| 01/01/2022 | $10000000441 | $10000000441.00 |
| 01/02/2022 | $21237492432 | $21237492432.00 |
| 01/03/2022 | $249475336 | $249475336.00 |
| 01/04/2022 | $24313369837 | $24313369837.00 |
| 01/05/2022 | $7873578754 | $7873578754.00 |
| 01/06/2022 | $24313884663 | $24313884663.00 |
| 01/07/2022 | $545883436 | $545883436.00 |
| 01/08/2022 | $35545828255 | $35545828255.00 |
| 01/09/2022 | $37565817436 | $37565817436.00 |
| 01/10/2022 | $3454343566 | $3454343566.00 |

The default MoneyFormat definition is used. This looks as follows: $###0.00;-$###0.00. In the results table, the format of the amount field displays the currency symbol and the decimal point and decimal places have been included.

## Example 2 - MoneyFormat with thousands separator and mixed input formats

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A mixed-input format dataset, which is loaded into a table named Transactions with thousands separators and decimal separators interspersed.
- A modification of the MoneyFormat definition is modified to include a comma as the thousands separator.
- One of the rows of data erroneously delimited with thousands separator commas in the wrong places. Note how this amount is left as text and not interpretable as a number.

Load script

```
SET MoneyThousandSep=',';
SET MoneyDecimalSep='.';
SET MoneyFormat = '$#,##0.00;-$#,##0.00';

Transactions:
Load
date,
id,
amount
Inline
[
date,id,amount
01/01/2022,1,'$10,000,000,441.45'
01/02/2022,2,'$212,3749,24,32.23'
01/03/2022,3,$249475336.45
01/04/2022,4,$24,313,369,837
01/05/2022,5,$7873578754
01/06/2022,6,$24313884663
01/07/2022,7,$545883436
01/08/2022,8,$35545828255
01/09/2022,9,$37565817436
01/10/2022,10,$3454343566
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- date
- amount

Add this measure:

=Sum(amount)

Under Number formatting, select Money to configure Sum(amount) as a monetary value.

Results table

| date | Amount | =Sum(amount) |
| --- | --- | --- |
| Totals |  | $119,548,811,911.90 |
| 01/01/2022 | $10,000,000,441.45 | $10,000,000,441.45 |
| 01/02/2022 | $212,3749,24,32.23 | $0.00 |
| 01/03/2022 | $249475336.45 | $249,475,336.45 |
| 01/04/2022 | $24 | $24.00 |
| 01/05/2022 | $7873578754 | $7,873,578,754.00 |
| 01/06/2022 | $24313884663 | $24,313,884,663.00 |
| 01/07/2022 | $545883436 | $545,883,436.00 |
| 01/08/2022 | $35545828255 | $35,545,828,255.00 |
| 01/09/2022 | $37565817436 | $37,565,817,436.00 |
| 01/10/2022 | $3454343566 | $3,454,343,566.00 |

At the start of the script, the MoneyFormat system variable is modified to include a comma as a thousands separator. In the Qlik Sense table, the formatting can be seen to include this separator. Furthermore, the row with the erroneous separator has not been interpreted correctly and remains as text. This is why it does not contribute towards the summation of the amount.
