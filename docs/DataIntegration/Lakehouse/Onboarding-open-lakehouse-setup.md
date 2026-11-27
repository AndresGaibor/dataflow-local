---
title: "Setting up Qlik Open Lakehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/Onboarding-open-lakehouse-setup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse"]
---

# Setting up Qlik Open Lakehouse

This section guides you through the steps required to set up a Qlik Open Lakehouse project.

To ensure you configure your Qlik Open Lakehouse correctly, complete the actions in the following order:

1. Create a network integration.
2. Use the initial lakehouse cluster created with the network integration, or create an additional lakehouse cluster.
3. Connect to your data catalog.

For CDC sources, deploy a separate Data Movement Gateway after the network integration is connected. The network integration gateway is created automatically during network integration setup.

## [*Step 1: Create a network integration*](network-integration.htm)

Connect to your AWS VPC or GCP VPC network and configure permissions that allow Qlik to manage resources on your behalf. The resources process data ingestion tasks.

## [*Step 2: Create a lakehouse cluster*](lakehouse-cluster.htm)

Create clusters using a scaling strategy that balances latency and cost requirements to support pipeline workloads.

## [*Set up connections to data catalogs*](../TargetConnections/data-catalog-connections.htm)

Create a connection to an Iceberg data catalog, such as AWS Glue Data Catalog in AWS or Google Lakehouse runtime catalog in GCP, to use as the target for your project.
