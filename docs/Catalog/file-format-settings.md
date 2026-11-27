---
title: "Uploading datasets and editing file format settings"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/file-format-settings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Understanding your data with catalog tools", "Viewing and managing datasets in the catalog"]
---

# Uploading datasets and editing file format settings

When you upload a [dataset](#glossary-0 "Glossary term") to Qlik Cloud Analytics, the file is formatted based on type. If there are any anomalies that might prevent you from using or analyzing the dataset, a notification is shown allowing you to change the file format settings.

## Uploading a dataset

From the Analytics [activity center](#glossary-1 "Glossary term"), click on Dataset in the Create page. Then click Upload data file.
Once the file is uploaded, the Engine will start profiling the dataset.

If an anomaly warning is returned, click File format settings to see more details and to solve the issues. If you dismiss the warning, it is not shown again for the selected dataset. You can access the File format settings from the More actions ![icon More menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu.

## File format settings

The File format settings dialog allows you to change to the appropriate file settings and see how the changes affect the interpretation of the dataset. Saving the settings triggers a refresh of all derived metadata, as these settings can affect the name, number, and content of fields in the dataset. When creating an application from the selected dataset, these new file settings are considered. Depending on the size of the dataset, it might take a few minutes to see the most recent changes on the Overview page.

If you open the File format settings dialog while a dataset profiling is in progress, a notification message displays and you can't save any new changes until the profiling is completed.

## File-specific settings

Supported files have different editable settings. Some file types don't have any settings associated with them. For files with sheets, such as Microsoft Excel, HTML, KML, and XML, the format settings will be at the sheet level, where different sheets in a file can have different settings.

The following file types are supported:

- [*FIX data files*](#FIX)
- [*Microsoft Excel files*](#XLS)
- [*HTML files*](#HTML)
- [*XML files*](#XML)
- [*KML files*](#KML)
- [*Delimited table files*](#Delimite)
- [*QVD files*](#QVD)
- [*QVX files*](#QVX)

### FIX data files

FIX (Fixed record) data files contain a single table in which each record (row of data) contains a number of columns with a fixed field size, usually padded with spaces or tab characters.

#### File format settings

File format settings for fixed record data files

| UI item | Description |
| --- | --- |
| Field names | Specifies whether the table contains Embedded field names or No field names. |
| Header size | Sets Header size to the number of lines to omit as table header. |
| Character set | Specifies the character set used in the table file. |
| Tab size | Number of spaces that one tab character represents in the table file. |
| Record line size | Number of lines that one record spans in the table file. Default is 1. |
| Field break positions | Specifies the positions separated by commas. Each position marks the start of a field. |
| Ignore EOF | Select Ignore EOF if your data contains end-of-file characters as part of the field value. |

### Microsoft Excel files

You can load data stored in XLS and XLSX files.

#### File format settings

File format settings for XLS and XLSX files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Header size | Set Header size to the number of lines to omit as table header. |

### HTML files

HTML files can contain several tables. All elements with a <TABLE> tag are interpreted as a table.

#### File format settings

File format settings for HTML files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Character set | Set the character set used in the table file. |

### XML files

You can load data that is stored in XML format.

There are no specific file format settings for XML files.

### KML files

You can load map files that are stored in KML format, to use in map visualizations.

There are no specific file format settings for KML files.

For more information about map data, see [*Loading your own map data*](../Visualizations/Map/load-map-data.htm).

### Delimited table files

These settings are validated for delimited table files, containing a single table where a line feed separates each record, and each field is separated with a delimited character, for example a CSV file.

#### File format settings

File format settings for delimited table files

| UI item | Description |
| --- | --- |
| Field names | Set to specify if the table contains Embedded field names or No field names. |
| Delimiter | Set the Delimiter character used in your table file. |
| Quoting | Set to specify how to handle quotes:  None = quote characters are not accepted  Standard = standard quoting (quotes can be used as first and last characters of a field value)  MSQ = modern-style quoting (allowing multi-line content in fields) |
| Header size | Set the number of lines to omit as table header. |
| Character set | Set character set used in the table file. |
| Comment | Data files can contain comments between records, denoted by starting a line with one or more special characters, for example //.  Specify one or more characters to denote a comment line. Qlik Sense does not load lines starting with the character(s) specified here. |
| Ignore EOF | Select Ignore EOF if your data contains end-of-file characters as part of the field value. |

### QVD files

You can load data stored in [QVD](#glossary-3 "Glossary term") format. QVD is a native Qlik format and can only be written to and read by Qlik Sense or QlikView. The file format is optimized for speed when reading data from a Qlik Sense script but it is still very compact.

There are no specific file format settings for QVD files.

For more information, see [*Working with QVD files*](../Scripting/work-with-QVD-files.htm).

### QVX files

You can load data that is stored in Qlik data eXchange (QVX) format. QVX files are created by custom connectors developed with the Qlik QVX SDK.

There are no specific file format settings for QVX files.
