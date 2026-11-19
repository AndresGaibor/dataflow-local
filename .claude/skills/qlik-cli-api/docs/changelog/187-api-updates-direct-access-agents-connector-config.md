---
source: https://qlik.dev/changelog/187-api-updates-direct-access-agents-connector-config/
last_updated: 2025-12-09T12:44:50Z
---

# Updated API - Direct Access Agents API configuration endpoints

The [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) has been updated with endpoints that provide
structured JSON-based configuration management for connector types and metrics collection. With these endpoints, you can
now configure File Connector allowed paths, Generic ODBC custom data type mappings, and  metrics collector settings
directly using the API.

The metrics collector logs and monitors resource utilization by Direct Access Gateway,
connectors, and the operating system, helping you plan and optimize data reloads.

Only users with the `TenantAdmin` (Tenant Admin) role can use these endpoints.

### Connector configuration endpoints

The following endpoints give you control over connector configuration:

- `GET /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths` - Retrieve the File
  Connector's allowed paths configuration.
- `PUT /api/v1/direct-access-agents/{agentId}/connectors/file-connector/files/allowed-paths` - Replace the contents of
  the allowed paths configuration file for the File Connector (full replacement only; partial updates are not
  supported).
- `GET /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings` - Retrieve
  the Generic ODBC Connector's custom data type mappings.
- `PUT /api/v1/direct-access-agents/{agentId}/connectors/odbc-connector/files/custom-data-type-mappings` - Replace the
  contents of the custom data type mapping configuration file for the Generic ODBC Connector (full replacement only;
  use API property names).

These endpoints are supported from Direct Access Gateway 1.7.5+ (ODBC mappings) and 1.7.6+ (File Connector allowed
paths).

### Metrics collector configuration endpoints

The following new endpoints give you control over metrics collector configuration:

- `GET /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration` - Retrieve the current metrics
  collector configuration for a Direct Access agent.
- `PUT /api/v1/direct-access-agents/{agentId}/tools/metrics-collector/configuration` - Configure metrics collection
  settings for a Direct Access agent (full replacement only; partial updates are not supported).

These endpoints are supported from Direct Access Gateway 1.7.9+.

For more information, refer to the [Direct Access Agents API reference documentation](https://qlik.dev/apis/rest/direct-access-agents/).
