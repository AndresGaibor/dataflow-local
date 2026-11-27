---
title: "Review and assign roles to provisioned users in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-review-assign-entitlements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Provisioning users and groups using SCIM"]
---

# Review and assign roles to provisioned users in Qlik Cloud

Once the provisioning process is started in Microsoft Entra ID (formerly Azure) and a synchronization is complete, you can view the provisioned users and assign roles to groups of these users in Qlik Cloud.

Do the following:

1. Access the Administration [activity center](#glossary-0 "Glossary term") for your [tenant](#glossary-1 "Glossary term").
2. Go to Manage users and select the All users tab.
3. In the table, select Provisioned to show the provisioned users from Microsoft Entra ID.

   ![Select provisioned from users table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-entitlements-users-filter.png "Click to view full size")

   The users provisioned to Qlik Cloud are members of the group added in the Microsoft Entra ID configuration steps.
4. Optionally, select the Permissions tab to grant a set of permissions to the group of users.

   ![Add group on Permissions tab](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-entitlements-permissions_3.png "Click to view full size")
5. To assign a security role to a group, click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) to expand the role. Select the Groups tab and click Assign.

   ![Expanded role on Permissions tab](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-entitlements-permissions2.png "Click to view full size")
6. From the Assign groups dialog, search for the group to add, select the group, and then click Assign.

   The following example assigns all Bounty Hunters group members to the Analytics Admin role.

   ![Assign groups dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-entitlements-assign-groups.png "Click to view full size")

Now that SCIM and auto-provisioning have been configured, you can add, update, and remove Qlik Cloud users from a centralized provisioning console in Microsoft Entra ID.
