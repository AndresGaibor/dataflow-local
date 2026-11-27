---
title: "Direct Query limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/limitations-direct-query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query"]
---

# Direct Query limitations

The following section describes the limitations of Direct Query.

The following limitations apply when using and creating Direct Query applications:

- Direct Query applications can only use a single database.
- Direct Query applications can only reload Direct Query data sources.
- The Qlik Analytics mobile application does not support Direct Query.
- Direct Query capabilities are dependent on the capabilities of the underlying cloud databases and SQL pushdown.
- Direct Query performance is heavily affected by the performance of the underlying data source.
- What is supported in Direct Query mode might be different in each application depending on the [data connection](#glossary-1 "Glossary term") type. Each database might treat the execution of queries differently.
- It is not possible to use Qlik Data Gateway - Direct Access data connections in Direct Query.
- Security is handled by the database.
- Direct Query application type can only be selected for databases where Direct Query mode is supported.
- To use Direct Query on a database, you need to have permission to read from the database.
- To use Direct Query on a data connection, you need to have the Can consume data permission in the space where the data connection resides.
- Interception and local execution of some operations will only follow the caching paradigm, which the user must turn on.
- The following [activity center](#glossary-2 "Glossary term") actions are not supported:

  - [Impact analysis](#glossary-3 "Glossary term")
  - Open without data
  - Evaluate performance
  - Reload
  - Schedule reload
- Direct Query applications can be published to managed spaces, but users in the managed space must have access to the data connection used by the Direct Query application.
- There is a 1 million row limit on what can be returned in a single query to an underlying database.
- The green, white and grey associative model is not supported. Because of the limitations of SQL query-based modelling, data is filtered rather than selected. For more information, see [*The associative selection model*](../Selections/associative-selection-model.htm).
- Sorting options are not supported in filter pane [visualizations](#glossary-4 "Glossary term"). Default sorting is applied automatically.
- Direct Query filter panes do not indicate excluded values in gray. For more information, see [*Selection states*](../Selections/selection-states.htm).
- Visualization extensions are not supported.
- Embedding application content is not supported.
- Sharing and downloading application content is not supported.
- Reporting capabilities, including the Qlik Reporting Service value-add features and subscription reports, are not supported in Direct Query applications.
- Context sensitive help is not available in the expression editor for Snowflake functions.
- The following [field](#glossary-5 "Glossary term") search capabilities are not supported:

  - Fuzzy search
  - Compound search
  - Implicit word-based search or word-based search expressed with "^"
  - "-" and "+" symbols indicating additional search semantics instructions
- When a Qlik Cloud Direct Query SQL query is constructed to request row data to populate a chart, the maximum result size will be constrained by a LIMIT n (or its database-specific equivalent) included in the relevant SQL query sent to the remote database.

  This LIMIT n serves to reduce potential query performance impact and Analytics engine memory use impact by limiting the maximum number of data result rows returned for a single query result.

  - LIMIT n will have n greater than or equal to 1000 in almost all generated SQL data queries. Specific charts have the following considerations:

    - Scatter plot chart data queries have a default n of 2500.
    - For a table chart the LIMIT n can be configured explicitly up to a maximum n of 100000 using the DirectQueryRowFetchMaxCount script variable described in [*Direct Query script variables*](internal-variables-direct-query.htm).
    - If DirectQueryRowFetchMaxCount is configured to be > 0 and < 2500 then the DirectQueryRowFetchMaxCountvalue will also be used to restrict the LIMIT n used to query data for a scatter plot.
  - It is important to note that the applied LIMIT discussed above applies only to data fetch queries to populate what is visible on a chart. Aggregation queries are not limited in any way and will always reflect the correct database-specific aggregation result of the complete dataset in the remote database.
  - The row data fetch limits will also impact on-demand application-generated content from a Direct Query application.
- The write table is not available in Direct Query applications.

## Bookmark limitations

You can create, update, and apply [bookmarks](#glossary-6 "Glossary term") in Direct Query applications in the same way as in in-memory applications. The following limitations apply:

- Bookmark details list only the selected fields. Selected values are not shown, and value counts are shown as 0.
- When you apply a bookmark, the saved selections are applied to the current data. If the data has changed since the bookmark was created, the result can be different.
- If a field, value, or alternate state saved in the bookmark no longer exists, it is skipped without a warning. The rest of the bookmark is applied.
- Selections are cleared when a session reconnects, or when the application is refreshed after a reload. To restore the selections, apply the bookmark again.
- The set analysis expression of a bookmark is empty when it is read through the API.

For more information, see [*Creating bookmarks*](../Bookmarks/create-bookmark.htm).
