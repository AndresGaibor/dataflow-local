---
title: "Harvest Forecast"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Harvest-Forecast.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Harvest Forecast

Harvest Forecast is a web-based project management and resource scheduling tool that helps teams plan, track, and allocate their people and time efficiently across multiple projects.

Harvest Forecast integration replicates data using the [Harvest Forecast Experimental API](https://help.getharvest.com/forecast/faqs/faq-list/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

You must have administrative privileges to create an OAuth2 App in your Harvest account.

To create your client ID and secret:

1. Log into your [Harvest](https://id.getharvest.com/sessions/new?go_back=%2Faccounts) account.
2. Go to the Developers tab.
3. In the new OAuth2 application section, specify the following requirements:
   - Name: Enter a name.
   - Redirect URL: Set it to https://connector.qlik.com/auth/oauth/v3.htm.
   - Access: Select the account from which you want to replicate data.
   - Products: Select the Harvest and Forecast products.
4. Click Create application.
5. Copy and paste your client ID and secret into a secured file.

To retrieve your account ID:

1. Log into your [Harvest](https://id.getharvest.com/sessions/new?go_back=%2Faccounts) account.
2. Go to the Developers tab.
3. Click Create new personal access token.
4. Enter a name for the token.
5. Copy and paste your account ID into a secured file.

## Creating the connection

For more information, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Provide a name for the connection in Connection name.
5. Select Open connection metadata to define metadata for the connection when it has been created.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | Select a Data Movement gateway if required by your use case.  Information note This field is not available with the Qlik Talend Cloud Starter subscription, as it does not support Data Movement gateway. If you have another subscription tier and do not want to use Data Movement gateway, select None.  For information on the benefits of Data Movement gateway and use cases that require it, see [*Qlik Data Gateway - Data Movement*](../../Gateways/replication-gateway.htm). |
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Account ID | Account ID. |
| Client ID | Client ID. |
| Client Secret | Client secret. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### assignments

The `assignments` table contains info about the assignments assigned to the people in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | Harvest Forecast documentation |

assignments table foreign keys

| Join assignments with | on |
| --- | --- |
| [clients](#clients) | ``` assignments.person_id = clients.updated_by_id ```  ``` assignments.updated_by_id = clients.updated_by_id ``` |
| [milestones](#milestones) | ``` assignments.person_id = milestones.updated_by_id ```  ``` assignments.updated_by_id = milestones.updated_by_id ```  ``` assignments.project_id = milestones.project_id ``` |
| [people](#people) | ``` assignments.person_id = people.id ```  ``` assignments.updated_by_id = people.id ```  ``` assignments.person_id = people.updated_by_id ```  ``` assignments.updated_by_id = people.updated_by_id ``` |
| [projects](#projects) | ``` assignments.person_id = projects.updated_by_id ```  ``` assignments.updated_by_id = projects.updated_by_id ```  ``` assignments.project_id = projects.id ``` |
| [placeholders](#placeholders) | ``` assignments.person_id = placeholders.updated_by_id ```  ``` assignments.updated_by_id = placeholders.updated_by_id ```  ``` assignments.placeholder_id = placeholders.id ``` |
| [roles](#roles) | ``` assignments.person_id = roles.updated_by_id ```  ``` assignments.updated_by_id = roles.updated_by_id ```  ``` assignments.placeholder_id = roles.placeholder_ids ``` |

assignments table schema

|  |
| --- |
| **active\_on\_days\_off**  BOOLEAN |
| **allocation**  INTEGER |
| **end\_date**  DATE-TIME |
| **id**  INTEGER |
| **notes**  STRING |
| **person\_id**  INTEGER |
| **placeholder\_id**  INTEGER |
| **project\_id**  INTEGER |
| **repeated\_assignment\_set\_id**  INTEGER |
| **start\_date**  DATE-TIME |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  INTEGER |

### clients

The `clients` table contains info about the clients in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | Harvest Forecast documentation |

clients table foreign keys

| Join clients with | on |
| --- | --- |
| [projects](#projects) | ``` clients.id = projects.client_id ```  ``` clients.updated_by_id = projects.updated_by_id ``` |
| [assignments](#assignments) | ``` clients.updated_by_id = assignments.person_id ```  ``` clients.updated_by_id = assignments.updated_by_id ``` |
| [milestones](#milestones) | ``` clients.updated_by_id = milestones.updated_by_id ``` |
| [people](#people) | ``` clients.updated_by_id = people.id ```  ``` clients.updated_by_id = people.updated_by_id ``` |
| [placeholders](#placeholders) | ``` clients.updated_by_id = placeholders.updated_by_id ``` |
| [roles](#roles) | ``` clients.updated_by_id = roles.updated_by_id ``` |

clients table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **harvest\_id**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  INTEGER |

### milestones

The `milestones` table contains info about the project milestones in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | Harvest Forecast documentation |

milestones table foreign keys

| Join milestones with | on |
| --- | --- |
| [assignments](#assignments) | ``` milestones.updated_by_id = assignments.person_id ```  ``` milestones.updated_by_id = assignments.updated_by_id ```  ``` milestones.project_id = assignments.project_id ``` |
| [clients](#clients) | ``` milestones.updated_by_id = clients.updated_by_id ``` |
| [people](#people) | ``` milestones.updated_by_id = people.id ```  ``` milestones.updated_by_id = people.updated_by_id ``` |
| [projects](#projects) | ``` milestones.updated_by_id = projects.updated_by_id ```  ``` milestones.project_id = projects.id ``` |
| [placeholders](#placeholders) | ``` milestones.updated_by_id = placeholders.updated_by_id ``` |
| [roles](#roles) | ``` milestones.updated_by_id = roles.updated_by_id ``` |

milestones table schema

|  |
| --- |
| **date**  DATE-TIME |
| **id**  INTEGER |
| **name**  STRING |
| **project\_id**  INTEGER |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  INTEGER |

### people

The `people` table contains info about the people in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | Harvest Forecast documentation |

people table foreign keys

| Join people with | on |
| --- | --- |
| [assignments](#assignments) | ``` people.id = assignments.person_id ```  ``` people.updated_by_id = assignments.person_id ```  ``` people.id = assignments.updated_by_id ```  ``` people.updated_by_id = assignments.updated_by_id ``` |
| [clients](#clients) | ``` people.id = clients.updated_by_id ```  ``` people.updated_by_id = clients.updated_by_id ``` |
| [milestones](#milestones) | ``` people.id = milestones.updated_by_id ```  ``` people.updated_by_id = milestones.updated_by_id ``` |
| [projects](#projects) | ``` people.id = projects.updated_by_id ```  ``` people.updated_by_id = projects.updated_by_id ``` |
| [placeholders](#placeholders) | ``` people.id = placeholders.updated_by_id ```  ``` people.updated_by_id = placeholders.updated_by_id ```  ``` people.roles = placeholders.roles ``` |
| [roles](#roles) | ``` people.id = roles.updated_by_id ```  ``` people.updated_by_id = roles.updated_by_id ```  ``` people.roles = roles.id ``` |

people table schema

|  |
| --- |
| **admin**  BOOLEAN |
| **archived**  BOOLEAN |
| **avatar\_url**  STRING |
| **color\_blind**  STRING |
| **email**  STRING |
| **first\_name**  STRING |
| **harvest\_user\_id**  INTEGER |
| **id**  INTEGER |
| **last\_name**  STRING |
| **login**  STRING |
| **personal\_feed\_token\_id**  INTEGER |
| **roles**  ARRAY This is a nested data structure. |
| **subscribed**  BOOLEAN |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  STRING |
| **weekly\_capacity**  INTEGER |
| **working\_days**  OBJECT This is a nested data structure:   - friday: BOOLEAN - monday: BOOLEAN - saturday: BOOLEAN - sunday: BOOLEAN - thursday: BOOLEAN - tuesday: BOOLEAN - wednesday: BOOLEAN |

### placeholders

The `placeholders` table contains info about the placeholders in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |

placeholders table foreign keys

| Join placeholders with | on |
| --- | --- |
| [assignments](#assignments) | ``` placeholders.updated_by_id = assignments.person_id ```  ``` placeholders.updated_by_id = assignments.updated_by_id ```  ``` placeholders.id = assignments.placeholder_id ``` |
| [clients](#clients) | ``` placeholders.updated_by_id = clients.updated_by_id ``` |
| [milestones](#milestones) | ``` placeholders.updated_by_id = milestones.updated_by_id ``` |
| [people](#people) | ``` placeholders.updated_by_id = people.id ```  ``` placeholders.updated_by_id = people.updated_by_id ```  ``` placeholders.roles = people.roles ``` |
| [projects](#projects) | ``` placeholders.updated_by_id = projects.updated_by_id ``` |
| [roles](#roles) | ``` placeholders.updated_by_id = roles.updated_by_id ```  ``` placeholders.id = roles.placeholder_ids ```  ``` placeholders.roles = roles.id ``` |

placeholders table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **id**  INTEGER |
| **name**  STRING |
| **roles**  ARRAY This is a nested data structure. |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  INTEGER |

### projects

The `projects` table contains info about the projects in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Replication Key** | updated\_at |
| **Useful links** | Harvest Forecast documentation |

projects table foreign keys

| Join projects with | on |
| --- | --- |
| [clients](#clients) | ``` projects.client_id = clients.id ```  ``` projects.updated_by_id = clients.updated_by_id ``` |
| [assignments](#assignments) | ``` projects.updated_by_id = assignments.person_id ```  ``` projects.updated_by_id = assignments.updated_by_id ```  ``` projects.id = assignments.project_id ``` |
| [milestones](#milestones) | ``` projects.updated_by_id = milestones.updated_by_id ```  ``` projects.id = milestones.project_id ``` |
| [people](#people) | ``` projects.updated_by_id = people.id ```  ``` projects.updated_by_id = people.updated_by_id ``` |
| [placeholders](#placeholders) | ``` projects.updated_by_id = placeholders.updated_by_id ``` |
| [roles](#roles) | ``` projects.updated_by_id = roles.updated_by_id ``` |

projects table schema

|  |
| --- |
| **archived**  BOOLEAN |
| **client\_id**  INTEGER |
| **code**  STRING |
| **color**  STRING |
| **end\_date**  DATE-TIME |
| **harvest\_id**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **notes**  STRING |
| **start\_date**  DATE-TIME |
| **tags**  ARRAY This is a nested data structure. |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  INTEGER |

### roles

The `roles` table contains info about the roles in your Harvest Forecast account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |

roles table foreign keys

| Join roles with | on |
| --- | --- |
| [assignments](#assignments) | ``` roles.updated_by_id = assignments.person_id ```  ``` roles.updated_by_id = assignments.updated_by_id ```  ``` roles.placeholder_ids = assignments.placeholder_id ``` |
| [clients](#clients) | ``` roles.updated_by_id = clients.updated_by_id ``` |
| [milestones](#milestones) | ``` roles.updated_by_id = milestones.updated_by_id ``` |
| [people](#people) | ``` roles.updated_by_id = people.id ```  ``` roles.updated_by_id = people.updated_by_id ```  ``` roles.id = people.roles ``` |
| [projects](#projects) | ``` roles.updated_by_id = projects.updated_by_id ``` |
| [placeholders](#placeholders) | ``` roles.updated_by_id = placeholders.updated_by_id ```  ``` roles.placeholder_ids = placeholders.id ```  ``` roles.id = placeholders.roles ``` |

roles table schema

|  |
| --- |
| **harvest\_role\_id**  INTEGER |
| **id**  INTEGER |
| **name**  STRING |
| **person\_ids**  ARRAY This is a nested data structure. |
| **placeholder\_ids**  ARRAY This is a nested data structure. |
| **updated\_at**  DATE-TIME |
| **updated\_by\_id**  INTEGER |
