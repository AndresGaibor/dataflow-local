---
title: "Retrieving and editing a pipeline configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Retrieving-editing-pipeline-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Declarative pipelines"]
---

# Retrieving and editing a pipeline configuration

You can retrieve YAML configuration files for a pipeline by exporting the project, or retrieving it from version control. Then you can edit the YAML files in your development environment to make changes.

You have three options when getting started:

- Export a project as YAML

  Exporting a project produces a ZIP file containing the YAML files for all tasks, datasets, and project settings. For more information, see [*Exporting and importing data pipelines*](../Introduction/Data-project-export-import.htm).

  Tip noteExport in Minimized format first. The minimized files show only what differs from defaults, making them easier to read and easier to replicate across projects. When you import a minimized file, Qlik Talend Data Integration applies the specified values and uses defaults for everything else. If you need to see the full list of available properties and their defaults, export the same project in Full format for reference.
- Import a project from version control

  For more information, see [*Importing a project from version control*](../VersionControl/Project-version-control.htm#Importin).
- You can also create a pipeline configuration from scratch by writing YAML files that match the required folder structure, but we recommend that you start from an existing template.

## Migrating a project to YAML format

Projects that were created before declarative pipeline management was introduced are stored in version control using legacy JSON files.

Information noteThe legacy JSON format remains supported until end of June 2027, giving you time to plan and migrate your projects smoothly.

You can migrate these projects to the YAML-based structure to take advantage of minimized files and the declarative pipeline workflow.

Information noteThis action is only available for projects stored in the legacy JSON format. Projects already using YAML files do not show this option.

To migrate a project to YAML format:

1. Open the project and open the version control menu.
2. Click Migrate to YAML format.
3. Review the confirmation message and click Migrate.

   Information noteThe migration process commits and pushes the current project state as JSON, then converts the files to the new YAML structure and commits again. Because the folder structure and file names change during conversion, the version history before the migration may not be directly comparable to history after the migration.

After the migration completes, the project is stored in YAML format on the current branch. Other branches that still contain JSON files will show the migration option the next time you switch to them.

Tip noteMigrate all environment branches in sequence — starting with development — to maintain a consistent structure across branches before you open pull requests between them.

## Understanding the file structure

The extracted folder contains the following files. File contents are the same across all type of tasks.

qtcp\_project.yaml
qtcp\_tasks/
<task-name>/
task.yaml
sourceSelection.yaml
schedule.yaml (only if a schedule is configured)
model.yaml (only if relationships are defined)
transformationRules.yaml (only if task-level rules are defined)
datasets/
<dataset-name>.yaml
newTaskDefaults.yaml (only if custom task defaults are defined)

### qtcp\_project.yaml

qtcp\_project.yaml contains project-level definitions, and contains properties such as name, platform, and default schema handling.

### task.yaml

task.yaml contains task-level definitions, and contains properties such as task name, type, connections, and full load and change capture behavior.

### sourceSelection.yaml

sourceSelection.yaml defines the source tables selected for the task. Each entry specifies the schema and table selection pattern.

Source selection differs between Landing, and other task types.

### Dataset files

Each dataset has one YAML file named after the dataset, located directly in the datasets/ folder. The file combines the dataset definition and explicit transformation rules.

Information noteThe dataset file is required for all tasks except landing tasks, and must contain the dataset ID if you want to refer to the dataset from other tasks.

### schedule.yaml

schedule.yaml defines when the task runs. The file contains a scheduling array with the schedule configuration. This file is only included if a schedule is set for the project.

### model.yaml

model.yaml defines the data model relationships for the task. The file contains a relationships array.

### transformationRules.yaml

transformationRules.yaml contains all task-level transformation rules in an array.

## Editing configuration files

Open the extracted folder in your IDE and edit the YAML files as needed. Common edits include:

- Changing connection names to point to a different environment.
- Adding or removing source tables in sourceSelection.yaml.
- Updating task settings such as load type or schema handling.
- Adding transformation rules to a dataset file.
- Adding a schedule to a task.

Warning noteReference connection names exactly as they are defined in the target space. A connection name that does not match will cause an import error.

## Object IDs in YAML files

For referenced objects — such as a task ID referenced in another task's source definition — you must define a unique ID and use it consistently across files.

## Related topics

- [*Validating a pipeline configuration*](Validating-pipeline-configuration.htm)
- [*Deploying a pipeline configuration*](Deploying-pipeline-configuration.htm)
