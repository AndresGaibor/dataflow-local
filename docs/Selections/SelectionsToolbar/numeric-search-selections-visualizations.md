---
title: "Numeric search"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/numeric-search-selections-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections", "Searching within selections or visualizations"]
---

# Numeric search

Numeric search is very similar to text search. The only difference is that the search string must begin with one of the relational operators ">" (greater than), ">=" (greater than or equal to), "<" (less than), or "<=" (less than or equal to).

Only values that fulfill the numeric requirement will be matched.

Numeric search for field values with one comparison (greater than 20)

![Numeric search for values matching a specific numeric comparison (in this case, values greater than 20). The search text is '>20'. No quotation marks are used in the actual search.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_NumericSearchResults-one-comparison.png "Click to view full size")

You can combine multiple numeric operators in a single search.

Numeric search for field values with multiple comparisons (greater than or equal to five, and less than 20)

![Numeric search for values matching a combination of numeric comparisons (in this case, greater than or equal to five, and less than 20. The numeric comparisons used are the 'less than' comparison' and 'greater than or equal to' comparison.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_NumericSearchResults-multi-comparison.png "Click to view full size")

Numeric searches can also be used to filter date fields.

Numeric search for dates on and after January 8, 2018

![Numeric search for dates matching a specific numeric condition (in this case, in this case, dates on and after January 8, 2018. The numeric comparison used is the 'greater than or equal to' comparison.).](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_NumericSearchResults-comparison-dates.png "Click to view full size")

The following table contains additional examples of numeric searches, with explanations of the results.

Numeric search examples

| Example | Result |
| --- | --- |
| >900 | Finds all values greater than 900. |
| <=900 | Finds all values less than or equal to 900. |
| >900<1000 | Finds all values greater than 900 and less than 1000. |
| <900>1000 | Finds all values less than 900 or greater than 1000. |
