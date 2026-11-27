---
title: "Regular expression functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regular-expressions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions"]
---

# Regular expression functions

This section describes the following regular expression functions:

| Function | Description |
| --- | --- |
| [REGEX\_EXTRACT](regexp_extract.htm) | Finds the first match of the regular expression pattern in string and returns the capturing group number requested |
| [REGEXP\_EXTRACT\_ALL](regexp_extract_all.htm) | Matches the regular expression on the input string. Returns the escape groups if any exist or the original string if none exists |
| [REGEXP\_LIKE](regexp_like.htm) | Evaluates the regular expression pattern and determines if it is contained within the string |
| [REGEX\_MATCH\_POSITION](regex_match_position.htm) | Matches the regular expression on the input string, and returns the index of the first match |
| [REGEX\_NAMED\_GROUPS](regex_named_groups.htm) | Matches the regular expression on the input string. Returns record with field names and group names |
| [REGEXP\_REPLACE](regexp_replace.htm) | Evaluates the regular expression pattern and replaces every instance found with the replacement |

## Regular expression patterns

The regular expression patterns used when performing RegEx pattern matches are described in the table below:

| Expression | Contact | Description |
| --- | --- | --- |
| Any character | . | Matches any single character except a line break. |
| Zero or more | \* | Matches zero or more occurrences of the preceding expression, making all possible matches. |
| One or more | + | Matches at least one occurrence of the preceding expression. |
| Beginning of line | ^ | Anchors the match string to the beginning of a line. |
| End of line | $ | Anchors the match string to the end of a line. |
| Beginning of word | < | Matches only when a word begins at this point in the text. |
| End of word | > | Matches only when a word ends at this point in the text. |
| Line break | \n | Matches a platform-independent line break. In a Replace expression, inserts a line break. |
| Digits | \d | Matches any digit [0-9]. |
| Any one character in the set | [] | Matches any one of the characters within the []. To specify a range of characters, list the starting and ending character separated by a dash (-), as in [a-z]. |
| Matches any character not in the set of characters following the ^. | [^...] | Matches any character not in the set of characters following the ^. |
| Or | | | Matches either the expression before or the one after the OR symbol (|). Mostly used within a group. For example, (sponge|mud) bath matches "sponge bath" and "mud bath." |
| Tagged expression | {} | Matches text tagged with the enclosed expression. |
| /C++ Identifier | :i | Matches the expression ([a-zA-Z\_$][a-zA-Z0-9\_$]\*). |
| Quoted string | :q | Matches the expression (("[^"]*")|('[^']*')). |
| Space or Tab | :b | Matches either space or tab characters. |
| Matches the expression ([0-9]+). | :z | Integer :z Matches the expression ([0-9]+). |
