---
title: "Table format"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-format.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
# Table format

The table format is a file specifier for the LOAD statement that defines the file type. If nothing is specified, a .txt
file is assumed.

Table format types

| Type | Description |
| --- | --- |
| txt | In a delimited text file the columns in the table are separated by a delimiter character.  [*Delimiter is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/delimiter.htm) |
| fix | In a fixed record file, each field is exactly a certain number of characters.  Typically, many fixed record length files contains records separated by a linefeed, but there are more advanced options to specify record size in bytes or to span over more than one line with Record is.  [*Record is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/record-is.htm)  **Note:** If the data contains multi-byte characters, [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-format.htm#glossary-0 "Glossary term") breaks can become misaligned as the format is based on a fixed length in bytes. |
| dif | In a .dif file, (Data Interchange Format) a special format for defining the table is used. |
| biff | Qlik Sense can also interpret data in standard Excel files by means of the biff format (Binary Interchange File Format). |
| ooxml | Excel 2007 and later versions use the ooxml .xslx format.  The **Table is** specifier can be used to define the sheet name to be loaded as a table.  [*Table is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-is.htm) |
| html | If the table is part of an html page or file, html should be used. |
| xml | xml (Extensible Markup Language) is a common markup language that is used to represent data structures in a textual format.  The **Table is** specifier can be used to define the path of the XML to be loaded as a table.  [*Table is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-is.htm) |
| qvd | The format qvd is the proprietary [QVD](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-format.htm#glossary-1 "Glossary term") files format, exported from a Qlik Sense application. |
| qvx | qvx is a file/stream format for high performance output to Qlik Sense. |
| parquet | Apache Parquet is a columnar storage format, highly efficient for storing and querying large datasets.  With Parquet files containing nested data, you can specify the table from the Parquet file to load using **Table is** specifier. For example: `LOAD * FROM [lib://DataFiles/company.parquet] (parquet, table is [company:salesrep.salesrep]);`.  [*Table is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-is.htm)  For more information on loading nested data in Parquet files, see [*Loading data from nested Parquet files*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-parquet-files.htm#Loading). |
| json | JSON (JavaScript Object Notation) is a language-independent data format.  If the JSON contains multiple arrays, the **Table is** specifier can be used to define the path to the iterator for the subtable.  [*Table is*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-is.htm) |

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
