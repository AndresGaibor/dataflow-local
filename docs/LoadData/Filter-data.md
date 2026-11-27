---
title: "Filtering data from files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Filter-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Adding data to the application from connections and new files"]
---

# Filtering data from files

You can create filter conditions when you add data from files. This allows you to select a subset of data to load. This can be useful when you want to reduce the amount of data loaded, or only use specific data, such as only sales over $40,000.

The first time that you add data from a file in the Add data step, you can apply filter conditions by clicking Filters.

Filters button

![Filters button.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_DataFiltersButton.png "Click to view full size")

Subsequently, you can change the conditions by clicking your table in the [Data manager](#glossary-0 "Glossary term"), and then clicking Edit this table. Click Select data from source, and then click Filters.

After you add the data to your application, and apply any filter conditions, you can then load the data into your application.

Information noteFor more advanced data manipulation, use the [Data load editor](#glossary-2 "Glossary term"). See the Scripting for beginners and Next steps in scripting tutorials to learn more.

The available filter conditions are:

- =
- >
- <
- >=
- <=
- <>

Consider the following when filtering data. Examples are provided below.

- You can apply filter conditions to numbers, dates, or text.
- Wildcard characters are not supported.
- You can apply multiple conditions. However, conflicting conditions on the same field may result in no data being returned.
- Conditions are applied alphabetically to text data. Conditions are case sensitive.
- You can use more than one letter for text data. For example, >ct will return the word cup, as will >=cu. Note that >c will also return cup.
- When you use more than one = condition, all must evaluate to true to return values. However, when you use more than one = condition on the same field, all values that evaluate to true are returned.
- The < and > conditions, when combined, must all evaluate to true to return values. If these conditions are combined with =, all conditions must evaluate to true.
- The <= and >= conditions, when combined, must all evaluate to true to return values. If these conditions are combined with =, all conditions must evaluate to true.
- Filters on date fields from QVD files are not supported.

### Examples

These examples use the following values from a single [field](#glossary-3 "Glossary term") (one column in a table): cup, fork, and knife.

- Conditions:
  - =cup
  - =fork
  - =knife
  - Returns: cup, fork, knife
  - The equals condition returns all values that are true.

- Conditions:
  - >b
  - <d
  - Returns: cup
  - The letter c is both greater than b and lesser than d.

- Conditions:
  - <b
  - >d
  - Returns: no values
  - There can be no values that are both lesser than b and greater than d.

- Conditions:
  - =fork
  - >g
  - Returns: no values
  - There can be no values that are both equal to fork and greater than g.

For information about adding data, see:

- [*Filtering data from data connectors*](Filter-data-connectors.htm)
- [*Adding data from a new data source*](adding-data-new-data-source.htm)
- [*Adding data from an existing data source*](adding-data-existing-source.htm)
