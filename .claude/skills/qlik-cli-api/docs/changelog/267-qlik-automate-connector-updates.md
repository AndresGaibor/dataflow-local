---
source: https://qlik.dev/changelog/267-qlik-automate-connector-updates/
last_updated: 2026-11-12T18:10:59+01:00
---

# Block updates - Databricks, Qlik Cloud Services & Slack connectors

Updates have been made to
[Qlik Automate](https://qlik.dev/toolkits/no-code/) connectors and blocks.
For updated blocks, existing blocks already deployed in your automations are not
updated automatically—you must manually replace them to use the
latest version. See below for full details.

### Databricks connector \{#267-databricks-connector}

**New blocks**:

- `Execute SQL statement`: Executes a SQL statement and optionally waits for its results for a
  specified time.

### Qlik Cloud Services connector \{#267-qlik-cloud-services-connector}

**Updated blocks**:

- `Do evaluation`: Replaced with a new version of the block. The previous version is
  retained as `Do evaluation - deprecated` for backward compatibility; use the new
  version going forward.

### Slack connector \{#267-slack-connector}

**New blocks**:

- `List channels by name`: Searches for Slack channels with a name that contains the given text
  (case-insensitive partial match) and returns the full channel objects for all matches found.
