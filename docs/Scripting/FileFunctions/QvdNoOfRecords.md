---
title: "QvdNoOfRecords Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/QvdNoOfRecords.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# QvdNoOfRecords Script function

Example: This script function returns the number of records
currently in a QVD file.

Syntax:

QvdNoOfRecords(filename)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a QVD file, if necessary including path, as a folder or web data connection.  Example: 'lib://Table Files/' |

Examples:

QvdNoOfRecords
('MyFile.qvd')

QvdNoOfRecords
('C:\MyDir\MyFile.qvd')

QvdNoOfRecords
('lib://DataFiles/MyFile.qvd')
