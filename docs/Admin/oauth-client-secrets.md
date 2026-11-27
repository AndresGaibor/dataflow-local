---
title: "Managing client secrets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-client-secrets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Managing client secrets

Confidential (Web) OAuth clients use a client secret or a private key to authenticate with Qlik Cloud. Tenant admins can manage client secrets to rotate credentials or replace compromised secrets.

You can add up to 5 client secrets to an OAuth client. To rotate a secret without interrupting the client application's access to Qlik Cloud, follow these steps:

1. Add a new client secret.
2. Update the client application to use the new secret.
3. Remove the old client secret.

## Adding a client secret

Do the following:

1. In the Administration activity center, go to OAuth.
2. Locate the OAuth client.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Manage secrets.
4. Click Generate a new client secret.
5. Copy the client secret and client ID, and store them securely.

   Information noteYou cannot access the client secret again after you close the dialog.
6. Click Close.

## Removing a client secret

Do the following:

1. In the Administration activity center, go to OAuth.
2. Locate the OAuth client.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Manage secrets.
4. Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) next to the client secret.
5. Click Close.

## Using private key JWT authentication

Confidential (Web) OAuth clients can use Private key JWT authentication instead of a client secret.

With this authentication method, the client uses a public/private key pair. You register the public key in JSON Web Key (JWK) format in Qlik Cloud. Your application uses the private key to sign JWTs.

You configure the authentication method under Authentication method and token duration when you create or edit an OAuth client.

For more information, see [*Creating OAuth clients*](mc-create-oauth-client.htm#Creating2) and [Create a public/private key pair for signing JWTs](https://qlik.dev/authenticate/oauth/oauth-private-key-jwt-reference/ "Create a public/private key pair for signing JWTs") on the Qlik Developer Portal.
