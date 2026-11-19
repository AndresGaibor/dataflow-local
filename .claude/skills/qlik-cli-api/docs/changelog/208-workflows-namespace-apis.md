---
source: https://qlik.dev/changelog/208-workflows-namespace-apis/
last_updated: 2026-04-10T13:38:45+02:00
---

# New Workflows namespace APIs for automation management

The Workflows namespace now includes APIs for managing automations and their
integrations. These new namespaced APIs replace the legacy v1 equivalents and
provide standardized interfaces aligned with Qlik's API design principles.

## What's available \{#208-whats-available}

The Workflows namespace includes three related APIs:

- **Automations API** (`/workflows/automations`): Create, read, update, and
  manage automation workflows in the Workflows namespace.
- **Automation Connections API** (`/workflows/automation-connections`):
  Manage connection credentials and configurations.
- **Automation Connectors API** (`/workflows/automation-connectors`): Access
  available connector definitions and capabilities.

## Why migrate \{#208-why-migrate}

The new Workflows namespace APIs offer:

- **Consistency**: Standardized request/response formats and query parameters
  aligned with Qlik API design principles.
- **Clarity**: APIs grouped by business context, making it easier to find and
  understand related resources.
- **Future-proof**: Prepared for versioning support, enabling non-breaking
  improvements.
- **Simplified paths**: Removal of `v1` from the path for cleaner, more
  intuitive API routes.

## Migration path \{#208-migration-path}

The legacy v1 APIs (`/v1/automations`, `/v1/automation-connections`, and
`/v1/automation-connectors`) remain fully supported and are not yet deprecated.
At the point of deprecation there will be a **12-month minimum
deprecation window**. Check this changelog for deprecation notices with clear
timelines.

To start migrating:

1. Review the [Automations API](https://qlik.dev/apis/rest/workflows/automations),
   [Automation Connections API](https://qlik.dev/apis/rest/workflows/automation-connections),
   and [Automation Connectors API](https://qlik.dev/apis/rest/workflows/automation-connectors)
   documentation.
2. Update your API calls to use the new `/workflows/*` paths.
3. Test your integrations in a non-production environment first.
4. Deploy updates during your normal release schedule.

> **Tip:** For details about API namespaces, timing, and the complete list of available
> namespaced APIs, see the [API namespaces overview](https://qlik.dev/apis/namespaces/).
