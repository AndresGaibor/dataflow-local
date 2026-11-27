---
title: "Filtering data from data connectors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Filter-data-connectors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Adding data to the application from connections and new files"]
---

# Filtering data from data connectors

Information noteFilter data is not available for all connectors.

You enter a data filter expression by selecting Filter data in the Select data to load step. Selecting Filter data opens a text box where you enter a filter expression. For example:

Sales >= 40000

Filter data selects from individual fields, such as Sales. It operates as an SQL WHERE clause. Most operators and keywords used in WHERE clauses can be used with Filter data. Valid operators include:

- =
- >
- >=
- <
- <=
- <>
- IN
- BETWEEN
- LIKE
- IS NULL
- IS NOT NULL

Qlik Sense builds a WHERE clause in the data [load script](#glossary-0 "Glossary term") from the expression entered in Filter data.

The AND operator can be used to combine operators, such as when you want to filter across more than one [field](#glossary-1 "Glossary term"). For example:

Sales <= 30000 AND RegionID = 45

The OR operator can be used to filter data that matches either condition. For example:

Name = 'Smith' OR Name = 'Jones'

You can get the same results from the IN operator. The IN operator is a shorthand method for using multiple OR conditions. For example:

Name IN ('Smith', 'Jones')

For information about adding data, see:

- [*Filtering data from files*](Filter-data.htm)
- [*Adding data from a new data source*](adding-data-new-data-source.htm)
- [*Adding data from an existing data source*](adding-data-existing-source.htm)
