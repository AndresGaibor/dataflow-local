---
source: https://qlik.dev/changelog/62-encryption-api/
last_updated: 2025-07-08T16:09:30Z
---

# New encryption API endpoints for encrypting your Qlik Cloud tenants

Qlik offers customers the ability to encrypt their tenants with their own
key. The
new [encryption API](https://qlik.dev/apis/rest/encryption)
provides you with the ability to deploy, manage, and cycle encryption keys on
one or more Qlik Cloud tenants via supported providers.

## Create & migrate to a new key provider

Here's an example of a cURL command that creates a new key provider:

```bash
curl --location "<TENANT>/api/v1/encryption/keyproviders" ^
--header "Authorization: Bearer <ACCESS_TOKEN>" ^
--header "Content-Type: application/json" ^
--data "{\"name\": \"<KEY_PROVIDER_NAME>\", \"arn\": \"<KMS_KEY_ARN>\", \"keyprovider\": \"AWS-KMS\" }"
```

The result is a JSON object that shows the details of the newly created KMS key provider.

```json
{
    "name": "<KEY_PROVIDER_NAME>",
    "tenantId": "<TENANT_ID>",
    "arn": "<KMS_KEY_ARN>",
    "arnFingerPrint": "<ARN_FINGERPRINT>",
    "keyprovider": "AWS-KMS",
    "createdAt": "2023-07-14T18:17:23Z",
    "promotedToCurrentAt": "0001-01-01T00:00:00Z",
    "demotedFromCurrentAt": "0001-01-01T00:00:00Z"
}
```

You can then migrate from the currently active key
provider to the new key provider specified by `<ARN_FINGERPRINT>`. Upon
successful migration, the migrated key provider becomes active.

```bash
curl -L "https://<TENANT>/api/v1/encryption/keyproviders/<ARN_FINGERPRINT>/actions/migrate" ^
-X POST ^
--header "Content-Type: application/json" ^
--header "Authorization: Bearer <ACCESS_TOKEN>"
```

The result is a JSON object that shows the details of the key provider migration.

```json
{
    "migrationId": "c75088bc-cfba-410a-aeda-2a5dd797f528",
    "tenantId": "<TENANT_ID>",
    "migratingFrom": "v1:rTfjXBtXurvLxUJqE4dvgyXIm6zLiaIE:iiTaqy+LNXkmCVEBN9mOwKwsNQZ0UdNUWW7s5TptbOrU67qAALinKb+UZUKBHYgVGflHmp2t2CvtBK4G",
    "migratingTo": "<KMS_KEY_ARN>",
    "migratingToFingerPrint": "<ARN_FINGERPRINT>",
    "migratingToPrefix": "#BYOKv1#:<ARN_FINGERPRINT>",
    "state": "New",
    "initiatedAt": "2023-07-18T12:08:04.634711507Z",
    "completedAt": "0001-01-01T00:00:00Z"
}
```

## Learn more about tenant encryption

To learn more:

- Review the [encrypt tenants](https://qlik.dev/manage/tenants/tenant-encryption) topic
  to learn how to send common requests.
- Visit
  the [configuring tenant encryption](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-tenant-encryption.htm)
  documentation to learn about the overall capability.
- Read
  the [no-code options for managing encryption](https://community.qlik.com/t5/Official-Support-Articles/How-to-get-started-with-the-Amazon-KMS-connector-and-Qlik-s/ta-p/2104061)
  to learn how to manage lifecycles in Qlik Automate.
- Access the [encrypt tenants API specification](https://qlik.dev/apis/rest/encryption) to see the
  full specification.
