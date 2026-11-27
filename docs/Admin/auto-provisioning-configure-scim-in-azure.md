---
title: "Configuring SCIM provisioning in Microsoft Entra ID for Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/auto-provisioning-configure-scim-in-azure.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Provisioning users and groups using SCIM"]
---

# Configuring SCIM provisioning in Microsoft Entra ID for Qlik Cloud

After [configuring Qlik Cloud for SCIM](auto-provisioning-configure-qlik-cloud-for-scim.htm), you must configure SCIM provisioning in Microsoft Entra ID (formerly Azure AD).

## Microsoft Entra ID requirements for SCIM

- Microsoft Entra ID with a P1 subscription or higher (formerly Microsoft Azure Active Directory P1)
- Access to Microsoft Azure Portal and permissions to create enterprise applications for your Microsoft Entra ID.
- Two separate applications in the enterprise application registry in your Microsoft Entra ID.

## Microsoft Entra ID configuration steps for SCIM provisioning

Do the following:

1. Navigate to the Microsoft Entra ID admin center at [entra.microsoft.com](https://entra.microsoft.com/).
2. Go to Identity > Applications > Enterprise applications.

   ![Azure Active Directory admin center](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-microsoft-entra-admin-center.png "Click to view full size")

   Alternatively, if you enter from the general Azure portal, select Enterprise applications from the Microsoft Entra ID menu.

   ![Azure portal](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-portal.png "Click to view full size")
3. Click + New application to set up the provisioning application.
4. From the Browse Microsoft Entra ID Gallery page, click + Create your own application.
5. From the Create your own application dialog, enter a name for the provisioning application and select Integrate any other application you don't find in the gallery.

   ![Create your own application dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-microsoft-entra-create-application.png "Click to view full size")
6. Click Create.
7. To configure the provisioning process, from the Overview page, select Provisioning from the Manage section.

   ![Overview page](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-microsoft-entra-overview-page.png "Click to view full size")
8. Select Automatic from the menu. After making this selection, the configuration screens appear.
9. Begin the configuration by completing the Admin Credentials.

   - Paste the [tenant](#glossary-0 "Glossary term") URL obtained when you enabled auto-provisioning in Qlik Cloud.
   - Paste the token to the Secret Token box.
   - Click Test Connection.

   ![Automatic provisioning mode](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-microsoft-entra-provisioning-mode-automatic.png "Click to view full size")

   Information noteThe hostname is not the Qlik Cloud tenant alias. The hostname is the default name given to the Qlik Cloud tenant when it is created
10. Select Mappings and click Provision Microsoft Entra ID Users to configure the auto-provisioning service to work with your Qlik Cloud tenant.
11. Qlik Cloud requires a specific set of attributes to synchronize users from Microsoft Entra ID, as shown below.

    ![Attribute mapping](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-mappings-attribute-user2.png "Click to view full size")

    The way SCIM works between Qlik Cloud and Microsoft Entra ID is to match the user's email address (mail) first to provision and synchronize any changes associated with the user's group membership or access to Qlik Cloud.

    Information noteThe UserPrincipalName attribute can be used instead of the mail attribute if the UserPrincipalName is a valid email address and is the same as the value in the email attribute sent during user authentication.

    The following steps configure user attribute mappings.

    1. In the top section of the attribute mappings, keep all the default [selections](#glossary-1 "Glossary term").

       ![Attribute mapping](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-microsoft-entra-attribute-mapping-default.png "Click to view full size")
    2. In the Attribute Mappings section, delete all the attributes except for the following:

       - userPrincipalName
       - mail
       - Switch([IsSoftDeleted], , "False", "True", "True", "False")
       - Join(" ", [givenName], [surname])
       - mailNickname

       If these attributes are not deleted, the provisioning and synchronization flows between Qlik Cloud and Microsoft Entra ID will fail

       ![Attribute mappings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-attribute-mappings.png "Click to view full size")
    3. Click userPrincipalName to open the attribute configuration.
    4. In the userPrincipalName Attribute Configuration dialog, set the Source attribute to objectId and the Matching precedence value to 2.

       Click Ok to save the changes.

       ![userPrincipalName Attribute Configuration dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-attribute-mapping-type.png "Click to view full size")
    5. Click mail to open the Attribute Configuration dialog.
    6. In the mail Attribute Configuration dialog, set the Match objects using this attribute to Yes and the Matching precedence value to 1.

       Click Ok to save the changes.
    7. Click mailNickname to open the attribute configuration.
    8. In the mailNickname Attribute Configuration dialog, set the Source attribute to objectId.

       Click Ok to save the changes.
    9. Upon completing these steps, the Attribute Mappings section looks like this:

       ![Attribute Mappings completed](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-attribute-mapping-completed.png "Click to view full size")

       If the UserPrincipalName attribute is a valid email address, the mappings should instead look like this:

       ![Attribute Mappings completed](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-attribute-mapping-completed-userPrincipalName.png "Click to view full size")
    10. Click Save at the top of the configuration page to apply the changes.
12. You might receive a message explaining the changes require a complete resynchronization. Assuming this is the initial configuration for SCIM with Qlik Cloud, click Yes.

    The attribute mapping configuration is now complete.
13. The following steps add users and groups to provision from Microsoft Entra ID to Qlik Cloud.

    1. Click Users and groups under the Manage section of the provisioning or application menus.

       ![Overview page](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-overview-users.png "Click to view full size")
    2. The Users and Groups table displays. Click Add user/group to add an assignment.
    3. In the Add Assignment dialog, click None Selected to add users and groups.

       The Users and groups dialog displays.
    4. Search and add users and groups to be provisioned through this dialog. In this example, the Bounty Hunters group is selected.

       ![Users and groups dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-users-groups-bounty-hunters.png "Click to view full size")

       Click Select to confirm the selection.
    5. If you're adding a group, the Add Assignment dialog displays a warning that explains only users directly added to the group will be provisioned. Microsoft Entra ID and SCIM provisioning doesn't support cascading nested groups.
    6. Click Assign to add the group to the provisioning application.

       The group now displays in the Users and groups section of the provisioning application.

       ![Users and groups section in the provisioning application](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-users-groups-section.png "Click to view full size")
14. To enable auto-provisioning, go to the Overview page for the provisioning section of the application and click Start provisioning.

    Information noteProvisioning might take a few minutes to several hours to complete during the first provisioning task depending on the number of users and groups being provisioned. This is a limitation of the SCIM provisioning capability.
15. Refresh the page in the browser. If the provisioning process has still not run, click Provision on demand from the menu.

    ![Provision on demand](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-provisioning-on-demand.png "Click to view full size")
16. Once the provisioning process has run, the Overview page updates on a page refresh in the browser and shows the status.

    ![Current cycle status](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-provisioning-status.png "Click to view full size")
17. To review the synchronization, click View provisioning logs to see more detail.

    ![Provisioning logs](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scim-config-azure-provisioning-logs.png "Click to view full size")

## Updating the SCIM token

When your SCIM token expires, you must manually renew it in Qlik Cloud. Then add the new token to your Admin Credentials of your provisioning in the Microsoft Entra admin center.

Do the following:

1. On the Overview page, click Edit provisioning.
2. In Admin Credentials, paste the new token to the Secret Token box, then click Save.

## Best practices for using SCIM between Qlik Cloud and Microsoft Entra ID

- One of the benefits of SCIM provisioning with Microsoft Entra ID is that it allows administrators to control which groups that have access to a target application, such as Qlik Cloud. It is recommended to add only the groups that represent the users and use cases you need, gradually over time. This approach makes Qlik Cloud access control easier to manage.
- Be prepared for SCIM provisioning to take an extended amount of time to synchronize users and groups during a provisioning job. The time it takes depends on the number of users and groups you add to the application in Microsoft Entra ID.
- If you're going to provision a large number of users to Qlik Cloud, consider adding a group to the application containing the large number of users so that you don't have to add each user to the application manually.

Information noteMicrosoft Entra ID provisioning using SCIM does not support provisioning users who are members of nested groups.
