---
title: "Validating a pipeline configuration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Validating-pipeline-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Declarative pipelines"]
---

# Validating a pipeline configuration

You can validate a pipeline configuration at two stages: in your IDE (Integrated Development Environment), and on the server before you apply changes. Validating early helps you catch errors before they affect a running project.

## Validating in the IDE

Qlik Talend Data Integration provides JSON schema definitions for all YAML configuration files. When you reference these schemas in your IDE, it can flag errors and offer suggestions as you type.

To enable schema validation in VS Code, install the YAML extension for VS Code (published by Red Hat). If you want to use another IDE, you can download schemas from [Qlik - Open Source Software.](https://github.com/qlik-oss)

With schema validation active, VS Code flags syntax errors, unknown properties, and missing required fields in real time.

Tip noteAlways validate your YAML files in the IDE before uploading. Catching errors locally is faster than waiting for server-side validation.

## Validating on the server

Server-side validation checks the logical consistency of the configuration in addition to syntax. This validation runs automatically when you import or apply changes. You can also run it manually using the Validate API before you deploy.

### Using the Validate-project-definitions API

The Validate-project-definitions API performs a dry-run import: it processes your configuration files and returns any validation errors without applying changes to the project. Use this in CI/CD pipelines to verify a configuration before triggering a deployment.

The API accepts a ZIP file in the same format (JSON or YAML) as an import and returns a list of errors. If there are no errors, the configuration is ready to deploy.

Information noteThe Validate-project-definitions API returns up to 50 errors per call. If your configuration has many errors, fix the reported ones and run validation again.

## Understanding validation errors

Validation errors include the type of error and the path to the file or property where it was found. for more information, see [Qlik.dev](http://qlik.dev/).

## Related topics

- [*Retrieving and editing a pipeline configuration*](Retrieving-editing-pipeline-configuration.htm)
- [*Deploying a pipeline configuration*](Deploying-pipeline-configuration.htm)
- [*Getting started with declarative pipelines*](Getting-started-declarative-pipelines.htm)
