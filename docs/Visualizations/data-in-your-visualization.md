---
title: "Using data assets in visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/data-in-your-visualization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Using data assets in visualizations

[Visualizations](#glossary-0 "Glossary term") use data in many different ways. How your data is comprised or created impacts your visualizations. Primarily, your data assets become [dimensions](#glossary-1 "Glossary term") and [measures](#glossary-2 "Glossary term") in your visualizations, defining the categories in your visualizations and the measurements of those categories. A [field](#glossary-3 "Glossary term") can be used to group data, or it can be transformed with an aggregate function to provide a measurement in data categories.

The types of data you have in your tables and fields also impacts whether they can be used as dimensions or measures, as well as what sorting options are most effective. For example, quantitative data and qualitative data have different recommended uses when they are used as either dimensions or measures.

In addition to providing the data to display, data assets can be used to control what data is displayed and how it is presented. For example, you can color a visualization using a dimension or measure not present in the visualization. For more information, see [*Changing the appearance of a visualization*](change-appearance-of-visualization.htm).

In sheet edit mode, the assets panel contains the different data sources you can use in your visualizations.
 For more information, see [*Assets panel in edit mode*](../Sheets/sheet-view.htm#Assets).

## Data assets

The following data assets are available when creating visualizations:

- Fields
- Measures
- Dimensions
- Master items

### Fields

Fields hold the data loaded into Qlik Sense. Fields contain one or more values and correspond to columns in a database table. The field data can be qualitative or quantitative.

When creating visualizations, you use fields to create your dimensions and measures. You can also use fields in different ways when you add visualizations to your application. Some visualizations, such as tables, can present fields in an unmodified state.

Some fields require extra considerations, such as date or time fields.

For more information, see [*Fields*](../DataSource/fields.htm).

### Measures

Measures are the data that you want to show. Measures are created from an expression composed of aggregation functions, such as Sum or Max, combined with one or several fields.

For more information, see [*Measures*](../Measures/measures.htm).

### Dimensions

Dimensions determine how the data in a visualization is grouped. For example: total sales per country or number of products per supplier. Dimensions display the distinct values from the field selected as a dimension. Dimensions can also be calculated using an expression.

For more information, see [*Data grouping with dimensions*](../Dimensions/dimensions.htm).

### Master items

Master items are dimensions, measures, or visualizations that can be reused in other visualizations and [sheets](#glossary-5 "Glossary term") in your application. Updating a [master item](#glossary-6 "Glossary term") updates every instance of it. This means you could have the same measure in 5 visualizations, and they would all update whenever the master item is changed.

Master items also have more design options available. You can, for example, assign colors to a master dimension distinct values so that the distinct values are consistent across visualizations.

Master items also include special dimensions such as drill-down dimensions and calendar measures.

For more information, see [*Reusing assets with master items*](../Assets/work-with-master-items.htm).

## Expressions

An expression is a combination of functions, fields, and mathematical operators (+ \* / =). Expressions are used to process data in the application in order to produce a result that can be seen in a [visualization](#glossary-7 "Glossary term").

Expressions are used primarily used to create measures. They can also be used to build calculated dimensions, or to set [properties](#glossary-8 "Glossary term") within different visualizations. For example, you can use expressions to define range limits for gauges, or reference lines for bar charts.

For more information, see [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm).

## Data types in visualizations

Different types of data have different properties; certain data may work better as dimensions, and some as measures. Similarly, as dimensions or measures, certain kinds of data may work better as a dimension in some visualizations better than others, or as a measure with certain [aggregation](#glossary-9 "Glossary term") functions.

The data in your fields can be quantitative or qualitative. Quantitative data values are measured numerically on an ascending scale. Quantitative data can be ratios or intervals:

- Ratio: Ratios are quantitative data that you can perform arithmetic operations on, such as cost or age.

  For example, you can sum sales values for the month to get totals.
- Interval: Intervals are quantitative data that you cannot perform arithmetic operations on.

  For example, you cannot calculate a sum of temperatures during the week, but you can calculate the average temperature per day, and the high/low for each day.

Qualitative data can not be measured numerically, but can be described through language. Qualitative data can be nominal or ordinal:

- Nominal: Fields with nominal data have distinct qualitative values, but without a set order.

  For example, product names or customer names are nominal data, as they have distinct values, but do not have a required order.
- Ordinal: Fields with ordinal data have qualitative values that have a ranked or positioned value. Ordinal data should be sorted by its order as opposed to alphabetically.

  For example, low, medium, high are ordinal values. Small, medium, and large are also ordinal values.

The following table contains a general overview of recommended visualization types and aggregation functions for data types. These recommendations should not be considered absolute.

Visualization recommendations for data types as measures

| Data type | Recommended aggregation functions | Non-recommended aggregation functions |
| --- | --- | --- |
| Nominal | Count | Average  Median  Sum |
| Ordinal | Count  Median | Average  Sum |
| Ratio | Count  Average  Median | Sum |
| Interval | Count  Average  Median  Sum | - |

Related learning:

- [Understanding dimensions and measures](/lnk/Understand_Dimensions_Measures_QS)
