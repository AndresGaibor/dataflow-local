---
title: "Len Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Len.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Len Script and chart function

Len() returns the length of the input string.

Syntax:

Len(text)

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expression

| Example | Result |
| --- | --- |
| `Len('Peter')` | Returns `5` |

## Example - Len fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `CustomerComment`. The field contains the original text string to evaluate.

Load script

```
Example:
Load  * inline [
CustomerComment
Please deliver after 5 PM.
Thank you for the quick service!
Can you add a gift wrap?
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `CustomerComment`

Create the following measure:

- `=Len(CustomerComment)`

Results table

| CustomerComment | Len(CustomerComment) |
| --- | --- |
| Can you add a gift wrap? | 24 |
| Please deliver after 5 PM. | 26 |
| Thank you for the quick service! | 32 |

The output of the measure `Len(CustomerComment)` returns the length of the `CustomerComment` input string.

## Example - Len scenario

Chart expression

Overview

This example analyzes customer feedback by looking at the length of each comment as an indicator of its depth or level of detail.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `TicketID`
  - `Description`

Load script

```
Example:
Load * inline [
TicketID, Description
1001, "I received the wrong product."
1002, "The package arrived damaged, and I would like a replacement."
1003, "I've been trying to reset my password for two days, and I haven't received an email."
1004, "My order status shows 'Delivered' but I have not received my package yet."
1005, "Is product XYZ available in size Large?"
1006, "I need help with an exchange for a faulty product, and I've attached photos."
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `TicketID`
- `Description`

Create the following calculated dimension:

- `=If(Len(Description) < 30, 'Short',If(Len(Description) <= 50, 'Medium', 'Long'))`, to calculate and assign a category (Short, Medium, Long) to the ticket based on the length of the description.

Results table

| TicketID | Description | If(Len(Description) < 30, 'Short',If(Len(Description) <= 50, 'Medium', 'Long')) |
| --- | --- | --- |
| 1001 | I received the wrong product. | Short |
| 1002 | The package arrived damaged, and I would like a replacement. | Long |
| 1003 | I've been trying to reset my password for two days, and I haven't received an email. | Long |
| 1004 | Is product XYZ available in size Large? | Medium |
| 1005 | My order status shows 'Delivered' but I have not received my package yet. | Long |
| 1006 | I need help with an exchange for a faulty product, and I've attached photos. | Long |

The output of the calculated dimension shows how you can use the `Len` function to categorize data by interpreting the length of text strings.

## Example - Len scenario using string manipulation

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `InputText`.

Load script

```
Example:
Load  * inline [
InputText
this is a sample text string
capitalize first letter only
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `InputText`

Create the following calculated dimensions:

- `=Upper(Left(InputText,1))` , to convert the first letter of the text string to uppercase.
- `=Mid(InputText,Len(upper(Left(InputText,1)))+1)`, to remove the first letter from the text string.
- `=Upper(left(InputText,1)) & Mid(InputText,len(upper(left(InputText,1)))+1)`, to combine the output from the first calculated dimension with the output from the second calculated dimension.

Results table

| InputText | Upper(Left(InputText,1)) | Mid(InputText,Len(upper(Left(InputText,1)))+1) | Upper(left(InputText,1)) & mid(InputText,len(upper(left(InputText,1)))+1) |
| --- | --- | --- | --- |
| this is a sample text string | T | his is a sample text string | This is a sample text string |
| capitalize first letter only | C | apitalize first letter only | Capitalize first letter only |

In the first calculated dimension, the `Upper` and `Left` functions are combined to return the first letter of the `InputText` as uppercase. In the second calculated dimension, the `Mid` function uses the `Len` function to return a text string that removes the first character from `InputText`. The third calculated dimension combines the first and second calculated dimensions and returns the `InputText` string with an uppercase first character.

Load script

This example uses the same functions (`Upper`, `Mid`, and `Len`) as the chart expression scenario. The load script creates a new field, `NewInputText`, that returns the `InputText` with an uppercase first character.

```
Example:
Load InputText, First&Second as NewInputText;
Load *, mid(InputText,len(First)+1) as Second;
Load *, upper(left(InputText,1)) as First;
Load  * inline [
InputText
this is a sample text string
capitalize first letter only ];
```

Results table

| InputText | NewInputText |
| --- | --- |
| this is a sample text string | This is a sample text string |
| capitalize first letter only | Capitalize first letter only |
