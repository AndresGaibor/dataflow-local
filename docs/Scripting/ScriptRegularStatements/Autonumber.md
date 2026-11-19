---
title: "AutoNumber"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# AutoNumber

This statement creates a unique integer value for each distinct evaluated value in a field encountered during
the script execution.

You can also use the [*autonumber Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumber.htm) function inside a LOAD statement, but this has some limitations when you want to use an optimized load. You can create an optimized load by loading the data from a QVD file first, and then using the AutoNumber statement to convert values to symbol keys.

Syntax:

AutoNumber \*fieldlist [Using namespace] ]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| \*fieldlist | A comma-separated list of the fields where the values should be replaced by a unique integer value.  You can use wildcard characters ? and \* in the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm#glossary-0 "Glossary term") names to include all fields with matching names. You can also use \* to include all fields. You need to quote field names when wildcards are used. |
| namespace | Using namespace is optional. You can use this option if you want to create a namespace, where identical values in different fields share the same key.  If you do not use this option, all fields will have a separate key index. |

Limitations:

When you have several LOAD statements in the script, you need to place the AutoNumber statement after the final LOAD statement.

Example - script with AutoNumber

## Script example

In this example, the data is first loaded without the AutoNumber statement. The AutoNumber statement is then added to show the effect.

### Data used in the example

Load the following data as an inline load in the data load editor to create the script example below. Leave the AutoNumber statement commented out for now.

RegionSales:
LOAD \*,
Region &'|'& Year &'|'& Month as KeyToOtherTable
INLINE
[ Region, Year, Month, Sales
North, 2014, May, 245
North, 2014, May, 347
North, 2014, June, 127
South, 2014, June, 645
South, 2013, May, 367
South, 2013, May, 221
];
Budget:
LOAD Budget,
Region &'|'& Year &'|'& Month as KeyToOtherTable
INLINE
[Region, Year, Month, Budget
North, 2014, May, 200
North, 2014, May, 350
North, 2014, June, 150
South, 2014, June, 500
South, 2013, May, 300
South, 2013, May, 200
];
//AutoNumber KeyToOtherTable;

For more information about using inline loads, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

### Create visualizations

Create two table [visualizations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm#glossary-1 "Glossary term") in a Qlik Sense [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm#glossary-2 "Glossary term"). Add KeyToOtherTable, Region, Year, Month, and Sales as [dimensions](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm#glossary-3 "Glossary term") to the first table. Add KeyToOtherTable, Region, Year, Month, and Budget as dimensions to the second table.

### Result

RegionSales table

| KeyToOtherTable | Region | Year | Month | Sales |
| --- | --- | --- | --- | --- |
| North|2014|June | North | 2014 | June | 127 |
| North|2014|May | North | 2014 | May | 245 |
| North|2014|May | North | 2014 | May | 347 |
| South|2013|May | South | 2013 | May | 221 |
| South|2013|May | South | 2013 | May | 367 |
| South|2014|June | South | 2014 | June | 645 |

Budget table

| KeyToOtherTable | Region | Year | Month | Budget |
| --- | --- | --- | --- | --- |
| North|2014|June | North | 2014 | June | 150 |
| North|2014|May | North | 2014 | May | 200 |
| North|2014|May | North | 2014 | May | 350 |
| South|2013|May | South | 2013 | May | 200 |
| South|2013|May | South | 2013 | May | 300 |
| South|2014|June | South | 2014 | June | 500 |

### Explanation

The example shows a composite field KeyToOtherTable that links the two tables. AutoNumber is not used. Note the length of the KeyToOtherTable values.

### Add AutoNumber statement

Uncomment the AutoNumber statement in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm#glossary-4 "Glossary term"):

AutoNumber KeyToOtherTable;

### Result

RegionSales table

| KeyToOtherTable | Region | Year | Month | Sales |
| --- | --- | --- | --- | --- |
| 1 | North | 2014 | June | 127 |
| 1 | North | 2014 | May | 245 |
| 2 | North | 2014 | May | 347 |
| 3 | South | 2013 | May | 221 |
| 4 | South | 2013 | May | 367 |
| 4 | South | 2014 | June | 645 |

Budget table

| KeyToOtherTable | Region | Year | Month | Budget |
| --- | --- | --- | --- | --- |
| 1 | North | 2014 | June | 150 |
| 1 | North | 2014 | May | 200 |
| 2 | North | 2014 | May | 350 |
| 3 | South | 2013 | May | 200 |
| 4 | South | 2013 | May | 300 |
| 4 | South | 2014 | June | 500 |

### Explanation

The KeyToOtherTable field values have been replaced with unique integer values and, as a result, the length of the field values has been reduced, thus conserving memory. The key fields in both tables are affected by AutoNumber and the tables remain linked. The example is brief for demonstration purposes, but would be meaningful with a table containing a large number of rows.
