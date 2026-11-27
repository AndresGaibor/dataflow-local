---
title: "Connecting to data streams"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Data-Streams.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources"]
---

# Connecting to data streams

The following streaming sources are supported in Qlik Open Lakehouse projects. Event data is continuously ingested for near real-time availability in downstream data integration, analytics, and AI workloads.

Apache Kafka and Amazon Kinesis provide durable, high-throughput pipelines for capturing events as they occur. Google Cloud Storage and Amazon S3 can also serve as streaming file sources. Kafka and Kinesis preserve message order within a partition or shard, but not across an entire topic or stream. Use a consistent partition key to keep changes for a record in the correct order.

#### Streaming ingestion versus batch ingestion

The difference between streaming and batch data sources is as follows:

- With both sources, events are efficiently ingested every minute, supporting low-latency processing and near-real-time analytics.
- With non-streaming sources, there is first a full load of the existing data and then changes are ingested. You can also reload the full load data from the source.
- With streaming sources, there is no clear distinction between initial load and events later. Qlik can manage retention and also supports partitions.

Information noteStreaming tasks are billed based on compute usage (vCores x runtime) rather than data volume.

In a Qlik Open Lakehouse project, streaming sources can only be used with the Streaming landing task and Streaming transform task:

- Streaming data is ingested using a Streaming landing task. The task reads events as they arrive, lands them in cloud storage, and persists them as Avro files. In AWS, the landing area is Amazon S3. In GCP, it is Google Cloud Storage. This approach supports schema evolution and complex data types such as structs.
- When you onboard data from a streaming source, a Streaming transform task is automatically added for each dataset that will be stored in Iceberg format. Optionally, the Streaming transform task can be used to standardize structures, enrich event payloads, or align data with downstream consumption models.
- A Mirror data task enables datasets from streaming sources to be mirrored to cloud data warehouses allowing downstream systems to consume streaming events without duplicating data. For more information, see [*Mirroring data to a cloud data warehouse*](../Lakehouse/mirroring-data.htm).

## Limitations

The following limitations apply to all data sources:

- If your files are of different types, which can occur when they originate from multiple sources or versions, the transform task created using a single sample file (for example, during onboarding) does not automatically account for those differences.
- If you change the data types in the landing task, for example because you need to hash the data, ensure the transform data types match the new data types.

## Supported sources

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-kinesis-square_48x48.png)

### [Amazon Kinesis](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-AWS-Kinesis-Data-Stream.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/amazon-s3-square_48x48.png)

### [Amazon S3](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-AWS-S3-Data-Stream.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/kafka-square.png)

### [Apache Kafka](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Apache-Kafka-Data-Stream.htm)

![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Data-connector-icons/googlecloudstorage-square.png)

### [Google Cloud Storage](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Connecting-Google-Cloud-Storage-Data-Stream.htm)
