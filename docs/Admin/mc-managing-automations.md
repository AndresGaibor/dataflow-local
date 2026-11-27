---
title: "Managing automations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-automations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud"]
---

# Managing automations

Automations run workflows across Qlik Cloud and connected services. In the Administration activity center, administrators can manage access, monitor automations, and manage automation owners and connections.

## Who can work with automations

Your permissions and the space where an automation is stored determine what you can do with automations.

### Administering automations

Tenant admins, analytics admins, and users with the Tenant Admin Automations permission can manage all automations in the tenant from the Administration activity center. They can enable and disable automations, change the space or owner, manage automation settings, and delete automations and connections.

### Creating and managing automations in personal spaces

To create and manage automations in your personal space, you must have the Private Automations permission.

Tenant admins can also manage automation templates.

By default, this permission is Allowed for all users. Tenant administrators can remove the permission from the default permissions and grant it to specific users or groups through a custom role.

Information noteDeprecated role: The Automation Creator role is deprecated and it will be removed in a future release. Avoid assigning it to users or groups. To replace it, use the Private automations permission in the default permissions or create a custom role. For more information, see [*Managing custom roles*](permissions-custom-roles-capacity-model.htm).

### Creating and managing automations in shared spaces

To create and manage automations in a shared space, you must have:

- The Shared Automations permission.
- The Can edit role in the shared space.

Tenant administrators can control the Shared Automations permission through the default permissions or custom roles.

### Related information

For information about creating automations, see [Qlik Automate](../../Sense_QlikAutomation/introduction/home-automation.htm).

For information about assigning permissions and roles, see [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm).

## Enabling individual automations

A tenant admin or analytics admin may need to disable automations to prevent rate limits from being exceeded.
Automations are enabled and disabled from the automations table view in the Administration activity center. When users create automations, they are enabled by default. You can enable and disable automations from the ![Three dots to expand menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu at the end of the automation row and select Enable or Disable.

When a tenant admin or analytics admin disables an automation, the automation owner will see a Disabled status on the automation overview page.

A disabled automation can be enabled by the tenant or analytics admin from the Administration activity center or by the automation owner from the automation overview page.
This means that the tenant or analytics admin cannot prevent the automation owner from re-enabling their automation.

Warning noteWhen an automation is re-enabled, you have the option of renewing the execution token. Renewing the execution token will break references to the automation that use a trigger URL or a Qlik Sense button object. Token renewal cannot be undone.

## Changing the owner of an automation

The tenant admin can change the owner of an automation from the Administration activity center. An OAuth bot user with the admin.automations scope can also change automation ownership programmatically. Changing the owner is useful when a user leaves the organization, when automations need to be transferred as part of a migration, or when the tenant admin needs to take control of an automation to prevent it from being re-enabled by the original owner.

To change the owner, click ![Three dots to show more options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Change owner.

When the tenant admin changes the owner, the automation is disabled and it will try to pick up the new owner's credentials for any relevant connection:

- Automations using internal (Qlik) connections will pick up the new credentials when the automation owner is changed.
- Automations that connect to other services will pick up the new credentials if the new owner has access to the space where the connection resides.
- Private connections will not work. These kind of connections need to be reconfigured in the individual block after a change of automation ownership.

If the new owner does not have the appropriate credentials, the automation needs to be manually reconfigured.

Warning noteWhen the automation is re-enabled after a change of ownership, you have the option of renewing the execution token. Renewing the execution token will break references to the automation that use a trigger URL or a Qlik Sense button object. Token renewal cannot be undone.

## Moving an automation from one space to another

The tenant admin or a user with Tenant Admin Automations permissions can move an automation from one space to another, regardless of their role in the space.

To move the automation, click ![Three dots to show more options](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), then select Move.

When an automation is moved to a new space, it will no longer be available in original space. All members of the new space will have access to the automation.

## Related topics

For information about monitoring automations, managing automation connections and templates, and managing automations programmatically, see:

- [*Monitoring automations*](mc-monitoring-automations.htm)
- [*Managing automation connections*](mc-managing-automation-connections.htm)
- [*Managing automations programmatically*](mc-managing-automations-programmatically.htm)
- [*Managing automation templates*](mc-managing-automation-templates.htm)
