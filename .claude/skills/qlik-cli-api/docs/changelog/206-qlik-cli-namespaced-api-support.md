---
source: https://qlik.dev/changelog/206-qlik-cli-namespaced-api-support/
last_updated: 2026-04-08T15:46:20+02:00
---

# qlik-cli 3.0.0 adds namespace command support

[qlik-cli](https://qlik.dev/toolkits/qlik-cli/) 3.0.0 now supports namespaced command groups that mirror the new
namespace structure.
You can invoke commands under logical namespaces, while legacy commands remain
available for non-namespace resources.

### New namespace command structure \{#206-new-namespace-command-structure}

Commands are now organized by namespace, reflecting the underlying API structure.
For example, `qlik ml deployment`: Machine learning deployments and experiments

Run `qlik --help` to see all available namespace groups and legacy command groups.

### Legacy commands \{#206-legacy-commands}

For most resources, legacy commands (for example, `qlik app`, `qlik user`) continue to work
unchanged and point to the existing `/api/v1/` endpoints. Use these while you plan your
migration to namespaced commands.

> **Breaking change - ml commands removed:** Legacy `qlik ml` commands have been removed. Support for the `/api/v1/ml/` endpoints
> is no longer available. Namespaced ML commands (resolving to `/api/ml/...`) are coming
> in a future release. If you currently use `qlik ml deployment` or `qlik ml experiment`,
> plan your migration timeline for when the namespaced equivalent becomes available.

### Replacement warnings \{#206-replacement-warnings}

When using a legacy command that has a namespaced replacement, a warning is displayed
pointing to the new command path. For example:

```txt
Warning: This command is being replaced by 'qlik workflows automation ls'.
```

This helps you identify which commands require updating during your migration.

### Migration path \{#206-migration-path}

Namespaced commands are the canonical path forward.
Legacy API v1 commands remain available during the migration window, but may be deprecated
with advance notice.

**Start your migration planning now.** Deprecation dates will be announced in this
changelog for each API v1 endpoint as its namespaced equivalent becomes available.
Beginning your migration early ensures readiness when deprecation is announced.

To prepare:

1. Audit your scripts to identify which qlik-cli commands you use (see `qlik --help`).
2. For commands with namespaced equivalents, plan your migration timeline.
3. For commands not yet available as namespaced versions, continue using legacy commands.
4. Watch this changelog for announcements of new namespaced commands and API v1 deprecation dates.

> **Tip:** For more details about API namespaces, see the [API namespaces overview](https://qlik.dev/apis/namespaces/).
