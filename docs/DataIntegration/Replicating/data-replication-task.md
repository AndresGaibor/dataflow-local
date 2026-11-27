---
title: "Creating a replication project"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/data-replication-task.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project"]
---

# Creating a replication project

Create a data replication project to efficiently and securely move data between supported data sources and targets. Data can be transformed and kept continually up-to-date with CDC.

There are two types of replication use case:

- Replicating data
- Landing data in a data lake

  Information noteWith all subscription tiers except the Qlik Talend Cloud Starter subscription, the replication use cases are split into separate replication task types: A "Replicate data" task for replication to databases and data warehouses, and a "Land data in data lake" task, for replication to cloud storage. With a Qlik Talend Cloud Starter subscription, there is no separate "Land data in data lake" task for cloud storage. Instead, the "Replicate data" task supports replication to all supported targets (databases, data warehouses, and cloud storage).

The data replication process consists of the following operations:

- Retrieving the data from the data source
- Transforming the data (optional)
- Loading the data to the target
- Keeping the data up-to-date with scheduled or real-time change capture

## Set up connections to your data sources and targets

While it is possible to set up connections during task setup, best practice dictates that you define and verify your connections before you set up your replication task. This way, when you set up your task, all you need to do is simply select the connectors you configured earlier.

Information noteIf you change the source connection, the target connection, or the source data gateway after the task has already been prepared, you must [recreate all the datasets](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Managing-datasets.htm#:~:text=the%20storage%20task.-,Recreating%20datasets,-You%20can%20recreate).

## [*Setting up connections to data sources*](../Landing/connecting-data-2.htm)

Set up a connection to your data source.

## [*Setting up connections to targets*](../TargetConnections/data-project-connections.htm)

Set up a connection to your target platform.

## Set up replication tasks

## [*Replicating data with a Standard, Premium, or Enterprise subscription*](replicating-other-subscriptions.htm)

Create replication tasks from supported data sources to any supported target, with real-time CDC and support for private connections.

## [*Replicating data with a Qlik Talend Cloud Starter subscription*](replicating-starter-subscription.htm)

Create replication tasks from SaaS applications and supported database sources to any supported target (databases, data warehouses, and cloud storage), with scheduled CDC.

## [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](landing-datalakes.htm#Landing)

Replicate data from any supported source to supported cloud storage targets.
