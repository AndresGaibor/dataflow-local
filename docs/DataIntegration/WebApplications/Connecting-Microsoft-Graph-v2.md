---
title: "Microsoft Graph"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Microsoft-Graph-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Microsoft Graph

Microsoft Graph is the unified REST API gateway to data and intelligence in Microsoft 365, Windows, and Enterprise Mobility + Security. It provides access to users, groups, mail, calendars, contacts, files, Teams, audit logs, directory roles, conditional access policies, applications, and service principals across a Microsoft Entra ID tenant.

It replicates data using the [Microsoft Graph REST API](https://learn.microsoft.com/en-us/graph/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To connect to Microsoft Graph, you need:

- A Microsoft 365 tenant containing the data you want to replicate.
- An Azure subscription with access to the [Azure portal](https://portal.azure.com) or [Entra Admin Center](https://entra.microsoft.com).
- Permission to register applications and grant admin consent in your Microsoft Entra ID tenant (Global Administrator or Application Administrator role).
- A Microsoft 365 license that covers the resources you intend to replicate:
  - Mail, calendar, and contacts data requires a Microsoft 365 Business Basic license or higher on the underlying mailbox.
  - Sign-in and directory audit logs require Microsoft Entra ID P1 or P2.
  - Teams chat messages and channel messages are protected APIs and require Microsoft approval and a Microsoft 365 E5 license or an appropriate add-on.

To register a Microsoft Entra ID application and grant API permissions:

1. Log into your [Microsoft Entra admin center](https://entra.microsoft.com/).
2. Navigate to Entra ID > App registrations.
3. Click New registration.
4. Enter a name for the application (for example, QlikDataIntegration), select Accounts in this organizational directory only, and click Register.
5. On the application's Overview page, copy the Application (client) ID and the Directory (tenant) ID and paste them into a secured file.
6. Navigate to Certificates & secrets > Client secrets > New client secret.
7. Enter a description and expiration date, and click Add.

   Copy and paste the secret Value into a secured file.
8. Navigate to API permissions > Add a permission > Microsoft Graph > Application permissions.
9. Add the following permissions:

   | Permission | Streams enabled |
   | --- | --- |
   | `User.Read.All` | `users`, `calendar_events`, `contacts`, `drive_items`, `mail_messages` |
   | `Group.Read.All` | `groups`, `group_member`, `group_owner`, `teams`, `channels`, `team_member` |
   | `ChannelMessage.Read.All` | Optional. Required for Teams channel message reading (protected API). |
   | `Chat.Read.All` | `chats`, `chat_messages` (protected APIs) |
   | `Files.Read.All` | `drives`, `drive_items` |
   | `Mail.Read` | `mail_messages` |
   | `Calendars.Read` | `calendar_events` |
   | `Contacts.Read` | `contacts` |
   | `Application.Read.All` | `applications`, `service_principals` |
   | `AuditLog.Read.All` | `audit_logs_directory`, `audit_logs_signins` |
   | `Policy.Read.All` | `conditional_access_policies` |
   | `RoleManagement.Read.Directory` | `directory_roles`, `directory_role_templates`, `directory_role_member` |
10. Click Grant admin consent for [your organization] and confirm.

    All permissions must show a Granted status before the connector can access those resources.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Fill in the required connection properties.
2. Provide a name for the connection in Connection name.
3. Select Open connection metadata to define metadata for the connection when it has been created.
4. Click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Tenant ID | Directory (tenant) ID. |
| Client ID | Application (client) ID. |
| Client Secret | Client secret. |
| Scope | The OAuth scope sent to the Microsoft identity platform when requesting an access token. Use https://graph.microsoft.com/.default to grant access to all consented application permissions. |
| Page Size | Optional. The number of records returned per Microsoft Graph API request. Default: 999. Allowed range: 100–999. Lower values reduce the per-request payload size; higher values reduce the total number of API requests. |

## Limitations and considerations

- All streams use Full Table replication — the complete set of records is retrieved on every sync. The Start Date field is captured as part of the connection configuration but does not limit the records returned.
- Admin consent is required for every Microsoft Graph permission listed in the API permissions table. Permissions without admin consent result in `403 Forbidden` errors when the connector attempts to read those resources.
- The `teams` stream queries the `/groups` endpoint filtered by `resourceProvisioningOptions/Any(x:x eq 'Team')`. The `groups` stream returns all groups including non-Teams groups. Teams-scoped child streams (`channels`, `team_member`) iterate only over the filtered teams parent.
- Reading Teams chat messages (`chats`, `chat_messages`) requires the application to be approved through Microsoft's protected-API request process and a Microsoft 365 E5 license or equivalent add-on. For more information, see [Protected APIs in Microsoft Teams](https://learn.microsoft.com/en-us/graph/teams-protected-apis).
- Audit log data (`audit_logs_directory`, `audit_logs_signins`) is retained for 7 days on the free Entra ID tier and 30 days on P1 or P2. Records outside the retention window are not available for replication.
- Field names are normalized from camelCase to snake\_case during extraction. For example, `userPrincipalName` becomes `user_principal_name`.
- Rate limiting is handled automatically. On `HTTP 429 Too Many Requests` responses, the connector waits for the duration specified in the `Retry-After` header. Transient `5xx` responses are retried with exponential backoff for up to 6 attempts.

## Schema

Schemas and naming conventions can change between versions. Verify your schema version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### users

The `users` table contains information about users in your Microsoft Entra ID tenant.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/user-list) |

### applications

The `applications` table contains information about application registrations in your Microsoft Entra ID tenant.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/application-list) |

### service\_principals

The `service_principals` table contains information about service principals in your Microsoft Entra ID tenant.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/serviceprincipal-list) |

