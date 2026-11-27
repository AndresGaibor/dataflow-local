---
title: "InEnvironment"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/InEnvironment.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# InEnvironment

The InEnvironment script keyword is used as an element within an IncludeModel statement.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

Syntax:

InEnvironment environment\_name

Arguments

| Argument | Description |
| --- | --- |
| environment\_name | The name of the environment, if applicable, containing the data product you want to load.  Follow the quoting conventions documented at [*Using quotation marks in the script*](../use-quotes-in-script.htm). Examples:  Production  [Production Environment]  "Production Environment" |

Example:

```
InEnvironment MySalesAnalysisEnvironment
```

## Learn more

- [*IncludeModel*](IncludeModel.htm)
- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
