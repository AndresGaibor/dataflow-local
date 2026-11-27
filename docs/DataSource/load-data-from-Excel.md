---
title: "Loading data from Microsoft Excel spreadsheets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/load-data-from-Excel.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading data from files"]
---

# Loading data from Microsoft Excel spreadsheets

Qlik Cloud Analytics and Qlik Sense can read data from Microsoft Excel spreadsheets. The supported file formats are XLS, XLSX, XLW and XLSM.

You can either use Add data in data manager, or select data in the data load editor. In both cases you can select named areas of a sheet, a single sheet, selected sheets, or all sheets from the spreadsheet file. Each sheets is loaded as a separate table, except if they have the same field structure, in which case they are concatenated into one table.

Tip noteWhen you load a Microsoft Excel spreadsheet, you are using the spreadsheet as a data source for Qlik Sense applications. That is, Microsoft Excel sheets become tables in Qlik Sense, not sheets in a Qlik Sense application.

You may find it useful to make some changes in Microsoft Excel before you load the spreadsheet.

## Selecting data from Microsoft Excel sheets

When you select data from Microsoft Excel sheets, there are some settings to assist you with interpreting the table data correctly:

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

## Preparing Microsoft Excel spreadsheets for easier loading with Qlik Sense

If you want to load Microsoft Excel spreadsheets into Qlik Sense, there are many functions you can use to transform and clean your data in the data [load script](#glossary-1 "Glossary term"), but it may be more convenient to prepare the source data directly in the Microsoft Excel spreadsheet file. This section provides a few tips to help you prepare your spreadsheet for loading it into Qlik Sense with minimal script coding required.

### Use column headings

If you use column headings in Microsoft Excel, they will automatically be used as field names if you select Embedded field names when selecting data in Qlik Sense. It is also recommended that you avoid line breaks in the labels, and put the header as the first line of the sheet.

### Formatting your data

It is easier to load an Microsoft Excel file into Qlik Sense if the content is arranged as raw data in a table. It is preferable to avoid the following:

- Aggregates, such as sums or counts. Aggregates can be defined and calculated in Qlik Sense.
- Duplicate headers.
- Extra information that is not part of the data, such as comments. The best way is to have a column for comments, that you can easily skip when loading the file in Qlik Sense.
- Cross-table data layout. If, for instance, you have one column per month, you should, instead, have a column called “Month” and write the same data in 12 rows, one row per month. Then you can always view it in cross-table format in Qlik Sense.
- Intermediate headers, for example, a line saying “Department A” followed by the lines pertaining to Department A. Instead, you should create a column called “Department” and fill it with the appropriate department names.
- Merged cells. List the cell value in every cell, instead.
- Blank cells where the value is implied by the previous value above. You need to fill in blanks where there is a repeated value, to make every cell contain a data value.

### Use named areas

If you only want to read a part of a sheet, you can select an area of columns and rows and define it as a named area in Microsoft Excel. Qlik Sense can load data from named areas, as well as from sheets.

Typically, you can define the raw data as a named area, and keep all extra commentary and legends outside the named area. This will make it easier to load the data into Qlik Sense.

### Remove password protection

Password protected files are not supported by Qlik Sense, so you need to remove password protection from the spreadsheet before loading it into Qlik Sense.

### Loading Excel Binary Workbook files (.xlsb)

It is not possible to load Excel Binary Workbook files (.xlsb) directly into Qlik Sense. The workaround is to use an ODBC [connection](#glossary-2 "Glossary term").
