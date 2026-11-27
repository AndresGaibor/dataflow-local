---
title: "ExtractRegExGroup Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ExtractRegExGroup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# ExtractRegExGroup Script and chart function

Expand/Collapse all

# ExtractRegExGroup Script and chart function

ExtractRegExGroup() extracts text from an input string expression using the composite regular expression pattern that is specified. When using the function, specify the group to use within the composite regex. The function returns a null value if no matches are found.

If you use the ExtractRegExGroup() function in a LOAD statement and field\_no is omitted, then the function will return multiple records. If several fields are loaded using ExtractRegExGroup(), the Cartesian products of all combinations are created.

This function performs regex operations that are case-sensitive. You can alternatively use the variant ExtractRegExGroupI() to perform case-insensitive regex operations.

Syntax:

ExtractRegExGroup
(text, regex, group [, field\_no])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | String expression containing the text to be extracted in the return value. |
| regex | The regular expression to use for extracting text. |
| group | The number of the group, in the case of a composite regular expression.  If the regular expression only contains one group, use the ExtractRegEx() function instead. Alternatively, use ExtractRegExGroup() with a group value of 0.  You can specify a negative group value to search for matches from right to left. |
| field\_no | The number of the match to extract. This is useful when multiple matches for the regular expression might be found in the text. For example, specify a value of 4 to extract the fourth match.  This is an optional argument. Default is 1 if not specified. |

Function examples

| Example | Result |
| --- | --- |
| ExtractRegExGroup('abc123 def456','([a-z]+)([0-9]+)',1) | Returns abc (first group of first match). |
| ExtractRegExGroup('abc123 def456','([a-z]+)([0-9]+)',1,2) | Returns def (first group of second match). |
| ExtractRegExGroup('abc123 def456','([a-z]+)([0-9]+)',2) | Returns 123 (second group of first match). |
| ExtractRegExGroup('abc123 def456','([a-z]+)([0-9]+)',2,2) | Returns 456 (second group of second match). |

## When to use ExtractRegExGroup

You can use Extract RegEx() to extract information that you want to isolate from data that might also contain other information (for example, free text or JSON strings). For example:

- Extract email addresses, telephone numbers, account numbers, and other information from text.
- Extract numeric values from text (for example, currency).
- Standardize formatting of text or numeric data.

## Example 1 – load script to parse transaction codes

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table named Transactions, which contains information about transactions. Certain details are captured with transaction codes using the following syntax:

  Transaction year-Transaction source (that is, online or in-store purchase)-Associated distribution center
- The creation of several new fields to extract each detail, each reusing the same composite regular expression.

Our requirements:

- The year can be any combination of four numbers.
- The values ONLINE and INSTORE are the only acceptable values for transaction source.
- The distribution center has to have exactly five numbers.

Load script

```
Transactions:

Load
	recno() as RecordID,
	ExtractRegExGroup(TransactionCode,'([0-9]{4})-(ONLINE|INSTORE)-([0-9]{5})',0) as TransactionCode_Unparsed,
	ExtractRegExGroup(TransactionCode,'([0-9]{4})-(ONLINE|INSTORE)-([0-9]{5})',1) as TransactionYear,
	ExtractRegExGroup(TransactionCode,'([0-9]{4})-(ONLINE|INSTORE)-([0-9]{5})',2) as TransactionSource,
	ExtractRegExGroup(TransactionCode,'([0-9]{4})-(ONLINE|INSTORE)-([0-9]{5})',3) as TransactionDC,
* Inline `
TransactionCode, Category
2025-ONLINE-60019, Product A
2024-INSTORE-60020, Product B
2025-ONLINE-60018, Product C
2024-ONLINE-60020, Product A
2025-INSTORE-60019, Product B
2025-ONLINE-60017, Product D
`;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- RecordID
- TransactionCode
- TransactionCode\_Unparsed
- TransactionYear
- TransactionSource
- TransactionDC

Results table

| RecordID | TransactionCode | TransactionCode\_Unparsed | TransactionYear | TransactionSource | TransactionDC |
| --- | --- | --- | --- | --- | --- |
| 1 | 2025-ONLINE-60019 | 2025-ONLINE-60019 | 2025 | ONLINE | 60019 |
| 2 | 2024-INSTORE-60020 | 2024-INSTORE-60020 | 2024 | INSTORE | 60020 |
| 3 | 2025-ONLINE-60018 | 2025-ONLINE-60018 | 2025 | ONLINE | 60018 |
| 4 | 2024-ONLINE-60020 | 2024-ONLINE-60020 | 2024 | ONLINE | 60020 |
| 5 | 2025-INSTORE-60019 | 2025-INSTORE-60019 | 2025 | INSTORE | 60019 |
| 6 | 2025-ONLINE-60017 | 2025-ONLINE-60017 | 2025 | ONLINE | 60017 |

These results highlight how the group argument allows you to reuse a single regex for multiple operations. The TransactionCode\_Unparsed field, which uses a group value of 0, does not provide any additional value in this case, but is shown here for the purpose of demonstrating the function.

## Example 2 – load script to extract business contact information

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table named BusinessContactInfo, which contains information about companies that was found on each company's website.
- ContactInfo is a field that contains free text, including company email addresses and phone numbers.
- The creation of several new fields to extract each detail, each reusing the same composite regular expression.

Our requirements:

- Email addresses must meet a specific set of requirements and syntax.
- Phone numbers must be NANP phone numbers with 10 digits. We want to allow the area code to be enclosed in brackets, and to allow blank spaces and hyphens at certain points.

Load script

```
BusinessContactInfo:

