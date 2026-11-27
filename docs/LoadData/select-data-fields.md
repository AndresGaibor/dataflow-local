---
title: "Selecting data fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/select-data-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Adding data to the application from connections and new files"]
---

# Selecting data fields

You can select which tables and fields to use when you add data, or when you edit a table.

Some data sources, such as a CSV file, contain a single table, while other data sources, such as Microsoft Excel spreadsheets or databases, can contain several tables.

If a table contains a header row, [field](#glossary-0 "Glossary term") names are usually automatically detected, but you may need to change the Field names setting in some cases. You may also need to change other table options, such as Header size or Character set, to interpret the data correctly. Table options are different for different types of data sources.

## Selecting data from a database

The steps for selecting data from a database depend on how you connect to the database. You can connect through a Qlik Database connector that is part of the Qlik ODBC Connector Package installed with Qlik Sense.

When you add data from a database, the data source can contain several tables.

Do the following:

1. This step is relevant to Databricks only. If your Databricks host supports Unity [catalog](#glossary-1 "Glossary term"), the catalog you specified in the Create new connection dialog will appear in the Catalog field. You can either leave it unchanged or selected a different catalog from the drop-down list.

   Information noteWhile you can select data from multiple databases, all of the databases must belong to the same catalog.
2. Select a Database from the drop-down list.

   Some selection dialogs do not have a Database drop-down list because the database name is entered when the connection is configured.
3. Select Owner of the database.

   The list of Tables is populated with views and tables available in the selected database. Some databases do not require that owners be specified in the data selection process.
4. Select a table.
5. Select the fields you want to load by checking the box next to each field you want to load.

   You can select all fields in the table by checking the box next to the table name.

   Tip noteYou can edit the field name by clicking on the existing field name and typing a new name. This may affect how the table is linked to other tables, as they are joined on common fields by default.
6. Select additional tables if you want to add data from them.
7. When you are done with your data selection, click Add data to continue with data profiling, and to see recommendations for table relationships.

   For more information, see [*Managing data associations*](associating-data.htm).

   If you want to load the data directly into your application, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside Add data and then disable data profiling. This will load the selected data as it is, bypassing the data profiling step, and you can start creating visualizations. Tables will be linked using natural associations, that is, by commonly-named fields.

   For more information, see [*Associations between logical tables*](../Scripting/associations-between-logical-tables.htm).

## Selecting data from a Microsoft Excel spreadsheet

When you add data from a Microsoft Excel spreadsheet, the file can contain several [sheets](#glossary-2 "Glossary term"). Each sheet is loaded as a separate table. An exception is if the sheet has the same field/column structure as another sheet or loaded table, in which case the tables are concatenated.

For more information, see [*Loading data from Microsoft Excel spreadsheets*](../DataSource/load-data-from-Excel.htm).

Do the following:

1. Make sure you have the appropriate settings for the sheet:

   Settings to assist you with interpreting the table data correctly

   | UI item | Description |
   | --- | --- |
   | Field names | Set to specify if the table contains Embedded field names or No field names. Typically in an Excel spreadsheet, the first row contains the embedded field names. If you select No field names, fields will be named A,B,C... |
   | Header size | Set to the number of rows to omit as table header, typically rows that contain general information that is not in a columnar format. |

   Example

   My spreadsheet looks like this:

   Spreadsheet example

   |  |  |  |  |
   | --- | --- | --- | --- |
   | Machine: | AEJ12B | - | - |
   | Date: | 2015-10-05 09 | - | - |
   | Timestamp | Order | Operator | Yield |
   | 2015-10-05 09:22 | 00122344 | A | 52 |
   | 2015-10-05 10:31 | 00153534 | A | 67 |
   | 2015-10-05 13:46 | 00747899 | B | 86 |

   In this case you probably want to ignore the two first lines, and load a table with the fields Timestamp, Order, Operator, and Yield. To achieve this, use these settings:

   Settings to ignore the two first lines and load the fields

   | UI item | Description |
   | --- | --- |
   | Header size | 2  This means that the first two lines are considered header data and ignored when loading the file. In this case, the two lines starting with Machine: and Date: are ignored, as they are not part of the table data. |
   | Field names | Embedded field names.  This means that the first line that is read is used as field names for the respective columns. In this case, the first line that will be read is the third line because the two first lines are header data. |
2. Select the first sheet to select data from. You can select all fields in a sheet by checking the box next to the sheet name.
3. Select the fields you want to load by checking the box next to each field you want to load.

   Tip noteYou can edit the field name by clicking on the existing field name and typing a new name. This may affect how the table is linked to other tables, as they are joined by common fields by default.
4. When you are done with your data selection, click Add data to continue with data profiling, and to see recommendations for table relationships.

   If you want to load the data directly into your application, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside Add data and then disable data profiling. This will load the selected data as it is, bypassing the data profiling step, and you can start creating visualizations. Tables will be linked using natural associations, that is, by commonly-named fields.

## Selecting data from a table file

You can add data from a large number of data files.

Do the following:

1. Make sure that the appropriate file type is selected in File format.
2. Make sure you have the appropriate settings for the file. File settings are different for different file types.

   For more information, see [*Choosing settings for file types*](#File).
3. Select the fields you want to load by checking the box next to each field you want to load. You can also select all fields in a file by checking the box next to the sheet name.

   Tip noteYou can edit the field name by clicking on the existing field name and typing a new name. This may affect how the table is linked to other tables, as they are joined by common fields by default.
4. When you are done with your data selection, click Add data to continue with data profiling, and to see recommendations for table relationships.

   Information noteIf you want to load the data directly into your application, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside Add data and then disable data profiling. This will load the selected data as it is, bypassing the data profiling step, and you can start creating visualizations. Tables will be linked using natural associations, that is, by commonly-named fields.

## Choosing settings for file types

### Delimited table files

These settings are validated for delimited table files, containing a single table where each record is separated by a line feed, and each field is separated with a delimited character, for example a CSV file.

#### File format settings

File format settings for delimited table files

| UI item | Description |
| --- | --- |
| File format for delimited table files | Set to Delimited or Fixed record.  When you make a selection, the select data dialog will adapt to the file format you selected. |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Delimiter | Set the Delimiter character used in your table file. |
| Quoting | Set to specify how to handle quotes:  None = quote characters are not accepted  Standard = standard quoting (quotes can be used as first and last characters of a field value)  MSQ = modern-style quoting (allowing multi-line content in fields) |
| Header size | Set the number of lines to omit as table header. |
| Character set | Set character set used in the table file. |
| Comment | Data files can contain comments between records, denoted by starting a line with one or more special characters, for example //.  Specify one or more characters to denote a comment line. Qlik Sense does not load lines starting with the character(s) specified here. |
| Ignore end-of-file character | Select Ignore end-of-file character if your data contains end-of-file characters as part of the field value. |

### Fixed record data files

Fixed record data files contain a single table in which each record (row of data) contains a number of columns with a fixed field size, usually padded with spaces or tab characters.

#### Setting field break positions

You can set the field break positions in two different ways:

- Manually, enter the field break positions separated by commas in Field break positions. Each position marks the start of a field.

  Example: 1,12,24
- Enable Field breaks to edit field break positions interactively in the field data preview. Field break positions is updated with the selected positions. You can:
  - Click in the field data preview to insert a field break.
  - Click on a field break to delete it.
  - Drag a field break to move it.

#### File format settings

File format settings for fixed record data files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Header size | Set Header size to the number of lines to omit as table header. |
| Character set | Set to the character set used in the table file. |
| Tab size | Set to the number of spaces that one tab character represents in the table file. |
| Record line size | Set to the number of lines that one record spans in the table file. Default is 1. |
| Ignore end-of-file character | Select Ignore end-of-file character if your data contains end-of-file characters as part of the field value. |

### HTML files

HTML files can contain several tables. Qlik Sense interprets all elements with a <TABLE> tag as a table.

#### File format settings

File format settings for HTML files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Character set | Set the character set used in the table file. |

### XML files

You can load data that is stored in XML format.

There are no specific file format settings for XML files.

### QVD files

You can load data that is stored in [QVD](#glossary-3 "Glossary term") format. [QVD](#glossary-4 "Glossary term") is a native Qlik format and can only be written to and read by Qlik Sense or QlikView. The file format is optimized for speed when reading data from a Qlik Sense script but it is still very compact.

There are no specific file format settings for QVD files.

For more information, see [*Working with QVD files*](../Scripting/work-with-QVD-files.htm).

### QVX files

You can load data that is stored in Qlik data eXchange (QVX) format. QVX files are created by custom connectors developed with the Qlik QVX SDK.

There are no specific file format settings for QVX files.

For more information, see [Building custom connectors with the Qlik QVX SDK](/en-US/sense-developer/November2026/Subsystems/QVXSDKAPI/Content/Sense_QVXSDKAPI/Introducing-QVX.htm).

### KML files

You can load map files that are stored in KML format, to use in map [visualizations](#glossary-5 "Glossary term").

There are no specific file format settings for KML files.

For more information about map data, see [*Loading your own map data*](../Visualizations/Map/load-map-data.htm).

## Returning to the previous step (Add data)

You can return to the previous step when adding data.

Do the following:

- Click the back arrow to return to the previous step of Add data.
