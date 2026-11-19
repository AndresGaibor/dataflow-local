---
title: "Script prefixes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/script-prefixes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords"]
---
Expand/Collapse all

# Script prefixes

Prefixes may be applied to applicable regular statements but never to control statements. The when and unless prefixes can however be used as suffixes to a few specific control statement clauses.

All script keywords can be typed with any combination of lower case and upper case characters. Field and variable names used in the statements are however case sensitive.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Add

The Add prefix can be added to any LOAD or SELECT statement in the script to specify that it should add records to another table. It also specifies that this statement should be run in a partial reload. The Add prefix can also be used in a Map statement.

[**Add**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Add.htm) [only] [Concatenate[(tablename )]] (loadstatement |
selectstatement)

[**Add**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Add.htm) [ Only ] mapstatement

Concatenate

If two tables that are to be concatenated
have different sets of fields, concatenation of
two tables can still be forced with the Concatenate
prefix.

[**concatenate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/concatenate.htm)[ (tablename ) ] ( loadstatement |
selectstatement )

Crosstable

The crosstable load
prefix is used to transpose “cross table” or “pivot table” structured data. Data structured this way is commonly encountered when working with spreadsheet sources. The output and aim of the crosstable load
prefix is to transpose such structures into a regular column-oriented table equivalent, as this structure is generally better suited for analysis in Qlik Sense.

[**crosstable**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/crosstable.htm) (attribute field name, data field name [ , n ] ) ( loadstatement |
selectstatement )

First

The First prefix to a LOAD or SELECT (SQL) statement is used for loading
a set maximum number of records from a data source table.

[**First**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/First.htm) n(
loadstatement | selectstatement
)

Generic

The Generic load prefix allows for conversion of entity–attribute–value modeled data (EAV) into a traditional, normalized relational table structure. EAV modeling is alternatively referred to as "generic data modeling" or "open schema".

[**Generic**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Generic.htm) ( loadstatement | selectstatement
)

Hierarchy

The hierarchy
prefix is used to transform a parent-child hierarchy table to a table that is useful in a Qlik Sense data model. It can be put in front of a LOAD
or a SELECT
statement and will use the result of the loading statement as input for a table transformation.

[**Hierarchy**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Hierarchy.htm) (NodeID,
ParentID, NodeName,
[ParentName], [PathSource],
[PathName], [PathDelimiter],
[Depth])(loadstatement | selectstatement)

HierarchBelongsTo

This prefix is used to transform a parent-child hierarchy table to a table that is useful in a Qlik Sense data model. It can be put in front of a LOAD or a SELECT statement and will use the result of the loading statement as input for a table transformation.

[**HierarchyBelongsTo**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/HierarchyBelongsTo.htm) (NodeID, ParentID,
NodeName, AncestorID,
AncestorName, [DepthDiff])(loadstatement
| selectstatement)

Inner

The join and keep prefixes can be preceded by the prefix inner.

If used before join it specifies
that an inner join should be used. The resulting table will thus only
contain combinations of field values from the raw data tables where the linking field values are represented in both tables. If used before keep, it specifies
that both raw data tables should be reduced to their common intersection
before being stored in Qlik Sense.

.

[**Inner**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Inner.htm) ( Join | Keep)
[ (tablename) ](loadstatement |selectstatement )

IntervalMatch

The IntervalMatch prefix is used to create a table matching discrete numeric values to one or more numeric intervals, and optionally matching the values of one or several additional keys.

[**IntervalMatch**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/IntervalMatch.htm) (matchfield)(loadstatement | selectstatement )

IntervalMatch (matchfield,keyfield1
[ , keyfield2,
... keyfield5 ] ) (loadstatement
| selectstatement )

Join

The join prefix joins the loaded
table with an existing named table or the last previously created data table.

[Inner | Outer | Left | Right ] [**Join**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Join.htm) [ (tablename )
]( loadstatement | selectstatement )

Keep

The keep prefix is similar to the join prefix. Just as the join prefix, it compares the loaded table with an existing named table or the last previously created data table, but instead of joining the loaded table with an existing table, it has the effect of reducing one or both of the two tables before they are stored in Qlik Sense, based on the intersection of table data. The comparison made is equivalent to a natural join made over all the common fields, i.e. the same way as in a corresponding join. However, the two tables are not joined and will be kept in Qlik Sense as two separately named tables.

