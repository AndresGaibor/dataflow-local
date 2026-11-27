---
title: "Trim Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Trim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Trim Script and chart function

Expand/Collapse all

# Trim Script and chart function

Trim() returns the input string trimmed of any leading and trailing
spaces.

Syntax:

Trim(text)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expression

| Example | Result |
| --- | --- |
| Trim( ' abc' ) | Returns abc |
| Trim( 'abc ' ) | Returns abc |
| Trim( ' abc ' ) | Returns abc |

## Example - Trim fundamentals

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

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the trim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputText

Create the following calculated dimension:

- =Trim(InputText) to remove any extra leading or trailing spaces from InputText.

Results table

| InputText | Trim(InputText) |
| --- | --- |
| '   abc    ' | 'abc' |
| ' def  ' | 'def' |

The output of the Trim function removes all leading and trailing spaces.

## Example - Trim scenario

Chart expression

Overview

A customer relationship management (CRM) system contains records with inconsistent data entry that include extra leading spaces. For reporting purposes, the data requires cleaning to remove these spaces and to ensure proper sorting and grouping of customer names.

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
'  John Doe '
'Jane Smith '
'   Michael Johnson'
'Emily Davis'
];
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the trim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CustomerName

Create the following calculated dimension:

- =Trim(CustomerName) to remove any extra leading or trailing spaces from CustomerName.

Results table

| CustomerName | Trim(CustomerName) |
| --- | --- |
| '   Michael Johnson' | 'Michael Johnson' |
| '  John Doe ' | 'John Doe' |
| 'Emily Davis' | 'Emily Davis' |
| 'Jane Smith ' | 'Jane Smith' |

The output shows that the Trim function removed all leading and trailing spaces from the original string values in CustomerName.

## Example - Trim advanced scenario

Chart expression

Overview

This example removes all leading and trailing spaces from the original text string. The chart expression includes measures that use the Len function to count the characters in the string before and after using the Trim function.

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

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the trim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- String

Create the following calculated dimension:

- =Trim(String), to remove any extra leading or trailing spaces

Create the following measures:

- =Len(String), to count the length of the original string
- =Len(Trim(String)), to count the length of the string after the spaces have been removed.

Results table

| String | Trim(String) | Len(String) | Len(Trim(String)) |
| --- | --- | --- | --- |
| ​'   abc    ' | 'abc' | 10 | 3 |
| ​'  def ' | 'def' | 6 | 3 |

When you compare the output of the Trim function to the original string values in the script, you can see how all leading and trailing spaces have been removed.

Load script

The following code shows how to use the function in a load script.

```
Set verbatim=1;
Example:
Load *, len(TrimString) as TrimStringLength;
Load *, trim(String) as TrimString;
Load *, len(String) as StringLength;
Load * inline [
String
'   abc    '
' def  '](delimiter is '\t');
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the trim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results table

| String | StringLength | TrimString | TrimStringLength |
| --- | --- | --- | --- |
| abc | 10 | abc | 3 |
| def | 6 | def | 3 |
