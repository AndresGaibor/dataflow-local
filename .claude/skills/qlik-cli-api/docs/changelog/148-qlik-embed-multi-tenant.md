---
source: https://qlik.dev/changelog/148-qlik-embed-multi-tenant/
last_updated: 2025-06-24T09:47:06+02:00
---

# qlik-embed adds support for embedding from different Qlik Cloud tenants

`qlik-embed` now supports multi-tenant embedding, allowing you to display visualizations from different Qlik Cloud
tenants on the same page.

You can define authentication configurations for each tenant and reference them using the `host-config` attribute in
`<qlik-embed>` elements.

This enables new use cases such as:

- Comparing customer-specific data from separate tenants
- Combining anonymous and authenticated content in one view
- Building dashboards that pull from multiple environments

For configuration examples and usage, see [Using qlik-embed with multiple tenants](https://qlik.dev/embed/qlik-embed/authenticate/multi-environments).
