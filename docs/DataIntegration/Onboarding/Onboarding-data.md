---
title: "Onboarding data to a data warehouse"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Onboarding/Onboarding-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects"]
---

# Onboarding data to a data warehouse

The first step of creating a data pipeline in a Qlik Talend Data Integration project is onboarding the data. This involves transferring the data from the data source and storing datasets in read-optimized format. You can update data with continuous change handling, or use scheduled reloads.

You create onboarding in a single operation, but it is performed in two steps.

- Landing the data

  This involves transferring the data continuously from the on-premises data source to a landing area, using a Landing data task.

  [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm)

  You can also land data to a lakehouse, where the data is landed to cloud file storage. This is available for Snowflake projects, where the landing target is set to Cloud file storage.

  [*Landing data to a lakehouse*](../Landing/Lake-landing.htm).
- Storing datasets

  This involves reading the initial load of landing data or incremental loads, and applying the data in read-optimized format using a Storage data task.

  [*Storing datasets*](../Storage/generating-datasets.htm)

When you have onboarded the data, you can use the stored datasets in several ways.

- You can use the datasets in an analytics application.
- You can create transformations.
- You can create a data mart.

## Onboard data

You start onboarding data in a project. Datasets will be stored in the cloud data warehouse defined in the project. For more information about projects, see [*Creating and managing data pipeline projects*](../Introduction/Data-projects.htm).

1. In your project, click Create and then Onboard data.

   Tip noteYou can also click ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on an existing source in the project, and then click Onboard data.
2. Add Name and Description for the onboarding.

   Click Next.
3. Select the source connection.

   You can select an existing source connection or create a new connection to the source.

   For more information, see [*Setting up connections to data sources*](../Landing/connecting-data-2.htm).

   Click Next.
4. Select data to load.

   For more information, see [*Selecting data*](#Selectin).

   Click Next.

   Settings is displayed, where you can select update method and history settings.
5. Select which method to use to update data in Update method:

   - Change data capture (CDC)

     If your data also contains tables that do not support CDC, or views, two data pipelines will be created. One pipeline with all tables supporting CDC, and another pipeline with all other tables and views using Reload and compare.
   - Reload and compare
6. If you are onboarding to Snowflake, you can choose one of the following loading methods:

   - Bulk loading (the default)

     If you select Bulk Loading, once the task is created, you will be able to tune the loading parameters in the task settings' Data uploading tab.
   - Snowpipe Streaming

     Information note

     Snowpipe Streaming will only be available for selection if the following conditions are met:

     - The Change data capture (CDC) update method is enabled.
     - The Authentication Mechanism in the Snowflake connector is set to Key Pair.
     - If you are using Data Movement gateway, version 2024.11.45 or later is required.

     If you select Snowpipe Streaming, make sure you are familiar with the [limitations and considerations](../TargetConnections/snowflake-target.htm#Limitati2) when using this method. Additionally, if you select Snowpipe Streaming and then switch to the Reload and compare update method, the loading method will automatically switch back to Bulk loading.

   The main reasons to choose Snowpipe Streaming over Bulk loading are:

   - Less costly: As Snowpipe Streaming does not use the Snowflake warehouse, operating costs should be significantly cheaper, although this will depend on your specific use case.
   - Reduced latency: As the data is streamed directly to the target tables (as opposed to via staging), replication from the data source to the target should be faster.

   Tip noteWhen using Snowpipe Streaming, the initial full load might be significantly slower than Bulk loading. To optimize the loading performance, especially when loading large datasets, best practice is to use Snowpipe Streaming together with the [parallel load feature](../Landing/Table-settings-landing.htm).
7. Select if you want to replicate history of previous data in addition to current data in History.

   Click Next when you are ready.
8. If you are not using Data Movement gateway to access your data source, the following section will be displayed in the settings:

   Replication scheduler

   - Replicate data every: You can schedule how often to capture changes from the data source and set a Start time and Start date. If the source datasets support CDC (Change data capture), only the changes to the source data will be replicated and applied to the corresponding target tables. If the source datasets do not support CDC (for example, Views), changes will be applied by reloading of all the source data to the corresponding target tables. If some of the source datasets support CDC and some do not, two separate sub-tasks will be created: one for reloading the datasets that do not support CDC, and the other for capturing the changes to datasets that do support CDC.

     The onboarding setup wizard allows you to schedule an hourly interval. After you have completed the onboarding wizard, you can explore different scheduling options, as described in [*Replication settings*](../Replicating/replicating-settings.htm#Scheduli).

   For information about minimum scheduling intervals according to data source type and subscription tier, see [*Minimum allowed scheduling intervals*](../../Admin/subscription-options-QTC.htm#Minimum).
9. Preview the data tasks that are created to onboard data, and rename them if you prefer.

   Tip noteThe names are used when naming database schemas in the storage data task. Consider using names that are unique to avoid conflicts with data tasks in other projects using the same data platform.
10. Select if you want to open any of the data tasks that are created, or return to the project.

    When you are ready, click Finish.

The onboarding data tasks are now created. To start replicating data you need to:

- Prepare and run the landing data task.

  For more information, see [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm).
- Prepare and run the storage data task.

  For more information, see [*Storing datasets*](../Storage/generating-datasets.htm)

### Selecting data

You can select specific tables or views, or use selection rules to include or exclude groups of tables.

Information noteIf the selection includes views, CDC is not supported.

Use % as a wildcard to define a selection criteria for schemas and tables.

- %.% defines all tables in all schemas.
- Public.% defines all tables in the schema Public.

Selection criteria gives you a preview based on your selections.

You can now either:

- Create a rule to include or exclude a group of tables based on the selection criteria.

  Click Add rule from selection criteria to create a rule, and select either Include or Exclude.

  You can see the rule under Selection rules.
- Select one or more datasets, and click Add selected datasets.

  You can see the added datasets under Explicitly selected datasets.

Selection rules only apply to the current set of tables and views, not to tables and views that are added in the future.

Related learning:

- [Using Qlik Cloud Data Integration to onboard and transform data](/lnk/Qlik_cloud_data_integration_onboard_transform)
