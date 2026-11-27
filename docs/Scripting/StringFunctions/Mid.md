---
title: "Mid Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Mid.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# Mid Script and chart function

Expand/Collapse all

# Mid Script and chart function

Mid() returns the part of the input string starting at the position of the character defined by the second argument, 'start', and returning the number of characters defined by the third argument, 'count'. If 'count' is omitted, the rest of the input string is returned. The first character in the input string is numbered 1.

Syntax:

Mid(text, start[, count])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| start | Integer defining the position of the first character in text to include. |
| count | Defines the string length of the output string. If omitted, all characters from the position defined by start are included. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| Mid( 'abcdef',3 ) | Returns cdef |
| Mid( 'abcdef',3, 2 ) | Returns cd |

## Example - Mid fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - InputText, the original text string
  - StartPosition, the starting position of the first character to include from the original text string after processing
  - CharacterCount, the number of characters to return (optional parameter)

Load script

```
Example:
Load * inline [
InputText, StartPosition, CharacterCount
abcdef, 3, 2
abcdef, 2, 3
210714, 3, 2
210714, 2, 3
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- InputText
- StartPosition
- CharacterCount

Create the following calculated dimensions:

- =mid(InputText,StartPosition), to calculate the characters to extract from InputText starting at the value in the StartPosition field. The function will return all characters from the StartPosition value to the end of InputString because no Count parameter was provided.
- =mid(InputText,StartPosition,CharacterCount), to calculate the characters to extract from InputText starting at the value in the StartPosition field. The value in CharacterCount determines the number of characters returned, starting from the value in the StartPosition field.

Results table

| InputText | StartPosition | CharacterCount | Mid(InputText,StartPosition) | Mid(InputText,StartPosition,CharacterCount |
| --- | --- | --- | --- | --- |
| abcdef | 2 | 3 | bcdef | bcd |
| abcdef | 3 | 2 | cdef | cd |
| 20210714 | 2 | 3 | 10714 | 107 |
| 20210714 | 3 | 2 | 0714 | 07 |

The first row returns the value bcdef for the first expression. The expression starts at position 2 and returns all characters because the Count argument is not set. The second expression also starts at position 2 but returns only the characters bcd because the Count argument is 2.

The second row returns the value cdef for the first expression. The expression starts at position 3 and returns all characters because the Count argument is not set. The second expression also starts at position 3 but returns only the characters cd because the Count argument is 2.

The third row returns the value 10714 for the first expression. The expression starts at position 2 and returns all characters because the Count argument is not set. The second expression also starts at position 2 but returns only the characters 107 because the Count argument is 3.

The fourth row returns the value 0714 for the first expression. The expression starts at position 3 and returns all characters because the Count argument is not set. The second expression also starts at position 2 but returns only the characters 07 because the Count argument is 2.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load *,
mid(Text,StartPosition) as Mid1,
mid(Text,StartPosition,Count) as Mid2;
Load * inline [
Text, StartPosition, Count
'abcdef', 3, 2
'abcdef', 2, 3
'210714', 3, 2
'210714', 2, 3
];
```

Results table

| Text | StartPosition | Mid1 | Count | Mid2 |
| --- | --- | --- | --- | --- |
| abcdef | 3 | cdef | 2 | cd |
| abcdef | 2 | bcdef | 3 | bcd |
| 210714 | 3 | 0714 | 2 | 07 |
| 210714 | 2 | 10714 | 3 | 107 |

## Example - Mid scenario

Chart expression

Overview

A data source contains a column called OrderID that uses the following structured format: ORDYYYY-COUNTRYCODE-ORDERNUMBER. To satisfy a reporting requirement, you must extract and present the country code as a separate column.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Orders.
- One field in the data table called OrderID.

Load script

```
Orders:
Load * inline [
OrderID
ORD2024-US-123456
ORD2024-UK-654321
ORD2024-CA-789123
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- OrderID

Create the following calculated dimension:

- =Mid(OrderID, 9, 2) to extract the two-letter country code from the OrderID.

Results table

| OrderID | Mid(OrderID, 9, 2) |
| --- | --- |
| ORD2024-CA-789123 | CA |
| ORD2024-UK-654321 | UK |
| ORD2024-US-123456 | US |

The output of the Mid function has successfully extracted the two-letter country codes from the OrderID string values.

## Learn more

- [*Index Script and chart function*](Index.htm)
