---
source: https://qlik.dev/changelog/255-automations-apis-deprecation/
last_updated: 2026-10-14T08:21:03Z
---

# Automation APIs deprecated in favor of namespaced Workflows APIs

> **Note:** Updated on October 14, 2026 to mention qlik-cli and `@qlik/api` impact.

The Automation connections, Automation connectors, and Automations REST APIs under `/api/v1/` are deprecated and will be
removed on or after November 30, 2027.

Equivalent APIs are available under the `/api/workflows/` namespace.

### What's changing \{#255-whats-changing}

| Deprecated API                                                                                                      | Replacement API                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [Automation connections API](https://qlik.dev/apis/rest/automation-connections/) (`/api/v1/automation-connections`) | [Workflows Automation connections API](https://qlik.dev/apis/rest/workflows/automation-connections/) (`/api/workflows/automation-connections`) |
| [Automation connectors API](https://qlik.dev/apis/rest/automation-connectors/) (`/api/v1/automation-connectors`)    | [Workflows Automation connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors/) (`/api/workflows/automation-connectors`)    |
| [Automations API](https://qlik.dev/apis/rest/automations/) (`/api/v1/automations`)                                  | [Workflows Automations API](https://qlik.dev/apis/rest/workflows/automations/) (`/api/workflows/automations`)                                  |

For existing operations, the replacement APIs use the same operation paths and request and response schemas.
Update your integrations to use the corresponding `/api/workflows/` base path before November 30, 2027.

For more information, see the [Workflows Automation connections API](https://qlik.dev/apis/rest/workflows/automation-connections/),
[Workflows Automation connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors/), and
[Workflows Automations API](https://qlik.dev/apis/rest/workflows/automations/).

### qlik-cli and qlik-api impact \{#255-qlik-cli-and-qlik-api-impact}

This change also affects qlik-cli and `@qlik/api` usage.
Existing qlik-cli commands using `qlik automation`, `qlik automation-connection`, or `qlik automation-connector` must be
updated to use the corresponding `qlik workflows` commands.
For more information, see the [qlik-cli workflows command reference](https://qlik.dev/toolkits/qlik-cli/workflows/workflows-automation/).

Applications using the deprecated `@qlik/api` modules must migrate to the corresponding `qlik.workflows` modules
(for example, `qlik.automations` → `qlik.workflows.automations`).
For more information, see the [@qlik/api workflows reference](https://qlikapi-ts.qlik.dev/modules/workflows.html).
