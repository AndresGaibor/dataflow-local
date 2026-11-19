---
source: https://qlik.dev/changelog/178-qlik-cli-2-29-update/
last_updated: 2025-11-12T15:35:12+01:00
---

# qlik-cli 2.29.0 - November 2025

A new release of [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) has been published, which expands the set of covered APIs
to include additional published [REST APIs](https://qlik.dev/apis/rest/), and fixes bugs.

## New commands \{#new-commands-2025-11}

qlik-cli now supports the following commands:

- `qlik automation-connector ls` - Retrieves a list of automation connectors.
- `qlik banner ls` - Retrieves the announcement banner configuration for the tenant.
- `qlik banner upsert` - Set an announcement banner.

## Bug fixes \{#bug-fixes-2025-11}

The following issues have been fixed:

- Handling of content-types with a sub-type, as returned by the `qlik report-filter ls` command.
- Improved handling when adding new specifications using the `qlik spec` command.
