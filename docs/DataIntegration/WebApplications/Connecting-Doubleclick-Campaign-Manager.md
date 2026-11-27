---
title: "Doubleclick Campaign Manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/WebApplications/Connecting-Doubleclick-Campaign-Manager.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to SaaS applications", "Supported SaaS applications"]
---

# Doubleclick Campaign Manager

Doubleclick Campaign Manager is a web-based ad management system for advertisers and agencies.

Doubleclick Campaign Manager integration replicates data using the [Campaign Manager 360 API](https://developers.google.com/doubleclick-advertisers/getting_started).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

Information noteMake sure that the account you use has read access to the tables you want to fetch.

Before you set up the connection, ensure the following requirements are met:

- You have an active **Campaign Manager 360** account.
- API access is enabled for your **Campaign Manager 360** account.
- Your **Campaign Manager 360** user profile has the appropriate access permissions. They are set in the Campaign Manager 360 interface and determine what you can do through both the UI and the API.

To generate your client ID and secret:

1. Log into your [Doubleclick Campaign Manager](https://developers.google.com/_d/signin) account.
2. Navigate to Credentials.
3. Click + Create Credentials, and select OAuth client ID.
4. From the Application type drop-down menu, select Web application.
5. Make sure Authorized Redirect URIs is set to https://connector.qlik.com/auth/oauth/v3.htm.
6. Click Create.
7. Copy and paste your client secret and client ID into a secured file.

   Make sure your client ID includes the Campaign Manager API scope. For more information, see [Authorize Requests](https://developers.google.com/doubleclick-advertisers/authorizing).

To locate your profile ID:

1. Log into your Doubleclick Campaign Manager account.
2. Click your profile icon in the upper-right corner.
3. Locate the ID of the profile you want to connect.

   It is a seven digit number next to the name of the profile. For example: `9999999`.

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
| Start Date | Enter the date, in the format `MM/DD/YYYY`, from which the data must be replicated from your source to your target. |
| Profile ID | Profile ID. |
| Client ID | Client ID. |
| Client Secret | Client Secret. |
