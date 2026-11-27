---
title: "Lakehouse clusters"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/lakehouse-clusters-admin.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing data governance and transfers"]
---

# Lakehouse clusters

To create and run Qlik Open Lakehouse projects, you must first set up a network integration. Once the integration is configured, a lakehouse cluster will be created automatically.

Setting up a network integration involves configuring settings and permissions in your cloud environment to allow Qlik to access resources and manage servers on your behalf (create, start, stop, scale, and roll). Once a network integration is configured and a connection established, a lakehouse cluster is created automatically. You can create multiple network integrations and clusters, and manage them in the Administration activity center.

## *[Creating a network integration](network-integration.htm)*

Connect to your AWS VPC or GCP VPC network and configure permissions to allow Qlik to manage resources on your behalf. The resources are used to run data ingestion tasks.

## *[Creating a lakehouse cluster](lakehouse-cluster.htm)*

Create clusters using a scaling strategy that balances latency and cost requirements to support the workloads of your pipelines.

## Learn more

- *[Onboarding data to Qlik Open Lakehouse](Onboarding-data-open-lakehouse.htm)*
