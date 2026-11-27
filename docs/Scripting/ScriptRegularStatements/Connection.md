---
title: "Connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Connection.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Connection

The Connection script keyword is used as an element within an IncludeModel statement. Connection specifies the location of the source data that is being loaded into the application, from a data product, as a table.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

Syntax:

Connection dataset\_connection

Arguments

| Argument | Description |
| --- | --- |
| dataset\_connection | A connection that can load the dataset containing the referenced table.  Depending on the location of the connection, use one of the following formats:   - environment:space:connection — Used for files located within environments (containers for data synchronized between Qlik Cloud and Qlik Talend Cloud). Environments are associated to spaces (particularly, [data spaces](#glossary-0 "Glossary term")).  For more information about environments, see [*Synchronizing and managing environments*](../../Admin/mc-administer-environments.htm). - space:connection — Used for connections with a space as the top-level storage container or in the same environment as the loading application. This could be connections located in [shared](#glossary-1 "Glossary term"), [managed](#glossary-2 "Glossary term"), or data spaces.  For example, for a dataset stored locally within Qlik Cloud (DataFiles connection), located in a space named Sales Analysis, you would use following: Sales Analysis:DataFiles - connection — Connection name only. This refers to connections located in your [personal space](#glossary-3 "Glossary term"). In this case, the connection would simply be: DataFiles   Examples:  [CustomerOrders:DataFiles]  [SalesData2026:SnowflakeSales] |

## Learn more

- [*IncludeModel*](IncludeModel.htm)
- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
