---
title: "Chr Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Chr.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Chr Script and chart function

Expand/Collapse all

# Chr Script and chart function

Chr() returns the Unicode character corresponding to the input integer, also known as a code point.

Syntax:

Chr(int)

Return data type: string

Arguments

| Argument | Description |
| --- | --- |
| int | The integer to evaluate. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Chr(65) | Returns the string A |
| Chr(163) | Returns the string £ |
| Chr(35) | Returns the string # |

## Example - Chr fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called InputInt. The field contains the integer value to evaluate.

Load script

```
Example:
Load * inline [
InputInt
65
163
35
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputInt

Create the following measure:

- =Chr(InputInt), to calculate the values in InputInt and return a Unicode character.

Results table

| InputInt | Chr(InputInt) |
| --- | --- |
| 35 | # |
| 65 | A |
| 163 | £ |

The first row returns the string # as that is the Unicode character that corresponds to the value of 35.

The second row returns the string A as that is the Unicode character that corresponds to the value of 65.

The third row returns the string £ as that is the Unicode character that corresponds to the value of 163.

## Example - Chr scenario

Chart expression

Overview

This example shows how to use the Chr function to create a bullet list of the text strings in a text object.

Results

Open a sheet. Create a new text object, and then add the following code to a measure:

- = Chr(149) & ' Revenue Growth' & Chr(10) & Chr(149) & ' Customer Satisfaction' & Chr(10) & Chr(149) & ' Market Share'

Output of the measure expression in text object

![Text object showing in a sheet with the text strings that were created using the measure expression.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-chr-example.png "Click to view full size")

The output is derived in the following way :

- Chr(149) returns a bullet point (•).
- Chr(10) inserts a line break (newline) between the items.
- The ampersand (&) is a string concatenation operator that concatenates the individual pieces of text into a single text string.
