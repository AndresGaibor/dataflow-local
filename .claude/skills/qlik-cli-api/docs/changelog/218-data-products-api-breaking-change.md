---
source: https://qlik.dev/changelog/218-data-products-api-breaking-change/
last_updated: 2026-05-12T15:52:05Z
---

# Breaking change - Data Products API PATCH endpoint limits operations per request

A breaking change is introduced on the `PATCH /data-governance/data-products/{dataProductId}` endpoint.

The number of PATCH operations per request is now limited to **8**, which matches the number of fields
available on the data product resource.
Requests that include more than 8 operations will receive an `HTTP 400 Bad Request` response.

To adapt to this change, update your PATCH requests to contain **no more than 8 operations**.

For more information, refer to the [Data Products API reference documentation](https://qlik.dev/apis/rest/data-governance/data-products/).
