---
title: "System functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/system-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# System functions

Expand/Collapse all

# System functions

System functions provide functions for accessing system, device and Qlik Sense application [properties](#glossary-1 "Glossary term").

Use the drop-down on each function to see a brief description and the syntax of each function. For some of the functions, you can get further details about that specific function by clicking the function name in the syntax description.

Author()

This function returns
a string containing the author property of the current application. It can be used in both the data load script and in a chart expression.

Information noteAuthor property can not be set in the current version of Qlik Sense. If you migrate a QlikView document, the author property will be retained.

CalcDim()

When used in a [dimension](#glossary-2 "Glossary term") expression, CalcDim() overrides the engine's automatic interpretation of how to internally handle the expression. Specifically, the function prevents a new internal field from being created in the data model. Instead, [selections](#glossary-3 "Glossary term") made in the application are treated as selections in applicable fields from the original data model.

[**calcdim**](calcdim.htm)(expr)

ClientPlatform()

This function returns the user agent string of the client browser. It can be used in both the data load script and in a chart expression.

Example:

Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36

ComputerName

This function returns a string containing the name of the engine instance as returned by
the operating system. It can be used in both the data load script and in a chart expression.

ComputerName( )

DocumentName

This function returns
a string containing the name of the current Qlik Sense application, without path but with extension. It can be used in both the data load script and in a chart expression.

DocumentName( )

DocumentPath

This function returns
a string containing the full path to the current Qlik Sense application. It can be used in both the data load script and in a chart expression.

DocumentPath( )

Information noteThis function is not supported in Qlik Cloud.

DocumentTitle

This function returns
a string containing the title of the current Qlik Sense application. It can be used in both the data load script and in a chart expression.

DocumentTitle( )

EngineVersion

This function returns
the full Qlik Sense engine version as a string.

[**EngineVersion**](EngineVersion.htm)()

GetCollationLocale

This script function returns the culture name of the collation locale that is used. If the variable CollationLocale has not been set, the actual user machine locale is returned.

GetCollationLocale( )

GetObjectField

GetObjectField() returns the field expression of the dimension. Index is an optional integer denoting the dimension that should be returned.

[**GetObjectField**](GetObjectField.htm)([index])

GetSysAttr

The GetSysAttr() function is used to return information about the tenant and space in which an application is located. With the GetSysAttr() function, you can evaluate the tenant ID and name, space ID and name, and other details about the environment where the application resides. This function simplifies space and tenant identification of a Qlik Sense application that might be moved between different environments. The function makes it easy to identify the specific environment you are working in. This is particularly useful during the development, testing, acceptance and production (DTAP) stages of an application's life cycle.

[**GetSysAttr**](GetSysAttr.htm)(name)

GetUserAttr

The GetUserAttr() function returns information for the user accessing an application. It can be used in both the data load script and in a chart expression.

[**GetUserAttr**](GetUserAttr.htm)(name)

GroupDimensionIndex

This function returns the index of the active field for the specified cyclic dimension. The first field has index value of 1. Enter the name of the cyclic dimension in single quotes. It can only be used in a chart expression.

GroupDimensionIndex(dim\_name Expression)

GroupDimensionLabel

This function returns the field label of current step in the specified cyclic dimension. Enter the name of the cyclic dimension in single quotes. It can only be used in a chart expression.

GroupDimensionLabel(dim\_name Expression)

IsPartialReload

This function returns - 1 (True) if the current reload is partial, otherwise 0 (False).

[**IsPartialReload**](IsPartialReload.htm)()

InObject

The InObject() chart function evaluates whether or not the current object is contained inside another object with the ID specified in the function argument. The object can be a sheet or a visualization.

[**InObject**](InObject.htm)(id\_str)

ObjectId

The ObjectId() chart function returns the ID of the object in which the expression is evaluated. The function takes an optional argument specifying which type of object the function concerns. The object can be a sheet or a visualization. This function is only available in chart expressions.

[**ObjectId**](ObjectId.htm)([object\_type\_str])

OSUser

This function returns a string containing the name of the user that is currently connected. It can be used in both the data load script and in a chart expression.

OSUser( )

Information noteIn Qlik Sense Desktop and Qlik Sense Client-Managed Mobile, this function always returns 'Personal\Me'.

ProductVersion

This function returns
the full Qlik Sense version and build number
as a string.

This function is deprecated and replaced by EngineVersion().

[**ProductVersion**](ProductVersion.htm)()

Information noteThis function is not supported in Qlik Cloud.

ReloadTime

This function returns a timestamp for when the last data load finished. The timestamp returned is in UTC format.  It can be used in both the data load script and in a chart expression.

ReloadTime( )

StateName

StateName() returns the name of the alternate state of the visualization in which it is used. StateName can be used, for example, to create visualizations with dynamic text and colors to reflect when the state of a visualization is changed. This function can be used in chart expressions, but cannot be used to determine the state that the expression refers to.

[**StateName**](StateName.htm)()

Information noteThis function is not supported in Qlik Cloud.
