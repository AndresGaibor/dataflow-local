---
title: "Synthetic keys"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/synthetic-keys.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Logical tables"]
---

# Synthetic keys

Qlik Sense creates synthetic keys when two or more data tables have two or more fields in common. These keys are anonymous fields that represent all occurring combinations of the composite key.

If you receive a warning about synthetic keys when loading data, you should review the data structure in the data model viewer. You should ask yourself whether the data model is correct or not. Sometimes it is, but most times the synthetic key is there due to an error in the script.

Multiple synthetic keys are often a symptom of an incorrect data model. However, a sure sign of an incorrect data model is if you have synthetic keys based on other synthetic keys.

Warning noteWhen the number of synthetic keys increases, depending on data amounts, table structure and other factors, Qlik Sense may or may not handle them gracefully, and may end up using excessive amount of time and/or memory. In such a case you need to re-work your script by removing all synthetic keys.

Three tables associated with synthetic key $Syn 1.

![Three tables associated with a synthetic key.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_SyntheticKeys_dmv.png "Click to view full size")

## Handling synthetic keys

If you need to avoid synthetic keys, there are a number of ways of solving this in the [data load script](#glossary-0 "Glossary term").

- Check that only fields that logically link two tables are used as keys.

  - Fields like “Comment”, “Remark” and “Description” may exist in several tables without being related, and should therefore not be used as keys.
  - Fields like “Date”, “Company” and “Name” may exist in several tables and have identical values, but still have different roles (Order Date/Shipping Date, Customer Company/Supplier Company). In such cases they should not be used as keys.
- Make sure that redundant fields aren’t used – that only the necessary fields connect. If for example a date is used as a key, make sure not to load year, month or day\_of\_month of the same date from more than one internal table.
- If necessary, form your own non-composite keys, typically using string concatenation inside an AutoNumber script function.

Related learning:

- [Introduction to the data model viewer](/lnk/Intro_Data_Model_Viewer_QS)
