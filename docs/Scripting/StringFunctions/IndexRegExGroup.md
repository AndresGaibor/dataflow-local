---
title: "IndexRegExGroup Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IndexRegExGroup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# IndexRegExGroup Script and chart function

Expand/Collapse all

# IndexRegExGroup Script and chart function

IndexRegExGroup() searches the input string and returns the starting position of the nth occurrence of the composite regular expression pattern that is specified. An optional fourth argument count provides the value of n, which is 1 if omitted. The positions in the string are numbered left to right from 1 and up. If no match is found, the function returns 0.

This function performs regex operations that are case-sensitive. You can alternatively use the variant IndexRegExGroupI() to perform case-insensitive regex operations.

Syntax:

IndexRegExGroup
(text, regex, group [, count])

Return data type: integer

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text within which you want to search for a regular expression. |
| regex | The regular expression to use for searching the input string. |
| group | The number of the group, in the case of a composite regular expression.  A group value of 0 returns the index of the entire regex. However, if the regular expression only needs to return the index of the entire match, use the IndexRegEx() function instead.  You can specify a negative group value to search for matches from right to left. |
| count | The number of the match. This is useful when multiple matches for the regular expression might be found in the text. For example, specify a value of 4 to search for the position of the fourth match.  This is an optional argument. Default is 1 if not specified. You can specify a negative value to search for matches from right to left. |

Function examples

| Example | Result |
| --- | --- |
| IndexRegExGroup('abc123','([a-z])([0-9]+)',0) | Returns 3 (start position of complete regex). |
| IndexRegExGroup('abc123','([a-z])([0-9]+)',1) | Returns 3 (start position of first group). |
| IndexRegExGroup('abc123','([a-z])([0-9]+)',2) | Returns 4 , which is the start position of the second group. In the input regex pattern, the string ([0-9]+) corresponds to the second group. |
| IndexRegExGroup('ABC123','([a-z])([0-9]+)',1) | Returns 0, because IndexRegExGroup() is case-sensitive. |
| IndexRegExGroupI('ABC123','([a-z])([0-9]+)',1) | Returns 3. The case-insensitive variant of the function, IndexRegExI(), is used. |

## When to use IndexRegExGroup

Use cases for this function include:

- Identifying where specific text patterns occur within larger bodies of text. For example, you might want to know where the domain of an email address is used across a series of long email messages.
- IndexRegExGroup() is particularly useful for advanced data processing, and is commonly used in the first step of a longer, more complex transformation. It is typically easier to solve problems with other regex functions such as ExtractRegExGroup(), MatchRegEx(), and CountRegEx(), but there may be times when IndexRegExGroup() offers solutions that these functions cannot provide.

