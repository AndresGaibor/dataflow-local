---
title: "Formkeep"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Formkeep.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Formkeep

Formkeep a cloud-based forms automation solution.

Formkeep integration replicates data using the [Formkeep API](https://support.formkeep.com/docs/do-you-have-any-api-documentation/).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your API token:

1. Log into your [Formkeep](https://formkeep.com/sign_in) account.
2. Open a form.
3. Navigate to the Reports tab.
4. Scroll down to JSON API Access.
5. Copy and paste your API token into a secured file.

To retrieve your form ID:

1. Log into your [Formkeep](https://formkeep.com/sign_in) account.
2. Open a form.
3. Navigate to the Form Settings tab.
4. In the Form ACTION Url field, locate your form ID after https://formkeep.com/f/.

   For example, in https://formkeep.com/f/001f217c2530, the ID is 001f217c2530.
5. Copy and paste your form ID into a secured file.

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
| Form IDs | Comma-separated list of form IDs to replicate. |
| API Token | API token. |
| Page Size | Number of submissions returned by a single request. Default number is set to 25. |

## Schema

Information note

Schemas and naming conventions can change from version to version. It is recommended to verify your version before continuing.

Depending on your destination, table and column names may not appear as they are outlined below.

### submissions

The `submissions` table contains information about submissions in your Formkeep account.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Primary Keys** | id |
| **Useful links** | [Formkeep method](https://support.formkeep.com/docs/do-you-have-any-api-documentation/ "Opens in new tab: Zoom API method") |
