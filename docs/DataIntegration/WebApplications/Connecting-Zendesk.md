---
title: "Zendesk"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Zendesk.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Zendesk

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual. For new tasks, use the improved [*Zendesk Chat*](Connecting-Zendesk-Chat.htm) and [*Zendesk Support*](Connecting-Zendesk-Support.htm) connectors.

Zendesk provides SaaS products related to customer support, sales, and other customer communications.. You can use Zendesk as a data source when landing or replicating data.

You can leave all custom report fields empty to use pre-built reports. Fill in the custom report fields, levels, and breakdowns fields to use user-defined reports.

Information noteThe Chat object is not supported.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

- Log into Zendesk, navigate to Settings > Channels > API, and enable Password Access.

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
| Email | Email address that is associated to your Zendesk account and your API token. Use the following format: {email\_address}/token, for example jdoe@example.com/token. |
| Token | API token. For example: 6wiIBWbGkBMo1mRDMuVwkw1EPsNkeUj95PIz2akv. |
| Subdomain | You can find your subdomain in Zendesk: Settings > Account > Subdomain.  You can also find it in the URL of your account homepage. If the URL is https://mydomain.zendesk.com/, the subdomain is mydomain. |
