---
title: "Binary"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Binary.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Binary

The binary statement is used
for loading the data from another Qlik Sense application or QlikView document, including section access data. Other elements of the application are not included, for example, sheets, stories, visualizations, master items or variables.

> **Note:** Loading scripts with binary statements is not supported. As scripts do not store the loaded data in the script, loading data from a script with a binary statement results in empty tables.

Only one binary statement is allowed in the script. The binary statement must be the first
statement of the script, even before the SET statements usually located at the beginning of the script.

Syntax:

binary [[path] filename ]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| path | The path to the file which should be a reference to a [data connection](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Binary.htm#glossary-0 "Glossary term") to a file share. Not required if filename is an application ID in a space. |
| filename | The name of the file, including the file extension .qvw or .qvf.  It can also be the ID of an application in a space in your tenant. Open an application to view the application ID in the URL.  If a file name or application ID is not supplied, the statement will load from the application itself. In other words, it will load from the application containing the binary statement. |

Limitations:

You cannot upload QVW or QVF files to the /DataFiles folder. Instead, you can upload the file to a file share, for example AWS S3 or Google Drive, and then load the data from a data connection connected to the file share.

Examples

| String | Description |
| --- | --- |
| Binary ; | This will load data from the application itself. |
| Binary [5136e455-5c4d-452d-b9d9-ef1bd4d0ddcb]; | This will load data from the specified application. |
| Binary [lib://Google\_Drive - youraccount@gmail.com/root/Retail Store Performance.qvw]; | In this example, Retail Store Performance.qvw is located in the Google Drive root directory. |
