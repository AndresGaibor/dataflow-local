---
source: https://qlik.dev/changelog/49-api-deprecation-license-attr/
last_updated: 2025-07-08T16:09:30Z
---

# API Updates - Deprecation of attributes on /v1/license/assignments

This changelog provides 60 days notice of deprecation and removal of some
undocumented attributes from the response of the `/v1/licenses/assignments` endpoint.

Qlik is making changes to ensure removal of user names and other identifiable
information from APIs where the data is available via other, more appropriate
APIs.

For more information on Qlik's API policies, please refer to
the [API policy](https://qlik.dev/apis/api-policy) page.

### Deprecation of response attributes

The attributes `name` and `userId` will be removed from the response from the
`/v1/licenses/assignments` endpoint. These are optional, undocumented attributes
that can be set when assigning a license. It will still be possible to use these
attributes in the API filter.

> **Note:**
> The endpoint will continue to return the user's `subject` as their primary
> identifier. Qlik recommends not using personally identifiable information (PII)
> in the `subject` attribute in Qlik Cloud. A good practice is to use system
> generated GUIDs to uniquely identify users.

When set on a license assignment, the response currently looks like:

```json
{
    "subject": "QLIKBOT\\f0e92f326ac77427df155940fec39e6b",
    "type": "professional",
    "userId": "637390ec6541614d3a88d6c1",
    "name": "EU OAuth Client",
    "excess": false,
    "created": "2023-06-29T12:24:34.639Z"
}
```

After deprecation, the endpoint will return:

```json
{
    "subject": "QLIKBOT\\f0e92f326ac77427df155940fec39e6b",
    "type": "professional",
    "excess": false,
    "created": "2023-06-29T12:24:34.639Z"
}
```

If you need to look up the `userId` and `name`, you can retrieve these using
the [list users](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers-get) endpoint.

```bash
curl --get --location 'https://<tenant>.<region>.qlikcloud.com/api/v1/users' ^
--header 'Authorization: Bearer <token>' ^
--header 'Content-type: application/json' ^
--header 'Accept: application/json' ^
--data-urlencode 'filter=subject eq "QLIKBOT\\f0e92f326ac77427df155940fec39e6b"'
```

This will return the full user information for the user with that subject, including
the most current `name` and `userId` (returned as `id`) attributes.

```json
{
   "data":[
      {
         "id":"637390ec6541614d3a88d6c2",
         "tenantId":"BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
         "clientId":"f0e92f326ac77427df155940fec39e6b",
         "status":"active",
         "subject":"qlikbot\\f0e92f326ac77427df155940fec39e6a",
         "name":"EU OAuth Client",
         ...
```

For more information on the license assignment endpoint, please review
the [v1/licenses/assignments](https://qlik.dev/apis/rest/licenses/#%23%2Fentries%2Fv1%2Flicenses%2Fassignments-get)
specification.
