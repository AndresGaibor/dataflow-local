---
title: "Step 2: Create a lakehouse cluster"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-cluster.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse"]
---

# Step 2: Create a lakehouse cluster

A lakehouse cluster defines the compute environment to run Qlik Open Lakehouse storage tasks. Each cluster specifies settings that include the number of instances, machine type, and scaling strategy.

When you create a network integration for a Qlik Open Lakehouse pipeline project, a cluster with a single AWS Spot Instance is created automatically. In GCP, the initial cluster uses Compute Engine resources. However, you can create additional clusters in the Administration and Data Integration activity centers.

Lakehouse clusters link pipelines to a group of AWS EC2 instances or GCP Compute Engine instances, allowing you to optimize workloads by assigning critical jobs to high-performance clusters and non-critical workloads to cost-effective machines. In GCP, the instances run in a managed instance group.

While a cluster is associated with a single VPC, multiple clusters can run within the same VPC. Additionally, a single cluster can run multiple jobs. It is helpful to define the compute requirements of your workloads before creating a lakehouse cluster. Cluster settings, including the scaling strategy, can be modified as needed, although some changes may require the cluster to be rolled. For more information on editing cluster settings, see [*Managing lakehouse clusters*](manage-clusters.htm)

When you create a lakehouse cluster, you specify the number of Spot and On-Demand instances that Qlik provisions in AWS. In GCP, you can choose Standard or Spot virtual machines for the cluster. For more information on cluster compute, see [*Lakehouse cluster*](lakehouse-pipeline-architecture.htm#lakehouse-cluster)

Using custom images is optional in AWS. When using custom images in AWS, an x86 image is required, but using both arm and x86 images is recommended to maximize availability of Spot Instances. For more information, see [*AMI requirements*](ami-requirements.htm) .

## Cluster capabilities

When you create a cluster, you must choose the workload type that the cluster runs: streaming, CDC, or mixed. For GCP, select CDC workloads. Streaming and mixed workloads are not supported for GCP. In AWS, you can use separate clusters for streaming and CDC sources. This ensures accurate and minimal billing charges. However, there are use cases when a mixed workload is appropriate and can share a cluster:

- For testing or evaluating small-scale projects with insignificant billing volumes.
- If non-streaming usage is minimal and you do not want to configure and maintain a separate cluster.

## Prerequisites

To create a lakehouse cluster, you need:

- A network integration within the current tenant.
- Permission to access the network integration.

## Creating a lakehouse cluster

To add a cluster to the current tenant, do the following:

1. In the Administration activity center, click Lakehouse clusters. Select the Lakehouse clusters tab, click Create new, then Lakehouse cluster, and configure it:

   - Name: Enter the name of the cluster.
   - Network integration: Select the network integration where the cluster will be deployed.
2. Integration space: Select the space that the cluster will belong to, as this is not inherited from the network integration.
3. Select the cluster capabilities for the workload:

   - Streaming workloads: Select this option when ingesting from a streaming data source in AWS.
   - CDC workloads: Select this option when ingesting from database and SaaS application sources.
   - Mixed workloads: In AWS, select mixed workloads when testing, or when streaming usage is minimal and workloads consist mostly of CDC sources.
4. Configure the family type:

   - Type: Select the instance type.
   - Size: Select the instance size.
5. Configure the instances for your cloud provider:

   - In AWS, enter the number of AWS On-Demand Instances and the minimum and maximum number of AWS Spot Instances to use.
   - In GCP, configure Standard and Spot Compute Engine virtual machines. Standard VM instances default to 0 and provide automatic fallback when Spot capacity is unavailable. Spot VM instances default to a minimum and maximum of 1.
6. Choose an appropriate strategy for your workload from the following options:

   - Low cost – Optimizes for low cost, though may lead to occasional periods of high latency.
   - Low latency - Strives to maintain low latency, while allowing brief, necessary spikes.
   - Consistent low latency - Proactively scales up to ensure latency remains low.
   - Manual scaling - Retains a static number of instances with no automatic scaling.
7. Select how your cluster receives software updates:

   - Early rollout: Ideal for development and staging clusters to validate new releases against custom set-ups and code, prior to production.
   - Later rollout: Updates are applied after a successful early rollout, and recommended for production environments.
8. Add a Key and Value for any tags you want to include that help you identify, organize, and manage resources.
