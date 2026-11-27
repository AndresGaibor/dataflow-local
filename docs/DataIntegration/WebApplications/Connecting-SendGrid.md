---
title: "SendGrid Core"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SendGrid.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# SendGrid Core

SendGrid (now part of Twilio) is a cloud-based email delivery and marketing platform.

SendGrid Core integration replicates data using the [SendGrid v3 API](https://www.twilio.com/docs/sendgrid/api-reference).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with a SendGrid API key.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your SendGrid account, you need:

- An active SendGrid account with API access enabled.
- Permission to create API keys in your SendGrid account (Administrator role, or a Restricted Access role with the required permissions already assigned).

To create an API key:

1. Log into your [SendGrid](https://login.sendgrid.com/login/identifier) account.
2. Navigate to Settings > API Keys > Create API Key.
3. Enter a name for the key, for example QlikDataIntegration.
4. Select Restricted Access to limit the key to only the required permissions.
5. Expand the permission categories and grant Read Access to the following:
   - Suppressions — required to replicate `blocks`, `bounces`, `invalids`, `spam_reports`, `global_suppressions`, `groups_all`, and `groups_members`.
   - Marketing Campaigns — required to replicate `contacts`, `lists_all`, `lists_members`, `segments_all`, `segments_members`, and `campaigns`.
   - Template Engine — required to replicate `templates_all`.
6. Click Create & View.
7. Copy and paste your API key into a secured file.

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
| API Key | API key. |

## Limitations and considerations

- An API key cannot be granted greater permissions than your own account's current permissions. If you have a Restricted Access role in SendGrid, you can only include permissions already assigned to your account.
- Custom contact fields defined in your SendGrid account appear as records inside the `custom_fields` array on each contact, not as separate top-level columns. Adding new custom contact fields does not require a destination schema reset.
- The `groups_members`, `lists_members`, and `segments_members` streams use `member_count` as the replication key. Each sync fetches member data only for groups, lists, or segments whose member count has increased since the last run. Membership changes that leave the count unchanged (for example, one member removed and another added) are not detected.
- The `groups_members` stream replicates suppressed (unsubscribed) email addresses for each unsubscribe group.
- This connector uses the Legacy Marketing Campaigns API endpoints (`/v3/contactdb/`). Accounts that have only ever used the newer Twilio SendGrid Marketing Campaigns (Single Sends) may find these endpoints unavailable or empty.

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### blocks

The `blocks` table contains information about email addresses that were blocked from receiving emails.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | end\_time |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/blocks-api "Opens in new tab: SendGrid API reference") |

### bounces

The `bounces` table contains information about email addresses that have bounced.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | end\_time |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/bounces-api "Opens in new tab: SendGrid API reference") |

### campaigns

The `campaigns` table contains information about email campaigns in your SendGrid account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/campaigns-api "Opens in new tab: SendGrid API reference") |

### contacts

The `contacts` table contains information about recipients in your SendGrid contact database.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | created\_at, updated\_at |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/contacts "Opens in new tab: SendGrid API reference") |

### global\_suppressions

The `global_suppressions` table contains email addresses that have globally unsubscribed from all emails.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | end\_time |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-global-suppressions "Opens in new tab: SendGrid API reference") |

### groups\_all

The `groups_all` table contains information about unsubscribe groups in your SendGrid account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-unsubscribe-groups "Opens in new tab: SendGrid API reference") |

### groups\_members

The `groups_members` table contains suppressed (unsubscribed) email addresses for each unsubscribe group.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | member\_count |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/suppressions-suppressions "Opens in new tab: SendGrid API reference") |

### invalids

The `invalids` table contains invalid email addresses that cannot receive mail.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | end\_time |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/invalid-emails-api "Opens in new tab: SendGrid API reference") |

### lists\_all

The `lists_all` table contains information about contact lists in your SendGrid account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/lists "Opens in new tab: SendGrid API reference") |

### lists\_members

The `lists_members` table contains contact recipients that belong to a contact list.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | member\_count |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/lists "Opens in new tab: SendGrid API reference") |

### segments\_all

The `segments_all` table contains information about contact segments in your SendGrid account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/segmenting-contacts "Opens in new tab: SendGrid API reference") |

### segments\_members

The `segments_members` table contains contact recipients that belong to a contact segment.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | member\_count |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/segmenting-contacts "Opens in new tab: SendGrid API reference") |

### spam\_reports

The `spam_reports` table contains email addresses that have marked your emails as spam.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | end\_time |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/spam-reports-api "Opens in new tab: SendGrid API reference") |

### templates\_all

The `templates_all` table contains information about email templates in your SendGrid account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [SendGrid API reference](https://www.twilio.com/docs/sendgrid/api-reference/transactional-templates "Opens in new tab: SendGrid API reference") |
