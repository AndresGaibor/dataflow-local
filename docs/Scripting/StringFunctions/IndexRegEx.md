---
title: "IndexRegEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IndexRegEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# IndexRegEx Script and chart function

Expand/Collapse all

# IndexRegEx Script and chart function

IndexRegEx() searches the input string and returns the starting position of the nth occurrence of the specified regular expression pattern. An optional third argument count provides the value of n, which is 1 if omitted. The positions in the string are numbered left to right from 1 and up. If no match is found, the function returns 0.

This function performs regex operations that are case-sensitive. You can alternatively use the variant IndexRegExI() to perform case-insensitive regex operations.

Syntax:

IndexRegEx
(text, regex [, count])

Return data type:  integer

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text within which you want to search for a regular expression. |
| regex | The regular expression to use for searching the input string. |
| count | The number of the match. This is useful when multiple matches for the regular expression might be found in the text. For example, specify a value of 4 to extract the position of the fourth match.  This is an optional argument. Default is 1 if not specified. You can specify a negative value to search for matches from right to left. |

Function examples

| Example | Result |
| --- | --- |
| IndexRegEx('abc123','[a-z][0-9]+') | Returns 3 (the start position of first match). |
| IndexRegEx('abc123','[a-z][0-9]+',2) | Returns 0 (regex does not have a second match). |
| IndexRegEx('ABC123','[a-z][0-9]+') | Returns 0, because IndexRegEx() is case-sensitive. |
| IndexRegExI('ABC123','[a-z][0-9]+') | Returns 3. The case-insensitive variant of the function, IndexRegExI(), is used. |

## When to use IndexRegEx

Use cases for this function include:

- Identifying where specific text patterns occur within larger bodies of text. For example, you might want to know where an email address pattern is used across a series of long email messages.
- IndexRegEx() is particularly useful for advanced data processing, and is commonly used in the first step of a longer, more complex transformation. It is typically easier to solve problems with other regex functions such as ExtractRegEx(), MatchRegEx(), and CountRegEx(), but there may be times when IndexRegEx() offers solutions that these functions cannot provide.

## Example 1 – load script to identify books by ISBN

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table ISBN containing email message content in a field named EmailBody.

We want to find the positions of all 13-digit ISBN codes from the natural language in the email message.

Load script

```
SET ISBN_RegEx = 'ISBN[ ]*([0-9]{3})-([0-9]{1})-([0-9]{4})-([0-9]{4})-([0-9]{1})';

ISBN:
LOAD IndexRegEx(EmailText,'$(ISBN_RegEx)',1) AS ISBNCode1,
IndexRegEx(EmailText,'$(ISBN_RegEx)',2) AS ISBNCode2,
IndexRegEx(EmailText,'$(ISBN_RegEx)',3) AS ISBNCode3,
* INLINE `
EmailText
Hi there! I have some books that I'm interested in ordering from your distribution center. Just wanted to make sure they were in stock before I put the order in on the system - do you think you could tell me whether you have these in stock, and how many you might be able to ship us? Thanks! Item 1: ISBN 123-3-1234-1234-0. This is one I've had a really hard time getting a hold of lately. Do you think you would have 5 in stock? If not, can I put a hold on the next 5 you get? Item 2: ISBN 012-2-0123-0123-4 ... This one is not high-priority, but if you have one, I'll take it! Item 3: ISBN 000-1-0123-0123-2. Customers have been requesting this one for a long time, and we haven't had it in stock for years due to it being out of print. Any chance you might have 7 of them? Thanks!
` (delimiter is '/t/';
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ISBNCode1
- ISBNCode2
- ISBNCode3

Results table

| ISBNCode1 | ISBNCode2 | ISBNCode3 |
| --- | --- | --- |
| 301 | 487 | 588 |

## Example 2 – chart expression to identify contacts with secondary phone numbers

Chart expression and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table named BusinessContactInfo, which contains information about companies that was found on each company's website.
- ContactInfo is a field that contains company phone numbers. We want to determine which companies have multiple phone numbers available.

Our requirements:

- Phone numbers must be NANP phone numbers with 10 digits.
- We want to allow the area code to be enclosed in brackets.
- We want to allow a single blank space or hyphen between each segment of a phone number.

Load script

```
BusinessContactInfo:

Load * Inline `
ID	CompanyName	ContactInfo
1	Company A	(123) 456-7890 (023) 123-4567
2	Company B	0123456790 1357913579 0246802468
3	Company C	234-567-8901

` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CompanyName

Add this calculated dimension to the table:

```
=if(IndexRegEx(ContactInfo, '\({0,1}[0-9]{3}\){0,1}[ -]{0,1}[0-9]{3}[ -]{0,1}[0-9]{4}', 2)=0, 'No secondary phone number(s)', 'Has secondary phone number(s)')
```

Results table

| CompanyName | =if(IndexRegEx(ContactInfo, '\({0,1}[0-9]{3}\){0,1}[ -]{0,1}[0-9]{3}[ -]{0,1}[0-9]{4}', 2)=0, 'No secondary phone number(s)', 'Has secondary phone number(s)') |
| --- | --- |
| Company A | Has secondary phone number(s) |
| Company B | Has secondary phone number(s) |
| Company C | No secondary phone number(s) |

Company A has one secondary phone number. Company B has two secondary phone numbers. Company C has three secondary phone numbers.

Information noteThe MatchRegEx() function is also useful for these types of validation use cases.

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](../regular-expressions-qlik-analytics.htm)
