---
title: "Introducing Data Integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-services-introduction.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Getting started with Qlik Talend Data Integration"]
---

# Introducing Data Integration

You can deliver data ready for consumption to Qlik Cloud or to cloud data warehouses, such as Snowflake, Google Cloud BigQuery, and Azure Synapse Analytics with Qlik Talend Data Integration. Data sources can be on-premises or in the cloud. The data can be kept up-to-date without manual intervention using CDC (Change Data Capture) or batch technologies, such as scheduled reloads. You can create a data pipeline and perform fit-for-purpose transformations and create data marts.

You can access Qlik Talend Data Integration home by selecting Data Integration from the launcher menu (![Launcher menu icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)).

Information noteUsers with Embedded Analytics User role cannot access Qlik Talend Data Integration.

For more information about the architecture of Qlik Talend Data Integration, see [*Dataset architecture in a cloud data warehouse*](../Storage/dataset-tables.htm).

## Subscription options

Qlik Talend Cloud subscriptions are based on a [capacity model](../../Admin/subscription-options-qlik-cloud.htm) with the volume of [Data Moved](../../Admin/subscription-value-meters.htm#Data2) as the primary value meter.

Qlik Talend Cloud is available in subscription options from four tiers: Starter, Standard, Premium, and Enterprise. The higher editions provide more advanced data sources and transformations. This includes capabilities hosted on Qlik Cloud and Talend Cloud. All subscriptions include [*Qlik Cloud Analytics Standard*](../../Admin/subscription-options-analytics.htm#_bm2).

For more information about subscription options, see [*Qlik Talend Cloud subscription options*](../../Admin/subscription-options-QTC.htm).

## Data spaces

Data spaces are governed areas of your Qlik Cloud tenant that are used to create and store projects. Inside the space, you can also create new connections using connectors, and manage access to Data Movement gateways. All data assets will be created in the space of the project that they belong to.

For more information, see [*Working in spaces in Data Integration*](../DataSpaces/working-spaces.htm).

## Projects

A project is where you create your data integration flow, using data tasks. The project is associated with a data platform that is used as target for all output. You can create a project with either of the following use cases:

- Data pipeline

  Create a simple linear pipeline, or a complex pipeline consuming several data sources and generating many outputs.

  [*Creating and managing data pipeline projects*](Data-projects.htm)
- Qlik Open Lakehouse

  Create a simple linear pipeline, or a complex pipeline consuming several data sources that stores data in Apache Iceberg.

  [*Creating a Qlik Open Lakehouse project*](../Lakehouse/creating-project.htm)
- Replication

  Replicate data from supported data sources to any supported target, or land data to a data lake.

  [*Creating a replication project*](../Replicating/data-replication-task.htm)

Information noteIt is not possible to move projects between spaces.

## Data task

A data task is the main unit of work in a project. You can create data tasks of the following types in a project. You create a new data task by clicking on Create in the top bar, and then clicking the appropriate task.

### Data tasks in data pipeline projects

Tip note In addition, you can also perform landing and storage with a single task, Onboarding data. This will create a Landing task, and a Storage task.

#### Data tasks in data warehouse projects

- Landing

  Copy data from a data source to a landing area. Data sources can be on-premises or in the cloud. The landing area can be a cloud target, or an Amazon S3 data bucket (only when creating QVD datasets).

  You can keep data up-to-date without manual intervention by using CDC, or by performing full loads that are scheduled to reload periodically.

  [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm)
- Lake landing

  Land data to a lakehouse, where the data is landed to cloud file storage managed by Snowflake. You can sync Iceberg tables with Snowflake Open Catalog to enable interoperability with other tools, such as Apache Spark.

  [*Landing data to a lakehouse*](../Landing/Lake-landing.htm).
- Registered data

  Register data that already exists on the data platform. This lets you use data that is onboarded with other tools than Qlik Talend Data Integration, for example, Qlik Replicate.

  [*Registering data that is already on the data platform*](../Onboarding/Registering-data.htm)
- Storage

  Create ready to consume datasets in a cloud data warehouse, or in Qlik Cloud, from the data copied by the landing data task. The datasets can be kept up-to-date with the landing data without manual intervention.

  [*Storing datasets*](../Storage/generating-datasets.htm)
- Transform

  Create reusable data transformations based on rules and custom SQL as a part of your data pipeline. You can perform row-level transformations and create datasets that are either materialized as tables, or created as views that perform transformations on the fly.

  [*Transforming data*](../Transformation/Transformations.htm)
- Data mart

  Create data marts to leverage your Storage data tasks or Transform data tasks. You can create any number of data marts depending on your business needs. Ideally, your data marts should contain repositories of summarized data collected for analysis on a specific section or unit within an organization.

  [*Creating and managing data marts*](../DataMarts/DataMarts.htm)
- Knowledge marts

  Creating knowledge marts lets you embed and store your structured data in a vector database. This allows the augmented context to be retrieved with semantic search features to be used as a context for Retrieval Augmented Generation (RAG) applications.

  [*Creating knowledge marts*](../KnowledgeMart/Creating-knowledge-marts.htm)

#### Data tasks in Qlik Open Lakehouse projects

- Lake landing

  Land data to a data lake.

  [*Landing data to Qlik Open Lakehouse*](../Lakehouse/landing-data.htm)
- Storage

  Store data in Iceberg format to enable efficient storage and high-performance querying. Automatic compaction and file clean-up help optimize storage and lower costs.

  [*Storing datasets*](../Lakehouse/storing-data.htm)
- Mirror

  Mirror tables to your cloud data warehouse without duplication of data. Users can query data directly from your data warehouse query engine. Add a Mirror data task to your pipeline, or use a Qlik Open Lakehouse project as your source to perform data transformations.

  [*Mirroring data to a cloud data warehouse*](../Lakehouse/mirroring-data.htm)

### Data tasks in replication projects

- Replication

  Replicate data from supported data sources to any supported target.

  [*Creating a replication project*](../Replicating/data-replication-task.htm)
- Lake landing

  Land data to a data lake.

  [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](../Replicating/landing-datalakes.htm)

## Monitoring your data tasks

You can monitor the status and progress of your data tasks with monitor views. A monitor view lets you view the status of all data tasks in the tenant, or a subset of data tasks based on a filter. You can create several views to monitor different aspects of your data pipelines. For more information, see [*Monitoring and operating your data tasks*](Monitoring-your-data-tasks.htm).

## Data products

Datasets that have been registered from a data project or a manual upload and added to your Catalog, can then be grouped and packaged in the form of a data product. You can group datasets by business domain for example, and make them available on the data marketplace for analytics consumers to use in applications. A data product can optionally include a semantic model that defines relationships, measures, and dimensions for the datasets. Semantic models enable Analytics developers to reuse pre-built data structures and business metrics, ensuring consistency across applications. For more information, see [*Working with data products*](../DataProducts/Data-products.htm) and [*Semantic models in data products*](../DataProducts/semantic-models-in-data-products.htm).

## Data stewardship

With Data stewardship you can curate and validate data. You can use your existing semantic types to make sure that data is consistently formed. You create a sprint which is the main body of work for the required stewardship tasks. The sprint contains information about the data and the data schema, and defines the user roles. During the sprint, all resolved records are stored in your own cloud data warehouse, and not in Qlik Talend Cloud.

[*Validating and correcting your data with data stewardship*](../DataStewardship/Governing-data-stewardship.htm)

## Connections

Connections are used to let data tasks access data sources, external storage and target platforms for data delivery and push-down transformations.

### Managing your connections

Click Connections on the left to view all your connections.

- You can edit connections that you own.

  Information noteYou can also edit all connections in a data space where you are the owner, or have a Can manage role.

  Click ... and then Edit.
- You can test a connection.

  Click ... and then Test connection.
- You can delete a connection.

  Click ... and then Delete.

### Creating a connection

The are several ways of creating connections:

- Click Create new in data task setup wizards where you select a connection.
- Click Create new and select Connection in Connections view.

You can filter connectors by:

- Category

  Data warehouse, Cloud storage, Database and Application.
- Type

  Source or Target.

You can also select from recently used connectors.

You will need to select which type of data source, and then enter address and authentication information.

See also:

- [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm).
- [*Setting up spaces and connections*](Settingup-spaces-connections.htm)
