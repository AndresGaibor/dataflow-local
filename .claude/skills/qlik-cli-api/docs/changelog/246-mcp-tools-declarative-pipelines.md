---
source: https://qlik.dev/changelog/246-mcp-tools-declarative-pipelines/
last_updated: 2026-09-07T10:22:18+02:00
---

# MCP tools for declarative pipelines

The Qlik MCP server now includes three additional tools purpose-built for declarative pipeline development:
`qlik_search`, `qlik_get_pipeline_project_details`, and `qlik_search_connection_objects`.

These tools let coding agents such as Claude Code or GitHub Copilot query a live Qlik tenant directly from the
editor:

- `qlik_search` has been extended to return pipeline projects and pipeline connections in addition to existing
  catalog resources.
- `qlik_get_pipeline_project_details` returns a project's binding values.
- `qlik_search_connection_objects` lists the source tables and views available in a given data connection.

With these tools, coding agents can introspect a live Qlik tenant's connection names, table structures, and project
bindings, reducing the risk of pipelines failing on import due to incorrect assumptions.

For more information, see the
[Declarative pipelines documentation](https://qlik.dev/manage/di-projects/declarative-pipelines/setup-vs-code/) and
[Qlik MCP tools documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Qlik-MCP-server-tools.htm)
on Qlik Help.
