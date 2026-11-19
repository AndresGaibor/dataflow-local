---
source: https://qlik.dev/changelog/64-filter-space-assignments-by-type/
last_updated: 2025-07-08T16:09:30Z
---

# The Spaces API adds support for filtering Assignments by type

The query parameter "type" has been added to the Spaces API.
Supported filter values: user or group.

This feature is useful for limiting the number of assignments returned from the endpoint
in cases where only one of the assignment types is of interest.

Example:

```bash
curl --get --location 'https://<TENANT>.<REGION>.qlikcloud.com/api/v1/spaces/<id>/assignments?type=user' \
--header 'Authorization: Bearer <API_KEY>'
```

Review the [Spaces API](https://qlik.dev/apis/rest/spaces) specification for
further information.
