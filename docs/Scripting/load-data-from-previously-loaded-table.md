---
title: "Loading data from a previously loaded table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/load-data-from-previously-loaded-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Logical tables"]
---

# Loading data from a previously loaded table

There are two ways to load and transform data from a table that already has been loaded.

- Resident LOAD - where you use the Resident predicate in a subsequent LOAD statement to load a new table.
- Preceding load - where you load from the preceding LOAD or SELECT statement without specifying a source.

## Resident or preceding LOAD?

In most cases, the same result can be achieved by using either method. A preceding LOAD is generally the faster option, but there are some cases where you need to use a Resident LOAD instead:

- If you want to use the Order\_by clause to sort the records before processing the LOAD statement.
- If you want to use any of the following prefixes, in which cases preceding LOAD is not supported:
  - Crosstable
  - Join
  - Intervalmatch

## Resident LOAD

You can use the Resident predicate in a LOAD statement to load data from a previously loaded table. This is useful when you want to perform calculations on data loaded with a SELECT statement where you do not have the option to use Qlik Sense functions, such as date or numeric value handling.

Example:

In this example, the date interpretation is performed in the Resident load as it can't be done in the initial Crosstable LOAD.

PreBudget:
Crosstable (Month, Amount, 1)
LOAD Account,
Jan,
Feb,
Mar,
…
From Budget;
Budget:
Noconcatenate
LOAD
Account,
Month(Date#(Month,'MMM')) as Month,
Amount
Resident PreBudget;
Drop Table PreBudget;

Tip noteA common case for using Resident is where you want to use a temporary table for calculations or filtering. Once you have achieved the purpose of the temporary table, it should be dropped using the Drop table statement.

## Preceding load

The [preceding load](#glossary-0 "Glossary term") feature allows you to load a table in one pass, but still define several successive transformations. Basically, it is a LOAD statement that loads from the LOAD or SELECT statement below, without specifying a source qualifier such as From or Resident as you would normally do. You can stack any number of LOAD statements this way. The statement at the bottom will be evaluated first, then the statement above, and so on until the top statement has been evaluated.

You can achieve the same result using Resident, but in most cases a preceding LOAD will be faster.

Another advantage of preceding load is that you can keep a calculation in one place, and reuse it in LOAD statements placed above.

Example 1: Transforming data loaded by a SELECT statement

If you load data from a database using a SELECT statement, you cannot use Qlik Sense functions to interpret data in the SELECT statement. The solution is to add a LOAD statement, where you perform data transformation, above the SELECT statement.

In this example we interpret a date stored as a string using the Qlik Sense function Date# in a LOAD statement, using the previous SELECT statement as source.

LOAD Date#(OrderDate,'YYYYMMDD') as OrderDate;
SQL SELECT OrderDate FROM … ;

Example 2: Simplifying your script by reusing calculations

In this example we use a calculation more than once in the script:

LOAD Age(FromDate + IterNo() – 1, BirthDate ) as Age,
Date(FromDate + IterNo() – 1 ) as ReferenceDate
Resident Policies
While IterNo() <= ToDate - FromDate + 1 ;

By introducing the calculation in a first pass, we can reuse it in the Age function in a preceding LOAD:

LOAD ReferenceDate,
Age(ReferenceDate, BirthDate ) as Age;
LOAD \*,
Date(FromDate + IterNo() – 1 ) as ReferenceDate
Resident Policies
While IterNo() <= ToDate - FromDate + 1 ;

### Limitations of preceding loads

- The following prefixes cannot be used in conjunction with preceding LOAD: Join, Crosstable and Intervalmatch.
- If you are using distinct to load unique records, you need to place distinct in the first load statement, as distinct only affects the destination table.

## Learn more

- [*Load*](ScriptRegularStatements/Load.htm)
- [*Drop table*](ScriptRegularStatements/drop-table.htm)
