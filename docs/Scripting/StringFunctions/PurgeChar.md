---
title: "PurgeChar Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/PurgeChar.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# PurgeChar Script and chart function

Expand/Collapse all

# PurgeChar Script and chart function

PurgeChar() returns a string consisting of the characters contained in the input string ('text'), excluding any that appear in the second argument ('remove\_chars').

Syntax:

PurgeChar(text, remove\_chars)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| remove\_chars | A string containing the characters in text to be removed. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| PurgeChar( 'a1b2c3','123' ) | Returns abc |
| PurgeChar( 'a1b2c3','1234' ) | Returns abc |
| PurgeChar( 'a1b22c3','1234' ) | Returns abc |
| PurgeChar( 'a1b2c3','312' ) | Returns abc |
| PurgeChar ( 'a1b2c3','Abc' ) | Returns a123 |

## Example - PurgeChar fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - InputText
  - CharsToPurge

Load script

```
Example:
Load * inline [
InputText, CharsToPurge
'a1b2c3', '123'
'a^b^c', '^'
'A^b^c', 'A^'
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputText
- CharsToPurge

Create the following calculated dimension:

- =PurgeChar(InputText,CharsToPurge), to calculate the characters in InputText that match the characters in CharsToPurge and return only those characters that do not match.

Results table

| InputText | CharsToPurge | PurgeChar(InputText,CharsToPurge) |
| --- | --- | --- |
| A^b^c | A^ | bc |
| a^b^c | ^ | abc |
| a1b2c3 | 123 | abc |

The output of the PurgeChar function returns only those characters from InputText that do not match the characters in CharsToPurge. For example, the first line returns bc and removes the other characters.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load
*,
purgechar(String1, String2) as PurgeChar;
Load * inline [
String1, String2
'a1b2c3', '123'
];
```

Results table

| String1 | String2 | PurgeChar |
| --- | --- | --- |
| a1b2c3 | 123 | abc |

## Example - PurgeChar scenario

Chart expression

Overview

A dataset contains customer names and phone numbers. This example parses the phone number strings to retain only numerical characters and discard all other characters, such as parentheses, dashes, periods, plus signs, and spaces.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - CustomerName
  - PhoneNumber

Load script

```
Example:
Load * inline [
CustomerName, PhoneNumber
John Doe, (123) 456-7890
Jane Smith, 123-456-7890
Bob Johnson, 123.456.7890
Alice Brown, +1 (123) 456 7890
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- CustomerName
- PhoneNumber

Create the following calculated dimension:

- =PurgeChar(PhoneNumber, '()- .+ '), to extract the non-numeric characters from the PhoneNumber field and return only numeric characters.

Results table

| CustomerName | PhoneNumber | PurgeChar(PhoneNumber,'()-.+ ') |
| --- | --- | --- |
| Alice Brown | +1 (123) 456 7890 | 11234567890 |
| Bob Johnson | 123.456.7890 | 1234567890 |
| Jane Smith | 123-456-7890 | 1234567890 |
| John Doe | (123) 456-7890 | 1234567890 |

The output of the PurgeChar function has successfully removed all non-numeric characters from the PhoneNumber string and returned only numbers.

## Learn more

- [*KeepChar Script and chart function*](KeepChar.htm)
