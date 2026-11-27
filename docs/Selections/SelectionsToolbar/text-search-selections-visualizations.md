---
title: "Text search"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/text-search-selections-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections", "Searching within selections or visualizations"]
---

# Text search

Text search is the main search method you can use in Qlik Sense. Use quotation marks, wildcards, and modifiers to search for values in a field. As you type your search string, Qlik Sense filters the field values and displays the matching items.

Text search can be split up into two separate search modes:

- Normal search
- Wildcard search

Search modes within text search

| Search type | Description | Example | Supported types of data |
| --- | --- | --- | --- |
| Normal search | Use text including plus and minus modifiers | ACME -Inc | Character or text string, numeric value, dual value |
| Wildcard search | Use text including wildcards, excluding plus and minus modifiers | \*company | Character or text string, numeric value, dual value |

## Normal search

Normal text cannot contain wildcards, but can contain plus and minus modifiers. Normal search can only be used interactively and cannot be used in search inside set analysis expressions.

If you perform a normal search, strings that match the search string are displayed. If you use several strings, separated by blanks, each of these is interpreted as a separate search string and displays all field values that contain any of the strings.

Normal text search using a single search string (no quotation marks)

![Text search for single string 'ab', with results. No quotation marks are used, and results are shown.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_TextSearchResults-one-string.png "Click to view full size")

Normal text search using two search strings separated by a space (no quotation marks)

![Text search for two separate strings: 'abc' and 'solution', separated by a space. No quotation marks are used, and results are shown.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_TextSearchResults-two-strings.png "Click to view full size")

Information note

Due to differences between how client and engine process your search inputs, the standard space character is the only separator that is fully supported as a word-boundary token. Other separators might be supported and interpreted as valid word-boundary tokens by the engine but cannot be used due to client-sided input limitations.

These client-sided limitations are necessary for the client to be able to parse and structure the text-strings entered character by character (through an ASCII-only regex) and translate these into separated, searchable words.

The actual interpretation of word-boundary classifiers is a rule-based classification provided by the ICU library via Unicode and is highly dependent on system language settings.

Normal text search examples

