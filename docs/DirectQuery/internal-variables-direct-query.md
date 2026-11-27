---
title: "Direct Query script variables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/internal-variables-direct-query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query"]
---

# Direct Query script variables

Expand/Collapse all

# Direct Query script variables

You can use script [variables](#glossary-0 "Glossary term") to describe and manipulate the internal structure of a Direct Query application or to enable additional reload output information.

Use the drop-down to see a brief description and the syntax of each variable.

DirectQueryResultCacheExpirySeconds

This variable allows an application to specify the age at which a cached query result will be considered stale.

The age is defined from when the result was first cached. If the age of a cached result is greater or equal to n seconds, it is considered stale and is not used as a cached result for a matching query. Instead, the query in question will be executed as if no cached result existed.

When the query executes again, its new result may be cached, depending on the current cache and memory state. If cached, it starts aging again until stale at n seconds.

The default value for this variable is 30. This means that the cached query result is considered stale after 30 seconds.

Supported variable values

| Value | Description |
| --- | --- |
| -1 | This setting means that the cache is kept during the time the user is logged in. |
| 0 | Caching is completely disabled. |
| 1-9,223,372,036,854,775,807 | Sets the cached result stale age in seconds. |
| > 9,223,372,036,854,775,807 | Same as setting the variable to 30. |

DirectQueryResultCacheExpirySeconds=n;

DirectQueryRowFetchMaxCount

The default value for the maximum number of rows fetched for most [charts](#glossary-2 "Glossary term") with Direct Query is driven by the client query and can vary from 256 to 1000. The exception is scatter plots, where the default maximum is fixed as 2500. This means that some Direct Query-supported charts will not show more than n row results, even if a non-limited SQL query for the chart’s content would result in greater than n rows.

The DirectQueryRowFetchMaxCount script variable exists to allow increasing or limiting the maximum rows to display in a table chart or to restrict the maximum results displayed on a scatter plot chart to less than the default maximum of 2500.

Information noteThe value of DirectQueryRowFetchMaxCount will not have any affect on [aggregation](#glossary-3 "Glossary term") operations.

Additionally, DirectQueryRowFetchMaxCount has the following considerations:

- The default value of DirectQueryRowFetchMaxCount is -1 (meaning it is not used).
- Setting the script variable DirectQueryRowFetchMaxCount to a specific value greater than 0 allows a table chart populating query to fetch up to DirectQueryRowFetchMaxCount rows from the database - up to the maximum values shown in the table below.
- If DirectQueryRowFetchMaxCount is configured to be between 0 and 2500, then the DirectQueryRowFetchMaxCount value will also be used to limit the maximum data rows retrieved for populating a scatter plot chart.
- To undo the effects of the DirectQueryRowFetchMaxCount script variable, the variable can either be undefined, or set explicitly to a -1 value.

Supported variable values

| Value | Description |
| --- | --- |
| 0 | A value of 0 is a special value that affects only table chart row fetching. This setting dynamically paginates over all applicable rows (as influenced by selections) for populating a table chart. Determining the maximum number of rows in total for the pagination is done by performing an initial count query to determine how many rows in total the remote database will return for the table’s populating query.  Setting this variable to 0 will result in all other supported Direct Query charts (except tables and scatter plots) fetching their default client-specified maximum number of rows. Scatter plots will fetch their default maximum of 2500 rows.  Information noteAs this performs two queries for each load or selection instead of one it can be more expensive regarding database performance and costs. |
| 1-100,000 | Sets the maximum number of rows to fetch for a table or scatter plot chart from the remote database. Note that a Scatter plot chart will never retrieve more than 2500 rows to display. |
| > 100,000 | Same effect as setting the variable to 0. |

DirectQueryRowFetchMaxCount=n;

DirectQueryPreviewSql

The default value of this variable is 0.

Setting this variable to a value > 0 enables additional information to be included in the output of a Direct Query application Load data (reload) action.

The additional information shows the SQL query sent out to the remote database to preview the result of a custom SQL definition of a table. This information can be helpful for validating, evaluating, or refining custom SQL statement result expectations. See the DirectQueryPreviewResp variable for related information.

DirectQueryPreviewSql=1;

DirectQueryPreviewResp

The default value of this variable is 0.

Setting this variable to a value > 0 enables additional information to be included in the output of a Direct Query application Load data (reload) action.

The additional information shows the results of a SQL query sent out to the remote database related to a custom SQL definition of a table. See the DirectQueryPreviewSql variable for related information.

DirectQueryPreviewResp=1;