## Example 1 – load script to find positions of ISBN components

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The creation of a [variable](#glossary-0 "Glossary term"), ISBN\_RegEx, to store the regular expression we want to use.
- A set of ISBN codes for books that a book store wants to order from several suppliers.

For each ISBN code, we need to extract the starting position of each of the following:

- EAN
- Group
- Registrant
- Publication
- Checksum

Load script

```
SET ISBN_RegEx = 'ISBN[ ]*([0-9]{3})-([0-9]{1})-([0-9]{4})-([0-9]{4})-([0-9]{1})';

ISBN:
LOAD Supplier,
IndexRegExGroup(Books,'$(ISBN_RegEx)',1) AS EAN,
IndexRegExGroup(Books,'$(ISBN_RegEx)',2) AS Group,
IndexRegExGroup(Books,'$(ISBN_RegEx)',3) AS Registrant,
IndexRegExGroup(Books,'$(ISBN_RegEx)',4) AS Publication,
IndexRegExGroup(Books,'$(ISBN_RegEx)',5) AS Checksum;
// Split the ISBN with the Group function in a preceding load to avoid generating a cartesian product
LOAD *,
ExtractRegEx(SupplierBooks, '$(ISBN_RegEx)') AS Books
INLINE [
Supplier, SupplierBooks
Supplier 1, ISBN 123-3-1234-1234-0 ISBN 012-2-0123-0123-4 ISBN 000-1-0123-0123-2 ISBN 234-5-2345-2345-1 ISBN 555-2-5555-5555-3 ISBN 222-4-2222-2222-2
Supplier 2, ISBN 000-0-3333-3333-3 ISBN 333-3-3333-3333-3 ISBN 555-1-5151-5151-3 ISBN 232-1-2323-2323-1 ISBN 008-0-7777-7777-3 ISBN 888-0-9999-0000-0
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- Supplier
- EAN
- Group
- Registrant
- Publication
- Checksum

Results table

| Supplier | EAN | Group | Registrant | Publication | Checksum |
| --- | --- | --- | --- | --- | --- |
| Supplier 1 | 6 | 10 | 12 | 17 | 22 |
| Supplier 1 | 6 | 10 | 12 | 17 | 22 |
| Supplier 1 | 6 | 10 | 12 | 17 | 22 |
| Supplier 1 | 6 | 10 | 12 | 17 | 22 |
| Supplier 1 | 6 | 10 | 12 | 17 | 22 |
| Supplier 1 | 6 | 10 | 12 | 17 | 22 |
| Supplier 2 | 6 | 10 | 12 | 17 | 22 |
| Supplier 2 | 6 | 10 | 12 | 17 | 22 |
| Supplier 2 | 6 | 10 | 12 | 17 | 22 |
| Supplier 2 | 6 | 10 | 12 | 17 | 22 |
| Supplier 2 | 6 | 10 | 12 | 17 | 22 |
| Supplier 2 | 6 | 10 | 12 | 17 | 22 |

In this case, each book contains components in the same positions.

## Example 2 – chart expressions to find URL positions (with IndexRegEx() comparison)

Chart expressions and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table named Correspondence, which contains email message text in a field named EmailBody.
- Email message content that contains web URLs.

We want to find the position of the second URL, if present, as well as the positions of the following components:

- Domain
- Path

We want to use a single regular expression to perform all operations.

Load script

```
Correspondence:

Load * Inline `
ID	EmailBody
1	Thanks again for this morning's meeting! You can find the meeting minutes posted here: https://example.com/resourceexample. If you still have any questions, always feel free to ask me or one of the other team members. Here are a few learning resources that might help you: http://www.example.ca/training1.pptx http://www.example.ca/training2.pptx http://www.example.ca/training3.pptx Thanks again!
2	Hi, you'll want to visit our company website for that, it's available at https://www.example.se.
3	Hello all, I just wanted to let you know that our online stores are now up and running! I couldn't be more excited. We are already seeing quite a bit of traffic and volume sold, which is very promising! For Product A, go to https://www.examplestore1.com/products. For Product B, you'll want go to https://www.examplestore2.com/products. Product C, go check out https://www.examplestore3.com/products. Cheers!

` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- ID

Add these calculated dimensions:

- URL 2 Position:

  ```
  =IndexRegExGroup(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',2)
  ```
- URL 2 Domain Position:

  ```
  =IndexRegExGroup(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',2,2)
  ```
- URL 2 Path Position:

  ```
  =IndexRegExGroup(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',6,2)
  ```

Results table

| ID | URL 2 Position | URL 2 Domain Position | URL 2 Path Position |
| --- | --- | --- | --- |
| 1 | 274 | 281 | 295 |
| 2 | 0 | 0 | 0 |
| 3 | 298 | 306 | 327 |

IndexRegEx() returns the start position of the entire URL, while IndexRegExGroup() returns start positions of individual parts of the URL, corresponding to the group value we used. The record with an ID value of 2 only contains one URL, so values of 0 are returned.

The same regular expression is used across all chart expressions to return different pieces of information. A breakdown of the groups defined in the regular expression is as follows.

Groups in regular expression

| Group number | Regex | URL part |
| --- | --- | --- |
| 1 | ([a-zA-Z0-9]+) | Protocol |
| 2 | (([a-zA-Z0-9]+\.)\*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)) | Domain (groups 3, 4, and 5) |
| 3 | ([a-zA-Z0-9]+\.)\* | Root domain |
| 4 | ([a-zA-Z0-9]+) | Top-level domain |
| 5 | ([a-zA-Z0-9]+) | Path (groups 7, 8, 9, and 10)(optional) |
| 6 | ((\/[a-zA-Z0-9]+)\*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))? | Sub-directory |
| 7 | (\/[a-zA-Z0-9]+)\* | File (groups 9 and 10) |
| 8 | (\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?) | File |
| 9 | ([a-zA-Z0-9]+) | File name |
| 10 | (\.[a-zA-Z0-9]+)? | File extension (optional) |

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](../regular-expressions-qlik-analytics.htm)
