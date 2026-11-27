---
title: "Contentful"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Contentful.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Contentful

Contentful is a headless content management system (CMS) that enables teams to create, manage, and distribute content across digital channels.

Contentful integration replicates data using the [Contentful API](https://www.contentful.com/developers/docs/references/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API token:

1. Log into your [Contentful](https://be.contentful.com/login) account.
2. Navigate to Settings > API Keys > Add API Keys.
3. Enter a name for the API key. Optionally, select which environment (master or development) the key has access to.
4. Copy and paste your Content Delivery API - Access Token into a secured file.

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
| Space ID | Contentful space ID. |
| API Token | Content Delivery API access token. |

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### assets

The `assets` table contains media files and other assets in your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/assets/assets-collection/get-all-assets-of-a-space/console/curl "Opens in new tab: Contentful API reference") |

### content\_types

The `content_types` table contains the content models (types) defined in your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-types/content-type-collection/get-all-content-types-of-a-space/console/curl "Opens in new tab: Contentful API reference") |

### entries

The `entries` table contains the content entries in your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entries/entries-collection/get-all-entries-of-a-space/console/curl "Opens in new tab: Contentful API reference") |

### environment\_templates

The `environment_templates` table contains templates used to create environments in your Contentful organization.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/content-model-templates/get-all-environment-templates/get-all-environment-templates/console/curl "Opens in new tab: Contentful API reference") |

### environments

The `environments` table contains the environments within your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/environments/environment-collection/get-all-environments-of-a-space/console/curl "Opens in new tab: Contentful API reference") |

### locales

The `locales` table contains the locales configured in your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/locales/locale-collection/get-all-locales-of-a-space/console/curl "Opens in new tab: Contentful API reference") |

### organizations

The `organizations` table contains the organizations associated with your Contentful account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/organizations/organizations-collection/get-all-organizations-an-account-has-access-to/console/curl "Opens in new tab: Contentful API reference") |

### security\_contacts

The `security_contacts` table contains the security contacts for your Contentful organization. Admin or owner access is required to replicate this table.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/security-contacts/security-contacts-collection/get-an-organization-security-contacts-an-admin-or-owner-has-access-to/console/curl "Opens in new tab: Contentful API reference") |

### tags

The `tags` table contains the tags applied to content in your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/tags/tag-collection/get-all-tags/console/curl "Opens in new tab: Contentful API reference") |

### tasks

The `tasks` table contains the entry tasks assigned to users in your Contentful space.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/entry-tasks/assigned-tasks-collection/get-all-tasks-that-are-assigned-to-you/console/curl "Opens in new tab: Contentful API reference") |

### taxonomy\_concepts

The `taxonomy_concepts` table contains the taxonomy concepts used to organize content in your Contentful organization.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | sys.id |
| **Useful links** | [Contentful API reference](https://www.contentful.com/developers/docs/references/content-management-api/#/reference/taxonomy/concept-collection/get-concepts/console/curl "Opens in new tab: Contentful API reference") |
