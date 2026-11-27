---
title: "Designing your pipeline project"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Designing-data-pipeline.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data"]
---

# Designing your pipeline project

Qlik Talend Data Integration provides the ability to create data pipelines to perform a variety of data integration tasks in support of your data architecture and analytics requirements.

You create your data integration flow in a pipeline project, using data tasks. The project is associated with a data platform that is used as target for all output. The project is stored in a data space. You must also create connections to your sources and targets.

## Create a space

![data pipeline project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_space_data.png)

## [*Working in spaces in Data Integration*](../DataSpaces/working-spaces.htm)

Create a data space that is used to create and store your project. Inside the space, you can also create new connections using connectors, and manage access to Data Movement gateways.

## Create connections to your sources and targets

![data pipeline project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.png)

## [*Setting up connections to data sources*](../Landing/connecting-data-2.htm)

Create connections to your data sources.

![data pipeline project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_target.png)

## [*Setting up connections to targets*](../TargetConnections/data-project-connections.htm)

Create connections to your target platform.

![data pipeline project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_data-gateway.png)

## [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm)

Set up Qlik Data Gateway - Data Movement to facilitate secure data movement from your enterprise data sources and SaaS applications to supported targets.

## Create a pipeline project

When you create a pipeline project, you must select your use case.

![data pipeline project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qdi_pipeline.svg)

### [*Creating and managing data pipeline projects*](Data-projects.htm)

Data pipeline projects support ingesting data from a large number of supported sources to a data platform where you can then transform data with ELT (pushdown) transformations to support data lakehouse and data warehouse architectures. Pipelines support log-based CDC and incremental data sources but provide a series of options for data ingestion to major data warehouse platforms.

Use a data pipeline project when you want to:

- Support type 1 and type 2 data structures with your ingestion processes.
- Transform and re-shape your data to of fit-for-purpose output or star-schemas for analytic workloads.
- Create a lakehouse based on Iceberg.
- Create a Qlik Open Lakehouse based on Apache Iceberg and mirror tables to your cloud data warehouse.
- Create complex pipelines that are managed across projects for organizational or functional boundaries.

![replication project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qdi_replicate.svg)

### [*Creating a replication project*](../Replicating/data-replication-task.htm)

Replication projects support direct replication from a large number of supported sources to data lakes or any supported target platforms. Data is applied directly to your target structures but complex transformations or reshaping of data is not supported. Replication pipelines support a larger set of target technologies for replication scenarios.

Use a replication project when you want to:

- Replicate data to your target and do not need complex transformations on that data.
- Replicate data to a target not supported by data pipelines.

![replication project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikIcons/schedule.svg)

### [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm)

In some cases, you might need to schedule your task to propagate changes from the data source to the target platform.

For information about use cases that require scheduling as well as instructions for setting up scheduling intervals, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).

## Manage versions of your pipeline project

![data pipeline project](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikIcons/governance.png)

## [*Manage your pipeline projects with version control*](../VersionControl/Project-version-control.htm)

Use version control to manage development of a data project, and to keep track of changes.

## Define pipelines in code

![declarative pipeline management](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikIcons/governance.png)

## [*Declarative pipelines*](../DeclarativePipelines/Declarative-pipelines-overview.htm)

Export a pipeline as YAML configuration files, edit them in your IDE, and deploy them with the import API or version control. Manage environments and promote pipelines using Git branching.
