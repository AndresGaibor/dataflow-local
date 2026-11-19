---
title: "Replace"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Replace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes", "Replace"]
---
# Replace

The Replace prefix
can be added to any LOAD or SELECT statement in the script to specify that the loaded table should replace another table. It also specifies that this statement should be run in a partial reload. The Replace prefix can also be used in a Map statement.

> **Note:** For partial reload to work properly, the application must be opened with data before a partial reload is triggered.

Perform a partial reload using the **Reload** button. For more information, see [*Button*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Button/button.htm). You can also use the Qlik Engine JSON API.

To perform a partial reload on a schedule, click ![More](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application and then choose **Schedule reload**. In the dialog box that opens, turn on **Partial reload**.

Syntax:

Replace [only] [Concatenate[(tablename)]] (loadstatement |
selectstatement)

  

Replace [only] mapstatement

During a normal (non-partial) reload, the Replace LOAD construction will work as a normal LOAD statement but be preceded by a Drop Table. First the old table will be dropped, then records will be generated and stored as a new table.

If the Concatenate prefix is used, or if there exists a table with the same set of fields, this will be the relevant table to drop. Otherwise, there is no table to drop and the Replace LOAD construction will be identical to a normal LOAD.

A partial reload will do the same. The only difference is that there is always a table from the previous script execution to drop. The Replace LOAD construction will always first drop the old table, then create a new one.

The Replace Map...Using statement causes mapping to take place also during partial script execution.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| only | An optional qualifier denoting that the statement should be executed only during partial reloads. It should be disregarded during normal (non-partial) reloads. |

Examples and results:

| Example | Result |
| --- | --- |
| Tab1:  Replace LOAD \* from File1.csv; | During both normal and partial reload, the Qlik Sense table Tab1 is initially dropped. Thereafter new data is loaded from File1.csv and stored in Tab1. |
| Tab1:  Replace only LOAD \* from File1.csv; | During normal reload, this statement is disregarded.  During partial reload, any Qlik Sense table previously named Tab1 is initially dropped. Thereafter new data is loaded from File1.csv and stored in Tab1. |
| Tab1:  LOAD a,b,c from File1.csv;  Replace LOAD a,b,c from File2.csv; | During normal reload, the file File1.csv is first read into the Qlik Sense table Tab1, but then immediately dropped and replaced by new data loaded from File2.csv. All data from File1.csv is lost.  During partial reload, the entire Qlik Sense table Tab1 is initially dropped. Thereafter it is replaced by new data loaded from File2.csv. |
| Tab1:  LOAD a,b,c from File1.csv;  Replace only LOAD a,b,c from File2.csv; | During normal reload, data is loaded from File1.csv and stored in the Qlik Sense table Tab1. File2.csv is disregarded.  During partial reload, the entire Qlik Sense table Tab1 is initially dropped. Thereafter it is replaced by new data loaded from File2.csv. All data from File1.csv is lost. |

## Learn more

- [*Partial reload*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/PartialReload.htm)
- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Concatenate*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm)
- [*Map*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Map.htm)
- [*Only*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Only.htm)
