---
title: "Selecting data in load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/select-data-to-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Selecting data in load scripts

You can select which fields to load from files or database tables and which views of the data source you want by using Select data in [Data load editor](#glossary-0 "Glossary term") or Script.

As well as selecting fields, you can also rename fields in the dialog. When you have finished selecting fields, you can insert the generated script code into your script.

Some data sources, such as a CSV file, contain a single table, while other data sources, such as Microsoft Excel spreadsheets or databases can contain several tables.

Warning note

Do not add a table in Data load editor that has already been added as a scripted table with the same name and same columns in Data manager.

You open Select data by clicking ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok.svg) on a data connection in Data load editor or Script.

You can also select data to load from the data catalog. For more information, see [*Loading data from the data catalog*](adding-data-catalog.htm).

## Selecting data from a database

When selecting data from a database, the data source can contain several tables.

Do the following:

1. In a script editor, click Data sources.
2. Under Data connections on the left, click ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on a database connection.

   The select data dialog is displayed.
3. This step is relevant to Databricks only. If your Databricks host supports Unity catalog, the catalog you specified in the Create new connection dialog will appear in the Catalog field. You can either leave it unchanged or selected a different catalog from the drop-down list.

   Information noteWhile you can select data from multiple databases, all of the databases must belong to the same catalog.
4. Select a Database from the drop-down list.

   Some selection dialogs do not have a Database drop-down list because the database name is entered when the connection is configured.
5. Select Owner of the database.

   The list of Tables is populated with views and tables available in the selected database.

   Some databases do not require that owners be specified in the data selection process.
6. Select a table.
7. Select the fields you want to load by checking the box next to each field you want to load.

   You can select all fields in the table by checking the box next to the table name.

   Tip noteYou can edit the field name by clicking on the existing field name and typing a new name. This may affect how the table is linked to other tables, as they are joined on common fields by default.
8. Select additional tables if you want to add data from them.

   Information noteYou cannot rename fields in the data selection wizard at the same time as you filter for fields by searching. You have to erase the search string in the text box first.

   Information noteIt is not possible to rename two fields in the same table so that they have identical names.
9. When you have finished your data selection, do the following:

   - Click Add.

     The data selection window is closed, and the LOAD /SELECT statements are inserted in the script in accordance with your selections.

## Selecting data from a Microsoft Excel spreadsheet

When you select data from a Microsoft Excel spreadsheet, the file can contain several sheets. Each sheet is loaded as a separate table. An exception is if the sheet has the same field/column structure as another sheet or loaded table, in which case, the tables are concatenated.

For more information, see [*Loading data from Microsoft Excel spreadsheets*](../DataSource/load-data-from-Excel.htm).

Do the following:

1. Click Data sources.
2. If the spreadsheet is in a space that you can access, you can select a space using the drop down menu.
3. Click ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on the appropriate folder connection in the data load editor.

   The select file dialog is displayed.
4. Select a file from the list of files accessible to this folder connection and click Continue.

   You can navigate to the folder within the space where the file is located. Navigate by selecting folders in the list, or type a specific folder path under Path.
5. Select the first sheet to select data from. You can select all fields in a sheet by checking the box next to the sheet name.
6. Make sure you have the appropriate settings for the sheet:

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
7. Select the fields you want to load by checking the box next to each field you want to load.

   Tip noteYou can edit the field name by clicking on the existing field name and typing a new name. This may affect how the table is linked to other tables, as they are joined by common fields by default.
8. When you are done with your data selection, do the following:

   - Click Add.

     The data selection window is closed, and the LOAD /SELECT statements are inserted in the script in accordance with your selections.

Tip noteYou can also use a Microsoft Excel file as data source using the ODBC interface. In that case you need to use an ODBC data connection instead of an All files data connection.

## Selecting data from a table file

You can select data from a large number of data files:

- Text files, where data in fields is separated by delimiters such as commas, tabs or semicolons (comma-separated variable (CSV) files).
- HTML tables.
- XML files.
- KML files.
- Qlik native QVD and QVX files.
- Fixed record length files.
- DIF files (Data Interchange Format).

Do the following:

1. If the file is in a space that you can access, you can select a space using the drop down menu.
2. Click ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) on the appropriate folder connection in the script editor.

   The select file dialog is displayed.
3. Select a file from the list of files accessible to this folder connection and click Continue.

   You can navigate to the folder within the space where the file is located. Navigate by selecting folders in the list, or type a specific folder path under Path.
