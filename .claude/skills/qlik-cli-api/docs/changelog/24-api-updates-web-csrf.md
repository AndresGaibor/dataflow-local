---
source: https://qlik.dev/changelog/24-api-updates-web-csrf/
last_updated: 2025-07-08T16:09:30Z
---

# New APIs - Web-integrations, CSRF-token and Tenants

### Web-integrations

A web integration is a resource representing a list of whitelisted origins
that can make requests to a specified tenant.
It is the implementation of the CORS mechanism within Qlik Cloud.

With this API you can;

- `POST/web-integrations`: Creates a web integration.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/web-integrations" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{"name":"My Web Integration","validOrigins":["https://thirdPartyApp.com"]}'
```

- `GET/web-integrations/{id}` : Retrieves a single web integration by ID.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/web-integrations/{id}" \
 -H "Authorization: Bearer <API-key>"
```

- `DELETE/web-integrations/{id}`: Deletes a single web integration by ID.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/web-integrations/{id}" \
 -X DELETE \
 -H "Authorization: Bearer <API-key>"
```

And more, see full API reference [here](https://qlik.dev/apis/rest/web-integrations)

### CSRF Token

This API is used to interact with the CSRF token
resource in Edge Auth in Qlik elastic environments.

- `GET/csrf-token`: Returns CSRF token via the qlik-csrf-token header.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/csrf-token" \
 -H "Authorization: Bearer <API-key>"
```

See API reference [here](https://qlik.dev/apis/rest/csrf-token)

### Tenants

Tenants is the resource representing a tenant.

- `POST/tenants`: Creates a tenant.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/tenants" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{"licenseKey":"string"}'
```

See API reference [here](https://qlik.dev/apis/rest/tenants)
