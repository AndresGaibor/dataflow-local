---
title: "ExtractRegEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ExtractRegEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# ExtractRegEx Script and chart function

Expand/Collapse all

# ExtractRegEx Script and chart function

ExtractRegEx() extracts text from an input string expression using the specified regular expression pattern. The function returns a null value if no matches are found.

This function performs regex operations that are case-sensitive. You can alternatively use the variant ExtractRegExI() to perform case-insensitive regex operations.

Syntax:

ExtractRegEx
(text, regex [, field\_no])

Return data type:  string

Arguments

| Argument | Description |
| --- | --- |
| text | String expression containing the text to be extracted in the return value. |
| regex | The regular expression to use for extracting text. |
| field\_no | The number of the match to extract. This is useful when multiple matches for the regular expression might be found in the text. For example, specify a value of 4 to extract the fourth match. This is an optional argument. Specify a negative value to reverse the order of the matches.  The following apply regardless of whether the function is used in a load script or chart expression:   - If field\_no is positive, the function will return one value, identifying matches from left to right. - If field\_no is negative, the function will return one value, identifying matches from right to left.   When using the function in a [load script](#glossary-0 "Glossary term"):   - If you use the ExtractRegEx() function in a LOAD statement and field\_no is omitted, the function generates as many records as there are matches. - If several fields are loaded using ExtractRegEx() and none of them specify a field\_no argument, the Cartesian products of all combinations are created.   When using the function in a [chart](#glossary-1 "Glossary term") expression:   - If the field\_no is omitted, the default value is 1. |

Function examples

| Example | Result |
| --- | --- |
| ExtractRegEx('a,b c;1 2,3','[a-z]|[0-9]', 1) | Returns a, which is the first match found. |
| ExtractRegEx('a,b c;1 2,3','[a-z]|[0-9]', 2) | Returns b, which is the second match found. |
| ExtractRegEx('a,b c;1 2,3','[a-z]|[0-9]', 4) | Returns 1, which is the fourth match found. |
| ExtractRegEx('abc','a|b',-1) | Returns b. When a negative value is specified, matches are counted in reverse. |
| ExtractRegEx('A,B C;1 2,3','[a-c]|[4-9]') | Returns a null value, because ExtractRegEx() is case-sensitive, and the case-insensitive variant was not used. |
| ExtractRegExI('A,B C;1 2,3','[a-c]|[4-9]') | Returns A, because the case-insensitive variant ExtractRegExI() was used. |

## When to use ExtractRegEx

You can use Extract RegEx() to extract information that you want to isolate from data that might also contain other information (for example, free text or JSON strings). For example:

- Extract email addresses, telephone numbers, account numbers, and other information from text.
- Extract numeric values from text (for example, currency).
- Standardize formatting of text or numeric data.

## Example 1 – load script to extract email addresses from JSON

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table OrderDetails containing a field OrderJson.
- The field OrderJson contains a JSON string with order data. Formatting, such as indentation and line breaks, has been removed from the JSON. The order data contains email addresses that we want to extract into separate values.
- A new table EmailAddresses, which is loaded after OrderDetails. In the EmailAddresses LOAD statement, we load the OrderJson field from the OrderDetails table, and create a new calculated field, Email, which contains the extracted email addresses. OrderDetails is then dropped.

Our requirements:

- Email addresses in a specific domain: example.com.
- Email addresses that contain any number of alphanumeric characters, as well as a defined set of special characters.

Load script

```
OrderDetails:

Load * Inline `
OrderJson
{"Orders":[{"order_id":"12345","customer":{"name":"John Doe","email":"john.doe@example.com"},"items":{"product":"Laptop","quantity":2,"price":1200},"total_price":2400},{"order_id":"12346","customer":{"name":"Jane Doe","email":"jane.doe@example.com"},"items":{"product":"Tablet","quantity":4,"price":400},"total_price":1600},{"order_id":"12347","customer":{"name":"Amalia Craig","email":"amalia.craig@example.com"},"items":{"product":"Desktop Computer","quantity":1,"price":1900},"total_price":1900},{"order_id":"12348","customer":{"name":"Ken Roberts","email":"ken.roberts@example.com"},"items":{"product":"Phone Charger Cable","quantity":110,"price":1900},"total_price":1210}]}
` (delimiter is '\t');

EmailAddresses:

Load OrderJson, ExtractRegEx(OrderJson, '[a-zA-Z0-9!#$%^&*-_+=~{|}\/.'']+@example.com') as Email Resident OrderDetails;

Drop table OrderDetails;
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- Email

Results table

| Email |
| --- |
| amalia.craig@example.com |
| jane.doe@example.com |
| john.doe@example.com |
| ken.roberts@example.com |

By not specifying an argument value for field\_no, all matches are extracted into separate values automatically.

## Example 2 – load script to extract numeric values from currency amounts

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table Sales containing sales data.
- Within the Sales table, a field named Amount, which contains transaction amounts in USD. These amounts are expressed as strings, which include currency symbols and codes.
- The definition of a custom field within Sales, OrderAmountNumeric\_USD, which extracts each amount into a purely numeric value. This data needs to be in numeric form so that we can use it in chart aggregations.

Load script

```
SET DateFormat='MM-DD-YYYY';

Sales:

Load ExtractRegEx(Amount, '[0-9]+.[0-9]{2}') as OrderAmountNumeric_USD, * Inline `

OrderID, OrderDate, Product, Amount
1, '12-27-2024', Software, $100.31 USD
2, '12-28-2024', Electronics, $513.93 USD
3, '12-29-2024', Grocery, $34.66 USD
4, '12-30-2024', Furniture, $1124.58 USD
5, '12-31-2024', Software, $95.95 USD
6, '01-01-2025', Software, $601.00 USD
7, '01-02-2025', Grocery, $1534.20 USD
8, '01-03-2025', Produce, $51.49 USD
9, '01-04-2025', Home Improvement, $176.12 USD
10, '01-05-2025', Produce, $432.77 USD
11, '01-06-2025', Software, $270.01 USD
12, '01-07-2025', Electronics, $83.85 USD
13, '01-08-2025', Furniture, $65.65 USD
14, '01-09-2025', Electronics, $1526.39 USD
15, '01-10-2025', Software, $432.44 USD
16, '01-11-2025', Furniture, $888.15 USD
17, '01-12-2025', Furniture, $300.00 USD
18, '01-13-2025', Grocery, $109.53 USD
19, '01-14-2025', Furniture, $487.97 USD
20, '01-15-2025', Software, $65.09 USD
`;
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension:

- OrderID
- Amount
- OrderAmountNumeric\_USD

Results table

| OrderID | Amount | OrderAmountNumeric\_USD |
| --- | --- | --- |
| 1 | $100.31 USD | 100.31 |
| 2 | $513.93 USD | 513.93 |
| 3 | $34.66 USD | 34.66 |
| 4 | $1124.58 USD | 1124.58 |
| 5 | $95.95 USD | 95.95 |
| 6 | $601.00 USD | 601.00 |
| 7 | $1534.20 USD | 1534.20 |
| 8 | $51.49 USD | 51.49 |
| 9 | $176.12 USD | 176.12 |
| 10 | $432.77 USD | 432.77 |
| 11 | $270.01 USD | 270.01 |
| 12 | $83.85 USD | 83.85 |
| 13 | $65.65 USD | 65.65 |
| 14 | $1526.39 USD | 1526.39 |
| 15 | $432.44 USD | 432.44 |
| 16 | $888.15 USD | 888.15 |
| 17 | $300.00 USD | 300.00 |
| 18 | $109.53 USD | 109.53 |
| 19 | $487.97 USD | 487.97 |
| 20 | $65.09 USD | 65.09 |

## Example 3 – chart expressions to extract email addresses from JSON

Chart expressions and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table OrderDetails containing a field OrderJson.
- The field OrderJson contains a JSON string with order data. Formatting, such as indentation and line breaks, has been removed from the JSON. The order data contains email addresses that we want to extract into separate values.

Our requirements:

- Email addresses in a specific domain: example.com.
- Email addresses that contain any number of alphanumeric characters, as well as a defined set of special characters.

Load script

```
OrderDetails:

Load * Inline `
OrderJson
{"Orders":[{"order_id":"12345","customer":{"name":"John Doe","email":"john.doe@example.com"},"items":{"product":"Laptop","quantity":2,"price":1200},"total_price":2400},{"order_id":"12346","customer":{"name":"Jane Doe","email":"jane.doe@example.com"},"items":{"product":"Tablet","quantity":4,"price":400},"total_price":1600},{"order_id":"12347","customer":{"name":"Amalia Craig","email":"amalia.craig@example.com"},"items":{"product":"Desktop Computer","quantity":1,"price":1900},"total_price":1900},{"order_id":"12348","customer":{"name":"Ken Roberts","email":"ken.roberts@example.com"},"items":{"product":"Phone Charger Cable","quantity":110,"price":1900},"total_price":1210}]}
` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a table and add each of the following expressions as calculated dimensions:

- =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',1)
- =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',2)
- =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',3)
- =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',4)

Results table

| =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',1) | =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',2) | =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',3) | =ExtractRegEx(OrderJson,'[a-zA-Z0-9!#$%^&\*-\_+=~{|}\/.'']+@example.com',4) |
| --- | --- | --- | --- |
| john.doe@example.com | jane.doe@example.com | amalia.craig@example.com | ken.roberts@example.com |

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](../regular-expressions-qlik-analytics.htm)
