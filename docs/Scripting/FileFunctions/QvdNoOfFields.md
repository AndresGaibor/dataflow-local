---
title: "QvdNoOfFields Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/QvdNoOfFields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---
# QvdNoOfFields Script function

This script function returns the number of fields
in a QVD file.

Syntax:

QvdNoOfFields(filename)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a QVD file, if necessary including path, as a folder or web data connection.  Example: 'lib://Table Files/' |

Examples:

QvdNoOfFields
('MyFile.qvd')

QvdNoOfFields
('C:\MyDir\MyFile.qvd')

QvdNoOfFields
('lib://DataFiles/MyFile.qvd')
