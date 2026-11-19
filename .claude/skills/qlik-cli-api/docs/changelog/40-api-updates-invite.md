---
source: https://qlik.dev/changelog/40-api-updates-invite/
last_updated: 2025-07-08T16:09:30Z
---

# New users API endpoint - Invite

### Users API - Invite

The Users API provides you with the ability to create, manage, and delete users
from Qlik Cloud tenants. Previously, you were only able to add existing Qlik
Cloud users to the tenant using
a POST request to [`users`](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers-post) with
a valid user `subject`.

The new endpoint at [`/v1/users/actions/invite`](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers%2Factions%2Finvite-post)
supports the addition of new and existing users to your tenant using the
email address of the new user.

Users new to Qlik Cloud will receive an email inviting them to register a Qlik
Account, and existing users will be prompted to log in with their existing Qlik
Account credentials.

> **Note:** Inviting only works for Qlik Account logins. If you are using your
> own Identity Provider and wish to pre-load users into the tenant, you should
> leverage Qlik Cloud [SCIM capabilities](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-configure-qlik-cloud-for-scim.htm)
> or send a [POST request](https://qlik.dev/apis/rest/users/#%23%2Fentries%2Fv1%2Fusers-post) with
> the desired `subject` to create the user.

- `POST/v1/users/actions/invite` : Invites one or more users to Qlik Cloud using their email.

```bash
curl "https://your-tenant.us.qlikcloud.com/api/v1/users/actions/invite" \
 -X POST \
 -H "Authorization: Bearer <API-key>" \
 -H "Content-type: application/json" \
 -d '{"invitees":[{"name":"John Smith","email":"john.smith@example.com","resend":true,"language":"en"}]}'
```

See full API reference [here](https://qlik.dev/apis/rest/users).