4. Make sure that the appropriate file type is selected in File format.
5. Make sure you have the appropriate settings for the file. File settings are different for different file types.

   For more information, see [*Choosing settings for file types*](#File).
6. Select the fields you want to load by checking the box next to each field you want to load. You can also select all fields in a file by checking the box next to the sheet name.

   Tip noteYou can edit the field name by clicking on the existing field name and typing a new name. This may affect how the table is linked to other tables, as they are joined by common fields by default.
7. When you are done with your data selection, click Add.
8. The data selection window is closed, and the LOAD /SELECT statements are inserted in the script in accordance with your selections.

   Information noteUsers with edit permissions in a space can read, write, and load DataFiles in that space. Other users will not see the DataFiles.

### Choosing settings for file types

#### Delimited table files

These settings are validated for delimited table files, containing a single table where each record is separated by a line feed, and each field is separated with a delimited character, for example a CSV file.

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

#### Fixed record data files

Fixed record data files contain a single table in which each record (row of data) contains a number of columns with a fixed field size, usually padded with spaces or tab characters.

You can set the field break positions in two different ways:

- Manually, enter the field break positions separated by commas in Field break positions. Each position marks the start of a field.

  Example: 1,12,24
- Enable Field breaks to edit field break positions interactively in the field data preview. Field break positions is updated with the selected positions. You can:
  - Click in the field data preview to insert a field break.
  - Click on a field break to delete it.
  - Drag a field break to move it.

File format settings for fixed record data files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Header size | Set Header size to the number of lines to omit as table header. |
| Character set | Set to the character set used in the table file. |
| Tab size | Set to the number of spaces that one tab character represents in the table file. |
| Record line size | Set to the number of lines that one record spans in the table file. Default is 1. |
| Ignore end-of-file character | Select Ignore end-of-file character if your data contains end-of-file characters as part of the field value. |

#### HTML files

HTML files can contain several tables. Qlik Sense interprets all elements with a <TABLE> tag as a table.

File format settings for HTML files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Character set | Set the character set used in the table file. |

#### XML files

You can load data that is stored in XML format.

There are no specific file format settings for XML files.

#### KML files

You can load map files that are stored in KML format, to use in map [visualizations](#glossary-1 "Glossary term").

There are no specific file format settings for KML files.

For more information, see [*Loading your own map data*](../Visualizations/Map/load-map-data.htm).

#### QVD files

You can load data that is stored in [QVD](#glossary-2 "Glossary term") format. QVD is a native Qlik format and can only be written to and read by Qlik Sense or QlikView. The file format is optimized for speed when reading data from a Qlik Sense script but it is still very compact.

There are no specific file format settings for QVD files.

For more information, see [*Working with QVD files*](../Scripting/work-with-QVD-files.htm).

#### QVX files

You can load data that is stored in Qlik data eXchange (QVX) format. QVX files are created by custom connectors developed with the Qlik QVX SDK.

There are no specific file format settings for QVX files.

For more information, see [Building custom connectors with the Qlik QVX SDK](/en-US/sense-developer/November2026/Subsystems/QVXSDKAPI/Content/Sense_QVXSDKAPI/Introducing-QVX.htm).

#### Apache Parquet

You can load data that is stored in Parquet format.

There are no specific file format settings for Parquet files.

[*Working with Apache Parquet files*](../Scripting/work-with-parquet-files.htm)

#### JSON

You can load data that is stored in JSON format.

There are no specific file format settings for JSON files.

[*Working with JSON files*](../Scripting/working-with-JSON.htm)

## Previewing scripts

The statements that will be inserted are displayed in the script preview, which you can choose to hide by clicking Preview script.

## Including LOAD statements

If Include LOAD statement is selected, SELECT statements are generated with preceding LOAD statements using the SELECT statements as input.

Information noteIf you rename fields in a table, a LOAD statement will be inserted automatically regardless of this setting.

## Inline loads

With inline loads, you can type data manually as text. A basic inline load creates a table, and inserts the data fields and records.

You can create and load inline tables in the Data load editor.

The following script contains a simple inline load.

```
MyTable:
Load * Inline [
Country, Year, Sales
Argentina, 2014, 66295.03
Argentina, 2015, 140037.89
Austria, 2014, 54166.09
Austria, 2015, 182739.87
];
```

The following syntax is used for the above inline load:

- Load \* Inline instructs Qlik Sense to load all fields from the inline table that follows.
- MyTable: defines the name of the table. The list of tables in the application can be accessed from [Data model viewer](#glossary-3 "Glossary term") and other areas.
- Square brackets enclose the data.
- The first line of the load statement defines the data fields.
- Commas separate data fields and records.
- A semi-colon closes the load statement.

For information about inline loads, see [*Using inline loads to load data*](../Scripting/inline-loads-qs.htm).

Related learning:

- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)
- [Loading data from a database](/lnk/Loading_data_from_database_QS)
