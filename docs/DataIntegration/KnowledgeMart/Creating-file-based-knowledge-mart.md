---
title: "Creating a file-based knowledge mart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/KnowledgeMart/Creating-file-based-knowledge-mart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Creating knowledge marts"]
---

# Creating a file-based knowledge mart

File-based knowledge marts let you embed and store your unstructured data in a vector database. This allows the augmented context to be retrieved with semantic search features to be used as a context for Retrieval Augmented Generation (RAG) applications.

The supported input formats are: `PDF`, `TXT`, and Word `DOCX`.

## Requirements

- You need a Qlik Talend Cloud Enterprise subscription.
- Supported on Snowflake and Databricks platforms. Snowflake Iceberg is not supported.
- A customer managed data gateway is required.

  Databricks requires Qlik Data Gateway - Data Movement version 2024.11.95 or higher.

## Installing the Qlik Data Gateway - Data Movement

Before creating file-based knowledge marts, you must install a specific Qlik Data Gateway - Data Movement. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Supported connections

For information on the supported:

- Vector databases, see [*Connecting to vector databases*](../Landing/connecting-vector-databases.htm).
- LLM connections, see [*Connecting to LLM connections*](../Landing/connecting-llm-connections.htm).
- File storage, see [*Connecting to file storage*](../Landing/connecting-file-storage.htm).
- Cloud storage (Amazon S3, Google Cloud Storage, Azure Data Lake Storage), see [*Connecting to cloud storage*](../TargetConnections/cloud-storage-connections.htm).

## Creating the files

1. Click Pipeline projects in the left menu and open a project.
2. From the Pipeline project page, you can create a file-based knowledge mart. Either:
   - Click Create new > File-based knowledge mart.
   - Click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) of the data task > File-based knowledge mart.

   The configuration window opens.
3. Enter a name.
4. Enter a description. This is optional.
5. Create or select a Source connection.
6. Select where to store the documents from the Store vectors in drop-down list. To store the documents with the project, select Data project platform.
7. If you selected External vector database, create or select a Vector database connection. The documents and vectors will be stored in this vector database.
8. Create or select an LLM connection. This connection is required for using the semantic search.
9. Click Create.
10. When the knowledge mart is created, add documents.

## Adding files

Information noteOnly text is written to documents. Text from diagrams or images is not extracted.

1. In the Folders tab of the Data task page, select a folder or click Select folders to select a new one.
2. Browse to the folder, select the check box of the folder.

   All the files in the folders will be read if they are in one of the supported formats, no matter when they are added to the folder.

   When you delete a file that already exists in the index from a folder, the data is still in the index. To remove the data from the index, use the same file but empty.

   To display the list of files in the folder, right-click it.
3. Click Save to close the Select folders window.
4. To edit the chunk size, the chunk overlap, click Settings > Runtime.
5. To edit the index name, click Settings > Vector database settings.

   For more information, see [*Index name*](#Index).
6. Click ![Actions icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_horizontal.png) on the right > Prepare.
7. When the preparation is completed, click Run. The documents are being embedded and transferred.

   The transfer is completed when the Run button is active.
8. When it is the first full load, verify the status of each file:
   1. Select Monitor in the menu.
   2. Select Full load status on the bottom of the page.

      ![Full load status in the Monitor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/knowledgemart-full-load-status.png)
   3. When some files failed and before you re-run everything, fix the errors or delete the files. If you keep the files in error, the next runs will fail.

   Information noteReloading all files could result in extra costs.

When your files are correct, you can ask questions about your data. For more information, see [*Using the test assistant*](Test-Assistant.htm).

## Full load and Change data capture (CDC)

Full load and CDC are supported.

Full load: A document is generated for each document instance and will be sent to the target.

CDC: A document is regenerated after any change.

When a file is changed or added, documents are read from this file. The file will be split into documents of chunks according to the chunk size and overlap.

When it is the first full load, verify the status of each file:

1. Select Monitor in the menu.
2. Select Full load status on the bottom of the page.

   ![Full load status in the Monitor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/knowledgemart-full-load-status.png)
3. When some files failed and before you re-run everything, fix the errors or delete the files. If you keep the files in error, the next runs will fail.

Information noteReloading all files could result in extra costs.

## Updating the input data

When you update the input data, you must run the data task to transfer the changes to the vector database or data platform.

As old chunks are deleted and new chunks are inserted, the field `hdr__operation` corresponds to an insert operation, not to an update operation. For more information, see [Dataset architecture in a cloud data warehouse](../Storage/dataset-tables.htm).

## Index name

Each knowledge mart has an index name that is used for the semantic search.

When you configure tasks to write into the same index, you must configure the same LLM parameters for the tasks.

If you want your documents to be in the same index, they must have the same index name.

To edit the index name:

1. In the Data task page, click Settings.
2. Select the Vector database settings tab.
3. Edit the Index name.
4. Click OK.

After you edited the index name, you must prepare the task. Otherwise, your changes will not apply in the next runs.

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

## Changing connections or data gateway

If you change the source connection, the vector connection, or the vector data gateway, you must prepare the task again.
