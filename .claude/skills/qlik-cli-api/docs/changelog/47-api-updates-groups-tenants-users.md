---
source: https://qlik.dev/changelog/47-api-updates-groups-tenants-users/
last_updated: 2025-07-08T16:09:30Z
---

# API Updates - Groups, Tenants & Users

To support customers who wish to manage their users, groups, and tenants via API, Qlik is releasing new and updated APIs
to support common tasks such as:

- Setting the tenant name or tenant alias
- Updating tenant auto assignment flags for new users joining the tenant
- Patching assigned roles by name to users and groups. Previously this could only be done for users, and required the
  use of the role ID
- Seeding groups to the tenant to set up access control prior to user logins. This is important when using Identity
  Providers other than Azure AD configured with SCIM

There are also important updates to group validation checks that any organization using groups via their Identity
Provider should review.

### New tenants endpoints

You're now able to read and patch information about your tenant.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/tenants/xxxxx-xxxxx-xxxxxxxxxxxxxxxxxxxx" \
 -H "Authorization: Bearer <dev-api-key>"
```

```shell
# Http 200 - Ok
{
  "id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "status": "active",
  "name": "1234567890abcde",
  "hostnames": [
    "1234567890abcde.us.qlikcloud.com",
    "your-tenant-alias.us.qlikcloud.com"
  ],
  "createdByUser": "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
  "created": "2020-10-01T17:58:14.846Z",
  "lastUpdated": "2023-03-23T13:25:12.107Z",
  "autoAssignCreateSharedSpacesRoleToProfessionals": true,
  "autoAssignPrivateAnalyticsContentCreatorRoleToProfessionals": true,
  "autoAssignDataServicesContributorRoleToProfessionals": true,
  "enableAnalyticCreation": false,
  "datacenter": "us-east-1",
  "links": {
    "self": {
      "href": "https://your-tenant-alias.us.qlikcloud.com/api/v1/tenants/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  }
}
```

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/tenants/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
 -X PATCH \
 -H "Authorization: Bearer <dev-api-key>" \
 -H "Content-type: application/json" \
 -d '[
    {
      "op": "replace",
      "path": "/name",
      "value": "Your Tenant Name"
    }
  ]'
```

```shell
# Http 204 - No Content
```

For the complete list of supported features, see the [Tenants API specifications](https://qlik.dev/apis/rest/tenants).

### New users API feature

You're now able to create or patch users with assigned roles by name, instead of by role ID.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users" \
 -X POST \
 -H "Authorization: Bearer <api-dev-key>" \
 -H "Content-type: application/json" \
 -d '{
      "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "subject": "my/subject",
      "name": "New Username",
      "email": "username@test.example",
      "assignedRoles": [
        { "name": "TenantAdmin" },
        { "name": "Developer" }
      ]
  }'
```

```shell
# Http 201 - Created
{
    "id": "6478e42bce55a79191a3ce8e",
    "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "status": "active",
    "subject": "my/subject",
    "name": "New Username",
    "email": "username@test.example",
    "assignedRoles": [
        {
            "id": "6478e405b3558e25bf22bfaf",
            "name": "TenantAdmin",
            "type": "default",
            "level": "admin"
        },
        {
            "id": "6478e405b3558e25bf22bfb6",
            "name": "Developer",
            "type": "default",
            "level": "user"
        }
    ],
    "assignedGroups": [],
    "groups": [],
    "createdAt": "2023-06-01T18:32:11.509Z",
    "lastUpdatedAt": "2023-06-01T18:32:11.509Z",
    "links": {
        "self": {
            "href": "https://your-tenant.us.qlikcloud.com/api/v1/users/6478e42bce55a79191a3ce8e"
        }
    }
}
```

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/users/6478e42bce55a79191a3ce8e" \
 -X PATCH \
 -H "Authorization: Bearer <api-dev-key>" \
 -H "Content-type: application/json" \
 -d '[
    {
      "op": "replace",
      "path": "/assignedRoles",
      "value": [
        { "name": "TenantAdmin" },
        { "name": "Developer" }
      ]
    }
  ]'
```

```shell
# Http 204 - No Content
```

For the complete list of supported features, see the [Users API specifications](https://qlik.dev/apis/rest/users).

### New groups endpoints

You're now able to create and patch information about your groups. This includes the ability to assign roles by name
or by ID.  Creation of groups is supported through the API for pre-seeding access to resources and role assignment prior
to user login. Assignment of users to groups continues to be managed by your identity provider.

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/groups" \
 -X POST \
 -H "Authorization: Bearer <api-dev-key>" \
 -H "Content-type: application/json" \
 -d '{
      "name": "admin group",
      "assignedRoles": [
          { "name": "TenantAdmin" }
      ]
  }'
```

```shell
# Http 201 - Created
{
    "id": "6478e535b778a912a1d543e6",
    "tenantId": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "createdAt": "2023-06-01T18:36:37.871Z",
    "lastUpdatedAt": "2023-06-01T18:36:37.871Z",
    "name": "admin group",
    "status": "active",
    "assignedRoles": [
        {
            "id": "6478e4b071aaa7f293fd71b0",
            "name": "TenantAdmin",
            "type": "default",
            "level": "admin"
        }
    ],
    "links": {
        "self": {
            "href": "https://your-tenant.us.qlikcloud.com/api/v1/groups/6478e535b778a912a1d543e6"
        }
    }
}
```

```shell
curl "https://your-tenant.us.qlikcloud.com/api/v1/groups/6478e535b778a912a1d543e6" \
 -X PATCH \
 -H "Authorization: Bearer <api-dev-key>" \
 -H "Content-type: application/json" \
 -d '[
    {
      "op": "replace",
      "path": "/assignedRoles",
      "value": [
        { "name": "TenantAdmin" },
        { "name": "Developer" }
      ]
    }
  ]'
```

```shell
# Http 204 - No Content
```

For the complete list of supported features, see the [Groups API specifications](https://qlik.dev/apis/rest/groups).

### Group validation updates

#### Maximum name length

Qlik Cloud now limits the length of group names to 256 characters. New groups with names that exceed the
character limit will not be created in the tenant. Any pre-existing groups within Qlik Cloud are unaffected
by this change.

Users attempting to log in with a group that exceeds the name length limit will be permitted but the new group
will be ignored.

#### Maximum number of groups per tenant

Qlik Cloud now limits each tenant to `10,000` active groups. Upon reaching the limit, no new groups can be created
in the tenant until existing groups are removed by an administrator.

Users attempting to log in with a new group that exceeds the maximum number of groups limit will be permitted but
the new group will be ignored.
