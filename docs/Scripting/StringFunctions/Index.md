---
title: "Index Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Index.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Index Script and chart function

Index() searches a string to find the starting position of
the nth occurrence of a provided substring. An optional third argument provides the value of n, which is 1 if omitted. A negative value searches from the end of the string. The positions in the string are numbered left to right from
1 and up.

Syntax:

Index(text, substring[, count])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| substring | A string of characters to search for in text.  **Note:** If the substring does not exist in the text, Index returns 0. |
| count | Defines which occurrence of substring to search for. For example, a value of 2 searches for the second occurrence. A negative value starts from the end of the string. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| `Index( 'abcdefg', 'cd' )` | Returns `3` |
| `Index( 'abcdabcd', 'b', 2 )` | Returns `6` (the second occurrence of `b`) |
| `Index( 'abcdabcd', 'b',-2 )` | Returns `2` (the second occurrence of `b` starting from the end) |
| `Left( Date, Index( Date,'-') -1` ) where `Date = 1997-07-14` | Returns `1997` |
| `Mid( Date, Index( Date, '-', 2 ) -2, 2 )` where `Date` =  `1997-07-14` | Returns `07` |
| `Index( 'abc', 'x' )` | Returns `0` (`x` does not exist in the string `abc`) |
| `Index( 'abc', 'a', 2 )` | Returns `0` (there is no 2nd occurrence of `a`) |

## Example - Index fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `InputString`.

Load script

```
Example:
Load * inline [
InputString
abcdefg
abcdabcd ];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `InputString`

Create the following calculated dimensions:

- `=Index(InputString, 'cd')`
- `=Index(InputString, 'e')`
- `=Index(InputString, 'b', -1)`

Results table

| InputString | Index(InputString, 'cd') | Index(InputString, 'e') | Index(InputString, 'b', -1) |
| --- | --- | --- | --- |
| abcdabcd | 3 | 0 | 6 |
| abcdefg | 3 | 5 | 2 |

The first row with the string `abcdabcd` returns:

- `3`—the first occurrence of `cd`
- `0`—because `e` is not found in the string
- `6`—the first occurrence of `b` starting from the end of the string

The second row with the string `abcdefg` returns:

- `3`—the first occurrence of `cd`
- `5`—the first occurrence of `e`
- `2`—the first occurrence of `b` starting from the end of the string

> **Note:** A negative `count` parameter scans the string in reverse. However, the position returned is always denoted from left to right, even if scanned in reverse.

Load script

The following code shows how to use the function in a load script.

```
Example:
Load
*,
index(String, 'cd') as Index_CD,               // returns 3  in Index_CD
index(String, 'b') as Index_B,                // returns 2 in Index_B
index(String, 'b', -1) as Index_B2;           // returns 2 or 6 in Index_B2
Load * inline [
String
abcdefg
abcdabcd ];
```

Results table

| String | Index\_CD | Index\_B | Index\_B2 |
| --- | --- | --- | --- |
| abcdefg | 3 | 2 | 2 |
| abcdabcd | 3 | 2 | 6 |

## Example - Index scenario

Chart expression

Overview

A customer support center has a dataset that contains subject lines from customer email messages. The support center wants to categorize these emails based on the keywords that appear in the subject line, for example, `Refund`, `Complaint`, and `Technical Issue`. The subject lines are stored in a field in the dataset called `EmailSubject`.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `EmailSubject`.

Load script

```
Example:
Load * inline [
EmailSubject
Request for a Refund - Order 12345
Technical Issue with Product XYZ
Complaint about delivery service
Follow-up on Refund Request
Technical Issue not resolved
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `EmailSubject`

Create the following calculated dimension:

- `=If(Index(EmailSubject, 'Refund') > 0, 'Refund', 'Other')`, to calculate which email subject text relate to refunds.

Results

| EmailSubject | If(Index(EmailSubject, 'Refund') > 0, 'Refund', 'Other') |
| --- | --- |
| Complaint about delivery service | Other |
| Follow-up on Refund Request | Refund |
| Request for a Refund - Order 12345 | Refund |
| Technical Issue not resolved | Other |
| Technical Issue with Product XYZ | Other |

The output of the `Index` function has successfully identified all subject lines which contain the string `Refund`. This is an example of how you can analyze and categorize data using nested functions and deliver value to users.
