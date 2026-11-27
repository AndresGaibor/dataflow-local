---
title: "Creating a Direct Query application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DirectQuery/create-direct-query-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Accessing cloud databases directly with Direct Query"]
---

# Creating a Direct Query application

When you create a new Qlik Sense analytics application, you have the option of creating it with a Direct Query [connection](#glossary-1 "Glossary term") instead of loading the data in-memory.

## Connecting to a database

The first step to getting started with Direct Query is to connect to a database.

Information noteFor a list of supported data sources, see [*Data sources in Qlik Cloud Analytics*](../../Sense_Helpsites/Connectors_SaaS.htm).

Do the following:

1. Create a new Qlik Sense analytics application.

   [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm)
2. Select an existing data connection or add a new data connection.

   Best practice is to use user defined credentials, for example with OAuth in Snowflake.

   [*Adding data to the application from connections and new files*](../LoadData/adding-data.htm)

   Information noteFor a list of supported data connection types, see [*Accessing cloud databases directly with Direct Query*](direct-access-with-direct-query.htm).
3. Click the menu.
4. Select Go to Direct Query.

## Selecting data source and tables

To perform analysis on your data, select the tables and columns to include.

Do the following:

1. In the Direct Query application you just created, select an Owner.
2. Select the table or tables that you want to analyze.
3. Click Next.

The Data model manager then opens.

## Creating relationships between tables to build data model in Data model manager

If you have included more than one table in your analysis, it is necessary to create relationships between tables and fields.

Information noteFor a full list of supported relationship types, see [*Accessing cloud databases directly with Direct Query*](direct-access-with-direct-query.htm).

Do the following:

1. In the Data model manager, click Relationship.
2. Select the tables and fields to relate.

   For more information, see [*Joining tables in Data manager*](../LoadData/join-keep-tables-in-data-manager.htm).

   Information noteYou can only select two tables at a time. To create more relationships, repeat the full procedure.

   Information noteCircular relationships are not supported.
3. When you have created relationships between all relevant fields and tables, click Apply changes.

All relationships appear on the home screen of the Data model manager. You can sort the relationships by which table they are based by clicking the corresponding table in the list.

Tip noteWhen creating a data model in Direct Query, keep the model as simple as possible, Complex queries are more likely to cause performance issues.

Tip noteWhen working with Direct Query, it is recommended that you create a template Direct Query application. This way, you can save time by duplicating the template application with the pre-defined model when creating a new Direct Query application.

## Adding visualizations

For instructions on how to add visualizations, see [*Creating visualizations*](../Visualizations/create-visualizations.htm).

Information noteNot all visualization types are supported in Direct Query applications, and some have different limitations compared to in-memory applications. For a complete list of supported charts and functions, see [*Accessing cloud databases directly with Direct Query*](direct-access-with-direct-query.htm).

You can use functions from the cloud database in [measure](#glossary-2 "Glossary term") expressions, but not in calculated [dimensions](#glossary-3 "Glossary term").

## Sharing Direct Query applications

Access to Direct Query applications is slightly different to in-memory applications as user access is normally controlled by the database with user defined credentials.

- The application and the data connection must be in a [shared space](#glossary-4 "Glossary term").
- Users must have a Can consume data role in the shared space and access to the database.
