---
source: https://qlik.dev/changelog/22-api-updates-users-groups-roles/
last_updated: 2025-07-08T16:09:30Z
---

# API Updates - Users, Groups and Roles

### NEW API: Roles

You're now able to list all assignable roles within your tenant.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/roles" \
 -H "Authorization: Bearer <API-key>"
```

```shell
# Http 200 - Ok
{
  "data": [
    {
      "id": "605a18af2ab08cdbfad09259",
      "tenantId": "",
      "name": "AnalyticsAdmin",
      "description": "",
      "type": "default",
      "level": "admin",
      "permissions": [
        "automation:delete",
        "automation:disable",
        "automation:enable",
        "automation:list",
        ...
      ],
      "createdAt": "2021-03-23T16:34:55.401Z",
      "lastUpdatedAt": "2022-04-29T12:06:44.246Z",
      "links": {
        "self": {
          "href": "https://your-tenant.us.qlikcloud.com/api/v1/roles/605a18af2ab08cdbfad09259"
        }
      }
    },
    ...
  ]
}
```

For the complete list of supported features, please see the [Roles API specifications](https://qlik.dev/apis/rest/roles).

### NEW API: Groups

You're now able to view groups within your tenant.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/groups" \
 -H "Authorization: Bearer <API-key>"
```

```shell
# Http 200 - Ok
{
  "data": [
   {
      "id": "603e591b00d28755ad41bd3b",
      "tenantId": "kg1knZuzosd7LR-CfvV7====tenantID",
      "createdAt": "2021-03-02T15:26:19.724Z",
      "lastUpdatedAt": "2021-03-02T15:26:19.724Z",
      "name": "Finance",
      "status": "active",
      "assignedRoles": [
        {
          "id": "60804cf8a77b649c66733f65",
          "name": "Developer",
          "type": "default",
          "level": "user"
        }
      ],
      "links": {
        "self": {
          "href": "https://your-tenant.us.qlikcloud.com/api/v1/groups/603e591b00d28755ad41bd3b"
        }
      }
    },
    ...
  ]
}
```

For the complete list of supported features, please see the [Groups API specifications](https://qlik.dev/apis/rest/groups).

### API DEPRECATIONS: Users

With the release of the new roles and groups APIs, a set of users features are being deprecated.
As of **November 1, 2022** they will no longer be available. Please ensure to follow the migrations to
avoid any downtime.

#### ENDPOINT: `GET /users/metadata`

Support for this endpoint is being removed. The role names can now be retrieved from
the [list roles endpoint](https://qlik.dev/apis/rest/roles#%23%2Fentries%2Froles-get).

#### ATTRIBUTE: `roles`

Support for `user.roles` is being removed and replaced with `user.assignedRoles`. Each assigned role reference
maps to an instance of a role object.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users/me" \
 -H "Authorization: Bearer <API-key>"
```

```shell
# Http 200 - Ok
{
  ...
  "roles": [
    "TenantAdmin",
    "Developer",
  ],
  "assignedRoles": [
    {
      "id": "60804cf8a77b649c66733f60",
      "name": "TenantAdmin",
      "type": "default",
      "level": "admin"
    },
    {
      "id": "60804cf8a77b649c66733f65",
      "name": "Developer",
      "type": "default",
      "level": "user"
    }
  ]
}
```

#### ATTRIBUTE: `created`, `lastUpdated`

The attributes `created` and `lastUpdated` are being renamed to `createdAt` and `lastUpdatedAt` respectively.

#### PATCH OPERATIONS & PATHS VALUES

Support for the operations `set`, `unset` and `add` are being removed. It's recommended to use the operation `replace`
for modifying the assigned roles.

Additionally, the path `/roles` is being deprecated in favor of using `/assignedRoles`

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users/123456789012345678901234" \
 -X PATCH \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '[
    {
      "op": "replace",
      "path": "/assignedRoles",
      "value": [
        { "id": "60804cf8a77b649c66733f60" },
        { "id": "60804cf8a77b649c66733f65" }
      ]
  ]'
```

```shell
# Http 204 - No Content
```

#### SORTING

Support for the sorting attributes `sortBy` and `sortOrder` is being removed and replaced with `sort`.
This query parameter can be prefixed with `+/-` to indicate the sort order.

**Examples**:

- `sort=+name`
- `sort=-name`
- `sort=name`

#### PAGINATION

The pagination query parameters `startingAfter` and `endingBefore` are being renamed to `next` and `prev` respectively.

#### QUERY PARAMETER: `tenantId`

The query parameter `tenantId` is no longer required and will default to the tenant being accessed.

#### QUERY PARAMETER: `subject`, `email`, `status`, `role`

These four user attributes are no longer supported as query parameters when querying users.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users?subject=1234567890&email=john.smith@corp.example&status=active" \
 -H "Authorization: Bearer <API-key>"
```

You can now perform the same query using the `filter` query parameter.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users?filter=subject eq "1234567890" and email eq "john.smith@corp.example" and status eq "active" \
 -H "Authorization: Bearer <API-key>"
```

For more complex filtering, you can optionally use the new filter endpoint.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users/actions/filter" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{
    "filter": "subject eq \"1234567890\""
  }'
```

For the complete list of supported features, please see the [Users API specifications](https://qlik.dev/apis/rest/users).
