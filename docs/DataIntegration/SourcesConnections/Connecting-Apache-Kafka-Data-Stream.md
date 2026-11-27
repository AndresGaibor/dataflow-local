---
title: "Apache Kafka Data Stream"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Apache-Kafka-Data-Stream.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to data streams"]
---

# Apache Kafka Data Stream

Connect to your Apache Kafka cluster to use as a streaming data source in your Qlik Open Lakehouse projects. Kafka connections can only be used with the Streaming landing task and Streaming transform task.

Qlik Open Lakehouse enables organizations to build real-time, analytics-ready pipelines on an open and scalable architecture. By integrating Apache Kafka as a streaming source, Qlik supports continuous ingestion of high-volume event data into Apache Iceberg tables. This combination delivers low-latency data availability and robust schema evolution, allowing teams to operationalize real-time insights and accelerate downstream transformations.

Streaming landing tasks and Streaming transform tasks enable Kafka topics to be central components of your Qlik Open Lakehouse projects. As data streams into Iceberg, it is quickly accessible for analytics, AI, and machine learning workloads, supporting time-sensitive decision-making and scalable data engineering practices. The result is a unified, query-optimized data layer that strengthens the reliability and performance of your streaming architectures. To analyze data from Kafka using your cloud data warehouse query engine, land and store the data in a Qlik Open Lakehouse and mirror the data to your warehouse using a [Mirror data task](../Lakehouse/mirroring-data.htm).

## Prerequisites

The following requirements apply when creating and using a Kafka streaming source:

- A network integration that has network connectivity to the broker servers.
- Ensure that the Kafka cluster is accessible from the network used by the lakehouse cluster that runs the landing task.
- A Kafka streaming source connection requires a Qlik Open Lakehouse target platform.

## Setting Kafka connection properties

To configure your Kafka connection, do the following:

1. In Connections, click Create connection.
2. Select the Space where you want to create the connection or choose Create new data space.
3. Select Kafka from the Connector name list or use the Search box. Ensure the Type is Source and the Category is Streaming.
4. Configure the following properties:

### Data source

Set your data source connection properties as follows:

- Select your Network integration from the list.
- In  Broker servers, enter a single host using the format hostname:port, for example, host1:9092.

  To enter a list of hosts, use the format: hostname:port, hostname:port, for example, host1:9092,host2:9092.

### Authentication details

- Select your Authentication method from the list:

  - PLAIN: This configuration is not secure, as the client has unrestricted access to your Kafka cluster, and data is transmitted without encryption. Use this option only when connecting to brokers that do not require SASL or Kerberos-based authentication.
  - SASL/SCRAM-SHA-256: Use this option to authenticate with a username and password using the SCRAM-SHA-256 challenge–response mechanism. This method provides stronger credential protection than SASL/PLAIN and requires the corresponding SCRAM credentials to be configured in Kafka.
  - SASL/SCRAM-SHA-512: This option authenticates with a username and password using the SCRAM-SHA-512 mechanism. This is the most secure SCRAM variant and requires matching SCRAM-SHA-512 credentials to be configured in the Kafka cluster.

Information noteTo use an alternative authentication method that is not listed, please contact Qlik support.

### TLS

Optionally, you can add a Certificate Authority (CA).

- To add a CA, select Use custom trust CA.
- In CA path, enter the path of the CA file to upload to Qlik Cloud. The CA file is available to the clusters running the tasks.

### Additional Kafka properties

Additional Kafka properties are optional.

Add a Key and Value for any tags you want to include that help you identify, organize, and manage resources.

### Schema registry connection

The schema registry server is optional.

To connect to a schema registry, click Set up a schema registry server and configure the settings:

- Schema Registry URI: Enter the URI in the format, http://schema-registry1.example.com:8081;http://schema-registry2.example.com:8081.
- Username: Enter the username for the server connection.
- Password: Enter the password for the server connection.

#### Schema registry connection TLS

If you choose to configure a schema registry server, you have the option to add a Certificate Authority (CA).

- To add a CA, select Use custom trust CA.
- In CA path, enter the path of the CA file to upload to Qlik Cloud. The CA file is available to the clusters running the tasks.

### Create the connection

When you have configured your security method, complete the following steps to create your connection:

- In Name, enter the display name for the connection, for example, My Kafka Streaming Source connection.
- Click Test connection to validate the credentials.
- Click Create.

## Mapping topics to datasets

The following use cases are supported when ingesting from a Kafka source:

| Topic | Target dataset | Use case | Mapping |
| --- | --- | --- | --- |
| One | One | Each topic is loaded to a target dataset. | Supported in the datasets mapping of the Streaming landing task. |
| One | Many | Duplicate a topic to multiple datasets. | Supported by using Add to target multiple times. |
| One | Many | Split an event to multiple targets. For example, an event contains orders and order lines that are split into multiple datasets. | Supported in the Streaming Transform task. Duplicate a dataset and select different fields in each dataset; or use the Fork processor and Select columns processor within the transformation flow. |
| One | Many | Split a topic into multiple datasets based on specific column values. | Supported in the Streaming Transform task. Configure a Filter processor for each column value used to split the topic into different datasets. To handle unmatched records, configure an additional Filter processor that outputs non-matching data to a separate dataset. |
| Many | One | Ingest all topics that meet a specific criteria to the same target dataset, or specific topics to the same dataset. | Supported in the datasets mapping of the Streaming landing task. If multiple topics are loaded into a single dataset and one of the topic loading tasks fails, then the dataset errors and the loading of other topics discontinues. |
