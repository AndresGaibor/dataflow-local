---
source: https://qlik.dev/changelog/259-qlik-cli-3-4-0-update/
last_updated: 2026-10-14T16:54:45+02:00
---

# qlik-cli 3.4.0 - October 2026

[qlik-cli](https://qlik.dev/toolkits/qlik-cli/) 3.4.0 fixes an issue where app commands against Qlik Sense Enterprise on Windows
could fail with `403 Forbidden` when the stored session had expired or didn't exist yet.
This release also adds new commands and flags, and deprecates the top-level automation commands.

## Bug fix \{#259-bug-fix}

In earlier versions, the first command that opened an Engine WebSocket connection could fail with HTTP 403 when the
local cookie store was empty.
qlik-cli requested a CSRF token and session cookie from `/qps/csrftoken`, but didn't include the new session cookie in
the WebSocket handshake.
The Qlik Sense proxy rejected the connection and logged
`Cross-Site WebSocket Hijacking attack prevention check failed`.
Running the same command a second time succeeded, because the cookie from the first run was then stored locally.

qlik-cli 3.4.0 includes the session cookie in the first WebSocket handshake, so the command succeeds on the first run.
No changes are required on the Qlik Sense server or virtual proxy.

Upgrade to qlik-cli 3.4.0 or later, regardless of your Qlik Sense version.

## New commands \{#259-new-commands}

qlik-cli now supports the following commands:

- `qlik alerting sharing-task task-execution` - Examine sharing task executions.
- `qlik connectivity direct-access-agent benchmark` - Manage Direct Access agent benchmarks.
- `qlik connectivity direct-access-agent load-performance-metric` - View Direct Access agent load performance metrics.
- `qlik data-governance data-quality fields-structure update` - Assign types to dataset fields.
- `qlik data-governance semantic-type` - Manage semantic types.

## New flags \{#259-new-flags}

- `--schedules-recurrence` on `qlik workflows automation create` and `qlik workflows automation update`.
- `--documentId` on `qlik assistant search` and `qlik knowledgebase search`.
- `--name` and `--description` on `qlik direct-access-agent benchmark create`.
- `--registerOnSelectionApp` on `qlik analytics odag-link create`.
- `--sampleMethod` on `qlik data-governance data-quality computation create`.
- `--jwksUri` on `qlik oauth-client create`.

## Deprecated commands \{#259-deprecated-commands}

The following commands are deprecated. Use the `qlik workflows` equivalents instead.

| Deprecated command                       | Replacement                              |
| ---------------------------------------- | ---------------------------------------- |
| `qlik automation` subcommands            | `qlik workflows automation`              |
| `qlik automation-connection` subcommands | `qlik workflows automation-connection`   |
| `qlik automation-connector ls`           | `qlik workflows automation-connector ls` |

This follows the deprecation of the Automation REST APIs. For more information, see
[Automation APIs deprecated in favor of namespaced Workflows APIs](https://qlik.dev/changelog/255-automations-apis-deprecation/).

For more information about the release, see the
[qlik-cli changelog](https://github.com/qlik-oss/qlik-cli/blob/master/CHANGELOG.md).
