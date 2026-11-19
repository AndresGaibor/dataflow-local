---
source: https://qlik.dev/changelog/57-reloads-api-improvements/
last_updated: 2023-12-19T16:00:34+01:00
---

# Improvements to Reloads API

New query parameters have been added to the Reloads API,
giving you additional flexibility in monitoring and managing analytics reloads
in your tenant.

Additions:

- `filter` - allows you to filter on `status` and `partial` with equals (`eq`).
- `log` - allows you to turn off the log that is usually returned with every
  API call to improve response time.

To filter on a single status (`RELOADING`),and exclude the logs:

```bash
curl --get --location 'https://<TENANT>.<REGION>.qlikcloud.com/api/v1/reloads' ^
--header 'Authorization: Bearer <ACCESS_TOKEN>' ^
--header 'Content-type: application/json' ^
--header 'Accept: application/json' ^
--data-urlencode 'filter=status eq "RELOADING"' ^
--data-urlencode 'log=false'
```

To filter on multiple statuses (`QUEUED` and `RELOADING`), and exclude the logs:

```bash
curl --get --location 'https://<TENANT>.<REGION>.qlikcloud.com/api/v1/reloads' ^
--header 'Authorization: Bearer <ACCESS_TOKEN>' ^
--header 'Content-type: application/json' ^
--header 'Accept: application/json' ^
--data-urlencode 'filter=(status eq "RELOADING") OR (status eq "QUEUED")' ^
--data-urlencode 'log=false'
```

Review the Reloads API specification for
further information.
