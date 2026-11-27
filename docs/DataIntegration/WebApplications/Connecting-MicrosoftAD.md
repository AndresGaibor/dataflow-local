---
title: "Microsoft Azure Active Directory"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-MicrosoftAD.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Microsoft Azure Active Directory

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual.

Microsoft Azure Active Directory is a directory service used for identity and access management. You can use Microsoft Azure Active Directory as a data source when landing or replicating data.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- For more information about Lite connectors, see [*SaaS application Lite connectors*](../Landing/connecting-web-applications.htm#SaaS2)
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Preparing for authentication

To access your Microsoft Azure Active Directory data, you need to authenticate the connection with your account credentials.

Information noteThis requires administrator access to the Microsoft Azure Active Directory account.

1. Go to https://portal.azure.com/#blade/Microsoft\_AAD\_RegisteredApps/ApplicationsListBlade and click New registration.
2. Set Name to Qlik
3. Set the redirect URL to https://connector.qlik.com/auth/oauth/v3.htm.
4. Click Register.
5. Copy the Application ID to Client ID in the connection settings.
6. Click API permissions.
7. Click Add a permission.
8. Click Microsoft Graph.
9. Click Delegated permissions, and select offline\_access.
10. In the list, select all integrations that contains data you want to include in the connection. For each integration, select all items that end with .Read, .Read.Basic, .Read.All or .Read.Shared. Click Add permissions when you are finished with your selections.
11. Click Grant admin consent for... and select Yes.
12. Click Certificates & secrets.
13. Click New client secret, and select Never.
14. Click Add.

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
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Graph Base URL | Graph base URL  Example: https://graph.microsoft.com/v1.0 |
