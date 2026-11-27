---
title: "File functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FileFunctions/file-functions-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# File functions

Expand/Collapse all

# File functions

The file functions (only available in script expressions) return information about the table file which is
currently being read. These functions will return NULL for all data sources
except table files (exception: ConnectString(
)).

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Attribute

This script function returns the value of the meta tags of different
media files as text. The following file formats are supported: MP3, WMA, WMV, PNG and JPG. If the file filename does not exist, is not a supported file format or does not contain a meta
tag named attributename, NULL will be returned.

[**Attribute**](Attribute.htm)(filename, attributename)

ConnectString

The ConnectString() function returns the name of the active data connection for ODBC or OLE DB connections. The function returns an empty string if no connect statement has been executed, or after a disconnect statement.

[**ConnectString**](ConnectString.htm)()

FileBaseName

The FileBaseName function returns a string containing the name of the table file currently being
read, without path or extension.

[**FileBaseName**](FileBaseName.htm)()

FileDir

The FileDir function returns a string containing the path to the directory of the table file
currently being read.

[**FileDir**](FileDir.htm)()

FileExtension

The FileExtension function returns a string containing the extension of the table file currently
being read.

[**FileExtension**](FileExtension.htm)()

FileName

The FileName function returns a string containing the name of the table file currently being
read, without path but including the extension.

[**FileName**](FileName.htm)()

FilePath

The FilePath function returns a string containing the full path to the table file currently
being read.

[**FilePath**](FilePath.htm)()

FileSize

The FileSize function returns an integer containing the size in bytes of the file filename
or, if no filename is specified,
of the table file currently being read.

[**FileSize**](FileSize.htm)()

FileTime

The FileTime function returns a timestamp in UTC format of the last modification of a specified file. If a file is not specified, the function returns a timestamp in UTC of the last modification of the currently read table file.

[**FileTime**](FileTime.htm)([ filename ])

QvdCreateTime

This script function returns the XML-header timestamp from a QVD file, if any is present, otherwise it returns NULL. In the timestamp, time is provided in UTC.

[**QvdCreateTime**](QvdCreateTime.htm)(filename)

QvdFieldName

This script function returns the name of field
number fieldno
in a QVD file. If the field does not exist NULL is returned.

[**QvdFieldName**](QvdFieldName.htm)(filename , fieldno)

QvdNoOfFields

This script function returns the number of fields
in a QVD file.

[**QvdNoOfFields**](QvdNoOfFields.htm)(filename)

QvdNoOfRecords

This script function returns the number of records
currently in a QVD file.

[**QvdNoOfRecords**](QvdNoOfRecords.htm)(filename)

QvdTableName

This script function returns the name of the
table stored in a QVD file.

[**QvdTableName**](QvdTableName.htm)(filename)
