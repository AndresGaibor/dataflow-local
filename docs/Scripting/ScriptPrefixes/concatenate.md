---
title: "Concatenate"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
Expand/Collapse all

# Concatenate

`Concatenate` is a script load prefix that enables a [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm#glossary-0 "Glossary term") to be appended to an already existing in-memory table. It is often used to append different sets of transactional data to a single central [fact](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm#glossary-1 "Glossary term") table, or to build up common reference datasets of a specific type that originate from multiple sources. It is similar in functionality to a SQL UNION operator.

The resulting table from a `concatenate` operation will contain the original dataset with the new rows of data appended to the bottom of that table. The source and target tables may have different fields present. Where fields are different, the resulting table will be widened to represent the combined result of all fields present in both the source table and the target table.

Syntax:

Concatenate[ (tablename ) ] ( loadstatement |
selectstatement )

Arguments

| Argument | Description |
| --- | --- |
| `tablename` | The name of an existing table. The named table will be the target of the `Concatenate` operation and any records of data loaded will be appended to that table. If the `tablename` parameter isn't used, the target table will be the last loaded table before this statement. |
| `loadstatement/selectstatement` | The `loadstatement/selectstatement` argument that follows the `tablename` argument will be concatenated to the specified table. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

Function example

| Example | Result |
| --- | --- |
| `Concatenate(Transactions) Load …. ;` | The data loaded in the load statement below the `Concatenate` prefix will be appended to the existing in-memory table named `Transactions` (assuming that a table named `Transactions` has been loaded prior to this point in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm#glossary-2 "Glossary term"). |

## Example 1 – Appending multiple sets of data to a target table with Concatenate load prefix

Load script and results

Overview

In this example you will load two scripts in sequential order.

- The first load script contains an initial dataset with dates and amounts that is sent to a table named `Transactions`.
- The second load script contains:

  - A second dataset that is appended to the initial dataset by using the `Concatenate` prefix. This dataset has an additional field, `type`, that is not in the initial dataset.
  - The `Concatenate` prefix.

Open the data load editor and add the load script below to a new tab.

First load script

```
Transactions: 
Load * Inline [ 

id, date, amount 
3750, 08/30/2018, 23.56 
3751, 09/07/2018, 556.31 
3752, 09/16/2018, 5.75 
3753, 09/22/2018, 125.00 
3754, 09/22/2018, 484.21 
3756, 09/22/2018, 59.18 
3757, 09/23/2018, 177.42 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `id`
- `date`
- `amount`

First load script results table

| id | date | amount |
| --- | --- | --- |
| 3750 | 08/30/2018 | 23.56 |
| 3751 | 09/07/2018 | 556.31 |
| 3752 | 09/16/2018 | 5.75 |
| 3753 | 09/22/2018 | 125.00 |
| 3754 | 09/22/2018 | 484.21 |
| 3756 | 09/22/2018 | 59.18 |
| 3757 | 09/23/2018 | 177.42 |

The table shows the initial dataset.

Second load script

Open the data load editor and add the load script below .

```
Concatenate(Transactions) 
Load * Inline [ 
id, date, amount, type 
3758, 10/01/2018, 164.27, Internal 
3759, 10/03/2018, 384.00, External 
3760, 10/06/2018, 25.82, Internal 
3761, 10/09/2018, 312.00, Internal 
3762, 10/15/2018, 4.56, Internal 
3763, 10/16/2018, 90.24, Internal 
3764, 10/18/2018, 19.32, External 
];
```

Results

Load the data and go to the [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm#glossary-3 "Glossary term"). Create this [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm#glossary-4 "Glossary term") as a [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm#glossary-5 "Glossary term").

- `type`

Second load script results table

| id | date | amount | type |
| --- | --- | --- | --- |
| 3750 | 08/30/2018 | 23.56 | - |
| 3751 | 09/07/2018 | 556.31 | - |
| 3752 | 09/16/2018 | 5.75 | - |
| 3753 | 09/22/2018 | 125.00 | - |
| 3754 | 09/22/2018 | 484.21 | - |
| 3756 | 09/22/2018 | 59.18 | - |
| 3757 | 09/23/2018 | 177.42 | - |
| 3758 | 10/01/2018 | 164.27 | Internal |
| 3759 | 10/03/2018 | 384.00 | External |
| 3760 | 10/06/2018 | 25.82 | Internal |
| 3761 | 10/09/2018 | 312.00 | Internal |
| 3762 | 10/15/2018 | 4.56 | Internal |
| 3763 | 10/16/2018 | 90.24 | Internal |
| 3764 | 10/18/2018 | 19.32 | External |

Note the null values in the `type` field for the first seven records loaded where `type` had not been defined.

## Example 2 – Appending multiple sets of data to a target table using implicit concatenation

Load script and results

Overview

A typical use case for implicitly appending data is when you load several files of identically structured data and want to append them all to a target table.

For example, by using `wildcards` in file names with syntax such as:

```
	 myTable: 
	  Load * from [myFile_*.qvd] (qvd); 
						
```

or in loops using constructs such as:

```
	for each file in filelist('myFile_*.qvd') 

	myTable: 
	Load * from [$(file)] (qvd); 

	next file
```

> **Note:** Implicit concatenation will take place between any two tables that are loaded with identically named fields, even if they aren't defined after one another in the script. This can lead to data being unintentionally appended to tables. If you don't want a secondary table with identical fields to be appended in this way, use the `NoConcatenate` load prefix. Renaming the table with an alternate table name tag is not sufficient to prevent implicit concatenation to occur. For more information, see [*NoConcatenate*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/NoConcatenate.htm).

In this example you will load two scripts in sequential order.

- The first load script contains an initial dataset with four fields that is sent to a table named `Transactions`.
- The second load script contains a dataset with the same fields as the first dataset.

Open the data load editor and add the load script below to a new tab.

First load script

```
Transactions: 
Load * Inline [ 
id, date, amount, type 
3758, 10/01/2018, 164.27, Internal 
3759, 10/03/2018, 384.00, External 
3760, 10/06/2018, 25.82, Internal 
3761, 10/09/2018, 312.00, Internal 
3762, 10/15/2018, 4.56, Internal 
3763, 10/16/2018, 90.24, Internal 
3764, 10/18/2018, 19.32, External 
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `id`
- `date`
- `amount`
- `type`

First load script results table

| id | date | type | amount |
| --- | --- | --- | --- |
| 3758 | 10/01/2018 | Internal | 164.27 |
| 3759 | 10/03/2018 | External | 384.00 |
| 3760 | 10/06/2018 | Internal | 25.82 |
| 3761 | 10/09/2018 | Internal | 312.00 |
| 3762 | 10/15/2018 | Internal | 4.56 |
| 3763 | 10/16/2018 | Internal | 90.24 |
| 3764 | 10/18/2018 | External | 19.32 |

The table shows the initial dataset.

Second load script

Open the data load editor and add the load script below .

```
Load * Inline [ 
id, date, amount, type 
3765, 11/03/2018, 129.40, Internal 
3766, 11/05/2018, 638.50, External 
];
```

Results

Load the data and go to the sheet.

Second load script results table

| id | date | type | amount |
| --- | --- | --- | --- |
| 3758 | 10/01/2018 | Internal | 164.27 |
| 3759 | 10/03/2018 | External | 384.00 |
| 3760 | 10/06/2018 | Internal | 25.82 |
| 3761 | 10/09/2018 | Internal | 312.00 |
| 3762 | 10/15/2018 | Internal | 4.56 |
| 3763 | 10/16/2018 | Internal | 90.24 |
| 3764 | 10/18/2018 | External | 19.32 |
| 3765 | 11/03/2018 | Internal | 129.40 |
| 3766 | 11/05/2018 | External | 638.50 |

The second dataset was implicitly concatenated onto the initial dataset because they had identical fields.
