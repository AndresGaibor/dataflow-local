---
source: https://qlik.dev/changelog/243-qlik-automate-connector-updates/
last_updated: 2026-08-04T12:18:13+01:00
---

# Block updates - Microsoft SQL Server & Qlik Cloud Services connectors

Updates have been made to
[Qlik Automate](https://qlik.dev/toolkits/no-code/) connectors and blocks.

### Microsoft SQL Server connector \{#243-microsoft-sql-server-connector}

**Updated blocks**:

- `Insert bulk`: Added an optional schema parameter to target a table in a specific
  database schema.
- `Insert record`: Added an optional schema parameter to target a table in a specific
  database schema.
- `Update record by one field`: Added an optional schema parameter to target a table in a
  specific database schema.
- `Upsert bulk`: Added an optional schema parameter to target a table in a specific
  database schema.

### Qlik Cloud Services connector \{#243-qlik-cloud-services-connector}

**Updated blocks**:

- `Raw API list request`: Added support for additional API namespaces and services,
  including auth settings, data governance, and direct access agents.
- `Raw API request`: Fixed an issue where calls to scheduling tasks endpoints with an
  empty request body incorrectly returned a "Request body must be empty" error. Also
  added support for additional API namespaces and services, including auth settings,
  data governance, and direct access agents.
