---
title: "Connecting to vector databases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/connecting-vector-databases.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections for knowledge marts"]
---

# Connecting to vector databases

You can connect to vector databases when you create knowledge marts in Qlik Talend Data Integration. For more information, see [*Creating knowledge marts*](../KnowledgeMart/Creating-knowledge-marts.htm).

Information noteYou need a Qlik Talend Cloud Enterprise subscription.

To connect to vector databases, set up Data Movement gateway. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Supported vector databases

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/elasticsearch-square.png)

### [Elasticsearch](../VectorDBs/connecting-elasticsearch.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/opensearch-square.png)

### [OpenSearch](../VectorDBs/Connecting-OpenSearch.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/pinecone-vector-square.png)

### [Pinecone Vector Search](../VectorDBs/connecting-pinecone.htm)

If your project is stored in Snowflake or Databricks, these connections can be used as vector databases. For more information on these connections, see [Snowflake](../TargetConnections/snowflake-target.htm) and [Databricks](../TargetConnections/databricks-target.htm).

For more information about the configuration, see the settings in [Creating a knowledge mart](../KnowledgeMart/Creating-a-knowledge-mart.htm) and [Creating a file-based knowledge mart](../KnowledgeMart/Creating-file-based-knowledge-mart.htm).
