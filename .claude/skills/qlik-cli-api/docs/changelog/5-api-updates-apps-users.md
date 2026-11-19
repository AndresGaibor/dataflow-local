---
source: https://qlik.dev/changelog/5-api-updates-apps-users/
last_updated: 2025-07-08T16:09:30Z
---

# SaaS API updates to Apps and Users APIs

## Engine REST API (Apps) updated with new attributes

The Engine REST API, aka Apps API, adds attributes for app name and description
for `POST` and `PUT` request operations related to publishing and republishing
Qlik Sense applications.

The new `checkOriginAppId` attribute is a true/false property validating that
the source Qlik Sense application has the same Id as the originally published
app.

```json
"attributes": {
  "name": "string",
  "description": "string"
},
"checkOriginAppId": true
```

For more information, see the API reference for republishing a Qlik Sense
application [here](https://qlik.dev/apis/rest/apps#%23%2Fentries%2Fapps%2F-appId%2Fpublish-put).

## Users API add attributes for user roles

As part of the ongoing work related to updates to users, groups, and roles in
the Users API added additional properties for setting roles
on users and new
roles that may be applied to user records. While this feature is not accessible
in product user interfaces, it does exist in the API. In addition, the Users API
is public/stable.

For more information, see the API
reference [here](https://qlik.dev/apis/rest/users#%23%2Fentries%2Fusers-post).
