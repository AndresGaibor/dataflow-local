---
title: "Merge"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Merge.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---

# Merge

The Merge prefix can be added to any LOAD or SELECT statement in the script to specify that the loaded table should be merged into another table. It also specifies that this statement should be run in a partial reload.

The typical use case is when you load a change log and want to use this to apply inserts, updates, and deletes to an existing table.

Information noteFor partial reload to work properly, the application must be opened with data before a partial reload is triggered.

Perform a partial reload using the Reload button. For more information, see [*Button*](../../Visualizations/Button/button.htm). You can also use the Qlik Engine JSON API.

To perform a partial reload on a schedule, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application and then choose Schedule reload. In the dialog box that opens, turn on Partial reload.

Syntax:

Merge [only] [(SequenceNoField [, SequenceNoVar])] On ListOfKeys [Concatenate [(TableName)]] (loadstatement | selectstatement)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| only | An optional qualifier denoting that the statement should be executed only during partial reloads. The statement is disregarded during normal (non-partial) reloads. |
| SequenceNoField | The name of the [field](#glossary-0 "Glossary term") containing a timestamp or a sequence number that defines the order of the operations. |
| SequenceNoVar | The name of the [variable](#glossary-1 "Glossary term") that gets assigned the maximum value for SequenceNoField of the table being merged. |
| ListOfKeys | A comma separated list of field names specifying the primary key. |
| Operation | The first field of the load statement must contain the operation as a text string: 'Insert', 'Update', or 'Delete'. ‘i’, ‘u’ and ‘d’ are also accepted. |

## General functionality

During a normal (non-partial) reload, the Merge LOAD construction works as a normal Load statement but with the additional functionality of removing older obsolete records and records marked for deletion. The first field of the Load statement must hold information about the operation: Insert, Update, or Delete.

For each loaded record, the record identifier is compared with previously loaded records, and only the latest record (according to the sequence number) will be kept. If the latest record is marked with Delete, none will be kept.

### Target table

Which table to modify is determined by the set of fields. If a table with the same set of fields (except the first field; the operation) already exists, this will be the relevant table to modify. Alternatively, a Concatenate prefix can be used to specify the table. If the target table is not determined, the result of the Merge LOAD construction is stored in a new table.

If the Concatenate prefix is used, the resulting table has a set of fields corresponding to the union of the existing table and the input to the merge. Hence, the target table may get more fields than the change log that is used as input to the merge.

A partial reload does the same as a full reload. One difference is that a partial reload rarely creates a new table. Unless you have used the Only clause, a target table with the same set of fields from the previous script execution always exists.

### Sequence number

If the loaded change log is an accumulated log, that is, it contains changes that already have been loaded, the parameter SequenceNoVar can be used in a Where clause to limit the amount of input data. The Merge LOAD could then be made to only load records where the field SequenceNoField is greater than SequenceNoVar. Upon completion, the Merge LOAD assigns a new value to the SequenceNoVar with the maximum value seen in the SequenceNoField field.

### Operations

The Merge LOAD can have fewer fields than the target table. The different operations treat missing fields differently:

Insert: Fields missing in the Merge LOAD, but existing in the target table, get a NULL in the target table.

Delete: Missing fields do not affect the result. The relevant records are deleted anyway.

Update: Fields listed in the Merge LOAD are updated in the target table. Missing fields are not changed. This means that the two following statements are not identical:

- Merge on Key Concatenate Load 'U' as Operation, Key, F1, Null() as F2 From ...;
- Merge on Key Concatenate Load 'U' as Operation, Key, F1 From ...;

The first statement updates the listed records and changes F2 to NULL. The second does not change F2, but instead, leaves the values in the target table.

Examples

## Example 1: Simple merge with specified table

In this example, an inline table named Persons is loaded with three rows. Merge then changes the table as follows:

- Adds the row, Mary, 4
   .
- Deletes the row, Steven, 3.
- Assigns the number 5 to Jake
  .

The LastChangeDate variable is set to the maximum value in the ChangeDate column after Merge is executed.

### Load script

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

```
Set DateFormat='D/M/YYYY';
Persons:
load * inline [
Name, Number
Jake, 3
Jill, 2
Steven, 3
];

Merge (ChangeDate, LastChangeDate) on Name Concatenate(Persons)
LOAD * inline [
Operation, ChangeDate,   Name,     Number
Insert,    1/1/2021,     Mary,     4
Delete,    1/1/2021,     Steven,
Update,    2/1/2021,     Jake,     5
];
```

For more information about using inline loads, see [*Using inline loads to load data*](../inline-loads-qs.htm).

### Result

Prior to the Merge Load, the resulting table appears as follows:

Resulting table

| Name | Number |
| --- | --- |
| Jake | 3 |
| Jill | 2 |
| Steven | 3 |

Following the Merge Load, the table appears as follows:

Resulting table

| ChangeDate | Name | Number |
| --- | --- | --- |
| 2/1/2021 | Jake | 5 |
| - | Jill | 2 |
| 1/1/2021 | Mary | 4 |

When the data is loaded, the Data load progress dialog box shows the operations that are performed:

Data load progress dialog box

![Data load progress dialog box.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_data_load_merge.png)

## Example 2: Data load script with missing fields

In this example, the same data as above is loaded, but now with an ID for each person.

Merge changes the table as follows:

- Adds the row, Mary, 4.
- Deletes the row, Steven, 3.
- Assigns the number 5 to Jake.
- Assigns the number 6 to Jill.

### Load script

Here we use two Merge Load statements, one for ‘Insert’ and ‘Delete’, and a second one for the ‘Update’.

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

```
Set DateFormat='D/M/YYYY';
Persons:
Load * Inline [
PersonID, Name, Number
1, Jake, 3
2, Jill, 2
3, Steven, 3
];

Merge (ChangeDate, LastChangeDate) on PersonID Concatenate(Persons)
Load * Inline [
Operation, ChangeDate,   PersonID, Name,     Number
Insert,    1/1/2021,     4,        Mary,     4
Delete,    1/1/2021,     3,        Steven,
];

Merge (ChangeDate, LastChangeDate) on PersonID Concatenate(Persons)
Load * Inline [
Operation, ChangeDate,   PersonID, Number
Update,    2/1/2021,     1,        5
Update,    3/1/2021,     2,        6
];
```

### Result

Following the Merge Load statements, the table appears as follows:

Resulting table

| PersonID | ChangeDate | Name | Number |
| --- | --- | --- | --- |
| 1 | 2/1/2021 | Jake | 5 |
| 2 | 3/1/2021 | Jill | 6 |
| 4 | 1/1/2021 | Mary | 4 |

Note that the second Merge statement does not include the field Name, and as a consequence, the names have not been changed.

## Example 3: Data load script - Partial reload using a Where-clause with ChangeDate

In the following example, the Only argument specifies that the Merge command is only executed during a partial reload. Updates are filtered based on the previously captured LastChangeDate. After Merge is finished, LastChangeDate variable is assigned the maximum value of the ChangeDate column processed during the merge.

### Load script

```
Merge Only (ChangeDate, LastChangeDate) on Name Concatenate(Persons)
LOAD Operation, ChangeDate,  Name, Number
from [lib://ChangeFilesFolder/BulkChangesInPersonsTable.csv] (txt)
where ChangeDate >='$(LastChangeDate)';
```

## Learn more

- [*Partial reload*](PartialReload.htm)
- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Concatenate*](concatenate.htm)
- [*Map*](../ScriptRegularStatements/Map.htm)
- [*Only*](../Only.htm)
