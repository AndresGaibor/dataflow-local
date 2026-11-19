---
title: "First"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
# First

The `First` prefix to a `LOAD` or `SELECT` (SQL) statement is used for loading a set maximum number of records from a data source table. A typical use case for using the `First` prefix is when you want to retrieve a small subset of records from a large and/or slow data load step. As soon as the defined “`n`” number of records has been loaded, the load step terminates prematurely, and the rest of the script execution continues as normal.

Syntax:

First n (
loadstatement | selectstatement
)

Arguments

| Argument | Description |
| --- | --- |
| `n` | An arbitrary expression that evaluates to an integer indicating the maximum number of records to be read. `n` can also be enclosed in parentheses: `(n)`. |
| `loadstatement | selectstatement` | The `load statement/select statement` that follows the n argument will define the specified table that must be loaded with the set maximum number of records. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function examples

| Example | Result |
| --- | --- |
| `FIRST 10 LOAD * from abc.csv;` | This example will retrieve the first ten lines from an excel file. |
| `FIRST (1) SQL SELECT * from Orders;` | This example will retrieve the first selected line from the `Orders` [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm#glossary-0 "Glossary term"). |

## Example – Load the first five rows

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset of dates from the first two weeks of 2020.
- The `First` [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm#glossary-1 "Glossary term") that instructs the application to only load the first five records.

Load script

```
Sales: 
FIRST 5 
LOAD 
* 
Inline [ 
date,sales 
01/01/2020,6000 
01/02/2020,3000 
01/03/2020,6000 
01/04/2020,8000 
01/05/2020,5000 
01/06/2020,7000 
01/07/2020,3000 
01/08/2020,5000 
01/09/2020,9000 
01/10/2020,5000 
01/11/2020,7000 
01/12/2020,7000 
01/13/2020,7000 
01/14/2020,7000 
];
```

Results

Load the data and open a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm#glossary-2 "Glossary term"). Create a new table and add `Date` as a [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm#glossary-3 "Glossary term") and `sum(sales)` as a [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm#glossary-4 "Glossary term"):

Results table

| Date | sum(sales) |
| --- | --- |
| 01/01/2020 | 6000 |
| 01/02/2020 | 3000 |
| 01/03/2020 | 6000 |
| 01/04/2020 | 8000 |
| 01/05/2020 | 5000 |

The script only loads the first five records of the `Sales` table.

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Select*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm)
