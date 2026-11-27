---
title: "QvdFieldName Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/QvdFieldName.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# QvdFieldName Script function

This script function returns the name of field
number fieldno
in a QVD file. If the field does not exist NULL is returned.

Syntax:

QvdFieldName(filename , fieldno)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a QVD file, if necessary including path, as a folder or web data connection.  Example: 'lib://Table Files/' |
| fieldno | The number of the [field](#glossary-0 "Glossary term") within the table contained in the [QVD](#glossary-1 "Glossary term") file. |

Examples:

QvdFieldName
('MyFile.qvd', 5)

QvdFieldName
('C:\MyDir\MyFile.qvd', 5)

QvdFieldName
('lib://DataFiles/MyFile.qvd', 5)

All three examples return the name of the fifth field of the table contained in the
QVD file.
