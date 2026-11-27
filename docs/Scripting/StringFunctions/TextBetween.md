---
title: "TextBetween Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/TextBetween.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# TextBetween Script and chart function

Expand/Collapse all

# TextBetween Script and chart function

TextBetween() returns the text in the input string that occurs between the characters specified as delimiters.

Syntax:

TextBetween(text,
delimiter1, delimiter2[, n])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | The original string. |
| delimiter1 | Specifies the first delimiting character (or string) to search for in text. |
| delimiter2 | Specifies the second delimiting character (or string) to search for in text. |
| n | Defines which occurrence of the delimiter pair to search between. For example, a value of 2 returns the characters between the second occurrence of delimiter1 and the second occurrence of delimiter2. |

Example: Chart expressions

| Example | Result |
| --- | --- |
| TextBetween( '<abc>', '<', '>' ) | Returns abc |
| TextBetween( '<abc><de>', '<', '>',2 ) | Returns de |
| TextBetween( 'abc', '<', '>' ) | Returns NULL  If any of the delimiter is not found in the string, NULL is returned. |
| TextBetween( '<a<b', '<', '>' ) | Returns NULL  If any of the delimiters are not found in the string, NULL is returned. |
| TextBetween( '<>', '<', '>' ) | Returns a zero-length string. |
| TextBetween( '<abc>', '<', '>', 2 ) | Returns NULL, as n is greater than the number of occurrences of the delimiters. |

## Example - TextBetween fundamentals

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
InputText,
<abc><de>
<def><ghi><jk>
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- InputText

Create the following calculated dimensions:

- =TextBetween(InputText,'<','>'), to calculate the first instance of the characters that appear between the delimiters '<' and '>' in the InputText field.
- =TextBetween(InputText,'<','>',2), to calculate the second instance of the characters that appear between the delimiters '<' and '>' in the InputText field.

Results table

| InputText | TextBetween(InputText,'<','>') | TextBetween(InputText,'<','>',2) |
| --- | --- | --- |
| <abc><de> | abc | de |
| <def><ghi><jkl> | def | ghi |

In the first calculated dimension, the output of the TextBetween function returns the first instance of the characters that appear between the delimiters '<' and '>'. For example, row 1 returns abc. The second calculated dimension has an n argument of 2, so the output returns the second instance of the characters that appear between the delimiters '<' and '>'. For example, row 1 returns de.

Load script

The following code shows how to use the function in a load script.

```
Load *,
textbetween(Text,'<','>') as TextBetween,
textbetween(Text,'<','>',2) as SecondTextBetween;
Load * inline [
Text
<abc><de>
<def><ghi><jkl>];
```

Results table

| Text | TextBetween | SecondTextBetween |
| --- | --- | --- |
| <abc><de> | abc | de |
| <def><ghi><jkl> | def | ghi |

## Example - TextBetween scenario

Chart expression

Overview

A dataset contains a data table with email addresses. This example uses the TextBetween function to extract the second-level domain from the address.

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A dataset which is loaded into a data table called Example.
- The following fields in the data table:

  - UserID
  - EmailAddress

Load script

```
Example:
Load * inline [
UserID, EmailAddress
1, alice@example.com
2, bob@sample.org
3, charlie@domain.net
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- UserID
- EmailAddress

Create the following calculated dimension:

- =TextBetween(EmailAddress,'@', '.'), to return the text between the characters '@' and '.' within the EmailAddress field.

Results table

| UserID | EmailAddress | TextBetween(EmailAddress,'@', '.') |
| --- | --- | --- |
| 1 | alice@example.com | example |
| 2 | bob@sample.org | sample |
| 3 | charlie@domain.net | domain |

The output of the TextBetween function returns the second-level domain for each user ID by searching for content between the specified delimiters: '@' and '.'.
