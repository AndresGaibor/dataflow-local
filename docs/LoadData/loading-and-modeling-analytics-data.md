---
title: "Loading and modeling analytics data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/loading-and-modeling-analytics-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Loading and modeling analytics data

You need to add data sources before you can create [sheets](#glossary-0 "Glossary term") and [visualizations](#glossary-1 "Glossary term") in a Qlik Sense application. Data sources can be added in the Analytics [activity center](#glossary-3 "Glossary term") or in a Qlik Sense application.

Qlik Cloud Analytics supports datasets, [data connections](#glossary-4 "Glossary term"), and data products. Datasets can be:

- Uploaded once and never modified.
- Replaced or refreshed with net new changes.

Data connections provide ways to access data sources you commonly use whether they are databases, local files, or remote files.

Once your data sources are added, you can load the data into an application and build your data model. You can take advantage of Insight Advisor’s analysis-based recommendations for associating tables and building data models, or you can create your own associations and joins. You can manage and modify the data from datasets and data connections once they are added in an application.

Data products allow you to gather and package trusted datasets related to the same domain. Once activated, the curated data products can be browsed and consumed in the data marketplace. For more information, see [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm).

You can also load and add data to scripts. Scripts allow you to load, transform, and export data for use in analytics applications. For more information, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).

## Adding data to Qlik Cloud Analytics

Learn how to add datasets and connections to data sources and manage them from spaces.

[*Adding and managing your analytics data*](../Spaces/managing-data-resources-spaces.htm)

## Loading data

Information noteIf your source data resides behind a firewall, you can securely access it using Qlik Data Gateway - Direct Access. For more information, see [*Qlik Data Gateway - Direct Access*](../Gateways/direct-access-gateway.htm).

### [*Loading data from the data catalog*](adding-data-catalog.htm)

Learn how to load data into your application from the datasets to which you have access.

### [*Loading data from the data marketplace*](../DataIntegration/Marketplace/loading-data-from-marketplace.htm)

Learn how to load data into your application from an existing data product that you can access in the data marketplace.

### [*Loading and managing data with Data Manager*](managing-data.htm)

Learn how to connect to, add, and manage data with Data Manager.

### [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm)

Learn how to connect to and retrieve data from various data sources using data load scripts.

### [*Collaboratively developing data load scripts in shared spaces*](script-codevelopment.htm)

Learn how to co-develop application load scripts with other users.

### [Data sources](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm)

Whether your data is stored on-premises or in the cloud, you can quickly load it into SaaS editions of Qlik Sense.

### [*Script syntax and chart functions*](script-syntax-functions.htm)

Learn how to use statements and functions in the script to load and transform data into your application.

Tutorial

### [Scripting for beginners](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/introduction-getting-started-scripting.htm)

This tutorial introduces loading and manipulating data in Qlik Sense using scripting in the data load editor.

Tutorial

### [Next steps in scripting](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/introduction-next-steps.htm)

This tutorial introduces advanced scripting concepts. This includes transforming data using cross-tables, cleaning data, and creating and loading data from Qlik data files (QVD).

Video (3 min)

### [Load, prepare, and associate data](https://share.vidyard.com/watch/bmF9Cs3d3bfh1snBtaJ8jH)

Video (3 min)

### [Connecting to your data](https://share.vidyard.com/watch/phDQNHgTYkUuFabpbq51mB)

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikIcons/video.svg)

Video (4 min)

### [Loading data from the data catalog](https://share.vidyard.com/watch/Nck5rRwL6wUTMXyYHJJHcJ)

Learn how to load data into your application from existing datasets that you can access in the data catalog

## Refreshing data

### [*Refreshing analytics data*](../Refresh/refresh-analytics-data.htm)

Learn about the various methods you can use to refresh the data for your application, script, data flow, or table recipe.

### [*Scheduling data refreshes with tasks*](../Refresh/refresh-work-with-tasks.htm)

Learn how to create tasks for convenient, flexible scheduling of data refreshes.

### [*Managing tasks for data refreshes*](../Refresh/refresh-manage-tasks.htm)

Learn how to manage existing tasks configured for data refreshes.

### [*Creating task chains for data refreshes*](../Refresh/task-chains-for-refresh.htm)

Learn how to start a chain of tasks that execute one after the other to refresh data across applications, scripts, data flows, and table recipes.

## Modeling data

### [*Viewing and transforming the data model*](../DataModeling/view-data-model.htm)

Learn how to view and transform the data structure of an application.

### [*Best practices for data modeling*](../DataModeling/best-practices-data-modeling.htm)

Take a look at the best practices for data modeling.

### [*Understanding your data with catalog tools*](../Catalog/catalog-overview.htm)

Learn how to improve your data efficiency while maintaining security and compliance standards.

Walkthrough

### [Combining tables using forced concatenation](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/step-by-step-concatenate-tables.htm)

This step-by-step walkthrough shows how you can use forced concatenation to combine two similar data tables.

Walkthrough

### [Incrementing data loads with the STORE command](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/step-by-step-store-load.htm)

This step-by-step example shows how to increment data loads using the Store command.

## Managing data

### [*Managing data security with Section Access*](../Scripting/Security/manage-security-with-section-access.htm)

Learn how use section access to control the security of an application.

### [*Managing big data with on-demand applications*](../DataSource/Manage-big-data.htm)

Learn how to load and analyze big data sources in Qlik Sense using on-demand applications.

### [*Managing data with dynamic views*](../DynamicViews/dynamic-views.htm)

Learn how to control the analytic sources and when data is refreshed in visualizations using dynamic views

### [*Customizing logical models for Insight Advisor*](../BusinessLogic/business_logic.htm)

Learn how to customize how Insight Advisor interprets your application data when generating insights from queries.

Tutorial

### [Customizing how Insight Advisor interprets data](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-customizing-insight-advisor.htm)

This tutorial introduces how you can use business logic to customize how Insight Advisor interprets your data in search-based analytics.

Related learning:

- [How do I load data into a Qlik Sense application?](/lnk/How_load_data_QS_SaaS_app)
- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