Load
	ExtractRegExGroupI(ContactInfo, '([a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']+@[a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']{1,50}\.[a-zA-Z0-9!#$%^&*\-_+=~{|}\/.'']{1,50})|(\({0,1}[0-9]{3}\){0,1}[ -]*[0-9]{3}[ -]*[0-9]{4})',1,1) as CompanyEmail,
	ExtractRegExGroupI(ContactInfo, '([a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']+@[a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']{1,50}\.[a-zA-Z0-9!#$%^&*\-_+=~{|}\/.'']{1,50})|(\({0,1}[0-9]{3}\){0,1}[ -]*[0-9]{3}[ -]*[0-9]{4})',2,2) as CompanyPhoneNum,
* Inline `
ID	CompanyName	ContactInfo
1	Company A	Email is: Company1@example.com, Phone number is: (123) 456-7890
2	Company B	Email is: company2@test.com, Phone # is: 0123456790
3	Company C	Email is: company3@placeholder.com, Phone no. is: 234-567-8901

` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- CompanyName
- CompanyEmail
- CompanyPhoneNum

Results table

| CompanyName | CompanyEmail | CompanyPhoneNum |
| --- | --- | --- |
| Company A | Company1@example.com | (123) 456-7890 |
| Company B | company2@test.com | 0123456790 |
| Company C | company3@placeholder.com | 234-567-8901 |

The same composite regular expression is reused to retrieve different information. The group argument specifies which of the two groups of the regular expression to search, and the field\_no argument specifies which overall match (across the entire string) that we want to find.

The ExtractRegEGroupxI() variant of the function ensures case-insensitive searches.

