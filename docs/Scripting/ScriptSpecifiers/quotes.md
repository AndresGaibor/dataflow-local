---
title: "Quotes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/quotes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load", "Format specification items"]
---

# Quotes

Quotes is a file specifier for the LOAD statement that defines whether quotes can be used and the precedence between quotes and separators. For text files only.

Syntax:

no quotes

msq

If the specifier is omitted, standard quoting is used, that is, the quotes " " or ' ' can be used, but only if they are the first and last non blank character of a [field](#glossary-0 "Glossary term") value.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| no quotes | Used if quotation marks are not to be accepted in a text file. |
| msq | Used to specify modern style quoting, allowing multi-line content in fields. Fields containing end-of-line characters must be enclosed within double quotes.  One limitation of the msq option is that single double-quote (") characters appearing as first or last character in field content will be interpreted as start or end of multi-line content, which may lead to unpredicted results in the data set loaded. In this case you should use standard quoting instead, omitting the specifier. |

## Learn more

- [*Using quotation marks in the script*](../use-quotes-in-script.htm)
- [*Load*](../ScriptRegularStatements/Load.htm)
- [*Script regular statements*](../ScriptRegularStatements/script-regular-statements.htm)
- [*Example - Multi-line content*](../inline-loads-qs.htm#ExMultLine)
