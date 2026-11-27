---
title: "Recovering access to your tenant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/idp-recover.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# Recovering access to your tenant

If you lose access to your [tenant](#glossary-0 "Glossary term") due to an incorrect IdP configuration, you can use the recovery path to regain access. This fallback mechanism reverts authentication to the default Qlik Account.

Loss of access typically occurs due to changes on the IdP side, such as:

- Expiry of secrets used to integrate Qlik with your IdP.
- Deletion or misconfiguration of the IdP integration.

## Accessing the recovery path

For all tenants except those deployed in Qlik Cloud Government, the recovery path URL is: https://<tenantname>.<region>.qlikcloud.com/login/recover

The recovery path can be used by the following users:

- Service account owner: The user who created the tenant.

- Invited user: Any user invited to the tenant through Qlik Account.

If the user has the Tenant Admin role assigned, they can log in via the recovery path and reconfigure the IdP settings to restore access.

## Best practices for tenant recovery

To maintain secure recovery access, follow these guidelines:

- Regularly review users:

  - Remove inactive accounts, especially those originally invited via the Qlik Account IdP.
- Preserve tenant admin access:

  - Ensure the service account owner retains the Tenant Admin role.

    Information noteSee also: [Known limitation in Qlik Cloud Services: Account Owner should not be removed as tenant admin](https://community.qlik.com/t5/Support-Knowledge-Base/Known-limitation-in-Qlik-Cloud-Services-Account-Owner-should-not/ta-p/1717890/highlight/true "Known limitation in Qlik Cloud Services: Account Owner should not be removed as tenant admin").
  - If you change the service account owner, assign the Tenant Admin role to the new user.
  - Avoid unassigning the Tenant Admin role without designating an alternative administrator.
- Store the recovery address securely:

  - During the initial configuration of your Qlik Cloud deployment, you were prompted to save the tenant URL and recovery path. Ensure the recovery address is stored in a safe location.
