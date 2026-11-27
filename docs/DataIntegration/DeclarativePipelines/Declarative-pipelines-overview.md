---
title: "Declarative pipelines"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Declarative-pipelines-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project"]
---

# Declarative pipelines

Declarative pipelines let you define, configure, and deploy Qlik Talend Data Integration pipeline projects entirely in code using YAML files. You edit the files in any integrated development environment or version control system, then deploy them to create or update projects.

## When to use declarative pipelines

Use declarative pipelines to promote:

- Collaboration
- Continuous Integration / Continuous Delivery
- Repeatable deployment to different environments
- API-driven automation

Here are some typical use cases:

- Define pipelines in code for continuous integration and development automation.
- Deploy identical pipeline configurations across multiple environments (development, verification, production).
- Reuse and share pipeline definitions across projects or teams.
- Automate large-scale project creation without manual work.

## How it works

A pipeline project is represented as a set of YAML files organized in a folder structure that mirrors the project's tasks and datasets. YAML files are easier to read, see diffs, review, reuse, and create automation.

You can export an existing project as YAML, edit the files, and import them back to apply your changes. If the project is connected to version control, the YAML files are directly available in your GitHub repository.

For more information about the YAML file structure, see [*Retrieving and editing a pipeline configuration*](Retrieving-editing-pipeline-configuration.htm).

Information noteBinding files (qtcp\_bindings\_definition.json and binding.json) remain in JSON format for compatibility with the bindings API. For Legacy export or in existing GitHub projects, the file is called bindingTemplate.json and not qtcp\_bindings\_definition.json.

## Typical workflow

Before you start, you must set up your development environment and version control. For more information, see [*Getting started with declarative pipelines*](Getting-started-declarative-pipelines.htm).

A typical declarative pipeline workflow looks like this:

1. Retrieve the pipeline configuration

   You can export an existing project as YAML, retrieve it from version control, or start from a template.

   [*Retrieving and editing a pipeline configuration*](Retrieving-editing-pipeline-configuration.htm)
2. Edit the pipeline configuration

   Modify the YAML files in your development environment. You can add tasks, change source selections, and update settings.

   [Developer guide: Declarative pipelines](https://qlik.dev/manage/di-projects/declarative-pipelines/)
3. Validate the pipeline configuration

   Check the files for syntax and semantic errors before deploying the pipeline.

   [*Validating a pipeline configuration*](Validating-pipeline-configuration.htm)
4. Deploy the pipeline configuration

   Import the files to create or update the project in Qlik Talend Data Integration.

   You can also commit the files to version control and perform apply from version control in the project in Qlik Talend Data Integration.

   [*Deploying a pipeline configuration*](Deploying-pipeline-configuration.htm)

## Relationship to version control

When a project is connected to version control, the YAML files are stored directly in your GitHub repository. You can edit the YAML files in GitHub or in any IDE, and then apply the changes back to the project.

For information about connecting a project to version control, see [*Manage your pipeline projects with version control*](../VersionControl/Project-version-control.htm).

Information noteIf you have an existing project that is connected to version control and uses the legacy JSON format, you can migrate it to YAML. For more information, see [*Migrating a project to YAML format*](Retrieving-editing-pipeline-configuration.htm#Migrate).

## Using AI assistants to configure pipelines

Use AI assistants (such as GitHub Copilot or Anthropic Claude) to streamline YAML configuration creation and editing. To ensure accuracy and adherence to project standards, follow these best practices:

1. **Select a high-capability model**: Use a premium, large-context model (for example, Anthropic Claude Sonnet 5.5 or higher) rather than a standard or "auto" model for complex YAML generation and schema adherence. Advanced models correctly interpret complex pipeline schemas and produce more accurate configurations.
2. **Install the declarative pipelines skills**: Install the declarative pipelines skills in your AI coding assistant of choice: Claude Code, GitHub Copilot, or Kiro.

   - **Claude Code**

     You can install the skills from the VS Code plugins screen or from a terminal.

     Option 1: VS Code plugins screen

     1. In the Claude prompt box, type `/plugins` and select Manage plugins.
     2. On the Marketplaces tab, enter qlik-oss/agentic-skills in the GitHub repo box and click Add.
     3. On the Plugins tab, search for qlik-data-pipelines-skills, click Install, and select a scope.

     Option 2: Terminal

     Open a terminal, either in VS Code or separately, and run the following commands:

     ```
     claude plugin marketplace add qlik-oss/agentic-skills
     claude plugin install qlik-data-pipelines-skills@qlik-cloud-skills
     ```

     Alternatively, run `claude` to start an interactive session, and then enter the following commands:

     ```
     /plugin marketplace add qlik-oss/agentic-skills
     /plugin install qlik-data-pipelines-skills@qlik-cloud-skills
     ```

     When prompted, select a scope.
   - **GitHub Copilot**

     You can install the skills from the GitHub Copilot prompt box or from a terminal.

     Option 1: Copilot prompt box

     In the GitHub Copilot prompt box, enter the following commands:

     ```
     /plugin marketplace add qlik-oss/agentic-skills
     /plugin install qlik-data-pipelines-skills@qlik-cloud-skills
     ```

     Option 2: Terminal

     Open a terminal, either in VS Code or separately, and run the following commands:

     ```
     copilot plugin marketplace add qlik-oss/agentic-skills
     copilot plugin install qlik-data-pipelines-skills@qlik-cloud-skills
     ```

     Alternatively, run `copilot` to start an interactive session, and then enter the following commands:

     ```
     /plugin marketplace add qlik-oss/agentic-skills
     /plugin install qlik-data-pipelines-skills@qlik-cloud-skills
     ```

     When prompted, select a scope.
   - **Kiro**

     - Install the Qlik Declarative Pipelines power from the [Kiro Powers catalog](https://kiro.dev/powers/). For installation instructions, see [Installing powers](https://kiro.dev/docs/powers/installation/) in the Kiro documentation.

## Using AI assistants with Qlik MCP tools

When you deploy a Qlik MCP server in your tenant, AI assistants can use dedicated MCP tools to help manage pipeline projects programmatically.

### Prerequisites

- Qlik MCP server is deployed in your tenant
- You have the Qlik MCP: Allowed permission assigned through a custom role
- You have permissions to create or edit pipeline projects
- An AI client with MCP support (such as VS Code with GitHub Copilot) is configured to use the Qlik MCP server

### Available MCP capabilities for data pipelines

AI assistants can use the following capabilities to configure and manage pipeline projects:

- **Search for spaces**: Get a list of available spaces.
- **Search for connections**: Get a list of available data connections.
- **Search for projects**: Get a list of existing pipeline projects.
- **Search for connection objects**: Discover available tables and views from a data source.
- **Get pipeline project details**: Retrieve project binding values.

### Related resources

- To deploy the MCP server, see [Qlik MCP server](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server.htm)
- For detailed MCP tool documentation, see [Qlik MCP tools](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server-tools.htm)
- For permission requirements, see [Qlik MCP server access and permissions](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-Permissions.htm)
