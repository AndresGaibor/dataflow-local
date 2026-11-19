---
source: https://qlik.dev/changelog/263-webhooks-api-deprecation-core-webhooks-api/
last_updated: 2026-11-12T11:04:27Z
---

# Webhooks API deprecated in favor of new namespaced Core webhooks API

> **Deprecation notice:** The [Webhooks API](https://qlik.dev/apis/rest/webhooks/) under `/api/v1/webhooks` is deprecated and will be removed on or after
> November 1, 2027.
>
> Migrate to the new [Core webhooks API](https://qlik.dev/apis/rest/core/webhooks/) under `/api/core/webhooks`.

The new [Core webhooks API](https://qlik.dev/apis/rest/core/webhooks/) in the `core` namespace replaces the 10 published
operations of the [Webhooks API](https://qlik.dev/apis/rest/webhooks/).

The following endpoints are deprecated and have a direct replacement:

| Deprecated endpoint                                                 | Replacement endpoint                                                  |
| ------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `GET /api/v1/webhooks`                                              | `GET /api/core/webhooks`                                              |
| `POST /api/v1/webhooks`                                             | `POST /api/core/webhooks`                                             |
| `GET /api/v1/webhooks/{id}`                                         | `GET /api/core/webhooks/{id}`                                         |
| `PATCH /api/v1/webhooks/{id}`                                       | `PATCH /api/core/webhooks/{id}`                                       |
| `PUT /api/v1/webhooks/{id}`                                         | `PUT /api/core/webhooks/{id}`                                         |
| `DELETE /api/v1/webhooks/{id}`                                      | `DELETE /api/core/webhooks/{id}`                                      |
| `GET /api/v1/webhooks/{id}/deliveries`                              | `GET /api/core/webhooks/{id}/deliveries`                              |
| `GET /api/v1/webhooks/{id}/deliveries/{deliveryId}`                 | `GET /api/core/webhooks/{id}/deliveries/{deliveryId}`                 |
| `POST /api/v1/webhooks/{id}/deliveries/{deliveryId}/actions/resend` | `POST /api/core/webhooks/{id}/deliveries/{deliveryId}/actions/resend` |
| `GET /api/v1/webhooks/event-types`                                  | `GET /api/core/webhooks/event-types`                                  |

The deprecated endpoints continue to work until removal. Plan your migration before the removal date.

To migrate an existing integration:

1. Replace `/api/v1/webhooks` with `/api/core/webhooks` in your API requests.
2. Keep the remaining path, query parameters, and request bodies unchanged.
3. Test your integration with the new endpoints in a non-production tenant.
4. Deploy the updated integration and remove any remaining calls to `/api/v1/webhooks`.

Both API paths use the same webhook resources. Existing webhooks, their IDs, and delivery history are preserved.
You don't need to recreate webhooks or migrate their data. Changing the API path also doesn't affect webhook
delivery payloads.

The following example shows the same request before and after migration:

```bash
# Deprecated
curl "https://<TENANT>.<REGION>.qlikcloud.com/api/v1/webhooks" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"

# Replacement
curl "https://<TENANT>.<REGION>.qlikcloud.com/api/core/webhooks" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

> **Note:** The `qlik webhook` commands in qlik-cli and the `webhooks` module in `@qlik/api` use the deprecated
> `/api/v1/webhooks` endpoints.
>
> Namespaced replacements are not available in qlik-cli 3.4.0 or `@qlik/api` 2.20.0. Until replacements are
> available, use direct REST API requests to access `/api/core/webhooks`.
>
> Watch this change log for updates to [qlik-cli](https://qlik.dev/toolkits/qlik-cli/) and [@qlik/api](https://qlikapi-ts.qlik.dev/).
