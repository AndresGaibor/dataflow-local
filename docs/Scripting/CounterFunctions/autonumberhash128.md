---
title: "autonumberhash128 Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash128.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Counter functions"]
---
# autonumberhash128 Script function

This script function calculates
a 128-bit hash of the combined input expression values and the returns
a unique integer value for each distinct hash value encountered during
the script execution. This function can be used for example for creating a compact
memory representation of a complex key.

> **Note:** You can only connect autonumberhash128 keys that have been generated in the same data load, as the integer is generated according to the order the table is read. If you need to use keys that are persistent between data loads, independent of source data sorting, you should use the hash128, hash160 or hash256 functions.

Syntax:

autonumberhash128(expression
{, expression})

Example: Creating a composite key

In this example we create a composite key using the autonumberhash128 function to conserve memory. The example is brief for demonstration purpose, but would be meaningful with a table containing a large number of rows.

Example data

| Region | Year | Month | Sales |
| --- | --- | --- | --- |
| North | 2014 | May | 245 |
| North | 2014 | May | 347 |
| North | 2014 | June | 127 |
| South | 2014 | June | 645 |
| South | 2013 | May | 367 |
| South | 2013 | May | 221 |

The source data is loaded using inline data. Then we add a [preceding load](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash128.htm#glossary-0 "Glossary term"), which creates a composite key from the Region, Year and Month fields.

RegionSales:
LOAD \*,
AutoNumberHash128(Region, Year, Month) as RYMkey;
LOAD \* INLINE
[ Region, Year, Month, Sales
North, 2014, May, 245
North, 2014, May, 347
North, 2014, June, 127
South, 2014, June, 645
South, 2013, May, 367
South, 2013, May, 221
];

The resulting table looks like this:

Results table

| Region | Year | Month | Sales | RYMkey |
| --- | --- | --- | --- | --- |
| North | 2014 | May | 245 | 1 |
| North | 2014 | May | 347 | 1 |
| North | 2014 | June | 127 | 2 |
| South | 2014 | June | 645 | 3 |
| South | 2013 | May | 367 | 4 |
| South | 2013 | May | 221 | 4 |

In this example you can refer to the RYMkey, for example 1, instead of the string 'North2014May' if you need to link to another table.

Now we load a source table of costs in a similar way. The Region, Year and Month fields are excluded in the preceding load to avoid creating a [synthetic key](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash128.htm#glossary-1 "Glossary term"), we are already creating a composite key with the autonumberhash128 function, linking the tables.

RegionCosts:
LOAD Costs,
AutoNumberHash128(Region, Year, Month) as RYMkey;
LOAD \* INLINE
[ Region, Year, Month, Costs
South, 2013, May, 167
North, 2014, May, 56
North, 2014, June, 199
South, 2014, June, 64
South, 2013, May, 172
South, 2013, May, 126
];

Now we can add a table [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash128.htm#glossary-2 "Glossary term") to a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash128.htm#glossary-3 "Glossary term"), and add the Region, Year and Month fields, as well as Sum [measures](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash128.htm#glossary-4 "Glossary term") for the sales and the costs. The table will look like this:

Results table

| Region | Year | Month | Sum([Sales]) | Sum([Costs]) |
| --- | --- | --- | --- | --- |
| Totals | - | - | 1952 | 784 |
| North | 2014 | June | 127 | 199 |
| North | 2014 | May | 592 | 56 |
| South | 2014 | June | 645 | 64 |
| South | 2013 | May | 588 | 465 |

## Learn more

- [*autonumberhash256 Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumberhash256.htm)
- [*autonumber Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/autonumber.htm)
