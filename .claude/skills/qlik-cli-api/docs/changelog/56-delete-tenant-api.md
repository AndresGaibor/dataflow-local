---
source: https://qlik.dev/changelog/56-delete-tenant-api/
last_updated: 2025-07-08T16:09:30Z
---

# New tenant deletion API endpoints for multiple tenant entitlements

Tenants are the highest level of logical separation in Qlik Cloud available to
Qlik customers. When using a multiple tenant entitlement, you can now
programmatically delete tenants via API.

If you are a customer with a single tenant entitlement, contact Qlik for
assistance with deleting your tenant.

The most common use case for tenant deletion is in an OEM context where you create
a tenant per end customer and need to offboard customers and delete their tenant
as their contracts with you come to an end. To learn more the lifecycle of OEM in
Qlik Cloud, review the [Platform Operations tutorial series](https://qlik.dev/manage/platform-operations/overview).

> **Important!**
> Deleting a tenant is a permanent action. Neither you nor Qlik can
> restore data from the tenant after it has been purged from Qlik Cloud. Use
> this capability with caution.

## Deactivate & reactivate a tenant

To deactivate a tenant and schedule it for deletion in 15 days, send this
request:

```bash
curl -L "https://register.eu.qlikcloud.com/api/v1/tenants/TENANT_ID/actions/deactivate" ^
-H "Authorization: Bearer ACCESS_TOKEN" ^
-H "qlik-confirm-hostname: my-tenant.eu.qlikcloud.com" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
-d "{\"purgeAfterDays\": 15}"
```

This response indicates that the tenant is in a deactivated state:

```json
{
    "id": "zWbTyyJ5lzYLnm9taTD49ja4JVdNKBUM",
    "status": "disabled",
    "estimatedPurgeDate": "2023-07-30T14:01:22.000Z"
}
```

To reactivate a tenant before the estimated purge date, send this request:

```bash
curl -L "https://register.eu.qlikcloud.com/api/v1/tenants/TENANT_ID/actions/reactivate" ^
-H "Authorization: Bearer ACCESS_TOKEN" ^
-H "qlik-confirm-hostname: my-tenant.eu.qlikcloud.com" ^
-H "Content-Type: application/json" ^
-H "Accept: application/json"
```

This response indicates that the tenant is in an activated state:

```json
{
    "id": "zWbTyyJ5lzYLnm9taTD49ja4JVdNKBUM",
    "status": "active"
}
```

## Learn more

To discover more about tenant deletion:

- Review the [delete tenants](https://qlik.dev/manage/tenants/delete-tenants) topic
  to learn about the overall capability.
- Visit the [delete a tenant](https://qlik.dev/manage/platform-operations/delete-a-tenant)
  tutorial in the Platform Operation series to view this in context of a programmatic
  tenant deployment.
- Access the [delete tenants API specification](https://qlik.dev/apis/rest/tenants) to see the
  full specification.