### groups

The `groups` table contains information about all groups (including Microsoft Teams groups) in your Microsoft Entra ID tenant.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/group-list) |

### group\_member

The `group_member` table contains information about the members of each group. This is a child stream of [groups](#groups).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, group\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/group-list-members) |

### group\_owner

The `group_owner` table contains information about the owners of each group. This is a child stream of [groups](#groups).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, group\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/group-list-owners) |

### teams

The `teams` table contains information about Microsoft Teams in your organization. Teams are retrieved as a filtered subset of groups (`$filter=resourceProvisioningOptions/Any(x:x eq 'Team')`).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/group-list) |

### channels

The `channels` table contains information about channels in each team. This is a child stream of [teams](#teams).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, team\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/channel-list) |

### team\_member

The `team_member` table contains information about the members of each team. This is a child stream of [teams](#teams).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, team\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/team-list-members) |

### chats

The `chats` table contains information about chats in Microsoft Teams. This is a protected API — see the Limitations section for access requirements.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/chat-list) |

### chat\_messages

The `chat_messages` table contains messages from each chat. This is a child stream of [chats](#chats). This is a protected API — see the Limitations section for access requirements.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, chat\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/chat-list-messages) |

### mail\_messages

The `mail_messages` table contains email messages for each user. This is a child stream of [users](#users). Requires a Microsoft 365 Business Basic license or higher on the underlying mailbox.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, user\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/user-list-messages) |

### calendar\_events

The `calendar_events` table contains calendar events for each user. This is a child stream of [users](#users). Requires a Microsoft 365 Business Basic license or higher on the underlying mailbox.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, user\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/user-list-events) |

### contacts

The `contacts` table contains contacts for each user. This is a child stream of [users](#users). Requires a Microsoft 365 Business Basic license or higher on the underlying mailbox.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, user\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/user-list-contacts) |

### drives

The `drives` table contains information about drives available in your organization.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/drive-list) |

### drive\_items

The `drive_items` table contains files and folders from each user's drive. This is a child stream of [users](#users).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, user\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/drive-list) |

### audit\_logs\_directory

The `audit_logs_directory` table contains directory audit log records. Requires Microsoft Entra ID P1 or P2 — see the Limitations section for retention details.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/directoryaudit-list) |

### audit\_logs\_signins

The `audit_logs_signins` table contains sign-in activity records. Requires Microsoft Entra ID P1 or P2 — see the Limitations section for retention details.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/signin-list) |

### conditional\_access\_policies

The `conditional_access_policies` table contains information about conditional access policies in your Microsoft Entra ID tenant.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/conditionalaccesspolicy-list) |

### directory\_roles

The `directory_roles` table contains information about directory roles that are activated in the Microsoft Entra ID tenant.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/directoryrole-list) |

### directory\_role\_templates

The `directory_role_templates` table contains information about directory role templates available in Microsoft Entra ID.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/directoryroletemplate-list) |

### directory\_role\_member

The `directory_role_member` table contains information about the members of each directory role. This is a child stream of [directory\_roles](#directory-roles).

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id, role\_id |
| **Useful links** | [Microsoft Graph documentation](https://learn.microsoft.com/en-us/graph/api/directoryrole-list-members) |
