---
title: "Searching within selections or visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/search-selections.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections"]
---

# Searching within selections or visualizations

You can search for values and make selections from the resulting filtered list. You can search selection items in the selection bar, and within visualizations such as filter panes and tables. Search is not case sensitive.

Click a selection item, and in the selection pop-up, type your search string. The list is filtered as you type, to display matching values. All matches are shown, including excluded values.

The result of searching for "Food" in the selection Product Group.

![Selection search.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SelectionSearch.png "Click to view full size")

The result of search for "Mich" in the Manager filter pane.

![List search.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ListSearch.png "Click to view full size")

Information noteYou can search for strings that contain up to 64,000 characters.

For a PDF containing examples with versions in several languages, see [Qlik Sense Cheat Sheet version 2.0](https://community.qlik.com/t5/Design/Qlik-Sense-Cheat-Sheet-version-2-0/ba-p/1667455).

## Search types

Qlik Sense supports the following methods of searching in selections and visualizations:

Search methods

| Search type | Description | Example | Supported data types in search field |
| --- | --- | --- | --- |
| Text search | Use text, including quotation marks, wildcards, and modifiers (minus and plus). Text search is separated into two different search modes: normal search and wildcard search.  For more information, see [*Text search*](text-search-selections-visualizations.htm). | \*company | Text string, numeric value, dual value |
| Numeric search | Relational symbols (">", ">=", "<" or "<=") allow values greater than, less than, and so on, to be found. For more information, see [*Numeric search*](numeric-search-selections-visualizations.htm). | >=5<20 | Numeric value, dual value |
| Fuzzy search | The tilde character ("~") as a prefix allows inexact matches to be found. For more information, see [*Fuzzy search*](fuzzy-search-selections-visualizations.htm). | ~beast company | Text string, numeric value, dual value |
| Expression search | An equals sign ("=") indicates an expression. Field values that match the expression are selected. For more information, see [*Expression search*](expression-search-selections-visualizations.htm). | =sum(Sales)> 1000000 | Text string, numeric value, dual value |
| Compound search | Use search operators to combine multiple searches within a single line. For more information, see [*Compound search*](compound-search-selections-visualizations.htm). | (\*ABC\* & ?\*Inc\*) | Text string, numeric value, dual value |

## Learn more

- [*Using smart search*](../../Search/use-smart-search-tool.htm)
- [Searching and Selecting Data](/lnk/Searching_selecting_data)

Related learning:

- [Searching and Selecting Data](/lnk/Searching_selecting_data)
