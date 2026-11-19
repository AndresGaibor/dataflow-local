---
title: "ReplaceRegEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# ReplaceRegEx Script and chart function

ReplaceRegEx() returns a string after replacing one or more matches
between an input string and a specified regular expression pattern. The text that replaces the matching text is specified in the to\_str argument. The function works from left to right, but if you specify a negative occurrence value, the functions reads from right to left.

This function performs regex operations that are case-sensitive. You can alternatively use the variant ReplaceRegExI() to perform case-insensitive regex operations.

[Video: https://share.vidyard.com/watch/1STBZFJeqoouP4SSofdb5R]

Syntax:

ReplaceRegEx
(text, regex, to\_str [, occurrence])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text that you want to replace, fully or partially, with the new text from to\_str. |
| regex | The regular expression that defines when to replace text. Matches between this argument and the text argument are replaced. |
| to\_str | The new text that you want to use to replace existing content from text. |
| occurrence | The number of the match (between input text and regular expression) to replace with new text.  This is an optional argument. The default is 0 if omitted. When a value of 0 is used, or if the argument is omitted, all matches between the text and regex are replaced with to\_str.  You can specify a negative value for occurrence if you want to identify matches from right to left. |

Function examples

| Example | Result |
| --- | --- |
| `ReplaceRegEx('abc123','[0-9]','x')` | Returns `abcxxx`. In this example, all text from the input string that matches the regex pattern are replaced with the new text. |
| `ReplaceRegEx('abc123','[0-9]','x',1)` | Returns `abcx23`. Only the first occurrence of a match between the input string and the regex pattern are replaced. |
| `ReplaceRegEx('abc123','[0-9]','x',4)` | Returns `abc123` . There are only three possible matches between the input string and the regex pattern, so no modification is performed. |
| `ReplaceRegEx('ABC123','[a-c]','5')` | Returns `ABC123`. No modification is performed because **ReplaceRegEx()** is case-sensitive, and the case-insensitive variant is not used. |
| `ReplaceRegExI('ABC123','[a-c]','5')` | Returns `555123`. The case-insensitive variant of the function, ReplaceRegExI(), is used. |

## When to use ReplaceRegEx

You can use ReplaceRegEx() for modifying text to meet formatting and compliance standards, especially when complex patterns exist in the data. For example, you can re-format telephone number strings so that only numeric values are included.

If needed, you can also use this function to mask sensitive information, such as personal identifiable information (PII), so that it is not shown to users analyzing your application.

## Example 1 – load script to update employee email addresses

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table `Employees` containing the email addresses of employees of an organization.
- Creation of a new field, `Email_Updated`, to perform a find and replace operation on values in the field `Email_Original`.

After the company has changed its name, all email addresses have been updated to reflect the new name.

Our requirements:

- Convert all domain references of `test.com` to `newcompanyname.com`.
- We need to use case-insensitive regex operations.

Load script

```
Employees:

Load 
ReplaceRegExI(Email_Original, '@[a-zA-Z0-9.-]*\.?test\.com', '@newcompanyname.com') as Email_Updated,
* Inline [
ID, Email_Original
1, john_doe@test.com
2, jane_doe@test.com
3, Michael_Andrews@test.com
4, charlie_kent@test.com
5, frances_johnson@test.com
6, rebecca_smith@test.com
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `Email_Original`
- `Email_Updated`

Results table

| ID | Email\_Original | Email\_Updated |
| --- | --- | --- |
| 1 | john\_doe@test.com | john\_doe@newcompanyname.com |
| 2 | jane\_doe@test.com | jane\_doe@newcompanyname.com |
| 3 | Michael\_Andrews@test.com | Michael\_Andrews@newcompanyname.com |
| 4 | charlie\_kent@support.test.com | charlie\_kent@newcompanyname.com |
| 5 | frances\_johnson@test.com | frances\_johnson@newcompanyname.com |
| 6 | rebecca\_smith@hr.test.com | rebecca\_smith@newcompanyname.com |

## Example 2 – load script to format ISBN codes

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- [Variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegEx.htm#glossary-0 "Glossary term") `ISBN_13` and `ISBN_10`, which store the regular expressions to use for 13-digit and 10-digit ISBN string patterns, respectively.
- A table `Employees` containing raw numeric values for ISBN book codes. The table contains both 13-digit and 10-digit ISBNs.
- Several operations to extract each part of the ISBN, and then return a string showing the entire code in the standard, expected format. We use a combination of ReplaceRegEx(), MatchRegEx(), ExtractRegExGroup(), and Pick().

Our requirements:

- We want to format the numbers into more readable text, using the standardized formatting:

  - ISBN ###-#-####-####-#
  - ISBN #-###-#####-#

Load script

```
Set ISBN_13 = '^([0-9]{3})([0-9]{1})([0-9]{4})([0-9]{4})([0-9]{1})$';
Set ISBN_10 = '^([0-9]{1})([0-9]{3})([0-9]{5})([0-9]{1})$';

Formatted_Codes:

Load
Pick(MatchRegEx(ISBN_Unformatted, '$(ISBN_13)', '$(ISBN_10)'), ReplaceRegEx(ISBN_Unformatted, '$(ISBN_13)', 'ISBN ' & ISBN_Component1 & '-' & ISBN_Component2 & '-' & ISBN_Component3 & '-' & ISBN_Component4 & '-' & ISBN_Component5), ReplaceRegEx(ISBN_Unformatted, '$(ISBN_10)', 'ISBN ' & ISBN_Component1 & '-' & ISBN_Component2 & '-' & ISBN_Component3 & '-' & ISBN_Component4)) as ISBN_Formatted;

Load *,
Pick(MatchRegEx(ISBN_Unformatted, '$(ISBN_10)', '$(ISBN_13)'), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_10)', 1, 1), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_13)', 1, 1)) as ISBN_Component1,
Pick(MatchRegEx(ISBN_Unformatted, '$(ISBN_10)', '$(ISBN_13)'), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_10)', 2, 1), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_13)', 2, 1)) as ISBN_Component2,
Pick(MatchRegEx(ISBN_Unformatted, '$(ISBN_10)', '$(ISBN_13)'), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_10)', 3, 1), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_13)', 3, 1)) as ISBN_Component3,
Pick(MatchRegEx(ISBN_Unformatted, '$(ISBN_10)', '$(ISBN_13)'), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_10)', 4, 1), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_13)', 4, 1)) as ISBN_Component4,
Pick(MatchRegEx(ISBN_Unformatted, '$(ISBN_10)', '$(ISBN_13)'), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_10)', 5, 1), ExtractRegExGroup(ISBN_Unformatted, '$(ISBN_13)', 5, 1)) as ISBN_Component5
inline `
ISBN_Unformatted
1233123412340
0122012301234
0001012301232
0111234567
5552555555553
2224222222222
1901234568
3333333333333
5551515151513
2321232323231
2444444444
8880999900000
`;
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `ISBN_Formatted`

