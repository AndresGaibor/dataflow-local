---
title: "Exporting and importing data pipelines"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Data-project-export-import.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects"]
---

# Exporting and importing data pipelines

You can export a data pipeline project to a file that contains everything required to reconstruct the data project. The export file can be imported to the same tenant, or to another tenant. You can use this, for example, to move projects from one tenant to another, or to make backup copies of projects. You can also update a project from an export file.

Information note

The export file format has been changed from a ZIP file containing several JSON files to a ZIP file containing several YAML files.

The JSON Zip archive will be supported for a transition period as Legacy until <date, 2027>.

Export your existing projects with the Minimal or All options to enjoy the new format.

## Exporting a data project

You need at least one of the following roles in the space where the project resides to export a project:

- Can edit
- Can view
- Can operate

To export a project:

1. In Data Integration > Pipeline projects, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the project and select Export.

   You can also open the project, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the top right, and select Export.
2. Select the export format:

   - Minimized (default) — exports only required and modified settings. Recommended for version control and code-first workflows.
   - Full — exports all settings including defaults. Use this to see the complete configuration or when troubleshooting.
   - Legacy — exports in the older JSON format. Use this only for integration with systems that cannot consume YAML.

The project is exported to a ZIP file with a file name that consists of the project name, the data platform, and a timestamp.

Warning noteDo not edit a legacy JSON export. Editing the JSON files directly can result in a project that cannot be imported. If you want to edit your pipeline configuration, export the project in Minimized or Full YAML format instead. For more information, see [*Retrieving and editing a pipeline configuration*](../DeclarativePipelines/Retrieving-editing-pipeline-configuration.htm).

## Importing projects

This section covers importing projects. You can import a cloud data warehouse project or a Qlik Cloud (via Amazon S3) project.

