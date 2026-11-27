---
title: "Microsoft Dynamics 365 CRM"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-MicrosoftDynamics365.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Microsoft Dynamics 365 CRM

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Microsoft Dynamics 365 is a cloud-based business applications platform that provides customer relationship management (CRM). You can land CRM data from Microsoft Dynamics 365 as a data source when landing or replicating data.

For more information about the API, see [Web API types and operations](https://learn.microsoft.com/en-us/previous-versions/dynamicscrm-2016/developers-guide/mt607990(v=crm.8)).

The following Microsoft Dynamics 365 modules are supported:

- Sales
- Marketing
- Customer Service
- Field Service
- Project Service Automation

Only standard objects are supported.

Metadata discovery is dynamic and based on the datasets used in your application.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

When using CDC, you must enable Change Tracking in Microsoft Dynamics 365 for all entities that need to be replicated.

- Out of the box entities are enabled by default.
- You can enable custom entities by navigating to the relevant Entity Definition page of your entity and selecting Change Tracking.

For more information, see [Enable change tracking for entities](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/entity-change-track).

Feature snapshot

| Feature/Functionality | Support details |
| --- | --- |
| Supported Qlik Talend Data Integration projects | Data pipeline projects and Replication projects. |
| [*Target update methods*](../SourcesConnections/Change-processing.htm) | Landing tasks:   - Change data capture (CDC) using Change Tables - Reload and compare   Replication tasks:   - Full load - Change data capture (CDC) using Change Tables - Change data capture (CDC). Using this method, changes are directly applied to the target.   Landing data in a data lake tasks:   - Change data capture (CDC) using Change Tables - Reload |
| [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm#Managing) | Manual metadata generation is required. |
| [*Automatic schema evolution*](../Replicating/replicating-settings.htm#Schema) | Not supported |
| Replication of LOB columns (NCLOB, CLOB, and BLOB) | Determined by the task type:   - Landing tasks: Supports limited LOB size only - Replication tasks: Supports unlimited LOB |
| Scheduled CDC | Only required when accessing data sources without [Data Movement gateway](../../Gateways/replication-gateway.htm). |
| Notifications | Fully supported  [*Setting notifications for changes in operation*](../Introduction/Notifications.htm) |
| Monitoring | Fully supported  [*Monitoring an individual data task*](../Introduction/Monitoring-data-tasks.htm) |
| Automatic denesting of JSON column payloads | Fully supported |

## Preparing for authentication

To access your Microsoft Dynamics 365 CRM data, you need to authenticate the connection with your account credentials.

Information noteThis requires administrator access to the Microsoft Dynamics 365 CRM account.

1. Go to https://portal.azure.com/#blade/Microsoft\_AAD\_RegisteredApps/ApplicationsListBlade and click New registration.
2. Set Name to Qlik
3. Set the redirect URL to https://connector.qlik.com/auth/oauth/v3.htm.
4. Click Register.
5. Copy the Application ID to Client ID in the connection settings.
6. Go to the API permissions tab, click Add a permission, and select Microsoft Graph.
7. Click Delegated permissions and select Offline\_access.
8. Click Add permissions.
9. Click Add a permission.
10. Click Dynamics CRM.
11. Click Permissions, and select user\_impersonation.
12. Click Add permissions.
13. Click Grant admin consent for... and thenclick Yes.
14. Click Certificates & secrets.
15. Click New client secret, and select Never or set the expiry as far in the future as possible.
16. Click Add.

Value contains your client secret that you can copy to Client Secret in the connection. You may also want to record the client secret for future use.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

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
| Client ID | Client ID. Application ID for the application you created. |
| Client Secret | Client secret. You can find your client secret on the application page. on the Certifications and secrets tab. |
| Authorization Endpoint | Authorization endpoint. You can find your authorization endpoint on the application page. Click Endpoints, and copy the value in OAuth 2.0 authorization endpoint (v1). |
| Token Endpoint | Token endpoint. You can find your token endpoint on the application page. Click Endpoints, and copy the value in OAuth 2.0 token endpoint (v1). |
| Service Root URL | Service root URL. To find the service root URL:   1. Go to your Microsoft Dynamics 365 CRM instance and click Settings or Advanced Settings. 2. At the top of the page next to Settings, click the downwards-facing arrow and select Customizations. 3. Click Developer Resources. |
| Resource | Resource. Use the first part of your Service Root URL.  Example: https://example.crm.dynamics.com |
