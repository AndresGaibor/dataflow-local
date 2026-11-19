---
title: "Drop table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-table.htm?id=966
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Drop table

One or several Qlik Sense internal tables can be dropped from the data model, and thus from memory, at any
time during script execution, by means of a drop
table statement. Optionally, use the drop mapping
table variant to drop mapping tables—those created with the Mapping prefix—before the end of script execution.

Syntax:

drop [mapping] table  tablename {, tablename2 ...}

drop [mapping] tables tablename {, tablename2 ...}

> **Note:** The forms drop table and drop tables are both accepted.

The following items will be lost as a result of
this:

- The actual table(s).
- All fields which are not part of remaining tables.
- Field values in remaining fields, which came exclusively
  from the dropped table(s).

Examples and results:

| Example | Result |
| --- | --- |
| ``` drop table Orders, Salesmen, T456a; ``` | This line results in three tables being dropped from memory. |
| ``` Tab1: Load * Inline [ Customer, Items, UnitPrice Bob, 5, 1.50 ];   Tab2: LOAD Customer, Sum( Items * UnitPrice ) as Sales resident Tab1 group by Customer;   drop table Tab1; ``` | Once the table Tab2 is created, the table Tab1 is dropped. |
| ``` // Load mapping table of country codes: map1: mapping LOAD *  Inline [ CCode, Country Sw, Sweden Dk, Denmark No, Norway ] ; // Load list of salesmen, mapping country code to country // If the country code is not in the mapping table, put Rest of the world Salespersons: LOAD *,  ApplyMap('map1', CCode,'Rest of the world') As Country  Inline [ CCode, Salesperson  Sw, John Sw, Mary Sw, Per  Dk, Preben Dk, Olle No, Ole  Sf, Risttu] ; // We don't need the CCode anymore Drop Field 'CCode'; 									 Drop Mapping Table map1;  Metrics:  Load * Inline [ Transaction ID, Sales Amount, Sales Cost, City, Customer ID 1000012, 4509.33, 1234.22, Oslo, 250v9849 1000013, 1043.21, 180.23, Gothenburg, 195d5930 1000014, 6038.35, 1400.10, Copenhagen, 195d5930  ]; ``` | This example shows how the Drop mapping table variant can be used. A mapping table map1 is created and then used in a subsequent LOAD statement with the ApplyMap function. After the mapping table has been used, it is dropped from memory, optimizing RAM usage for the data to be loaded in subsequent tables of the script execution.  In this case, with only a few rows in the mapping table, the RAM optimization would be minimal. However, for large mapping tables or when creating mapping tables within loops, performance can be significantly improved. |

## Learn more

- [*Rename table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/rename-table.htm)
- [*Drop field*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-field.htm)
- [*Drop*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop.htm)
- [*Table/Tables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Table.htm)
- [*Mapping*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm)
