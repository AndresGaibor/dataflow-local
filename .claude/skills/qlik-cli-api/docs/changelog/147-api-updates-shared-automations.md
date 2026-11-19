---
source: https://qlik.dev/changelog/147-api-updates-shared-automations/
last_updated: 2025-06-18T10:28:46+01:00
---

# Updated API - Qlik Automate in shared spaces

With the recent introduction of support for Qlik Automate in shared spaces, there are updates
to the Qlik Automate API to enable customers to take advantage of these features programmatically.

Space related properties have been added to relevant endpoints in the Qlik Automate API, and
two management endpoints have been released.

Examples of changes in current endpoints includes:

- `GET /automations`:
  - New query parameter `listAll` allowing administrators to list all automations in the tenant.
  - New field `spaceId` supported in filter query enabling users to filter automations based on spaces.

- `POST /automations`:
  - New field `spaceId` in the request payload expanding automation creation in shared spaces.

- `GET /automations/{id}/runs`
  - New fields `spaceId` `ownerId` `executedById` in filter query and API response for enhanced filtering.

## New endpoints

New API endpoints have been added to move automations between spaces, and to change owners.

Move an automation to a different space:

```shell
curl  'https://tenant.region.qlikcloud.com/v1/automations/00000000-0000-0000-0000-000000000000/actions/change-space' \
  -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
  -d '{
  "spaceId": "5f0f78b239ff4f0001234567"
}'
```

Successful response: `204 No Content`

Change the owner of an automation:

```shell
curl  'https://tenant.region.qlikcloud.com/v1/automations/00000000-0000-0000-0000-000000000000/actions/change-owner' \
  -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
  -d '{
  "userId": "sWYAHxZxhtcmBT7Ptc5xJ5I6N7HxwnEy"
}'
```

Successful response: `204 No Content`

For more information please refer to the [Automations API reference](https://qlik.dev/apis/rest/automations/).
