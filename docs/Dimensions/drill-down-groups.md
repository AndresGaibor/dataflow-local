---
title: "Drill-down groups"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/drill-down-groups.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Data grouping with dimensions"]
---

# Drill-down groups

When several fields form a natural hierarchy, it can make sense to create a drill-down group.

Example 1:

Organization: Company, Department, Employee

Example 2:

Geography: Continent, Country, State, City

When you use a drill-down group as a [dimension](#glossary-0 "Glossary term") in a [chart](#glossary-1 "Glossary term"), the chart uses the first [field](#glossary-2 "Glossary term") in the group's list of fields that has more than one possible value. If the currently made [selections](#glossary-3 "Glossary term") cause the field to have only one possible value, the next field in the list is used instead, provided that it has more than one possible value. If no field in the list has more than one possible value, the last field is used anyway.

In the first example above, Company will be used as chart dimension until a single company is selected. The chart will then show Department. If a single department is selected, the chart will switch to Employee.

As selections are reverted, so that more than one value becomes possible in the upper fields of the group's field list, the chart is automatically drilled back up.

## Drill-up

The drill-up function is available in bar charts, pie charts, and line charts. Other [visualizations](#glossary-4 "Glossary term") reflect the changes made in the charts, but cannot themselves be used to drill up through the different dimensions. When you drill down in a dimension group, breadcrumbs provide links back to the previous dimensions. Click the dimension that you want to drill up to.

In the following bar chart, the breadcrumbs Year > Quarter > Month enable drilling up.

![Bar chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Breadcrumbs.png)

## Learn more

- [*Creating a drill-down dimension*](create-drill-down-dimension.htm)
- [Select data](/lnk/Select_Data_QS)

Related learning:

- [Select data](/lnk/Select_Data_QS)
