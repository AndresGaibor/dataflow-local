---
title: "LTrim Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/LTrim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# LTrim Script and chart function

Expand/Collapse all

# LTrim Script and chart function

LTrim() returns the input string trimmed of any leading spaces.

Syntax:

LTrim(text)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| LTrim( ' abc' ) | Returns abc |
| LTrim( 'abc ' ) | Returns abc |

## Example - LTrim fundamentals

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

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the LTrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputText

Create the following calculated dimension:

- =LTrim(InputText) to remove leading spaces from InputText.

Results table

| InputText | LTrim(InputText) |
| --- | --- |
| '   abc    ' | 'abc   ' |
| ' def  ' | 'def  ' |

The output of the LTrim function removed all leading spaces to the left of the original text but retained all trailing spaces.

## Example - LTrim scenario

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
'  John Doe'
'Jane Smith'
'  Michael Johnson'
'Emily Davis'
];
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the LTrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CustomerName

Create the following calculated dimension:

- =LTrim(CustomerName) to remove any leading spaces from CustomerName.

Results table

| CustomerName | LTrim(CustomerName) |
| --- | --- |
| '  Michael Johnson' | 'Michael Johnson' |
| '  John Doe' | 'John Doe' |
| 'Emily Davis' | 'Emily Davis' |
| 'Jane Smith' | 'Jane Smith' |

The output shows that the LTrim function removed all leading spaces from the original string values in CustomerName.

## Example - LTrim advanced scenario

Chart expression

Overview

This example removes all leading spaces from the original text string. The chart expression includes measures that use the Len function to count the characters in the string before and after using the LTrim function.

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

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the LTrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- String

Create the following calculated dimension:

- =LTrim(String), to remove any extra leading spaces.

Create the following measures:

- =Len(String), to count the length of the original string.
- =Len(LTrim(String)), to count the length of the string after the leading spaces have been removed.

Results table

| String | LTrim(String) | Len(String) | Len(LTrim(String)) |
| --- | --- | --- | --- |
| ​'   abc    ' | 'abc    ' | 10 | 7 |
| ' def  ' | 'def  ' | 6 | 5 |

When you compare the output of the LTrim function to the original string values in the script, you can see how all leading spaces have been removed.

Load script

The following code shows how to use the function in a load script.

```
Set verbatim=1;
Example:

Load *,
len(LtrimString) as LtrimStringLength;
Load *,
ltrim(String) as LtrimString;
Load *,
len(String) as StringLength;
Load * Inline [
String
'   abc    '
' def  '];
```

Information noteThe "Set verbatim=1" statement is included in the example to ensure that the spaces are not automatically trimmed before the demonstration of the ltrim function. See [*Verbatim*](../SystemVariables/Verbatim.htm)  for more information.

Results table

| String | StringLength | LtrimString | LtrimStringLength |
| --- | --- | --- | --- |
| abc | 10 | abc | 7 |
| def | 6 | def | 5 |

## Learn more

- [*RTrim Script and chart function*](RTrim.htm)
