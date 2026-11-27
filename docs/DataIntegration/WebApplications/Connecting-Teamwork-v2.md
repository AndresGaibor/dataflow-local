---
title: "Teamwork"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Teamwork-v2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Teamwork

Teamwork is a team project management solution.

Teamwork integration replicates data using the [Teamwork API](https://apidocs.teamwork.com/docs/teamwork).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API key:

1. Log into your [Teamwork](https://www.teamwork.com/launchpad/login/?continue=%2Flaunchpad%2Fwelcome) account.
2. Click your profile icon in the main navigation menu.
3. Navigate to Settings > API Keys.
4. Copy and paste your API key into a secured file.

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
| Subdomain | You can find your subdomain in the URL of your Teamwork account. If the URL is my-teamwork-site.teamwork.com, the subdomain is my-teamwork-site. |
| API Key | API key. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### collaborators

The `collaborators` table contains info about the collaborators in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/spaces/v1/collaborators/get-v1-spaces-space-id-pages-page-id-collaborators-json) |

### companies

The `companies` table contains info about the companies in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/companies/get-v2-companies-json) |

### company

The `company` table contains info about the company in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/companies/get-v2-companies-id-json) |

### customers

The `customers` table contains info about the customers in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/customers/get-v2-customers-json) |

### customer

The `customer` table contains info about the customer in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/customers/get-v2-search-customers-json) |

### inboxes

The `inboxes` table contains info about the inboxes in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/inboxes/get-v2-inboxes-json) |

### milestones

The `milestones` table contains info about the milestones in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/teamwork/v3/milestones/get-projects-api-v3-milestones-json) |

### notebooks

The `notebooks` table contains info about the notebooks in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/teamwork/v3/notebooks/get-projects-api-v3-notebooks-json) |

### pages

The `pages` table contains info about the pages in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/spaces/v1/pages/head-v1-pages-page-id-json) |

### projects

The `projects` table contains info about the projects in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/teamwork/v3/projects/get-projects-api-v3-projects-json) |

### spaces

The `spaces` table contains info about the spaces in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/spaces/v1/spaces/get-v1-spaces-json) |

### tags

The `tags` table contains info about the tags in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/spaces/v1/tags/get-v1-tags-json) |

### tasks

The `tasks` table contains info about the tasks in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/teamwork/v3/tasks/get-projects-api-v3-projects-project-id-tasks-json) |

### ticket\_details

The `ticket_details` table contains info about the tickets in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/tickets/get-v2-search-tickets-json) |

### ticket\_priorities

The `ticket_priorities` table contains info about the priorities in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/ticket-priorities/get-v2-ticketpriorities-json) |

### ticket\_search

The `ticket_search` table contains info about the tickets in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/tickets/get-v2-search-tickets-json) |

### ticket\_types

The `ticket_types` table contains info about the types in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/ticket-types/get-v2-tickettypes-json) |

### tickets

The `tickets` table contains info about the tickets in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/desk/v2/tickets/post-v2-installations-installation-id-tickets-id-recover-json) |

### users

The `users` table contains info about the users in your Teamwork account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Teamwork documentation](https://apidocs.teamwork.com/docs/spaces/v1/users/get-v1-users-json) |
