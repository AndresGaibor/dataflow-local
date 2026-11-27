---
title: "Creating a knowledge mart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/KnowledgeMart/Creating-a-knowledge-mart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Creating knowledge marts"]
---

# Creating a knowledge mart

Knowledge marts let you embed and store your structured data in a vector database. This allows the augmented context to be retrieved with semantic search features to be used as a context for Retrieval Augmented Generation (RAG) applications.

The output is in the `JSON` format.

Information noteYou need a Qlik Talend Cloud Enterprise subscription.

## Requirements

- You need a Qlik Talend Cloud Enterprise subscription.
- Supported on Snowflake and Databricks platforms. Snowflake Iceberg is not supported.
- A customer managed data gateway is required.

  Databricks requires Qlik Data Gateway - Data Movement version 2024.11.95 or higher.

## Installing the Qlik Data Gateway - Data Movement

Before creating a knowledge mart, you must install a specific Qlik Data Gateway - Data Movement. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Supported connections

For information on the supported:

- Vector databases, see [*Connecting to vector databases*](../Landing/connecting-vector-databases.htm).
- LLM connections, see [*Connecting to LLM connections*](../Landing/connecting-llm-connections.htm).
- File storage, see [*Connecting to file storage*](../Landing/connecting-file-storage.htm).

## Creating the data

1. Click Pipeline projects in the left menu and open a project.
2. From the Pipeline project page, you can generate and publish documents to a vector database. Either:
   - Click Create new > Knowledge mart.
   - Click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) of the data task > Knowledge mart.

   The configuration window opens.
3. Enter a name.
4. Enter a description. This is optional.
5. Select where to store the documents from the Store vectors in drop-down list. To store the documents with the project, select Data project platform.
6. If you selected External vector database, create or select a Vector database connection. The documents and vectors will be stored in this vector database.
7. Create or select an LLM connection. This connection is required for using the semantic search.
8. Click Create.
9. When the data is created, add documents.

## Adding documents

Information noteOnly the text format is supported. For example, text from diagrams or images cannot be extracted.

1. In the Datasets tab of the Data task page, click Add in the left panel.
2. Select the base dataset from which the document will be generated. A document will be created for each record. For example, for a list of patients, a document will be created for each patient.
3. The Document schema name field is pre-filled with the name of the selected base dataset. Rename it if needed.
4. Enter a description. This is optional.
5. Select the data you want to include to enrich the document.
6. Click OK. You are back to the Document schemas tab.
7. Select the Datasets tab.
8. In the left panel, select the dataset you chose as the base dataset earlier.
9. To remove the data you do not want to include in the documents, select the checkbox and click Remove.
10. Select Metadata for all fields that you want to define as metadata. You can filter according to metadata before sending the data to the LLM.

    Information noteOn Databricks, the metadata is implemented by a single field containing a JSON representation of the key and values of selected metadata fields.
11. To improve the semantic search performed by the LLM, rename data whose names are not clear enough.

    Example: Rename dt to date.
12. When you removed and renamed data as needed, click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) on the right > Prepare. The documents are being generated in `JSON` format.
13. When the documents are generated:
    1. Select the Datasets tab.
    2. To verify your documents before running the task, click View data to display a data sample.
    3. Click Run. The documents are being transferred to the vector database or the data platform depending on the configuration.

The transfer is completed when the Run button is active.

To make sure everything has been transferred, you can ask questions about your data. For more information, see [*Using the test assistant*](Test-Assistant.htm).

## Full load and Change Data Capture (CDC)

Full load and CDC are supported.

Full load: A document is generated for each document instance and will be sent to the target.

CDC: A document is regenerated after any change in the base or related entity.

A new document is created when an entry is added to the base entity. If no entries in the related entities can be connected to a base entity, they will not appear in the documents.

## Updating the input data

When you update the input data, you must run the data task to transfer the changes to the vector database or data platform.

## Index name

Each knowledge mart has an index name that is used for the semantic search.

When you configure tasks to write into the same index, you must configure the same LLM parameters for the tasks.

