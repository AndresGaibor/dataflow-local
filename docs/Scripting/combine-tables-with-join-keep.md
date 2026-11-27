---
title: "Combining tables with Join and Keep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/combine-tables-with-join-keep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting", "Transforming data"]
---

# Combining tables with Join and Keep

A join is an operation that uses two tables
and combines them into one. The records of the resulting table are combinations
of records in the original tables, usually in such a way that the two records
contributing to any given combination in the resulting table have a common
value for one or several common fields, a so-called natural join. In Qlik Sense,
joins can be made in the script, producing logical tables.

It is possible to join tables already in the script. The Qlik Sense logic will then not see the separate tables, but rather the result of the join, which is a single internal table. In some situations this is needed, but there are disadvantages:

- The loaded tables often become larger, and Qlik Sense works slower.
- Some information may be lost: the frequency (number of records) within the original table may no longer be available.

The Keep functionality, which has the effect of reducing one or both of the two tables to the intersection of table data before the tables are stored in Qlik Sense, has been designed to reduce the number of cases where explicit joins need to be used.

Information noteIn this documentation, the term join is usually used for joins made before the internal tables are created. The association made after the internal tables are created, is however essentially also a join.

## Join

The simplest way to make a join is with the Join prefix in the script, which joins the internal table with another named table or with the last previously created table. The join will be an outer join, creating all possible combinations of values from the two tables.

Example:

LOAD a, b, c from table1.csv;
join LOAD a, d from table2.csv;

