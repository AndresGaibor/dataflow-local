---
source: https://qlik.dev/changelog/116-api-updates-di-projects/
last_updated: 2024-11-28T10:44:20Z
---

# Updated API - The Data Integration Projects API now supports export and import of projects

The [Data Integration Projects API](https://qlik.dev/apis/rest/di-projects/) manages Qlik Talend
Cloud Pipeline projects.

New export/import APIs for Qlik Talend Cloud Pipelines offer a programmatic way
to export and import projects across tenants and spaces for deployment purposes.

They allow programmers to export projects as a .zip file. They also include
creating projects and reading or updating the project variables (referred to as bindings)
before importing project contents.

5 new API endpoints are available:

- Export the project contents as a .zip file
- Retrieve the bindings for a specified project
- Create a project
- Update bindings for a specified project
- Import project contents from a .zip file

For more information, review the [reference documentation for the Data Integration Projects API](https://qlik.dev/apis/rest/di-projects/).
