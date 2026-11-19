---
source: https://qlik.dev/changelog/69-collections-api-improvements/
last_updated: 2025-07-08T16:09:30Z
---

# Improvements to Collections API

The `PATCH` method has been added to the [Collections API](https://qlik.dev/apis/rest/collections),
giving you the ability to update more collection metadata, with greater flexibility.

The Collections API is the engine behind public and private collections, but also
tags assigned to content in the [Items API](https://qlik.dev/apis/rest/items).

With the `PATCH` method, you no longer need to send a full `PUT` payload when
updating collections, simplifying the calls, and reducing access control complexity.

To make a private collection public (assuming you have the appropriate access rights, and at least
one item in the collection), you must change the
`type` of the collection from `private` to `publicgoverned`:

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/collections/{collectionId}" ^
 -X PATCH ^
 -H "Authorization: Bearer <API-key>" ^
 -H "Content-type: application/json" ^
 -d '[{"op":"replace","path":"/type","value":"publicgoverned"}]'
```

Example response:

```json
{
    "name": "My Public Collection",
    "description": "A logical grouping of content for a business unit or team, which still respects space permissions.",
    "type": "publicgoverned",
    "id": "{collectionId}",
    ...
}
```

To unpublish the collection, change the `type` back to `private`.

The `PATCH` operation can also be used on the `name` and `description` of the collection.

Review the [Collections API](https://qlik.dev/apis/rest/collections) specification for
further information.
