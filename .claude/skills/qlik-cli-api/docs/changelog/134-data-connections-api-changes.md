---
source: https://qlik.dev/changelog/134-data-connections-api-changes/
last_updated: 2025-05-12T16:48:26+02:00
---

# API breaking change notice - Data Connections and Data Credentials APIs

As part of improvements to the [Data Connections](https://qlik.dev/apis/rest/data-connections/)
and [Data Credentials](https://qlik.dev/apis/rest/data-credentials) APIs
to support the update of credentials on existing connections without
knowing the specific encoding format, a breaking change will be made to the supported
payload structure for the following endpoints:

- [`PATCH /api/v1/data-connections/{qId}`](https://qlik.dev/apis/rest/data-connections/#patch-v1-data-connections-qID)
- [`PATCH /api/v1/data-credentials/{qId}`](https://qlik.dev/apis/rest/data-credentials/#patch-v1-data-credentials-qID)

In both cases, the payload of the call will change from an object format:

```json
{
  "patchData": [
    {
      "op": "add",
      "path": "/qName",
      "value": "New value"
    }
  ]
}
```

To an array format:

```json
[
  {
    "op": "add",
    "path": "/qName",
    "value": "New value"
  }
]
```

These changes make the APIs more consistent with others in the platform, while
adding support for making updates to additional properties.

> **Breaking change:** These breaking changes will take effect on or after May 23, 2025.
> After these changes are deployed, `PATCH` requests using the old payload format will return a `400` status.
> You can update your integration to use the new format if a `400` status is returned.
