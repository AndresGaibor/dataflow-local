---
source: https://qlik.dev/changelog/133-openapi-spec-changes/
last_updated: 2025-04-22T09:44:00Z
---

# OpenAPI Specification Breaking Changes

To enhance the usability and clarity of the REST API documentation on [qlik.dev](https://qlik.dev/),
a breaking change will be made to the downloadable OpenAPI specifications available in
the [REST API Reference](https://qlik.dev/apis/rest/).

Currently, the OpenAPI specifications are missing key elements that limit their compatibility with third-party tools.
The upcoming update will address this.

The following enhancements will be introduced:

- The `servers.url` field, which is currently empty, will be updated to use a templated URL.
- All endpoint paths will be updated to include the full API prefix. For example: `/v1/apps` will become `/api/v1/apps`.

```yaml title="OpenAPI spec servers example"
servers:
  - url: "https://{tenant}.{region}.qlikcloud.com"
    variables:
      tenant:
        default: your-tenant
        description: Name of the tenant that will be called
      region:
        default: us
        description: The region the tenant is hosted in
```

```yaml title="OpenAPI spec paths example"
paths:
  /api/v1/apps:
    get:
      summary: List all apps
      description: Retrieve a list of apps.
      operationId: listApps
      parameters:
        - name: limit
          in: query
          description: The maximum number of results to return.
          required: false
          schema:
            type: integer
            default: 100
```

These changes will make it easier to import the specifications into third party tooling without any modifications.

> **Breaking change:** These breaking changes will take effect on or after May 19, 2025.