| Example | Result |
| --- | --- |
| "orange juice" | Only finds field values that contain the whole string “orange juice”. See  [*Quotation marks*](#Quotati). |
| orange juice | Without the quotation marks, all fields that contain either “orange” or “juice” would be displayed. |
| +orange +juice | Finds matches such as “orange juice”, “orange and apple juice” and “juice from oranges”. See [*Plus modifier (+)*](#Plus). |
| -orange ‑juice | Excludes results containing orange or juice. See [*Minus modifier (-)*](#Minus). |

### Quotation marks

If you want separate search strings to be interpreted as only one string, use quotation marks (" ") to link the strings together.

Text search using a single search string (contained within quotation marks)

![Text search for single string 'abc solution', with quotation marks. Results show only fields containing the entire search string; in this case, the only result is 'ABC Solutions'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_TextSearchResults-one-string-quotes.png "Click to view full size")

### Modifiers

Modifiers allow you to refine the results of your searches by including or excluding values meeting specific conditions.

There are two types of modifiers available:

- Plus modifier (+)
- Minus modifier (-)

#### Plus modifier (+)

By using the plus modifier, you set the condition that strings with a plus sign must be included in the matching items. However, the strings do not necessarily need to be next to each other, nor in the same order as they were entered.

In the following example, the plus modifier is placed next to the value abc. The results must contain this value, but order does not matter. The second string, solution, is not bound by this condition so it can appear in results but does not need to be present.

Search containing plus modifier (+)

![Search containing a plus modifier in front of two separate strings. Specifically, the value '+abc solution' is searched. The actual search does not contain the quotation marks.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-plus-modifier-ex-1.png "Click to view full size")

#### Minus modifier (-)

Placing the minus modifier before a search term excludes results containing that text.

In this example, the minus sign before the word "solution" removes all values containing this string from the results.

Search string with minus modifier (-)

![Search using the minus modifier. Specifically, the value '-solution' is searched. The actual search does not contain the quotation marks.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-minus-modifier.png "Click to view full size")

#### Combining modifiers

You can combine minus and plus modifiers in a single search. In this example, values containing the string "solution" will be excluded, and the string "abc" must be present in order for the value to appear in the results.

Search combining minus and plus modifiers

![Search using both the minus and plus modifiers. Specifically, the value '-solution +abc' is searched. The actual search does not contain the quotation marks.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-minus-plus-modifiers.png "Click to view full size")

## Wildcard search

Wildcard search allows you to make your text searches more flexible. Wildcard search can be used in interactive situations and with set analysis. Wildcard search must not include plus or minus modifiers.

You can use one or several wildcards in a search string. The following wildcards can be used:

- \* wildcard
- ? wildcard
- ^ wildcard

Wildcard text search examples

| Example | Result |
| --- | --- |
| a\* | Finds all values that begin with the letter “a”, including strings with several words where the first word begins with an “a”. |
| \*b | Finds all values that end with the letter “b”, including strings with several words where the last word ends with a “b”. |
| \*c\* | Finds all values that contain the letter “c”, including strings with several words. |
| \*^ab\* | Returns all values that have words that begin with “ab”.  Equivalent to a normal search for “ab”, but unlike the normal search it can be made more complex using wildcards. It can also be used in a programmatic search, such as in Set Analysis. |
| r?ck | Finds all values that have four letters and start with an “r”, followed by any character, and ending with “ck”, for example, “rack”, “rick”, “rock”, and “ruck”. |
| r?? ????d | Finds all values that consist of a three-letter word beginning with an “r” and a five-letter word ending with a “d”. |

Information noteIf you use wildcards, only those records that match the entire search string are displayed; that is, a blank does not imply a logical OR. The search string '\*creamed' does not get a match on "Rocky's creamed corn" since the value does not end with “creamed”. Neither does “creamed\*” result in a match on "Rocky's creamed corn", since the value does not start with “creamed”.

Information noteSpace in a search string makes a difference. If you search for “\*corn” you get matches on strings ending with, for example, “popcorn” as well as “corn”. If you use a space in your search string, “\* corn”, you only get matches that end with “corn”.

#### \* wildcard

The \* wildcard is used in the place of zero or more characters, including spaces. This wildcard is flexible and matches any character or any block of characters in a specific position.

In this example, all values starting with the string "company" are listed in the results.

Search string with \* wildcard after defined characters

![Search with * wildcard after several defined characters. Placing this wildcard after the word 'Company' returns all values beginning with this word. The actual search does not contain the quotation marks.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-wildcard-asterisk-example1.png "Click to view full size")

Here, all values ending with the string "company" are listed in the results.

Search string with \* wildcard before defined characters

![Search with * wildcard before several defined characters. Placing this wildcard before the word 'Company' returns all values ending with this word. The actual search does not contain the quotation marks.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-wildcard-asterisk-example2.png "Click to view full size")

By placing \* wildcards before and after a string, the results will include all values containing this string.

Search string with \* wildcard before and after defined characters

![Search for the word 'Company', surrounded by * wildcards. Configuring the wildcards in this way returns all values containing this word. The actual search does not contain the quotation marks.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-wildcard-asterisk-example3.png "Click to view full size")

#### ? wildcard

The ? wildcard is used in the place of a single character, including spaces. This wildcard is useful when you suspect that a string may be misspelled, when you are unsure of the spelling, or when the string contains special characters that may be difficult to reproduce correctly.

This wildcard can be substituted for all characters in the string, or used in combination with defined characters.

Search string with ? wildcard symbols for all characters

![Search using ? wildcard for all search characters. In this case, all values with the same number of characters contained in the search are listed in the results (for example, 'ABC Solution'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-wildcard-question-example1.png "Click to view full size")

Search string with ? wildcard symbols after three defined characters

![Search using ? wildcard for all search characters except for the first characters 'ABC' (no quotation marks used in actual search). In this case, one result is listed: 'ABC Solution'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-wildcard-question-example2.png "Click to view full size")

#### ^ wildcard

The ^ wildcard is used to filter values by the character or characters at the beginning of a word within a field value. This wildcard is only used in conjunction with other wildcards.

In this example, the search string "\*^a\*" will return all values containing a string starting with the letter "a".

Search string with ^ and \* wildcards

![Search combining two different wildcard types.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchResults-caret-example.png "Click to view full size")
