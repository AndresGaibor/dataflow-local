---
title: "Using mapping as an alternative to joining"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-mapping-as-alternative-join.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---
# Using mapping as an alternative to joining

The Join prefix in Qlik Sense is a powerful way of combining several data tables in the data model.

One disadvantage is that the combined tables can become large and create performance problems. An alternative to Join in situations where you need to look up a single value from another table is to use mapping instead. This can save you from loading unnecessary data that slows down calculations and potentially can create calculation errors, as joins can change the number of records in the tables.

A mapping table consists of two columns: a comparison [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-mapping-as-alternative-join.htm#glossary-0 "Glossary term") (input) and a mapping value field (output).

In this example we have a table of orders (Orders), and need to know the countries of the customers, which are stored in the customer table (Customers).

Orders data table

| OrderID | OrderDate | ShipperID | Freight | CustomerID |
| --- | --- | --- | --- | --- |
| 12987 | 2007-12-01 | 1 | 27 | 3 |
| 12988 | 2007-12-01 | 1 | 65 | 4 |
| 12989 | 2007-12-02 | 2 | 32 | 2 |
| 12990 | 2007-12-03 | 1 | 76 | 3 |

Customers data table

| CustomerID | Name | Country | ... |
| --- | --- | --- | --- |
| 1 | DataSales | Spain | ... |
| 2 | BusinessCorp | Italy | ... |
| 3 | TechCo | Germany | ... |
| 4 | Mobecho | France | ... |

In order to look up the country (Country) of a customer, we need a mapping table that looks like this:

Mapping table

| CustomerID | Country |
| --- | --- |
| 1 | Spain |
| 2 | Italy |
| 3 | Germany |
| 4 | France |

The mapping table, which we name MapCustomerIDtoCountry, is defined in the script as follows:

MapCustomerIDtoCountry:
Mapping LOAD CustomerID, Country From Customers ;

The next step is to apply the mapping, by using the ApplyMap function when loading the order table:

Orders:
LOAD \*,
ApplyMap('MapCustomerIDtoCountry', CustomerID, null()) as Country
From Orders ;

The third parameter of the ApplyMap function is used to define what to return when avalue is not found in the mapping table, in this case Null().

The resulting table will look like this:

Result table

| OrderID | OrderDate | ShipperID | Freight | CustomerID | Country |
| --- | --- | --- | --- | --- | --- |
| 12987 | 2007-12-01 | 1 | 27 | 3 | Germany |
| 12988 | 2007-12-01 | 1 | 65 | 4 | France |
| 12989 | 2007-12-02 | 2 | 32 | 2 | Italy |
| 12990 | 2007-12-03 | 1 | 76 | 3 | Germany |

## Learn more

- [*ApplyMap Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/ApplyMap.htm)
- [*Mapping*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptPrefixes/Mapping.htm)
