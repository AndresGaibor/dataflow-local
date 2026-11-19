---
source: https://qlik.dev/changelog/213-auth-settings-api/
last_updated: 2026-04-23T18:35:05+02:00
---

# New REST API - Authentication Settings API for managing session policies

The [Authentication Settings API](https://qlik.dev/apis/rest/core/auth-settings/) allows tenant administrators
to programmatically manage authentication and session policies for their Qlik Cloud tenant.

## Session policy management \{#213-session-policy-management}

Tenant administrators can now retrieve and update authentication settings that control user session behavior:

- **Session inactivity timeout**: Configure the duration of inactivity before a user session automatically expires
- **Maximum session lifespan**: Set the maximum allowed duration for a user session, regardless of activity

These settings apply tenant-wide and help enforce security policies around session management.

## API operations \{#213-api-operations}

The API supports the following operations:

- `GET /api/core/auth-settings`: Retrieve the tenant's current authentication settings, including configured values and
  defaults
- `PATCH /api/core/auth-settings`: Update authentication settings using JSON Patch (RFC 6902) operations

The API requires the `TenantAdmin` role.

For more information, see the [reference documentation for the Authentication Settings API](https://qlik.dev/apis/rest/core/auth-settings/).
