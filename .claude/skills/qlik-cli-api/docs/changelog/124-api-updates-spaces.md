---
source: https://qlik.dev/changelog/124-api-updates-spaces/
last_updated: 2025-02-27T09:35:38Z
---

# Updated API - The Spaces API adds endpoints to manage space shares

The [Spaces API](https://qlik.dev/apis/rest/spaces/) has been updated to include new endpoints to manage
space shares.

This supports two tasks:

- Sharing a resource (for example, a Qlik Sense application) to specific users or groups
  in a tenant without giving them access to other content in that space.
- Managing analytic links for Qlik Sense apps in a tenant with the anonymous
  capability enabled.

The new endpoints are:

- `POST /api/v1/spaces/{spaceId}/shares` - Share a resource in a space with specific users
  or groups, or create a link share in an anonymous tenant.
- `GET /api/v1/spaces/{spaceId}/shares` - Get a list of shares for a space.
- `GET /api/v1/spaces/{spaceId}/shares/{shareId}` - Get a share by ID.
- `PATCH /api/v1/spaces/{spaceId}/shares/{shareId}` - Update a share by ID.
- `DELETE /api/v1/spaces/{spaceId}/shares/{shareId}` - Delete a share by ID.

For more information on this API, review the [Spaces API specification](https://qlik.dev/apis/rest/spaces/).