## Example 3 – load script to extract components from ISBN codes

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- The creation of a [variable](#glossary-0 "Glossary term"), ISBN\_RegEx, to store the regular expression we want to use for all extractions.
- A set of ISBN codes for books that a book store wants to order from several suppliers.

We need to extract the following from each ISBN code:

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
ExtractRegExGroup(Books,'$(ISBN_RegEx)',1) AS EAN,
ExtractRegExGroup(Books,'$(ISBN_RegEx)',2) AS Group,
ExtractRegExGroup(Books,'$(ISBN_RegEx)',3) AS Registrant,
ExtractRegExGroup(Books,'$(ISBN_RegEx)',4) AS Publication,
ExtractRegExGroup(Books,'$(ISBN_RegEx)',5) AS Checksum;
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
| Supplier 1 | 000 | 1 | 0123 | 0123 | 2 |
| Supplier 1 | 012 | 2 | 0123 | 0123 | 4 |
| Supplier 1 | 123 | 3 | 1234 | 1234 | 0 |
| Supplier 1 | 222 | 4 | 2222 | 2222 | 2 |
| Supplier 1 | 234 | 5 | 2345 | 2345 | 1 |
| Supplier 1 | 555 | 2 | 5555 | 5555 | 3 |
| Supplier 2 | 000 | 0 | 3333 | 3333 | 3 |
| Supplier 2 | 008 | 0 | 7777 | 7777 | 3 |
| Supplier 2 | 232 | 1 | 2323 | 2323 | 1 |
| Supplier 2 | 333 | 3 | 3333 | 3333 | 3 |
| Supplier 2 | 555 | 1 | 5151 | 5151 | 3 |
| Supplier 2 | 888 | 0 | 9999 | 0000 | 0 |

## Example 4 – chart expressions to extract business contact information (with ExtractRegEx() comparison)

Chart expressions and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table named BusinessContactInfo, which contains information about companies that was found on each company's website.
- ContactInfo is a field that contains free text, including company email addresses and phone numbers. We want to extract each email address and phone number with chart expressions.

Our requirements:

- Email addresses must meet a specific set of requirements and syntax.
- Phone numbers must be NANP phone numbers with 10 digits. We want to allow the area code to be enclosed in brackets, and to allow blank spaces and hyphens at certain points.

Load script

```
BusinessContactInfo:

Load * Inline `
ID	CompanyName	ContactInfo
1	Company A	Email is: Company1@example.com, Phone number is: (123) 456-7890
2	Company B	Email is: company2@test.com, Phone # is: 0123456790
3	Company C	Email is: company3@placeholder.com, Phone no. is: 234-567-8901

` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- CompanyName

Add the following calculated dimensions to the table:

- ```
  =ExtractRegExGroupI(ContactInfo, '([a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']+@[a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']{1,50}\.[a-zA-Z0-9!#$%^&*\-_+=~{|}\/.'']{1,50})|(\({0,1}[0-9]{3}\){0,1}[ -]*[0-9]{3}[ -]*[0-9]{4})',1,1)
  ```
- ```
  =ExtractRegExGroupI(ContactInfo, '([a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']+@[a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']{1,50}\.[a-zA-Z0-9!#$%^&*\-_+=~{|}\/.'']{1,50})|(\({0,1}[0-9]{3}\){0,1}[ -]*[0-9]{3}[ -]*[0-9]{4})',2,2)
  ```

Results table

| CompanyName | =ExtractRegExGroupI(ContactInfo, '([a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']{1,50}\.[a-zA-Z0-9!#$%^&\*\-\_+=~{|}\/.'']{1,50})|(\({0,1}[0-9]{3}\){0,1}[ -]\*[0-9]{3}[ -]\*[0-9]{4})',1,1) | =ExtractRegExGroupI(ContactInfo, '([a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']{1,50}\.[a-zA-Z0-9!#$%^&\*\-\_+=~{|}\/.'']{1,50})|(\({0,1}[0-9]{3}\){0,1}[ -]\*[0-9]{3}[ -]\*[0-9]{4})',2,2) |
| --- | --- | --- |
| Company A | Company1@example.com | (123) 456-7890 |
| Company B | company2@test.com | 0123456790 |
| Company C | company3@placeholder.com | 234-567-8901 |

The same composite regular expression is reused to retrieve different information. The group argument specifies which of the two groups of the regular expression to search, and the field\_no argument specifies which overall match (across the entire string) that we want to find.

The ExtractRegEGroupI() variant of the function ensures case-insensitive searches.

## Example 5 – URL parsing (with ExtractRegEx() comparison)

Chart expressions and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table named Correspondence, which contains email message text in a field named EmailBody.
- Email message content that contains web URLs.

We want to extract the second URL, if present, into the following components:

- Full URL
- Protocol
- Domain
- Path

We want to use a single regular expression to control all extraction.

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

- URL 2:

  ```
  =ExtractRegEx(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',2)
  ```
- URL 2 Protocol:

  ```
  =ExtractRegExGroup(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',1,2)
  ```
- URL 2 Domain:

  ```
  =ExtractRegExGroup(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',2,2)
  ```
- URL 2 Path:

  ```
  =ExtractRegExGroup(EmailBody,'([a-zA-Z0-9]+):\/\/(([a-zA-Z0-9]+\.)*([a-zA-Z0-9]+)\.([a-zA-Z0-9]+))((\/[a-zA-Z0-9]+)*(\/([a-zA-Z0-9]+)(\.[a-zA-Z0-9]+)?))?',6,2)
  ```

Results table

| ID | URL 2 | URL 2 Protocol | URL 2 Domain | URL 2 Path |
| --- | --- | --- | --- | --- |
| 1 | http://www.example.ca/training1.pptx | http | www.example.ca | /training1.pptx |
| 2 | - | - | - | - |
| 3 | https://www.examplestore2.com/products | https | www.examplestore2.com | /products |

ExtractRegEx() returns the entire URL, while ExtractRegExGroup() returns individual parts of the URL, corresponding to the group value we used. The record with an ID value of 2 only contains one URL, so no data is returned for it.

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
