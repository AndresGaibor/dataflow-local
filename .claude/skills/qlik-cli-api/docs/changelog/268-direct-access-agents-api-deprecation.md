---
source: https://qlik.dev/changelog/268-direct-access-agents-api-deprecation/
last_updated: 2026-11-12T18:51:23+01:00
---

# Direct Access Agents API deprecated in favor of Connectivity Direct Access Agents API

> **Deprecation notice:** The [Direct Access Agents API](https://qlik.dev/apis/rest/direct-access-agents/) under `/api/v1/direct-access-agents` is deprecated
> and will be removed on or after November 1, 2027.
>
> Migrate to the [Connectivity Direct Access Agents API](https://qlik.dev/apis/rest/connectivity/direct-access-agents/) under
> `/api/connectivity/direct-access-agents`.

The Direct Access Agents API is now available in the `connectivity` namespace. Each operation of the v1 API has a
replacement in the namespaced API with the same path after the base path.

To migrate an existing integration:

1. Replace `/api/v1/direct-access-agents` with `/api/connectivity/direct-access-agents` in your API requests.
2. Keep the remaining path, query parameters, and request bodies unchanged.
3. Test your integration in a non-production tenant.
4. Deploy the updated integration and remove any remaining calls to `/api/v1/direct-access-agents`.

The following example shows the same request before and after migration:

```bash
# Deprecated
curl "https://<TENANT>.<REGION>.qlikcloud.com/api/v1/direct-access-agents/<AGENT_ID>/configurations" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"

# Replacement
curl "https://<TENANT>.<REGION>.qlikcloud.com/api/connectivity/direct-access-agents/<AGENT_ID>/configurations" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

### qlik-cli impact \{#268-qlik-cli-impact}

In qlik-cli 4.0.0, the `qlik direct-access-agent` commands are deprecated and still call the v1 endpoints. Use the
`qlik connectivity direct-access-agent` commands instead, which call `/api/connectivity/direct-access-agents`.
Most commands keep the same subcommand names. These commands differ:

| Deprecated command                                                         | Replacement command                                                                                   |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `qlik direct-access-agent connector file allowed-paths get`                | `qlik connectivity direct-access-agent connector file-connector file allowed-path ls`                 |
| `qlik direct-access-agent connector file allowed-paths update`             | `qlik connectivity direct-access-agent connector file-connector file allowed-path update`             |
| `qlik direct-access-agent connector file allowed-paths edit`               | `qlik connectivity direct-access-agent connector file-connector file allowed-path edit`               |
| `qlik direct-access-agent connector file custom-data-type-mappings get`    | `qlik connectivity direct-access-agent connector odbc-connector file custom-data-type-mapping ls`     |
| `qlik direct-access-agent connector file custom-data-type-mappings update` | `qlik connectivity direct-access-agent connector odbc-connector file custom-data-type-mapping update` |
| `qlik direct-access-agent connector file custom-data-type-mappings edit`   | `qlik connectivity direct-access-agent connector odbc-connector file custom-data-type-mapping edit`   |
| `qlik direct-access-agent tool metrics-collector configuration ls`         | `qlik connectivity direct-access-agent tool metrics-collector configuration <AGENT_ID>`               |
| `qlik direct-access-agent tool metrics-collector configuration update`     | `qlik connectivity direct-access-agent tool metrics-collector configuration update <AGENT_ID>`        |

`qlik direct-access-agent tool metrics-collector configuration edit` has no replacement. To change the settings, use
`qlik connectivity direct-access-agent tool metrics-collector configuration update <AGENT_ID>`, which replaces the full
configuration. Partial updates are not supported.

If you already use `qlik connectivity direct-access-agent benchmark create` or `benchmark ls` from qlik-cli 3.4.0,
pass the agent ID with the `--direct-access-agentId` flag in 4.0.0 instead of as a positional argument.

### @qlik/api impact \{#268-qlik-api-impact}

The `directAccessAgents` module in `@qlik/api` calls the deprecated v1 endpoints, and its functions are marked as
deprecated. Migrate to `connectivity.directAccessAgents`, which calls `/api/connectivity/direct-access-agents`.

Use `@qlik/api` 2.25.0 or later. Version 2.25.0 adds `updateDirectAccessAgentConfigurations`, which patches agent
configurations. Version 2.24.0 lacks this function and uses temporary names that 2.25.0 renamed.

The `PATCH` operation requires `Content-Type: application/json-patch+json`. The generated SDK currently sends
`application/json` by default, so override the `Content-Type` header when you call
`updateDirectAccessAgentConfigurations`. Check the [@qlik/api reference](https://qlikapi-ts.qlik.dev/) for the
functions available in the version you install.

Some function names differ between the two modules:

| `directAccessAgents` function                                            | `connectivity.directAccessAgents` function                               |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `getDirectAccessAgentConfiguration`                                      | `getDirectAccessAgentConfigurations`                                     |
| `patchDirectAccessAgentConfiguration`                                    | `updateDirectAccessAgentConfigurations`                                  |
| `putDirectAccessAgentConnectorsFileConnectorFilesAllowedPaths`           | `setDirectAccessAgentConnectorsFileConnectorFilesAllowedPaths`           |
| `putDirectAccessAgentConnectorsOdbcConnectorFilesCustomDataTypeMappings` | `setDirectAccessAgentConnectorsOdbcConnectorFilesCustomDataTypeMappings` |
| `getDirectAccessAgentConnectorFilesWithoutQuery`                         | `getDirectAccessAgentConnectorFiles`                                     |
| `updateDirectAccessAgentConnectorFileWithoutQuery`                       | `updateDirectAccessAgentConnectorFile`                                   |
