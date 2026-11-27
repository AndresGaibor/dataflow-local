---
title: "Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/synchronized-resources.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud"]
---

# Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions

With a Qlik Talend Cloud subscription, selected resources are synchronized with Talend Cloud. Synchronization reduces duplicate setup and keeps configurations, permissions, and access consistent across both systems.

Information noteThis topic applies only to customers with a Qlik Talend Cloud subscription.

## Overview of synchronized resources

This section provides a high-level overview of the resources that are synchronized or shared between Qlik Cloud and Talend Cloud. For detailed rules and exceptions, see the topics listed below.

The following resources are synchronized:

- Users – Accounts are synchronized between both platforms according to specific rules.
- Roles and permissions – Talend roles and permissions are synchronized to Qlik Cloud and are visible in the Administration activity center.
- Environments – Environments are synchronized when created or updated in either system.
- Spaces – Spaces that are assigned to environments are synchronized between both platforms.
- Tenant encryption settings – The configuration in Qlik Cloud applies to both systems. If you rotate or remove encryption keys, the change affects both tenants.

In a synchronized setup, administrators can manage users, roles, environments, and spaces across both platforms. Qlik Cloud displays the combined set of users and roles for both Qlik and Talend. The Talend Management Console displays only the subset required for Talend services. Updates to environments and assigned spaces are synchronized in both directions, so changes in one system appear in the other.

For more information, see:

- [*Synchronizing users*](synchronized-resources-users.htm)
- [*Synchronizing roles and permissions*](synchronized-resources-roles.htm)
- [*Synchronizing and managing environments*](mc-administer-environments.htm)
- [*Tenant encryption*](../Introduction/tenant-encryption.htm)

### Synchronization actions by resource

The following tables provide an overview of how create, update, and delete actions are synchronized between Qlik Cloud and Talend Cloud.

#### Users

Synchronization of users

| Action | Qlik Cloud | Talend Cloud |
| --- | --- | --- |
| Create | Synced only if Talend role assigned | Creates user in Qlik if not existing |
| Update | Synced to Talend | Synced to Qlik |
| Delete | Deleted from both systems | Deleted from Talend only |

#### Roles and permissions

Synchronization of roles and permissions

| Action | Qlik Cloud | Talend Cloud |
| --- | --- | --- |
| Create | Synced to Talend | Synced to Qlik |
| Update | Synced to Talend | Synced to Qlik |
| Delete | Deleted from both systems | Deleted from both systems |

#### Environments

Synchronization of environments

| Action | Qlik Cloud | Talend Cloud |
| --- | --- | --- |
| Create | Synced to Talend | Synced to Qlik |
| Update | Synced to Talend | Synced to Qlik |
| Delete | Deleted from both systems | Deleted from both systems |

#### Spaces

Synchronization of data spaces and Talend spaces

| Action | Qlik Cloud | Talend Cloud |
| --- | --- | --- |
| Create | Synced if assigned to an environment | Synced to Qlik |
| Update | Synced to Talend | Synced to Qlik |
| Delete | Deleted from both systems | Deleted from both systems |

#### Space permissions

Synchronization of space permissions

| Action | Qlik Cloud | Talend Cloud |
| --- | --- | --- |
| Assign | Synced to Talend | Synced to Qlik |
| Edit | Synced to Talend | Synced to Qlik |
| Unassign | Synced to Talend | Synced to Qlik |

## What is not synchronized

Some resources are stored locally on their system and are not synchronized:

- Users

  - Users in Qlik Cloud without any Talend role are not synchronized.
  - Users deleted in Talend Cloud are not automatically deleted from Qlik Cloud.
  - User groups are not synchronized.
- Roles and permissions

  - Roles assigned to users through groups or the Auto assign option (rather than individually) are not synchronized.
- Spaces

  - Data spaces not assigned to an environment stay local to Qlik Cloud.
  - Content within data spaces and Talend spaces (such as files and datasets) is not synchronized.
  - Managed and shared spaces stay local to Qlik Cloud.
  - Group-based space permissions assigned in Qlik Cloud are not synchronized. Only individual user permissions are synchronized.
