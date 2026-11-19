---
title: "Load"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#distinct?id=972
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
Expand/Collapse all

# Load

The LOAD statement loads fields
from a file, from data defined in the script, from a previously
loaded table, from a web page, from the result of a subsequent SELECT
statement or by generating data automatically. It is also possible to load data from analytic connections.

Syntax:

LOAD [ distinct ] fieldlist

[( from file [ format-spec ] |

from\_field fieldassource [format-spec]|

inline data [ format-spec ] |

resident table-label |

autogenerate size ) |extension pluginname.functionname([script] tabledescription)]

[
where criterion | while criterion
]

[
group by groupbyfieldlist
]

[order by orderbyfieldlist ]

Arguments

| Argument | Description |
| --- | --- |
| distinct | You can use distinct as a predicate if you only want to load unique records. If there are duplicate records, the first instance will be loaded.  If you are using preceding loads, you need to place distinct in the first load statement, as distinct only affects the destination table.  [*Preceding load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm#Precedin) |
| fieldlist | fieldlist ::= ( \* | field{, \* | field } )  A list of the [fields](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-0 "Glossary term") to be loaded. Using \* as a field list indicates all fields in the table. field ::= ( fieldref | expression ) [as aliasname ] The field definition must always contain a literal, a reference to an existing field, or an expression. fieldref ::= ( fieldname |@fieldnumber  |@startpos:endpos [ I | U | R | B | T] ) fieldname is a text that is identical to a field name in the table. Note that the field name must be enclosed by straight double quotation marks or square brackets if it contains e.g. spaces. Sometimes field names are not explicitly available. Then a different notation is used:  @fieldnumber represents the field number in a delimited table file. It must be a positive integer preceded by "@". The numbering is always made from 1 and up to the number of fields.  @startpos:endpos represents the start and end positions of a field in a file with fixed length records. The positions must both be positive integers. The two numbers must be preceded by "@" and separated by a colon. The numbering is always made from 1 and up to the number of positions. In the last field, n is used as end position.   - If   @startpos:endpos   is immediately followed by the characters I or   U, the bytes read will be interpreted as a binary   signed (I) or unsigned (U)   integer (Intel byte order). The number of positions read must be 1, 2   or 4. - If @startpos:endpos is   immediately followed by the character R, the bytes   read will be interpreted as a binary real number (IEEE 32-bit or 64 bit   floating point). The number of positions read must be 4 or 8. - If @startpos:endpos is immediately followed   by the character B, the bytes read will be interpreted   as a BCD (Binary Coded Decimal) numbers according to the COMP-3 standard.   Any number of bytes may be specified.   expression can be a numeric function or a string function based on one or several other fields in the same table. For further information, see the syntax of expressions.  as is used for assigning a new name to the field. |
| from | from is used if data should be loaded from a file using a folder. When loading from a file in space in Qlik Cloud Analytics, a valid path must be used. See [*Rules for valid space folder paths*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules).  file ::= [ path ] filename  In Qlik Cloud Analytics, hierarchical folder structures are supported and can be referenced in the statement.  Examples:   - Personal space (top-level path): [lib://DataFiles/abc.qvd] - Personal space (nested folder): [lib://DataFiles/MyFolder/abc.qvd] - Shared space (top-level path): [lib://TeamSharedSpace:DataFiles/xyz.qvd] - Shared space (nested folder): [lib://TeamSharedSpace:DataFiles/MyFolder/abc.qvd]   For more information and examples, see [*Loading files from spaces in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#SpaceStore). |
| from\_field | from\_field is used if data should be loaded from a previously loaded field. fieldassource::=(tablename, fieldname)  The field is the name of the previously loaded tablename and fieldname. format-spec ::= ( fspec-item {, fspec-item } ) The format specification consists of a list of several format specification items, within brackets. For more information, see [*Format specification items*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/format-specification-items.htm).  **Note:** from\_field only supports commas as the list delimiter in when separating fields in tables. |
| inline | inline is used if data should be typed within the script, and not loaded from a file. data ::= [ text ]  Data entered through an inline clause must be enclosed by specific characters – square brackets, quotation marks, or back ticks. The text between these is interpreted in the same way as the content of a file. Hence, where you would insert a new line in a text file, you should also do it in the text of an inline clause: by pressing the Enter key when typing the script.  In a simple inline load, the number of columns are defined by the first line. format-spec ::= ( fspec-item {, fspec-item } ) You can customize the inline load with many of the same format specification items that are available for other loaded tables. These items are listed in brackets. For more information, see [*Format specification items*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/format-specification-items.htm).  For more information about inline loads, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm). |
| resident | resident is used if data should be loaded from a previously loaded table. table label is a label preceding the LOAD or SELECT statement(s) that created the original table. The label should be given with a colon at the end.  [*Loading data from a previously loaded table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm)  [*Table labels*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/table-labels.htm) |
| autogenerate | autogenerate is used if data should be automatically generated by Qlik Sense. size ::= number  Number is an integer indicating the number of records to be generated.  The field list must not contain expressions which require data from an external data source or a previously loaded table, unless you refer to a single field value in a previously loaded table with the Peek function. |
| where | where is a clause used for stating whether a record should be included in the selection or not. The selection is included if criterion is True. criterion is a logical expression. |
| while | while is a clause used for stating whether a record should be repeatedly read. The same record is read as long as criterion is True. In order to be useful, a while clause must typically include the IterNo( ) function.  criterion is a logical expression. |
| group by | group by is a clause used for defining over which fields the data should be aggregated (grouped). The aggregation fields should be included in some way in the expressions loaded. No other fields than the aggregation fields may be used outside aggregation functions in the loaded expressions.  groupbyfieldlist ::= (fieldname { ,fieldname } ) |
| order by | order by is a clause used for sorting the records of a resident table before they are processed by the load statement. The resident table can be sorted by one or more fields in ascending or descending order. The sorting is made primarily by numeric value and secondarily by national collation order. This clause may only be used when the data source is a resident table. The ordering fields specify which field the resident table is sorted by. The field can be specified by its name or by its number in the resident table (the first field is number 1).  orderbyfieldlist ::= fieldname [ sortorder ] { , fieldname [ sortorder ] }  sortorder is either asc for ascending or desc for descending. If no sortorder is specified, asc is assumed.  fieldname, path, filename and aliasname are text strings representing what the respective names imply. Any field in the source table can be used as fieldname. However, fields created through the as clause (aliasname) are out of scope and cannot be used inside the same load statement. |

If no source of data is given by means
of a from, inline, resident, from\_field, extension or autogenerate clause, data will be loaded
from the result of the immediately succeeding SELECT or LOAD statement. The succeeding statement should not have a prefix.

[*Loading data from a previously loaded table*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm)

> **Note:** The file extension of DataFiles connections is case sensitive. For example: .qvd.

Examples:

Selecting
certain fields, renaming and calculating fields 

Load only three specific fields from a delimited file:

LOAD FirstName, LastName, Number from [lib://DataFiles/data1.csv];

Rename first field as A and second field as B when loading a file without labels:

LOAD @1 as A, @2 as B from [lib://DataFiles/data3.txt] (ansi,
txt, delimiter is '\t', no labels);

Load Name as a concatenation of FirstName, a space character, and LastName:

LOAD FirstName&' '&LastName as Name
from [lib://DataFiles/data1.csv];

Load Quantity, Price and Value (the product of Quantity and Price):

LOAD Quantity, Price, Quantity\*Price as Value
from [lib://DataFiles/data1.csv];

Selecting
certain records

Load only unique records, duplicate records will be discarded:

LOAD distinct FirstName, LastName, Number from [lib://DataFiles/data1.csv];

Load only records where the field Litres has a value above zero:

LOAD \* from [lib://DataFiles/Consumption.csv] where Litres>0;

Loading
data not on file and auto-generated data

Load a table with inline data, two fields named CatID and Category:

LOAD \* Inline

[CatID, Category

0,Regular

1,Occasional

2,Permanent];

Load a table with inline data, three fields named UserID, Password and Access:

LOAD \* Inline [UserID, Password, Access

A, ABC456, User

B, VIP789, Admin];

Load a table with 10 000 rows. Field A will contain the number of the read record (1,2,3,4,5...) and field B will contain a random number between 0 and 1:

LOAD RecNo( ) as A, rand( ) as B autogenerate(10000);

> **Note:** The parenthesis after autogenerate is allowed but not required.

Loading
data from a previously loaded table

First we load a delimited table file and name it tab1:

tab1:

SELECT A,B,C,D from [lib://DataFiles/data1.csv];

Load fields from the already loaded tab1 table as tab2:

tab2:

LOAD A,B,month(C),A\*B+D as E resident tab1;

Load fields from already loaded table tab1 but only records where A is larger than B:

tab3:

LOAD A,A+B+C resident tab1 where A>B;

Load fields from already loaded table tab1 ordered by A:

LOAD A,B\*C as E resident tab1 order by A;

Load fields from already loaded table tab1, ordered by the first field, then the second field:

LOAD A,B\*C as E resident tab1 order by 1,2;

Load fields from already loaded table tab1 ordered by C descending,
then B in ascending order, and then the first field in descending order:

LOAD A,B\*C as E resident
tab1 order by C desc, B asc, 1 desc;

Loading data from previously loaded fields

Load field Types from previously loaded table Characters as A:

LOAD A from\_field (Characters,
Types);

Loading
data from a succeeding table (preceding load)

Load A, B and calculated fields X and Y from Table1 that is loaded in succeeding SELECT statement:

LOAD A, B, if(C>0,'positive','negative')
as X, weekday(D) as Y;

SELECT A,B,C,D from Table1;

Grouping
data

Load fields grouped (aggregated) by ArtNo:

LOAD ArtNo, round(Sum(TransAmount),0.05) as
ArtNoTotal from table.csv group by ArtNo;

Load fields grouped (aggregated) by Week and ArtNo:

LOAD Week, ArtNo, round(Avg(TransAmount),0.05)
as WeekArtNoAverages from table.csv group by Week, ArtNo;

Reading one record
repeatedly

In this example we have a input file Grades.csv containing the grades for each student condensed in one field:

Student,Grades

Mike,5234

John,3345

Pete,1234

Paul,3352

The grades, in a 1-5 scale, represent subjects Math, English, Science and History. We can separate the grades into separate values by reading each record several times with a while clause, using the IterNo( ) function as a counter. In each read, the grade is extracted with the Mid function and stored in Grade, and the subject is selected using the pick function and stored in Subject. The final while clause contains the test to check if all grades have been read (four per student in this case), which means next student record should be read.

MyTab:

LOAD
Student,

mid(Grades,IterNo(
),1) as Grade,

pick(IterNo(
), 'Math', 'English', 'Science', 'History') as Subject from [lib://DataFiles/Grades.csv]

while IsNum(mid(Grades,IterNo(),1));

The result is a table containing this data:

![Resulting data table](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_LoadRepeated.png)

Loading from analytic connections

The following sample data is used.

Values:
Load
Rand() as A,
Rand() as B,
Rand() as C
AutoGenerate(50);

Loading data using a function

In these examples, we assume that we have an analytic connection plugin named P that contains a custom function Calculate(Parameter1, Parameter2). The function returns the table Results that contains the fields Field1 and Field2.

Load \* Extension P.Calculate( Values{A, C} );

Load all fields that are returned when sending the fields A and C to the function.

Load Field1 Extension P.Calculate( Values{A, C} );

Load only the Field1 field when sending the fields A and C to the function.

Load \* Extension P.Calculate( Values );

Load all fields that are returned when sending the fields A and B to the function. As fields are not specified, A and B are used as they are the first in order in the table.

Load \* Extension P.Calculate( Values {C, C});

Load all fields that are returned when sending the field C to both parameters of the function.

Load \* Extension P.Calculate( Values {String(A), Mixed(B)});

Load all fields that are returned when sending the field A forced as a string and B forced as a numeric to the function.

Loading data by evaluating a script

Load A as A\_echo, B as B\_echo Extension R.ScriptEval( 'q;', Values{A, B} );

Load the table returned by the script q when sending the values of A and B.

Load \* Extension R.ScriptEval( '$(My\_R\_Script)', Values{A, B} );

Load the table returned by the script stored in the My\_R\_Script variable when sending the values of A and B.

Load \* Extension R.ScriptEval( '$(My\_R\_Script)', Values{B as D, \*} );

Load the table returned by the script stored in the My\_R\_Script variable when sending the values of B renamed to D, A and C. Using \* sends the remaining unreferenced fields.

## Loading files from spaces in Qlik Cloud Analytics

In Qlik Cloud Analytics, when loading data from a data file within a load script, you can use a LOAD statement or insert QVS code. In both cases, hierarchical space folder structures can be referenced in your script statement. Follow the rules for [valid space folder paths](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules). Additionally, the file and all referenced folders need to already exist in the specified location. Otherwise, the reload fails.

Examples: Reference to file at the top-level path of a space

This example loads the file orders.csv from a personal space. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
LOAD * FROM [lib://DataFiles/orders.csv];
```

This example loads the file orders.csv from a [shared](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-1 "Glossary term"), [managed](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-2 "Glossary term"), or [data space](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-3 "Glossary term"). The name of the space is TeamSharedSpace. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
LOAD * FROM [lib://TeamSharedSpace:DataFiles/orders.csv];
```

Examples: References to specific folder path within a space

This example loads the file orders\_Europe.csv from the folder Orders By Region within a personal space.

```
LOAD * FROM [lib://DataFiles/Orders By Region/orders_Europe.csv];
```

This example loads the file orders\_Europe.csv from the folder Orders By Region within a [shared](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-4 "Glossary term"), [managed](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-5 "Glossary term"), or [data space](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm#glossary-6 "Glossary term"). The name of the space is SalesSpace.

```
LOAD * FROM [lib://SalesSpace:DataFiles/Orders By Region/orders_Europe.csv];
```

For more information about referencing space folder structure in load scripts, see [*Referencing space folder structure in application and script development*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#FolderStructureRefExamples).
