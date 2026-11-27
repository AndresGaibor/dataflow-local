---
title: "Add"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Add.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Add

The Add prefix can be added to any LOAD or SELECT statement in the script to specify that it should add records to another table. It also specifies that this statement should be run in a partial reload. The Add prefix can also be used in a Map statement.

Information noteFor partial reload to work properly, the application must be opened with data before a partial reload is triggered.

Perform a partial reload using the Reload button. For more information, see [*Button*](../../Visualizations/Button/button.htm). You can also use the Qlik Engine JSON API.

To perform a partial reload on a schedule, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application and then choose Schedule reload. In the dialog box that opens, turn on Partial reload.

Syntax:

Add [only] [Concatenate[(tablename)]] (loadstatement |
selectstatement)

Add [only] mapstatement

During a normal (non-partial) reload, the Add LOAD construction will work as a normal LOAD statement. Records will be generated and stored in a table.

If the Concatenate prefix is used, or if there exists a table with the same set of fields, the records will be appended to the relevant existing table. Otherwise, the Add LOAD construction will create a new table.

A partial reload will do the same. The only difference is that the Add LOAD construction will never create a new table. There always exists a relevant table from the previous script execution to which the records should be appended.

No check for duplicates is performed. Therefore, a statement using the Add prefix will often include either a distinct qualifier or a where clause guarding duplicates.

The Add Map...Using statement causes mapping to take place also during partial script execution.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| only | An optional qualifier denoting that the statement should be executed only during partial reloads. It should be disregarded during normal (non-partial) reloads. |

Examples and results:

| Example | Result |
| --- | --- |
| Tab1:  LOAD Name, Number FROM Persons.csv;  Add LOAD Name, Number FROM newPersons.csv; | During normal reload, data is loaded from Persons.csv and stored in the Qlik Sense table Tab1. Data from NewPersons.csv is then concatenated to the same Qlik Sense table.  During partial reload, data is loaded from NewPersons.csv and appended to the Qlik Sense table Tab1. No check for duplicates is made. |
| Tab1:  SQL SELECT Name, Number FROM Persons.csv;  Add LOAD Name, Number FROM NewPersons.csv where not exists(Name); | A check for duplicates is made by means of looking if Name exists in the previously loaded table data.  [*Exists Script function*](../InterRecordFunctions/Exists.htm)  During normal reload, data is loaded from Persons.csv and stored in the Qlik Sense table Tab1. Data from NewPersons.csv is then concatenated to the same Qlik Sense table.  During partial reload, data is loaded from NewPersons.csv which is appended to the Qlik Sense table Tab1. A check for duplicates is made by means of seeing if Name exists in the previously loaded table data. |
| Tab1:  LOAD Name, Number FROM Persons.csv;  Add Only LOAD Name, Number FROM NewPersons.csv where not exists(Name); | During normal reload, data is loaded from Persons.csv and stored in the Qlik Sense table Tab1. The statement loading NewPersons.csv is disregarded.  During partial reload, data is loaded from NewPersons.csv which is appended to the Qlik Sense table Tab1. A check for duplicates is made by means of seeing if Name exists in the previously loaded table data.  [*Exists Script function*](../InterRecordFunctions/Exists.htm) |

## Learn more

- [*Partial reload*](PartialReload.htm)
- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Concatenate*](concatenate.htm)
- [*Map*](../ScriptRegularStatements/Map.htm)
- [*Only*](../Only.htm)
