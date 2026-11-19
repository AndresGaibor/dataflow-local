---
title: "Partial reload"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/PartialReload.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script prefixes"]
---
Expand/Collapse all

# Partial reload

A full reload always starts by deleting all tables in the existing data model, and then runs the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/PartialReload.htm#glossary-0 "Glossary term").

> **Note:** Partial reloads are not supported with load scripts for scripts. For information on scripts, see [*Working with scripts in the catalog*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/using-the-script-editor.htm).

A partial reload will not do this. Instead it keeps all tables in the data model and then executes only Load and Select statements preceded by an Add, Merge, or Replace prefix. Other data tables are not affected by the command. The only argument denotes that the statement should be executed only during partial reloads, and should be disregarded during full reloads. The following table summarizes statement execution for partial and full reloads.

| Statement | Full reload | Partial reload |
| --- | --- | --- |
| Load ... | Statement will run | Statement will not run |
| Add/Replace/Merge Load ... | Statement will run | Statement will run |
| Add/Replace/Merge Only Load ... | Statement will not run | Statement will run |

Partial reloads have several benefits compared to full reloads:

- Faster, because only data recently changed needs to be loaded. With large data sets the difference is significant.
- Less memory is consumed, because less data is loaded.
- More reliable, because queries to source data run faster, reducing the risk of network problems.

> **Note:** For partial reload to work properly, the application must be opened with data before a partial reload is triggered.

Perform a partial reload using the **Reload** button. For more information, see [*Button*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Button/button.htm). You can also use the Qlik Engine JSON API.

To perform a partial reload on a schedule, click ![More](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application and then choose **Schedule reload**. In the dialog box that opens, turn on **Partial reload**.

## Limitations

A partial reload will fail if there are commands with references to tables that existed during full reload, but not during partial reload.

Example

### Example commands

```
LEFT JOIN(<Table_removed_after_full_reload>)
```

```
CONCATENATE(<Table_removed_after_full_reload>)
```

Where <Table\_removed\_after\_full\_reload> is a table that existed in full reload, but not in partial reload.

### Workaround

As a workaround you can surround the command with following if-statement:

```
IF NOT IsPartialReload() THEN ... ENDIF.
```

A partial reload can remove values from the data. However, this will not be reflected in the list of distinct values, which is a table maintained internally. So, after a partial reload, the list will contain all distinct values that have existed in the [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/PartialReload.htm#glossary-1 "Glossary term") since the last full reload, which may be more than what currently exists after the partial reload.
This affects the output of the FieldValueCount() and the FieldValue() functions. The FieldValueCount() could potentially return a number greater than the current number of field values.

Example

## Example 1

### Load script

Add the example script to your application and do a partial reload. To see the result, add the fields listed in the results column to a [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/PartialReload.htm#glossary-3 "Glossary term") in your application.

```
T1:
Add only Load distinct recno()+10 as Num autogenerate 10;
```

### Result

Resulting table

| Num | Count(Num) |
| --- | --- |
| 11 | 1 |
| 12 | 1 |
| 13 | 1 |
| 14 | 1 |
| 15 | 1 |
| 16 | 1 |
| 17 | 1 |
| 18 | 1 |
| 19 | 1 |
| 20 | 1 |

### Explanation

The statement is only executed during a partial reload. If the "distinct" prefix is omitted, the count of the Num field will increase
with each subsequent partial reload.

## Example 2

### Load script

Add the example script to your application. Do a full reload and view the result. Next, do a partial reload and view the result. To see the results, add the fields listed in the results column to a sheet in your application.

```
T1:
Load recno() as ID, recno() as Value autogenerate 10;

T1:
Replace only Load recno() as ID, repeat(recno(),3) as Value autogenerate 10;
```

### Result

Output table after full reload

| ID | Value |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |

Output table after partial reload

| ID | Value |
| --- | --- |
| 1 | 111 |
| 2 | 222 |
| 3 | 333 |
| 4 | 444 |
| 5 | 555 |
| 6 | 666 |
| 7 | 777 |
| 8 | 888 |
| 9 | 999 |
| 10 | 101010 |

### Explanation

The first table is loaded during a full reload and the second table simply replaces the first table during a partial reload.

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Select*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm)
- [*Add*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Add.htm)
- [*Merge*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Merge.htm)
- [*Replace*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Replace.htm)
