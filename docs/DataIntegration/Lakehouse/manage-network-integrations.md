---
title: "Managing network integrations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/manage-network-integrations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Managing network integrations and lakehouse clusters"]
---

# Managing network integrations

Network integrations are required to create and run Qlik Open Lakehouse projects and managed from the Administration activity center.

## Monitoring a network integration

To monitor your network integrations, in the Administration activity center, select Lakehouse clusters to open the Network integrations tab. The following information is available for each network integration created within the current tenant:

| Column | Description |
| --- | --- |
| Name | The network integration name. |
| Provider account | The cloud provider account or project, for example, an AWS account or Google Cloud project. |
| Provider network | The VPC ID. |
| Region | The VPC region. |
| Space | The associated space. |
| Status | The status of the network integration. |
| Message | The error message when the status is Deployment failed or Disconnected. |
| Owner | The user that created the network integration. |
| Created | The date and time when the network integration was created. |

## Network integration status

A network integration is in one of the following statuses, indicating the current condition of the gateway:

| Status | Description |
| --- | --- |
| Deploying | Pending an on-demand gateway. |
| Deployment failed | Failed to create the gateway. |
| Connecting | During the deployment process, the status is Connecting when the gateway is up but has not yet connected to Qlik Cloud. |
| Disconnected | The gateway has not connected to Qlik Cloud. If the connection issue resolves, the gateway reconnects automatically. |
| Connected | The gateway is running and connected to Qlik Cloud. |

## Viewing network integration settings

To view the settings for an integration, do the following:

1. In the network integrations list, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_5x16.png) More actions on the network integration you want to view.
2. Select ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view_19x15.png) View to open the network integration properties pane.

## Viewing network integration logs

To open the log viewer, do the following:

1. In the network integrations list, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_5x16.png)More actions on the network integration you want to view.
2. Select ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_file_15x15.png) View logs to open the Log viewer window.
3. Use the select lists to change which service logs you want to view, e.g. Data Movement Gateway logs, Source connections logs. Services may not have logs available.
4. The active log is shown by default. Use the log list to display a previous log.
5. To export a log file, click Download. The log viewer exports the content to a text file.

## Deleting a network integration

A network integration can only be deleted if no clusters are associated with it, and can be deleted regardless of the state of the gateway. When you delete a network integration, only the gateway is deleted from your cloud environment. You must manually delete all other entities.

To delete a network integration, do the following:

1. Delete the clusters that are associated with the network integration.
2. In the network integrations list, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical_5x16.png) More actions on the network integration you want to delete, and select ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_12x16.png) Delete.
3. In the confirmation dialog, click Delete network integration.
4. Manually delete the remaining entities created during the network integration set-up.
