---
title: "What is Backus-Naur formalism?"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Backus-Naur-formalism.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script syntax overview"]
---

# What is Backus-Naur formalism?

The Qlik Sense command line syntax and script
syntax are described in a notation called Backus-Naur formalism, also known as
BNF code.

The following table provides a list of symbols used in BNF code, with a description of how they are interpreted:

Symbols

| Symbol | Description |
| --- | --- |
| | | Logical OR: the symbol on either side can be used. |
| ( ) | Parentheses defining precedence: used for structuring the BNF syntax. |
| [ ] | Square brackets: enclosed items are optional. |
| { } | Braces: enclosed items may be repeated zero or more times. |
| Symbol | A non-terminal syntactic category, that: can be divided further into other symbols. For example, compounds of the above, other non-terminal symbols, text strings, and so on. |
| ::= | Marks the beginning of a block that defines a symbol. |
| LOAD | A terminal symbol consisting of a text string. Should be written as it is into the script. |

All terminal symbols are printed in a bold
face font. For example, "(" should be interpreted as a parenthesis
defining precedence, whereas "("
should be interpreted as a character to be printed in the script.

Example:

The description of the alias statement is:

alias fieldname as aliasname
{ , fieldname as aliasname}

This should be interpreted as the text string "alias", followed
by an arbitrary [field](#glossary-0 "Glossary term") name, followed by the text string "as",
followed by an arbitrary alias name. Any number of additional combinations
of "fieldname as alias" may be given,
separated by commas.

The following statements are correct:

alias a
as first;

alias a
as first, b as second;

alias a
as first, b as second, c as third;

The following statements are not
correct:

alias a
as first b as second;

alias
a as first { , b as second };
