---
title: "Script regular statements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/script-regular-statements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords"]
---
Expand/Collapse all

# Script regular statements

Regular statements are typically used for manipulating data in one way
or another. These statements may be written over any number of lines in
the script and must always
be terminated by a semicolon, ";".

All script keywords can be typed with any combination of lower case and upper case characters. Field and variable names used in the statements are however case sensitive.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Alias

The alias statement is used
for setting an alias according to which a field will be renamed whenever
it occurs in the script that follows.

[**Alias**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Alias.htm) fieldname as aliasname {,fieldname as aliasname}

Autonumber

This statement creates a unique integer value for each distinct evaluated value in a field encountered during
the script execution.

[**Autonumber**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Autonumber.htm) fields [Using namespace] ]

Binary

The binary statement is used
for loading the data from another QlikView document, including section access data.

[**Binary**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Binary.htm) [[path] filename ]

comment

Provides a way of displaying the field comments (metadata) from databases and spreadsheets. Field names not present in the application will be ignored. If multiple occurrences of a field name are found, the last value is used.

[**comment**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment.htm) \*fieldlist using mapname

[**comment**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment.htm) fieldname with comment

comment table

Provides a way of displaying the table comments (metadata) from databases or spreadsheets.

[**comment-table**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment-table.htm) tablelist using mapname

[**comment-table**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/comment-table.htm) tablename with comment

Connect

The CONNECT
statement is used to define access to a data connection.

LIB [**CONNECT**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/CONNECT.htm) TO connection

Constrain

