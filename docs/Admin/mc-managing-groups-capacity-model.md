---
title: "Managing user groups"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-groups-capacity-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing users - Capacity-based subscriptions"]
---

# Managing user groups

User groups are essential for effective identity management, helping administrators streamline user permissions and maintain a secure, organized system. In Qlik Cloud, groups can be created directly in the Administration activity center or provisioned from an identity provider.

## Types of groups

There are two types of user groups:

- Identity provider (IdP) groups: These groups are sourced from an external identity provider and cannot be edited, deleted, or managed directly within Qlik Cloud. All management must be performed through the external identity provider. SCIM provisioning and synchronization only apply to IdP-managed groups. Custom groups in the tenant are not exposed through SCIM group endpoints and are not updated, deleted, or replaced by SCIM operations.
- Custom groups: These groups are created and managed within the Qlik Cloud tenant. Tenant administrators can create, edit, delete, and manage members of custom groups directly from the Administration activity center or via APIs. Both Qlik Account users and users provisioned from identity providers can be added to custom groups. Custom groups can be used together with IdP-managed groups, so a user can belong to groups synchronized from an identity provider and also belong to one or more custom groups in the tenant.

Custom groups are immediately available for use, while IdP groups are dynamically created in Qlik Cloud when a user associated with the group logs in for the first time. If you are using SCIM to provision users and groups, groups can be populated in advance. For more information, see [*Provisioning users and groups using SCIM*](auto-provisioning-using-SCIM.htm). You can view all groups in the Administration activity center.

In the Administration activity center, IdP-managed groups and custom groups appear together in the groups list. The user interface shows the group type with icons and labels, such as Managed (IdP) and Custom, so that you can distinguish between them.

IdP-managed groups and custom groups can have the same name because the group type distinguishes them. To avoid confusion, we recommend using unique group names when possible. For example, you can prefix custom group names with CG-.

Example of two groups with the same name but different icons: the first is an IdP group, and the second is a custom group.

![A screenshot of two groups with the same name but different icons.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_icons.png "Click to view full size")

Groups are labeled by type ("Managed (IdP)" and "Custom") in the Groups table.

![A screenshot of two groups with the same name, differentiated by type labels.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_labels.png "Click to view full size")

## Example scenarios for groups

You can use groups to manage access based on group memberships. Assign security roles and space roles to IdP groups and custom groups to control permissions across the tenant.

Information note

Users can belong to both IdP-managed groups and custom groups at the same time. These group types work independently. SCIM synchronization only manages IdP-managed groups and does not affect custom groups.

Below are some example scenarios of using IdP groups and custom groups:

### Example: Custom group for a software development project

If your organization is launching a new software development project, you can create a custom group specifically for the project team. This will allow you to assign project-specific roles and permissions, ensuring each team member has the access needed to collaborate effectively

### Example: IdP group for marketing team

Suppose you work in the marketing department of an organization that integrates with an external identity provider. You can create an IdP group for the marketing team that grants unique permissions to access essential tools and resources. When a new member joins the team and is added to the IdP group, they automatically receive the correct permissions in Qlik Cloud, allowing them to start working without delays.

### Example: Custom groups for access control based on user responsibilities

To efficiently manage access, create custom groups based on the tasks or responsibilities that users perform in different spaces. These user responsibilities help assign appropriate permissions within Qlik Cloud and ensure each user has access to what they need for their work.

1. Establish clearly defined user responsibilities (for example, developer, tester, owner, and user) in each space.

   The table shows user responsibilities in different spaces. User1 is developer in the Sales space and tester in the Operations space.

   ![Table with users and corresponding roles in different spaces.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_user_roles.png "Click to view full size")
2. Create custom groups for each user responsibility. Assign space roles, such as Can view or Can contribute, to the groups to match the level of access required in the space.

   Custom groups are created to manage access in shared and managed spaces. For example, the Sales-Developer group needs the Can view and Can contribute roles in the Sales space, and the Operations-Tester group needs the Can view role in the Operations space.

   ![Table with groups and corresponding group permissions in shared and managed spaces.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_group_roles.png "Click to view full size")
3. Map users to the appropriate custom groups based on their responsibilities in each space. For example, User1 may be a developer in the Sales space but a tester in the Operations space, with different permissions assigned for each responsibility.

   Users are assigned to the different groups based on their responsibilities. User1 is a member of both the Sales-Developer and Operations-Tester groups.

   ![A screenshot of four expanded groups with different users assigned to them.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_example.png "Click to view full size")

