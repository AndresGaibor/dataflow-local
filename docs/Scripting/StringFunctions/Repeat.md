---
title: "Repeat Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Repeat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Repeat Script and chart function

Expand/Collapse all

# Repeat Script and chart function

Repeat() forms a string consisting of the input string
repeated the number of times defined by the second argument.

Syntax:

Repeat(text[, repeat\_count])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| repeat\_count | Defines the number of times the characters in the string text are to be repeated in the output string. |

Example: Chart expression

| Example | Result |
| --- | --- |
| Repeat( ' \* ', 4 ) | Returns \*\*\*\* |

## Example - Repeat fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called InputText.

Load script

```
Example:
Load * inline [
InputText
hello world!
hOw aRe you?
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputText

Create the following calculated dimension:

- =Repeat(InputText,2), to calculate the number of times to repeat the value in InputText. In this example, each string will be repeated twice.

Results table

| InputText | Repeat(InputText,2) |
| --- | --- |
| hello world! | hello world!hello world! |
| hOw aRe you? | hOw aRe you?hOw aRe you? |

The output of the Repeat function includes two instances of the InputText string, for example, row 1 returns hello world!hello world!.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load *,
repeat(String,2) as Repeat;
Load * inline [
String
hello world!
hOw aRe you? ];
```

Results table

| String | Repeat |
| --- | --- |
| hello world! | hello world!hello world! |
| hOw aRe you? | hOw aRe you?hOw aRe you? |

## Example - Repeat scenario

Chart expression

Overview

This example uses customer satisfaction data to convert a numeric satisfaction score into a visual representation using smiley face emojis ☺.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - Customer
  - SatisfactionScore

Load script

```
Example:
Load * inline [
Customer, SatisfactionScore
John,4
Mary,2
Peter,5
Susan,3
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Customer
- SatisfactionScore

Create the following calculated dimension:

- =Repeat('☺',(SatisfactionScore)), to calculate and display the score visually with emojis.

Results table

| Customer | SatisfactionScore | Repeat('☺',SatisfactionScore) |
| --- | --- | --- |
| John | 4 | ☺☺☺☺ |
| Mary | 2 | ☺☺ |
| Peter | 5 | ☺☺☺☺☺ |
| Susan | 3 | ☺☺☺ |

The output of the Repeat function shows a visual representation of customer satisfaction using smiley face emojis to represent the numerical satisfaction score.

## Example - Repeat advanced scenario

Chart expression

Overview

A dataset of customer accounts contains account numbers with varying character lengths. This example demonstrates how to use the Repeat function to standardize the length of account numbers.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- One field in the data table called AccountNo.

Load script

```
Example:
Load * inline [
AccountNo
123
45125783
41523
489654
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- AccountNo

Create the following calculated dimension:

- =Repeat(0,10 - Len(AccountNo)) & AccountNo, to pad the account number with zeros to a total length of 10 characters.

Results table

| AccountNo | Repeat(0, 10 - Len(AccountNo)) & AccountNo |
| --- | --- |
| 123 | 0000000123 |
| 41523 | 0000041523 |
| 489654 | 0000489654 |
| 45125783 | 0045125783 |

The output of the Repeat function shows a standardized length of 10 characters for all account numbers.
