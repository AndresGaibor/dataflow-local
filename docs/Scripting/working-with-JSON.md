---
title: "Working with JSON files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/working-with-JSON.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading data from files"]
---

# Working with JSON files

Load data from JSON files in Qlik Cloud.

You can load data from JSON files just like any other data file supported by Qlik Cloud. For more information, see [*Loading data from files*](../DataSource/load-data-from-files.htm).

You can load data from a JSON file in the [load script](#glossary-0 "Glossary term") with the LOAD command. For example:

LOAD \* from [lib://DataFiles/xyz.json] (json);

For more information, see [*Load*](ScriptRegularStatements/Load.htm).

Load statements can filter or reorder the fields by listing the desired in the field list instead of using the wild card. For example: LOAD a.b, b.c FROM […] (json);. Nonexisting fields will not trigger an error.

## Loading nested objects from JSON

If a value is an object, then the members of that object are used to extend the table with additional fields. Each field name is a combination of the parent and child. For example, the JSON below contains nested objects:

```
[
	{"name":{"first":"Alice","last":"Stephenson"}},
	{"name":{"first":"Bob"}},
	{"name":{"last":"Roberts"}}
]
```

When loaded with LOAD \* FROM [lib://DataFiles/example.json] (json);, it results in the following table of data:

Example nested data table

| name.first | name.last |
| --- | --- |
| Alice | Stephenson |
| Bob | null |
| null | Roberts |

## Loading multiple tables

JSON data with arrays must be loaded using multiple load statements. The content of the array is hashed and used as a key to link the tables.

For example, the JSON below has multiple tables.

```
[
	{"a":[1,2],"b":[3,4]},
	{"a":[2,3],"b":[4,5]}
]
```

This would need to be loaded with the following load statement:

LOAD \* FROM [...] (json);
LOAD \* FROM [...] (json, table is [/\*/a]);
LOAD \* FROM [...] (json, table is [/\*/b]);

The table is specifier is the path to the iterator for the subtable. This results in the following tables of data:

Table 1

| %Key\_a | %Key\_b |
| --- | --- |
| <hash of [1,2]> | <hash of [3,5]> |
| <hash of [2,3]> | <hash of [4,5]> |

Table 2

| %Key\_a | a..@1 |
| --- | --- |
| <hash of [1,2]> | 1 |
| <hash of [1,2]> | 2 |
| <hash of [2,3]> | 2 |
| <hash of [2,3]> | 3 |

Table 3

| %Key\_b | b..@1 |
| --- | --- |
| <hash of [3,5]> | 3 |
| <hash of [3,5]> | 4 |
| <hash of [4,5]> | 4 |
| <hash of [4,5]> | 5 |

Information noteIf your data contains multiple arrays with identical content, use the keyword DISTINCT in the subtable load statements. For example: LOAD DISTINCT \* FROM [lib://DataFiles/Sales.json] (json, all tables);

### Peeking into arrays

The field list can be used when loading data to peek into arrays that otherwise would be loaded as subtables. For example

```
[
	{"pos":[1,2,3]},
	{"pos":[4,5,6]}
]
```

This can be loaded with the following load statement:

LOAD pos.0 AS x, pos.1 AS y, pos.2 AS z FROM […] (json);.

This results in the following table.

| x | y | z |
| --- | --- | --- |
| 1 | 2 | 3 |
| 4 | 5 | 6 |

### Loading all tables

You can make a load of all tables by specifying all tables instead of Table is. For example:

LOAD \* FROM [lib://DataFiles/Sales.json] (json, all tables);

#### Limitations

JSON files have the following limitations:

- A single LOAD statement from a JSON can load a maximum of the following:

  - 5,000 fields
  - 1,000 tables
