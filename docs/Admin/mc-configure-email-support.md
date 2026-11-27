---
title: "Configuring email for reports and notifications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-configure-email-support.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Configuring email for reports and notifications

Configure an email provider to enable users to subscribe to reports and share charts.
Users can also receive [notifications](#glossary-0 "Glossary term") about applications, [notes](#glossary-2 "Glossary term"), spaces, and alerts.

You need to set up an email provider from which emails are sent. Choose between Microsoft 365 or an SMTP provider like G Suite. Microsoft 365 uses the OAuth2.0 protocol which uses service tokens, eliminating the need to share user credentials.

Only one active provider can be configured at a time, and for security reasons, only the credentials for the active provider are stored. This avoids storing of sensitive data that is not currently in use. Activating a new provider will deactivate the currently active one. Selecting None will delete any saved settings.

Tenant administrators can configure email settings.

## Configuring an SMTP email provider

SMTP is a standard protocol used for sending emails, and it allows you to connect to the email server of your chosen provider to send messages.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Email and reports tab.
2. In the Email provider section, select SMTP.
3. Enter the SMTP server address from which to send email notifications.
4. Enter the port number for the email server.
5. Choose the security type:

   - StartTLS
   - SSL/TLS
   - None
6. Enter the sender email address. This is the email address that recipients will see in the From field of the email.
7. Enter the sender name. This name appears as the sender in email notifications.
8. For Username, do one of the following:

   - If you intend to use the sender email address for email server credentials, select the Same as sender email address checkbox.
   - If the sender email address will not be used for email server credentials, clear the Same as sender email address checkbox and enter an email address in the Username field.
9. Enter the email account password.
10. Click Save to activate the email provider.

    Information noteIf you have a previously active provider, it will be deactivated.
11. Click Send test email to verify the configuration.
12. Enter the email address where you want to receive a test message and click Send.
    If the configuration is correct, you should receive a message with the subject "Test email from the Qlik Cloud Administration activity center" from the configured sender email address.

    Information noteTo prevent received emails from ending up in the spam folder, add the IP addresses for your region to the allowlist. These addresses can be also used for DNS SPF records. For more information see [*Allowlisting domains and IP addresses*](../Introduction/qlik-cloud-dns-ip.htm).

## Configuring a Microsoft 365 email provider using OAuth2

When setting up Microsoft 365 as email provider in Qlik Cloud, you need to provide tenant ID, client ID, and client secret. These details are part of the OAuth 2.0 authentication process, ensuring secure communication between your application and Microsoft 365.

In supported Qlik Cloud Government tenants, you can select a cloud region for Microsoft 365 email configuration. This setting controls which Microsoft cloud endpoints are used for authentication and sending email.

Information note

If you use the Microsoft 365 SMTP service, check the Outlook service limits for a single mailbox in [Microsoft Graph service-specific throttling limits](https://learn.microsoft.com/en-us/graph/throttling-limits#outlook-service-limits). When using features like tabular reporting or subscriptions, your Qlik Cloud tenant's file production could potentially reach these service limits.

### Before you begin

- You must have administrator access in Microsoft Entra ID.
- You must be able to create and configure application registrations.

### Obtaining the tenant ID, client ID, and client secret

To find the tenant ID, log in to the Microsoft Entra admin center and go to Identity > Overview. The Tenant ID is shown on the Properties tab.

To obtain the client ID and client secret, you need to create a new application registration in Microsoft Entra ID. Once the application is created, do the following:

1. Go to the application overview page and copy the Application (client) ID.
2. Go to Certificates & secrets > Client secrets and select New client secret. Copy the secret and store it safely.

For more information, see:

- [How to find your Microsoft Entra tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant)
- [Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

### Add Microsoft Graph permissions

You also need to add Microsoft Graph permission for sending emails.

1. In the Microsoft Entra admin center, go to API permissions and click Add a permission.
2. Under Microsoft APIs, click Microsoft Graph and select Application permissions.
3. Add the permission Mail.Send.

For more information, see [Application permission to Microsoft Graph](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#application-permission-to-microsoft-graph).

### Configuring the email server

Do the following:

1. In the Qlik Cloud Administration activity center, go to the Settings page, then select the Email and reports tab.
2. In the Email provider section, select Microsoft 365.
3. Enter the sender email address.

   This should be a UserPrincipalName (UPN) for a Microsoft Entra ID user account. The email address that recipients will see in the From field of the email will be the user's full email address.

   Information note

   You can restrict the sender to specific mailboxes. For more information, see [Limiting application permissions to specific Exchange Online mailboxes](https://learn.microsoft.com/en-gb/graph/auth-limit-mailbox-access).
4. For Tenant ID, enter the unique identifier assigned to your Microsoft 365 tenant.
5. Enter the Client ID and Client secret for your Microsoft Entra ID application registration. These are used for authentication with the email service.

   Qlik Cloud Government note

   If you are using a Qlik Cloud Government and Qlik Cloud Government - DoD tenant, you can also select a Cloud region. Select one of the available options:

   - Global: Suitable for connecting to O365 (Office 365) Commercial environments.
   - GCC/GCC High: Suitable for connecting to Office 365 Government Community Cloud (GCC) and Office 365 Government Community Cloud High (GCCH) environments.

   For more information about configuring email providers in Qlik Cloud Government, see [Qlik Cloud Government — Qlik Cloud Administration](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg.htm#Admin) and [Qlik Cloud Government - DoD — Qlik Cloud Administration](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg-dod.htm#Admin).
6. Click Save to activate the email provider.

   Information noteIf you have a previously active provider, it will be deactivated.
7. Click Send test email to verify the configuration.
8. Enter the email address where you want to receive a test message and click Send.
   If the configuration is correct, you should receive a message with the subject "Test email from the Qlik Cloud Administration activity center" from the configured sender email address.

   Information noteTo prevent received emails from ending up in the spam folder, add the IP addresses for your region to the allowlist. These addresses can be also used for DNS SPF records. For more information, see [*Allowlisting domains and IP addresses*](../Introduction/qlik-cloud-dns-ip.htm).

## Learn more

- [*Administering reporting and subscriptions*](mc-administer-subscriptions.htm)
- [*Enabling and disabling reporting, subscriptions, and sharing features*](mc-enable-reporting-features.htm)
- [How do I configure an email server in Qlik Cloud?](/lnk/How_configure_email_server_Cloud)
- [How do I email Qlik Sense charts?](/lnk/How_email_Qlik_Sense_charts)

Related learning:

- [How do I configure an email server in Qlik Cloud?](/lnk/How_configure_email_server_Cloud)
- [How do I email Qlik Sense charts?](/lnk/How_email_Qlik_Sense_charts)
