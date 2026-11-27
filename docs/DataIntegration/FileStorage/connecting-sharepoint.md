---
title: "Sharepoint"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/FileStorage/connecting-sharepoint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections for knowledge marts", "Connecting to file storage"]
---

# Sharepoint

Sharepoint in Microsoft 365 helps organizations share and manage content, knowledge, and applications.

You must install Qlik Data Gateway - Data Movement. For more information, see [*Setting up Qlik Data Gateway - Data Movement for knowledge marts*](../../Gateways/gateways-for-knowledge-mart.htm).

## Preparing for authentication

To access your data, you need to authenticate the connection with your account credentials.

To connect to Sharepoint, you need :

- The hostname. For example: `mycompany.sharepoint.com`.
- The site name. For example: `https://mycompany.sharepoint.com/sites/<site-name>`.
- The tenant ID, client ID, and client secret. For more information, see the [Microsoft](https://learn.microsoft.com/en-us/azure/active-directory-b2c/client-credentials-grant-flow?pivots=b2c-user-flow) documentation.

### Required permissions

**Microsoft Graph (8 permissions)** — all Delegated, Admin consent not required, all Granted for QlikTech Inc.

- `email` — View users' email address
- `Mail.Read` — Read user mail
- `offline_access` — Maintain access to data you have given it access to
- `openid` — Sign users in
- `profile` — View users' basic profile
- `User.Read` — Sign in and read user profile
- `Files.Read.All` — Read all files that user can access
- `Sites.Read.All` — Read items in all site collections

**Sharepoint (5 permissions)** — all Delegated, Admin consent not required, all Granted for QlikTech Inc.

- `AllSites.Manage` — Read and write items and lists in all site collections
- `AllSites.Read` — Read items in all site collections
- `AllSites.Write` — Read and write items in all site collections
- `MyFiles.Read` — Read user files
- `Project.Read` — Read user projects

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
| Hostname | The Sharepoint hostname. |
| Site name | The Sharepoint site name. |
| Drive name | The Sharepoint drive name. |
| Tenant ID | The Sharepoint tenant ID. |
| Client ID | The Sharepoint client ID. |
| Client secret | The Sharepoint client secret. |
