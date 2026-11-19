---
title: "Store"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Store

The Store statement creates a QVD, Parquet, CSV, or TXT file.

Syntax:

Store [ fieldlist from] table into filename [ format-spec ];

The statement will create an explicitly named [QVD](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm#glossary-0 "Glossary term"), Parquet, or text file.

The statement can only export fields from one data
table, unless you are storing to Parquet. If fields from several tables are to be exported into a QVD, CSV, or TXT file, an explicit join must be made previously in the script to create the data table that should be exported. You can store multiple tables in a single Parquet by nesting the data in the Parquet files.

The text values are exported to the CSV file in UTF-8 with BOM format. A
delimiter can be specified, see LOAD. The store statement to a CSV file does not support BIFF
export.

> **Note:** In some cases with data that is not well-formed, fields will be surrounded by double quotes to ensure that the data is interpreted correctly. This can happen, for example, when the field contains characters such as quotes, comma, space or line breaks.

You can specify whether to store your file in your personal space or a shared space where you have write permissions. If you store in a shared space, members can use that data to create applications in the space. See: [*Managing permissions in shared spaces*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-shared-spaces.htm).

Arguments:

Store command arguments

| Argument | Description |
| --- | --- |
| fieldlist::= ( \* | [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm#glossary-1 "Glossary term")) { , field } ) | A list of the fields to be selected. Using \* as field list indicates all fields.  field::= fieldname [as aliasname ]  fieldname is a text that is identical to a field name in table. (Note that the field name must be enclosed b straight double quotation marks or square brackets if it contains spaces or other non-standard characters.)  aliasname is an alternate name for the field to be used in the resulting QVD or CSV file. |
| table | A script label representing an already loaded table to be used as source for data. |
| filename | The name of the target file including a valid path to an existing folder [data connection](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm#glossary-2 "Glossary term"). For specifics about what is considered a valid path, see [*Rules for valid space folder paths*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules).  In Qlik Cloud Analytics, hierarchical folder structures are supported and can be referenced in the statement.  Examples:   - Personal space (top-level path): [lib://DataFiles/abc.qvd] - Personal space (nested folder): [lib://DataFiles/MyFolder/abc.qvd] - Shared space (top-level path): [lib://TeamSharedSpace:DataFiles/xyz.qvd] - Shared space (nested folder): [lib://TeamSharedSpace:DataFiles/MyFolder/abc.qvd]   For more information and examples, see [*Storing files to spaces in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Store.htm#SpaceStore). |
| format-spec ::=( ( txt | qvd | parquet), compression is codec) | You can set the format specification to either of these file formats. If the format specification is omitted, qvd is assumed.   - txt   for CSV and TXT files. - qvd for QVD files. - parquet for Parquet files.   If you use parquet, you can also set which compression codec to use with compression is. If you do not specify the compression codec with compression is, `snappy` is used. The following compression settings are available:   - `uncompressed` - `snappy` - `gzip` - `lz4` - `brotli` - `zstd` - `lz4_hadoop`   Example:  `Store mytable into [lib://DataFiles/myfile.parquet] (parquet, compression is lz4);` |

> **Note:** The file extension of DataFiles connections is case sensitive. For example: .qvd.

Examples:

Store mytable into [lib://DataFiles/xyz.qvd];

Store \* from mytable into [lib://DataFiles/myfile.qvd];

Store Name, RegNo from mytable into [lib://DataFiles/xyz.qvd];

Store Name as a, RegNo as b from mytable into [lib://DataFiles/myfile.qvd];

Store mytable into [lib://DataFiles/myfile.txt] (txt);

Store mytable into [lib://DataFiles/myfile.parquet] (parquet);

Store \* from mytable into [lib://DataFiles/myfile.csv] (txt);

Store \* from mytable into [lib://TeamSharedSpace:DataFiles/myfile.qvd];

## Storing in Parquet files

Parquet is a strongly typed file format, where each field contains a single specific type of data (such as in32, double, timestamp, or text). Qlik Sense stores internal data as a loosely typed dual, where data from difference sources can be mixed into the same fields. As only one part of the dual can be stored in each field in Parquet, it is important to know what each field contains. By default, Qlik Sense uses the field type to determine how the field should be stored. When storing data in Parquet files in a specific format, you must specify what type of data your fields are when loading them. If you try to store data into incompatible fields in a Parquet file, such as numbers in a text field or text in a timestamp field, you will end up with null values.

When loading data you intend to store in Parquet, it is possible to change the default behavior. You can either format it to change your data type or tag it to force specific column types in Parquet.

### Formatting data for storage in Parquet

You can use Qlik Sense formatting functions to classify your data. For example, **Text()**, **Num()**, **Interval()**, or **Timestamp()** can enforce data formats when storing data in Parquet. Qlik Sense can store data into almost 20 data types depending on field attributes and automatic field tags. For more information, see [*Interpretation functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/interpretation-functions.htm).

Example: Formatting data with **Num()** and **Text()**

The following example demonstrates preparing data for storage in Parquet. **Num()** is applied to the num field. **Text()** is applied to both text and mixed. In the case of mixed, **Text()** prevents it from being treated like a number field in Parquet and having the text values changed to null values.

Data:
LOAD \* INLINE [
num, text, mixed
123.321, abc, 123
456.654, def, xyz
789.987, ghi, 321
];
Format:  
NoConcatenate
LOAD num, text, Text(mixed) as mixed RESIDENT Data;
STORE Format INTO [lib://DataFiles/Tmp.parquet] (parquet);

### Tagging data for storage in Parquet

You tag your data with `$parquet` tags to force specific column types when storing data in Parquet. Each data type can be enforced by adding the corresponding control tag. For example, to store a field as INT32 in Parquet, tag it with `$parquet-int32` in the load script. Depending on the data type, either the string or the numerical representation of the dual data will be stored.

The following Parqeut control tags can be used to tag fields for storing in Parquet files.

Parquet control tags

| Control tag | Dual | Physical type | Logical type | Converted type |
| --- | --- | --- | --- | --- |
| `$parquet-boolean` | Number | BOOLEAN | NONE | NONE |
| `$parquet-int32` | Number | INT32 | NONE | NONE |
| $parquet-int64 | Number | INT64 | NONE | NONE |
| $parquet-float | Number | FLOAT | NONE | NONE |
| $parquet-double | Number | DOUBLE | NONE | NONE |
| $parquet-bytearray | String | BYTE\_ARRAY | NONE | UTF8 |
| $parquet-bytearrayfix | Number | FIXED\_LEN\_BYTE\_ARRAY | NONE | DECIMAL |
| $parquet-decimal | Number | INT64 | DECIMAL | DECIMAL |
| $parquet-date | Number | INT32 | DATE | DATE |
| $parquet-time | Number | INT64 | TIME | TIME\_MICROS |
| $parquet-timestamp | Number | INT64 | TIMESTAMP | TIMESTAMP\_MICROS |
| $parquet-string | String | BYTE\_ARRAY | STRING | UTF8 |
| $parquet-enum | String | BYTE\_ARRAY | ENUM | ENUM |
| $parquet-interval | Number | FIXED\_LEN\_BYTE\_ARRAY | INTERVAL | INTERVAL |
| $parquet-json | String | BYTE\_ARRAY | JSON | JSON |
| $parquet-bson | String | BYTE\_ARRAY | BSON | BSON |
| $parquet-uuid | String | FIXED\_LEN\_BYTE\_ARRAY | UUID | NONE |

Example: Tagging data for storage in Parquet

In this example, two tags are used to define the data for Parquet. The field num is tagged with `$parquet-int32` to define it as a number field that will be set as INT32 in Parquet.

Data:
LOAD \* INLINE [
num, text,
123.321, abc
456.654, def
789.987, ghi
];
TAG num WITH '$parquet-int32';
STORE Format INTO [lib://DataFiles/Tmp.parquet] (parquet);

### Storing nested data in Parquet files

You can store multiple tables in a Parquet files by nesting them into structured data. **Store** supports structured nodes and list nodes in a star schema. Single tables can also be stored in nested mode by using the **Delimiter is** specifier.

When storing tables, specify the tables you want to include separated by commas. For example: `STORE Table1, Table2, Table3 INTO [lib://<file location>/<file name>.parquet] (parquet);`. You can control which fields are stored by using a field list in the **Store** statement. For example `STORE Field1, Field2, FROM Table1, Table2 INTO [lib://<file location>/<file name>.parquet] (parquet);`. All fields in the field list must be in one or more of the listed tables. The first table in the **Store** statement will be used as the fact table in the star schema.

Field names are used to control how groups will be created and nested. By default, field names are split into nodes with a period (`.`). The delimiter can be changed by setting the system variable FieldNameDelimiter or by using the specifier **Delimiter is**. The specifier will override the system variable. For more information, see [*Working with variables in the data load editor*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-variables-in-data-load-editor.htm).

Field names are split by the delimiter and the parts are used to create the schema with nested groups. For example, `STORE Field1, Field1.Field2, Field1.Field3, Field1.Field4 FROM Table1 INTO [nested.parquet] (parquet, delimiter is '.');` will create two groups (Group1 and Group2) with Fields1, Field2 and Field3, Field4.

> **Note:** Groups and fields may not have the same name in a node in the schema. For example, `STORE Address, Address.Street INTO [nested.parquet] (parquet, delimiter is '.'');` will fail because Address is ambiguous and is both a data field and a group.

When storing nested data in Parquet, keys between tables are transformed into link nodes in the schema. Tables are transformed into structured nodes in the schema. You can override the default transformation using field names.

Example: Storing nested data in a Parquet file

company:
LOAD \* INLINE [
company, contact
A&G, Amanda Honda
Cabro, Cary Frank
Fenwick, Dennis Fisher
Camros, Molly McKenzie
];
salesrep:
LOAD \* INLINE [
company, salesrep
A&G, Bob Park
Cabro, Cezar Sandu
Fenwick, Ken Roberts
Camros, Max Smith
];
headquarter:
LOAD \* INLINE [
company, country, city
A&G, USA, Los Angeles
Cabro, USA, Albuquerque
Fenwick, USA, Baltimore
Camros, USA, Omaha
];
region:
LOAD \* INLINE [
region, city
West, Los Angeles
Southwest, Albuquerque
East, Baltimore
Central, Omaha
];
STORE company, salesrep, headquarter, region INTO [lib://DataFiles/company.parquet] (parquet)
DROP TABLES company, salesrep, headquarter, region;

The resulting Parquet file has the following schema:

company (String)
contact (String)
company:salesrep (List)
salesrep (Group)
salesrep (String)
company:headquarter (List)
headquarter (Group)
country (String)
city (String)
city:region (List)
region (Group)
region (String)

#### Limitations

Storing nested data in Parquet has the following limitations:

- Store does not support map nodes.
- Storing does not include key fields generated from loading nested parquet files.
- You cannot store data from tables together that are not linked with key fields.
- The nested file denormalizes the data model. Non-referenced values will not be saved and values referenced multiple times will be copied.

## Storing files to spaces in Qlik Cloud Analytics

When you use a Store statement in a load script in Qlik Cloud, you can reference the exact folder in a space where you want to store the created files. Follow the rules for [valid space folder paths](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules). Additionally, the following behaviors also apply and are unique to Store statements:

- If the space exists but the specified folder path does not, the path will be created in the space. One or more folders might be created depending on the defined folder structure. The file is generated and stored there.
- If the space exists but the specified folder path uses invalid folder delimiters (for example, `\`, `\\`, `//`, `/./`, or `/../`), the Store statement is still executed. The output file is instead saved at the top-level path in the target space and will have a name that contains its full path, not only the specified name.
- If the space does not exist, the Store statement cannot be executed and returns an error.

The following examples demonstrate how to refer to a specific folder path in the space within your Store statement.

Example: Storing file at the top-level path of a space

In this example, the entire table mytable is exported into Qlik Cloud Analytics as a file named myfile.qvd. The file is added to the shared space TeamSharedSpace. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
Store * from mytable into [lib://TeamSharedSpace:DataFiles/myfile.qvd];
```

Example: Storing file to a specific folder path within a space

In this example, the entire table mytable is exported into Qlik Cloud Analytics as a file named myfile.qvd. The file is added to the folder SalesData within the space TeamSharedSpace.

```
Store * from mytable into [lib://TeamSharedSpace:DataFiles/SalesData/myfile.qvd];
```

For more information about referencing space folder structure in load scripts, see [*Referencing space folder structure in application and script development*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#FolderStructureRefExamples).
