---
source: https://qlik.dev/changelog/23-qlik-cli-update/
last_updated: 2025-07-08T16:09:30Z
---

# qlik-cli 2.14.3 released

## 2.14.3

- New: Commands have been updated to reflect the latest API changes.

New API: [Users](https://qlik.dev/apis/rest/users)

Updated: [Spaces](https://qlik.dev/apis/rest/spaces)

Updated: [Collections](https://qlik.dev/apis/rest/collections)

- New: OAuth 2.0 machine-to-machine support. Users are now able to authorize
  with Qlik Cloud SaaS over client credentials flow.

- New: Added command for tenant creation.

`qlik tenant create`
Note: This only works with specific entitlements
such as an active subscription with the multiple tenants entitlement.

- New: Added commands for web-integrations management.
  Web-integrations enable users to manage whitelisted origins that
  can make requests to a specified tenant (CORS).

```bash
qlik web-integration create --name myAllowList --validOrigins "https://www.google.com"
# returns a web-integration id
{
  "created": "...",
  "createdBy": "***********mSUL6MIzchD_",
  "id": "DSghcTBrzTkJBCN53IjQatRUWIJkvbno",
  "lastUpdated": "...",
  "name": "myQllowList",
  "tenantId": "**********PMZOEbLC9z52Op_G",
  "validOrigins": [ "https://www.google.com" ]
}
```

- New: Added commands for groups and roles management.

```bash
qlik role ls | jq '.[] | select(.name | contains("AnalyticsAdmin"))'
# returns object with role permission for AnalyticsAdmin
{
  "createdAt": "...",
  "description": "...",
  "id": "********36af85d",
  "lastUpdatedAt": "...",
  "level": "admin",
  "name": "AnalyticsAdmin",
  "permissions": [...]
}
qlik group ls
# fetch existing groups
[
  {
    "createdAt": "...",
    "id": "*********df6c8fc0b36c",
    "lastUpdatedAt": "...",
    "name": "Administrators",
    "status": "active",
    "tenantId": "*****OVEWVPMZOEbLC9z52Op_G"
  },
  ...
]
```

To update to new version, use the command
`qlik update`

previous version updates:

### 2.13.0

- Fix: Added qlik-cli to User-Agent header
- Fix: Creating IdP of type JWTAuth now works
  `identity-provider create jwtauth`

Click to view full
[changelog updates](https://github.com/qlik-oss/qlik-cli/blob/master/CHANGELOG.md#2143)