Tip noteIf you are using version control, you can import projects from version control. For more information, see [*Importing a project from version control*](../VersionControl/Project-version-control.htm#Importin) .

You can change which data platform to use with the following limitations:

- It is not possible to change data platform from a cloud data warehouse to Qlik Cloud, or the other way around.
- It is not possible to change a Snowflake project using landing to cloud file storage to another data platform, or the other way around.

### Before importing a project

Before you start importing a project consider:

- Create all new connections that you will need if you are importing to a new tenant or space.
- If the project uses SaaS application connections that do not exist yet, you must create the connections and generate metadata before you start importing.
- If you are importing a cross-project pipeline, you must import the upstream projects first.

### Importing a cloud data warehouse project

Information noteThis section covers importing a project with a cloud data warehouse as data platform. For information about importing a project with Qlik Cloud (via Amazon S3) as data platform, see [*Importing a project with Qlik Cloud as data platform*](#Importin).

You can import an exported cloud data warehouse project to the same tenant it was exported from, or to another tenant. When the project is imported into a tenant other than the original data project's tenant, you need to define new connections for the project, the staging area and for all data sources.

If the project consumes tasks from other projects, you must map projects and tasks unless names for spaces and projects are identical.

1. In Data Integration > Pipeline projects, click Create new and select Import project.
2. Add the export file. You can either drop it on the dialog, or browse to select the file.

   Click Next.
3. Set Project properties for the new project.

   You must select which space to add the project to in Space.

   In Data platform you can change the data platform of the project, and the connection to the data platform.

   Changing Connection is required if you imported a project from another tenant, or if you changed the data platform in the previous step.

   You can change the connection to the staging area. This is required if you imported a project from another tenant, or in some cases if you changed the data platform in the previous step.

   Click Next.
4. Set Default project settings for the new project.

   You can add a prefix to the data schemas that are created in the project in Prefix for all schemas. This is useful when the imported project is in the same cloud data warehouse as the exported project.

   You can also set a default name in Database name. For Snowflake projects you can set a default Data warehouse name, and for Databricks projects you can set a default Catalog name. You can use the project default name for all task types, or set the name to default or a custom name for each task type.

   Click Next.
5. Set Connections and task settings.

   You can replace the imported source connections or cross-project sources with a connection that uses the same connector. For example, if the imported source connection is MySQL, then the replacement connection must also be MySQL. This is required if you imported a project from another tenant.

   In Task settings (Optional) you can also change task settings that you want to override in the original project.
6. When you are ready, click Import.

The project is added to Data Integration home.

### Importing a project with Qlik Cloud as data platform

You can import an exported Qlik Cloud (via Amazon S3) project to the same tenant it was exported from, or to another tenant. When the project is imported into a tenant other than the original data project's tenant, you need to define new connections for the project, the staging area and for all data sources.

It is not possible to change data platform from Qlik Cloud to a cloud data warehouse, such as Snowflake.

1. In Data Integration > Pipeline projects, click Create new and select Import project.
2. Add the export file. You can either drop it on the dialog, or browse to select the file.

   Click Next.
3. Name

   Change the name of the project. The default name is the original project name prefixed with Imported\_.
4. Space

   Select which space to add the project to.
5. Description

   Add or edit the description of the project.
6. Store QVD files in:

   Select where to generate QVD files.

   - Qlik managed storage
   - Customer managed storage

     Amazon S3 storage managed by you.
7. Data connection

   If you selected Customer managed storage, you can change the connection to the Amazon S3 storage area.

   This is required if you imported a project from another tenant.
8. Connection to staging area

   You can change the connection to the Amazon S3 staging area.

   This is required if you imported a project from another tenant, or in some cases if you changed the data platform in the previous step.
9. Click Next.
10. Set connections for the tasks added in the original version

    You can replace the imported source connections with a connection that uses the same connector. For example, if the imported source connection is MySQL, then the replacement connection must also be MySQL.

    This is required if you imported a project from another tenant.
11. In Task settings (Optional) you can change task settings that you want to override in the original project.
12. When you are ready, click Import.

The project is added to Data Integration home.

## Updating a project

You can update a project from an export file. This will replace all tasks in the data pipeline, but connections and settings will not be replaced. Data tasks that are not included in the imported project will be removed.

For example, you can import a project exported from the development data space into a project in the production data space to update the production project.

Before you start updating the project:

- If you want a backup of the project before you update, export it by clicking ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then Export.
- You must stop all tasks that will be removed from the data pipeline before you update the project.
- If the project uses SaaS application connections that do not exist yet, you must create the connections and generate metadata before you start importing.
- Make sure that the imported project uses the same cloud data platform, for example, Snowflake.

To update a project:

1. Open the project that you want to update.
2. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Import.
3. Select or drop the file that you want to import.
4. Make any required changes for mapping connections that are different between the project and the imported project.

   For example, the imported project could be using a source connection named SQL1, while this project uses a similar connection named SQL2. In this case, map the imported connection to SQL2 in Set connections for the tasks added in the original version.

   Information noteWhen selecting a connection to map, you can create a new database connection, but not a SaaS application connection.

   Click Import when you are ready.

The project is now updated according to the imported file. You may need to validate and sync data tasks that have been updated through the import.

## Best practices

Here are some general best practices when importing and exporting projects.

- Avoid adding the same dataset to two projects and importing one project to the other project. This can create conflicts that are hard to resolve and can cause recreation of datasets:

  Information noteWhen a dataset is added to a task, it gets an internal identifier. Internal identifiers are used to allow for seamless renaming and other metadata operations in a pipeline. When creating the same dataset in a separate project or branch, the internal identifier will be different causing conflicts when importing a project to the other project. This may cause the prepare process to drop and recreate a dataset even if it has the same name.

## Limitations

- Notifications are not included when you export a pipeline. You need to set up new notifications in the imported pipeline.
- Saved SQL workbench scripts are not included when you export a project.

  If you import the project as a new project, saved SQL workbench scripts are empty.

  If you import to update an existing project, existing saved SQL workbench scripts are not changed.
- The zip file for import must have the project files directly in it and not in a nested sub-folder.

  When creating a zip file in mac OS, if you click on a folder and chose to zip it, the zip file will include a nested sub-folder containing the files, which means the zip file cannot be imported.
- The following scenario can create conflicts that are hard to resolve:

  1. Make changes to the same dataset in two projects.
  2. Export project 1.
  3. Import project 1 into project 2.
- Do not design pipelines that create loops or mutual dependencies between projects. Exporting and importing such projects is not supported.
- When importing an older project (before JSON support was introduced) with Registered data and Storage tasks, JSON fields on the source were mapped to BLOB. The native type was still kept on Registered data, for example Variant on Snowflake. When importing after JSON support was added, the logical type may change to JSON.
- Knowledge mart tasks can be exported and imported only between projects that use the same data platform type. Exporting a project with knowledge mart tasks from Snowflake and importing it into Databricks, or exporting from Databricks and importing into Snowflake, is not supported.
