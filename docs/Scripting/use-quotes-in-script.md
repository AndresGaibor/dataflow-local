---
title: "Using quotation marks in the script"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-quotes-in-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures"]
---
# Using quotation marks in the script

You can use quotation marks in script statements in a number of different ways.

## Inside LOAD statements

In a LOAD
statement the following symbols should be used as quotation marks:

Field names

| Description | Symbol | Code point | Example |
| --- | --- | --- | --- |
| double quotation marks | " " | 34 | "string" |
| square brackets | [ ] | 91, 93 | [string] |
| grave accents | ` ` | 96 | `string` |

String literals

| Description | Symbol | Code point | Example |
| --- | --- | --- | --- |
| single quotation marks | ' ' | 39 | 'string' |

## In SELECT statements

For a SELECT
statement interpreted by an ODBC driver, usage may vary. Usually, you should use the straight double quotation marks (Alt + 0034) for [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-quotes-in-script.htm#glossary-0 "Glossary term") and table names, and the straight single
quotation marks (Alt + 0039) for literals, and avoid using grave accents. However, some ODBC drivers not only
accept grave accents as quotation marks, but also prefer them. In such a case, the generated SELECT
statements contain grave accent quotation marks.

### Microsoft Access quotation marks example

Microsoft Access ODBC Driver 3.4 (included in
Microsoft Access 7.0) accepts the following quotation marks when analyzing the SELECT
statement:

Field names and table names:

- [ ]
- " "
- ` `

String literals:

- ' '

Other databases may have different conventions.

## Outside LOAD statements

Outside a LOAD statement, in places where Qlik Sense expects an expression, double quotation marks denote a [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-quotes-in-script.htm#glossary-1 "Glossary term") reference and not a field reference. If you use double quotation marks, the enclosed string will be interpreted as a variable and the value of the variable will be used.

## Out-of-context field references and table references

Some script functions refer to fields that have already been created, or are in the output of a LOAD statement, for example Exists() and Peek(). These field references are called out-of-context field references, as opposed to source field references that refer to fields that are in context, that is, in the input table of the LOAD statement.

Out-of-context field references and table references should be regarded as literals and therefore need single quotation marks.

## Difference between names and literals

The difference between names and literals becomes clearer comparing
the following examples:

Example:

'Sweden' as Country

When this expression is used as a part of the field list in a LOAD
or SELECT statement, the text string "Sweden"
will be loaded as field value into the Qlik Sense field "Country".

Example:

"land"
as Country

When this expression is used as a part of the field list in a LOAD
or SELECT statement, the content of the database field or table column named "land"
will be loaded as field values into the Qlik Sense field "Country". This means that land will be treated as a field reference.

## Difference between numbers and string literals

The difference between numbers and string literals becomes clearer comparing the following examples.

Example:

'12/31/96'

When this string is used as a part of an expression, it will in a first step be interpreted as the text string "12/31/96", which in turn may be interpreted as a date if the date format is 'MM/DD/YY'. In that case it will be stored as a dual value with both a numeric and a textual representation.

Example:

12/31/96

When this string is used as a part of an expression, it will be interpreted numerically as 12 divided by 31 divided by 96.

## Using quotation marks in a string

When a string contains characters that can be used as quotation marks, it is important to clearly indicate where a string begins and where it ends when quoting the string. If the string is not properly quoted, the script will fail or it will load data incorrectly.

There are two methods for quoting a string that contains quotation marks.

### Use a specific quotation mark to quote the string

Choose a quotation mark that is not used inside the string, and use it to quote the entire string. Qlik Sense will use that specific quotation mark to determine where the string begins and ends.

Any of the following quotation marks can be used to quote the entire string:

- Double quotation marks " "
- Square brackets [ ]
- Grave accents ` `
- Single quotation marks ' '

Example:

[Table '1 "2"]

Square brackets are used to quote the string. The string loads as : Table '1 "2"

'string `Name1` "Name2'

Single quotation marks are used to quote the string. The string loads as: string `Name1` "Name2

### Use escape characters

Escape characters are an additional instance of the quotation mark that is used to quote the string. They must be added beside every instance of the quotation mark that appears within the string. When all quotation marks are used inside a string, you need to add escape characters beside the same type of quotation mark used to quote the string. Escape characters can also be used if you want to use a quotation mark that is already in use in a string.

Only the following marks can be used as escape characters:

- Double quotation marks " "
- Square brackets [ ]
- Single quotation marks ' '

Example:

"Michael said ""It's a beautiful day""."

If you quote the string using the double quotation marks " ", then you must add an extra double quotation mark beside every double quotation mark used inside the string.

This string is loaded as Michael said "It's a beautiful day". By using the escape character `""`, the Qlik Sense [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-quotes-in-script.htm#glossary-2 "Glossary term") understands which double quotation marks are part of the string and which quotation mark indicates the end of the string. The single quotation mark ' used in the abbreviation It's does not need to be escaped because it is not the mark used to quote the string.

Example:

'Michael said: "It''s a beautiful day".'

If you quote this string using single quotation marks, then you must add an extra single quotation mark beside each single quotation mark used inside the string.

This string is loaded as Michael said "It's a beautiful day". The double quotation mark " used for quoting what Michael said does not need to be escaped because it is not the mark used to quote the string.

Example:

[Michael said [It's a "beautiful day]].]

Square brackets [ ] behave differently from the other two quotation marks. If you want to use brackets as an escape character, you must add an extra bracket beside the right square bracket ] only, and not beside the left square bracket [.

This string is loaded as Michael said [It's a "beautiful day]. Only the right square bracket ] is escaped. The single quotation mark ' and the double quotation mark " used in the string do not need to be escaped as they are not used to quote the string.

## Learn more

- [*Load*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Load.htm)
- [*Select*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Select.htm)
- [*Script statements and keywords*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/script-statements-keywords.htm)
