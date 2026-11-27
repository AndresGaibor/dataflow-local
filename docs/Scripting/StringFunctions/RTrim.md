---
title: "RTrim Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/RTrim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# RTrim Script and chart function

Expand/Collapse all

# RTrim Script and chart function

RTrim() returns the input string trimmed of any trailing spaces.

Syntax:

RTrim(text)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| RTrim( ' abc' ) | Returns abc |
| RTrim( 'abc ' ) | Returns abc |

## Example - RTrim fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called InputText.

Load script

```
Set verbatim=1;
Example:
Load * inline [
InputText
'   abc    '
' def  '];
```

Information noteThe Set verbatim=1 statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the RTrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputText

Create the following calculated dimension:

- =RTrim(InputText) to remove trailing spaces from InputText.

Results table

| InputText | RTrim(InputText) |
| --- | --- |
| '      abc    ' | '      abc' |
| ' def  ' | ' def' |

The output of the RTrim function removed all trailing spaces to the right of the original text but retained all leading spaces.

## Example - RTrim scenario

Chart expression

Overview

A customer relationship management (CRM) system contains records with inconsistent data entry that include extra trailing spaces. For reporting purposes, the data requires cleaning to remove these spaces and to ensure proper sorting and grouping of customer names.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called CustomerName.

Load script

```
Set verbatim=1;
Example:
Load * inline [
CustomerName
'John Doe  '
'Jane Smith'
'Michael Johnson  '
'Emily Davis'
];
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the trim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CustomerName

Create the following calculated dimension:

- =RTrim(CustomerName) to remove any trailing spaces from CustomerName.

Results table

| CustomerName | RTrim(CustomerName) |
| --- | --- |
| 'Emily Davis' | 'Emily Davis' |
| 'Jane Smith' | 'Jane Smith' |
| 'John Doe  ' | 'John Doe' |
| 'Michael Johnson  ' | 'Michael Johnson' |

The output shows that the RTrim function removed all trailing spaces from the original string values in CustomerName.

## Example - RTrim advanced scenario

Chart expression

Overview

This example removes all trailing spaces from the original text string. The chart expression includes measures that use the Len function to count the characters in the string before and after using the RTrim function.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called String.

Load script

```
Set verbatim=1;
Example:
Load * inline [
String
'   abc    '
' def  '];
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the RTrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- String

Create the following calculated dimension:

- =RTrim(String), to remove any extra trailing spaces.

Create the following measures:

- =Len(String), to count the length of the original string.
- =Len(RTrim(String)), to count the length of the string after the trailing spaces have been removed.

Results table

| String | RTrim(String) | Len(String) | Len(RTrim(String)) |
| --- | --- | --- | --- |
| ​'  abc    ' | '  abc' | 10 | 6 |
| ​' def  ' | ' def' | 6 | 4 |

When you compare the output of the RTrim function to the original string values in the script, you can see how all trailing spaces have been removed.

Load script

The following code shows how to use the function in a load script.

```
Set verbatim=1;
Example:
Load *, len(RtrimString) as RtrimStringLength;
Load *, rtrim(String) as RtrimString;
Load *, len(String) as StringLength;
Load * Inline [
String
'   abc    '
' def  '];
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the rtrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results table

| String | StringLength | RtrimString | RtrimStringLength |
| --- | --- | --- | --- |
| '   abc    ' | 10 | '   abc' | 6 |
| ' def  ' | 6 | ' def' | 4 |

## Learn more

- [*LTrim Script and chart function*](LTrim.htm)
