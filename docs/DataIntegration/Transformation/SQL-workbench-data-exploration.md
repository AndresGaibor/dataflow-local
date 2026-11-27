---
title: "Exploring data with SQL Workbench"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/SQL-workbench-data-exploration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Exploring data with SQL Workbench

Use SQL Workbench to troubleshoot data and to develop SQL queries. You can explore data and validate SQL across prepared tasks and data warehouse layers in a project context.

SQL Workbench is available for data pipeline projects that use a data warehouse. You run queries in the data warehouse connected to the project.

Information noteReplication projects, data pipeline projects with Qlik Cloud as target, and Qlik Open Lakehouse projects are not supported. In supported projects you can view and add mirror tasks in upstream Qlik Open Lakehouse projects.

## Limitations

- Only read-only SQL queries are supported. Data modification statements are blocked.
- Lake landing and knowledge marts are not supported in the object browser.
- Macros are not supported. If a transformation includes macros, the full load transformation is shown in Source query.

## Required permissions

- To run queries, you must have Can view data in the space where the project connection resides.
- To save, edit, rename, or delete SQL scripts, you must have Can edit in the project space.

For more information about space roles, see [*Data space roles and permissions*](../DataSpaces/permissions-data-space.htm).

## Opening SQL Workbench

Open SQL Workbench in a data pipeline project. SQL Workbench always runs in the context of the current project.

- Click SQL Workbench in the top menu.

Information noteIf you do not see SQL Workbench, verify project type and permissions.

## Browsing tables

Tables lists tables from prepared tasks in:

- The current project.
- Referenced projects on the same data platform.

Only physical tables on external schemas are shown.

For Qlik Open Lakehouse projects, Tables lists mirror tasks from the current project and referenced projects. SQL Workbench displays only mirror tasks that match the project's lakehouse type: Snowflake, Amazon Redshift, Databricks, or Google BigQuery.

For each table, you can view database, schema, columns, and data types.

Information noteIf a task is not prepared, it will not be displayed in Tables.

- Click Filter by task type to filter the tasks.
- Click Sort and group to arrange tasks and set a sorting order.

### Adding more projects

From the start, you will only see tasks from the current project. You can add more projects to be able to use them in your query.

- Click ![add](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add more projects to be available.

  You can select from projects using the same data warehouse.

  Select the projects and click Apply.

All prepared tasks in the selected projects are now available.

For Qlik Open Lakehouse projects, SQL Workbench displays only mirror tasks that match the project's lakehouse type.

## Creating queries

You can use one or more tabs to write SQL and run selected statements or the current statement.

Each tab runs in its own session, which allows parallel query execution.

When editing the query, you can use the following tools:

- ![Undo](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back.svg) Undo the previous edit
- ![Undo](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward.svg) Redo what was previously undone
- ![Auto format](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_align_left.svg) Auto format the SQL code
- ![Comment](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_comment_outline.svg) Comment/uncomment the current line
- ![Search](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg) Search and replace text in the code

### Adding a SELECT statement for a table

You can add a SELECT statement that returns all fields of a table.

- Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the table in Tables, and click Add SELECT statement.

A SELECT statement returning all fields from the selected table is added to the query editor.

### Adding a query from a transformation dataset

You can add the source query of a dataset created in a Transform task.

- Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the dataset in Tables, and click Add source query.

The query that was used to create the selected dataset is added to the query editor.

## Running queries

You can run the entire query, or a selected statement by clicking Run query.

- If you have not selected anything in the query editor, the entire query is run.
- If you selected a statement in the editor, that statement is run.

When the query is run, you can check the outcome in:

- Results

  Sample data returned by the query.

  Information noteYou must have Can view data role in the connection space. Additionally, Viewing data in Data Integration must be turned on in your tenant.
- Metadata

  Lists columns with information about data types and Nullability.

## Saving and managing SQL scripts

You can save SQL scripts in SQL Workbench for reuse by clicking Save. Scripts are saved in the project and can be viewed by all project users. You can list, open, rename, and delete scripts in  Saved scripts.

Information noteSaved SQL workbench scripts are not included when exporting a project. For more information, see [*Exporting and importing data pipelines*](../Introduction/Data-project-export-import.htm).

- To delete a script, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the script and then Delete.
- To rename a script, click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the script and then Edit.

## Troubleshooting

- If query execution fails with permission errors, verify that you have the required roles in the project space and connection space.
- If objects are missing, verify that source tasks are prepared.
- If a statement is blocked, verify that it is read-only SQL.

For general troubleshooting, see [*Troubleshooting data tasks*](../Deploying/Troubleshooting-data-assets.htm).
