---
title: "Configuring Qlik Cloud for SCIM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-configure-qlik-cloud-for-scim.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Provisioning users and groups using SCIM"]
---

# Configuring Qlik Cloud for SCIM

The first step in provisioning users and groups using SCIM is to configure Qlik Cloud.

## Qlik Cloud requirements for SCIM

- A Qlik Cloud [tenant](#glossary-0 "Glossary term") with the “Bring your own Identity Provider” entitlement.
- Tenant admin access to the Qlik Cloud Administration activity center.
- An active interactive identity provider configuration for Microsoft Entra ID (formerly Azure AD) in your Qlik Cloud tenant. For more information, see [How To: Configure Qlik Sense Enterprise SaaS to use Azure AD as an IdP](https://community.qlik.com/t5/Official-Support-Articles/How-To-Configure-Qlik-Sense-Enterprise-SaaS-to-use-Azure-AD-as/ta-p/1704442).

## Qlik Cloud configuration steps for SCIM

Do the following:

1. Open your Qlik Cloud Administration [activity center](#glossary-1 "Glossary term") by clicking ![Qlik Sense SaaS navigation menu. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg) > Administration > Identity provider.

   ![Select Administration from the navigation menu and select Identity provider](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-qlik-cloud-launcher-rev.png)
2. Click ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) for the Microsoft Entra ID configuration and select Manage auto provisioning.

   ![Select Manage auto provisioning from the More menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-qlik-cloud-more.png "Click to view full size")
3. Click Enable to retrieve the configuration information to supply to Microsoft Entra ID.

   ![Enable Manage auto provisioning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-qlik-cloud-manage-auto-provisioning.png "Click to view full size")
4. The access token to allow Microsoft Entra ID to perform provisioning jobs on your tenant and the URL for your Qlik Cloud tenant displays. Click Copy and close.

   ![Copy access token](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-qlik-cloud-copy-token.png "Click to view full size")
5. Paste the copied content from the clipboard to a text editor for later use.
