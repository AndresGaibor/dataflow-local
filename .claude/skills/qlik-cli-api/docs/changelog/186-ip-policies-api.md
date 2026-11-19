---
source: https://qlik.dev/changelog/186-ip-policies-api/
last_updated: 2025-12-04T10:33:01Z
---

# New REST API - IP Policies API for managing IP allowlisting rules

The new [IP Policies API](https://qlik.dev/apis/rest/core/ip-policies/) allows users with the `TenantAdmin` role to programmatically
manage IP allowlisting rules in their Qlik Cloud tenant.
This is the first API released under the new `core` namespace, grouping platform-wide resources.

This API lets you define, update, and delete IP policies that control access to your Qlik Cloud tenant by only
permitting specific IPv4 addresses or ranges.
Enabling an IP policy turns on allowlisting, limiting tenant access to the defined IPs.

The API supports the following operations:

- `GET /core/ip-policies`: List existing IP policies in the tenant.
- `POST /core/ip-policies`: Create a new IP policy.
- `GET /core/ip-policies/{id}`: Retrieve details of a specific IP policy.
- `PATCH /core/ip-policies/{id}`: Update a policy's name, allowed IPs, or status.
- `DELETE /core/ip-policies/{id}`: Delete an IP policy.

For more information, see the [reference documentation for the IP Policies API](https://qlik.dev/apis/rest/core/ip-policies/).
