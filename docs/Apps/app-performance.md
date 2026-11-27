---
title: "Optimizing application performance"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/app-performance.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Optimizing application performance

Application performance can be improved with reduced application size, simplified data models, and strategic use of [set analysis](#glossary-1 "Glossary term"). This section will help you avoid performance issues by pointing out areas where performance can be impacted and how you can evaluate and monitor application performance.

You can monitor your application’s performance using the performance evaluation tool, and you can also test how it performs on different engine sizes by manually assigning larger engines. For more details, see [*Application performance evaluation*](app-performance-evaluation.htm) and [*Assigning engines to improve application performance*](app-performance-select-engine.htm).

## Application complexity

These are loose categories that can help diagnose issues.
The most complex applications have the lowest performance.

Simple applications:

- Do not include complex set analysis or If() statements.
- Do not include large tables.
- Have a simple data model.
- Contain simple calculations.
- May have large data volumes.

Moderate applications:

- Have a data model with many tables, but follow best practices.
- Use set analysis and several If() statements.
- Have large or wide tables on sheets (15 columns or more).

Complex applications:

- Have a very complex data model.
- Connect to large data volumes.
- Contain complex calculations, charts, and tables.

## Large data volumes

You can employ these architecture strategies when you are connecting to large data volumes.

### Segmentation

You can segment [QVDs](#glossary-2 "Glossary term") by [dimensions](#glossary-3 "Glossary term") such as time frame, region or [aggregation](#glossary-4 "Glossary term") level. For example, you can have:

- A QVD that contains data from the two most recent years.
- A QVD that contains historical data further than two years.
- A QVD that contains all data aggregated on a higher level. For example, per month instead of date, or per country instead of individual customers.
- One large QVD with all the data, which is only used by a small subset of users.

You can segment the applications in a similar way. Smaller applications will address the analytical needs of most users. This saves memory.

You can also have multiple applications focused on different regions. This way, users will not open an application with data that they are not interested in or do not have rights to access. Data that is not accessible via [section access](#glossary-5 "Glossary term") still affects memory.

### On-Demand Application Generation (ODAG)

Qlik Sense on-demand applications give users aggregate views of big data stores. They can identify and load relevant subsets of the data for detailed analysis.

From a user perspective, there are two applications:

1. A shopping cart with aggregated data.
2. An empty template application used to display detail.

The user makes [selections](#glossary-6 "Glossary term") in the shopping cart application. Once a threshold has been met, a custom LOAD script is created which populates the template application with the requested details.
For more information, see [*Managing big data with on-demand applications*](../DataSource/Manage-big-data.htm).

### Application chaining

Application chaining (known as document chaining in QlikView) means that there is an aggregated application, which users consume regularly.
If a user needs more detail, selections can be passed from the aggregated application to a detail application, so that they can view a lower level of granularity. This saves memory, because users are not loading unnecessary detail. Application chaining can be performed by adding button objects to a sheet. For more information, see [*Application chaining*](../Visualizations/Button/create-buttons.htm#Applicat).

Application chaining is also supported via APIs. For example, you can use the App Integration API to create custom application chaining. For more information, see [App Integration API](/en-US/sense-developer/November2026/Subsystems/APIs/Content/Sense_ClientAPIs/app-integration-api.htm).

### Dynamic views

Dynamic views enable up-to-date visualizations for high data volume or rapidly changing data scenarios. Consider the following when working with dynamic views:

- When you update dynamic views, the data source is loaded directly. The update performance is affected by the performance of the underlying data source.
- Dynamic view template applications can help you create dynamic charts.

For more information about using dynamic views, see [*Managing data with dynamic views*](../DynamicViews/dynamic-views.htm).

### Direct Query

While in-memory applications are recommended, Direct Query allows you to keep data in its original source. Consider the following to optimize your Direct Query usage:

- The performance of Direct Query is heavily affected by the performance of the underlying data source.
- Keep your Direct Query data model as simple as possible, as complex queries might cause performance issues.

For more information about Direct Query, see [*Accessing cloud databases directly with Direct Query*](../DirectQuery/direct-access-with-direct-query.htm).

## Data model performance

These are indicators that can impact data model performance. Each one is a best practice that will improve application usability.

Data model performance best practices

| Action | Description |
| --- | --- |
| Synthetic keys removed | Qlik Sense creates synthetic keys when two or more data tables have two or more fields in common. This may mean that there is an error in the script or the data model. To diagnose synthetic keys, see [*Synthetic keys*](../Scripting/synthetic-keys.htm). |
| Circular references removed from data model | Circular references occur when two fields have more than one association. Qlik Sense will attempt to resolve these by changing the connection to one of the tables. However, all circular reference warnings should be resolved, see [*Understanding and solving circular references*](../LoadData/understand-circular-references.htm). |
| Appropriate granularity of data | You should only load data that is necessary. For example: a group of users only need data divided by week, month, and year. You can either load in the aggregated data or aggregate the data within the load script to save memory. If a user does need to visualize data at a lower level of granularity, you can use ODAG or document chaining. |
| QVDs used where possible | A QVD is a file containing a table of data exported from Qlik Sense. This file format is optimized for speed when reading data from a script, but is still very compact. Reading data from a QVD file is typically 10-100 times faster than reading from other data sources. For more information, see: [*Working with QVD files*](../Scripting/work-with-QVD-files.htm). |
| QVD files optimized on load | QVD files can be read in two modes: standard (fast) and optimized (faster). The selected mode is determined automatically by the script engine. There are some limitations regarding optimized loads. It is possible to rename fields, but any of these operations will result in a standard load:   - Any transformations on the fields that are loaded. - Using a where clause causing Qlik Sense to unpack the records. - Using Map on a field that is loaded. |
| Incremental loads leveraged | If your application connects to a large amount of data from databases that are continuously updated, reloading the entire data set can be time consuming. Instead, you should use incremental load to retrieve new or changed records from the database. For more information, see [*Loading new and updated records with incremental load*](../LoadData/use-QVD-files-incremental-load.htm). |
| Snowflake model consolidated | If you have a snowflake data model, you may be able to reduce the number of data tables by joining some of them using the Join prefix or other mapping. This is especially important for large fact tables. A good rule of thumb is to have only one large table. For more information see [To Join or Not to Join](https://community.qlik.com/t5/Qlik-Design-Blog/To-Join-or-not-to-Join/ba-p/1463102). |
| Tables that have a small number of fields are denormalized | If you have two tables with few fields, it may improve performance to join them. For more information, see [*Combining tables with Join and Keep*](../Scripting/combine-tables-with-join-keep.htm). |
| Denormalized lookup (leaf) tables with mapping loads | You should not use the Join prefix if you only need to add one field from a table to another. You should use the ApplyMap lookup function, see [Don't join - use ApplyMap](https://community.qlik.com/t5/Qlik-Design-Blog/Don-t-join-use-Applymap-instead/ba-p/1467592). |
| Time stamps removed or decoupled from date field | Date fields can fill up space when the timestamp is present as the string representation is larger, and the number of distinct values is larger. If the precision is not necessary for your analysis, you can round the timestamp to e.g. the nearest hour using Timestamp(Floor(YourTimestamp,1/24)) or remove the time component completely using Date(Floor(YourTimestamp)).  If you want the timestamp, you can decouple it from the date itself. You can use the same Floor() function, and then create a new field with the extracted time by using something along the lines of: Time(Frac(YourTimestamp)). |
| Unnecessary fields removed from data model | You should only load necessary fields in your data model. Avoid using Load \* and SELECT. Make sure you keep:   - Fields that are necessary for your analysis. - Fields that are actually being used in the application. |
| Link tables avoided when dealing with high data volumes | You should use link tables where possible. However, if you are dealing with large data volumes, concatenated tables can out-perform link tables. |
| Concatenated dimensions broken to new fields | You should break apart concatenated dimensions into separate fields. This reduces the number of unique occurrences of values in your fields. This is similar to how timestamps can be optimized. |
| AutoNumber used where possible | You can create an optimized load by loading your data from a QVD file first, and then using the AutoNumber statement to convert values to symbol keys. For more information, see [*AutoNumber*](../Scripting/ScriptRegularStatements/Autonumber.htm). |
| Data islands avoided | Data islands can be useful, but they usually affect performance. If you are creating islands for selection values, use variables. |
| QVDs are stored based on incremental timeframes | You should store QVD in segments, such as monthly. These smaller monthly QVD can then support many different applications that might not need all of the data. |

## Sheet performance

These are best practices that will improve performance of [sheets](#glossary-7 "Glossary term") and [visualizations](#glossary-8 "Glossary term").

Sheet performance best practices

| Action | Description |
| --- | --- |
| The If() function is avoided where possible | If the  If() function is used inside an aggregation function, it will operate at the record level and be evaluated many times.  For example, if you have 1000 records in an aggregation, an If() condition will be evaluated 1000 times. This could cascade rapidly if you nest statements. You should use set analysis instead. A set analysis filter is applied before the aggregation, resulting in a faster response. These responses can also be cached via set analysis, where If() cannot. You could also consider other functions and modifications to the data model. |
| Fields from different tables inside an aggregation table are avoided where possible. | When an aggregation is evaluated, the calculation runs through two steps:   1. The first step is finding the relevant combinations on which the to make the calculation. This step is single-threaded. 2. The second step is performing the calculation. This step is multi-threaded.   The single-threaded part can affect performance considerably. One example is if you have multiple fields inside the aggregation, for example, Sum(Quantity\*ListPrice). If Quantity is in the fact table, and ListPrice is in the master products table, the engine first needs to join the two tables to find the combinations before it can start to sum the product. The joining is the single-threaded part, and the summing is multi-threaded. If both fields are found in the same table, no join is necessary, and the aggregation is evaluated considerably faster. |
| Aggr() and nested Aggr() functions are used minimally | The Aggr() function greatly affects performance. Incorrect use can give inaccurate results. For example, in a table with dimensions that vary from the dimensions within the Aggr() function. For more information, see [When should AGGR not be used?](https://community.qlik.com/t5/Qlik-Design-Blog/When-should-the-Aggr-function-NOT-be-used/ba-p/1467855) |
| Set analysis is used where possible | You can use set analysis to define a set of data values that is different from the normal set defined by the current selections. For more information, see [*Set analysis*](../ChartFunctions/SetAnalysis/set-analysis-expressions.htm). |
| String comparisons avoided where possible | String comparisons are not as efficient as set analysis. For example, you should avoid Match(), MixMatch(), WildMatch(), and Pick(). Create flags in the script or use set analysis instead. For more information, see [*Conditional functions*](../Scripting/ConditionalFunctions/conditional-functions.htm) and [Performance of conditional aggregations](https://community.qlik.com/t5/Qlik-Design-Blog/Performance-of-Conditional-Aggregations/ba-p/1463021). |
| Calculation conditions are used on objects containing intensive calculations | You may have visualizations with many records when there are no selections. As a best practice, add calculation conditions to objects so that they only render after certain selections have been made. This stops the creation of very large hypercubes. For example: GetSelectedCount([Country])=1 OR GetPossibleCount([Country])=1. In this scenario, the [visualization](#glossary-9 "Glossary term") will not render unless the user selects a single country, or makes other selections where only a single country is possible. |
| Measures are pre-calculated in the script where possible | Any measure that is at the lowest level of granularity of the data model should be calculated in the script. For example, if in the same record in a table you have Sales and Cost, you could derive the margin by calculating Sales - Cost AS Margin. You can also aggregate other values in advance if you know that they will not vary based on selection, or that are bound to a different level of granularity. |
| Tables have less than 15 columns and have calculation conditions | A table with 15 columns could be considered wide. If your tables consist of many records, you should use calculated conditions on the table object so that it only renders after certain selections or criteria have been met. If your table is very wide, consider:   - Creating multiple smaller tables that show conditionally. - Using methods to conditionally show columns. - Keeping your tables limited to only what fields are necessary for your analysis. |
| Sheets do not have an excessive number of objects | Objects are calculated when the user navigates to the sheet. Every time a user makes a selection on that sheet, each object will be recalculated if that current state does not exist in the cache. If you have a sheet with many charts, the user will have to wait for every object to calculate on nearly every selection. This puts significant load on the engine. As a best practice, follow the Dashboard/Analysis/Reporting (DAR)  concept to develop a clean and minimal application. For more information, see [DAR methodology](https://community.qlik.com/t5/Qlik-Design-Blog/DAR-methodology/ba-p/1466733). |
| Numeric flags are leveraged in the script for use in set analysis | Set analysis with flags can be more efficient than using string comparisons or multiplication. |
| Master items or [variables](#glossary-10 "Glossary term") used for expressions | Master items enable drag and drop of governed metrics and guarantee that expressions will be cached. For example, Sum(Sales) is different from SUM(Sales). Expressions are cached on spelling and case, and need to match verbatim in order to be reused. |

## Data load performance

Optimizing data loading is important for a seamless and responsive experience when working with applications in Qlik Cloud. This section highlights performance-affecting factors and provides guidance on how to prevent performance issues.

### Qlik Data Gateway - Direct Access

When you use Qlik Data Gateway - Direct Access to reload data into your application, the following factors affect performance:

- Connection speed and latency between the machine hosting the Data Gateway and the database.
- Connection speed and latency between the machine hosting the Data Gateway and your Qlik Cloud tenant. Ideally, host the Data Gateway in the same region as your Qlik Cloud tenant for improved performance.

### Database storage

Slow storage connections can increase reload times. Consider the following for databases hosted on-premises or in the cloud:

- On-premises: If your database is on-premises and shares a server with other applications, its performance might be impacted by the activities of these other applications.
- Cloud: When sized correctly, cloud databases typically offer better performance than on-premise databases. For optimal results, choose a region for your cloud storage that is close to your Qlik Cloud tenant.
