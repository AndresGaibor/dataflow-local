---
source: https://qlik.dev/changelog/38-api-updates-changeowner/
last_updated: 2025-07-08T16:09:30Z
---

# New apps API endpoint & tutorial - change app object owner

### Apps API

The [`apps`](https://qlik.dev/apis/rest/apps) API provides access to create and manage Qlik
Sense and QlikView apps in Qlik Cloud.

To support Qlik customers migrating from Qlik Sense Enterprise Client-Managed to
Qlik Cloud, a new endpoint at
[`/v1/apps/{appId}/objects/{objectId}/actions/change-owner`](https://qlik.dev/apis/rest/apps/#%23%2Fentries%2Fv1%2Fapps%2F-appId%2Fobjects%2F-objectId%2Factions%2Fchange-owner-post)
has been added. The new endpoint supports changing the owner of app objects in
Qlik Sense apps.

This means that administrators can now migrate Qlik Sense apps with no loss of
private or community content, ensuring that your users have no interruption in
access to all of the objects from Client-Managed, including bookmarks, stories,
sheets, snapshots, and more.

A full tutorial demonstrating the migration of an app and reassignment of object
ownership is available [here](https://qlik.dev/manage/migrate/qlik-cli-app-objects-migrate).

> **Note:** You must own the object to change it's ownership to another user.

- `POST/v1/apps/{appId}/objects/{$objectId}/actions/change-owner` : Change owner of object

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/apps/{appId}/objects/{objectId}/actions/change-owner" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{"ownerId":"string"}'
```

See full API reference [here](https://qlik.dev/apis/rest/apps), or review
the full tutorial [here](https://qlik.dev/manage/migrate/qlik-cli-app-objects-migrate).