The resulting internal table has the fields a, b, c and d. The number of records differs depending on the [field](#glossary-0 "Glossary term")values of the two tables.

Information noteThe names of the fields to join over must be exactly the same. The number of fields to join over is arbitrary. Usually the tables should have one or a few fields in common. No field in common will render the cartesian product of the tables. All fields in common is also possible, but usually makes no sense. Unless a table name of a previously loaded table is specified in the Join statement the Join prefix uses the last previously created table. The order of the two statements is thus not arbitrary.

For more information, see [*Join*](ScriptPrefixes/Join.htm).

## Using Join

The explicit Join prefix in the Qlik Sense script language performs a full join of the two tables. The result is one table. Such joins can often result in very large tables.

Do the following:

1. Open the Advanced Scripting Tutorial application.
2. Add a new script section in the Data load editor.
3. Call the section Transactions.
4. Under DataFiles in the right menu, click Select data.
5. Upload and then select Transactions.csv.

Tip noteUnder Field names, make sure that Embedded field names is selected to include the names of the table fields when you load the data.

6. In the Select data from window, click Add.
7. Upload and then select Salesman.xlsx.
8. In the Select data from window, click Add.

Your script should look like this:

LOAD
"Transaction ID",
"Salesman ID",
Product,
"Serial No",
"ID Customer",
"List Price",
"Gross Margin"
FROM [lib://DataFiles/Transactions.csv]
(txt, codepage is 28591, embedded labels, delimiter is ',', msq);
LOAD
"Salesman ID",
Salesman,
"Distributor ID"
FROM [lib://DataFiles/Salesman.xlsx]
(ooxml, embedded labels, table is Salesman);

9. Click Load data.
10. Open the Data model viewer. The data model looks like this:

Data model: Transactions, Salesman, and Product tables

![Data model, Transactions, Salesman, and Product tables.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_Join1.png "Click to view full size")

However, having the Transactions and Salesman tables separated may not be the required result. It may be better to join the two tables.

Do the following:

1. To set a name for the joined table, add the following line above the first LOAD statement:

```
Transactions:
```

2. To join the Transactions and Salesman tables, add the following line above the second LOAD statement:

```
Join(Transactions)
```

Your script should look like this:

```
Transactions:
LOAD
    "Transaction ID",
    "Salesman ID",
    Product,
    "Serial No",
    "ID Customer",
    "List Price",
    "Gross Margin"
FROM [lib://DataFiles/Transactions.csv]
(txt, codepage is 28591, embedded labels, delimiter is ',', msq);

Join(Transactions)
LOAD
    "Salesman ID",
    Salesman,
    "Distributor ID"
FROM [lib://DataFiles/Salesman.xlsx]
(ooxml, embedded labels, table is Salesman);
```

3. Click Load data.
4. Open the Data model viewer. The data model looks like this:

Data model: Transactions and Product tables

![Data model following Join.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_Join2.png "Click to view full size")

All the fields of the Transactions and Salesman tables are now combined into a single Transactions table.

Information noteTo learn more about when to use Join, see these blog posts in Qlik Community: [To Join or not to Join](https://community.qlik.com/t5/Qlik-Design-Blog/To-Join-or-not-to-Join/ba-p/1463102), [Mapping as an Alternative to Joining](https://community.qlik.com/t5/Qlik-Design-Blog/Mapping-as-an-Alternative-to-Joining/bc-p/1473459).
The behaviors are discussed in the context of QlikView. However, the logic applies equally to Qlik Sense.

## Keep

One of the main features of Qlik Sense is its ability to make associations between tables instead of joining them, which reduces space in memory, increases speed and gives enormous flexibility. The Keep functionality has been designed to reduce the number of cases where explicit joins need to be used.

The Keep prefix between two LOAD or SELECT statements reduces one or both of the two tables to the intersection of table data before they are stored in Qlik Sense. The Keep prefix must always be preceded by one of the keywords Inner, Left or Right. The selection of records from the tables is made in the same way as in a corresponding join. However, the two tables are not joined and will be stored in Qlik Sense as two separately named tables.

For more information, see [*Keep*](ScriptPrefixes/Keep.htm).

## Inner

The Join and Keep prefixes in the data [load script](#glossary-1 "Glossary term") can be preceded by the prefix Inner.

If used before Join, it specifies that the join between the two tables should be an inner join. The resulting table contains only combinations between the two tables with a full data set from both sides.

If used before Keep, it specifies that the two tables should be reduced to their common intersection before being stored in Qlik Sense.

Example:

In these examples we use the source tables Table1 and Table2.

Note that these are examples only. There are no accompanying exercises to be completed in Qlik Sense.

Table 1

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Table2

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

### Inner Join

First, we perform an Inner Join on the tables, resulting in VTable, containing only one row, the only record existing in both tables, with data combined from both tables.

VTable:
SELECT \* from Table1;
inner join SELECT \* from Table2;

VTable

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |

### Inner Keep

If we perform an Inner Keep instead, we will still have two tables. The two tables are associated via the common field A.

VTab1:
SELECT \* from Table1;
VTab2:
inner keep SELECT \* from Table2;

VTab1

| A | B |
| --- | --- |
| 1 | aa |

VTab2

| A | C |
| --- | --- |
| 1 | xx |

For more information, see [*Inner*](ScriptPrefixes/Inner.htm).

## Left

The Join and Keep prefixes in the data load script can be preceded by the prefix left.

If used before Join, it specifies that the join between the two tables should be a left join. The resulting table only contains combinations between the two tables with a full data set from the first table.

If used before Keep, it specifies that the second table should be reduced to its common intersection with the first table before being stored in Qlik Sense.

Example:

In these examples we use the source tables Table1 and Table2.

Table1

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Table2

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

First, we perform a Left Join on the tables, resulting in VTable, containing all rows from Table1, combined with fields from matching rows in Table2.

VTable:
SELECT \* from Table1;
left join SELECT \* from Table2;

VTable

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |
| 2 | cc | - |
| 3 | ee | - |

If we perform a Left Keep instead, we will still have two tables. The two tables are associated via the common field A.

VTab1:
SELECT \* from Table1;
VTab2:
left keep SELECT \* from Table2;

VTab1

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

VTab2

| A | C |
| --- | --- |
| 1 | xx |

For more information, see [*Left*](ScriptPrefixes/Left.htm).

## Right

The Join and Keep prefixes in the Qlik Sense script language can be preceded by the prefix right.

If used before Join, it specifies that the join between the two tables should be a Right Join. The resulting table only contains combinations between the two tables with a full data set from the second table.

If used before Keep, it specifies that the first table should be reduced to its common intersection with the second table before being stored in Qlik Sense.

Example:

In these examples we use the source tables Table1 and Table2.

Table1

| A | B |
| --- | --- |
| 1 | aa |
| 2 | cc |
| 3 | ee |

Table2

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

First, we perform a Right Join on the tables, resulting in VTable, containing all rows from Table2, combined with fields from matching rows in Table1.

VTable:
SELECT \* from Table1;
right join SELECT \* from Table2;

VTable

| A | B | C |
| --- | --- | --- |
| 1 | aa | xx |
| 4 | - | yy |

If we perform a Right Keep instead, we will still have two tables. The two tables are associated via the common field A.

VTab1:
SELECT \* from Table1;
VTab2:
right keep SELECT \* from Table2;

VTab1

| A | B |
| --- | --- |
| 1 | aa |

VTab2

| A | C |
| --- | --- |
| 1 | xx |
| 4 | yy |

For more information, see [*Right*](ScriptPrefixes/Right.htm).
