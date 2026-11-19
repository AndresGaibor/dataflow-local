---
source: https://qlik.dev/changelog/164-api-updates-reports/
last_updated: 2025-10-31T14:06:52+01:00
---

# Updated API - New outputs listing endpoint in the Reports API

A new Reports API endpoint is now available:

- `GET:/v1/reports/{id}/outputs`: This returns a list of outputs produced for the given report request.
  The outputs are generated asynchronously and are only complete when the status of the report request is
  `done`, `failed`, or `aborted`.

For more information, see the [Reports API reference](https://qlik.dev/apis/rest/reports/#get-api-v1-reports-id-outputs).
