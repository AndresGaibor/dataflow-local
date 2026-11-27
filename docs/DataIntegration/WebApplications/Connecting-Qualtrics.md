---
title: "Qualtrics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Qualtrics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Qualtrics

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Qualtrics is an online survey software platform. You can land survey data from Qualtrics as a data source when landing or replicating data.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your Qualtrics data, you need to authenticate the connection with your account credentials.

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
| Organization Name | Organization name, sometimes called the brand. This is displayed when you hover the mouse over the people icon at the top of your organization's Qualtrics screen. |
| API Token | API token. To generate an API token:   1. In your Qualtrics account navigate to Account Settings. 2. Under Qualtrics IDs in the API section, click Generate Token. |
| Data Center ID | Data center ID.  In your Qualtrics account navigate to Account Settings > Qualtrics IDs. Your Data center ID is displayed in User. |
| Start Date | Start date for queries taking date parameters in the format YYYY-MM-DD. |
