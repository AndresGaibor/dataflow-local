---
title: "Accessing cloud databases directly with Direct Query"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/direct-access-with-direct-query.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Accessing cloud databases directly with Direct Query

Use Direct Query to read SQL databases without having to import or load the data in memory.

Direct Query gives the user more options on how they want to access their data in order to suit their individual needs. Accessing the data through Direct Query allows the user to keep the data in its underlying data source. This increases the speed at which users can interact with their data in exchange for the flexibility that an in-memory Qlik Cloud application offers.

In general, it is recommended that you import your data into Qlik Cloud whenever possible. In-memory Qlik Cloud applications allow you to better customize your experience and get the most out of your data. However, if you find yourself in a situation where your goals cannot be met by importing data, Direct Query might be the solution for you. Due to their streamlined functionality, Direct Query applications can also help new users take their first step towards creating fully functional and fast in-memory applications.

You can create your Direct Query application using Data model manager to help select tables and fields, and define relationships between them. For more information, see [*Creating a Direct Query application*](create-direct-query-app.htm).

You can also use custom SQL in the load script to define the data model for your Direct Query application. This allows you to use variables and Qlik expressions while building your data model. For more information, see [*Creating a Direct Query application with custom SQL*](create-data-model-custom-sql.htm).

## Direct Query use case examples

You might consider using Direct Query instead of in-memory applications in the following cases:

Direct Query use cases

