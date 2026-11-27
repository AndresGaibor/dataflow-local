---
title: "WithTables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/WithTables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# WithTables

The WithTables script keyword is used as an element within an IncludeModel statement. WithTables specifies which tables from the data product to integrate into the data model of the application.

Information note

For details and full syntax specification, see [*IncludeModel*](IncludeModel.htm).

Syntax:

WithTables Table table\_name1  Fields fieldlist Connection dataset\_connection {, Table table\_nameN Fields fieldlist Connection dataset\_connection,... }

Arguments and keywords

| Argument or keyword | Description |
| --- | --- |
| [Table](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Table.htm) | Keyword specifying the use of a table. Loads one table per Table statement. |
| table\_name | Specifies the name of the table to use in the data model.  Follow the quoting conventions documented at [*Using quotation marks in the script*](../use-quotes-in-script.htm). Examples:  MyDataTable  [My Data Table]  "My Data Table" |
| [Fields](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Field.htm) | Keyword instructing to use the specified fields (fieldlist) from the table to integrate into the data model. |
| fieldlist | List of fields from the table referenced in the preceding Table statement.  You can use \* to use all fields from the table, or provide a comma-separated list of specific fields.  Examples:  Amount, Quantity, Region  [Amount], [Quantity], [Region] |
| [*Connection*](Connection.htm) | Keyword specifying to use the dataset specified in dataset\_connection. |
| dataset\_connection | A connection that can load the dataset containing the referenced table.  Depending on the location of the connection, use one of the following formats:   - environment:space:connection — Used for files located within environments (containers for data synchronized between Qlik Cloud and Qlik Talend Cloud). Environments are associated to spaces (particularly, [data spaces](#glossary-0 "Glossary term")).  For more information about environments, see [*Synchronizing and managing environments*](../../Admin/mc-administer-environments.htm). - space:connection — Used for connections with a space as the top-level storage container or in the same environment as the loading application. This could be connections located in [shared](#glossary-1 "Glossary term"), [managed](#glossary-2 "Glossary term"), or data spaces.  For example, for a dataset stored locally within Qlik Cloud (DataFiles connection), located in a space named Sales Analysis, you would use following: Sales Analysis:DataFiles - connection — Connection name only. This refers to connections located in your [personal space](#glossary-3 "Glossary term"). In this case, the connection would simply be: DataFiles   Examples:  [CustomerOrders:DataFiles]  [SalesData2026:SnowflakeSales] |

## Learn more

- [*IncludeModel*](IncludeModel.htm)
- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
