---
title: "Prerequisites in GCP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration"]
---

# Prerequisites in GCP

Configure the Google Cloud resources required to create a network integration for your Qlik Open Lakehouse pipeline projects.

To create a network integration, you must first configure the required resources in Google Cloud Platform. We recommend you follow the instructions below, saving the relevant project, network, bucket, and service account details for each resource to a file. When all resources are created, use the information to configure a network integration for your Qlik Open Lakehouse pipeline projects.

Follow the instructions for creating each resource below. Complete them in order, making a note of each setting. When you have finished, follow the instructions for creating a [*Creating a GCP network integration*](gcp-manual-integration.htm).

## [*VPC network and subnet*](gcp-vpc-network-subnet.htm)

Configure a VPC network and subnet to integrate Qlik with your Google Cloud environment, including Cloud NAT and Private Google Access so that the lakehouse cluster can start.

## [*Cloud Storage internal bucket*](gcp-cloud-storage-bucket.htm)

Create a Cloud Storage bucket to store metadata object definitions, configurations, and intermediate data.

## [*Firewall and network tags*](gcp-firewall-network-tags.htm)

Define firewall rules and a dedicated network tag to control inbound and outbound traffic to your Compute Engine instances.

## [*Management service account*](gcp-management-service-account.htm)

Create a management service account that grants Qlik the permissions it needs to manage Google Cloud resources and run tasks in your Qlik Open Lakehouse pipeline projects.

## [*Instances service account*](gcp-instances-service-account.htm)

Configure a service account for the Qlik-managed Compute Engine instances to securely access your Google Cloud resources without storing credentials on the instance.

## [*Image and VM requirements*](gcp-image-vm-requirements.htm)

Review the Compute Engine image and VM requirements for running Qlik Open Lakehouse in your Google Cloud environment.
