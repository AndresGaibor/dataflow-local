---
title: "Concatenating tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/concatenate-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Logical tables"]
---

# Concatenating tables

Concatenation is an operation that combines two tables into one.

The two tables are merely added to each other. That is, data is not changed and the resulting table contains the same number of records as the two original tables together. Several concatenate operations can be performed sequentially, so that the resulting table is concatenated from more than two tables.

## Automatic concatenation

If the field names and the number of fields of two or more loaded tables are exactly the same, Qlik Sense will automatically concatenate the content of the different statements into one table.

Example:

LOAD a, b, c from table1.csv;

LOAD a, c, b from table2.csv;

The resulting internal table has the fields a, b and c. The number of records is the sum of the numbers of records in table 1 and table 2.

Information noteThe number and names of the fields must be exactly the same. The order of the two statements is arbitrary.

## Forced concatenation

Even if two or more tables do not have exactly the same set of fields, it is still possible to force Qlik Sense to concatenate the two tables. This is done with the concatenate prefix in the script, which concatenates a table with another named table or with the last previously created table.

Example:

LOAD a, b, c from table1.csv;

concatenate LOAD a, c from table2,csv;

The resulting internal table has the fields a, b and c. The number of records in the resulting table is the sum of the numbers of records in table 1 and table 2. The value of field b in the records coming from table 2 is NULL.

Information note Unless a table name of a previously loaded table is specified in the concatenate statement the concatenate prefix uses the most recently created table. The order of the two statements is thus not arbitrary.

## Preventing concatenation

If the field names and the number of fields in two or more loaded tables are exactly the same, Qlik Sense will automatically concatenate the content of the different statements into one table. This is possible to prevent with a noconcatenate statement. The table loaded with the associated LOAD or SELECT statement will then not be concatenated with the existing table.

Example:

LOAD a, b, c from table1.csv;

noconcatenate LOAD a, b, c from table2.csv;

Related learning:

- [What is concatenate?](/lnk/What_is_concatenate)
