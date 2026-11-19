---
source: https://qlik.dev/changelog/196-api-data-products/
last_updated: 2026-04-20T13:34:03+01:00
---

# New API - Data Products API

The new Data Products API is now available for automating data product management and governance.
This API allows you to programmatically create, manage, activate, and monitor data products.

Data products are packages that group related datasets within a single, curated offering.
They enable organizations to organize and govern data by business domain, making it easier for business users to
discover and consume trusted, well-documented datasets.

With the Data Products API, you can:

- Create new data products within spaces using `POST /api/data-governance/data-products`
- Retrieve and manage data product details using `GET /api/data-governance/data-products/{dataProductId}`
- Update data product metadata and datasets using `PATCH /api/data-governance/data-products/{dataProductId}`
- Manage products across spaces with move operations using `POST /api/data-governance/data-products/{dataProductId}/actions/move`
- Activate data products to make them discoverable using `POST /api/data-governance/data-products/{dataProductId}/actions/activate`
- Track data product changes through changelogs using `GET /api/data-governance/data-products/{dataProductId}/changelogs`
- Export data product documentation for stakeholder sharing using `GET /api/data-governance/data-products/{dataProductId}/actions/export-documentation`

For more information, refer to:

- The [Data Products API reference documentation](https://qlik.dev/apis/rest/data-governance/data-products/)
- The [Create and activate a data product tutorial](https://qlik.dev/manage/data-governance/create-data-product/)
