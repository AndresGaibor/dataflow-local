---
title: "CountRegEx Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/CountRegEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "String functions"]
---
Expand/Collapse all

# CountRegEx Script and chart function

CountRegEx() returns the number of occurrences of the specified regular expression pattern in the input string text. If there is no match, 0 is returned.

This function performs regex operations that are case-sensitive. You can alternatively use the variant CountRegExI() to perform case-insensitive regex operations.

Syntax:

CountRegEx
(text, regex)

Return data type:  numeric

Arguments

| Argument | Description |
| --- | --- |
| text | The input string text within which you want to search for a regular expression. |
| regex | The regular expression pattern to search for. |

Function examples

| Example | Result |
| --- | --- |
| `CountRegEx('abc123','[a-z]')` | Returns `3`. |
| `CountRegEx('abc123','[a-z][0-9]')` | Returns `1`. |
| `CountRegEx('abc123','[0-9]')` | Returns `3`. |
| `CountRegEx('ABC','[a-z]{3}')` | Returns `0`. |
| `CountRegExI('ABC','[a-z]{3}')` | Returns `1`. Because the CountRegExI() variant is used, text searches are not case-sensitive. |

## When to use CountRegEx

Examples of use cases for CountRegEx() include:

- Counting the number of times a particular text pattern occurs within a string. For example, you could search for instances of email addresses, telephone numbers, and other information within documents and email messages.
- Validating whether data matches a specific syntax requirement. For example, you could identify occurrences of error in data entry.

## Example 1 – load script to count valid year ranges

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A tabled named `Vehicles` containing a list of vehicles, along with the condition and model year of each vehicle.
- For each record in `Vehicles`, a calculation to determine whether the year range for the vehicle meets the expected syntax. Valid year ranges include 1990s, 2000s, 2010s, and 2020s. This calculation is performed using the CountRegEx() function.

Load script

```
Vehicles:
Load CountRegEx(Model_YearRange, '(^19[0-9][0-9]s$)|(^20[0-9][0-9]s$)') as Valid_Year_Data,
* Inline [
Vehicle_ID, Condition, Model_YearRange
1, Good,20100s
2,Fair,2020s
3, Poor,2020s
4, Good,210s
5, Excellent,2000s
6, Excellent,2020s
7, Excellent,202s
8, Good,2010s
9, Poor,2010ss
10, Poor,1990s
];
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `Vehicle_ID`
- `Valid_Year_Data`

Results table

| Vehicle\_ID | Valid\_Year\_Data |
| --- | --- |
| 1 | 0 |
| 2 | 1 |
| 3 | 1 |
| 4 | 0 |
| 5 | 1 |
| 6 | 1 |
| 7 | 0 |
| 8 | 1 |
| 9 | 0 |
| 10 | 1 |

You can also add a KPI to the sheet, and add this [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/CountRegEx.htm#glossary-0 "Glossary term"):

```
Sum(Valid_Year_Data)
```

This chart shows the total number of records with valid Model\_YearRange values.

> **Note:** The MatchRegEx() function is also useful for these types of validation use cases.

## Example 2 – load script to count number of email addresses in text strings

Load script and results

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A tabled named `Employees` containing data about a company's employees. All email address for each employee are contained within a single string.
- The creation of a field, `NoOfEmails`, to calculate how many email addresses are contained within the input string for each employee.

Load script

```
Employees:

Load CountRegExI(Emails, '@[a-zA-Z0-9.-]*\.?[a-zA-Z0-9]*\.com') as NoOfEmails,
* Inline `
ID	Emails
1	john_doe@test.com john_michael_doe@example.com j.doe123@example123.com
2	jane_doe@test.com
3	Michael_Andrews@test.com Michael_John_Andrews@example.com
4	charlie_kent@support.test.com charlie_peter_kent@support.example.com cp.kent.1985@test123.com c_p_kent@test123.com
5	frances_johnson@test.com frances_johnson@example.com
6	rebecca_smith@hr.test.com
` (delimiter is '\t');
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `Emails`
- `NoOfEmails`

Results table

| ID | Emails | NoOfEmails |
| --- | --- | --- |
| 1 | john\_doe@test.com john\_michael\_doe@example.com j.doe123@example123.com | 3 |
| 2 | jane\_doe@test.com | 1 |
| 3 | Michael\_Andrews@test.com Michael\_John\_Andrews@example.com | 2 |
| 4 | charlie\_kent@support.test.com charlie\_peter\_kent@support.example.com cp.kent.1985@test123.com c\_p\_kent@test123.com | 4 |
| 5 | frances\_johnson@test.com frances\_johnson@example.com | 2 |
| 6 | rebecca\_smith@hr.test.com | 1 |

