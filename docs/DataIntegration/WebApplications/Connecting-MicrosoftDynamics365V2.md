---
title: "Microsoft Dynamics 365 CRM V2"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-MicrosoftDynamics365V2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Microsoft Dynamics 365 CRM V2

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Microsoft Dynamics 365 is a cloud-based business applications platform that provides customer relationship management (CRM). You can use Microsoft Dynamics 365 CRM as a data source when landing or replicating data.

Microsoft Dynamics 365 CRM integration replicates data using the [Dynamics 365 Web API](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview).

See the [Schema](#Schema) section for a list of objects available for replication.

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

To retrieve your credentials:

1. Log into your [Microsoft Azure](https://portal.azure.com/auth/login/) account.
2. Click New registration.
   1. Set Name to Precog.
   2. Set the redirect URL to https://precog.cloud and click Register.
3. Copy the Application (client) ID and paste it into a secured file.
4. Click Endpoints.
   1. Copy the value in OAuth 2.0 authorization endpoint (v1) — this is your Authorization Endpoint — and paste it into a secured file.
   2. Copy the value in OAuth 2.0 token endpoint (v1) — this is your Token Endpoint — and paste it into a secured file.
5. Click API permissions.
   1. Click Add a permission > Microsoft Graph > Delegated permissions, select offline\_access, and click Add permissions.
   2. Click Add a permission > Dynamics CRM, select user\_impersonation, and click Add permissions.
6. Click Grant admin consent for... and click Yes. If you do not have administrator rights, ask your Azure Active Directory administrator to grant consent.
7. Click Certificates & secrets > New client secret, set the expiry to Never, and click Add.

   Copy the Value — this is your Client Secret — and paste it into a secured file.
8. In your Dynamics CRM instance, navigate to Settings > Customizations > Developer Resources.

   Copy the Service Root URL and paste it into a secured file.

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
| Client ID | Client ID. |
| Authorization Endpoint | Authorization endpoint. |
| Token Endpoint | Token endpoint. |
| Client Secret | Client secret. |
| Service Root URL | Service root URL. |
| Resource | The first part of your Service Root URL. Example: https://example.crm.dynamics.com |

## Schema

Schemas and naming conventions can change from version to version. Verify your version before continuing.

Datasets are discovered dynamically from the Microsoft Dynamics 365 CRM metadata endpoint. All standard Dynamics 365 entities are supported.

Depending on your destination, table and column names may not appear as they are outlined below.

|  |  |
| --- | --- |
| **Replication Method** | CDC |
| **Replication Key** | modifiedOn |
