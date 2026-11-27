---
title: "Salesforce"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Salesforce.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications", "Deprecated SaaS applications"]
---

# Salesforce

Information noteThis connector is deprecated, and cannot be used to create new tasks. Although deprecated, the connector remains fully supported, and tasks which are already using this connector will continue to work as usual. For new tasks, use the improved [*Salesforce*](Connecting-Salesforce-v2.htm) connector.

Salesforce is a cloud-based CRM platform. You can land Salesforce data as a data source when landing or replicating data.

- For more information about connecting to SaaS applications, see [*Connecting to SaaS applications*](../Landing/connecting-web-applications.htm).
- Depending on your use case, you might need to install Data Movement gateway to move data from SaaS applications. For more information, see [*When is Data Movement gateway required?*](../../Gateways/replication-gateway.htm#top).

## Supported versions and objects

The following Salesforce versions are supported:

- Salesforce Sales Cloud
- Salesforce Service Cloud
- Salesforce Marketing Cloud

  This requires using Salesforce Marketing Cloud Connect. For more information, see [Marketing Cloud Connect](https://help.salesforce.com/s/articleView?id=sf.mc_co_marketing_cloud_connect.htm&type=5).
- Salesforce Commerce Cloud

Information noteThe Vote object is not supported.

For more information about the results returned from Salesforce, see [Salesforce REST API Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_queryall.htm).

If the data contains custom objects using the extension of \_\_c in the name, they will be created in the target with \_c instead, using one \_ and not two.

## Preparing for authentication

To access your Salesforce data, you need to authenticate the connection with your account credentials. You must create a private app in Salesforce and retrieve a client ID and a client secret:

1. Log into Salesforce and create a new Connected app. Name this app and API and provide your email address.
2. Enable OAuth Settings and set Callback URL to https://connector.qlik.com/auth/oauth/v3.htm.
3. Add the following OAuth Scopes:

   - Manage user data via APIs (api)
   - Access unique user identifiers (openid)
   - Perform requests at any time (refresh\_token, offline\_access)
4. Select Configure ID Token and set Token valid for to 720.
5. Deselect Require Proof Key for Code Exchange (PKCE) Extension for Supported Authentication Flows.
6. Scroll down and click Save.

   At this point Salesforce advises to allow from 2-10 minutes for your changes to take effect on the server before using the connected app.
7. Copy Consumer key to the Client ID connection setting.
8. Copy Consumer secret to the Client Secret connection setting.
9. Provide your Salesforce Host. You can copy this from the location bar in your browser when accessing your Salesforce instance.
10. Scroll down and click Add.

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
| Salesforce Instance | Salesforce instance. To find your Salesforce instance:   1. Log in to Salesforce, and click Setup. 2. Click Company Information. 3. Copy your Salesforce instance, for example UM1 or AP8, in the right column below Organization Edition.   If you are using a sandbox or a custom domain, use your domain with .salesforce.com excluded. Example: <domain>.sandbox.my if the sandbox domain is <domain>.sandbox.my.salesforce.com. |
| Client ID | Client ID. |
| Client Secret | Client secret. |
| Login Domain | Login domain.  For the default production domain use login.salesforce.com.  If you are using a sandbox or a custom domain, use your domain. Example: <domain>.sandbox.my.salesforce.com for a sandbox domain. |