If you want your documents to be in the same index, they must have the same index name.

To edit the index name:

1. In the Data task page, click Settings.
2. Select the Vector database settings tab.
3. Edit the Index name.
4. Click OK.

## Viewing task information

Click ![Information](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) on the menu bar to view task information, such as:

- Owner
- Space
- Data platform
- Project ID
- Data task runtime ID

## Settings

You can view and edit the settings of a knowledge mart.

From the Data task page, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) > Settings.

Information noteAs the settings depend on the storage (Databricks, Snowflake, etc.), the following tables describe the settings that are always available. More settings can be available.

This table describes the settings of the Connections tab.

| Settings | Description |
| --- | --- |
| Source connection | The source connection. |
| Store vectors in | From the drop-down list, select:   - External vector database - Data project platform |
| Vector database connection This setting is available when External vector database is selected for Store vectors in. | The vector database connection.  For more information, see [*Connecting to vector databases*](../Landing/connecting-vector-databases.htm). |
| LLM connection | The LLM connection. For more information, see [*Connecting to LLM connections*](../Landing/connecting-llm-connections.htm).  When you want to use Databricks as an LLM connection, configure the Embedding model serving endpoint and Completion model serving endpoint when creating the knowledge mart. For more information, see the [Databricks documentation](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-foundation-model-endpoints#create-an-external-model-serving-endpoint). |

This table describes the settings of the Platform settings tab.

| Settings | Description |
| --- | --- |
| Data task schema | The name of the data task schema. |
| Internal schema | The name of the internal schema. |
| Prefix for all tables and views | The prefix for resolving conflicts between multiple data tasks. |

This table describes the settings of the Vector database settings tab.

| Settings | Description |
| --- | --- |
| Index schema This setting is not available when External vector database is selected for Store vectors in. | The name of the index schema. |
| Index name | The name of the index. |
| If the index already exists | When multiple tasks are writing to the same index, select whether the index must be deleted or not:  - Use the existing index: The index is not deleted. - Drop and create the index: The index is deleted. |
| Databricks vector search endpoint | The name of the vector search endpoint created in Databricks. For more information, see [*Configuring Databricks for knowledge marts*](Creating-knowledge-marts.htm#Configur) .  Information noteOnly applicable to projects using Databricks as data platform. |

This table describes the settings of the Runtime tab.

| Settings | Description |
| --- | --- |
| Parallel execution | The maximum number of database connection.  Enter a value from 1 to 50. |
| Bulk size | For knowledge marts, the bulk size is the number of documents loaded in each bulk request. For file-based knowledge marts, the bulk size is the number of files loaded in each bulk request.  On Snowflake and Databricks, the bulk size is not required as everything is loaded in one query. |
| Maximum number of records to load | 0 means that all records are loaded. |

This table describes the settings of the Views tab for Snowflake

| Settings | Description |
| --- | --- |
| Standard views | Use standard views to display the results of a query as if it were a table. |
| Snowflake secure views | Use Snowflake secure views for views designated for data privacy or sensitive information protection, such as views created to limit access to sensitive data that should not be exposed to all users of the underlying tables. Snowflake secure views can execute more slowly than Standard views. |

This table describes the settings of the Test assistant tab.

| Settings | Description |
| --- | --- |
| Number of documents in context | The number of relevant documents that will be passed to the model as context. |
| Prompt template | Enter the template the AI must follow to filter the documents to be included. |
| Filter | Enter the expression to filter the documents to be included. As the filter is based on the metadata and the file-based knowledge marts do not have metadata, think carefully of the filter you are configuring. It might be more relevant to exclude data instead of including them.  For more information, see [*Using the test assistant*](Test-Assistant.htm). |
| Document retrieval | Select the option from the drop-down list:  - Show retrieved context: The test assistant provides the documents from which it generates the answer. - Don't show retrieved context: The test assistant generates an answer but does not provide the documents. |
| Answers generation | Select the option from the drop-down list:  - Generate answers: The test assistant generates an answer based on the documents. - Don't generate answers: The test assistant answers with documents only. |
