---
source: https://qlik.dev/changelog/18-api-updates-misc/
last_updated: 2025-07-08T16:09:30Z
---

# SaaS API Updates 21-Dec-2021

### Data Connections API

Two new endpoints are added to the Data Connections API.

- `data-connections/actions/delete` that deletes multiple connections and is
  only available to Admins.

- `data-connections/actions/update` that updates multiple connections and
  is only available to Admins.

Learn more about this [here](https://qlik.dev/apis/#rest-api-data-connections).

### Reloads API

The following endpoints are new to the Reloads API.

- `GET /reloads`: Reloads allows for triggering reloads of apps to refresh its
  data. Traditionally this has only been possible through the JSON-RPC websocket
  API, but can now also be done by using this REST API.

- `GET /reloads/{reloadId}`: Finds and returns a reload record.

- `POST /reloads`: Reloads an app specified by an app ID.

Read more [here](https://qlik.dev/apis/rest/reloads).

### Reporting Service API

The new Reporting Service API provides the ability to generate
reports in PNG, PDF, and xlsx formats programmatically. Reports content could
be either a single visualization, an entire sheet, a story or a composition of
sheets.

Comprises two endpoints:

- `POST/reports`: Queues a new report request generation
- `GET/reports/{id}/status`: Gets report request processing status

Learn more [here](https://qlik.dev/apis/rest/reports).
