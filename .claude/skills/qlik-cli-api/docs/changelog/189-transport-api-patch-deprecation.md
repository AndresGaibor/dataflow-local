---
source: https://qlik.dev/changelog/189-transport-api-patch-deprecation/
last_updated: 2025-12-16T09:27:09Z
---

# Email configuration (Transports) PATCH endpoint deprecated in favor of PUT

The `PATCH /api/v1/transports/email-config` endpoint is being deprecated in favor of the new
`PUT /api/v1/transports/email-config` endpoint. The PATCH endpoint will be removed on or after **October 31, 2026**.

## Why migrate to PUT

The PUT endpoint provides several advantages over PATCH:

- **Automatic validation**: The PUT endpoint validates the entire email server configuration automatically when you
  submit it.
- **Sender name support**: The PUT endpoint supports the new `senderName` attribute, which PATCH doesn't support.
- **Simpler payloads**: With PUT, you send the complete email server configuration in a single request. PATCH requires
  a longer payload structure to update the sender name.

## Migration requirements

When using the PUT endpoint, you must send the complete email server configuration in each request. The endpoint
validates the configuration automatically upon submission.

### Example: Using PUT endpoint for basic authentication email provider configuration

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/transports/email-config" \
  -X PUT \
  -H "Authorization: Bearer <API-key>" \
  -H "Content-Type: application/json" \
  -d '{
    "providerConfig": {
      "serverAddress": "smtp.example.com",
      "securityType": "StartTLS",
      "serverPort": 587,
      "username": "noreply",
      "emailPassword": "your-password",
      "senderName": "Your Sender Name",
      "emailAddress": "noreply@example.com"
    },
    "serviceProvider": "BasicAuth"
}'
```

## Timeline

You must migrate all integrations using `PATCH /api/v1/transports/email-config` to `PUT /api/v1/transports/email-config`
before the migration deadline.

For more information, see [the Email configuration (Transports) API reference documentation](https://qlik.dev/apis/rest/transports).
