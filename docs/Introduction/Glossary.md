---
title: "Glossary"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/Glossary.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Introducing Qlik Cloud"]
---

# Glossary

Leave your feedback here

[![Close feedback widget](../_images/img/nav/close-white.svg)](javascript:void(0))

1. [Qlik Cloud](/en-US/cloud-services)
2. [Introducing Qlik Cloud](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/introducing-qlik-cloud.htm)

# Glossary

## Activity center

Activity centers are the central point of access for applications, spaces, and other content. There are four activity centers in Qlik Cloud: Insights, Analytics, Qlik Talend Data Integration, and Administration. Activity centers were formerly known as hubs.

Similar terms: Access point, Hub

See: [*Qlik Cloud interface overview*](../QlikCloudNavigation/Qlik-Cloud-Interface-Overview.htm)

## Administrator, analytics

Analytics administrators are administrators who only have permissions to manage the Analytics service's user resources.

See: [*Permissions for analytics administrators*](../Admin/SaaS-user-permissions.htm#Analytic)

## Administrator, audit

Audit administrators can access application feedback and usage metrics for Insight Advisor and Insight Advisor Chat.

See: [*Permissions for audit administrators*](../Admin/SaaS-user-permissions.htm#Audit)

## Administrator, data

Data administrators are administrators limited to managing data spaces and the data resources contained within those spaces.

See: [*Permissions for data administrators*](../Admin/SaaS-user-permissions.htm#Data)

## Administrator, tenant

Tenant administrator are administrators responsible for managing users, system extensions, and system customizations. Tenant administrators have full access to the Administration activity center.

See: [*Permissions for tenant administrators*](../Admin/SaaS-user-permissions.htm#Tenant)

## Aggregation

An aggregation is a calculation using multiple records in the source tables. Often it is a single field aggregated with a function such as sum, count, min, max, or average. For example, the sum of sales.

Similar terms: Calculation, Measure, Metric

See: [*Measures*](../Measures/measures.htm)

## Analyzer user entitlement

Analyzer entitlement is intended for users who only consume sheets and applications created by others. You need Professional entitlement to create, edit, or publish sheets or applications.

See: [*Managing user entitlements*](../Admin/SaaS-user-allocations.htm)

## Anonymous access

Anonymous access is a way to make analytics content from Qlik Sense available to users who are not members of a Qlik Cloud tenant. When an application is made available using anonymous access, visualizations and sheets from the application can be embedded into external web pages, and all sheets can also be made available directly for exploration by external users.

This functionality is only available with a Qlik Anonymous Access subscription. For more information, see [*Qlik Anonymous Access subscriptions*](../Admin/subscription-options-anonymous.htm).

See: [*Sharing application content with anonymous access*](../Share/share-anonymous-access.htm)

## Application

This term has several definitions:

1. A Qlik Sense or QlikView application: Applications are task-specific, purpose-built applications. Applications contain data loaded from data sources that is interpreted through visualizations.

   Similar terms: Document, workbook

   See: [*Understanding applications*](../Apps/App.htm)
2. The Qlik Analytics mobile app: A mobile app for iOS and Android devices. In the mobile app, you connect to and interact with your cloud data. You can work with your available applications.

   See: [*Qlik Analytics mobile app*](../Mobile/qsmsaas-intro.htm)

## Apply dataset

The dataset on which a trained machine learning model is making predictions. The output of a Qlik Predict prediction is a new dataset with predicted values for a chosen target field.

See: [*Creating predictions on datasets*](../AutoML/creating-predictions.htm)

## Area under curve (AUC)

A ROC Curve for AUC (area under curve) describes how good a machine learning model is at predicting the positive class when the actual outcome is positive. The closer the True Positive Rate is to 1.0 (the maximum possible area under the curve), the more deterministic the model is. The ROC Curve is useful for understanding if separation between classes is possible, thereby indicating if the data is good enough to accurately distinguish between predicted outcomes.

See: [*AUC and ROC curve*](../AutoML/scoring-binary-classification.htm#AUC)

## Assistant

Assistants provide a chat-based generative AI tool for asking questions and getting answers from unstructured data sources in knowledge bases.

See: [*Working with assistants*](../QlikAnswers/Assistants/assistants.htm)

## Associative insights

Associative insights is an Insight Advisor feature that compares your selections and the values excluded by your selections to help you find blind spots and hidden relationships.

See: [*Discovering your data with associative insights*](../Selections/associative-insights.htm)

## Binary classification (experiment and model type)

In Qlik Predict, an experiment that trains machine learning models to predict values for a target column with two possible values—for example, a Canceled column with values yes or no.

Similar terms: Experiment type, multiclass classification experiment

See: [*Classification problems*](../AutoML/classification-problems.htm)

## Bookmark

Bookmarks let you save specific selection states so they can be applied again in an application later and shared with other users. Layout information can be stored in bookmarks, so users can be taken to the correct place in the application when applying the bookmark.

See: [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm)

## Business logic

Business logic is a suite of features that allows you to customize the behavior of Insight Advisor. Business logic has two main features:

- Logical model: The data model of the application used when generating visualizations.
- Vocabulary: Alternative terms for natural language queries.

Similar terms: Logical model, vocabulary, domain logic

See: [*Customizing logical models for Insight Advisor*](../BusinessLogic/business_logic.htm)

## Cardinality

The uniqueness of data values in a column. When training a machine learning model, Qlik Predict cannot use feature columns with high cardinality (too many unique values) or no cardinality (column data consisting of one constant value).

See: [*Cardinality*](../AutoML/cardinality.htm)

## Catalog

The catalog is the area of activity centers where you can find your applications, datasets, data products, and data sources.
Catalog tools allow you to profile your data.

See: [*Understanding your data with catalog tools*](../Catalog/catalog-overview.htm)

## CDC (Change Data Capture)

In CDC landing mode, changes to the data source are captured as they occur and applied to the target in near real time.

See: [*Landing data from data sources*](../DataIntegration/Landing/Landing-data-data-sources.htm) and Full load below.

## Chart

Charts are objects where calculations, aggregations, and groupings can be made. Graphical visualizations, such as bar charts and pie charts are common examples, but also non-graphical objects such as pivot tables are charts.

A chart consists of dimensions and measures, where the measures are calculated once per dimensional value. If the chart contains multiple dimensions, the measures are calculated once per combination of dimensional values.

Similar terms: Visualization, Hypercube, Cube

See: [*Choosing the right visualization*](../Visualizations/creating-visualization.htm)

## Collection

Collections are a tool that let you group applications, charts, notes, automations, experiments and links in activity centers for ease of access and sorting.

## Confusion matrix

A confusion matrix summarizes the accuracy of prediction results in a classification model. The number of correct and incorrect predictions are summarized for each class. This gives you insight not only into the errors being made by your classifier but also the types of errors that are being made.

See: [*Confusion matrix*](../AutoML/scoring-binary-classification.htm#Confusio)

## Cross-validation

A process completed during experiment training in Qlik Predict in which training data is split into five segments (folds), allowing each segment of the data to be used as a test on the other four segments. Cross-validation results in metrics that will show how well a model can make predictions on data it has never seen before.

See: [*Holdout data and cross-validation*](../AutoML/holdout-crossvalidation.htm)

## Custom object

Custom objects are custom visualizations added to tenants by tenant administrators or included in one of the Qlik extension bundles.

Similar terms: Extensions

See: [*Creating a visualization using a custom object*](../Visualizations/create-visualization-extensions.htm)

## Data asset

A fit-for-purpose collection of datasets.

See: [*Creating and managing data pipeline projects*](../DataIntegration/Introduction/Data-projects.htm)

## Data catalog

The data catalog is a component in Data manager and Data load editor that enables you to select and load data from all the datasets to which you have access.

See: [*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm)

## Data connection

### In Analytics Services:

Data connections are used to load data from external data sources into Qlik Cloud for the purpose of creating analytics, in the form of applications and scripts. Data connections can load data from databases and remotely stored files.

See: [*Adding and managing your analytics data*](../Spaces/managing-data-resources-spaces.htm)

### In Data Integration:

Data connections are used to let data tasks access data sources, and external storage and cloud data warehouses used in a data project.

See: [*Setting up connections to data sources*](../DataIntegration/Landing/connecting-data-2.htm)

## Data flow

A data flow is an intuitive no-code experience that allows you to create a visual flow to prepare data. Place your source on the canvas, and use a variety of processors to combine and shape your data in order to produce clean datasets for your analytics applications or ML experiments.

See: [*Loading and preparing data with Data flow*](../DataFlow/loading-preparing-with-data-flow.htm)

## Data Gateway, Data Movement

Qlik Data Gateway - Data Movement allows you to move firewalled data from your enterprise data sources to cloud and on-premises targets, over a strictly outbound, encrypted and mutually authenticated connection. By eliminating the need to open inbound firewall ports, Qlik Data Gateway - Data Movement provides a secure and trusted means for accessing your enterprise data.

Similar terms: Data Movement gateway

See: [*Qlik Data Gateway - Data Movement*](../Gateways/replication-gateway.htm)

## Data Gateway, Direct Access

Qlik Data Gateway - Direct Access allows Qlik SenseSaaS applications to securely access firewalled data, over a strictly outbound, encrypted, and mutually authenticated connection.

See: [*Qlik Data Gateway - Direct Access*](../Gateways/direct-access-gateway.htm)

## Data leakage

An undesired phenomenon in machine learning in which an algorithm is trained with data for which it will be used to generate predictions. One indicator of data leakage is unrealistically high model performance, which results only from memorization of target values (which were incorrectly provided in the training data, either directly or indirectly) and not from actual learning of patterns and associations.

See: [*Data leakage*](../AutoML/data-leakage.htm)

## Data load editor

The Data load editor is a script editor that allows you to build and customize the script that loads data into your application.

Similar terms: Script editor

See: [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm)

## Data manager

Data manager is an application component that allows you to load and manage data sources in an application. You can also preview and associate the data and perform data transformations.

See: [*Loading and managing data with Data Manager*](../LoadData/managing-data.htm)

## Data marketplace

Depending on your rights and role in the organization, the Data marketplace is the area of Qlik Talend Data Integration activity center where data product managers working on data integration manage data products, and where data consumers such as analytics users browse available data products for their analytics applications.

See: [*Activating data products to the data marketplace*](../DataIntegration/Marketplace/Consuming-in-data-marketplace.htm)

## Data mart

Data marts are the part of your data pipeline that contain a subset of data from your Storage or Transform data assets. You can create any number of data marts depending on your business needs. Ideally, your data marts should contain repositories of summarized data collected for analysis on a specific section or unit within your organization.

See: [*Creating and managing data marts*](../DataIntegration/DataMarts/DataMarts.htm)

## Data model viewer

Data model viewer is an application component that allows you to view the structure of the data added to an application and view metadata about tables and fields.

See: [*Viewing and transforming the data model*](../DataModeling/view-data-model.htm)

## Data pipeline

In a data project, a data pipeline is a set of tasks for integrating data. Onboarding moves data into the project from data sources that are on-premises or in the cloud and store the data in ready-to-consume data sets. You can also perform transformations and create data marts to leverage your generated and transformed data sets. The data pipeline can be simple and linear, or it can be a complex pipeline consuming several data sources and generating many outputs.

See: [*Creating and managing data pipeline projects*](../DataIntegration/Introduction/Data-projects.htm)

## Data product

Data products are highly trusted, re-usable, and consumable data assets. More specifically, they are curated collections of productized datasets and business-approved metadata and domain logic designed to solve domain-specific business outcomes.

See: [*Creating data products*](../DataIntegration/DataProducts/Creating-data-products.htm)

## Data profiling

Data profiling displays statistics and information about your data sets.

See: [*Managing field-level metadata and data profiling*](../Catalog/Profiling-data.htm)

## Data project

A data project is where you create your data pipeline, using data assets. The data project is associated with a data platform that is used as target for all output. You can create a simple linear pipeline, or a complex pipeline consuming several data sources and generating many outputs.

See: [*Introducing Data Integration*](../DataIntegration/Introduction/Data-services-introduction.htm)

## Data task

A data task is the main unit of work in a data project. In a data project. you can create data tasks of the following types:

- Landing - Move your data from the data source to a cloud data warehouse or Qlik Cloud.
- Storage - Store landing data in read-to-consume datasets.
- Registered data - Register data that already exists on the data platform.
- Transform - Transform your data according to target requirements and business needs.
- Data mart - Create data marts from stored or transformed data.

You can also combine the landing and storage into a single "Onboarding" task.

See: [*Data task*](../DataIntegration/Introduction/Data-services-introduction.htm#Data)

## Dataset

The term dataset is sometimes synonymous with table. It can refer to the original source table, the table after undergoing transformations, or the fact and dimension tables in a data mart.

It can also refer to a logical table, where there are several instance tables and views:

- Current data
- History, which holds previous versions of the table
- Changes

See: [*Managing datasets*](../DataIntegration/Introduction/Managing-datasets.htm)

## Dimension

### In Analytics Services:

A dimension is an entity used to categorize data in a chart. For example, the slices in a pie chart or the bars of a bar chart represent individual values in a dimension. Dimensions are often a single field with discrete values, but can also be calculated in an expression.

Similar terms: Category, group

See: [*Data grouping with dimensions*](../Dimensions/dimensions.htm)

### In Data Integration:

A dimension is a dataset in a data mart that forms part of the star schema. Dimension datasets hold the descriptive information for all related fields that are included in the fact table’s records. A few common examples of dimension datasets are Customer and Product. Since the data in a dimension dataset is often denormalized, dimension datasets have a large number of columns.

See: [*Creating and managing data marts*](../DataIntegration/DataMarts/DataMarts.htm)

## Discovery Agent

A service available in Qlik Cloud Analytics that allows creation of insight triggers and generation of insights from these insight triggers, in the form of an easy-to-consume feed.

Similar terms: Feed, insight trigger

See: [*Discovery Agent*](../DiscoveryAgent/discovery-agent.htm#Search)

## Distribution list

The list of all possible receivers who can be added as recipients (individually or as part of a group) from a Qlik Sense report task. Each Qlik Sense application can have one distribution list. When you create a report task, you select only the recipients and groups from your distribution list to which you want to send the task output. Report filters can be added individually to recipients in the distribution list, allowing burst reporting administered from a single report task.

Similar terms: Report task, report filter

See: [*Creating a distribution list for your report*](../Reporting/Generate/cloud-in-app-reports-distribution.htm)

## Dynamic views

Dynamic views allow you to query and view relevant subsets of large datasets from another application in a chart. They can be dynamically refreshed as selections are made. Dynamic views are similar to on-demand applications.

See: [*Managing data with dynamic views*](../DynamicViews/dynamic-views.htm)

## Experiment type

The experiment type defines the type of machine learning model that will be trained in an ML experiment. The experiment type is defined by the number of unique vales, as well as type of data, in the selected target column. The following experiment types are available: binary classification, multiclass classification, regression, and time series.

Similar terms: Target (machine learning), binary classification experiment, multiclass classification experiment, regression experiment

See: [*Machine learning concepts*](../AutoML/machine-learning-basics.htm#Machine)

## Fact

A fact table works with dimension tables. A fact table holds the data to be analyzed, and a dimension table stores data about the ways in which the data in the fact table can be analyzed. Thus, the fact table consists of two types of columns: primary key columns and measure columns. The primary key columns allows joins with dimension tables, and the measures columns contain the data that is being analyzed. For example, the Orders fact dataset will simply list that on such and such a day, a certain customer bought a quantity of a certain product whereas the related dimension datasets will provide more information about the customer, the product, and the region in which the transaction took place.

See: [*Creating and managing data marts*](../DataIntegration/DataMarts/DataMarts.htm)

## Favorites

Favorites is a section available to all users where they can add applications, datasets, automations, notes, experiments and charts from the hub.
Favorites are private.

## Feature (machine learning)

A variable in a machine learning problem that can potentially contribute to the value of the target column. In Qlik Predict, features are columns in a dataset which can have varying levels of influence on the results in the target column. Features are sometimes called covariates.

See: [*Machine learning concepts*](../AutoML/machine-learning-basics.htm#Machine)

## Feed

A scrollable interface in Qlik Cloud Analytics that allows users to explore insights in an easily consumable manner.

Similar terms: Insight trigger, Discovery Agent

See: [*Discovery Agent*](../DiscoveryAgent/discovery-agent.htm#Search)

## Field

A field contains values, loaded from a data source. At a basic level, a field corresponds to a column in a table. Fields are used to create dimensions and measures in visualizations.

See: [*Fields*](../DataSource/fields.htm)

## Full load

In Qlik Talend Data Integration, Full Load refers to the initial replication of data from the data source to the landing.

See: [*Landing data from data sources*](../DataIntegration/Landing/Landing-data-data-sources.htm) and CDC above.

## Holdout data

In an ML experiment, holdout data is a subset of the training dataset that is set aside and not used during the training of an algorithm and subsequently used to score model performance.

See: [*Holdout data and cross-validation*](../AutoML/holdout-crossvalidation.htm)

## Hub

The hub is the central point of access for applications, spaces, and collections. The term hub has been replaced with activity center.

Similar terms: Access point, Activity center

## Hyperparameter optimization

A process of fine-tuning the constraints, weights, and learning rates of a machine learning model to increase its performance in solving a problem. In Qlik Predict, this is not enabled by default but can be applied during experiment configuration for potentially improved results.

See: [*Hyperparameter optimization*](../AutoML/hyperparameter-optimization.htm)

## Impact analysis

Impact analysis shows the forward-looking, downstream view of a database, application, or field dependencies.

See: [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm)

See: [*Analyzing impact analysis in Data Integration*](../Catalog/impact-analysis-di.htm)

## Insight Advisor

Insight Advisor is a suite of features. Insight Advisor can help build your data model, create visualizations, and analyze your data.

See: [*What is Insight Advisor and business logic?*](../BusinessLogic/Tutorial/tutorial-what-is-insight-advisor.htm)

## Insight Advisor Analysis Types

Insight Advisor Analysis Types is an Insight Advisor feature that creates visualizations for you by letting you select the analysis type you want to see and the data you want used.

See: [*Insight Advisor Analysis Types*](../Insights/insight-advisor-create-visualizations.htm#AnalysisType)

## Insight Advisor Chat

Insight Advisor Chat is a chat-based interface for conversational analytics. Insight Advisor Chat enables you to ask questions from the applications to which you have access. Insight Advisor Chat then returns relevant visualizations.

See: [*Exploring applications with conversational analytics*](../Insights/insights-chat.htm)

## Insight Advisor Search

Insight Advisor Search is a Insight Advisor feature that allows you to ask natural language questions in an application and receive relevant visualizations.

See: [*Insight Advisor Search*](../Insights/insight-advisor-create-visualizations.htm#Search)

## Insight trigger

An item created in sheets by application developers to allow automatic generation of insights, which are consumed in the form of a feed.

Similar terms: Feed, Discovery Agent

See: [*Working with Discovery Agent insight triggers*](../DiscoveryAgent/insight-triggers.htm#Search)

## Intelligent model optimization

A set of capabilities in Qlik Predict that provide advanced, automatic refinement of the models you train in an experiment. With intelligent model optimization, you can quickly train ready-to-deploy machine learning models without needing to iterate feature selection or apply advanced processing to your data manually. Advanced refinement steps can include dropping of features, performing feature-level transformations, and applying handling across specific rows.

See: [*Intelligent model optimization*](../AutoML/intelligent-model-optimization.htm)

## Key driver analysis

A tool in a Qlik Sense application that allows you to compare the influence that a set of fields in your application has on the data trends and outcomes of a specific target field. You can employ key driver analysis to gain understanding of what is driving business and organizational performance metrics, and take action with data-driven decisions.

See: [*Uncovering the key influencers behind your data using key driver analysis*](../KeyDrivers/introduction-key-driver-analysis.htm)

## Knowledge base

Knowledge bases are collection of individual data sources, connected through a data connection, that are indexed data for use in generating responses to user questions.

See: [*Working with knowledge bases*](../QlikAnswers/KnowledgeBases/knowledge-bases.htm)

## Knowledge mart

Creating knowledge marts lets you embed and store your structured and unstructured data in a vector database. This allows the augmented context to be retrieved with semantic search features to be used as a context for Retrieval Augmented Generation (RAG) applications.

See: [*Creating knowledge marts*](../DataIntegration/KnowledgeMart/Creating-knowledge-marts.htm)

## Land

The process of moving data from a data source to a landing zone in a cloud data warehouse.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Landing

In Qlik Talend Data Integration, landing can refer to one of the following:

- A database - commonly known as a landing zone - in a cloud data warehouse where source data initially "lands" before being processed further down the data pipeline
- The actual task or process that moves the data from the data source to the landing zone

The landing task in Qlik Talend Data Integration controls the continuous or scheduled landing of data from the data sources to the landing zone.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Large application support

With large application support, you can work with applications that are larger than the standard application size for your subscription. Administrators can assign large application support to specific spaces.

See: [*Large application support*](../Admin/large-app-support.htm)

## Lineage

Lineage tracks data and data transformations back to their original source, representing it as a lineage graph.

See: [*Analyzing lineage in Analytics*](../Catalog/lineage.htm)

See: [*Analyzing lineage in Data Integration*](../Catalog/lineage-di.htm)

## Live views

In Qlik Talend Data Integration, Live views allow you to access both current data (ODS) and historical data (HDS). Live views include data from changes tables that is not yet applied to the current or prior tables. This lets you see data with lower latency without having to apply changed data frequently. The ability to delay the merge allows for reduced costs and processing requirements in the target platform.

See also: [*Live view*](../DataIntegration/Storage/dataset-tables.htm#Live)

## Load script

The load script is a sequence of statements that defines what data to load and how to link the different loaded tables. It can be generated with the Data manager, or with the Data load editor, where it also can be viewed and edited.

Similar terms: Script

See: [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm)

## Logical model

The logical model is the underlying data model that tells Insight Advisor how to use data when generating visualizations.

Similar terms: Logic model, logic framework

See: [*Building logical models for Insight Advisor with Business logic*](../BusinessLogic/business-logic-logical-models.htm)

## Master item

Master items are dimension, measures, or visualizations that have been saved so they can be reused in other visualizations or sheets. You can then make changes or updates to the master item in a single place and have it impact all objects that use the master item.

See: [*Reusing assets with master items*](../Assets/work-with-master-items.htm)

## Measure

A measure is a calculation base on one ore more aggregations. For example, the sum of sales is a single aggregation, while the sum of sales divided by the count of customers is a measure based on two aggregations.

Similar terms: Aggregation, calculation, metric

See: [*Measures*](../Measures/measures.htm)

## ML deployment

A container to which one or more machine learning models are deployed for use in predictions.

See: [*Deploying models*](../AutoML/deploying-models.htm)

## ML experiment

An asset in Qlik Predict which allows you to train machine learning models using historical data, with the goal of deploying one or more of the final results for making predictions on new data.

See: [*Working with experiments*](../AutoML/working-with-experiments.htm)

## Model alias

A reference pointing to a model within an ML deployment. Predictions from ML deployments are directed to an alias rather than a specific model. This allows flexible and dynamic prediction workflows where models can easily be replaced without requiring configuration or API call updates. An ML deployment can contain up to 10 aliases, including the default alias.

See: [*Using multiple models in your ML deployment*](../AutoML/ml-deployment-available-models.htm)

## Model metrics

Details about how well an algorithm is performing during experiment training in Qlik Predict. Model metrics display how accurately each model is learning to determine the correct outcome to the machine learning problem. This helps in deciding which model you will deploy for use in creating predictions.

See: [*Analyzing models*](../AutoML/analyze-models.htm)

## Monitor in hub

Monitor in hub is a feature that allows you to add charts from sheets or Insight Advisor to activity centers so you can monitor them, without opening an application.

See: [*Monitoring visualizations*](../Hub/monitor-charts-hub.htm)

## Multiclass classification (experiment and model type)

In Qlik Predict, an experiment that trains machine learning models to predict values for a target column with 3 to 10 possible values—for example, a Plan Type  column with values such as Green Plan, Red Plan, or Purple Plan.

Similar terms: Experiment type, binary classification experiment

See: [*Classification problems*](../AutoML/classification-problems.htm)

## Net Changes table

Qlik Talend Data Integration performs data replication based on changes that appear in the source database's transaction log. A single update operation on the source, such as "UPDATE MyTable SET f1=..., f2=..." could potentially update many rows in the source database and create a large number of change records that the replication task will need to apply to the target. Replication tasks offers two Change Processing modes: Transactional apply and Batch optimized apply. In Transactional apply Change Processing mode, the replication task essentially applies each change to the target, which may take much longer than the original UPDATE took on the source. Batch optimized apply mode, on the other hand, is designed to handle efficient replication of a large number of changes. In this mode, the replication task accumulates changes for multiple tables in a memory cache. Repeated changes to the same row are updated in the memory cache. When the maximum memory cache size defined for the task is reached (or when the configured time has elapsed), the replication task does the following:

- Writes the cached (net) changes to a special table on the target (the Net Changes table),
- Bulk uploads the changes to the target table
- Uses SQL statements to update the target tables based on the data in the Net Changes table.

See: [*Replication settings*](../DataIntegration/Replicating/replicating-settings.htm)

## Notes

Notes let you quickly add text commentary to an application or chart. They can also contain snapshots of data. You can keep them private or share them with other users.

Similar terms: Comments

See: [*Capturing and sharing insights using Notes*](../Notes/notes-overview.htm)

## Notifications

Notifications let you know when there have been changes to applications or spaces, or when alerts you set have been triggered. You can also get notifications on operational changes for Data Integration tasks and data gateways.

See: [*Notifications*](profile-settings.htm#Notifica)

## On-demand application

On-demand applications load selections of data from large datasets without loading the full dataset into the application.

See: [*On-demand apps*](../LoadData/using-OnDemand-apps.htm)

## Onboarding

In a data project, the first step of creating a data pipeline is onboarding the data. This involves transferring the data continuously from the on-premises data source and generating datasets in read-optimized format.

See: [*Onboarding data to a data warehouse*](../DataIntegration/Onboarding/Onboarding-data.htm)

## Permissions

Permissions control what users can do in Qlik Cloud. They cover access to content, tenant-wide actions, and client applications. Space roles define access within spaces, and sharing lets you grant access to a single application. Tenant-wide permissions are managed through security roles and default permissions, while OAuth scopes filter these permissions for client applications.

Similar terms: Rights, user roles, security roles

See:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)
- [*Data space roles and permissions*](../DataIntegration/DataSpaces/permissions-data-space.htm)
- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users-capacity-model.htm)
- [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm)
- [*Sharing applications with users who are not space members*](../Spaces/sharing-content-with-non-space-members.htm)
- [*Creating and managing OAuth clients*](../Admin/mc-create-oauth-client.htm)

## Permutation importance

How much the machine learning model performance depends on a feature. When iterating on which features to include in the model, permutation importance can be used to determine which columns to keep, and which columns can be dropped.

See: [*Understanding permutation importance*](../AutoML/permutation-importance.htm)

## Preceding load

A preceding load is a script construct that allows you to load from the following LOAD or SELECT statement without specifying that source. Preceding loads are often faster than resident loads.

See: [*Loading data from a previously loaded table*](../Scripting/load-data-from-previously-loaded-table.htm)

## Prediction (machine learning)

An estimate, by a machine learning model, of the future value of a target column. In Qlik Predict, predictions can be generated by ML deployments as batch predictions (entire dataset with a prediction for reach row), or as real-time predictions (returned data consisting of predictions for one or a handful of dataset rows). Predictions can also be generated from an deployment using the Qlik Predict analytics connector.

Similar terms: Prediction, batch; prediction, real-time

See: [*Working with ML predictions*](../AutoML/working-with-predictions.htm)

## Prediction speed (machine learning)

The speed at which a machine learning model can generate predictions. In Qlik Predict, prediction speed is calculated using the combined feature computing time and test dataset prediction time. It is displayed in rows per second.

See: [*Prediction speed*](../AutoML/best-models.htm#PredictionSpeed)

## Prediction, batch (machine learning)

A batch prediction is a prediction that is generated on an entire dataset (the apply dataset). A prediction is generated for each row in the apply dataset, and delivered as a new dataset (the prediction dataset). This new dataset may also include probabilities if the model is a classification model.

Similar terms: Prediction, Apply dataset

See: [*Creating predictions on datasets*](../AutoML/creating-predictions.htm)

## Prediction, real-time (machine learning)

A real-time prediction is a prediction that is generated in real time on one or a few rows of data. Real-time predictions are generated using the real-time prediction endpoint in the Machine Learning API.

Similar terms: Prediction

See: [*Creating real-time predictions*](../AutoML/creating-real-time-predictions.htm)

## Processor

A processor is a logical component that you can add to your transformation flows in order to perform transformation operations on incoming data and return the transformed data to the next step of the flow.

See: [*Adding transformation flows*](../DataIntegration/Transformation/Adding-transformation-flows.htm)

## Professional user entitlement

Professional entitlement is intended for users who will create content in Qlik Sense. A user with Professional entitlement can create shared spaces, create, edit, and publish sheets or applications, and can create and edit alerts.

See: [*Managing user entitlements*](../Admin/SaaS-user-allocations.htm)

## Properties

When editing a sheet, Properties contains options for configuring and styling visualizations.

See: [*Properties panel*](../Sheets/navigating-sheets.htm#Properti)

## Qlik Answers

Qlik Answers is a plug-and-play subscription that adds generative AI (GenAI) knowledge assistants to Qlik Cloud. Qlik Answers assistants allow you to ask questions and get answers from unstructured data sources, such as text files and PDF.

See: [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm)

## QVD

A QlikView Data file (QVD) is a file containing data exported from Qlik Sense or QlikView. It is a native Qlik Sense format optimized for loading data quickly. You can also generate QVD files with Qlik Talend Data Integration.

See: [*Working with QVD files*](../Scripting/work-with-QVD-files.htm)

## Registered data

You can register data that already exists on the target platform to curate and transform data, and create data marts. This lets you use data that is onboarded with other tools than Qlik Talend Data Integration, for example, Qlik Replicate, or Stitch.

See: [*Registering data that is already on the data platform*](../DataIntegration/Onboarding/Registering-data.htm)

## Regression (experiment and model type)

In Qlik Predict, an experiment that trains machine learning models to predict values for a numeric target column with more than 10 possible values—for example, a Customer lifetime value column containing numeric data. Regression experiments are similar to, but distinct from, time series experiments. A regression experiment predicts numeric data without date-specific forecasts, while a time series experiment predicts numeric data for specific date values.

Similar terms: Experiment type, time series experiment

See: [*Regression problems*](../AutoML/regression-problems.htm)

## Report filter

A filter used to control the application data included in reports generated using in-application reporting. A report filter functions like a Qlik Sense application bookmark, but is purpose-configured for reporting capabilities. Report filters are highly customizable, and can be used in distribution lists and report tasks, as well as individual objects when authoring report templates.

Similar terms: Bookmark, report task, report template, distribution list

See: [*Working with report filters*](../Reporting/Generate/cloud-in-app-reports-filters.htm)

## Report task

A task created in a Qlik Sense application that converts one or more report templates into report output, applying data reduction as defined by the selected report filters. The report output is delivered according to the configured distribution settings.

Similar terms: Distribution list, report template, report filter

See: [*Working with report tasks*](../Reporting/Generate/cloud-in-app-reports-tasks.htm)

## Report template

A file outlining the structure, content, and data that is included in generated reports. With in-application reporting, you can create templates using Qlik add-ins for Microsoft Office, the embedded PixelPerfect designer, or the embedded HTML designer.

Similar terms: Tabular report, report task

See: [*Designing report templates*](../Reporting/Design/design-report-templates.htm)

## Report, tabular

A report containing table-based data from a Qlik Sense application, created based on a Microsoft Excel template file. In a tabular report, you can include visualization and application data in tabular form, and include chart images. Output can be in .xlsx or PDF format.

Similar terms: Report task, report template

See: [*Designing tabular report templates*](../Reporting/Design/Excel/design-tabular-report-templates.htm)

## Resident load

A resident load is a script construct that allows you to load from an already loaded table. Resident loads are often faster than accessing the original data source again.

See: [*Loading data from a previously loaded table*](../Scripting/load-data-from-previously-loaded-table.htm)

## Schemas

In a data project, artifacts are generated in an internal schema and a data asset schema.

- The internal schema contains the physical data tables.
- The data asset schema contains the views that you can use to consume the data.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Script

A script is a Qlik Cloud application for loading, transforming, and exporting data.

See: [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm)

## Script

Script is a scripting tool where you can edit the load scripts that load and export data from your script.
Script also allows you to view and manage inputs and outputs of your script, as well as published copies of the script.

See: [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm)

## Section access

Section access is a section of the data load script containing a security table that defines which users can see what data in an application.

See: [*Managing data security with Section Access*](../Scripting/Security/manage-security-with-section-access.htm)

## Selections

Selections are values selected by a user in visualizations in an application used to filter data. When a selection is made, all associated visualizations are updated to reflect the selection. Selections can be saved as bookmarks, and shared with other users.

See: [*Exploring data with visualizations*](../Selections/make-selection.htm)

## Service account owner

The service account owner (SAO) is responsible for maintaining and configuring the Qlik Cloud subscription.

See: [*Service account owner*](qlik-sense-admin-roles.htm#Service)

## Set analysis

Set analysis defines an alternative set of selections in a visualization different from those in the current selection. This allows for comparative analysis.

See: [*Set analysis*](../ChartFunctions/SetAnalysis/set-analysis-expressions.htm)

## SHAP importance

A measurement of how much influence each feature in an experiment has on the predicted outcome of the target. Qlik Predict creates aggregated, row-level SHAP importance ranking charts automatically during the training of binary classification and regression experiments.

See: [*Understanding SHAP importance in experiment training*](../AutoML/shap-importance.htm)

## Sheet

Sheets are components of Qlik Sense applications. They present visualizations to application users so they can explore, analyze, and discover data. Sheets can be public or private.

Similar terms: Dashboard, worksheet

See: [*Sheet view*](../Sheets/sheet-view.htm)

## Sheet objects

Sheets objects are components used to create an interface on a sheet. Not all sheet objects visualize data such as tables and charts. The can include other objects such as buttons, text objects, and extensions.

Similar terms: Visualization, chart

See: [*Sheet view*](../Sheets/sheet-view.htm)

## Snapshot

Snapshots are graphical representations of a visualization at a certain point of time. Snapshots are used to create stories.

Similar terms: Screenshot

See: [*Collecting insights for stories using snapshots*](../StoryTelling/Story/collect-insights-for-story.htm)

## Space, data

Data spaces are governed areas of your Qlik Cloud tenant that are used to create and store data projects. Inside the space, you can also create new data connections using connectors, and manage access to Data Movement gateways. All data assets will be created in the space of the data project that they belong to.

See: [*Working in spaces in Data Integration*](../DataIntegration/DataSpaces/working-spaces.htm)

## Space, managed

Managed spaces are carefully controlled spaces used to share applications with a limited group of users.

See: [*Working in managed spaces*](../Spaces/working-in-managed-spaces.htm)

## Space, personal

A personal space is a private space belonging to users where they can develop applications.

See: [*Working in spaces*](../Spaces/Spaces.htm)

## Space, shared

Shared spaces are areas applications and data sources can be shared with other users for collaborative development.

See: [*Working in shared spaces*](../Spaces/working-in-shared-spaces.htm)

## SQL transformation

A SQL transformation allows you to input a SQL SELECT query into a transformation task in a pipeline to define complex or simple transformations.

See: [*Adding SQL transformations*](../DataIntegration/Transformation/Adding-SQL-based-tables.htm)

## Storage

Storage is the part of the data pipeline that contains ready to consume datasets in a cloud data warehouse, or in Qlik Cloud, from the data copied from the landing zone. The datasets can be kept up-to-date with the landing zone data without manual intervention.

See: [*Storing datasets*](../DataIntegration/Storage/generating-datasets.htm)

## Story

A story is an application tool that allows you to share data insights and discoveries you have made in an application with other users, combining reporting, presentation, and exploratory analysis.

Similar terms: Report

See: [*Sharing insights with data storytelling*](../StoryTelling/use-data-storytelling.htm)

## Subscription

Subscription reports let you schedule recurring emails containing a PDF of your selected sheets or charts.

See: [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm)

## Synthetic key

A synthetic key is a composite key between two tables in the data model. They are created when two or more tables have two or more fields in common. If you receive a warning about synthetic keys when loading data, you may need to review the data structure in the data model viewer. A synthetic key is not necessarily a problem, but if you have synthetic keys based on other synthetic keys, there may be errors in your data model.

See: [*Synthetic keys*](../Scripting/synthetic-keys.htm)

## Table recipe

A table recipe allows you to easily prepare tabular datasets within a no-code, spreadsheet-like interface. Iteratively explore, clean, and transform data through a series of reusable steps to produce a recipe.

See: [*Loading and preparing data with Table recipe*](../TableRecipe/loading-preparing-with-table-recipe.htm)

## Tables: ODS, HDS, and Change

In a data project, there are several types of table, which may or may not exist depending on the project settings:

- Current table (ODS)

  This table contains the replica of the data source updated with changes during the latest apply interval.
- Prior table (HDS)

  This table contains Type 2 historical data. It is only generated if History is enabled in the data task settings.

  When a source table record is updated, a new record is added to the prior table each time. The history record is a copy of the previous current record, which also includes what was updated, and when it was valid.
- Change table

  This table contains all changes that are not yet applied to the current table. It is only generated if the landing mode Full load and CDC is used.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Target

This term has several definitions:

1. In the context of machine learning, a target is the information that a machine learning problem aims to predict. In Qlik Predict, the target is a column in the dataset.

   See: [*Machine learning concepts*](../AutoML/machine-learning-basics.htm#Machine)
2. In the context of data movement, a target refers to the destination or endpoint where data is intended to be transferred, stored, or loaded. It's the location or system that receives the data being moved from a source. The target could be a database, data warehouse, cloud storage, server, or any other destination where the data is meant to be utilized, analyzed, or processed. Data movement involves transferring information from a source to a target, often as part of data integration, migration, or synchronization processes.

   See: [*Integrating data*](../DataIntegration/Introduction/Data-services.htm)

## Tenant

The tenant is your cloud deployment of Qlik Cloud. It is a container for items such as users, applications, and spaces.

Similar terms: Deployment

See: [*Creating and configuring your tenant*](qcs-tenant-domain.htm)

## Time series (experiment and model type)

In Qlik Predict, an experiment that trains machine learning models to forecast date-specific values for a numeric target column with more than 10 possible values—for example, Sales values by date or time stamp. Time series experiments are similar to, but distinct from, regression experiments. A regression experiment predicts numeric data without date-specific forecasts, while a time series experiment predicts numeric data for specific date values.

Similar terms: Experiment type, regression experiment

See: [*Time series problems*](../AutoML/time-series-problems.htm)

## Training dataset

The dataset used to train a machine learning model in Qlik Predict. By allowing algorithms to learn patterns and associations in your data, the resulting model is equipped to make predictions on new data (the apply dataset).

See: [*Getting your dataset ready for training*](../AutoML/dataset-preparation.htm)

## Transform

A transform task is the part of your data pipeline that allows you to create reusable data transformations based on rules and custom SQL. You can perform row-level transformations and create datasets that are either materialized as tables, or created as views that perform transformations on the fly.

See: [*Transforming data*](../DataIntegration/Transformation/Transformations.htm)

## Transformation flow

A transformation flow is a visual representation of a data transformation. Transformation flows allow you to easily create complex or simple transformations with sources, processors, and targets, and provide a data preview of transformations at every step of your flow.

See: [*Adding transformation flows*](../DataIntegration/Transformation/Adding-transformation-flows.htm)

## Type 1 - Operational Data Store (ODS)

In a Type 1 dataset, the new information simply overwrites the original information. In other words, no history is kept.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Type 2 - Historical Data Store (HDS)

In a Type 2 dataset, a new record is added to the table to represent the new information. Therefore, both the original and the new record will be present. The new record will have its own primary key.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Variable

A variable in Qlik Sense is a container storing a static value or a calculation, for example a numeric or alphanumeric value.

See: [*Using variables in expressions*](../Variables/work-with-variables.htm)

## Views

Views are used in data projects. A view is a virtual representation of the physical datasets. As views result from querying the physical datasets, they will always pick the relevant data from the underlying dataset. Views have several advantages over physical datasets: they are able to produce a single result set from joins between multiple datasets; they control access to underlying data; and they do not take up any significant disk space.

There can be several types of view in a data project. Which views are created depends on if you have enabled live views and history, and if you are using change processing.

See: [*Dataset architecture in a cloud data warehouse*](../DataIntegration/Storage/dataset-tables.htm)

## Visualization

Visualizations are charts, extensions, and other objects that visualize your data for exploration in a sheet.

Similar terms: Chart

See: [*Working with visualizations*](../Visualizations/working-with-visualizations.htm)

## Vocabulary

Vocabulary is a business logic feature that allows you to add synonyms and custom analyses to Insight Advisor Search and Insight Advisor Chat.

See: [*Creating vocabularies for Insight Advisor*](../BusinessLogic/business-logic-vocabulary.htm)

## Write table

A table-based chart available in analytics applications. The write table allows analyzers to make changes to editable columns. These changes can be extracted via API, and can be used in third-party systems or loaded back into Qlik Cloud with applications and scripts.

See: [*Write table*](../Visualizations/WriteTable/Analyze/write-table.htm)

## Help Resources

- [Qlik Help Videos](https://www.youtube.com/channel/UCFxZPr8pHfZS0n3jxx74rpA)
- [Qlik Developer](https://qlik.dev/)
- [Qlik Training](https://www.qlik.com/us/services/training)
- [Qlik Learning](https://learning.qlik.com)
- [Qlik Customer Portal](https://customerportal.qlik.com/)
- [Qlik Resource Library](https://www.qlik.com/us/resource-library)

## Products

### Data Integration and Quality

- [Qlik Talend](https://www.qlik.com/us/products/qlik-talend-data-integration-and-quality)
- [Qlik Talend Cloud](https://www.qlik.com/us/products/qlik-talend-cloud)
- [Talend Data Fabric](https://www.qlik.com/us/products/talend-data-fabric)

### Analytics & AI

- [Qlik Cloud Analytics](https://www.qlik.com/us/products/qlik-cloud-analytics)
- [Qlik Answers](https://www.qlik.com/us/products/qlik-answers)
- [Qlik Predict](https://www.qlik.com/us/products/qlik-predict)
- [Qlik Automate](https://www.qlik.com/us/products/qlik-automate)

## Why Qlik?

- [Why Qlik](https://www.qlik.com/us/why-qlik-is-different)
- [Trust and Security](https://www.qlik.com/us/trust)
- [Trust and Privacy](https://www.qlik.com/us/trust/privacy)
- [Trust and AI](https://www.qlik.com/us/trust/ai)
- [Why Qlik for AI](https://www.qlik.com/us/why-qlik-for-ai)
- [Compare Qlik](https://www.qlik.com/us/compare)
- [Featured Technology Partners](https://www.qlik.com/us/products/technology/featured-partners)
- [Data Sources and Targets](https://www.qlik.com/us/products/data-sources)
- [Qlik Regions](https://www.qlik.com/us/regions)

## About Qlik

- [Company](https://www.qlik.com/us/company)
- [Leadership](https://www.qlik.com/us/company/leadership)
- [CSR](https://www.qlik.com/us/company/corporate-responsibility)
- [DEI&B](https://www.qlik.com/us/company/diversity)
- [Academic Program](https://www.qlik.com/us/company/academic-program)
- [Partner Program](https://www.qlik.com/us/partners)
- [Careers](https://www.qlik.com/us/company/careers)
- [Newsroom](https://www.qlik.com/us/company/press-room)
- [Global Office/Contact](https://www.qlik.com/us/contact)

![](../_images/img/logos/logo-qlik-footer.svg)

- [Qlik Community](https://community.qlik.com/)
- [![](../_images/img/social/twitter-2024.svg)](https://twitter.com/qlik)
- [![](../_images/img/social/linkedin-2024.svg)](https://www.linkedin.com/company/qlik)
- [![](../_images/img/social/fb-2024.svg)](https://www.facebook.com/qlik)

- [Legal Agreements](https://www.qlik.com/us/legal/legal-agreements)
- [Product Terms](https://www.qlik.com/us/legal/product-terms)
- [Legal Policies](https://www.qlik.com/us/legal/legal-policies)
- [Privacy & Cookie Notice](https://www.qlik.com/us/legal/privacy-and-cookie-notice)
- [Terms of Use](https://www.qlik.com/us/legal/terms-of-use)
- [Trademarks](https://www.qlik.com/us/legal/trademarks)
- Do Not Share My Info

Copyright © 1993-2026 QlikTech International AB. All rights reserved.
