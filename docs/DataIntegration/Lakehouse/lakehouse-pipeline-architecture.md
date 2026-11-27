---
title: "Qlik Open Lakehouse architecture"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-pipeline-architecture.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse"]
---

# Qlik Open Lakehouse architecture

Qlik Open Lakehouse provides a fully managed, end-to-end solution in Qlik Talend Cloud to ingest, process, and optimize data in an Iceberg-based lakehouse. This solution delivers low–latency query performance and efficient data operations at scale.

The Qlik Open Lakehouse architecture combines secure communication, scalable compute, and efficient data processing to deliver a modern lakehouse experience. In AWS environments, Qlik Open Lakehouse uses AWS-native components, including EC2 and S3. In GCP environments, it uses Google Cloud components, including Compute Engine and Cloud Storage.

## Core components

The following entities are required to create a Qlik Open Lakehouse.

### Data Movement Gateway (CDC)

The Data Movement Gateway runs in your on-premises or cloud environment. It captures changes from source systems, such as RDBMS, SAP, or mainframes, and sends the data to a cloud storage landing zone: Amazon S3 in AWS or Cloud Storage in GCP. For AWS streaming sources, the Streaming landing task does not require the Data Movement Gateway.

### Network integration gateway

The network integration gateway facilitates secure communication between Qlik services in the cloud and lakehouse clusters within your environment. In AWS, the gateway runs on an EC2 instance and is automatically deployed as an On-Demand Instance during the network integration process. In GCP, the gateway runs on a Compute Engine instance. The gateway is fully managed by Qlik. New versions are deployed automatically on release.

When the network integration functions correctly, a status of Connected is displayed in the Lakehouse clusters view in the Administration Activity Center. The status changes to Disconnected if connectivity issues arise.

### Lakehouse cluster

The lakehouse cluster is a group of cloud compute instances responsible for data processing. In AWS, the instances run in an EC2 Auto-Scaling Group. In GCP, they run in a managed instance group. The cluster instances coordinate and execute workloads to process incoming data from the landing area and, after processing, store the data in the target location in Iceberg format.

During network integration setup, Qlik automatically creates an initial lakehouse cluster. In AWS, the cluster starts with a single Spot Instance. In GCP, the cluster uses Compute Engine resources in the configured network. You can manage and create additional clusters to support your ongoing lakehouse requirements. When you configure a cluster, you grant Qlik permission to create, start, stop, scale, or roll back the servers to fulfill data processing requirements. Each cluster is associated with a single network integration, though multiple clusters can run within the same network integration. A single cluster can run many lakehouse tasks.

In AWS, a Spot Instance uses spare Amazon EC2 capacity at a lower cost than an On-Demand Instance but can be interrupted by AWS with little notice. Qlik uses On-Demand Instances to maintain capacity when Spot Instances are unavailable. In GCP, Spot virtual machines can be preempted with 30 seconds of notice. The GCP cluster uses separate Managed Instance Groups for Standard and Spot virtual machines, so the Standard group provides a minimum capacity floor. Using Spot capacity can reduce the compute costs of your Qlik Open Lakehouse.

For both AWS and GCP, you can configure a scaling strategy that best suits the workload and budget for your project. The following scaling strategies can be applied to a cluster:

- Low cost: Ideal for development or QA environments, and workloads that do not depend on fresh, real-time data. Qlik strives to keep the cost as low as possible, resulting in occasional periods of high latency.
- Low latency: Designed for non-mission critical workloads where near real-time data freshness is acceptable. While this strategy aims for low latency, brief spikes may be experienced.
- Consistent low latency: Suitable for production environments with high-scale data that must have real-time data freshness. Qlik proactively scales the instances to ensure low latency, which can incur higher costs.
- No scaling: A good option for workloads that process a consistent volume of data. Select this choice to retain a static number of instances with no automatic scaling and predictable costs.

### Cloud storage buckets

Each project uses two cloud storage buckets: an internal bucket and a target bucket. In AWS, these are Amazon S3 buckets. In GCP, they are Cloud Storage buckets.

