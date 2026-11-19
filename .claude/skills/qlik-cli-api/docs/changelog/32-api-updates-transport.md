---
source: https://qlik.dev/changelog/32-api-updates-transport/
last_updated: 2025-07-08T16:09:30Z
---

# New API - Transport

### Transport API

The Transport API is the service responsible for managing notification channels
and email configurations for the sending of system notifications,
as well as updates from analytics services in the hub, such as data alerts
and subscriptions.

These notifications provide users with information about events such as failed
reloads, users being added to spaces, data alerts being triggered, and regular
subscription snapshots being sent to subscribers. Note that any workflows running
in Qlik Automate (including the report blocks) will use their own
SMTP/ email configuration - only system notifications from Qlik Automate
will be sent via the transport API.

The endpoints in this release provide the ability to configure and review the
email server configuration for this service, including the following examples:

- `GET/v1/transports/email-config` : Returns the email configuration for a given tenant id.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config" \
 -H "Authorization: Bearer <API-key>"
```

- `PATCH/v1/transports/email-config` : Patch the email configuration for a given tenant id.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config" \
 -X PATCH \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d
 '{
    "op": "replace",
    "path": "/username",
    "value": "New name"
  }'
```

- `DELETE/v1/transports/email-config`: Deletes email configuration for a given tenant id.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config" \
 -X DELETE \
 -H "Authorization: Bearer <API-key>"
```

- `POST/v1/transports/email-config/actions/send-test-email` : Send a test mail with the
  supplied email info(subject, body, recipient).

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config/actions/send-test-email" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
     "body":"string",
     "subject":"string",
     "recipient":"string"
     }'
```

- `POST/v1/transports/email-config/actions/validate` : Returns the isValid value
  for the email configuration for the tenant. Will return false if no email configuration exists.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config/actions/validate" \
 -X POST \
 -H "Authorization: Bearer <API-key>"
```

- `POST/v1/transports/email-config/actions/verify-connection`: Verifies connection to email server
  for tenant provided via JWT.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config/actions/verify-connection" \
 -X POST \
 -H "Authorization: Bearer <API-key>"
```

See full API reference [here](https://qlik.dev/apis/rest/transports), or read
more about [configuring SMTP providers for your tenant](https://qlik.dev/manage/tenants/email-provider).
