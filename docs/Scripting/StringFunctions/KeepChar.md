---
title: "KeepChar Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/KeepChar.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# KeepChar Script and chart function

KeepChar() returns a string consisting of any of the characters in the first string that match the characters in the second string. This function is case-sensitive.

Syntax:

KeepChar(text, keep\_chars)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| keep\_chars | A string containing the characters in text to be kept. This argument is case-sensitive. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `KeepChar ( 'a1b2c3','123' )` | Returns `123` |
| `KeepChar ( 'a1b2c3','1234' )` | Returns `123` |
| `KeepChar ( 'a1b22c3','1234' )` | Returns `1223` |
| `KeepChar( 'a1b2c3','312' )` | Returns `123` |

## Example - KeepChar fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `InputText` which contains the original text string to be processed.
  - `CharsToKeep` which contains the list of characters to retain from the original text string after processing.

Load script

```
Example:
Load * inline [
InputText, CharsToKeep
'a1b2c3', '123'
'a^b^c', 'abc'
'A^b^c', 'abc'
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputText
- CharsToKeep

Create the following calculated dimension:

- `=KeepChar(InputText, CharsToKeep)`, to calculate the characters in `InputText` that match the characters in `CharsToKeep`.

Results table

| InputText | CharsToKeep | KeepChar(InputText, CharsToKeep) |
| --- | --- | --- |
| a1b2c3 | 123 | 123 |
| a^b^c | abc | abc |
| A^b^c | abc | bc |

The `KeepChar(InputText, CharsToKeep)` column returns only those characters in `InputText` that exactly match the characters in `CharsToKeep`. For example, the third row returns `bc` as those are the only characters in `InputText` that match the characters in `CharsToKeep`. The uppercase character `A` is not returned as the items in `CharsToKeep` are only lowercase.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load
*,
keepchar(String1, String2) as KeepChar;
Load * inline [
String1, String2
'a1b2c3', '123'
];
```

Results table

| String1 | String2 | KeepChar |
| --- | --- | --- |
| a1b2c3 | 123 | 123 |

## Example - KeepChar scenario to parse unstructured text

Chart expression

Overview

This example uses the function to parse unstructured text (letters, numbers, and symbol characters) and deliver a structured output that retains only numerical characters.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `InputText` which contains the original text string to be processed.
  - `CharsToKeep` which contains the list of characters to retain from the original text string after processing.

Load script

```
Example:
Load * inline [
InputText, InputCategory, CharsToKeep
'The numeric code for input processing is 123-456|789.', 'Code', '0123456789'
'Delivery of batch number: 333*456789.', 'Batch', '0123456789'
'Find the goods received in bay 16a', 'Bay', '0123456789'
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputText
- CharsToKeep

Create the following calculated dimension:

- `=KeepChar(InputText, CharsToKeep)`, to calculate the characters in `InputText` that match the characters in `CharsToKeep`.

Results table

| InputText | CharsToKeep | KeepChar(InputText, CharsToKeep) |
| --- | --- | --- |
| Delivery of batch number: 333\*456789 | 0123456789 | 333456789 |
| Find the goods received in bay 16a | 0123456789 | 16 |
| The numeric code for input processing is 123-456|789 | 0123456789 | 123456789 |

Compare the output of the `KeepChar` function to the original `InputText` string values that loaded in the script. The `KeepChar` function has successfully removed all non-numeric characters from the input text.

## Learn more

- [*PurgeChar Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/PurgeChar.htm)
