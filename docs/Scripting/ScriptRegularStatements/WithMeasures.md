---
title: "WithMeasures"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/WithMeasures.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# WithMeasures

The WithMeasures script keyword is used as an element within an IncludeModel statement. WithMeasures specifies the measures from the data product's semantic model to define as master measures in the application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

Syntax:

WithMeasures measurelist

Arguments

| Argument | Description |
| --- | --- |
| measurelist | List of measures from data product's semantic model to be converted into master measures.  You can use \* to convert all measures, or provide a comma-separated list of specific measures.  Example:  [Sales], [Total Quantity], [Cost] |

## Learn more

- [*IncludeModel*](IncludeModel.htm)
- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