The Constrain statement can be used in combination with Let or Set statements for defining script [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/script-regular-statements.htm#glossary-0 "Glossary term"). The Constrain statement allows you to define constraints on possible values for these variables. If a variable definition violates the constraints, the reload fails. With constraints, you can require variable values to match specific types, fall within specific numeric ranges, and match with acceptable values that you define.

[**Constrain**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Constrain.htm) variablename = json

Declare

The Declare statement is used to create field definitions, where you can define relations between fields or functions. A set of field definitions can be used to automatically generate derived fields, which can be used as dimensions. For example, you can create a calendar definition, and use that to generate related dimensions, such as year, month, week and day, from a date field.

definition\_name:

Declare [Field[s]] Definition [Tagged tag\_list ]

[Parameters parameter\_list ]

Fields field\_list

[Groups group\_list ]

<definition name>:

Declare [Field][s] Definition

Using <existing\_definition>

[With <parameter\_assignment> ]

Derive

The Derive statement is used to generate derived fields based on a field definition created with a Declare statement. You can either specify which data fields to derive fields for, or derive them explicitly or implicitly based on field tags.

Derive [Field[s]] From [Field[s]] field\_list Using definition

Derive [Field[s]] From Explicit [Tag[s]] (tag\_list) Using definition

Derive [Field[s]] From Implicit [Tag[s]] Using definition

Directory

The Directory
statement defines which directory to look in for data files in subsequent LOAD statements,
until a new Directory statement is made.

[**Directory**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Directory.htm) [path]

Disconnect

The Disconnect statement terminates the current ODBC/OLE DB/Custom connection. This statement is optional.

[**Disconnect**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Disconnect.htm)

drop field

One or several Qlik Sense fields can be dropped from the data model, and thus from memory, at any time
during script execution, by means of a drop
field statement. The "distinct" property of a table is removed after a drop field statement.

> **Note:** Both drop field and drop fields are allowed forms with
> no difference in effect. If no table is specified, the field will be dropped from all tables where
> it occurs.

[**drop-field**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-field.htm) fieldname [ , fieldname2 ...] [from tablename1 [ , tablename2 ...]]

drop fields fieldname [ , fieldname2 ...] [from tablename1 [ , tablename2 ...]]

drop table

One or several Qlik Sense internal tables can be dropped from the data model, and thus from memory, at any
time during script execution, by means of a drop
table statement. Optionally, use the drop mapping
table variant to drop mapping tables—those created with the Mapping prefix—before the end of script execution.

> **Note:** The forms drop table and drop tables are both accepted.

[Drop [mapping] table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/drop-table.htm)
tablename [, tablename2 ...]

drop [mapping] tables[
tablename [, tablename2 ...]

drop variable

Use the Drop variable statement to drop a script variable during script execution. When a variable is dropped, it is not available or visible, for example, in sheet view.

> **Note:** Both drop variable and drop variables are allowed forms with
> no difference in effect.

[Drop variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Drop-Variable.htm) variablename [ , variablename2 ...]

Drop variables variablename [ , variablename2 ...]

FlushLog

The FlushLog statement forces Qlik Sense to write the content of the script buffer to the script log file.

[**FlushLog**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/FlushLog.htm)

Force

The force statement forces Qlik Sense
to interpret field values of subsequent LOAD
and SELECT
statements as written with only upper case letters, with only lower case
letters, as always capitalized or as they appear (mixed). This statement
makes it possible to associate field values from tables made according
to different conventions.

[**Force**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Force.htm) ( capitalization | case upper | case
lower | case mixed )

LOAD

The LOAD statement loads fields
from a file, from data defined in the script, from a previously
loaded table, from a web page, from the result of a subsequent SELECT
statement or by generating data automatically. It is also possible to load data from analytic connections.

[**Load**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm) [ distinct
] \*fieldlist

[( from file [ format-spec ] |

from\_field fieldassource [format-spec]

inline data [ format-spec ] |

resident table-label |

autogenerate size )]

[
where criterion | while criterion
]

[
group\_by groupbyfieldlist
]

[order\_by orderbyfieldlist ]

[extension pluginname.functionname(tabledescription)]

Let

The let statement is a complement to the set
statement, used for defining script variables.
The let statement, in opposition
to the set statement, evaluates
the expression on the right side of the ' =' at script run time before it is assigned to
the variable.

[**Let**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Let.htm) variablename=expression

Loosen Table

One or more Qlik Sense internal data tables can be explicitly declared loosely
coupled during script execution by using a Loosen Table statement. When a table is loosely coupled, all associations between field values in the table are removed. A similar effect could be achieved by loading each field of the loosely coupled table as independent, unconnected tables. Loosely coupled can be useful during testing to temporarily isolate different parts of the data structure. A loosely coupled table can be identified in the table viewer by the dotted lines. The use of one or more Loosen Table
statements in the script will make Qlik Sense disregard any setting of tables
as loosely coupled made before the script execution.

tablename [
, tablename2 ...]

Loosen Tables tablename [
, tablename2 ...]

Map ... using

The map ... using statement is
used for mapping a certain field value or expression to the values of
a specific mapping table. The mapping table is created through the Mapping
statement.

[**Map**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Map.htm) \*fieldlist Using 
mapname

NullAsNull

The NullAsNull statement turns
off the conversion of NULL values to string values previously set by a NullAsValue statement.

[**NullAsNull**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/NullAsNull.htm) \*fieldlist

NullAsValue

The NullAsValue statement specifies for which fields that NULL should be converted to a value.

[**NullAsValue**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/NullAsValue.htm) \*fieldlist

Qualify

The Qualify statement is used for switching on the qualification of field names, i.e. field names will get the table name as a prefix.

[**Qualify**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Qualify.htm) \*fieldlist

Rem

The rem statement is used for
inserting remarks, or comments, into the script, or to temporarily deactivate script
statements without removing them.

[**Rem**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Rem.htm) string

Rename Field

This script function renames one or more existing Qlik Sense field(s) after they have been loaded.

[**rename-field**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/rename-field.htm) (using mapname
| oldname to newname{ , oldname to newname })

Rename Fields (using mapname
| oldname to newname{ , oldname to newname })

Rename Table

This script function renames one or more existing Qlik Sense internal table(s) after they have been loaded.

[**rename-table**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/rename-table.htm) (using mapname
| oldname to newname{ , oldname to newname })

Rename Tables (using mapname
| oldname to newname{ , oldname to newname })

Section

With the section statement,
it is possible to define whether the subsequent LOAD and SELECT statements should be considered
as data or as a definition of the access rights.

[**Section**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Section.htm) (access | application)

Select

The selection of fields from an ODBC
data source or OLE DB provider is made through standard SQL SELECT statements. However, whether the SELECT statements
are accepted depends on the ODBC driver or OLE DB provider
used.

[**Select**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm) [all | distinct | distinctrow | top n [percent] ] \*fieldlist

From tablelist

[Where criterion ]

[Group by fieldlist [having criterion ] ]

[Order by fieldlist [asc | desc] ]

[ (Inner | Left | Right | Full)Join tablename on fieldref = fieldref ]

Set

The set statement is used for
defining script variables. These can
be used for substituting strings, paths, drives, and so on.

[**Set**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Set.htm) variablename=string

Sleep

The sleep statement pauses script
execution for a specified time.

[**Sleep**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Sleep.htm) n

SQL

The SQL statement allows you to send an arbitrary SQL command through an
ODBC or OLE DB connection.

[**SQL**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQL.htm) sql\_command

SQLColumns

The sqlcolumns statement returns
a set of fields describing the columns of an ODBC
or OLE DB data source, to which a connect
has been made.

[**SQLColumns**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLColumns.htm)

SQLTables

The sqltables statement returns
a set of fields describing the tables of an ODBC or OLE DB data source, to which a connect
has been made.

[**SQLTables**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLTables.htm)

SQLTypes

The sqltypes statement returns
a set of fields describing the types of an ODBC or OLE DB data source, to which a connect
has been made.

[**SQLTypes**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/SQLTypes.htm)

Star

The string used for representing the set of all the values of a field
in the database can be set through the star
statement. It affects the subsequent LOAD
and SELECT
statements.

[**Star**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Star.htm) is [
string ]

Store

The Store statement creates a QVD, Parquet, CSV, or TXT file.

[**Store**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm) [ \*fieldlist from] table into filename [ format-spec ];

Tag

This script statement provides a way to assign tags to one or more fields or tables. If an attempt to tag a field or table not present in the application is made, the tagging will be ignored. If conflicting occurrences of a field or tag name are found, the last value is used.

[**Tag**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Tag.htm)[field|fields] fieldlist with tagname

Tag [field|fields] fieldlist using mapname

Tag table tablelist with tagname

Trace

The trace statement writes a string to the **Script
Execution Progress** window and to the script log file, when used. It is very useful for debugging purposes. Using $-expansions of variables that are calculated prior to the trace statement, you can customize the message.

[**Trace**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Trace.htm) string

Unmap

The Unmap statement disables field value
mapping specified by a previous Map … Using statement for subsequently loaded fields.

[**Unmap**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Unmap.htm) \*fieldlist

Unqualify

The
Unqualify statement is used for
switching off the qualification of field names that has been previously
switched on by the Qualify statement.

[**Unqualify**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Unqualify.htm) \*fieldlist

Untag

This script statement provides a way to remove tags from fields or tables. If an attempt to untag a field or table not present in the application is made, the untagging will be ignored.

[**Untag**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Untag.htm)[field|fields] fieldlist with tagname

Tag [field|fields] fieldlist using mapname

Tag table tablelist with tagname
