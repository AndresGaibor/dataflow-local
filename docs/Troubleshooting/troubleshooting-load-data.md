---
title: "Troubleshooting - Loading data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-load-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data"]
---

# Troubleshooting - Loading data

This section describes problems that can occur when loading and modeling data in Qlik Cloud Analytics and Qlik Sense.

## Attaching a file by dropping it in Add data does not work

You are trying to attach a file by dragging and dropping it on the Add data/Data files dialog, but the file is not uploaded.

Possible cause

The file is stored in a ZIP archive. It is not possible to attach individual files from a ZIP archive.

Proposed action

Extract the files from the ZIP archive before attaching them.

## Character set problems with non-ANSI encoded data files

You may experience problems with character encoding in non-ANSI encoded data files when using an ODBC data connection.

Possible cause

ODBC data connections do not provide full capabilities for character set encoding.

Proposed action

Do the following:

- If possible, import the data files using a folder [data connection](#glossary-0 "Glossary term"), which supports more options for handling character codes. This is probably the best option if you are loading a Microsoft Excel spreadsheet or a text data file.

## Circular references warning when loading data

Possible cause

If you have loaded more than two tables, the tables can be associated in such a way that there is more than one path of associations between two fields, causing a loop in the data structure.

Proposed action

For more information, see [*Understanding and solving circular references*](../LoadData/understand-circular-references.htm).

## Columns are not lining up as expected when selecting data from a fixed record file

Possible cause

The file uses tab characters to pad the columns. Typically, you will see that the field headings do not line up with the expected data if you select Field breaks in the select dialog.

In this case, the tab character is usually equivalent to a number of characters.

Proposed action

Do the following:

1. Select No field names in Field names.
2. Select Field breaks.
3. Increase the setting of Tab size until you see the columns lining up with the header.
4. Insert [field](#glossary-1 "Glossary term") breaks by clicking at the appropriate column positions.
5. Select Data preview.
6. Select Embedded field names in Field names.

The columns are now lined up properly, and each field should have the correct field name.

## Data connection stops working after SQL Server is restarted

Possible cause

If you create a data connection to a SQL Server, and then restart the SQL Server, the data connection may stop working, and you are not able to select data. Qlik Sense has lost connection to the SQL Server and was not able to reconnect.

Proposed action

Do the following:

- Close the application, and open it again from your [activity center](#glossary-3 "Glossary term").

## Data load editor does not display the script

When [Data load editor](#glossary-4 "Glossary term") is opened, the content of the editor is blank, and the script cannot be edited.

Possible cause

The script contains very complex constructions, for example, a large number of nested if statements.

Proposed action

Open the data load editor in safe mode by adding /debug/dle\_safe\_mode to the URL. This will disable syntax highlighting and auto-complete functions, but you should be able to edit and save the script.

Tip noteConsider moving the complex parts of the script to a separate text file, and use the include variable to inject it into the script at runtime.For more information, see [*Include*](../Scripting/SystemVariables/Include.htm).

## Data load script is executed without error, but data is not loaded

The script is executed without syntax or load errors, but data is not loaded as expected. A general recommendation is to activate debug to step through the script and examine execution results, but here are some common causes of error.

For more information, see [*Debugging the data load script*](../LoadData/debug-data-load-script.htm).

### A statement is not terminated with a semicolon

Possible cause

You have forgotten to terminate a statement with a semicolon.

Proposed action

Do the following:

- Terminate all statements with a semicolon.

### Single quote character inside a string

Possible cause

A string contains a single quote character in, for example, a SET variable statement.

Proposed action

Do the following:

- If a string contains a single quote character, it needs to be escaped with an extra single quote.

For more information, see [*Using quotation marks in the script*](../Scripting/use-quotes-in-script.htm).

## Data manager does not show tables in application that contains data

When opening an application created in a Qlik Sense version earlier than 3.0, [Data manager](#glossary-5 "Glossary term") shows no tables and a message is displayed that the application contains no data.

Possible cause

The improved data model in Qlik Sense 3.0 and later requires a data reload to complete data profiling and preparation.

Proposed action

Click Load data in Data manager. This requires that the application can access the data sources that are used in the application.

## Date fields are not recognized as date fields in sheet view

You have fields containing date or timestamp data, but they are not recognized as date fields in sheet view, that is, they are not indicated with ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) in the assets panel and other field lists.

### Data profiling was disabled when the table was added

Possible cause

When you added the tables, you disabled data profiling from ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the Add data button.

With this option, date and timestamp fields that are recognized will function correctly, but they are not indicated with ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) in the assets panel and other field lists, and expanded property fields are not available.

Proposed action

Open Data manager and click Load data.

Now, all date and timestamp fields should be indicated with ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) in the assets panel of sheet view. If they are still not indicated with ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg), the field data is probably using a format that is not recognized as a date.

### Date format was not recognized

Possible cause

The input format of the date field was not recognized when the table was loaded. Usually, Qlik Sense recognizes date fields automatically, based on locale settings and common date formats, but in some cases you may need to specify the input format.

Proposed action

Open Data manager and edit the table containing the field that was not recognized as a date. The field is most likely indicated with ![field type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) as a general field. Change the field type to Date or Timestamp, with an input format that matches the field data.

For more information, see [*Making sure a date or timestamp field is recognized correctly*](../LoadData/changing-date-time-format.htm#Making).

## Error message "Invalid path" when attaching a file

Possible cause

The file name is too long. Qlik Sense only supports file names up to 171 characters.

Proposed action

Rename the file to a name that contains less than 172 characters.

### Unsupported functions or statements are used in the script

Possible cause

If you get a syntax error when running the script in the data load editor, it may be related to using QlikView script statements or functions that are not supported in Qlik Sense.

Proposed action

Do the following:

- Remove the invalid statement or replace it with a valid one.

For more information, see [*QlikView functions and statements not supported in Qlik Sense*](../Scripting/QlikView-functions-statements-not-supported.htm).

## Microsoft Excel: Loading data from files in data manager or data load editor fails

Possible cause

Excel spreadsheet has Freeze Panes or Split screen enabled, and there are empty cells in a table.

Proposed action

Disable Freeze Panes or Split screen, or clean the spreadsheet, and then reload the data.

## Reload fails on connectors with user defined credentials

Application reload fails when using connectors that authenticate with user defined credentials.

Possible cause

You do not have credentials associated with the connections used in the application or the credentials you have assigned to the connections are invalid.

Proposed action

You must assign credentials to the connections used in the application.

Do the following:

1. In the Analytics activity center, right-click on the connection from the Data Sources page of the space where the connection lives.
2. Select Edit Credentials.
3. Input new credentials or select existing credentials from the list.

## Synthetic keys warning when loading data

If you have loaded several files, you may receive a warning that synthetic keys have been created after loading the data.

Possible cause

If two tables contain more than one common field, Qlik Sense creates a [synthetic key](#glossary-6 "Glossary term") to resolve the linking.

For more information, see [*Synthetic keys*](../Scripting/synthetic-keys.htm).

Proposed action

In many cases, you do not need to do anything about synthetic keys if the linking is meaningful, but it is a good idea to review the data structure in the data model viewer.

## Tables with common fields are not automatically associated by field name

You have added two or more tables using Add data. The tables have fields with a common field name, but they are not automatically associated.

Possible cause

When you added the tables, you kept the default option to enable data profiling in the Add data dialog. This option auto-qualifies all field names that are common between tables. For example, if you add table A and table B with a common field F1 using this option, the field will be named F1 in table A, and B.F1 in table B. This means that the tables are not automatically associated.

Proposed action

Open Data manager and select the Associations view. Now you can associate the tables based on data profiling recommendations.

When you have associated the tables, click Load data.

For more information, see [*Managing data associations*](../LoadData/associating-data.htm).
