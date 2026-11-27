---
title: "WithDimensions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/WithDimensions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# WithDimensions

The WithDimensions script keyword is used as an element within an IncludeModel statement. WithDimensions specifies the dimensions from the data product's semantic model to define as master dimensions in the application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

Syntax:

WithDimensions dimensionlist

Arguments

| Argument | Description |
| --- | --- |
| dimensionlist | List of dimensions from data product's semantic model to be converted into master dimensions.  You can use \* to convert all dimensions, or provide a comma-separated list of specific dimensions.  Example:  [Product Name], [Region], [Customer] |

## Learn more

- [*IncludeModel*](IncludeModel.htm)
- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
