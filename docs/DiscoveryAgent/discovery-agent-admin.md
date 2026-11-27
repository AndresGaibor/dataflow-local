---
title: "Administering Discovery Agent"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/discovery-agent-admin.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Discovery Agent"]
---

# Administering Discovery Agent

Expand/Collapse all

# Administering Discovery Agent

Administering the [Discovery Agent](#glossary-0 "Glossary term") involves:

- Activating it by enabling cross-region inference.
- Setting permissions for users to work with [insight triggers](#glossary-1 "Glossary term") and to access [feeds](#glossary-2 "Glossary term"). Some permissions can be configured both by [tenant administrators](#glossary-3 "Glossary term") and users, and others are configured by tenant administrators only.

Information note

Discovery Agent tenant-level permissions are turned off by default in the default permissions. To activate Discovery Agent, administrators can either enable the Discovery Agent permissions in the default permissions or assign them to specific users through a custom role. Using a custom role allows administrators to grant access based on specific use cases.

To learn more about these permissions, see [*Discovery Agent permissions*](#Permissions).

## Activating Discovery Agent

To activate Discovery Agent, cross-region inference needs to be enabled for the Qlik Cloud tenant. Cross-region inference authorizes the tenant to send some data temporarily to other Qlik Cloud regions for generative AI interactions.

Enabling cross-region inference is done by a tenant administrator.

For more information, see [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm).

## Discovery Agent permissions

To work with Discovery Agent, you need:

- [*Administrator-assigned permissions*](#AdminAssigned)
- [*Space permissions*](#Space)

### Administrator-assigned permissions

Administrator-assigned permissions

The following administrator-assigned permissions are required depending on the action. Tenant administrators set these permissions by using default permissions and custom security roles.

- To create and manage insight triggers, the user needs the Insight triggers permission set to Allowed. This permission is available under Content types > Applications.
- To explore and act upon insights in the feed, the user needs the Insights feed permission set to Allowed. This permission is available under Features and actions > Agentic AI.

For more information, see:

- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)
- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users.htm) (user-based subscriptions)
- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users-anonymous.htm) (Qlik Anonymous Access subscriptions)

A list of all available default permissions and custom role permissions can be found at:

- [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
- [*Default permissions and custom roles*](../Admin/permissions-scopes.htm) (user-based subscriptions)
- [*Default permissions and custom roles*](../Admin/permissions-scopes-anonymous.htm) (Qlik Anonymous Access subscriptions)

Information noteIf you are creating insight triggers in your personal space, you need the Private Analytics Content Creator role assigned to you as well. This is assigned by a tenant administrator.

Information noteTenant administrators can view insight triggers and all feed insights without additional permissions. They can also create and manage insight triggers in apps they own by adding themselves to the space.

### Space permissions

The following sections outline the permissions needed in spaces for working with insight triggers and feeds. These permissions are required in addition to the corresponding [*Administrator-assigned permissions*](#AdminAssigned).

Shared space permissions

Professional users

Discovery Agent actions by role in shared spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-4 "Glossary term") in the application | Yes | Yes | Yes | Yes | No | No |
| View [insight triggers](#glossary-5 "Glossary term") in the application | Yes | Yes | Yes | Yes | Yes | No |
| View insights from the application in your feed | Yes | Yes | Yes | Yes | Yes | No |

Analyzers

Discovery Agent actions by role in shared spaces – Analyzer users

| Action | Owner (Space) | Can manage | Can edit data in applications | Can edit | Can view | Can consume data |
| --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-6 "Glossary term") in the application | Yes | Yes | Yes | Yes | No | No |
| View [insight triggers](#glossary-7 "Glossary term") in the application | Yes | Yes | Yes | Yes | No | No |
| View insights from the application in your feed | Yes | Yes | Yes | Yes | Yes | No |

Administrators

Tenant and analytics administrator Discovery Agent actions in a shared space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create and manage [insight triggers](#glossary-8 "Glossary term") in the application | No |
| View [insight triggers](#glossary-9 "Glossary term") in the application | Yes |
| View insights from the application in your feed | Yes |

Managed space permissions

Professional users

Discovery Agent actions by role in managed spaces – Professional and capacity-based subscription users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-10 "Glossary term") in the application | Yes | Yes | No | No | No | No | No | No |
| View [insight triggers](#glossary-11 "Glossary term") in the application | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| View insights from the application in your feed | Yes | Yes | No | Yes | Yes | Yes | No | Yes |

Analyzers

Discovery Agent actions by role in managed spaces – Analyzer users

| Action | Owner (Space) | Can manage | Can publish | Can contribute | Can view | Has restricted view | Can consume data | Can operate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create and manage [insight triggers](#glossary-12 "Glossary term") in the application | No | No | No | No | No | No | No | No |
| View [insight triggers](#glossary-13 "Glossary term") in the application | Yes | Yes | No | Yes | Yes | Yes | No | Yes |
| View insights from the application in your feed | Yes | Yes | No | Yes | Yes | Yes | No | Yes |

Administrators

Tenant and analytics administrator Discovery Agent actions in a managed space

| Action | Tenant and analytics admin supported |
| --- | --- |
| Create and manage [insight triggers](#glossary-14 "Glossary term") in the application | No |
| View [insight triggers](#glossary-15 "Glossary term") in the application | Yes |
| View insights from the application in your feed | Yes |

### Permissions for exploring Discovery Agent insights in Qlik Answers

User permissions for exploring insights in Qlik Answers are governed by Qlik Answers permissions, as well as the permissions for Discovery Agent.

For more information about permissions for Qlik Answers, see [*Qlik Answers access and permissions*](../QlikAnswers/qlik-answers-permissions.htm).
