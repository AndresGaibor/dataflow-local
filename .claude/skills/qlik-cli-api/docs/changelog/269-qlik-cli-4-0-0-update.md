---
source: https://qlik.dev/changelog/269-qlik-cli-4-0-0-update/
last_updated: 2026-11-13T13:34:32Z
---

# qlik-cli 4.0.0 - November 2026

[qlik-cli](https://qlik.dev/toolkits/qlik-cli/) 4.0.0 updates the default Qlik Cloud API version to `2026-11`, adds new commands for
webhooks and data contracts, and includes breaking changes and deprecations.

> **Breaking changes:** qlik-cli 4.0.0 removes the `qlik app evaluation` commands and changes how you pass the agent ID to Direct Access agent
> benchmark commands. Review the [breaking changes](#269-breaking-changes) before you upgrade.

### API version update \{#269-api-version-update}

qlik-cli now uses API version `2026-11` by default.
For more information about dated API versions and deprecation warnings, see [API versioning](https://qlik.dev/apis/versioning/).
For the API changes in this version, see
[Quarterly API versioning and the 2026-11 API release](https://qlik.dev/changelog/266-quarterly-api-versioning-2026-11-release/).

### Breaking changes \{#269-breaking-changes}

The following changes may require updates to existing scripts:

- qlik-cli 4.0.0 removes the `qlik app evaluation` commands because the API no longer provides them.
  Use `qlik analytics app evaluation` instead.
- `qlik connectivity direct-access-agent benchmark create` and `benchmark ls` now require the agent ID in the
  `--direct-access-agentId` flag instead of as a positional argument:

  ```bash
  # qlik-cli 3.4.0
  qlik connectivity direct-access-agent benchmark ls <AGENT_ID>

  # qlik-cli 4.0.0
  qlik connectivity direct-access-agent benchmark ls --direct-access-agentId <AGENT_ID>
  ```

### New commands \{#269-new-commands}

qlik-cli now supports the following commands:

- `qlik connectivity direct-access-agent benchmark cancel` - Request benchmark cancellation.
- `qlik connectivity direct-access-agent benchmark get` - Get benchmark status.
- `qlik connectivity direct-access-agent configuration` - View Direct Access agent configuration.
- `qlik connectivity direct-access-agent connector` - Manage Direct Access agent connector configuration.
- `qlik connectivity direct-access-agent restart` - Restart the agent.
- `qlik connectivity direct-access-agent tool` - Manage Direct Access agent tools.
- `qlik core webhook` - Manage webhooks with the namespaced Core API. Replaces the legacy `qlik webhook` commands.
  For more information, see [Webhooks API deprecated in favor of new namespaced Core webhooks
  API](https://qlik.dev/changelog/263-webhooks-api-deprecation-core-webhooks-api/).
- `qlik data-governance data-contract` - Manage data contracts.
  For more information, see
  [New REST API - Data contracts API for managing dataset expectations](https://qlik.dev/changelog/261-data-contracts-api/).
- `qlik data-governance data-quality global-result data-quality-rule filter` - Get rule-quality aggregation for a
  rule across datasets. For more information, see [New Data qualities API endpoint for retrieving rule results
  across datasets](https://qlik.dev/changelog/265-data-qualities-api-rule-results/).
- `qlik scheduling task resource reload` - Create reload tasks for apps.
  For more information, see [New Scheduling Tasks API endpoints for creating reload
  tasks](https://qlik.dev/changelog/262-scheduling-tasks-api-reload-task-endpoints/).

### New flags \{#269-new-flags}

- `--accessTokenExpirationDuration` on `qlik oauth-client create`.
- `--allowedAuthTypes`, `--connectionBlockSettings-restrictionType`, and `--connectionBlockSettings-useConfigs` on
  `qlik connectivity data-source settings update`.

### Deprecated commands and flags \{#269-deprecated-commands-and-flags}

| Deprecated command or flag                                                | Replacement                                         |
| ------------------------------------------------------------------------- | --------------------------------------------------- |
| `qlik direct-access-agent` subcommands                                    | `qlik connectivity direct-access-agent` subcommands |
| `--schedules-interval` on `qlik workflows automation create` and `update` | `--schedules-recurrence`                            |

Most `qlik direct-access-agent` subcommands keep the same name under `qlik connectivity direct-access-agent`.
Some connector and tool subcommands have new paths, and
`qlik direct-access-agent tool metrics-collector configuration edit` has no replacement.
For the full command mapping, see the qlik-cli impact section of [Direct Access Agents API deprecated in favor of
Connectivity Direct Access Agents API](https://qlik.dev/changelog/268-direct-access-agents-api-deprecation/#268-qlik-cli-impact).

Qlik plans to remove the `--schedules-interval` flag on or after November 1, 2027 (API version `2027-11`).

For more information about the release, see the
[qlik-cli changelog](https://github.com/qlik-oss/qlik-cli/blob/master/CHANGELOG.md).
