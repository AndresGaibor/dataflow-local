---
source: https://qlik.dev/changelog/233-declarative-pipelines/
last_updated: 2026-07-07T08:37:34+02:00
---

# Declarative Pipelines for Qlik Talend Cloud Pipelines

Declarative Pipelines are now available in Qlik Talend Cloud Pipelines, introducing a new way of designing and
configuring your pipelines programmatically, in YAML format.

[image: Visual Studio Code displaying a declarative pipeline task YAML file, with inline schema documentation listing the allowed task types.]

Published schemas power inline property documentation, auto-complete, and real-time validation, without leaving your
editor.
If you use Visual Studio Code, schemas can be automatically retrieved.

Natively integrated with GitHub, Declarative Pipelines lets teams apply GitOps-style workflows including peer review,
version control, and consistent promotion across environments.

This release also ships with AI capabilities: using Claude Code, GitHub Copilot, or any other agent of your choice, you
can leverage the schemas and bundled instructions to generate schema-valid YAML, accelerating pipeline authoring from
day one.

Alongside the schema, you can validate your YAML project structure using the new
`POST /api/v1/di-projects/utils/actions/validate-project-definitions` API endpoint.
This endpoint operates as a dry-run validation before you import the project into your tenant.

With the new YAML format, a new API endpoint is available for project import. When importing YAML-based ZIP
archives, use `POST /api/v1/di-projects/{projectId}/actions/import-async`.

> **Note:** The legacy JSON format remains supported until the end of June 2027, giving you time to plan and migrate your projects.

For more information, see:

- the [Declarative Pipelines developer documentation](https://qlik.dev/manage/di-projects/declarative-pipelines/)
- the [Declarative Pipelines documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DeclarativePipelines/Declarative-pipelines-overview.htm)
  on Qlik Help
- [Validate project definitions](https://qlik.dev/apis/rest/di-projects/#post-v1-di-projects-utils-actions-validate-project-definitions)
- [Import a project asynchronously](https://qlik.dev/apis/rest/di-projects/#post-v1-di-projects-projectid-actions-import-async)
