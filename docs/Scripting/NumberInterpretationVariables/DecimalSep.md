---
title: "DecimalSep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "Number interpretation variables"]
---
# DecimalSep

The decimal separator defined replaces the decimal symbol set by your regional settings.

Qlik Sense automatically interprets text as numbers whenever a recognizable number pattern is encountered. The `ThousandSep` and `DecimalSep` system [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-0 "Glossary term") determine the makeup of the patterns applied when parsing text as numbers. The `ThousandSep` and `DecimalSep` variables set the default number format pattern when visualizing numeric content in front-end [charts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-1 "Glossary term") and tables. That is, it directly impacts the **Number formatting** options for any front end expression.

Assuming a thousand separator of comma ‘`,`’ and a decimal separator of ‘`.`’, these are examples of patterns that would be implicitly converted to numeric equivalent values:

0,000.00

0000.00

0,000

These are examples of patterns that would remain unchanged as text; that is, not converted to numeric:

0.000,00

0,00

Syntax:

`DecimalSep`

Function examples

| Example | Result |
| --- | --- |
| `Set DecimalSep='.';` | Sets ‘.’ as the decimal separator. |
| `Set DecimalSep=',';` | Sets ‘,’ as the decimal separator. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example – Effect of setting number separator variables on different input data

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-2 "Glossary term") of sums and dates with the sums set in different format patterns.
- A table named `Transactions`.
- The `DecimalSep` variable which is set to ‘`.`’.
- The `ThousandSep` variable which is set to '`,`'.
- The `delimiter` variable that is set as the '|' character to separate the different fields in a line.

Load script

```
Set ThousandSep=','; 
Set DecimalSep='.'; 
						
Transactions: 
Load date, 
id, 
amount as amount 
Inline  
[ 
date|id|amount 
01/01/2022|1|1.000-45 
01/02/2022|2|23.344 
01/03/2022|3|4124,35 
01/04/2022|4|2431.36 
01/05/2022|5|4,787 
01/06/2022|6|2431.84 
01/07/2022|7|4132.5246 
01/08/2022|8|3554.284 
01/09/2022|9|3.756,178 
01/10/2022|10|3,454.356 
] (delimiter is '|');
```

Results

Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-3 "Glossary term"). Create a new table and add this [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-4 "Glossary term") as a [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-5 "Glossary term") `amount`.

Create this [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm#glossary-6 "Glossary term"):

`=sum(amount)`

Results table

| Amount | =Sum(amount) |
| --- | --- |
| Totals | 20814.7086 |
| 1.000-45 |  |
| 3.756,178 |  |
| 4124,35 |  |
| 23.344 | 23.344 |
| 2431.36 | 2431.36 |
| 2431.84 | 2431.84 |
| 3,454.356 | 3454.356 |
| 3554.284 | 3554.284 |
| 4132.5246 | 4132.5246 |
| 4,787 | 4787 |

Any value not interpreted as number remains as text and is aligned to the left by default. Any successfully converted values are aligned to the right, retaining the original input format.

The expression column shows the numeric equivalent, which is by default formatted with only a decimal separator ‘`.`’. This can be overridden with the **Number formatting** drop down setting in the expression configuration.
