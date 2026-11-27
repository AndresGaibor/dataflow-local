---
title: "SubFieldRegEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubFieldRegEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---

# SubFieldRegEx Script and chart function

Expand/Collapse all

# SubFieldRegEx Script and chart function

SubFieldRegEx() extracts text from an input string expression, using the specified regular expression pattern as a delimiter. The function returns a null value if no matches are found.

This function performs regex operations that are case-sensitive. You can alternatively use the variant SubFieldRegExI() to perform case-insensitive regex operations.

Syntax:

SubFieldRegEx
(text, regex\_delimiter [, field\_no])

Return data type: string

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text within which you want to search for a regular expression pattern. |
| regex\_delimiter | String expression containing the regular expression to use as a delimiter. You can specify more than one delimiter in the same regular expression pattern by separating them with a | (vertical pipe) character. |
| field\_no | Integer value indicating the number of the subdivision you want to extract. For example, specify a value of 4 to extract the fourth subdivision. This is an optional argument.  The following apply regardless of whether the function is used in a load script or chart expression:   - If field\_no is positive, the function will return one value, identifying matches from left to right. - If field\_no is negative, the function will return one value, identifying matches from right to left.   When using the function in a [load script](#glossary-0 "Glossary term"):   - If you use the SubFieldRegEx() function in a LOAD statement and field\_no is omitted, the function generates as many records as there are matches. - If several fields are loaded using SubFieldRegEx() and none of them specify a field\_no argument, the Cartesian products of all combinations are created.   When using the function in a [chart](#glossary-1 "Glossary term") expression:   - If the field\_no is omitted, the default value is 1. |

Function examples

| Example | Result |
| --- | --- |
| SubFieldRegEx('a,b c;1 2,3',' |,|;', 1) | Returns a. In this example, three delimiter characters are specified (space, comma, and semicolon). |
| SubFieldRegEx('a;b;c;1;2;3',';', 2) | Returns b. In this case, only one delimiter character is specified (semicolon). |
| SubFieldRegEx('a,b c;1 2,3',' |,|;', 4) | Returns 1. |

## When to use SubFieldRegEx

You can use SubFieldRegEx() to extract multiple individual values from a delimited list. For example, if you have a comma-separated list contained within a larger block of natural language, you can use this function to isolate each individual value from the list into a new record in your data model.

## Example 1 – load script to separate tags by transaction

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table Transaction\_By\_Tag, which initially contains transaction data. This data is processed to extract individual tag values into new records.
- The creation of a field, TransactionTag, to store the extracted tag values.

In the field containing the transaction tags, multiple tags are contained within text strings, separated by delimiters. The delimiter could be any of the following characters: , | ;

Load script

```
Transaction_By_Tag:

Load SubFieldRegEx(Tags, ',|;|\|') as TransactionTag,
* Inline [
ID	Product	Tags	Amount
1	Product A	Special order,Eligible for return,Warranty included	100.93
2	Product B	Ineligible for return|No warranty available	51.11
3	Product C	No warranty available	12.83
4	Product B	Special order;Liquidation sale;Warranty included	209.48
] (delimiter is '\t');

drop fields Tags;
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ID
- Product
- TransactionTag

Results table

| ID | Product | TransactionTag |
| --- | --- | --- |
| 1 | Product A | Eligible for return |
| 1 | Product A | Warranty included |
| 1 | Product A | Special order |
| 2 | Product B | No warranty available |
| 2 | Product B | Ineligible for return |
| 3 | Product C | No warranty available |
| 4 | Product B | Liquidation sale |
| 4 | Product B | Special order |
| 4 | Product B | Warranty included |

This example demonstrates that when used in a load script, SubFieldRegEx() returns a separate row for each match found in the input string.

## Example 2 – chart expressions to separate tags by transaction

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A table Transaction\_By\_Tag, which contains transaction data.
- A field, Tags, that contains text strings to store all tags associated with a transaction.

Our requirements:

- In the field containing the transaction tags, multiple tags are contained within text strings, separated by delimiters. The delimiter could be any of the following characters: , | ;
- We want to use chart expressions to separate each tag into its own field, with up to three tags possible to add to a transaction.

Load script

```
Transaction_By_Tag:

Load * Inline [
ID	Product	Tags	Amount
1	Product A	Special order, Eligible for return, Warranty included	100.93
2	Product B	Ineligible for return | No warranty available	51.11
3	Product C	No warranty available	12.83
4	Product B	Special order;Liquidation sale;Warranty included	209.48
] (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- ID
- Tags

Add these calculated dimensions:

- =SubFieldRegEx(Tags, ',|;|\|', 1)
- =SubFieldRegEx(Tags, ',|;|\|', 2)
- =SubFieldRegEx(Tags, ',|;|\|', 3)

Results table

| ID | Tags | =SubFieldRegEx(Tags, ',|;|\|', 1) | =SubFieldRegEx(Tags, ',|;|\|', 2) | =SubFieldRegEx(Tags, ',|;|\|', 3) |
| --- | --- | --- | --- | --- |
| 1 | Special order, Eligible for return, Warranty included | Special order | Eligible for return | Warranty included |
| 2 | Ineligible for return | No warranty available | Ineligible for return | No warranty available | - |
| 3 | No warranty available | No warranty available | - | - |
| 4 | Special order;Liquidation sale;Warranty included | Special order | Liquidation sales | Warranty included |

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](../regular-expressions-qlik-analytics.htm)
