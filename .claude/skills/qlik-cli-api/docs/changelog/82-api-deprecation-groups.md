---
source: https://qlik.dev/changelog/82-api-deprecation-groups/
last_updated: 2025-07-08T16:09:30Z
---

# API updates - Groups

Qlik is announcing a 30-day deprecation window for an unpublished endpoint on
the [Groups API](https://qlik.dev/apis/rest/groups/).

No sooner than 30 days from the date of this notice,
`GET /api/v1/groups/user-claims/:userID` will be removed from the Groups API.

To migrate to a published endpoint, use `GET /api/v1/users/:id`.

```shell
curl "https://<TENANT>/api/v1/users/<USER_ID>?fields=groups" \
 -H "Authorization: Bearer <ACCESS_TOKEN>"
```

```shell
# Http 200 - Ok
{
  "id": "<USER_ID>",
  "groups": [
    "accounting",
    "developer"
  ]
}
```