- Internal bucket: Stores landing data, metadata, pipeline configuration, and intermediate data.
- Target bucket: Stores the Iceberg table data. The catalog connection determines the target bucket.

## High-level flow

### Initial setup

1. VPC and infrastructure provisioning - Configure a VPC in your AWS account or a VPC network in your GCP project, along with subnets, cloud storage buckets, and the required access configuration by following the instructions within the Qlik documentation.
2. Network integration configuration - The tenant admin creates a network integration in Qlik Talend Cloud using previously provisioned infrastructure details.
3. Deployment of Qlik components - Qlik automatically provisions the network integration gateway and an initial lakehouse cluster within your VPC or VPC network.
4. Establish communication - The network integration gateway securely establishes communication with Qlik Talend Cloud.
5. CDC gateway deployment - If you use a CDC source, deploy a separate Data Movement Gateway either on-premises or in your cloud environment.
6. Ready to operate - You can create and manage Qlik Open Lakehouse projects and tasks according to their access permissions when set-up is complete.

### Creating a Qlik Open Lakehouse project

The following task types are available. GCP supports CDC ingestion and mirroring to BigQuery. Streaming workflows remain documented for existing AWS projects.

#### Landing data task

1. Source configuration - The Data Movement Gateway is configured to capture changes from source systems, including RDBMS, SAP, mainframes, and more.
2. Data landing - The CDC task continuously sends raw change data to the designated Amazon S3 landing bucket in AWS or Cloud Storage landing bucket in GCP.

#### Storage data task

1. Register an Iceberg catalog connection, for example, AWS Glue Data Catalog in AWS or Google Lakehouse runtime catalog in GCP.
2. Define a storage task in Qlik Talend Cloud.
3. Qlik Talend Cloud sends task definitions to the network integration gateway.
4. The network integration gateway securely forwards the task instructions to the Qlik lakehouse cluster.
5. The cluster continuously reads raw data from a landing bucket in Amazon S3 or Cloud Storage, processes it, and writes the output to Iceberg tables in the corresponding cloud storage.
6. The lakehouse cluster scales up or down based on load when an automatic scaling strategy is selected. A no-scaling strategy keeps a static number of instances.
7. Monitoring data is sent to Qlik Talend Cloud, and logs and metrics are forwarded to Qlik.

#### Mirror data task

You can create external Iceberg tables to query data stored in your data lake from your cloud data warehouse without duplication. This allows you to use your data warehouse analytics engine on Iceberg-managed data stored in formats such as Parquet in Amazon S3 or Cloud Storage. For GCP projects, mirror the tables to BigQuery. By referencing external tables rather than duplicating data to your data warehouse, you reduce storage costs, maintain a single source of truth, and ensure consistency between lakehouse and warehouse environments.

## Communication between your network integration and Qlik Talend Cloud

The network integration establishes an outbound secured HTTPS connection to Qlik Talend Cloud. After acceptance, the connection is converted to a secured WebSocket (WSS). A dedicated WSS channel receives lakehouse task commands and controls. The network integration also periodically uses HTTPS to receive and send data-related events. Metrics and logs are sent to Qlik from the lakehouse clusters.

The following measures are taken to ensure your data is secure:

- All connections from your network integration to Qlik Talend Cloud are outbound. No inbound access is required.
- Metadata, commands, and control requests are transmitted using communication channels secured with HTTPS, creating an additional layer of encryption between the network integration and Qlik Talend Cloud.
- Customer content data flows between resources that you own and is not sent to Qlik Talend Cloud. Limited metadata, such as table and column names, is sent to Qlik Talend Cloud to support task definitions. Logs and metrics sent to Qlik are anonymized.
- Data is anonymized before sending to Qlik. Qlik uses anonymized data to proactively support you should the logs or metrics indicate an issue.

## Dataset architecture

The architecture of a dataset in a Qlik Open Lakehouse pipeline project is determined by the data source. For more information, see the following:

- [CDC sources (databases and SaaS applications)](lakehouse-datasets-architecture.htm)
- [Streaming sources](lakehouse-datasets-architecture-streaming.htm)
