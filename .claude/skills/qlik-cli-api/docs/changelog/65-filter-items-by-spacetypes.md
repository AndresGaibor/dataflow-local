---
source: https://qlik.dev/changelog/65-filter-items-by-spacetypes/
last_updated: 2025-07-08T16:09:30Z
---

# The Items API adds support for space type filtering and deprecates old query parameter shared

The query parameter `spaceType` has been added to the Items API to help better
support programmatic CICD workflows where you need to deploy and manage content
across different space types.

Supported space types for the filter:

- `shared`
- `managed`
- `data`
- `personal`

This new query parameter is useful for listing items within just one specific space type
or within a couple of selected space types.

> **Note:** The query parameter `shared` is now deprecated in favor of the new
> query parameter `spaceType`,which provides support for all space types as opposed
> to just `shared` spaces. `shared` will be removed no sooner than 60 days from the
> date of this notice.

Example:

```bash
curl --get --location 'https://<TENANT>.<REGION>.qlikcloud.com/api/v1/items?spaceType=shared,personal' \
--header 'Authorization: Bearer <API_KEY>'
```

Review the [Items API](https://qlik.dev/apis/rest/items) specification for
further information.
