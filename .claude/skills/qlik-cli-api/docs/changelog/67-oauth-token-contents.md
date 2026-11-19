---
source: https://qlik.dev/changelog/67-oauth-token-contents/
last_updated: 2023-11-29T15:53:15+01:00
---

# OAuth tokens no longer contain PII

The format for OAuth 2.0 access tokens issued by Qlik Cloud has changed to
remove private data about the access token for security purposes. With this
change access tokens no longer include information about the tenant or user.

Do not inspect access tokens. They are to be treated as opaque values. Qlik
Cloud access token format is not documented and is subject to change.

Client applications can use the access token to obtain data from Qlik Cloud
using published APIs. For example, the client can request user information from
the  `api/v1/users/me` endpoint with the access token.

For change purposes, here is the new format of the access token compared to the
old format.

### New format

```json
{
  "subType": "user",
  "purpose": "accessToken",
  "jti": "KF_xLCfjmaJJCNx0X4mT_oBsAfFiUb6g",
  "iat": 1701174495,
  "exp": 1701196095,
  "aud": "https://tenant.us.example.com",
  "iss": "qlik.api"
}
```

### Old format

```json
{
  "sub": "8o0raWkhGS6J9Psgu03j6av-hrffhhu1",
  "subType": "user",
  "tenantId": "J5XP4G7osoRlVjbj3oL_rYgZU3GAWmV6",
  "userId": "8o0raWkhGS6J9Psgu03j6av-hrffhhu1",
  "clientId": "45ab6571f94d9e6dc507ea976f67e780",
  "origin": "http://localhost:5000",
  "grantId": "64550d07a1c5c8c91f43c3a1",
  "scope": "user_default",
  "allowedLocations": [
    "header"
  ],
  "jti": "BF-Tl8CvHn6kFjUEttXDLp1Yhzu5wD7p",
  "iat": 1683295522,
  "exp": 1683317122,
  "aud": "https://tenant.us.example.com",
  "iss": "qlik.api"
}
```
