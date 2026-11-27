---
title: "Generating a SQL transformation from a text prompt"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Generating-SQL-from-text-prompt.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding SQL transformations"]
---

# Generating a SQL transformation from a text prompt

You can use SQL assistant to generate a SQL transformation from a text prompt where you describe the transformation that you want to achieve. You can for example select columns, join tables, or filter records.

The query is generated using generative AI based on your text prompt and dataset information, and using the syntax of your target data platform.

Information noteQlik does not control the generated output. Due to the nature of GenAI, responses may not produce SQL that meets your requirement without review or editing. The generated query is considered “Content” under the terms of Qlik Customer Agreement.

SQL assistant must be enabled on tenant level by a tenant admin in the Administration activity center.

Information note

To use the AI SQL assistant, you must opt in to cross-region inference. This allows Qlik Cloud to send inference requests outside your tenant region.

For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).

Text prompt and dataset information are sent to a third party generative AI (GenAI) model to generate SQL code. The information is treated as customer data and will not be used to train Qlik Cloud or the GenAI model on AWS Bedrock.

For more information about availability and information that is shared, see [*Generative AI-based assistant in Data Integration*](../../Admin/mc-manage-DI-features.htm#Generati).

Qlik Cloud Government note

SQL assistant is not available in Qlik Cloud Government.

## Generating a SQL query with SQL assistant

SQL assistant is available in SQL transformations in Transform data tasks. You must have added at least one dataset to the SQL transformation.

For more information about SQL transformations, see [*Adding SQL transformations*](Adding-SQL-based-tables.htm).

1. Click SQL Assistant.

   SQL Assistant is opened with a text prompt.
2. Type your description of the transformation that you want to achieve in Prompt.

   Example: List all customers over 5 million in sales. Include total sales and total opportunities for each customer.

   Tip noteWhen you reference columns in the prompt, make sure that they exist in the selected datasets.
3. Click Generate.
4. Review the generated SQL query that is displayed in SQL.

   You can rate the results by clicking ![Like](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_like.svg "Like") or ![Dislike](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dislike.svg "Dislike"). This will help Qlik improve the experience of SQL assistant.

   If the generated transformation does not seem accurate, or if you want to change something, click Edit prompt, make your changes to the prompt and generate a new query.
5. When you are happy with the resulting SQL query, click Apply to copy to the SQL transformation.
6. Click Extract parameters.
7. Clilck Describe table.
8. Check the resulting dataset in Results. You can also click View data to view a data sample of the results.
9. If you are happy witht he results, click OK to save and apply the SQL transformation.

## Information that is shared

The following information is shared with the Generative AI model to generate a query.

- Text prompt
- Additional generation instructions to adapt the query to your target data platform.
  Example: Generate a SQL query in a Snowflake-compatible syntax
- Dataset names and descriptions.
- Column names, data types and sizes.
- Primary key columns(unique identifiers).
- Relationships between datasets

  Example: "order\_detail" is attached to "order" using the "order\_id" key.

## Usage limitations

The following usage limitations apply for SQL assistant.

- Single call: 18k tokens.

  If this is exceeded, remove datasets that are not needed, or provide a less complex description in the prompt.
- Daily (per tenant): 1M tokens
- Monthly (per tenant): 10M tokens

When calculating usage, a token represents 6 characters. The call to the GenAI model consists of:

- General instructions to generate a SQL query. This part is of fixed size.
- The text prompt.
- A schema representation of the metadata in the datasets. This part can be very large if you have selected a large number of datasets.

## Limitations

- Incremental SQL generation is not supported. For more information, see [*Adding SQL transformations*](Adding-SQL-based-tables.htm#top).
- You can only transform data in current tables. Prior tables, change tables and live views are not supported. For more information about tables and views, see [*Dataset architecture in a cloud data warehouse*](../Storage/dataset-tables.htm).
- Platform independent functions are not used, for example, $CONCAT).

## Best practice

- Check that the data model in the source datasets include all required relationships when related columns have different names. In general, the GenAI model will relate columns with the same name without a defined relationship.

  Example: When ShipVia column in Orders should relate to shipper\_id column in Shippers, you should create a relationship in the data model before generating a SQL transformation.
- Select only the source datasets required for the transformation. Obsolete source data may cause incorrect or irrelevant results, and increase usage of tokens.
- You can add descriptions in the prompt to identify columns or datasets with a name that is not obvious.

  Example: cus\_ct contains the Customers dataset.
