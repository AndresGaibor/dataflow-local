---
source: https://qlik.dev/changelog/174-automation-connectors-api/
last_updated: 2025-10-23T10:07:51+02:00
---

# New REST API - Automation Connectors API for connector list access

The new [Automation Connectors API](https://qlik.dev/apis/rest/automation-connectors/) allows you to programmatically discover available
automation connectors and their metadata.

The API provides access to the connector list so you can look up connector IDs needed for programmatic connection
creation with the [Automation Connections API](https://qlik.dev/apis/rest/automation-connections/).
It also enables enrichment of monitoring and telemetry with connector names and metadata.

The new operation is:

- `GET /v1/automation-connectors`: Retrieve a list of automation connectors.

For more information, see the [reference documentation for the Automation Connectors API](https://qlik.dev/apis/rest/automation-connectors/).
