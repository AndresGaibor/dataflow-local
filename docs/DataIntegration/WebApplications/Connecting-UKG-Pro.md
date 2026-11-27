---
title: "UKG Pro - UltiPro"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-UKG-Pro.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# UKG Pro - UltiPro

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

UKG Pro - UltiPro is a human capital management platform. You can use UKG Pro - UltiPro as a data source when landing or replicating data.

You can leave all custom report fields empty to use pre-built reports. Fill in the custom report fields, levels, and breakdowns fields to use user-defined reports.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

### Finding Customer API Key

You will need to be logged into the UKG Ultipro application as a System Administrator.

Open the system configuration and navigate to the Web Services page. Your Customer API Key is listed at the top of your UltiPro Web Services page.

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
| Customer API Key | API key. |
| Host | The host name of your UKG Pro - UltiPro web service page, excluding https://. The host can be found in all your web service endpoints.  Example: In the endpoint https://service7.ultipro.com/services/LoginService the Host is service7.ultipro.com. |
| Service Account Username | User name of the UKG Pro - UltiPro service account to use. |
| Service Account Password | Password to the UKG Pro - UltiPro service account to use. |
| Start Date | Start date for history datasets in YYYY-MM-DD format. |
| UTA Start Datetime | Start time in ISO format.  Information noteThis field is only supported if you have access to UTA. |
| UTA End Datetime | End time in ISO format.  Information noteThis field is only supported if you have access to UTA. |
