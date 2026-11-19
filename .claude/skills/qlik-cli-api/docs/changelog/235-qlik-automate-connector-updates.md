---
source: https://qlik.dev/changelog/235-qlik-automate-connector-updates/
last_updated: 2026-07-16T09:31:27Z
---

# Block updates - Qlik Automate connectors

Updates have been made to
[Qlik Automate](https://qlik.dev/toolkits/no-code/) connectors and blocks.

### Qlik Cloud Services connector \{#235-qlik-cloud-services-connector}

**New blocks**:

- `List current changes from change store incrementally`: On the first run,
  this block returns a list of all saved changes from a change store that
  are currently active in a write table. On subsequent runs, it will only
  retrieve changes that have been updated since the previous run.