Results table

| ISBN\_Formatted |
| --- |
| ISBN 000-1-0123-0123-2 |
| ISBN 0-111-23456-7 |
| ISBN 1-901-23456-8 |
| ISBN 2-444-44444-4 |
| ISBN 012-2-0123-0123-4 |
| ISBN 123-3-1234-1234-0 |
| ISBN 222-4-2222-2222-2 |
| ISBN 232-1-2323-2323-1 |
| ISBN 333-3-3333-3333-3 |
| ISBN 555-1-5151-5151-3 |
| ISBN 555-2-5555-5555-3 |
| ISBN 888-0-9999-0000-0 |

## Example 3 – chart expression to update secondary email addresses

Chart expression and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table `Employees` containing the email addresses of employees of an organization. These are stored in a single string for each employee, in which multiple email addresses are stored.

Our requirements:

- Secondary email addresses need to be updated to use the domain `newcompanyname.com`. We do not want to update any primary email addresses.
- We need to use case-insensitive regex operations.

Load script

```
Employees:

Load * Inline [
ID, Emails
1, Primary: john_doe@test.com Secondary: john_michael_doe@example.com
2, Primary: jane_doe@test.com Secondary: jane_tabitha_doe_doe@example.com
3, Primary: Michael_Andrews@test.com Secondary: Michael_John_Andrews@example.com
4, Primary: charlie_kent@test.com Secondary: charlie_peter_kent@example.com
5, Primary: frances_johnson@test.com Secondary: frances_johnson@example.com
6, Primary: rebecca_smith@test.com Secondary: rebecca_danielle_smith@example.com
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `Emails`

Add the following calculated dimension:

```
=ReplaceRegExI(Emails,'@[a-zA-Z0-9.-]*\.?[a-zA-Z0-9]*\.com','@newcompanyname.com',2)
```

Results table

| ID | Emails | =ReplaceRegExI(Emails,'@[a-zA-Z0-9.-]\*\.?example\.com','@newcompanyname.com',2) |
| --- | --- | --- |
| 1 | Primary: john\_doe@test.com Secondary: john\_michael\_doe@example.com | Primary: john\_doe@test.com Secondary: john\_michael\_doe@newcompanyname.com |
| 2 | Primary: jane\_doe@test.com Secondary: jane\_tabitha\_doe\_doe@example.com | Primary: jane\_doe@test.com Secondary: jane\_tabitha\_doe\_doe@newcompanyname.com |
| 3 | Primary: Michael\_Andrews@test.com Secondary: Michael\_John\_Andrews@example.com | Primary: Michael\_Andrews@test.com Secondary: Michael\_John\_Andrews@newcompanyname.com |
| 4 | Primary: charlie\_kent@test.com Secondary: charlie\_peter\_kent@example.com | Primary: charlie\_kent@test.com Secondary: charlie\_peter\_kent@newcompanyname.com.com |
| 5 | Primary: frances\_johnson@test.com Secondary: frances\_johnson@example.com | Primary: frances\_johnson@test.com Secondary: frances\_johnson@newcompanyname.com |
| 6 | Primary: rebecca\_smith@test.com Secondary: rebecca\_danielle\_smith@example.com | Primary: rebecca\_smith@test.com Secondary: rebecca\_danielle\_smith@newcompanyname.com |

By specifying a value of 2 for the occurrence argument, we are able to only update the second instance that matches the regex pattern.

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm)
