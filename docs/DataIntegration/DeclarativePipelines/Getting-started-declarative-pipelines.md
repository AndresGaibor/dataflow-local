---
title: "Getting started with declarative pipelines"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Getting-started-declarative-pipelines.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Declarative pipelines"]
---

# Getting started with declarative pipelines

Before you can define and deploy pipelines in code, you need the right permissions, a compatible integrated development environment, and optionally a GitHub connection for version control integration.

## Prerequisites

- You must have the Can edit role in the space where the project resides to export, import, and deploy pipeline configurations.
- Connections (source and target) must exist in the target space before you import a pipeline configuration. You reference connections by name in the YAML files.

## Setting up your integrated development environment

You can edit pipeline YAML files in any text editor. For syntax highlighting, auto-completion, and real-time schema validation, you can use Visual Studio Code with the YAML extension.

To set up VS Code for declarative pipeline development:

1. Install [Visual Studio Code](https://code.visualstudio.com/).
2. Install the [YAML extension by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) from the VS Code Extensions Marketplace.

VS Code will highlight errors in your YAML files as you type, before you deploy to Qlik Talend Data Integration.

Tip noteIf you want to use another integrated development environment, you can download schemas from [Qlik - Open Source Software.](https://github.com/qlik-oss/schemas)

## Setting up version control (optional)

If you want to manage pipeline configurations in GitHub, connect your project to version control. This lets you commit YAML files directly from the project, apply changes from the repository, and promote configurations across environments using branches and pull requests.

For setup instructions, see [*Getting started*](../VersionControl/Project-version-control.htm#Getting) in [*Manage your pipeline projects with version control*](../VersionControl/Project-version-control.htm).

Information noteIf you have an existing project that is connected to version control and uses the legacy JSON format, you can migrate it to YAML. For more information, see [*Migrating a project to YAML format*](Retrieving-editing-pipeline-configuration.htm#Migrate).
