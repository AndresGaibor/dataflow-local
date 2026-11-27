---
title: "Creating a GCP network integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/gcp-manual-integration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Setting up Qlik Open Lakehouse", "Step 1: Create a network integration"]
---

# Creating a GCP network integration

A GCP network integration allows Qlik to provision and manage resources in your Google Cloud environment. These resources process tasks in your Qlik Open Lakehouse pipeline projects.

## Prerequisites

Before you create a network integration, complete the instructions in [*Prerequisites in GCP*](gcp-configuration.htm). Have the following information available:

- Google Cloud project
- Region
- VPC network and subnet
- Cloud Storage internal bucket
- Management service account email
- Instances service account email
- Firewall and network tag details

## Creating a manual network integration

In the Administration activity center, go to Lakehouse clusters, open the Network integration tab, and click Create new. Complete the four-step wizard.

### Network details

1. Enter the Network integration name and select the Integration space.
2. Enter the GCP project ID and select the Region.
3. Enter the VPC network name or self-link and the Subnet name. The subnet must be in the selected region.

### Integration settings

For GCS bucket for internal Qlik files, enter the internal bucket name without the `gs://` prefix.

### Access control

- Management service account email: Enter the management service account email.
- Network tags: Optionally, add the tags that your firewall rules use.
- Instances service account email: Enter the instances service account email.
- SSH key: Optionally, enter a public SSH key for access to Qlik-managed instances.

### Create cluster

Configure the initial lakehouse cluster, then click Create. For cluster configuration details, see [*Step 2: Create a lakehouse cluster*](lakehouse-cluster.htm).

The initial lakehouse cluster uses Compute Engine resources in the configured Google Cloud network. You can manage the cluster and create additional clusters after the network integration is created.
