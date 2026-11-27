---
title: "Managing lakehouse clusters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/manage-clusters.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Managing network integrations and lakehouse clusters"]
---

# Managing lakehouse clusters

As a tenant or data admin, you can create and manage lakehouse clusters from the Lakehouse clusters section of the Administration or Data Integration activity centers. Users without an admin account can view and manage clusters from the Data Integration activity center according to granted permissions.

## Monitoring a cluster

A lakehouse cluster is created during the network integration deployment using basic configuration. In the Administration activity center, click Lakehouse clusters, and select the Lakehouse clusters tab. The existing clusters within your tenant are displayed as follows:

| Column | Description |
| --- | --- |
| Name | The name of the compute cluster. |
| Cluster ID | The unique ID for the cluster allocated by Qlik. |
| Network integration | The VPC integration the cluster is running on. |
| Space | The associated space. |
| Status | The status of the cluster. |
| Capabilities | The cluster workload capability. |
| Message | The error message if the cluster encounters issues during deployment or operation. |
| Version | The Qlik Open Lakehouse version deployed on the cluster. |
| Created | The user who created the cluster, and the date and time when the cluster was created. |

### Cluster status

Each cluster can be in one of the following states:

| Status | Description |
| --- | --- |
| Deploying | The cluster is being created within your VPC. |
| Deployment failed | The cluster creation failed due to an unrecoverable error that requires user intervention. |
| Stopping | The cluster is shutting down. |
| Stopped | The cluster has successfully stopped. |
| Deleting | The cluster is being deleted. |
| Disconnected | The cluster is disconnected from QCS. |
| Running (under provisioned) | The cluster encountered issues while attempting to scale. |
| Running (pending resources) | No instances are available for the cluster, for example, because the quota limit has been reached. |
| Running | The cluster is active. |

### Cluster capabilities

The cluster capabilities can be as follows:

| Capabilities | Description |
| --- | --- |
| Streaming workloads | In AWS, required for streaming ingestion or streaming transformation workloads. Tasks running on this cluster are charged based on compute usage. |
| CDC workloads | Use this capability when tracking CDC changes from database or SaaS applications. Billing is based on data volume ingested. Tasks running on this cluster are free of charge. |
| Mixed workloads | In AWS, supports streaming and CDC capabilities on the same cluster. Note that CDC sources are charged based on data volume. Additionally, compute usage is charged for any task running on the cluster. |

Information noteRemoving a cluster capability is only allowed if there are no tasks using that capability.

## Managing a cluster

To manage an existing cluster, do the following:

1. In the Lakehouse clusters list, select the cluster you want to manage, and click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_5x16.png) More actions.
2. In the cluster properties pane, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_5x16.png) More actions.
3. Select one of the following actions, which are visible depending on the current state of the cluster:

- Start: A cluster with a status of Stopping or Stopped can be started. All entities configured to run on the cluster will be resumed when the cluster is running.
- Stop: You can pause a cluster with a status of Deploying, Disconnected, Running, Running (under provisioned), or Pending resources. All entities configured to run on the cluster will be stopped.
- View: The cluster details pane provides an overview of the cluster settings, including status, number of instances, family type, and scaling strategy.
- Edit: Cluster properties can be edited regardless of status.
- Roll: Rolling a cluster gradually replaces the cluster instances with new instances, and can be performed when the cluster status is Disconnected, Running, or Running (under provisioned). This action applies cluster configuration changes with immediate effect. Choose between:
  - Gradual: Ensures there is no downtime as the instances continue to run while updates are applied.
  - Immediate: All instances shut down immediately, causing a delay until they are updated and restarted.

  Information noteIn GCP-based projects, the Gradual option keeps downtime to a minimum but doesn’t eliminate it. Downtime is typically a couple of minutes. No data is lost, and data that arrives during the downtime is processed right after the roll completes.
- Scale now: Change the scaling strategy for a cluster in a Running state. This is available when Spot Instances have been configured. Click Scale now to change the number of instances.
- Delete: A cluster can be deleted if no entities are currently associated with it. Otherwise, tasks must first be deleted or moved to another cluster. The cluster state must be Deployment failed, or Stopped before it can be deleted.
- Redeploy: Visible if cluster creation failed due to an unrecoverable error that requires user intervention, resulting in a status of Deployment failed. This action enables you to manually deploy the cluster.

Information noteFor more information on lakehouse cluster architecture and selecting an appropriate scaling strategy for your workload, see [*Lakehouse cluster*](lakehouse-pipeline-architecture.htm#lakehouse-cluster)

## Editing a cluster

To edit the properties for an existing cluster, do the following:

1. In the Lakehouse clusters list, select the cluster you want to manage.
2. In the cluster properties pane, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_5x16.png) More actions, and select Edit.
3. The following cluster properties can be changed:

   - Name: You can change the name of the cluster.
   - Family type: The instance family type can be scaled up or down. Any changes require the cluster to be rolled.
4. Edit the instances in the cluster for your cloud provider:

   - In AWS:

     - AWS On-Demand Instances: You can change the minimum number of guaranteed On-Demand Instances for the cluster.
     - AWS Spot Instances: Update the Minimum and Maximum number of Spot Instances.
   - In GCP, configure Standard and Spot Compute Engine virtual machines.
5. If required, change the scaling strategy for the ephemeral instances handling your workload. The following options are available:

   - Low cost: Optimizes for low cost, though may lead to occasional periods of high latency.
   - Low latency: Strives to maintain low latency, while allowing brief, necessary spikes.
   - Consistent low latency: Proactively scales up to ensure latency remains low.
   - Manual scaling: Retains a static number of instances with no automatic scaling.
6. Tags

   Add, edit, or delete associated Tags. Any changes require the cluster to be rolled.
