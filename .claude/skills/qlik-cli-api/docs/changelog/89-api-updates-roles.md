---
source: https://qlik.dev/changelog/89-api-updates-roles/
last_updated: 2025-07-08T16:09:30Z
---

# API updates - Roles

Qlik is announcing a change in behavior for
the [Roles API](https://qlik.dev/apis/rest/roles/). This API
currently returns a list of all available roles on the tenant,
and a change is being made to who can access this API.

As of **April 9, 2024**, only users assigned the Tenant Admin role will be able to
access the roles API. All other users will be denied access with a `http 403` error.

**How to access role information for non-Tenant Admin users**

Today, any user can retrieve role records as shown below. Once
the change is made, any user without the `TenantAdmin` role
will receive a `http 403` forbidden response.

```shell
curl "https://<TENANT>/api/v1/roles" \
 -H "Authorization: Bearer <ACCESS_TOKEN>"
```

```shell
# Http 200 - Ok
{
    "data": [
        {
            "id": "<ROLE_ID>",
            "tenantId": "<TENANT_ID>",
            "name": "<ROLE_NAME>",
        },
        ...
    ],
    "links": {
        "self": {
          "href": "https://<TENANT>/api/v1/roles"
        }
    }
}
```

Although users without the Tenant Admin role will not be able to return all roles in the tenant,
they remain able to list the roles that they are assigned either directly, or via group membership.
They can do this via the `/api/v1/users/me` endpoint.

```shell
curl "https://<TENANT>/api/v1/users/me?fields=assignedGroups,assignedRoles" \
 -H "Authorization: Bearer <ACCESS_TOKEN>"
```

```shell
# Http 200 - Ok
{
  "id": "<USER_ID>",
  "assignedRoles": [
      {
        "id": "<ROLE_ID>",
        "name": "<ROLE_NAME>",
        "type": "default",
        "level": "user"
      },
      ...
  ],
  "assignedGroups": [
    {
      "id": "<GROUP_ID>",
      "name": "<GROUP_NAME>",
      "assignedRoles": [
        {
          "id": "<ROLE_ID>",
          "name": "<ROLE_NAME>",
          "type": "default",
          "level": "user"
        },
        ...
      ]
    },
    ...
  ],
  "links": {
      "self": {
        "href": "https://<TENANT>/api/v1/users/me?fields=assignedGroups,assignedRoles"
      }
  }
}
```
