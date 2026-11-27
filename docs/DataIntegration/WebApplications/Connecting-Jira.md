---
title: "Jira Cloud Platform"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Jira.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Jira Cloud Platform

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual. For new tasks, use the improved [*Jira*](Connecting-Jira-v2.htm) connector.

Jira is a cloud based platform that allows bug tracking and agile project management. You can use Jira Cloud Platform as a data source when landing or replicating data.

The following datasets are supported:

- Calculated Metrics
- Issue Fields (CDC is not supported)
- Issues
- Users (CDC is not supported)
- Groups (CDC is not supported)
- User Groups (CDC is not supported)
- Projects (CDC is not supported)

For more information about the API, see the [Atlassian documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#version).

This video provides an introduction to connecting to Jira.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your data, you need to authenticate the connection with your Jira Cloud Platform account credentials. Make sure that your credentials only contain ASCII characters. Your credentials are saved in the connection.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

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
| Domain | The domain name for your organisation.  Example: your-domain.atlassian.net |
| User email | Email address for your Atlassian account. |
| User API token | An API token for your Atlassian account.  For more information about finding an API token, see [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account). |

## Troubleshooting

### You cannot authenticate the connector using your Jira Cloud Platform credentials

Possible cause

Your Jira Cloud Platform login, your Jira Cloud Platform password, or both contain non-ASCII characters.

Proposed action

Try changing your credentials through your Jira Cloud Platform account, or use a different Jira Cloud Platform account.
