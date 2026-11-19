---
title: "Capitalize Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Capitalize.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Capitalize Script and chart function

Capitalize() function converts the first character of each word in a text string to uppercase and converts all other characters to lowercase.

Syntax:

Capitalize(text)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `Capitalize( 'star trek' )` | Returns `Star Trek` |
| `Capitalize( 'AA bb cC Dd' )` | Returns `Aa Bb Cc Dd` |

## Example - Capitalize fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `TextToCapitalize`.

Load script

```
Example:
Load * inline [
TextToCapitalize
50 Cent
a-ha
BIGBANG
girl in red
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `TextToCapitalize`

Create the following calculated dimension:

- `=Capitalize(TextToCapitalize)`, to calculate which characters to capitalize.

Results table

| TextToCapitalize | Capitalize(TextToCapitalize) |
| --- | --- |
| 50 Cent | 50 Cent |
| a-ha | A-Ha |
| BIGBANG | Bigbang |
| girl in red | Girl In Red |

There is no change to the first row of data as the first set of characters starts with a number and the second is already capitalized.

In the second row, the first and third characters are capitalized.

In the third row, only the first letter is capitalized, and all subsequent letters are set to lowercase.

In the fourth row, the first letter of each word is capitalized.

Load script

The following code shows how to use the function in a load script.

```
Load 
String,
Capitalize(String)
Inline
[String
rHode iSland
washingTon d.C.
new york];
```

Results table

| String | Capitalize(String) |
| --- | --- |
| rHode iSland | Rhode Island |
| washingTon d.C. | Washington D.C. |
| new york | New York |

## Example - Capitalize scenario

Chart expression

Overview

A dataset of customer names are entered using various formats, such as all lowercase, all uppercase, or mixed case. The `Capitalize` function is used to clean the data so that the customer's first and last name are properly capitalized when displayed in the dashboard.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `CustomerName`.

Load script

```
Example:
Load * inline [
CustomerName
john smith
JANE DOE
miCHAel Brown
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CustomerName

Create the following calculated dimension:

- `=Capitalize(CustomerName)`, to capitalize the customer names.

Results table

| CustomerName | Capitalize(CustomerName) |
| --- | --- |
| JANE DOE | Jane Doe |
| john smith | John Smith |
| miCHAel Brown | Michael Brown |

Compare the output of the `Capitalize` function to the original `CustomerName` string values that loaded in the script. You can see how the function successfully converted the names to use proper case. Displaying customer names with standardized capitalization improves the appearance, consistency, and readability of the dashboard.
