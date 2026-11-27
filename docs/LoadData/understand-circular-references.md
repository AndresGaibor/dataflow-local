---
title: "Understanding and solving circular references"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/understand-circular-references.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Logical tables"]
---

# Understanding and solving circular references

If there are circular references ("loops") in a data structure, the tables are associated in such a way that there is more than one path of associations between two fields.

This type of data structure should be avoided as much as possible, since it might lead to ambiguities in the interpretation of data.

Three tables with a circular reference, since there is more than one path of associations between two fields.

![Three tables with a circular reference.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_CircularTables.png "Click to view full size")

Qlik Sense solves the problem of circular references by breaking the loop with a loosely coupled table. When Qlik Sense finds circular data structures while executing the [load script](#glossary-0 "Glossary term"), a warning dialog will be shown and one or more tables will be set as loosely coupled. Qlik Sense will typically attempt to loosen the longest table in the loop, as this is often a transaction table, which normally should be the one to loosen. In the data model viewer, loosely-coupled tables are indicated by the red dotted links to other tables.

Example:

Data is loaded from three tables that include the following:

- Names of some national soccer teams
- Soccer clubs in some cities
- Cities of some European countries

View of the source data tables in Excel.

![Tables in Excel.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_CircularRefData.png "Click to view full size")

This data structure is not very good, since the [field](#glossary-1 "Glossary term") name Team is used for two different purposes: national teams and local clubs. The data in the tables creates an impossible logical situation.

When loading the tables into Qlik Sense, Qlik Sense determines which of the [data connections](#glossary-2 "Glossary term") that is least important, and loosens this table.

Open the [Data model viewer](#glossary-3 "Glossary term") to see how Qlik Sense interprets the relevance of the data connections:

View of the circular references as noted by red dotted lines.

![Circular references between tables.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_Circular.png "Click to view full size")

The table with cities and the countries they belong to is now loosely coupled to the table with national teams of different countries and to the table with local clubs of different cities.

## Solving circular references

When circular references occur, you need to edit the data load script by assigning a unique name to one of the fields with identical names.

Do the following:

1. Open the data load editor.
2. Edit the LOAD statement for one of the duplicate field names.

   In this example, the LOAD statement of the table that holds the local teams and their cities would include with a new name for Team, for example LocalClub. The updated LOAD statement reads:

   LOAD City, Team as LocalClub

3. Click ![load data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_play_2_outline.svg) in the toolbar to reload data in the application.

You now have logic that works throughout all the tables. In this example, when Germany is selected, the national team, the German cities and the local clubs of each city are associated:

![Sheet with four tables.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_CircularSolved.png)

When you open the Data model viewer, you see that the loosely coupled connections are replaced with regular connections:

![Three tables with regular connections in the Data model viewer.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_CircularSolved_dmv.png)

Related learning:

- [Introduction to the data model viewer](/lnk/Intro_Data_Model_Viewer_QS)