| Use case | Purpose and description |
| --- | --- |
| Big data sources | Direct Query is faster to initialize and less resource intensive for applications with more than 20 million rows. This can be very helpful when your applications are used primarily for monitoring or status reporting, where only a few or no [selections](#glossary-1 "Glossary term") are made. |
| Efficient in-memory applications | Direct Query provides functionality to quickly and easily extract data slices into the Qlik Cloud engine with filtering applied across all affected tables. For more information, see [*Exporting Direct Query application settings to a template application*](export-to-template-app-direct-query.htm) |
| Direct Query for writeback | When writeback based on Qlik Automate is set up to modify underlying database data, Direct Query can show the modified database results directly. The same functionality in an in-memory application would require the user to import the modified tables again. |
| Exploring new databases and tables | Direct Query can be used to explore new or unfamiliar databases and tables. This allows the user to make an informed decision on whether data needs to be imported from the underlying data source. |

## Tutorials

For a tutorial about how to use Qlik Sense applications, see [*Tutorial - Beginning with the Basics*](../Tutorials/introduction-beginning-with-basics.htm).

For a tutorial about Direct Query, see the following:

- [Direct Query - Part 1: Overview and Operation](https://www.youtube.com/watch?v=ZiTgqYvFFho)
- [Direct Query - Part 2: Hybrid Analytics Solutions with On Demand Application Generation (ODAG)](https://www.youtube.com/watch?v=15uIcFY6DJc)

Information noteThe Direct Query capability in Qlik Cloud is different from the Direct Query statement in QlikView. For more information, see [Direct Query.](/en-US/qlikview/May2022/Subsystems/Client/Content/QV_QlikView/Scripting/ScriptRegularStatements/direct-query.htm)

## Supported capabilities

Direct Query applications have different capabilities compared to in-memory applications.

Direct Query supports the following:

- [Data connection](#glossary-2 "Glossary term") types:

  Information noteIt is not possible to use Qlik Data Gateway - Direct Access data connections in Direct Query.

  - Amazon Redshift
  - Azure SQL
  - Azure Synapse Analytics
  - Databricks
  - Google BigQuery
  - Microsoft SQL Server
  - PostgreSQL
  - Snowflake

  Information noteA subset of scalar functions are supported in the data connections.
- In-memory data analysis emulation:

  - A subset of [set analysis](#glossary-3 "Glossary term").
  - Multi-table [charts](#glossary-4 "Glossary term") over arbitrary complex models. Existing model requirements for in-memory applications will still be in place. For example, association loops between tables are not allowed.
  - Basic [aggregation](#glossary-5 "Glossary term") types:

    - Sum
    - Count
    - Min
    - Max
    - Avg
    - Only
  - Pre- and post-aggregation calculations, based on function and operation set provided by the underlying database.
- Table relationship types:

  - Inner join
  - Full outer join
- Iterative modeling and dashboard creation.
- [Bookmarks](#glossary-6 "Glossary term"). Save your selections and apply them again later. For more information, see [*Bookmark limitations*](limitations-direct-query.htm#Bookmarks).
- Visualization features:

  - Standard charts:

    - Bar chart
    - Bullet chart
    - Button
    - Combo chart
    - Container
    - Filter pane
    - Gauge
    - KPI
    - Line chart
    - Map
    - Mekko chart
    - Pie chart
    - Scatter plot
    - Table
    - Text & image
    - Waterfall chart
  - Dashboard bundle:

    - Video player
    - Variable input
  - Visualization bundle:

    - Funnel
    - Multi KPI
    - Radar
    - Sankey
    - Word cloud
- A subset of [field](#glossary-7 "Glossary term") search capabilities:

  - A search string without special symbols (for example, "\*" and "?" for pattern search, or "=" for expression-based search) is interpreted as a prefix search over full string value.
  - Pattern search symbols and capabilities:

    - "\*" - any 0 or more symbols
    - "?" - any single symbol
  - Range-based search (based on ">", "<", ">=", "<="):

    - For numerical values, the lower/upper boundaries are detected based on the numerical value. For example, >10<100 is equivalent to <100>10. Both are interpreted as [SearchedField] > 10 AND [SearchedField] < 100.
    - For other data types, the lower/upper boundaries are detected by their order in the search condition. For example, >Value1<Value2 is not the same as <Value2>Value1. In the second case, Value2 is assumed to correspond to the lower boundary and will be interpreted as [SearchedField] < Value2 OR [SearchedField] > Value1.
  - Expression-based search, assuming the expression meets Direct Query limitations.

  Information noteFor a complete list of in-memory search capabilities, see [Searching within selections or visualizations](https://help.qlik.com/en-US/sense/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/search-selections.htm).
- Qlik Engine functions in $(=...) expressions.

  Within a KPI or a custom SQL expression in Direct Query, it is possible to use the following Qlik script and chart functions:

  - [**GetUserAttr**](../Scripting/SystemFunctions/GetUserAttr.htm)
  - [**if**](../Scripting/ConditionalFunctions/if.htm)
  - [**Chr**](../Scripting/StringFunctions/Chr.htm)
  - [**Replace**](../Scripting/StringFunctions/Replace.htm)
  - Literals and string operators

  An expression using one or more of the above options will be expanded exclusively within the Qlik Engine.

  Information noteMixing remote Native SQL functions and Qlik Engine functions within the same single $(=...) expression is not supported.

  To combine Qlik Engine function use and remote SQL database function (optionally including + set/selections), use nested $(=...) expressions:

  $(= ...<EngineFuncs> ... $(=... <set/selection &| Native SQL funcs>) ... )

  For example:

  '$(=Replace(GetUserAttr('userEmail'), '$(=Char(111))' , Chr(48)))'

  In the above nested expression example, the Replace(), GetUserAttr(), and Chr() functions are Qlik Engine functions and are enclosed in the outermost $(=…) expression. The nested $(=Char(111)) expression is not referencing an Engine function, however. It is a remote SQL database function (in MS SQL, for example).

  Assuming the user’s email in Qlik Cloud is 'root@qlik.com' then the above expression expansion would in this order,

  1. Expand the $(=CHAR(111)) non-Engine function via the remote SQL database, resulting in the lower-case letter o.
  2. Expand the CHR(48) Engine function to character "0'.
  3. Expand GetUserAttr('userEmail') to 'root@qlik.com'.
  4. Finally expand ‘$(=Replace('root@qlik.com', ‘o' , ‘0’)’ for a final result of 'r00t@qlik.com'.

## Learn more

- [*Direct Query limitations*](limitations-direct-query.htm)
- [*Creating ODAG links in Direct Query applications*](create-odag-links-direct-query.htm)
- [*Supported data types*](data_type_direct_query.htm)
