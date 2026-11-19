---
title: "String functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/string-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# String functions

This section describes functions for handling and manipulating strings.

All functions can be used in both the [data load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/string-functions.htm#glossary-0 "Glossary term") and in chart expressions, except for Evaluate which can only be used in the data load script.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Capitalize

Capitalize() function converts the first character of each word in a text string to uppercase and converts all other characters to lowercase.

[**Capitalize**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Capitalize.htm)(text)

Chr

Chr() returns the Unicode character corresponding to the input integer, also known as a code point.

[**Chr**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Chr.htm)(int)

CountRegEx

CountRegEx() returns the number of occurrences of the specified regular expression pattern in the input string text. If there is no match, 0 is returned.

[**CountRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/CountRegEx.htm)(text, regex)

Evaluate

Evaluate() finds if the input text string can be evaluated as a valid Qlik Sense expression, and if so, returns the value of the expression as a string. If the input string
is not a valid expression, NULL is returned.

[**Evaluate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Evaluate.htm)(expression\_text)

ExtractRegEx

ExtractRegEx() extracts text from an input string expression using the specified regular expression pattern. The function returns a null value if no matches are found.

[**ExtractRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ExtractRegEx.htm)(text, regex [, field\_no])

ExtractRegExGroup

ExtractRegExGroup() extracts text from an input string expression using the composite regular expression pattern that is specified. When using the function, specify the group to use within the composite regex. The function returns a null value if no matches are found.

[**ExtractRegExGroup**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ExtractRegExGroup.htm)(text, regex, group [, field\_no])

FindOneOf

FindOneOf() searches a string to find the position of the occurrence of any character from a set of provided characters. The position of the Nth occurrence of any character from the search set is returned where N is the optional third parameter of the function. If no third parameter is supplied, the first occurrence is returned. If no match is found,
0 is returned.

[**FindOneOf**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/FindOneOf.htm)(text, char\_set[, count])

Hash128

Hash128() returns a 128-bit hash value of the combined input expression values. The result is a 22-character string.

[**Hash128**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Hash128.htm)(expr{, expression})

Hash160

Hash160() returns
a 160-bit hash value of the combined input expression values. The result is a 27-character string.

[**Hash160**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Hash160.htm)(expr{, expression})

Hash256

Hash256() returns a 256-bit hash value of the combined input expression values. The result is a 43-character string.

[**Hash256**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Hash256.htm)(expr{, expression})

Index

Index() searches a string to find the starting position of
the nth occurrence of a provided substring. An optional third argument provides the value of n, which is 1 if omitted. A negative value searches from the end of the string. The positions in the string are numbered left to right from
1 and up.

[**Index**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Index.htm) (text, substring[, count])

IndexRegEx

IndexRegEx() searches the input string and returns the starting position of the nth occurrence of the specified regular expression pattern. An optional third argument count provides the value of n, which is 1 if omitted. The positions in the string are numbered left to right from 1 and up. If no match is found, the function returns 0.

[**IndexRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IndexRegEx.htm)(text, regex [, count])

IndexRegExGroup

ExtractRegExGroup() extracts text from an input string expression using the composite regular expression pattern that is specified. When using the function, specify the group to use within the composite regex. The function returns a null value if no matches are found.

[**IndexRegExGroup**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IndexRegExGroup.htm)(text, regex, group [, count])

IsJson

IsJson() tests whether a specified string contains valid JSON (JavaScript Object Notation) data. You can also validate a specific JSON data type.

[**IsJson**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IsJson.htm)(json [, type])

IsRegEx

IsRegEx() returns whether the specified text is a valid regular expression.

[**IsRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/IsRegEx.htm)(expr [, debug)

JsonGet

JsonGet() returns the path of a JSON (JavaScript Object Notation) data string. The data must be valid JSON but can contain extra spaces or newlines.

[**JsonGet**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonGet.htm)(json, path)

JsonSet

JsonSet() modifies a string containing JSON (JavaScript Object Notation) data. It can set or insert a JSON value with the new location specified by the path. The data must be valid JSON but can contain extra spaces or newlines.

[**JsonSet**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/JsonSet.htm)(json, path, value)

KeepChar

KeepChar() returns a string consisting of any of the characters in the first string that match the characters in the second string. This function is case-sensitive.

[**KeepChar**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/KeepChar.htm)(text, keep\_chars)

Left

Left() returns a string consisting of the first (leftmost) characters of the input string, where the number of characters is determined by the second argument.

[**Left**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Left.htm)(text, count)

Len

Len() returns the length of the input string.

[**Len**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Len.htm)(text)

LevenshteinDist

LevenshteinDist() returns the Levenshtein distance between two strings. It is defined as the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one string into the other.
The function is useful for fuzzy string comparisons.

[**LevenshteinDist**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/LevenshteinDist.htm)(text1, text2)

Lower

Lower() converts all the characters in the input string to lower case.

[**Lower**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Lower.htm)(text)

LTrim

LTrim() returns the input string trimmed of any leading spaces.

[**LTrim**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/LTrim.htm)(text)

MatchRegEx

MatchRegEx() compares an input string (text) with one or more regular expressions (regex). It returns the numeric location of the regular expression patterns that match. Returns a match response only if the evaluation of the regular expression matches the entire text input. If no matches are found, the function returns 0.

[**MatchRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/MatchRegEx.htm)(text, regex1 [ , regex2,...regexN])

Mid

Mid() returns the part of the input string starting at the position of the character defined by the second argument, 'start', and returning the number of characters defined by the third argument, 'count'. If 'count' is omitted, the rest of the input string is returned. The first character in the input string is numbered 1.

[**Mid**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Mid.htm)(text, start[, count])

Ord

Ord() returns the numeric (ASCII or Unicode) value of the first character of a string. This function is useful to evaluate or compare strings based on their underlying character codes, for example, when sorting or filtering strings with non-standard characters.

[**Ord**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Ord.htm)(text)

PurgeChar

PurgeChar() returns a string consisting of the characters contained in the input string ('text'), excluding any that appear in the second argument ('remove\_chars').

[**PurgeChar**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/PurgeChar.htm)(text, remove\_chars)

Repeat

Repeat() forms a string consisting of the input string
repeated the number of times defined by the second argument.

[**Repeat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Repeat.htm)(text[, repeat\_count])

Replace

Replace() returns a string after replacing all occurrences of a given substring
within the input string with another
substring. The function is non-recursive and works from left to right.

[**Replace**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Replace.htm)(text, from\_str, to\_str)

ReplaceRegEx

ReplaceRegEx() returns a string after replacing one or more matches
between an input string and a specified regular expression pattern. The text that replaces the matching text is specified in the to\_str argument. The function works from left to right, but if you specify a negative occurrence value, the functions reads from right to left.

[**ReplaceRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegEx.htm)(text, regex, to\_str [, occurrence])

ReplaceRegExGroup

ReplaceRegExGroup() returns a string after replacing one or more matches
between an input string and the composite regular expression pattern that is specified. The text that replaces the matching text is specified in the to\_str argument. The function works from left to right, but if you specify a negative occurrence value, the function reads from right to left.

[**ReplaceRegExGroup**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/ReplaceRegExGroup.htm)(text, regex, to\_str, group [, occurrence])

Right

Right() returns a string consisting of the last (rightmost)
characters of the input string, where the number of characters is determined by the second argument.

[**Right**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Right.htm)(text, count)

RTrim

RTrim() returns the input string trimmed of any trailing spaces.

[**RTrim**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/RTrim.htm)(text)

SubField

SubField() is used to extract substring components from a parent string field, where the original record fields consist of two or more parts separated by a delimiter.

[**SubField**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubField.htm)(text,
delimiter[, field\_no ])

SubFieldRegEx

SubFieldRegEx() extracts text from an input string expression, using the specified regular expression pattern as a delimiter. The function returns a null value if no matches are found.

[**SubFieldRegEx**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubFieldRegEx.htm)(text, regex\_delimiter [, field\_no])

SubStringCount

SubStringCount() returns
the number of occurrences of the specified substring in the input string text.
If there is no match, 0 is returned.

[**SubStringCount**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/SubStringCount.htm)(text, substring)

TextBetween

TextBetween() returns the text in the input string that occurs between the characters specified as delimiters.

[**TextBetween**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/TextBetween.htm)(text,
delimiter1, delimiter2[, n])

Trim

Trim() returns the input string trimmed of any leading and trailing
spaces.

[**Trim**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Trim.htm)(text)

Upper

Upper() converts all the characters in the input string to upper case for all text characters in the expression. Numbers and symbols are ignored.

[**Upper**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/StringFunctions/Upper.htm)(text)
