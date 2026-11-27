---
title: "FromSpace"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/FromSpace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# FromSpace

The FromSpace script keyword can be used as an element within an IncludeModel statement. It specifies to load the data product, with its semantic model, from a specified space.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

Syntax:

FromSpace data\_product\_space

Arguments

| Argument | Description |
| --- | --- |
| data\_product\_space | Specifies the space of the data product you want to load, if you are using FromSpace to explicitly specify a particular space from which to load. This is not applicable if you are using FromPersonalSpace or FromCurrentSpace.  Follow the quoting conventions documented at [*Using quotation marks in the script*](../use-quotes-in-script.htm). Examples:  MyAnalyticsSpace  "My Analytics Space"  [My Analytics Space] |

## Learn more

- [*IncludeModel*](IncludeModel.htm)
- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