This structured approach simplifies permission management, making it easier to scale and adapt to your organization’s needs.

## Managing access permissions for groups

Permissions for group members are controlled by their assigned roles, regardless of whether the groups are IdP-provided or custom-created. When a role is assigned to a group, all members inherit the permissions associated with that role.

If users have roles assigned both individually and through group memberships, they might end up with duplicate role assignments. To completely remove a role from users, ensure you unassign it from both the Permissions > Users tab and the Permissions > Groups tab.

In cases where a user has different roles assigned individually and through group membership within a space, the higher permission level takes precedence.

For instructions on assigning tenant-wide roles to a group, see [*Assigning security roles and custom roles*](SaaS-roles-capacity-model.htm). For more information about space roles, see:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)
- [*Data space roles and permissions*](../DataIntegration/DataSpaces/permissions-data-space.htm)

## Listing group members

Tenant administrators can view the members of both IdP groups and custom groups.

On the Groups tab, IdP-managed groups and custom groups appear together in the list. The user interface shows the group type with labels so that you can distinguish between them.

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Groups tab, find the group by scrolling through the list or using the search feature.
3. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) next to the group to expand the list of members.

## Creating custom groups

Tenant administrators can create custom groups. Members can be added either during creation or at a later time.

To create multiple groups at once, you can use qlik-cli or APIs.

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Groups tab, click Create new.
3. Enter a name for the group.

   The Create group dialog.

   ![A screenshot of the Create group dialog.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_create.png "Click to view full size")

   Tip note

   You can create a custom group with the same name as an existing IdP-managed group, but not another custom group with the same name. To avoid confusion, use a clear naming convention when possible, such as adding CG- at the start of custom group names.
4. Optionally, add a description.
5. To add members to the group:

   1. Search for users by name or email.
   2. Select users to add them to the group.
6. Click Create.

After creating the group, go to the Permissions tab to assign roles that will grant permissions to group members.

## Adding or removing members of a custom group

As a tenant administrator, you can add or remove members from custom groups. Users can be added from both Qlik Account and other identity providers.

Information note

You cannot add or remove IdP-managed group memberships within Qlik Cloud. To manage these groups, use your external identity provider.

Users can belong to both IdP-managed groups and custom groups at the same time. If SCIM synchronization updates a user's IdP-managed group memberships, the user's custom group memberships are not changed.

### Adding or removing members

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Groups tab, find the group you want to manage.
3. Click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) to expand the list of group members.
4. To add members:

   1. Click Assign.
   2. Search for and select the users you want to add.

      The Assign users dialog.

      ![A screenshot of the Assign users to group dialog.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_add.png "Click to view full size")
   3. Click Assign.
5. To remove members:

   1. Use the search field to find specific users.

      The expanded details of a group.

      ![A screenshot of an expanded group on the groups tab with a member selected.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_custom_groups_remove.png "Click to view full size")
   2. Select the users you want to remove.
   3. Click Unassign.
   4. Confirm the action to remove the selected members.

## Editing group details

Tenant administrators can modify a group's name and description.

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Groups tab, find the group you want to edit.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
4. In the Edit group dialog, modify the group's name or description as needed.
5. Click Save to apply your changes.

## Deleting custom groups

Tenant administrators can delete custom groups only if they have no assigned members. Before deleting a group, make sure all members are unassigned.

To delete multiple groups at once, you can use qlik-cli or APIs.

Do the following:

1. In the Administration activity center, go to Manage users.
2. On the Groups tab, find the group that you want to delete.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Delete.
4. Confirm the deletion.

Information note

You cannot delete IdP groups directly within Qlik Cloud. To remove an IdP group that is no longer in use:

1. Delete the group in your external identity provider. This ensures the group is no longer being synchronized.
2. Clean up the group in Qlik Cloud using qlik-cli or APIs, as deleting it from the IdP does not automatically remove it from Qlik Cloud.

For more information, see:

- [Manage groups](https://qlik.dev/manage/manage-groups/#delete-a-group)
- [REST API: Groups](https://qlik.dev/apis/rest/groups/#delete-v1-groups-groupId)
- [qlik-cli: Group](https://qlik.dev/toolkits/qlik-cli/group/group-rm/)
