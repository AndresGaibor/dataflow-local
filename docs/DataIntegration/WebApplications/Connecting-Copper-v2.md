---
title: "Copper"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Copper-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Copper

Copper is a customer relationship management app.

Copper integration replicates data using the [Copper API](https://developer.copper.com/introduction/authentication.html#api-keys).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To generate an API key:

1. Log into your [Copper](https://app.copper.com/users/sign_in) account.
2. Navigate to System Settings > API Keys > Generate API Key.
3. Copy and paste your API key into a secured file.

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
| User Email | User email. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### account

The `account` table contains info about the account in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/account-and-users/fetch-account-details.html) |

### activities\_search

The `activities_search` table contains info about the activities in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/activities/list-activities-search.html) |

### companies

The `companies` table contains info about the companies in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/companies/list-companies-search.html) |

### contact\_types

The `contact_types` table contains info about the contact types in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/people/list-contact-types.html) |

### custom\_field\_definitions

The `custom_field_definitions` table contains info about the account specific fields in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/custom-fields/general/list-custom-field-definitions.html) |

### customer\_sources

The `customer_sources` table contains info about the customer sources in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/leads/list-customer-sources.html) |

### lead\_statuses

The `lead_statuses` table contains info about the lead statuses in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/leads/list-lead-statuses.html) |

### leads

The `leads` table contains info about the leads in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/leads/list-leads-search.html) |

### loss\_reasons

The `loss_reasons` table contains info about the leads in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/opportunities/list-loss-reasons.html) |

### opportunities

The `opportunities` table contains info about the opportunities in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/opportunities/list-opportunities-search.html) |

### people

The `people` table contains info about the people in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/people/list-people-search.html) |

### pipeline\_stages

The `pipeline_stages` table contains info about the positions of opportunities within their pipelines in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/opportunities/list-pipeline-stages.html) |

### pipelines

The `pipelines` table contains info about the list of pipelines in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/opportunities/list-pipelines.html) |

### projects

The `projects` table contains info about the projects in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/projects/list-projects-search.html) |

### tags

The `tags` table contains info about the tags in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | name |
| **Useful links** | [Copper documentation](https://developer.copper.com/tags/list-tags.html) |

### tasks

The `tasks` table contains info about the tasks in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/tasks/list-tasks-search.html) |

### users

The `users` table contains info about the users in your Copper account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Copper documentation](https://developer.copper.com/account-and-users/list-users.html) |
