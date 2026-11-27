---
title: "Permissions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-permissions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse"]
---

# Permissions

To create and manage entities for your Qlik Open Lakehouse, ensure you have the necessary permissions.

## Network integrations

The following permissions are required to create and manage network integrations:

| Action | Required Qlik Cloud role |
| --- | --- |
| Create a network integration. | Tenant Admin, or Data Admin. |
| Read network integration settings and monitoring. | Tenant Admin, Data Admin, Owner, Can Edit, Can View, Can Manage, Can Operate, or Can Consume. |
| List network integrations. | Tenant Admin, Data Admin, Owner, Can Edit, Can View, Can Manage, Can Operate, or Can Consume. |
| Update the properties of an existing network integration. | Tenant Admin, or Data Admin. |
| Delete a network integration. | Tenant Admin, or Data Admin. |
| Change the owner of a network integration. | Tenant Admin, or Data Admin. |
| Change the space of a network integration. | Tenant Admin, or Data Admin. |

## Lakehouse clusters

The following permissions are required to create and manage lakehouse clusters:

| Action | Required Qlik Cloud role |
| --- | --- |
| Create lakehouse clusters. | Tenant Admin, or Data Admin. |
| Read lakehouse clusters settings and monitoring. | Tenant Admin, Data Admin, Owner, Can Edit, Can View, Can Manage, Can Operate, or Can Consume. |
| List lakehouse clusters. | Tenant Admin, Data Admin, Owner, Can Edit, Can View, Can Manage, Can Operate, or Can Consume. |
| Update the properties of an existing cluster. | Tenant Admin, Data Admin, Owner, Can Edit, or Can Manage. |
| Operate an existing cluster (stop, start, roll, scale). | Tenant Admin, Data Admin, Owner, Can Manage, or Can Operate. |
| Delete a lakehouse cluster. | Tenant Admin, or Data Admin. |
| Change the owner of a lakehouse cluster. | Tenant Admin, or Data Admin. |
| Change the space of a lakehouse cluster. | Tenant Admin, or Data Admin. |

## Data catalog connections

To create and manage data catalog connections, the following permissions are required:

| Action | Required Qlik Cloud role |
| --- | --- |
| Create a data catalog connection. | Owner, or Can Manage. |
| Read data catalog connection settings and monitoring. | Owner, Can Edit, Can View, Can Manage, Can Consume, or Can View Data. |
| List data catalog connection. | Tenant Admin, Data Admin, Owner, Can Edit, Can View, Can Manage, Can Operate, Can Consume, or Can View Data. |
| Update the properties of an existing data catalog connection. | Owner, or Can Manage. |
| Delete a data catalog connection. | Tenant Admin, Data Admin, Owner, or Can manage. |
| Read data. | Owner, Can Edit, Can View, Can Manage, or Can View Data. |
| Change the owner of a data catalog connection. | Tenant Admin, or Data Admin. |
| Change the space of a data catalog connection. | Tenant Admin, or Data Admin. |
