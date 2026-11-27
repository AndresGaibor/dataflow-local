---
title: "ThousandSep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/ThousandSep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---

# ThousandSep

Expand/Collapse all

# ThousandSep

The thousands separator defined replaces the digit grouping symbol of the operating
system (regional
settings).

Syntax:

ThousandSep

Qlik Sense object using the ThousandSep variable (with thousands separator)

![Example of a Qlik Sense object with a value using the thousands separator. The image shows a measure 'max(amount)', and the value of this measure is 47,873,578,754.00.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-thousandsep-basic-example.png "Click to view full size")

Qlik Sense applications interpret text [fields](#glossary-0 "Glossary term") that conform to this formatting as numbers. This formatting will be displayed in [chart](#glossary-1 "Glossary term") objects when a numerical field’s Number formatting property is set to Number.

ThousandSep is helpful when handling data sources received from multiple regional settings.

Information noteIf the ThousandSep variable is modified after objects have already been created and formatted in the application, the user will need to re-format each relevant field by de-selecting and then re-selecting the Number formatting property Number.

The following examples show possible uses of the ThousandSep system variable:

Set ThousandSep=','; //(for example, seven billion will be displayed as: 7,000,000,000)

Set ThousandSep=' '; //(for example, seven billion will be displayed as: 7 000 000 000)

These topics may help you work with this function:

Related topics

| Topic | Description |
| --- | --- |
| [*DecimalSep*](DecimalSep.htm) | In instances of text field interpretation, the decimal separator settings, as provided by this function, must also be respected. For number formatting, DecimalSep will be used by Qlik Sense where necessary. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 - Default system variables

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-2 "Glossary term") which is loaded into a table named Transactions.
- Use of the default ThousandSep variable definition.

Load script

```
Transactions:
Load
date,
id,
amount
Inline
[
date,id,amount
01/01/2022,1,10000000441
01/02/2022,2,21237492432
01/03/2022,3,41249475336
01/04/2022,4,24313369837
01/05/2022,5,47873578754
01/06/2022,6,24313884663
01/07/2022,7,28545883436
01/08/2022,8,35545828255
01/09/2022,9,37565817436
01/10/2022,10,3454343566
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add this field as a dimension:date.
2. Add the following [measure](#glossary-3 "Glossary term"):

   =sum(amount)
3. In the [properties](#glossary-4 "Glossary term") panel, under Data, select the measure.
4. Under Number formatting, select Number.

Adjusting number formatting for a chart measure

![Setting the Number formatting property for a measure to Number.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-thousandsep-number-formatting.png "Click to view full size")

Results table

| date | =sum(amount) |
| --- | --- |
| 01/01/2022 | 10,000,000,441.00 |
| 01/02/2022 | 21,237,492,432.00 |
| 01/03/2022 | 41,249,475,336.00 |
| 01/04/2022 | 24,313,369,837.00 |
| 01/05/2022 | 47,873,578,754.00 |
| 01/06/2022 | 24,313,884,663.00 |
| 01/07/2022 | 28,545,883,436.00 |
| 01/08/2022 | 35,545,828,255.00 |
| 01/09/2022 | 37,565,817,436.00 |
| 01/10/2022 | 3,454,343,566.00 |

In this example, the default ThousandSep definition, which is set to comma format (‘,’), is used. In the results table, the format of the amount field displays a comma between thousand groupings.

## Example 2 - Changing system variable

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The same dataset from the first example, which is loaded into a table named Transactions.
- Modification of the ThousandSep definition, at the start of the script, to display a '\*' character as the thousands separator. This is an extreme example, and is used solely to demonstrate the functionality of the variable.

The modification used in this example is extreme and not commonly used, but is shown here to demonstrate the functionality of the variable.

Load script

```
SET ThousandSep='*';

Transactions:
Load
date,
id,
amount
Inline
[
date,id,amount
01/01/2022,1,10000000441
01/02/2022,2,21237492432
01/03/2022,3,41249475336
01/04/2022,4,24313369837
01/05/2022,5,47873578754
01/06/2022,6,24313884663
01/07/2022,7,28545883436
01/08/2022,8,35545828255
01/09/2022,9,37565817436
01/10/2022,10,3454343566
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add this field as a dimension:date.
2. Add the following measure:

   =sum(amount)
3. In the properties panel, under Data, select the measure.
4. Under Number formatting, select Custom.

Results table

| date | =sum(amount) |
| --- | --- |
| 01/01/2022 | 10\*000\*000\*441.00 |
| 01/02/2022 | 21\*237\*492\*432.00 |
| 01/03/2022 | 41\*249\*475\*336.00 |
| 01/04/2022 | 24\*313\*369\*837.00 |
| 01/05/2022 | 47\*873\*578\*754.00 |
| 01/06/2022 | 24\*313\*884\*663.00 |
| 01/07/2022 | 28\*545\*883\*436.00 |
| 01/08/2022 | 35\*545\*828\*255.00 |
| 01/09/2022 | 37\*565\*817\*436.00 |
| 01/10/2022 | 3\*454\*343\*566.00 |

At the start of the script, the ThousandSep system variable is modified to a '\*'. In the results table, the format of the amount field can be seen to display a ‘\*’ between thousand grouping.

## Example 3 - Text interpretation

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a table named Transactions.
- Data which has its numerical field in text format, with a comma used as the thousands separator.
- Use of the default ThousandSep system variable.

Load script

```
Transactions:
Load
date,
id,
amount
Inline
[
date,id,amount
01/01/2022,1,'10,000,000,441'
01/02/2022,2,'21,492,432'
01/03/2022,3,'4,249,475,336'
01/04/2022,4,'24,313,369,837'
01/05/2022,5,'4,873,578,754'
01/06/2022,6,'313,884,663'
01/07/2022,7,'2,545,883,436'
01/08/2022,8,'545,828,255'
01/09/2022,9,'37,565,817,436'
01/10/2022,10,'3,454,343,566'
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table and add this field as a dimension:date.
2. Add the following measure:

   =sum(amount)
3. In the properties panel, under Data, select the measure.
4. Under Number formatting, select Number.
5. Add the following measure to evaluate whether or not the amount field is a numerical value:

   =isnum(amount)

Results table

| date | =sum(amount) | =isnum(amount) |
| --- | --- | --- |
| 01/01/2022 | 10,000,000,441.00 | -1 |
| 01/02/2022 | 21,492,432.00 | -1 |
| 01/03/2022 | 4,249,475,336.00 | -1 |
| 01/04/2022 | 24,313,369,837.00 | -1 |
| 01/05/2022 | 4,873,578,754.00 | -1 |
| 01/06/2022 | 313,884,663.00 | -1 |
| 01/07/2022 | 2,545,883,436.00 | -1 |
| 01/08/2022 | 545,828,255.00 | -1 |
| 01/09/2022 | 37,565,817,436.00 | -1 |
| 01/10/2022 | 3\*454\*343\*566.00 | -1 |

Once the data is loaded, we can see that Qlik Sense has interpreted the amount field as a numerical value, due to the data conforming to the ThousandSep variable. This is demonstrated by the isnum() function, which evaluates each entry to -1, or TRUE.

Information note

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.
