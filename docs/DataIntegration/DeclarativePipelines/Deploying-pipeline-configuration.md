---
title: "Deploying a pipeline configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Deploying-pipeline-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Declarative pipelines"]
---

# Deploying a pipeline configuration

You deploy a pipeline configuration by importing a ZIP file containing the YAML configuration files. You can use the UI or the Import API to create new projects or update existing ones. Both accept minimized YAML and the legacy JSON format.

When using version control, you can commit your changes and perform Apply from remote to get them into Qlik Talend Data Integration.

## Before you begin

Before importing:

- Verify that all connections referenced in the YAML files exist in the target space. Connection names in the YAML file must match exactly.
- If the pipeline includes cross-project references, for example, a pipeline task that reads from a landing task in another project, import the upstream project first.
- Validate the configuration files to confirm there are no errors. See [*Validating a pipeline configuration*](Validating-pipeline-configuration.htm).

## Importing from the UI

### Creating a new project

To create a new project from a configuration file:

1. In Data Integration > Pipeline projects, click Create new.
2. Select Import project.
3. Select the target space.
4. Upload the ZIP file containing the configuration.
5. Click Import.

If the import succeeds, the project opens. If there are errors, a list of validation messages is displayed. Correct the errors in your configuration files and try again.

### Updating an existing project

To update an existing project with a new configuration:

1. In Data Integration > Pipeline projects, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the project and select Import.
2. Upload the ZIP file containing the updated configuration.
3. Click Import.

Information noteImporting a configuration overwrites the current project settings with the values in the YAML files. Settings not present in the imported files are left unchanged if you exported in minimized format, or reset to defaults if you exported in full format.

## Importing using the API

The Import API accepts a ZIP file and the target space ID. It returns the updated project on success, or a list of errors if validation fails.

The Import API supports both YAML (minimized or full) and legacy JSON exports. You do not need to convert existing JSON exports before importing.

Tip noteUse the Validate-project-definitions API before the Import API in CI/CD pipelines to separate validation failures from deployment failures. See [*Validating a pipeline configuration*](Validating-pipeline-configuration.htm).

## Applying changes from version control

If the project is connected to a version control repository, you can apply remote changes directly from the project. When you apply changes, Qlik Talend Data Integration reads the current YAML files from the connected branch and imports them.

Validation runs before changes are applied. If there are errors, you receive the same error messages as a manual import.

For details on setting up version control, see [*Manage your pipeline projects with version control*](../VersionControl/Project-version-control.htm).

## Handling import errors

When import fails, Qlik Talend Data Integration returns a list of validation errors. Each error includes the error type and the path to the file or property where the issue was found.

Up to 50 errors are returned per import attempt. Fix the reported errors and re-import to check for additional issues.

For a description of each error type and how to resolve it, see [*Validating a pipeline configuration*](Validating-pipeline-configuration.htm).

## Related topics

- [*Validating a pipeline configuration*](Validating-pipeline-configuration.htm)
- [*Retrieving and editing a pipeline configuration*](Retrieving-editing-pipeline-configuration.htm)
- [*Exporting and importing data pipelines*](../Introduction/Data-project-export-import.htm)
