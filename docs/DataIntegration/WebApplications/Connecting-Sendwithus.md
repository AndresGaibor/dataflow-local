---
title: "Sendwithus"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Sendwithus.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Sendwithus

Sendwithus is a transactional email management platform that allows teams to design, manage, and send email templates.

Sendwithus integration replicates data using the [Sendwithus API](https://support.sendwithus.com/api/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with a Sendwithus API key.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To create an API key:

1. Log into your [Sendwithus](https://app.sendwithus.com/login) account.
2. Navigate to Technical > API Settings.
3. Click Create New API Key.
4. Enter a description for the key.
5. Copy and paste your API key into a secured file.

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

## Schema

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### drip\_campaigns

The `drip_campaigns` table contains information about drip campaigns configured in your Sendwithus account.

|  |  |
| --- | --- |
| **Replication Method** | Full Table |
| **Primary Key** | id |
| **Useful links** | [Sendwithus API reference](https://support.sendwithus.com/api/#getalistofcampaigns "Opens in new tab: Sendwithus API reference") |

### log\_events

The `log_events` table contains events associated with a specific email log entry.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | log\_id, status, created |
| **Useful links** | [Sendwithus API reference](https://support.sendwithus.com/api/#retrieveeventsforaspecificlog_id. "Opens in new tab: Sendwithus API reference") |

### logs

The `logs` table contains email send log entries for your Sendwithus account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Sendwithus API reference](https://support.sendwithus.com/api/#logsapi "Opens in new tab: Sendwithus API reference") |

### snippets

The `snippets` table contains reusable content snippets defined in your Sendwithus account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Sendwithus API reference](https://support.sendwithus.com/api/#getallsnippets "Opens in new tab: Sendwithus API reference") |

### templates

The `templates` table contains email templates defined in your Sendwithus account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Key** | id |
| **Useful links** | [Sendwithus API reference](https://support.sendwithus.com/api/#getalistoftemplates "Opens in new tab: Sendwithus API reference") |
