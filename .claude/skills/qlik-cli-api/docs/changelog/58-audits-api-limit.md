---
source: https://qlik.dev/changelog/58-audits-api-limit/
last_updated: 2025-03-11T11:54:24Z
---

# Minimum and maximum values for limit query parameter on Audits API

Minimum and maximum values have been added (which were already restricted in the
implementation details) for the `limit` parameter in the `/audits` endpoint.

- `minimum`: 1 (minimum value can be set as limit parameter)
- `maximum`: 100 (maximum value can be set as limit parameter)
- `default`: 10 (default value of the limit parameter if not set)

Example:

```bash
curl --get --location 'https://<TENANT>.<REGION>.qlikcloud.com/api/v1/audits?limit=<LIMIT>' ^
--header 'Authorization: Bearer <API_KEY>'
```

Review the Audits API specification for
further information.
