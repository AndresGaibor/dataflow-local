---
title: "Filter data from an ODBC database"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Filter-ODBC-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Filter data from an ODBC database

When selecting data from a database in the Select data to load step, in either Add data or the Data load editor, you can select a subset of data in the fields you are loading. This can be useful when you want specific data, such as only sales over $40,000. And it reduces the amount of data loaded.

Information noteYou can only filter data when using Qlik Sense.

You enter a data filter expression by selecting Filter data in the Select data to load step. Selecting Filter data opens a text box where you enter a filter expression. For example:

Sales >= 40000

Filter data selects from individual fields, such as Sales. It operates as an SQL WHERE clause. Most operators and keywords used in WHERE clauses can be used with Filter data. Valid operators include:

- =
- >
- >=
- <
- <=
- IN
- BETWEEN
- LIKE
- IS NULL
- IS NOT NULL

Qlik Sense builds a WHERE clause in the data load script from the expression entered in Filter data.

The keyword AND can be used to combine operators, such as when you want to filter based on more than one field. For example:

Sales < 30000 AND RegionID = 45

The OR keyword can also be used. For example:

Name = Smith OR Name = Jones

You can get the same results from the IN operator. The IN operator is a shorthand method for using multiple OR conditions. For example:

Name IN ('Smith', 'Jones')
