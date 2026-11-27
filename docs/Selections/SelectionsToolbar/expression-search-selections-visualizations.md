---
title: "Expression search"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/expression-search-selections-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections", "Searching within selections or visualizations"]
---

# Expression search

With an expression search, you can search for values across all fields associated with the search field.

An expression search always begins with an equals sign ("="). The expression is evaluated for every value in every field associated with the search field. All values for which the search expression returns a non-zero value are selected.

In a filter pane with Sales values, you can use a search such as: "=Sum(Sales) > 1000000" to find values larger than 1,000,000. This is a simple search and you could get the same result by using the numeric search: ">1000000". Often, an expression search is the only choice. For example, if you want to search for values in associated fields, you have to use an expression search.

In the example below, the search "=Sum(Sales) > 1000000" in the Customer field returns every value in the Customer field for which the Sales column value is greater than 1000000.

Expression search

![Example of an expression search. The search string is '=sum(Sales)>1000000' (no quotation marks included in the actual search). This search will return results for values in the 'Customer' field associated with values of Sales which are greater than 1000000.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_expression-search-example.png "Click to view full size")

Example:

Let us assume that you have a filter pane for sales representatives. You can then use an expression search for the sales representatives who have sales larger than, for example, 5,000,000. The search string is similar to the previous one: "=Sum(Sales) > 50000000". Because the sales values are associated with the sales representatives, you can perform the search in the Sales Rep filter pane.

Expression search in a filter pane using a search string

![Expression search in a filter pane with results. In this case, '=Sum(Sales) > 50000000' is entered in the search box (no quotations marks included in the actual search). The results display values in the 'Sales Rep Name' field associated with values in the 'Sales' column which are greater than 5,000,000.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SearchExpression.png "Click to view full size")
