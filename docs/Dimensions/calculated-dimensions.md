---
title: "Calculated dimensions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/calculated-dimensions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Data grouping with dimensions"]
---

# Calculated dimensions

You can use expressions to create calculated [dimensions](#glossary-0 "Glossary term"). A calculated dimension consists of an expression involving one or more fields. All standard functions may be used.

Information noteFor performance reasons, it is recommended to perform all calculations in the data load editor. When dimensions are calculated in the [chart](#glossary-1 "Glossary term"), Qlik Sense first calculates the dimension values, and then aggregates the [measures](#glossary-2 "Glossary term") for these calculated values, which affects the performance more than calculations in the [load script](#glossary-3 "Glossary term").

There are cases when calculated dimensions are powerful in data analysis, for example, if you want to generate the dimensions values during analysis, when dimension values are dependent on the [selections](#glossary-4 "Glossary term").

Calculated dimensions are also useful if you want to modify a [field](#glossary-5 "Glossary term").

Once you have created a calculated dimension, you can use it as any other dimension.

Example:

You have a field called Calendar Month that includes each of the months of the year. In your application, you want include a table that shows the sales for each of the first 6 months of the year. For the rest of the months, you want to see a total. You can use an expression to create this calculated dimension.

Syntax:

If ([Calendar Month] <7, [Calendar Month], 'Rest')

## Learn more

- [*Creating a calculated dimension*](create-calculated-dimension.htm)
