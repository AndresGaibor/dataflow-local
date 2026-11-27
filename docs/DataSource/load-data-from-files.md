---
title: "Loading data from files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/load-data-from-files.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Loading data from files

Qlik Cloud Analytics and Qlik Sense can read data from a variety of file formats.

## File formats

There are several supported data file formats:

- Text files: Data in fields must be separated by delimiters such as commas, tabs, or semicolons. For example: comma-separated variable (CSV) files.
- HTML tables
- Excel files

  Information noteYou cannot load data from password-protected Excel files, or Excel Binary Workbook files (.xlsb).

  For more information, see [*Loading data from Microsoft Excel spreadsheets*](load-data-from-Excel.htm).
- XML files
- Qlik native QVD and QVX files

  For more information, see [*Working with QVD files*](../Scripting/work-with-QVD-files.htm).
- Apache Parquet files

  For more information, see [*Working with Apache Parquet files*](../Scripting/work-with-parquet-files.htm).
- JSON files

  For more information, see [*Working with JSON files*](../Scripting/working-with-JSON.htm).
- Fixed record length files
- Data Interchange Format (DIF) files: DIF files can only be loaded with the data load editor.
- Geographic data files:

  - GEOJSON
  - ESRIJSON
  - GML
  - KML
  - SHPZIP
  - DXF

  Information note

  The following file types must be loaded using a GeoOperations connection:

  - GEOJSON
  - ESRIJSON
  - GML
  - SHPZIP
  - DXF

  For more information, see [*Qlik GeoOperations analytics sources*](../../Global_Common/GeoOperationsFunctions/GeoOperations.htm).
- QlikView script files (QVS)

DataFiles [connections](#glossary-0 "Glossary term") are automatically created for each space you can access. For example, under Data Connections you might see:

- DataFiles: connection to your [personal space](#glossary-1 "Glossary term").
- DataFiles (Marketing team): connection to a [shared space](#glossary-2 "Glossary term").

You can also load and store files from shared space folders if you have edit permission. For more information, see [*Adding data from uploaded data files*](../LoadData/adding-data-datafiles.htm).

Information noteThe file extension of DataFiles connections is case sensitive. For example: .qvd.

## How do I load data from files?

There are several ways to load data from files.

Information noteUsers with edit permissions in a space can read, write, and load DataFiles in that space. Other users will not see the DataFiles.

### Adding data from the data catalog

You can load data from datasets to which you have access using the [data catalog](#glossary-3 "Glossary term"). You can load data from multiple datasets.

Under Add data, click Add from data catalog.

For more information, see [*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm).

### Selecting data from a data connection in the data load editor

You can go to Data Connections, and use the ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) Select data dialog to select data to load.

For more information, see [*Selecting data in load scripts*](../LoadData/select-data-to-load.htm).

### Loading data from a file by writing script code

Files are loaded using a LOAD statement in the script. LOAD statements can include the full set of script expressions. To read in data from another Qlik Sense application, you can use a Binary statement.

For more information, see [*Load*](../Scripting/ScriptRegularStatements/Load.htm).

Related learning:

- [How do I load data into a Qlik Sense application?](/lnk/How_load_data_QS_SaaS_app)
