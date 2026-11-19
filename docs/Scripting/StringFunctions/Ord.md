---
title: "Ord Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Ord.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Ord Script and chart function

Ord() returns the numeric (ASCII or Unicode) value of the first character of a string. This function is useful to evaluate or compare strings based on their underlying character codes, for example, when sorting or filtering strings with non-standard characters.

Syntax:

Ord(text)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `Ord( 'A' )` | Returns the integer `65` |
| `Ord( 'Ab' )` | Returns the integer `65` |

## Example - Ord fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `Chinese`
  - `Western`

Load script

```
Example:
Load * inline [
Chinese, Western
古琴, Guqin
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Chinese`
- `Western`

Create the following calculated dimensions:

- `=ord(Chinese)`, to return the numeric value of the value in the field named `Chinese`.
- `=ord(Western)`, to return the numeric value of the value in the filed named `Western`.

Results table

| Chinese | Western | ord(Chinese) | ord(Western) |
| --- | --- | --- | --- |
| `古琴` | `Guqin` | 21476 | 71 |

Load script

The following code shows how to use the function in a load script.

```
Example:
Load *,
ord(Chinese) as OrdUnicode,
ord(Western) as OrdASCII;
Load * inline [
Chinese, Western
古琴, Guqin ];
```

Results table

| Chinese | Western | OrdUnicode | OrdASCII |
| --- | --- | --- | --- |
| 古琴 | Guqin | 21476 | 71 |

## Example - Ord scenario

Chart expression

Overview

A dataset of product codes includes some codes that are considered invalid because they start with a special character instead of an alpha-numeric one. Using the `Ord` function to identify the invalid product codes, a new measure is created to label the records either Valid or Invalid.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded in a data table called `Products`.
- One field in the data table called `ProductCode`.

Load script

```
Products:
Load * inline [
ProductCode
AB123
#EX45
12XY9
DEF456
*KLM78
GH789
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `ProductCode`

Create the following calculated dimensions:

- `=Ord(ProductCode)`, to return the numeric value of the first character.

- `=If(Ord(ProductCode) < 48 OR (Ord(ProductCode) > 57 AND Ord(ProductCode) < 65) OR Ord(ProductCode) > 122, 'Invalid Product Code', 'Valid Product Code')`, to check if the ordinal value of the code is alphanumeric. If it is not then that record is flagged as `Not Valid`.

Results table

| Product Code | Ord(ProductCode) | If(Ord(ProductCode) < 48 OR (Ord(ProductCode) > 57 AND Ord(ProductCode) < 65) OR Ord(ProductCode) > 122, 'Invalid Product Code', 'Valid Product Code') |
| --- | --- | --- |
| \*KLM78 | 42 | Invalid Product Code |
| #EX45 | 35 | Invalid Product Code |
| 12XY9 | 49 | Valid Product Code |
| AB123 | 65 | Valid Product Code |
| DEF456 | 68 | Valid Product Code |
| GH789 | 71 | Valid Product Code |

Comparing the output of the `Ord` function to a range of valid alphanumeric values, you can determine which product codes are not valid.
