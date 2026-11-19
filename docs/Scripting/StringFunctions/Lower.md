---
title: "Lower Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Lower.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# Lower Script and chart function

Lower() converts all the characters in the input string to lower case.

Syntax:

Lower(text)

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The string to evaluate. |

Example: Chart expression

| Example | Result |
| --- | --- |
| `Lower( 'abcD' )` | Returns `abcd` |

## Example - Lower fundamentals

Chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- One field in the data table called `InputText`.

Load script

```
Example:
Load * inline [
InputText
rHode iSland
washingTon d.C.
new york
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `InputText`

Create the following calculated dimension:

- `=Lower(InputText)` to convert all characters in the `InputText` field to lowercase.

Results table

| InputText | Lower(InputText) |
| --- | --- |
| new york | new york |
| rHode iSland | rhode island |
| washingTon d.C. | washington d.c. |

The output of the `Lower` function converts all values to lowercase.

Load script

The following code shows how to use the function in a load script.

```
Load
String,
Lower(String)
Inline
[String
rHode iSland
washingTon d.C.
new york];
```

Results table

| String | Lower(String) |
| --- | --- |
| rHode iSland | rhode island |
| washingTon d.C. | washington d.c. |
| new york | new york |

## Example - Lower scenario

Chart expression

Overview

A dataset of customer data contains email addresses with mixed-case characters for the domain. The company wants to standardize these addresses to use all lowercase.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called `Example`.
- The following fields in the data table:

  - `CustomerID`
  - `EmailAddress`
  - `Inquiry`

Load script

```
Example:
Load * inline [
CustomerID,	EmailAddress, Inquiry
1001,john.doe@Gmail.com, Inquiry about product return
1002,mary.jane@yahoo.com, Inquiry about order status
1003,a.smith@GMAIL.COM, Inquiry about shipping details
1004,lisa.black@outlook.com, General product inquiry
1005,james.wong@Yahoo.COM, Question about pricing
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `CustomerID`
- `EmailAddress`

Create the following calculated dimension:

- `=Lower(EmailAddress)` to separate the domain part of the email as a new column and convert the characters to lowercase.

Results table

| CustomerID | EmailAddress | Lower(EmailAddress) |
| --- | --- | --- |
| 1001 | john.doe@Gmail.com | john.doe@gmail.com |
| 1002 | MARY.JANE@YAHOO.COM | mary.jane@yahoo.com |
| 1003 | a.smith@GMAIL.COM | a.smith@gmail.com |
| 1004 | lisa.black@Outlook.Com | lisa.black@outlook.com |
| 1005 | james.wong@Yahoo.COM | james.won@yahoo.com |

The output of the `Lower` function returns all email addresses in lowercase.
