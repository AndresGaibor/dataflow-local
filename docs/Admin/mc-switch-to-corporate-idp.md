---
title: "Switching from Qlik Account to a corporate identity provider"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-switch-to-corporate-idp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# Switching from Qlik Account to a corporate identity provider

This topic covers transitioning from Qlik Account to a corporate identity provider (IdP), including considerations for email matching and handling Section Access tables.

## Important considerations

- Supported identity providers: Ensure your IdP supports either OpenID Connect (OIDC) or SAML protocols.
- Recovery address: Always use the recovery address when changing IdPs to prevent the risk of locking yourself out during the change. For more information, see [*Recovering access to your tenant*](idp-recover.htm).
- Deactivation or deletion of corporate IdP: Deactivating or deleting your corporate IdP configuration will revert your tenant back to Qlik Account. For more information, see [*Identity providers in Qlik Cloud*](mc-create-idp-configuration.htm#Deleting).

## Removing Section Access table before configuring the corporate IdP

Before switching to your corporate IdP, remove or comment out the Section Access table in all applications, and perform a reload. After activating the IdP, recreate the Section Access table using the new identities provided by the IdP. Perform another reload to reactivate the table in the data model.

For information, see [*Managing data security with Section Access*](../Scripting/Security/manage-security-with-section-access.htm).

## Managing content during IdP transition

Transitioning to a corporate IdP can disrupt user access and the content they own. To minimize this, ensure that users' email addresses remain consistent across the switch, as this will help retain their associated content. Pay close attention to mapping content for existing users to their new corporate identities.

## Configuring a new corporate IdP

Do the following:

1. Configure the interactive IdP in the Administration activity center, see [*Identity providers in Qlik Cloud*](mc-create-idp-configuration.htm).
2. Test the verification flow and ensure the result is successful. As a [tenant admin](#glossary-0 "Glossary term"), manually verify that the email and email\_verified claims are present and with a value of true. This is important for successfully mapping content after the switch. Do not activate the IdP yet.
3. Examine the Users list for the tenant via the Administration activity center.
4. Identify users whose current email address does not match the corporate email address. When you switch IdPs to preserve content, the email addresses should match.
5. For users who do not have a matching email address, the tenant admin needs to manually move content to the new account.
6. Again, check the user list via the Administration activity center and verify that the correct corporate email addresses are now assigned to all users.
7. Activate the interactive IdP.
8. Open a new browser instance or an incognito window, to avoid conflict with existing login sessions. Access the tenant URL (<tenant>.<region>.qlikcloud.com/login) and verify that it takes you to the new interactive IdP.
9. Log in and access the activity center. Verify that Qlik Account content remains available to the user.
10. Open the Administration activity center and verify that the user has the new IdP subject assigned to their existing User ID.
11. Verify that the license assignments in the Administration activity center are still set correctly for all the users who have logged into the new corporate IdP.
12. Recreate the Section Access tables, see [*Switching from Qlik Account to a corporate identity provider*](#Remove).
