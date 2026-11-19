---
title: "LookUp Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/LookUp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---
# LookUp Script function

LookUp() looks into a table that is already loaded and returns the value of field\_name corresponding to the first
occurrence of the value match\_field\_value
in the field match\_field\_name.
The table can be the current table or another table previously loaded.

Syntax:

LookUp(field\_name,
match\_field\_name, match\_field\_value [, table\_name])

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| field\_name | Name of the field for which the return value is required. Input value must be given as a string (for example, quoted literals). |
| match\_field\_name | Name of the field to look up match\_field\_value in. Input value must be given as a string (for example, quoted literals). |
| match\_field\_value | Value to look up in match\_field\_name [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/LookUp.htm#glossary-0 "Glossary term"). |
| table\_name | Name of the table in which to look up the value. Input value must be given as a string (for example quoted literals).  If table\_name is omitted the current table is assumed. |

> **Note:** Arguments without quotes refer to the current table. To refer to other tables, enclose an argument in single quotes.

Limitations:

The order in which the search is made is the load
order, unless the table is the result of complex operations such as joins,
in which case, the order is not well defined. Both field\_name
and match\_field\_name must be fields
in the same table, specified by table\_name.

If no match is found, NULL
is returned.

Example

### Load script

Load the following data as an inline load in the data load editor to create the example below.

```
ProductList:
Load * Inline [
ProductID|Product|Category|Price
1|AA|1|1
2|BB|1|3
3|CC|2|8
4|DD|3|2
] (delimiter is '|');
 
OrderData:
Load *, Lookup('Category', 'ProductID', ProductID, 'ProductList') as CategoryID
Inline [
InvoiceID|CustomerID|ProductID|Units
1|Astrida|1|8
1|Astrida|2|6
2|Betacab|3|10
3|Divadip|3|5
4|Divadip|4|10
] (delimiter is '|');
 
Drop Table ProductList;
```

For more information about using inline loads, see [*Using inline loads to load data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/inline-loads-qs.htm).

### Create a visualization

Create a table [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/LookUp.htm#glossary-1 "Glossary term") in a Qlik Sense [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/LookUp.htm#glossary-2 "Glossary term"). Add fields ProductID, InvoiceID, CustomerID, Units, and CategoryID to the table.

### Result

Resulting table

| ProductID | InvoiceID | CustomerID | Units | CategoryID |
| --- | --- | --- | --- | --- |
| 1 | 1 | Astrida | 8 | 1 |
| 2 | 1 | Astrida | 6 | 1 |
| 3 | 2 | Betacab | 10 | 2 |
| 3 | 3 | Divadip | 5 | 2 |
| 4 | 4 | Divadip | 10 | 3 |

### Explanation

The sample data uses the Lookup() function in the following form:

`Lookup('Category', 'ProductID', ProductID, 'ProductList')`

The ProductList table is loaded first.

The Lookup() function is used to build the OrderData table. It specifies the third argument as ProductID. This is the field for which the value is to be looked up in the second argument 'ProductID' in the ProductList, as denoted by the enclosing single quotes.

The function returns the value for 'Category' (in the ProductList table), loaded as CategoryID.

The drop statement deletes the ProductList table from the data model because it is not required, which leaves the resulting OrderData table.

> **Note:** The Lookup() function is flexible and can access any previously loaded table. However, it is slow compared with the Applymap() function.

## Learn more

- [*ApplyMap Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/MappingFunctions/ApplyMap.htm)
