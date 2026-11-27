---
title: "Iterable Preview"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Iterable-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Iterable  [Preview](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/feature-preview-program-overview.htm)

Iterable is a cross-channel customer engagement platform for marketing teams, providing campaign management, customer journey orchestration, email, SMS, and push messaging, and engagement analytics.

Iterable integration replicates data using the [Iterable API](https://api.iterable.com/api/docs).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To set up your Iterable account, you need:

- An Iterable project hosted in Iterable's US Data Center (USDC). The European Data Center (EDC) is not supported.
- An Iterable user account with the Org Admin role or the Manage Integrations project permission.

To create an API key:

1. Log into your [Iterable](https://app.iterable.com) account.
2. Navigate to Integrations > API Keys.
3. Click New API Key.
4. Enter a descriptive name, for example QlikDataIntegration.
5. For Key type, select Server-side. Do not select Read-only, Mobile, JavaScript, or any JWT-enabled variant — those key types are not supported by the connector.
6. Click Create.

   Copy and paste the API key into a secured file.

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
| Iterable API Key | API key. |
| Window in Days | The sliding-window size, in days, used when paginating Iterable's data export endpoint for high-volume engagement streams. Lower values shorten each request but increase the total number of requests; higher values reduce the number of requests but each takes longer. Default: 30. |

## Limitations and considerations

- **Server-side API key only.** Read-only, Mobile, JavaScript, and JWT-enabled API keys are not supported. A Read-only Server-side key passes initial connection validation but cannot access Iterable's data export API, so syncs of the `email_*` and `users` streams will fail.
- The API key is validated when the connection is saved. If the key has insufficient permissions, has been disabled, or was created in a different Iterable data center, connection creation fails with an authentication error.
- **Data export rate limit.** Iterable's data export API — used by the `email_*` and `users` streams — applies a limit of 4 requests per minute per project, compared to 100 requests per second for standard resource endpoints. The Window in Days setting controls how many data-export requests are issued per sync: a 1-year backfill at the default 30-day window produces approximately 12 requests per affected stream and fits within the limit, whereas very small window values produce significantly more requests and may exceed the export rate limit.
- Rate-limit responses (`HTTP 429`) and transient server errors (`5xx`) are retried automatically with exponential backoff. Authentication errors (`401`) and validation errors (`400`) are surfaced immediately and fail the sync.
- **Renamed fields in `users`.** Two user-profile fields are renamed to avoid case-normalization collisions at the destination: `Industry` is emitted as `_industry`, and the nested field `offers.Intro APR` is emitted as `_offers.intro APR`. This applies only to these two fields in the `users` stream.
- **`list_users` is a thin membership view.** Each record contains only `email`, `listId`, and a synthetic `updatedAt` timestamp set to the time the sync ran. It does not include user profile fields. To get full user data, sync the `users` stream and join on `email`.
- **`templates` re-reads all records on every sync.** The Iterable templates API does not support server-side filtering by `updatedAt`, so the connector retrieves all templates on every sync and applies the bookmark filter client-side. Sync time for this stream does not decrease as the bookmark advances.
- Start Date sets the initial bookmark for the eleven incremental streams only. Once a stream has advanced past Start Date, subsequent syncs resume from the saved bookmark. Changing Start Date in the connection settings does not affect records already replicated.

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### campaigns

The `campaigns` table contains information about campaigns in your Iterable project.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updatedAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#campaigns_campaigns "Opens in new tab: Iterable API reference") |

### channels

The `channels` table contains information about messaging channels configured in your Iterable project.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#channels_channels "Opens in new tab: Iterable API reference") |

### email\_bounce

The `email_bounce` table contains email bounce events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_click

The `email_click` table contains email click events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_complaint

The `email_complaint` table contains email spam complaint events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_open

The `email_open` table contains email open events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_send

The `email_send` table contains email send events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_send\_skip

The `email_send_skip` table contains events where an email send was skipped due to suppression rules or other filters in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_subscribe

The `email_subscribe` table contains email subscribe events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### email\_unsubscribe

The `email_unsubscribe` table contains email unsubscribe events recorded in your Iterable project. Records are append-only events with no primary key.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | createdAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |

### list\_users

The `list_users` table contains user membership records for each list in your Iterable project. This is a child stream of [lists](#lists). See the Limitations section for details on the fields available in this stream.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | email, listId |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#lists_getUsers "Opens in new tab: Iterable API reference") |

### lists

The `lists` table contains subscription lists defined in your Iterable project. The [list\_users](#list-users) stream is a child of this stream.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#lists_getLists "Opens in new tab: Iterable API reference") |

### message\_types

The `message_types` table contains message type configurations defined in your Iterable project.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#messageTypes_getMessageTypes "Opens in new tab: Iterable API reference") |

### metadata

The `metadata` table contains project-level metadata key-value pairs stored in your Iterable project.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | key |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#metadata_list "Opens in new tab: Iterable API reference") |

### templates

The `templates` table contains email and message templates created in your Iterable project.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | templateId |
| **Replication Key** | updatedAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#templates_getTemplates "Opens in new tab: Iterable API reference") |

### users

The `users` table contains user profiles stored in your Iterable project.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | email |
| **Replication Key** | profileUpdatedAt |
| **Useful links** | [Iterable API reference](https://api.iterable.com/api/docs#export_exportDataJson "Opens in new tab: Iterable API reference") |
