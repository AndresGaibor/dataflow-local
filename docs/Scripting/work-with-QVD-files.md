---
title: "Working with QVD files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-QVD-files.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting"]
---

# Working with QVD files

A QVD (QlikView Data) file is a file containing a table of data exported from a Qlik Sense application or from a script. QVD is a native Qlik format and can only be written
to and read by Qlik Sense or QlikView. The file format is optimized for speed when reading
data from a script but it is still very compact. Reading data from a QVD file is typically 10-100 times faster than reading from other
data sources.

QVD files can be read in two modes: standard (fast) and
optimized (faster). The selected mode is determined automatically by the script engine.

There are some limitations regarding optimized loads. It is possible to rename fields, but any of the operations mentioned here will disable the optimized load and result in a standard load.

- Any transformations on the fields that are loaded.
- Using a where clause causing Qlik Sense to unpack the records.
- Using Map on a field that is loaded.

## Purpose of QVD files

QVD files can be used for many purposes and more than one may apply in any given situation. At least four major uses can
be easily identified:

- Decreasing
  load on database servers

  The amount of data fetched from external data
  sources can also be greatly reduced. This reduces the workload on external databases and network traffic. Furthermore, when several scripts
  share the same data, it is only necessary to load it once from the source
  database into a QVD file. Other applications or scripts can make use of the same data through this QVD file.
- Consolidating data from multiple applications

  With the binary script statement, data can be loaded from a single application into another application or script, but
  with QVD files a load script can combine data from any number of applications or other data sources. This makes it possible for applications and scripts to consolidate
  similar data from different business units, for example.
- Incremental

  In many common cases, the QVD functionality can be used for incremental load by loading only new records from a growing database.

For more information, see [*Loading new and updated records with incremental load*](../LoadData/use-QVD-files-incremental-load.htm).

Information note

To see how the Qlik Community is using Qlik Automateto improve QVD load times, see [How to split QVDs using an automation to improve reloads](https://community.qlik.com/t5/Official-Support-Articles/How-to-split-QVDs-using-an-automation-to-improve-reloads/ta-p/1997153)

## Creating QVD files

A QVD file can be created and named using the Store command in the load script. State in the script that a previously-read table, or part thereof, is to be exported to
an explicitly-named file at a location of your choice.

For more information, see [*Store*](ScriptRegularStatements/Store.htm).

## Reading data from QVD files

A QVD file can be read or accessed by the following methods:

- Loading a QVD file as
  an explicit data source. QVD files can be referenced by a LOAD statement in the script, just like any other type of text files (csv, fix, dif, biff etc).

  For example:

  - LOAD \* from [lib://DataFiles/xyz.qvd];
  - LOAD Name, RegNo from [lib://DataFiles/xyz.qvd];
  - LOAD Name as a, RegNo as b from [lib://DataFiles/xyz.qvd];
- Accessing QVD files from
  the script. A number of script functions (all beginning with qvd)
  can be used for retrieving various information on the data found in the XML header of a QVD file.

## QVD format

A QVD file holds exactly one data table and consists of three parts:

- Header.

  Information noteIf the QVD file was generated with QlikView the header is a well-formed XML header (in UTF-8 char set) describing the fields in the table, the layout of the subsequent information and other metadata.
- Symbol tables in a byte-stuffed format.
- Actual table data in a bit-stuffed format.
