---
source: https://qlik.dev/changelog/99-qlik-cli-update/
last_updated: 2025-06-19T11:53:14Z
---

# qlik-cli Update - June 2024

## qlik-cli 2.25.0

A new release of [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) has been published.

Change summary:

- Added `oauth-client` command for the `oauth-clients` API
- Added `automation-connections` command for the `automation-connections` API
- Updated app properties exported on `qlik app unbuild` command
- Added CSRF support for Qlik Sense Enterprise client-managed
- Tidied up various descriptions
- Removed deprecated `qlik catwalk` commands
- Removed deprecated `qlik csp-header` commands

### Added `oauth-client` command for the `oauth-clients` API

The `oauth-clients` API allows you to create and manage OAuth clients, used for
authentication in Qlik Cloud. These are designed to support use cases such as
embedding, automation, orchestration, and more.

Explore the new commands under:

```bash
qlik oauth-client
```

If you're new to OAuth in Qlik Cloud, explore the [OAuth2 overview](https://qlik.dev/authenticate/oauth/).

### Added `automation-connections` command for the `automation-connections` API

Automations are the primary resource for [Qlik Automate](https://qlik.dev/toolkits/no-code/),
which provide no-code methods for integrating with Qlik and third-party services.

The [recently released Automation-connections API](https://qlik.dev/changelog/97-api-updates-automation-connections/)
allows you to create and manage connectivity to services. These connections can be
used by one or more automations.

Explore the new commands under:

```bash
qlik automation-connection
```

### Updated app properties exported on `qlik app unbuild` command

Added missing app properties to the unbuild command, to ensure a more complete
unbuild of the app.

### Added CSRF support for Qlik Sense Enterprise client-managed

An upcoming change in Qlik Sense Enterprise client managed will make
it a requirement to include a CSRF-token when establishing websocket connections.
This adds a forwards-compatible fix for that.

### Removed deprecated `qlik csp-header` commands

This deprecated endpoint has now been removed. It was replaced
by `qlik csp-origin generate-header`.
