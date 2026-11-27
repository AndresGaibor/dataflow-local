---
title: "CDC data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/onboarding-data-cdc.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Onboarding data"]
---

# CDC data

The onboarding process transfers data from a CDC or SaaS source and stores it in Iceberg tables. Changes from the data sources are continuously applied to the storage tables in efficient mini-batches.

## Onboard data

You start onboarding data in a project. Datasets are stored in the S3 location defined in the project. For more information about projects, see [*Creating and managing data pipeline projects*](../Introduction/Data-projects.htm).

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

     If your data contains tables that do not support CDC, or views, two data pipelines will be created: one pipeline with all tables supporting CDC, and another pipeline with all other tables and views using Reload and compare.
   - Reload and compare
6. Select if you want to replicate history of previous data in addition to current data in History.
7. Click Next when you are ready.
8. Preview the data tasks that are created to onboard data, and rename them if you prefer.

   Tip noteThe names are used when naming database schemas in the Storage data task. Consider using names that are unique to avoid conflicts with data tasks in other projects using the same data platform.
9. Select if you want to open any of the data tasks that are created, or return to the project.

   When you are ready, click Finish.
10. The onboarding data tasks are now created. To start replicating data you need to:
11. Prepare and run the Landing data task.

    For more information, see [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm).
12. Prepare and run the Storage data task.

    For more information, see [*Storing datasets*](storing-data.htm).

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