(Inner | Left | Right) [**Keep**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Keep.htm) [(tablename ) ]( loadstatement | selectstatement )

Left

The Join
and Keep
prefixes can be preceded by the prefix left.

If used before join it specifies
that a left join should be used. The resulting table will only contain
combinations of field values from the raw data tables where the linking field values are represented in the first table. If used before keep, it specifies
that the second raw data table should be reduced to its common intersection
with the first table, before being stored in Qlik Sense.

[**Left**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Left.htm) ( Join | Keep)
[ (tablename) ](loadstatement |selectstatement )

Mapping

The mapping prefix is used to create a mapping table that can be used to, for example, replace field values and field names during script execution.

[**Mapping**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm) (
loadstatement | selectstatement
)

Merge

The Merge prefix can be added to any LOAD or SELECT statement in the script to specify that the loaded table should be merged into another table. It also specifies that this statement should be run in a partial reload.

[**Merge**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Merge.htm) [only] [(SequenceNoField [, SequenceNoVar])] On ListOfKeys [Concatenate [(TableName)]] (loadstatement | selectstatement)

NoConcatenate

The NoConcatenate prefix forces
two loaded tables with identical field sets
to be treated as two separate internal tables, when they would otherwise be automatically concatenated.

[**NoConcatenate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/NoConcatenate.htm)(
loadstatement |
selectstatement )

Outer

The explicit Join
prefix can be preceded by the prefix Outer to specify an outer join. In an outer join, all combinations between
the two tables are generated. The resulting table will thus contain combinations of field values from the raw data tables where the linking field values are represented in one or both tables. The Outer keyword is optional and is the default join type used when a join prefix is not specified.

[**Outer**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Outer.htm) Join
[ (tablename) ](loadstatement
|selectstatement )

Partial reload

A full reload always starts by deleting all tables in the existing data model, and then runs the load script.

A [*Partial reload*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/PartialReload.htm) will not do this. Instead it keeps all tables in the data model and then executes only Load and Select statements preceded by an Add, Merge, or Replace prefix. Other data tables are not affected by the command. The only argument denotes that the statement should be executed only during partial reloads, and should be disregarded during full reloads. The following table summarizes statement execution for partial and full reloads.

Replace

The Replace prefix
can be added to any LOAD or SELECT statement in the script to specify that the loaded table should replace another table. It also specifies that this statement should be run in a partial reload. The Replace prefix can also be used in a Map statement.

[**Replace**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Replace.htm) [only] [Concatenate[(tablename) ]] (loadstatement |
selectstatement)

[**Replace**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Replace.htm) [only] mapstatement

Right

The Join
and Keep
prefixes can be preceded by the prefix right.

If used before join it specifies
that a right join should be used. The resulting table will only contain
combinations of field values from the raw data tables where the linking field values are represented in the second table. If used before keep, it specifies
that the first raw data table should be reduced to its common intersection
with the second table, before being stored in Qlik Sense.

[**Right**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Right.htm) (Join | Keep) [(tablename)](loadstatement
|selectstatement )

Sample

The sample prefix to a LOAD or SELECT statement is used for loading
a random sample of records from the data source.

[**Sample**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Sample.htm) p
( loadstatement | selectstatement
)

Semantic

Tables containing relations between records can be loaded through a
semantic prefix. This can for example be self-references within a table, where one record points to another, such as parent, belongs to, or predecessor.

[**Semantic**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Semantic.htm) ( loadstatement
| selectstatement)

Unless

The unless prefix and suffix
is used for creating a conditional clause which determines whether a statement
or exit clause should be evaluated or not. It may be seen as a compact
alternative to the full if..end if
statement.

([**Unless**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Unless.htm) condition
statement | exitstatement Unless condition )

When

The when prefix and suffix is
used for creating a conditional clause which determines whether a statement
or exit clause should be executed or not. It may be seen as a compact
alternative to the full if..end if
statement.

( [**When**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/When.htm) condition
statement | exitstatement when condition )
