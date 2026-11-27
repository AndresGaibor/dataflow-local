---
title: "QvdCreateTime Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/QvdCreateTime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "File functions"]
---

# QvdCreateTime Script function

This script function returns the XML-header timestamp from a QVD file, if any is present, otherwise it returns NULL. In the timestamp, time is provided in UTC.

Syntax:

QvdCreateTime(filename)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| filename | The name of a QVD file, if necessary including path, as a folder or web data connection.  Example: 'lib://Table Files/' |

Example:

QvdCreateTime('MyFile.qvd')

QvdCreateTime('C:\MyDir\MyFile.qvd')

QvdCreateTime('lib://DataFiles/MyFile.qvd')
