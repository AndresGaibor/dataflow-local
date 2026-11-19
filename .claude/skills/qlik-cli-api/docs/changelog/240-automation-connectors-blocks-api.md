---
source: https://qlik.dev/changelog/240-automation-connectors-blocks-api/
last_updated: 2026-07-23T17:56:15+02:00
---

# New Automation Connectors API endpoint for connector details

The [Automation Connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors/) adds a new endpoint
that retrieves complete connector details, including all visible connector blocks and their metadata.

Use this endpoint to fetch connector information and available connector blocks (names, GUIDs,
descriptions, inputs) programmatically, rather than consulting documentation or the UI.

The new endpoint is:

- `GET /workflows/automation-connectors/{connectorId}`: Returns connector details including a
  list of visible connector blocks with their names, GUIDs, descriptions, inputs, snippet
  availability, and example output payloads for each block.

By default, the response includes only visible blocks. The system excludes hidden blocks
(such as deprecated blocks, lookup blocks, and OAuth configuration blocks).

For more information, see the reference documentation for the
[Automation Connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors/).
