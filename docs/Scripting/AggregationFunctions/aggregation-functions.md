---
title: "Aggregation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/aggregation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
# Aggregation functions

The family of functions known as aggregation functions consists of functions that take multiple [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/aggregation-functions.htm#glossary-0 "Glossary term") values as their input and return a single result per group, where the grouping is defined by a [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/aggregation-functions.htm#glossary-1 "Glossary term") [dimension](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/aggregation-functions.htm#glossary-2 "Glossary term") or a group by clause in the script statement.

Aggregation functions include Sum(), Count(), Min(), Max(), and many more.

Most aggregation functions can be used in both the data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/aggregation-functions.htm#glossary-3 "Glossary term") and chart expressions, but the syntax differs.

Limitations:

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

When naming an entity, avoid assigning the same name to more than one field, variable, or measure. There is a strict order of precedence for resolving conflicts between entities with identical names. This order is reflected in any objects or contexts in which these entities are used. This order of precedence is as follows:

- Inside an aggregation, a field has precedence over a variable. Measure labels are not relevant in aggregations and are not prioritized.
- Outside an aggregation, a measure label has precedence over a variable, which in turn has precedence over a field name.
- Additionally, outside an aggregation, a measure can be re-used by referencing its label, unless the label is in fact a calculated one. In that situation, the measure drops in significance in order to reduce risk of self-reference, and in this case the name will always be interpreted first as a measure label, second as a field name, and third as a variable name.

## Using aggregation functions in a data load script

Aggregation functions can only be used inside LOAD  and SELECT statements.

## Using aggregation functions in chart expressions

The parameter of the aggregation function must not contain other aggregation functions, unless these inner aggregations contain the TOTAL qualifier. For
more advanced nested aggregations, use the advanced function Aggr, in combination with a specified dimension.

An aggregation function aggregates over the set of possible records defined by the selection. However, an alternative set of records
can be defined by using a set expression in [set analysis](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/AggregationFunctions/aggregation-functions.htm#glossary-4 "Glossary term").

See: [*Set analysis*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/set-analysis-expressions.htm)

## How aggregations are calculated

An aggregation loops over the records of a specific table, aggregating the records in it. For example, Count(<Field>) will count the number of records in the table where <Field> resides. Should you want to aggregate just the distinct field values, you need to use the distinct clause, such as Count(distinct <Field>).

If the aggregation function contains fields from different tables, the aggregation function will loop over the records of the cross product of the tables of the constituent fields. This has a performance penalty, and for this reason such aggregations should be avoided, particularly when you have large amounts of data.

## Aggregation of key fields

The way aggregations are calculated means that you cannot aggregate key fields because it is not clear which table should be used for the aggregation. For example, if the field <Key> links two tables, it is not clear whether Count(<Key>) should return the number of records from the first or the second table.

However, if you use the distinct clause, the aggregation is well-defined and can be calculated for a key field linked across two tables.

If you use a key field inside an aggregation function without the distinct clause, Qlik Sense will return a number which may be meaningless. The solution is to either use the distinct clause, or use a copy of the key – a copy that resides in one table only.

For example, in the following tables, ProductId is the key between the tables.

ProductId key between Products and Details tables

![Data model showing two tables linked by a key field 'ProductId'](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ProductIdDetails.png)

Count(ProductId) can be counted either in the Products table (which has only one record per product – ProductId is the primary key) or it can be counted in the Details table (which most likely has several records per product). If you want to count the number of distinct products, you should use Count(distinct ProductId). If you want to count the number of rows in a specific table, you should not use the key.

### Aggregations of key fields contained in three or more tables

The distinct prefix only works with key fields linking up to two tables. When grouping an aggregation over a key field that exists in three or more tables, any operation that requires frequency information for a field will return NULL. In the case of a key field linking three or more tables, a non-key copy of the field must be used instead.

Related learning:

- [Associating Tables and Transforming Data](https://help.qlik.com/lnk/Assoc_tables_transform_data_QS)