## Example 3 – chart expression to count occurrences of string

Chart expression and results

Overview

Open the Data load editor and add the following load script to a new section.

The load script contains the text from a number of corporate correspondences that were sent out to employees of an organization. The data has already been cleansed of any personal identifiable information (PII), other than the company name and the email address that sent each correspondence. The body of each message has been collapsed into a single continuous string. In other words, all formatting and newline characters have been removed.

Our requirements:

- Identify which messages contain a string that includes the email address TestCompanyNameCorrespondence@test.com, along with a specific introduction to this address that indicates that it was the sender.
- We want flexibility in which introductions to identify, but also to still have some definite restrictions. The introductions `Sender` and `Sent by` are both considered valid. To achieve this goal, regex patterns can be used.
- Case sensitivity of email addresses is not a factor. Therefore, the search should be case-insensitive.

Load script

```
Correspondences:
Load * Inline [
ID|MessageBody
1|Sent by-- TestCompanyNameCorrespondence@test.com Good morning TestCompanyName team! I hope you are all well. I am just reaching out about the fabulous benefits package we launched just year. Our goal is to take a poll of what you all think. Can you please rate the new options from 1-10 in a response to this email, by this Tuesday? Thank you! 
2|Sender: TestCompanyNameIT@test.com Did you know you can access our IT portal anytime, from any of your company devices? It's true! Reach out to your team lead to learn more.
3|Sender: TESTCOMPANYNAMECORRESPONDENCE@test.COM URGENT: This is a message to inform employees of an ongoing issue with our local branch. The branch will be closed until further notice. Thank you
4|Sender: TestCompanyNameVolunteering@test.com Dear team! We are looking for volunteers to help with this year's charity event! We need 40 volunteers to help with the event. If you are interested, please send an email to your direct supervisor. Thanks, TestCompanyName team members, for helping make the world a better place!
5|Sender is TestCompanyNameCorrespondence@test.com Hi folks, it's time to announce the annual TestCompanyName staff party! The party will be taking place at the office this year. Please make sure to RSVP, and we hope to see you there! Sincerely, the TestCompanyName management team
] (delimiter is |);
```

Results

Load the data and open a sheet. Create a new table and add these fields as dimensions:

- `ID`
- `MessageBody`

Add the following measure:

```
=CountRegExI(MessageBody,'(Sender.*TestCompanyNameCorrespondence@test.com)|(Sent by.*TestCompanyNameCorrespondence@test.com)')
```

In the measure properties, set **Totals function** to **Sum**. This configures the totals row at the top of the table to count the total number of records that contribute to the count.

The measure counts the number of matches for the specified regex pattern within the message content. In the regex pattern, `.*` indicates any number of any character except newline characters. The pattern also accounts for variation in how the email address is introduced: both `Sender` and `Sent by` are valid matches. The CountRegExI() variant of the function ensures case-insensitive searches.

Results table

| ID | MessageBody | =CountRegExI(MessageBody,'(Sender.\*TestCompanyNameCorrespondence@test.com)|(Sent by.\*TestCompanyNameCorrespondence@test.com)') |
| --- | --- | --- |
| **Totals** | - | **3** |
| 1 | Sent by-- TestCompanyNameCorrespondence@test.com Good morning TestCompanyName team! I hope you are all well. I am just reaching out about the fabulous benefits package we launched just year. Our goal is to take a poll of what you all think. Can you please rate the new options from 1-10 in a response to this email, by this Tuesday? Thank you! | 1 |
| 2 | Sender: TestCompanyNameIT@test.com Did you know you can access our IT portal anytime, from any of your company devices? It's true! Reach out to your team lead to learn more. | 0 |
| 3 | Sender: TESTCOMPANYNAMECORRESPONDENCE@TEST.COM URGENT: This is a message to inform employees of an ongoing issue with our local branch. The branch will be closed until further notice. Thank you | 1 |
| 4 | Sender: TestCompanyNameVolunteering@test.com Dear team! We are looking for volunteers to help with this year's charity event! We need 40 volunteers to help with the event. If you are interested, please send an email to your direct supervisor. Thanks, TestCompanyName team members, for helping make the world a better place! | 0 |
| 5 | Sender is TestCompanyNameCorrespondence@test.com Hi folks, it's time to announce the annual TestCompanyName staff party! The party will be taking place at the office this year. Please make sure to RSVP, and we hope to see you there! Sincerely, the TestCompanyName management team | 1 |

Across the five messages, there are three that match the specified regex pattern. Each message contains one match.

> **Note:** The MatchRegEx() function is also useful for these types of validation use cases.

## Learn more

- [*Working with regular expressions in load scripts and chart expressions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/regular-expressions-qlik-analytics.htm)
