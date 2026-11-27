---
title: "OneDrive"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/FileStorage/connecting-onedrive.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections for knowledge marts", "Connecting to file storage"]
---

# OneDrive

OneDrive is an online storage space in the cloud that is provided for licensed users in an organization.

You must install Qlik Data Gateway - Data Movement. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

To connect to OneDrive, you need the tenant ID, client ID and client secret. For more information, see the [Microsoft](https://learn.microsoft.com/en-us/azure/active-directory-b2c/client-credentials-grant-flow?pivots=b2c-user-flow) documentation.

## Creating the connection

1. Click Authenticate when you have filled in the required connection settings.

   You may be asked to log in to the source application.

   A window is displayed with an authentication code.
2. Copy the code to the clipboard and return to the connection dialog.
3. Paste the code in Complete authentication with the code provided by the source and click Verify.

   Tip noteYou may need to scroll down to see this field.

   When status is Verified, the authentication is verified.
4. Fill in the required connection properties.
5. Provide a name for the connection in Name.
6. Click Test connection to verify the configuration.
7. When the test is successful, click Create.

Connection settings

| Setting | Description |
| --- | --- |
| Data gateway | You need a customer-managed data gateway. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm). |
| Tenant ID | The OneDrive tenant ID. |
| Client ID | The OneDrive client ID. |
| Client secret | The OneDrive client secret. |
| Default Root directory | The path to the root directory. |
