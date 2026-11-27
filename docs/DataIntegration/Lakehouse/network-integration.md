---
title: "Step 1: Create a network integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/network-integration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse"]
---

# Step 1: Create a network integration

As a tenant or data admin, you can create a network integration from the Lakehouse clusters section of the Administration activity center.

The first step in creating a Qlik Open Lakehouse project is to connect to your AWS VPC or GCP VPC network and configure access to allow Qlik to manage resources on your behalf. To run data integration tasks, Qlik needs to start, stop, scale, and roll your clusters.

Each tenant can have one or more network integrations, enabling flexibility in connecting to different environments or regions. A network integration is associated with a specific space and can have multiple, associated lakehouse clusters; however, each lakehouse cluster is deployed on a single network integration. An initial lakehouse cluster is created during network integration setup. In AWS, it starts with a single Spot Instance. In GCP, it uses Compute Engine resources. You can create additional clusters.

## Network integration

A network integration is a prerequisite for creating Qlik Open Lakehouse pipeline projects. When you create a network integration, you customize the network resources in your AWS or GCP environment. A lakehouse cluster is created as part of this process, which you can edit and manage after the integration completes. You can also create new lakehouse clusters.

Before you start, complete the prerequisites for your cloud provider: [*Prerequisites in AWS*](aws-configuration.htm) or [*Prerequisites in GCP*](gcp-configuration.htm).

### Network integration gateway

The network integration gateway facilitates secure communication between Qlik Cloud services in the cloud and the lakehouse clusters within your environment. It is created automatically as part of network integration setup and is fully managed by Qlik. In AWS, it runs on an EC2 instance. In GCP, it runs on a Compute Engine instance.

The network integration gateway is different from the Data Movement Gateway. The network integration gateway handles communication and control between Qlik Cloud and your lakehouse resources. The Data Movement Gateway captures changes from CDC sources and is deployed separately when you create a CDC pipeline.

If the communication gateway is functioning correctly, a status of Connected is displayed in the [*Managing network integrations*](manage-network-integrations.htm). If there are connectivity issues, the status changes to Disconnected.

## [*Prerequisites in AWS*](aws-configuration.htm)

Configure the entities in your cloud environment to create a network integration.

## [*Prerequisites in GCP*](gcp-configuration.htm)

Configure the Google Cloud resources required to create a network integration.

## [*Creating an AWS network integration*](manual-integration.htm)

Create a network integration to allow Qlik Cloud to provision and manage resources in your AWS cloud environment. The network integration gateway and initial lakehouse cluster are created during this process.

## [*Creating a GCP network integration*](gcp-manual-integration.htm)

Create a network integration to allow Qlik Cloud to provision and manage resources in your Google Cloud environment. The network integration gateway and initial lakehouse cluster are created during this process.
