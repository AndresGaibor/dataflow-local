---
title: "Renaming fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/rename-fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Fields"]
---

# Renaming fields

Sometimes it is necessary to rename [fields](#glossary-0 "Glossary term") in order to obtain the desired associations. The three main reasons for renaming fields are:

- Two fields are named differently although they denote the same thing:
  - The field ID in the Customers table
  - The field CustomerID
    in the Orders table

  The two fields denote a specific customer identification code and should both be named the same, for example CustomerID.
- Two fields are named the same but actually
  denote different things:

- The field Date in the Invoices table
- The field Date in the Orders table

The two fields should preferably be renamed, to for example InvoiceDate and OrderDate.

- There may be errors such as misspellings in the database or different
  conventions on upper- and lowercase letters.

Since fields can be renamed in the script, there is no need to change the
original data. There are two different ways to rename fields as shown in the examples.

Example 1:  Using the alias statement

The LOAD or SELECT statement can be preceded by an alias statement.

Alias ID
as CustomerID;

LOAD \* from
Customer.csv;

Example 2:  Using the as specifier

The LOAD or SELECT statement can contain the as specifier.

LOAD ID
as CustomerID, Name, Address, Zip, City, State from Customer.csv;

## Learn more

- [*Alias*](ScriptRegularStatements/Alias.htm)
- [*Fields*](fields.htm)
- [Associating Tables and Transforming Data](/lnk/Assoc_tables_transform_data_QS)

Related learning:

- [Associating Tables and Transforming Data](/lnk/Assoc_tables_transform_data_QS)
