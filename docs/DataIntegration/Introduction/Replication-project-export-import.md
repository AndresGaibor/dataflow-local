---
title: "Exporting and importing replication projects"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Replication-project-export-import.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project"]
---

# Exporting and importing replication projects

You can export a data replication project to a file that contains everything required to reconstruct the data replication project. The export file can be imported to the same tenant, or to another tenant. You can use this, for example, to move projects from one tenant to another, or to make backup copies of projects. You can also update a project from an updated export file.

Information note

The export file format has been changed from a ZIP file containing several JSON files to a ZIP file containing several YAML files.

The JSON Zip archive will be supported for a transition period as Legacy until <date, 2027>.

Export your existing projects with the Minimal or All options to enjoy the new format.

## Exporting a data project

You need at least one of the following roles in the space where the project resides to export a project:

- Can edit
- Can view
- Can operate

To export a project, do one of the following:

- In Data Integration > Projects, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the project to export, and select Export.
- Open the project, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the top right, and select Export.

The project is exported to a ZIP file with a file name that consists of the project name, the data platform, and a timestamp.

Warning noteDo not edit the exported file. Doing so might result in a project file that cannot be imported.

## Importing a replication project

You can import an exported replication project to the same tenant it was exported from, or to another tenant. When the replication project is imported to a different tenant, you need to define new connections for all data sources and targets.

To import a project:

1. In Data Integration > Pipeline projects, click Create new and select Import project.
2. Add the export file. You can either drop it on the dialog, or browse to select the file.

   Click Next.
3. Set Project properties for the new project.

   You must select which space to add the project to in Space.

   Click Next.
4. Set Connections and task settings.

   You can replace the imported source and target connections, but the replacement connection must use the same connector. For example, if the imported source connection is MySQL, then the replacement connection must also be MySQL. Replacing the connections is required if you imported a project from another tenant.

   In Task settings (Optional) you can change task settings that you want to override in the original version.
5. When you are ready, click Import.

The project is added to Data Integration home.

## Updating an existing project

You can update a project from an export file. This will replace all tasks in the project, but connections and task settings will not be replaced. Tasks that are not included in the imported project will be removed.

For example, you can import a project exported from the development data space into a project in the production data space to update the production project.

Before you start updating the project:

- To backup the project before you update, export it by clicking ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then Export.
- Stop any tasks that will be removed from the project.
- If the project uses SaaS application connections that do not exist yet, you must create the connections and generate metadata before you start the import.

To update a project:

1. Open the project that you want to update.
2. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Import.
3. Select or drop the file that you want to import.
4. Make any required changes for mapping connections that are different between the project and the imported project.

   For example, the imported project could be using a source connection named SQL1, while the existing project uses a similar connection named SQL2. In this case, map the imported connection to SQL2 in Set connections for the tasks added in the original version.

   Information noteWhen selecting a connection to map, you can create a new database connection, but not a SaaS application connection.
5. Click Import when you are ready.

The project is now updated according to the imported file.

## Limitations

- Notifications are not included when you export a pipeline. You need to set up new notifications in the imported pipeline.
- The zip file for import must have the project files directly in it and not in a nested sub-folder.

  When creating a zip file in mac OS, if you click on a folder and chose to zip it, the zip file will include a nested sub-folder containing the files, which means the zip file cannot be imported.
