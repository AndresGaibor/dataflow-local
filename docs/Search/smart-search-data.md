---
title: "Using search results to change selections"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Search/smart-search-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Using smart search"]
---

# Using search results to change selections

## Interacting with search results for data

When you search data, the results show the combinations of matches found in the entire Qlik Sense database. The results are based on [field](#glossary-0 "Glossary term") associations. They are sorted by the number of matched search terms, in descending order. If there is more than one match, the results are ranked by relevance. Click a match to insert it into the search field.

When you select a result, you make an actual selection of the values, and your current [selections](#glossary-1 "Glossary term") and the [visualizations](#glossary-2 "Glossary term") containing the selected data are updated.

The screenshot illustrates the categories that are available in the database: john, Vegetables, and sugar.

![Search view with search results.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SmartSearchResults-new.png "Click to view full size")

Information note If you select a [dimension](#glossary-3 "Glossary term") value in the search result, the field name (not the dimension name) will be displayed in the selections bar.

You can clear the search field by clicking the cancel icon ![Close](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_close.svg) to the right in the search field. Click the search icon ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_search.svg) to close smart search.

The search terms are always compared to the beginnings of the words in the database. Searching for “read” does not present “bread” as a match, whereas “reader” and “Reading” would both match. The search terms are colored to show the matches. When there are more than six search terms, the colors are reused.

### Using smart search to change the current selection

When you use smart search to search the data in an application, and you make a selection from the results, you can search within that selection. Then you can click on search results to change your current selections. Smart search searches within your selections automatically, all you need to do is add search strings and perform a new search. You can do this over and over to filter your search results.

Using smart search to search within the selections Region and Product type.

![Smart search view with search results.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SmartSearchWithinCurrentSelection-new.png "Click to view full size")

When you search within your current selection, smart search will find results associated with your current selection. If the terms you are searching for are not associated with the current selection, you will see an option to clear the current selection. If you clear the selection you will see the result for the searched terms without having to re-enter them.

If you search within a selection, and your search terms are excluded because of the selections (dark gray), there will be no results.

If you search within a selection using multiple terms and your query does not produce a result for all of your search terms, you can view partial matches by clicking Show partial matches.

Searching for the multiple terms 'fresh fruit' did not produce a result for all search terms, making the option 'Show partial matches' available.

![Option 'Show partial matches' available in Smart seach view.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SmartSearchNotAssociated-new.png "Click to view full size")

If you search within a selection and your query does not produce a result, you will get the message “No matches found within your current selection.”. If the selection is locked, you can consider to unlock the selection and perform a new search.

No result searching for 'sugar' in the selection Product Type.

![Message 'No matches found within current selection' in Smart search view. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SmartSearchLockedNonAssociated-new.png "Click to view full size")
