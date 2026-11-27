---
title: "Compound search"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/compound-search-selections-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections", "Searching within selections or visualizations"]
---

# Compound search

With a compound search, you can combine two or more searches with search operators. This allows customized and specific filtering of data. A compound search is triggered by enclosing the search within a set of parentheses. You can use multiple search operators in a single compound search.

Compound search in Qlik Sense

![Example of a compound search using the OR operator (|). The search text is '(01|03)', without the quotation marks. It returns values '01' and '03'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearchGeneric.png "Click to view full size")

In its most basic form, a compound search can contain a single value. Unlike other search methods, a compound search for a single term will only return values that are an exact match with the search term. This can help you create more specific searches of your data.

Compound search using a single search term

![Compound search using only one search term. In this case, the search is entered in the 'Region' field and the search text is '(Spain)', without quotation marks. The 'Region' value 'Spain' is the only listed result.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearchSingleTerm.png "Click to view full size")

A compound search can contain one or more wildcards. If search content contains spaces, use quotation marks to enclose the value as it appears within the compound search.

For more information about quotation marks and wildcards, see [*Text search*](text-search-selections-visualizations.htm).

Compound search using multiple wildcards and quotation marks

![An example of a compound search. This uses quotation marks (to specify search for strings with spaces), an OR search operator, and two wildcards (* and ?). The search text is 'P?????C' contained in quotation marks, separated with a '|' (no quotation marks) from the second search '*B' (no quotation marks). This search text is contained within parantheses, and the results include values 'Prod. B' and 'Prod. C'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearchMultWildcardQuotes.png "Click to view full size")

## OR search operator ("|")

Using the OR operator, the compound search will return values that match any of the included searches.

Compound search using the OR search operator

![Compound search using the OR operator. In this case, the search text is '(2012|2013|2014)', with no quotation marks in the actual search. The results include the values '2012', '2013', and '2014'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearch_Operator_OR.png "Click to view full size")

## AND search operator ("&")

Using the AND operator, the compound search will return values that match all of the search items included in the statement. Since compound searches return exact matches only, this operator is typically only used with one or more wildcards.

Compound search using the AND search operator

![Compound search using the AND operator. In this case, the search text is '(2012|2013|2014)', with no quotation marks in the actual search. The results include the values '2012', '2013', and '2014'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearch_Operator_AND.png "Click to view full size")

This additional example uses the AND operator and multiple wildcards in a compound search.

Additional example of compound search using the AND search operator

![Compound search using the AND operator. In this case, the search text is '(*ABC* ['and' operator symbol] ?Inc*)', with no quotation marks in the actual search. The results include the value 'Solutions ABC Inc'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearch-and-operator.png "Click to view full size")

## XOR search operator ("^")

Using the XOR operator, the compound search will return values that match either the first or second search, but not both.

In the example below, the search returns values that either start with the letter "j'" or end with the letter "h", but values that match both these criteria (such as "Josh") are not included.

Compound search using the XOR search operator

![In this case, the search text is '(J* ^ *h)'', with no quotation marks in the actual search. The results include the values 'John' and 'Smith', but not, for example, 'Josh'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearch_Operator_XOR.png "Click to view full size")

This example uses the XOR operator and multiple wildcards.

Additional example of compound search using the XOR search operator

![Compound search using the XOR operator. In this case, the search text is '(*ABC*^?*Inc*)', with no quotation marks in the actual search. The results include the values 'ABC New Solution', 'ABC Solution', 'Neat ABC Company', and 'Solution Company Inc.'.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CompoundSearch_xor-operator.png "Click to view full size")

## Considerations for normal searches within a compound search

Information note

Due to differences between how client and engine process your search inputs, the standard space character is the only separator that is fully supported as a word-boundary token. Other separators might be supported and interpreted as valid word-boundary tokens by the engine but cannot be used due to client-sided input limitations.

These client-sided limitations are necessary for the client to be able to parse and structure the text-strings entered character by character (through an ASCII-only regex) and translate these into separated, searchable words.

The actual interpretation of word-boundary classifiers is a rule-based classification provided by the ICU library via Unicode and is highly dependent on system language settings.
