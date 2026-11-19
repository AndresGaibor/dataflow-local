---
title: "QvdTableName Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/QvdTableName.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---
# QvdTableName Script function

This script function returns the name of the
table stored in a QVD file.

Syntax:

QvdTableName(filename)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a QVD file, if necessary including path, as a folder or web data connection.  Example: 'lib://Table Files/' |

Examples:

QvdTableName
('MyFile.qvd')

QvdTableName
('C:\MyDir\MyFile.qvd')

QvdTableName
('lib://data\MyFile.qvd')
