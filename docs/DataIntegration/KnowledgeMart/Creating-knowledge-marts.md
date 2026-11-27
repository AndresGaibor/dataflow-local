---
title: "Creating knowledge marts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/KnowledgeMart/Creating-knowledge-marts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Creating knowledge marts

Creating knowledge marts lets you embed and store your structured and unstructured data in a vector database. This allows the augmented context to be retrieved with semantic search features to be used as a context for Retrieval Augmented Generation (RAG) applications.

RAG optimizes the LLM output by providing additional context to the LLM with the query.

## Requirements

- You need a Qlik Talend Cloud Enterprise subscription.
- Supported on Snowflake and Databricks platforms. Snowflake Iceberg is not supported.
- A customer managed data gateway is required.

  Databricks requires Qlik Data Gateway - Data Movement version 2024.11.95 or higher.

## Installing the Qlik Data Gateway - Data Movement

To use knowledge marts, you need to connect to vector databases and LLM connections which requires to install a specific Qlik Data Gateway - Data Movement. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Viewing and downloading the logs

You can view and download the logs for the knowledge marts. For more information, see [*Troubleshooting Data Movement gateway*](../../Gateways/dm-gateway-troubleshooting.htm).

## Prerequisites

You can use data tasks of the following types as source for a knowledge mart:

- Storage
- Transform

Before you can create a knowledge mart, you need to do the following in the source data tasks:

- Populate the datasets with data that you want to use in your knowledge mart. For more information, see [*Onboarding data to a data warehouse*](../Onboarding/Onboarding-data.htm).
- Create a dataset relational model to define the relationships between the source datasets. For more information, see [*Creating a data model*](../Transformation/Create-data-model.htm).

  Warning noteAll source datasets must have keys.

### Configuring Databricks for knowledge marts

If you use Databricks as data platform, you must perform some configuration in Databricks to be able to create knowledge marts.

- Create a SQL warehouse in Databricks. It is recommended to use Serverless Compute.

  You must also configure Data Security for SQL Warehouses and Serverless Compute to enable storage integration.
- Create an endpoint in Vector Search. You refer to the name of this endpoint in Vector database settings in the knowledge mart task.

  Choose the Type based on your performance requirements, Standard is suitable for most use cases.

  If needed, define a Serverless Usage Policy to associate tags for cost attribution.
- Configure Databricks models in Serving.

  Under Serving Endpoints, you can use the LLM Embeddings and Chat Models available in Databricks. Make sure to verify the models you plan to use in your data pipeline.

  You can also create a Serving Endpoint for a custom model, or use a Foundation Model, for example, OpenAI or Azure OpenAI.

  Examples:

  Embedding Model: databricks-gte-large-en

  Chat/Completion Model: databricks-meta-llama-3-1-405b-instruct

## Limitations

There are limitations when you use source datasets matching all these conditions:

- Created by SQL transformation or a transformation flow
- Non-materialized
- Historical Data Store (Type 2) turned off

These datasets are considered updated on every run which may affect efficiency and cost. You can mitigate this by:

- Changing the source datasets to be materialized.
- Using explicit dataset transformations.
- Creating global rules that transform multiple datasets.

Knowledge mart tasks can be exported and imported only between projects that use the same data platform type. Exporting a project with knowledge mart tasks from Snowflake and importing it into Databricks, or exporting from Databricks and importing into Snowflake, is not supported.

### Supported encoding format

Your files must be properly encoded in UTF-8. Other formats may be wrongly interpreted.

Information noteQlik adds 2 transformation rules that remove all binary content from the output: QLIK\_\_REMOVE\_BLOB\_COLUMNS and QLIK\_\_REMOVE\_BYTES\_COLUMNS.

### Supported characters

The file and folder names can contain the following characters:

- [0-9], [a-Z], [A-Z]
- ! - \_ . \* ' ()

Other special characters might be supported but, because of significant special character handling, it is recommended to only use the characters from the list above.

### Relationships

- It is not possible to relate data from two datasets. Create a transform task where you define the relationship in the data model, and use the transform task as source for the task.
- When two datasets are related in the data model, both datasets will be available in the task, even if you only selected one of the datasets.

## Deleting a task

You can delete the data task if it is not running, and there are no dependencies to downstream tasks in the same project.

- In Pipeline project view of the project, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Delete.

Artifacts (tables and views) created by the task will also be deleted, unless you select to keep them.

Information noteKeep in mind that the artifacts you keep will no longer be updated by the task.

If the task is set to Drop and create the index, the index is dropped only if you selected to delete artifacts. If you select to keep artifacts the index is preserved.

## Changing connections or data gateway

If you change the vector connection or the vector data gateway, you must prepare the task again.

## Troubleshooting

### Files moved to OneDrive are not recognized by File knowledge mart

Possible cause

If files are moved or synced to OneDrive using options that preserve the old file created and modified date, the file is not recognized as a new file.

Proposed action

Change the file modified date to the current date.

### Runtime error when using Pinecone

Possible cause

NULL values in metadata columns are not supported by Pinecone. Result would be a runtime error.

Proposed action

- Transform the NULL values to other values, for example an empty string, or the word NULL, in a transformation before the knowledge mart.
- Use another vector database.
- Do not use the column as metadata.
