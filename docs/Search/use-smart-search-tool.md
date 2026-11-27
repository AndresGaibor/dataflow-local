---
title: "Using smart search"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Search/use-smart-search-tool.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Using smart search

Smart search is the global search tool in Qlik Sense, enabling you to search the entire data set in your application from any [sheet](#glossary-1 "Glossary term") in the application. Smart search is available from the [selections](#glossary-2 "Glossary term") bar in a sheet by clicking ![Selection search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_search.svg).

Smart search [field](#glossary-3 "Glossary term") where you can search the entire data set in your application from any sheet.

![Smart search field.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SmartSearchBar.png "Click to view full size")

Information note

Smart search only supports text search. Search operators other than quotation marks are not supported.

If you click on a result under Apply a selection, the results disappear and the selection is applied.

Smart search is available when you are analyzing data on a sheet. The data results help you to find associations and make selections in your data.

You can search for data in [visualizations](#glossary-4 "Glossary term") in your sheet with Insight Advisor, which you can access by clicking Insight Advisor in the sheet view. Insight Advisor can also generate new vizualizations based on your data searches.

For more information, see [*Creating visualizations with Insight Advisor*](../Insights/insight-advisor-create-visualizations.htm).

You can also search within selections and visualizations such as tables and filter panes.

For more information, see [*Searching within selections or visualizations*](../Selections/SelectionsToolbar/search-selections.htm).

## What happens when you search

As you type your search query, Qlik Sense searches data items. Smart search filters the field values and displays the matching items. Smart search looks for:

- Field values
- Dimension values (also [dimension](#glossary-5 "Glossary term") values that are created as master items)

Information noteMeasures ([measure](#glossary-6 "Glossary term") values) are not included in smart search.

The results of searching for 'John Vegetables sugar', which generates one search query for each term.

![Smart search result.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SmartSearchResult.png "Click to view full size")

### A: Search field

Separate search terms with spaces. To link words into one search term, use quotation marks, for example, “mountain bike”. Suggested search strings are displayed beneath the search field

### B: Apply a selection

The search results from the application data, shown with one result per row.

Click Show me more to see more results.

For more information, see [*Using search results to change selections*](smart-search-data.htm).

### C: Color-coded search result terms

A color code is assigned to each search term found. It shows partial matches as well as full matches.

You can clear the search field by clicking the cancel icon ![Close](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_close.svg) to the right in the search field. Click the search icon ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_search.svg) to close smart search.

The search terms are always compared against the beginning of the words in the database. Searching for “read” does not present “bread” as a match, whereas “reader” and “Reading” would both be matches. The search terms are each given a color to support the identification of the matches. When there are more than six search terms, the colors are reused.

## Learn more

- [*Searching within selections or visualizations*](../Selections/SelectionsToolbar/search-selections.htm)
- [Searching and Selecting data](/lnk/Searching_selecting_data)

Related learning:

- [Searching and Selecting data](/lnk/Searching_selecting_data)
