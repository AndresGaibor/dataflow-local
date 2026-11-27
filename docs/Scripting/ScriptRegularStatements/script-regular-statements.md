---
title: "Script regular statements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/script-regular-statements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords"]
---

# Script regular statements

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

[**Alias**](Alias.htm) fieldname as aliasname {,fieldname as aliasname}

Autonumber

This statement creates a unique integer value for each distinct evaluated value in a field encountered during
the script execution.

[**Autonumber**](Autonumber.htm) fields [Using namespace] ]

Binary

The binary statement is used
for loading the data from another QlikView document, including section access data.

[**Binary**](Binary.htm) [[path] filename ]

comment

Provides a way of displaying the field comments (metadata) from databases and spreadsheets. Field names not present in the application will be ignored. If multiple occurrences of a field name are found, the last value is used.

[**comment**](comment.htm) \*fieldlist using mapname

[**comment**](comment.htm) fieldname with comment

comment table

Provides a way of displaying the table comments (metadata) from databases or spreadsheets.

[**comment-table**](comment-table.htm) tablelist using mapname

[**comment-table**](comment-table.htm) tablename with comment

Connect

The CONNECT
statement is used to define access to a data connection.

LIB [**CONNECT**](CONNECT.htm) TO connection

Connection

The Connection script keyword is used as an element within an IncludeModel statement. Connection specifies the location of the source data that is being loaded into the application, from a data product, as a table.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**Connection**](Connection.htm) dataset\_connection

Constrain

The Constrain statement can be used in combination with Let or Set statements for defining script [variables](#glossary-0 "Glossary term"). The Constrain statement allows you to define constraints on possible values for these variables. If a variable definition violates the constraints, the reload fails. With constraints, you can require variable values to match specific types, fall within specific numeric ranges, and match with acceptable values that you define.

[**Constrain**](Constrain.htm) variablename = json

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

[**Directory**](Directory.htm) [path]

Disconnect

The Disconnect statement terminates the current ODBC/OLE DB/Custom connection. This statement is optional.

[**Disconnect**](Disconnect.htm)

drop field

One or several Qlik Sense fields can be dropped from the data model, and thus from memory, at any time
during script execution, by means of a drop
field statement. The "distinct" property of a table is removed after a drop field statement.

Information noteBoth drop field and drop fields are allowed forms with
no difference in effect. If no table is specified, the field will be dropped from all tables where
it occurs.

[**drop-field**](drop-field.htm) fieldname [ , fieldname2 ...] [from tablename1 [ , tablename2 ...]]

drop fields fieldname [ , fieldname2 ...] [from tablename1 [ , tablename2 ...]]

drop table

One or several Qlik Sense internal tables can be dropped from the data model, and thus from memory, at any
time during script execution, by means of a drop
table statement. Optionally, use the drop mapping
table variant to drop mapping tables—those created with the Mapping prefix—before the end of script execution.

Information noteThe forms drop table and drop tables are both accepted.

[Drop [mapping] table](drop-table.htm)
tablename [, tablename2 ...]

drop [mapping] tables[
tablename [, tablename2 ...]

drop variable

Use the Drop variable statement to drop a script variable during script execution. When a variable is dropped, it is not available or visible, for example, in sheet view.

Information note

Both drop variable and drop variables are allowed forms with
no difference in effect.

[Drop variable](Drop-Variable.htm) variablename [ , variablename2 ...]

Drop variables variablename [ , variablename2 ...]

FlushLog

The FlushLog statement forces Qlik Sense to write the content of the script buffer to the script log file.

[**FlushLog**](FlushLog.htm)

Force

The force statement forces Qlik Sense
to interpret field values of subsequent LOAD
and SELECT
statements as written with only upper case letters, with only lower case
letters, as always capitalized or as they appear (mixed). This statement
makes it possible to associate field values from tables made according
to different conventions.

[**Force**](Force.htm) ( capitalization | case upper | case
lower | case mixed )

FromCurrentSpace

The FromCurrentSpace script keyword can be used as an element within an IncludeModel statement. It specifies to load the data product, with its semantic model, from the the same space as the including application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**FromCurrentSpace**](FromCurrentSpace.htm)

FromPersonalSpace

The FromPersonalSpace script keyword can be used as an element within an IncludeModel statement. It specifies to load the data product, with its semantic model, from the user's personal space.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**FromPersonalSpace**](FromPersonalSpace.htm)

FromSpace

The FromSpace script keyword can be used as an element within an IncludeModel statement. It specifies to load the data product, with its semantic model, from a specified space.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**FromSpace**](FromSpace.htm) data\_product\_space

IncludeModel

The IncludeModel statement loads a data product and its semantic model, including tables, relationships, measures, and dimensions. Measures and dimensions from the semantic model automatically appear as master items in the application.

[**IncludeModel**](IncludeModel.htm) data\_product\_name [InEnvironment environment\_name] [FromSpace data\_product\_space | FromCurrentSpace | FromPersonalSpace] [WithTables Table table\_name1  Fields fieldlist Connection dataset\_connection {, Table table\_nameN Fields fieldlist Connection dataset\_connection,... }] [WithMeasures measurelist] [WithDimensions dimensionlist]

InEnvironment

The InEnvironment script keyword is used as an element within an IncludeModel statement.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**InEnvironment**](InEnvironment.htm) environment\_name

LOAD

The LOAD statement loads fields
from a file, from data defined in the script, from a previously
loaded table, from a web page, from the result of a subsequent SELECT
statement or by generating data automatically. It is also possible to load data from analytic connections.

