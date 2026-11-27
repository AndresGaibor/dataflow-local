---
title: "SAP Cloud for Customer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-SAP-Cloud-for-customer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# SAP Cloud for Customer

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

SAP Cloud for Customer is a SaaS platform for sales and service enablement. You can use SAP Cloud for Customer as a data source when landing or replicating data.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

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
| Username | Your user name in SAP Cloud for Customer. |
| Password | Your password in SAP Cloud for Customer. |
| OData URL | The OData discovery URL for your SAP Cloud for Customer tenant. Examples:   - Standard OData service: `https://<tenant>.crm.ondemand.com/sap/c4c/odata/v1/c4codataapi/` - Custom OData service: `https://<tenant>.crm.ondemand.com/sap/c4c/odata/cust/v1/campaigndata/` |
