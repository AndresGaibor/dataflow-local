---
title: "MatchRegEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/MatchRegEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# MatchRegEx Script and chart function

MatchRegEx() compares an input string (text) with one or more regular expressions (regex). It returns the numeric location of the regular expression patterns that match. Returns a match response only if the evaluation of the regular expression matches the entire text input. If no matches are found, the function returns 0.

This function performs regex operations that are case-sensitive. You can alternatively use the variant MatchRegExI() to perform case-insensitive regex operations.

Syntax:

MatchRegEx
(text, regex1 [ , regex2,...regexN])

Return data type: integer

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text to which you want to match one or more regular expressions. For a match to occur, this input string needs to be an exact match with the regex pattern. |
| regex | The regular expression to try to match to the input string. You can specify more than one regular expression in a single expression, separated as subsequent arguments. |

Function examples

| Example | Result |
| --- | --- |
| `MatchRegEx('testSample','test')` | Returns `0` . The function only returns a match response when there is an exact match between text and the regex pattern. Even though `testSample` contains `test`, it contains other text (`Sample`), preventing an exact match. |
| `MatchRegEx('abc123','[a-z]','[0-9]','[a-z]+[0-9]+','.+')` | Returns `3` .The third regex pattern is the first to match the data. |
| `MatchRegEx('ABC','[abc]+','[123]')` | Returns `0`, because MatchRegEx() is case-sensitive. |
| `MatchRegExI('ABC','[abc]+','[123]')` | Returns `1` .The case-insensitive variant of the function, MatchRegExI(), is used. |

## When to use MatchRegEx

Use cases for this function include:

- Validating text to meet formatting and compliance standards, and to identify errors in data.
- Identifying differences in how text is formatted. For example, you can identify how many phone numbers use format A, format B, and so on.

## Example 1 – load script to analyze phone number formats

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table `BusinessContactInfo` containing contact phone numbers for various businesses. The phone numbers are 10-digit NANP phone numbers.
- A calculated field, `PhoneNumberFormat`, to assess whether each phone number matches one of a specific set of phone number formats.

There are three different formats that we want to check for: (###) ###-####, ###-###-####, and ##########.

Load script

```
BusinessContactInfo:

Load MatchRegEx(ContactInfo,'\({0,1}[0-9]{3}\) [0-9]{3}-[0-9]{4}', '[0-9]{3}-[0-9]{3}-[0-9]{4}', '[0-9]{10}') as PhoneNumberFormat,
* Inline `
ID	CompanyName	ContactInfo
1	Company A	(123) 456-7890
2	Company B	0123456790
3	Company C	234-567-8901
4	Company D	(024) 680-2456
5	Company E	(135) 791-3579
6	Company F	8901234567
7	Company G	235-235-2352
8	Company H	(555) (555) (5555)
9	Company I	2342342343
10	Company J	444-444-4444
` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `CompanyName`
- `ContactInfo`
- `PhoneNumberFormat`

Results table

| CompanyName | ContactInfo | PhoneNumberFormat |
| --- | --- | --- |
| Company A | (123) 456-7890 | 1 |
| Company B | 0123456790 | 3 |
| Company C | 234-567-8901 | 2 |
| Company D | (024) 680-2456 | 1 |
| Company E | (135) 791-3579 | 1 |
| Company F | 8901234567 | 3 |
| Company G | 235-235-2352 | 2 |
| Company H | (555) (555) (5555) | 0 |
| Company I | 2342342343 | 3 |
| Company J | 444-444-4444 | 2 |

From here, for example, you could create KPIs to calculate the total count of each phone number format, as well as the number of phone numbers that do not have a recognized format:

Examples of aggregation expressions to count occurrences of each format

| Format | Number of instances | Chart expression |
| --- | --- | --- |
| (###) ###-#### | 3 | =Count({<PhoneNumberFormat={'1'}>} PhoneNumberFormat) |
| ###-###-#### | 3 | =Count({<PhoneNumberFormat={'2'}>} PhoneNumberFormat) |
| ########## | 3 | =Count({<PhoneNumberFormat={'3'}>} PhoneNumberFormat) |
| Unrecognized format | 1 | =Count({<PhoneNumberFormat={'0'}>} PhoneNumberFormat) |

## Example 2 – chart expression to identify ISBN format

Chart expression and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table `Books` listing ISBN codes for various books.

From this data, we want to identify whether each ISBN code is a valid 10-digit or 13-digit code, based on syntax specified in a regex pattern.

Load script

```
Books:

Load * Inline [
Book
ISBN 123-3-1234-1234-0
ISBN 012-2-0123-0123-4
ISBN 000-1-0123-0123-2
ISBN 0-111-23456-7
ISBN 555-2-5555-5555-3
ISBN 222-4-2222-2222-2
ISBN 1-901-23456-8
ISBN 333-3-3333-3333-3
ISBN 555-1-5151-5151-3
ISBN 232-1-2323-2323-1
ISBN 2-444-44444-4
ISBN 888-0-9999-0000-0
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- `Book`

Add this calculated dimension, and give it the label ISBN Format:

```
=if(MatchRegEx(Book, 'ISBN[ ]*([0-9]{3})-([0-9]{1})-([0-9]{4})-([0-9]{4})-([0-9]{1})', 'ISBN[ ]*([0-9]{1})-([0-9]{3})-([0-9]{5})-([0-9]{1})')=1, '13-digit', 
	if(MatchRegEx(Book, 'ISBN[ ]*([0-9]{3})-([0-9]{1})-([0-9]{4})-([0-9]{4})-([0-9]{1})', 'ISBN[ ]*([0-9]{1})-([0-9]{3})-([0-9]{5})-([0-9]{1})')=2, '10-digit',
		'Invalid ISBN'))
```

Results table

| Book | ISBN Format |
| --- | --- |
| ISBN 000-1-0123-0123-2 | 13-digit |
| ISBN 0-111-23456-7 | 10-digit |
| ISBN 1-901-23456-8 | 10-digit |
| ISBN 2-444-44444-4 | 10-digit |
| ISBN 012-2-0123-0123-4 | 13-digit |
| ISBN 123-3-1234-1234-0 | 13-digit |
| ISBN 222-4-2222-2222-2 | 13-digit |
| ISBN 232-1-2323-2323-1 | 13-digit |
| ISBN 333-3-3333-3333-3 | 13-digit |
| ISBN 555-1-5151-5151-3 | 13-digit |
| ISBN 555-2-5555-5555-3 | 13-digit |
| ISBN 888-0-9999-0000-0 | 13-digit |

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm)
