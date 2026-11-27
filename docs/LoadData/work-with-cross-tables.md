---
title: "Working with crosstables in the data load script"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/work-with-cross-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Working with crosstables in the data load script

A crosstab is a common type of table featuring a matrix of values between two orthogonal lists of header data. It is usually not the optimal data format if you want to associate the data to other data tables.

This topic describes how you can unpivot a crosstab, that is, transpose parts of it into rows, using the crosstable prefix to a LOAD statement in the data [load script](#glossary-0 "Glossary term").

## Unpivoting a crosstab with one qualifying column

A crosstab is often preceded by a number of qualifying columns, which should be read in a straightforward way. In this case there is one qualifying column, Year, and a matrix of sales data per month.

Crosstab with one qualifying column

| Year | Jan | Feb | Mar | Apr | May | Jun |
| --- | --- | --- | --- | --- | --- | --- |
| 2008 | 45 | 65 | 78 | 12 | 78 | 22 |
| 2009 | 11 | 23 | 22 | 22 | 45 | 85 |
| 2010 | 65 | 56 | 22 | 79 | 12 | 56 |
| 2011 | 45 | 24 | 32 | 78 | 55 | 15 |
| 2012 | 45 | 56 | 35 | 78 | 68 | 82 |

If this table is simply loaded into Qlik Sense, the result will be one [field](#glossary-1 "Glossary term") for Year and one field for each of the months. This is generally not what you would like to have. You would probably prefer to have three fields generated:

- The qualifying column, in this case Year, marked with green in the table above.
- The attribute field, in this case represented by the month names Jan - Jun marked with yellow. This field can suitably be named Month.
- The data matrix values, marked with blue. In this case they represent sales data, so this can suitably be named Sales.

This can be achieved by adding the crosstable prefix to the LOAD or SELECT statement, for example:

crosstable (Month, Sales) LOAD \* from ex1.xlsx;

This creates the following table in Qlik Sense:

Table with crosstable prefix added to the LOAD or SELECT statement

| Year | Month | Sales |
| --- | --- | --- |
| 2008 | Jan | 45 |
| 2008 | Feb | 65 |
| 2008 | Mar | 78 |
| 2008 | Apr | 12 |
| 2008 | May | 78 |
| 2008 | Jun | 22 |
| 2009 | Jan | 11 |
| 2009 | Feb | 23 |
| ... | ... | ... |

## Unpivoting a crosstab with two qualifying columns

In this case there are two qualifying columns to the left, followed by the matrix columns.

Crosstab with two qualifying columns

| Salesman | Year | Jan | Feb | Mar | Apr | May | Jun |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A | 2008 | 45 | 65 | 78 | 12 | 78 | 22 |
| A | 2009 | 11 | 23 | 22 | 22 | 45 | 85 |
| A | 2010 | 65 | 56 | 22 | 79 | 12 | 56 |
| A | 2011 | 45 | 24 | 32 | 78 | 55 | 15 |
| A | 2012 | 45 | 56 | 35 | 78 | 68 | 82 |
| B | 2008 | 57 | 77 | 90 | 24 | 90 | 34 |
| B | 2009 | 23 | 35 | 34 | 34 | 57 | 97 |
| B | 2010 | 77 | 68 | 34 | 91 | 24 | 68 |
| B | 2011 | 57 | 36 | 44 | 90 | 67 | 27 |
| B | 2012 | 57 | 68 | 47 | 90 | 80 | 94 |

The number of qualifying columns can be stated as a third parameter to the crosstable prefix as follows:

crosstable (Month, Sales, 2) LOAD \* from ex2.xlsx;

This creates the following result in Qlik Sense:

Table with qualifying columns stated as a third parameter to the crosstable prefix

| Salesman | Year | Month | Sales |
| --- | --- | --- | --- |
| A | 2008 | Jan | 45 |
| A | 2008 | Feb | 65 |
| A | 2008 | Mar | 78 |
| A | 2008 | Apr | 12 |
| A | 2008 | May | 78 |
| A | 2008 | Jun | 22 |
| A | 2009 | Jan | 11 |
| A | 2009 | Feb | 23 |
| ... | ... | ... | ... |

## Learn more

- [*Crosstable*](../Scripting/ScriptPrefixes/crosstable.htm)