[**Load**](Load.htm) [ distinct
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

[**Let**](Let.htm) variablename=expression

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

[**Map**](Map.htm) \*fieldlist Using 
mapname

NullAsNull

The NullAsNull statement turns
off the conversion of NULL values to string values previously set by a NullAsValue statement.

[**NullAsNull**](NullAsNull.htm) \*fieldlist

NullAsValue

The NullAsValue statement specifies for which fields that NULL should be converted to a value.

[**NullAsValue**](NullAsValue.htm) \*fieldlist

Qualify

The Qualify statement is used for switching on the qualification of field names, i.e. field names will get the table name as a prefix.

[**Qualify**](Qualify.htm) \*fieldlist

Rem

The rem statement is used for
inserting remarks, or comments, into the script, or to temporarily deactivate script
statements without removing them.

[**Rem**](Rem.htm) string

Rename Field

This script function renames one or more existing Qlik Sense field(s) after they have been loaded.

[**rename-field**](rename-field.htm) (using mapname
| oldname to newname{ , oldname to newname })

Rename Fields (using mapname
| oldname to newname{ , oldname to newname })

Rename Table

This script function renames one or more existing Qlik Sense internal table(s) after they have been loaded.

[**rename-table**](rename-table.htm) (using mapname
| oldname to newname{ , oldname to newname })

Rename Tables (using mapname
| oldname to newname{ , oldname to newname })

Section

With the section statement,
it is possible to define whether the subsequent LOAD and SELECT statements should be considered
as data or as a definition of the access rights.

[**Section**](Section.htm) (access | application)

Select

The selection of fields from an ODBC
data source or OLE DB provider is made through standard SQL SELECT statements. However, whether the SELECT statements
are accepted depends on the ODBC driver or OLE DB provider
used.

[**Select**](Select.htm) [all | distinct | distinctrow | top n [percent] ] \*fieldlist

From tablelist

[Where criterion ]

[Group by fieldlist [having criterion ] ]

[Order by fieldlist [asc | desc] ]

[ (Inner | Left | Right | Full)Join tablename on fieldref = fieldref ]

Set

The set statement is used for
defining script variables. These can
be used for substituting strings, paths, drives, and so on.

[**Set**](Set.htm) variablename=string

Sleep

The sleep statement pauses script
execution for a specified time.

[**Sleep**](Sleep.htm) n

SQL

The SQL statement allows you to send an arbitrary SQL command through an
ODBC or OLE DB connection.

[**SQL**](SQL.htm) sql\_command

SQLColumns

The sqlcolumns statement returns
a set of fields describing the columns of an ODBC
or OLE DB data source, to which a connect
has been made.

[**SQLColumns**](SQLColumns.htm)

SQLTables

The sqltables statement returns
a set of fields describing the tables of an ODBC or OLE DB data source, to which a connect
has been made.

[**SQLTables**](SQLTables.htm)

SQLTypes

The sqltypes statement returns
a set of fields describing the types of an ODBC or OLE DB data source, to which a connect
has been made.

[**SQLTypes**](SQLTypes.htm)

Star

The string used for representing the set of all the values of a field
in the database can be set through the star
statement. It affects the subsequent LOAD
and SELECT
statements.

[**Star**](Star.htm) is [
string ]

Store

The Store statement creates a QVD, Parquet, CSV, or TXT file.

[**Store**](Store.htm) [ \*fieldlist from] table into filename [ format-spec ];

Tag

This script statement provides a way to assign tags to one or more fields or tables. If an attempt to tag a field or table not present in the application is made, the tagging will be ignored. If conflicting occurrences of a field or tag name are found, the last value is used.

[**Tag**](Tag.htm)[field|fields] fieldlist with tagname

Tag [field|fields] fieldlist using mapname

Tag table tablelist with tagname

Trace

The trace statement writes a string to the Script
Execution Progress window and to the script log file, when used. It is very useful for debugging purposes. Using $-expansions of variables that are calculated prior to the trace statement, you can customize the message.

[**Trace**](Trace.htm) string

Unmap

The Unmap statement disables field value
mapping specified by a previous Map … Using statement for subsequently loaded fields.

[**Unmap**](Unmap.htm) \*fieldlist

Unqualify

The
Unqualify statement is used for
switching off the qualification of field names that has been previously
switched on by the Qualify statement.

[**Unqualify**](Unqualify.htm) \*fieldlist

Untag

This script statement provides a way to remove tags from fields or tables. If an attempt to untag a field or table not present in the application is made, the untagging will be ignored.

[**Untag**](Untag.htm)[field|fields] fieldlist with tagname

Tag [field|fields] fieldlist using mapname

Tag table tablelist with tagname

WithDimensions

The WithDimensions script keyword is used as an element within an IncludeModel statement. WithDimensions specifies the dimensions from the data product's semantic model to define as master dimensions in the application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**WithDimensions**](WithDimensions.htm) dimensionlist

WithMeasures

The WithMeasures script keyword is used as an element within an IncludeModel statement. WithMeasures specifies the measures from the data product's semantic model to define as master measures in the application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**WithMeasures**](WithMeasures.htm) measurelist

WithTables

The WithTables script keyword is used as an element within an IncludeModel statement. WithTables specifies which tables from the data product to integrate into the data model of the application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

[**WithTables**](WithTables.htm) Table table\_name1  Fields fieldlist Connection dataset\_connection {, Table table\_nameN Fields fieldlist Connection dataset\_connection,... }
