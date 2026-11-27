---
title: "IncludeModel"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/IncludeModel.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# IncludeModel

Expand/Collapse all

# IncludeModel

The IncludeModel statement loads a data product and its semantic model, including tables, relationships, measures, and dimensions. Measures and dimensions from the semantic model automatically appear as master items in the application.

Syntax:

IncludeModel data\_product\_name [InEnvironment environment\_name] [FromSpace data\_product\_space | FromCurrentSpace | FromPersonalSpace] [WithTables Table table\_name1  Fields fieldlist Connection dataset\_connection {, Table table\_nameN Fields fieldlist Connection dataset\_connection,... }] [WithMeasures measurelist] [WithDimensions dimensionlist]

Arguments and keywords

| Argument or keyword | Description |
| --- | --- |
| data\_product\_name | The name of the data product to load. |
| [*FromSpace*](FromSpace.htm), [*FromCurrentSpace*](FromCurrentSpace.htm), or [*FromPersonalSpace*](FromPersonalSpace.htm) | Keywords specifying the space from which to load the data product.  Use one of the following as needed. If all of these keyword options are omitted, the IncludeModel statement looks for the data product in your personal space.   - FromSpace: Load the data product located in the space specified with data\_product\_space. - FromCurrentSpace: Load the data product located in the current space. - FromPersonalSpace: Load the data product located in your personal space. |
| data\_product\_space | Specifies the space of the data product you want to load, if you are using FromSpace to explicitly specify a particular space from which to load. This is not applicable if you are using FromPersonalSpace or FromCurrentSpace.  Follow the quoting conventions documented at [*Using quotation marks in the script*](../use-quotes-in-script.htm). Examples:  MyAnalyticsSpace  "My Analytics Space"  [My Analytics Space] |
| [*InEnvironment*](InEnvironment.htm) | Keyword specifying to use the data product in the environment specified with environment\_name.  Not required if the data product is not located in an environment. |
| environment\_name | The name of the environment, if applicable, containing the data product you want to load.  Follow the quoting conventions documented at [*Using quotation marks in the script*](../use-quotes-in-script.htm). Examples:  Production  [Production Environment]  "Production Environment" |
| [*WithTables*](WithTables.htm) | Keyword specifying to use the tables defined in subsequent Table statements. |
| [Table](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Table.htm) | Keyword specifying the use of a table. Loads one table per Table statement. |
| table\_name | Specifies the name of the table to use in the data model.  Follow the quoting conventions documented at [*Using quotation marks in the script*](../use-quotes-in-script.htm). Examples:  MyDataTable  [My Data Table]  "My Data Table" |
| [Fields](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Field.htm) | Keyword instructing to use the specified fields (fieldlist) from the table to integrate into the data model. |
| fieldlist | List of fields from the table referenced in the preceding Table statement.  You can use \* to use all fields from the table, or provide a comma-separated list of specific fields.  Examples:  Amount, Quantity, Region  [Amount], [Quantity], [Region] |
| [*Connection*](Connection.htm) | Keyword specifying to use the dataset specified in dataset\_connection. |
| dataset\_connection | A connection that can load the dataset containing the referenced table.  Depending on the location of the connection, use one of the following formats:   - environment:space:connection — Used for files located within environments (containers for data synchronized between Qlik Cloud and Qlik Talend Cloud). Environments are associated to spaces (particularly, [data spaces](#glossary-0 "Glossary term")).  For more information about environments, see [*Synchronizing and managing environments*](../../Admin/mc-administer-environments.htm). - space:connection — Used for connections with a space as the top-level storage container or in the same environment as the loading application. This could be connections located in [shared](#glossary-1 "Glossary term"), [managed](#glossary-2 "Glossary term"), or data spaces.  For example, for a dataset stored locally within Qlik Cloud (DataFiles connection), located in a space named Sales Analysis, you would use following: Sales Analysis:DataFiles - connection — Connection name only. This refers to connections located in your [personal space](#glossary-3 "Glossary term"). In this case, the connection would simply be: DataFiles   Examples:  [CustomerOrders:DataFiles]  [SalesData2026:SnowflakeSales] |
| [*WithMeasures*](WithMeasures.htm) | Keyword instructing to convert the specified measures from the data product (measurelist) into master measures. |
| measurelist | List of measures from data product's semantic model to be converted into master measures.  You can use \* to convert all measures, or provide a comma-separated list of specific measures.  Example:  [Sales], [Total Quantity], [Cost] |
| [*WithDimensions*](WithDimensions.htm) | Keyword instructing to convert the specified dimensions from the data product (dimensionlist) into master dimensions. |
| dimensionlist | List of dimensions from data product's semantic model to be converted into master dimensions.  You can use \* to convert all dimensions, or provide a comma-separated list of specific dimensions.  Example:  [Product Name], [Region], [Customer] |

## Remarks

The IncludeModel statement is typically generated automatically by the data catalog when you choose to load a data product with its semantic model. You can also write the statement manually or edit the generated statement to customize which fields, measures, and dimensions are included.

Relationships defined in the semantic model are automatically applied to the loaded tables, creating associations in your data model.

Operations for measures and dimensions are applied at the end of the data load after the tables and fields are loaded. If the load fails before that phase, no measure or dimension operations are applied.

Information noteYou must have Can consume data or Can view permission in the space containing the data product to use the IncludeModel statement.

### Master item properties

Most attributes of master items inherited from semantic models are read-only in the consuming application. Some other master item attributes, such as those related to visualizations, can still be edited within the application.

The read-only behavior applies to the user interface only—you can set a number of master item properties via API:

- Properties that are configurable in the semantic model but read-only in the consuming application's user interface. This includes title, description, and tags.
- Properties that are not configured in the semantic model and not exposed in the consuming application's user interface.

Changes to properties defined by the semantic model will be overwritten when the application reloads.

### Master item deletion

In an unpublished application, you can delete an inherited master item, but it reappears on the next reload if it is still referenced in the IncludeModel script. To permanently remove it, remove it from the script first. You can also duplicate an inherited master item. The duplicate is an ordinary application master item and is fully editable.

## Example 1 – Load specific tables, along with all measures and dimensions

Load script

This example loads specific tables, and their relationships, from the data product and its semantic model. It also uses wildcards (\*) to load all fields from the specific tables, and that all measures and dimensions in the semantic model are to be defined as master items in the application.

```
IncludeModel [Sales Performance Data] FromSpace [Sales Analysis Space]
WithTables
    Table [Transactions] Fields * Connection [Sales Analysis Space:DataFiles],
    Table [Products] Fields * Connection [Sales Analysis Space:DataFiles]
WithMeasures *
WithDimensions *;
```

The components of this IncludeModel statement are:

- Data product name: Sales Performance Data
- Data product space: Sales Analysis Space
- Tables: Transactions and Products
- Fields: all
- Measures and dimensions: all

The two tables are loaded with their relationships. All measures and dimensions in the semantic model will appear as master items in the application.

## Example 2 – Load specific tables, measures, and dimensions

Load script

This example loads specific tables, and their relationships, from the data product and its semantic model. It uses wildcards (\*) to load all fields from the specific tables. Specific measures and dimensions are defined as master items, rather than automatically defining all measures and dimensions as master items.

```
IncludeModel [Customer Analytics] FromSpace [sales]
WithTables
    Table [Customers] Fields * Connection [sales:DataFiles],
    Table [Orders] Fields * Connection [sales:DataFiles]
WithMeasures [Total Revenue], [Customer Count]
WithDimensions [Customer Name];
```

The components of this IncludeModel statement are:

- Data product name: Customer Analytics
- Data product space: sales
- Tables: Customers and Orders
- Fields: all
- Measures: Total Revenue and Customer Count
- Dimensions: Customer Name

The two tables are loaded with their relationships. Each of the specific measures and dimensions from the semantic model will appear as master items in the application.

## Example 3 – Load specific tables, along with all measures and dimensions (dataset located in environment)

Load script

This example loads specific tables, and their semantic model relationships, from a data product located in a data space contained within an environment (see [*Synchronizing and managing environments*](../../Admin/mc-administer-environments.htm)). It also uses wildcards (\*) to load all fields from the specific tables, and that all measures and dimensions in the semantic model are to be defined as master items in the application.

```
IncludeModel [Sales Performance Data]
    InEnvironment 'Production'
    FromSpace [Sales Analysis Space]
WithTables
    Table [Transactions] Fields * Connection [Sales Analysis Space:DataFiles],
    Table [Products] Fields * Connection [Sales Analysis Space:DataFiles]
WithMeasures *
WithDimensions *;
```

The components of this IncludeModel statement are:

- Data product name: Sales Performance Data
- Data product environment: Production
- Data product space: Sales Analysis Space
- Tables: Transactions and Products
- Fields: all
- Measures and dimensions: all

The two tables are loaded with their relationships. All measures and dimensions in the semantic model will appear as master items in the application.

## IncludeModel script limitations

The WithTables: \* wildcard syntax is not supported. You must list tables explicitly.

## Learn more

- [*Semantic models in data products*](../../DataIntegration/DataProducts/semantic-models-in-data-products.htm)
- [*Consuming data products in applications*](../../DataIntegration/DataProducts/consuming-data-products-apps.htm)
- [*Data catalog*](../../LoadData/data-catalog.htm)
