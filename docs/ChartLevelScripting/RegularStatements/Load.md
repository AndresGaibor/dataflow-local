---
title: "Load"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/RegularStatements/Load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Regular statements"]
---

# Load

In a [chart](#glossary-0 "Glossary term") modifying context, the LOAD statement loads additional data to the hypercube from data defined in the script, or from a previously
loaded table. It is also possible to load data from analytic connections.

Information noteThe LOAD statement must have either Replace or Add prefix, or it will be rejected.

Syntax:

Add | Replace LOAD fieldlist

(

inline data [ format-spec ] |

resident table-label

) | extension pluginname.functionname([script] tabledescription)]

[
where criterion | while criterion
]

[
group by groupbyfieldlist
]

[order by orderbyfieldlist ]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| fieldlist | fieldlist ::= ( \* | field{, \* | field } )  A list of the fields to be loaded. Using \* as a field list indicates all fields in the table. field ::= ( fieldref | expression ) [as aliasname ] The field definition must always contain a literal, a reference to an existing field, or an expression. fieldref ::= ( fieldname |@fieldnumber  |@startpos:endpos [ I | U | R | B | T] ) fieldname is a text that is identical to a field name in the table. Note that the field name must be enclosed by straight double quotation marks or square brackets if it contains e.g. spaces. Sometimes field names are not explicitly available. Then a different notation is used:  @fieldnumber represents the field number in a delimited table file. It must be a positive integer preceded by "@". The numbering is always made from 1 and up to the number of fields.  @startpos:endpos represents the start and end positions of a field in a file with fixed length records. The positions must both be positive integers. The two numbers must be preceded by "@" and separated by a colon. The numbering is always made from 1 and up to the number of positions. In the last field, n is used as end position.   - If   @startpos:endpos   is immediately followed by the characters I or   U, the bytes read will be interpreted as a binary   signed (I) or unsigned (U)   integer (Intel byte order). The number of positions read must be 1, 2   or 4. - If @startpos:endpos is   immediately followed by the character R, the bytes   read will be interpreted as a binary real number (IEEE 32-bit or 64 bit   floating point). The number of positions read must be 4 or 8. - If @startpos:endpos is immediately followed   by the character B, the bytes read will be interpreted   as a BCD (Binary Coded Decimal) numbers according to the COMP-3 standard.   Any number of bytes may be specified.   expression can be a numeric function or a string function based on one or several other fields in the same table. For further information, see the syntax of expressions.  as is used for assigning a new name to the field. |
| inline | inline is used if data should be typed within the script, and not loaded from a file. data ::= [ text ]  Data entered through an inline clause must be enclosed by double quotation marks or by square brackets. The text between these is interpreted in the same way as the content of a file. Hence, where you would insert a new line in a text file, you should also do it in the text of an inline clause, i.e. by pressing the Enter key when typing the script. The number of columns are defined by the first line. format-spec ::= ( fspec-item {, fspec-item } ) The format specification consists of a list of several format specification items, within brackets. For more information, see [*Format specification items*](../../Scripting/ScriptSpecifiers/format-specification-items.htm). |
| resident | resident is used if data should be loaded from a previously loaded table. table label is a label preceding the LOAD statement that created the original table. The label should be given with a colon at the end.  [*Loading data from a previously loaded table*](../../Scripting/load-data-from-previously-loaded-table.htm)  [*Table labels*](../../Scripting/table-labels.htm) |
| extension | You can load data from analytic connections. You need to use the extension clause to call a function defined in the server-side extension (SSE) plugin, or evaluate a script.  You can send a single table to the SSE plugin, and a single data table is returned. If the plugin does not specify the names of the fields that are returned, the fields will be named Field1, Field2, and so on.  Extension pluginname.functionname( tabledescription );   - Loading data using a function in an SSE plugin  tabledescription ::= (table { ,tablefield} )  If you do not state table fields, the fields will be used in load order. - Loading data by evaluating a script in an SSE plugin  tabledescription ::= ( script, table { ,tablefield} )   Data type handling in the table field definition  Data types are automatically detected in analytic connections. If the data has no numeric values and at least one non-NULL text string, the field is considered as text. In any other case it is considered as numeric.  You can force the data type by wrapping a field name with String() or Mixed().   - String() forces the field to be text. If the field is numeric, the text part of the dual value is extracted, there is no conversion performed. - Mixed() forces the field to be dual.   String() or Mixed() cannot be used outside extension table field definitions, and you cannot use other Qlik Sense functions in a table field definition.  You can read more about analytic connections in the GitHub repository. [qlik-oss/server-side-extension](https://github.com/qlik-oss/server-side-extension) |
| where | where is a clause used for stating whether a record should be included in the selection or not. The selection is included if criterion is True. criterion is a logical expression. |
| while | while is a clause used for stating whether a record should be repeatedly read. The same record is read as long as criterion is True. In order to be useful, a while clause must typically include the IterNo( ) function.  criterion is a logical expression. |
| group by | group by is a clause used for defining over which fields the data should be aggregated (grouped). The [aggregation](#glossary-1 "Glossary term")fields should be included in some way in the expressions loaded. No other fields than the aggregation fields may be used outside aggregation functions in the loaded expressions.  groupbyfieldlist ::= (fieldname { ,fieldname } ) |
| order by | order by is a clause used for sorting the records of a resident table before they are processed by the load statement. The resident table can be sorted by one or more fields in ascending or descending order. The sorting is made primarily by numeric value and secondarily by national collation order. This clause may only be used when the data source is a resident table. The ordering fields specify which field the resident table is sorted by. The field can be specified by its name or by its number in the resident table (the first field is number 1).  orderbyfieldlist ::= fieldname [ sortorder ] { , fieldname [ sortorder ] }  sortorder is either asc for ascending or desc for descending. If no sortorder is specified, asc is assumed.  fieldname, path, filename and aliasname are text strings representing what the respective names imply. Any field in the source table can be used as fieldname. However, fields created through the as clause (aliasname) are out of scope and cannot be used inside the same load statement. |

## Learn more

- [*Add*](../Prefixes/Add.htm)
- [*Replace*](../Prefixes/Replace.htm)
