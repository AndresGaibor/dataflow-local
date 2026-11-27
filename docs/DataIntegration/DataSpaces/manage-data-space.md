---
title: "Managing spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataSpaces/manage-data-space.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Working in spaces in Data Integration"]
---

# Managing spaces

To manage a space, you must be a tenant admin, a data admin, or the space owner. Members of the space who have the Can manage role can also manage the space.

Information noteWhen you create a space, you are automatically assigned the Is owner role. See [*Data space roles and permissions*](permissions-data-space.htm) for details about roles and permissions.

Information noteIf your organization has a Qlik Talend Cloud Premium or Enterprise subscription, you can organize spaces into environments and synchronize them with Talend Cloud. For more information, see [*Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions*](../../Admin/synchronized-resources.htm).

## Creating a space

If you are a tenant admin or data admin, you can create a space:

- From the Administration activity center on the Spaces page.
- From the Qlik Talend Data Integration home.

  If you are a non-admin user with space creator role, you can create spaces from the Qlik Talend Data Integration Home.

## Managing spaces

You can manage a space in Data Integration home by selecting the space in the filter at the top of Pipeline projects or Connections, and then clicking Space settings.

To make any changes in the space you must be either of:

- Tenant admin
- Data admin
- Owner of the space
- Member of the space with the Can manage role

The following options are available:

- Rename

  You can rename the space or change the description.
- Details

  You can view details of the space and edit members and connections.
- Members

  When a space is first created, only the user who creates the space is a member of the space. To allow other users access to the space and resources inside the space, add members to the space and assign them roles that give them permissions on the space and resources in the space.
- Connections

  You can view and edit connections that are created in the space.

  [*Managing data connections for administrators*](../../Admin/mc-administer-data-connections.htm)
- Gateway agents

  You can view Data Movement gateways created in the space.

  [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm)
- Notifications

  You can view and edit settings for notifications for the space.

  [*Setting notifications for a data space*](../Introduction/Notifications.htm#Setting2)
- Delete

  You can delete the space.

Tip noteYou can also manage spaces in the Spaces section of the Administration activity center.

## Adding members to spaces

You can add and remove space members, and you can change or remove their roles.

If groups are allowed in the tenant, you can add groups of members to your space. If a space member has individual permissions and group permissions in a space, the highest permission level is applied

Do the following:

1. In the space, click Space settings and select Members.
2. Click Add members.
3. Search for users or groups by name and select the members you want to add to the space.
4. Select permissions for the new members and click Add.

You can also add all users as members to a space to easily share content with everyone in the tenant. For example, if you have resources that should be generally available, you can store them in a space that anyone has access to.

Do the following:

1. In the space, click Space settings and select Members.
2. Click Add members.
3. Select permissions in the dropdown list next to Anyone at <your tenant name>.
4. Click Done.

## Requesting access to spaces via a data product

When datasets stored in spaces to which you do not have access are in a data product, you can request access from the space owner or the space manager.

Once the access is granted, you have access to the entire space. Depending on your role, you may have access to resources beyond the dataset from which you have requested the access.

For more information, see [*Requesting access to spaces*](../DataProducts/Requesting-space-access.htm).

## Changing a space owner

Only the tenant admin and the data admin can change the space owner. This can only be done fromAdministration.

Do the following:

1. From the Spaces section of Administration, click Change owner.
2. In the Change owner window, search for a user by name, email, subject, or user ID.
3. Click Apply.

Related learning:

- [Differentiate and manage Qlik Cloud spaces](/lnk/Differentiate_manage_spaces)
- [Administer and allocate space roles in Qlik Cloud](/lnk/Administer_allocate_space_roles)
