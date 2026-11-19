---
source: https://qlik.dev/changelog/81-api-updates-groups/
last_updated: 2024-03-12T08:31:35Z
---

# API updates - Users

To support customers in managing their users, groups, and tenants via API, Qlik has added the fields
parameter to the Users API. This gives customers total control over the data returned when retrieving
an individual user record.

### Get user record

You can now specify which user attributes to include in the response. The following example illustrates
how to request the "groups" field to be returned.

```shell
curl "https://<TENANT>/api/v1/users/xxxxxxxxxxxxxxxxxxxxxxxx?fields=groups" \
 -H "Authorization: Bearer <ACCESS_TOKEN>"

 # alternatively
curl "https://<TENANT>/api/v1/users/me?fields=groups" \
 -H "Authorization: Bearer <ACCESS_TOKEN>"
```

```shell
# Http 200 - Ok
{
  "id": "xxxxxxxxxxxxxxxxxxxxxxxx",
  "groups": [
    "accounting",
    "developer"
  ]
}
```

> *Note*: The "groups" field will not return system groups such as the "Everyone" group.
