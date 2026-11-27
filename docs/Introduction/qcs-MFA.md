---
title: "Configuring multi-factor authentication ( MFA )"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-MFA.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Registering for a Qlik Account"]
---

# Configuring multi-factor authentication (MFA)

Multi-factor authentication (MFA) adds an extra layer of security to your Qlik Cloud account, reducing the risk of unauthorized access to sensitive data. MFA makes it significantly harder for unauthorized individuals to gain access, even if your password is compromised, by requiring an additional verification step to authenticate.

Information noteThese instructions apply when you use Qlik Account as identity provider. If your organization uses an external identity provider, follow their process.

## When is MFA required?

While MFA is recommended, it remains optional when using Qlik Account as your identity provider (IdP). If you require MFA to be mandatory, consider using a third-party IdP for greater control over authentication methods. Refer to the documentation of your chosen IdP for details.

Although MFA is not required for the service account owner and tenant administrators, we strongly recommend enabling it due to the sensitive nature of the information they can access.

## Setting up MFA with Qlik Account

You can set up MFA at any time to increase the security of your Qlik Account. MFA adds an extra layer of protection by requiring a one-time code in addition to your password when logging in.

### Before you begin

Install an MFA application on your mobile or desktop device.

Popular options include:

- Mobile: Google Authenticator, Okta Verify, Authy, LastPass, Microsoft Authenticator.
- Desktop: Google Authenticator, One Login.

Information noteAfter setting up MFA, do not delete the app or uninstall it from your device. You'll need it every time you log in.

### Set up MFA

Do the following:

1. Click your user profile icon and select Manage account.
2. Select Security.
3. Under Multi-factor authentication, click Set up.
4. To proceed, you need to log out and log back in. Click Log out.
5. Log in again. You will be prompted to set up MFA.

The security settings page.

![Setup screen with QR code and field to add one-time code.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_security_options.png "Click to view full size")

### Add your Qlik account to your MFA app

Tip noteQlik Cloud supports various MFA apps. This example shows how to configure MFA using Google Authenticator on a mobile device.

1. Open your MFA app.
2. Choose the option to add a new account:

   - In Google Authenticator, tap the + icon and select Scan a QR code.
3. Scan the QR code displayed on the Qlik Cloud setup screen.

   - If you’re unable to scan, click Trouble Scanning? and manually enter the code shown on the screen.

   MFA setup screen.

   ![Setup screen with QR code and field to add one-time code.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_mfa_setup.png "Click to view full size")
4. Your MFA app will generate a 6-digit one-time code for your Qlik account. Enter the code on the Qlik setup page and click Continue.
5. Copy and store the recovery code shown on the screen in a secure location (such as a password manager).
6. Click Continue to complete the setup.

MFA is now enabled. You'll be required to enter a one-time code from your MFA app each time you log in.

## Managing your MFA recovery code

When you set up MFA, a recovery code is generated. This code is essential for regaining access to your account if you ever lose access to your MFA device. Store this code securely.

Important points about your recovery code:

- The recovery code is for one-time use only. Once used, a new code will be generated.
- Protect your recovery code with the same level of security as your password. Consider saving it in a password manager.

## Logging in with MFA

After you have set up MFA, you will be asked to provide a one-time code from your MFA app each time you log in.

Do the following:

1. Log in to Qlik Cloud with your username and password.
2. After your credentials are verified, you will be prompted to enter a one-time code.

   MFA login screen.

   ![Setup screen field to enter one-time code.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_mfa_login.png "Click to view full size")
3. Open your MFA app and locate your Qlik account.
4. Enter the 6-digit code displayed in the app.
5. Click Continue to complete the login.

Tip noteYou can select Remember this device for 30 days to reduce how often MFA is required on trusted devices. This setting is stored in your browser cookies.

If you no longed have access to your MFA app, you can use your recovery code to log in. For more help, see [*Troubleshooting MFA*](#Troubles).

## Regenerating your recovery code

If needed, you can regenerate a new recovery code.

Do the following:

1. Click your user profile icon and select Manage account.
2. Select Security.
3. Under Account recovery, click Regenerate.
4. To proceed, you need to log out and log back in. Click Log out.
5. Log in again, providing a one-time code from your MFA app. Then click Continue.
6. Authenticate once more using MFA to generate a new code.
7. Copy and store the new recovery code securely.
8. Click Continue to finish.

## Turning off MFA

If necessary, you can disable MFA. However, we strongly recommend keeping it enabled for enhanced security.

Do the following:

1. Click your user profile icon and select Manage account.
2. Select Security.
3. Under Multi-factor authentication, click Remove.
4. To proceed, you need to log out and log back in. Click Log out and remove.
5. Log in again, providing a one-time code from your MFA app.

MFA is now turned off. You can set it up again at any time.

## Troubleshooting MFA

### Lost access to your MFA device?

If you can't access your MFA application due to a lost device, an invalid verification code, or switching to a new smartphone, use your MFA recovery code to sign in. After signing in, you will receive a new recovery code. Copy and save this code securely, and then set up MFA for your account again.

### Lost your recovery code?

If you have lost your MFA recovery code, contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) to reset MFA for your account. Once your account has been reset, log in to Qlik Cloud to set up MFA again.

Information noteAlways keep your recovery code in a secure location to avoid losing access to your account.

### General tips

Refer to the troubleshooting steps provided here: [Troubleshoot Multi-Factor Authentication Issues](https://auth0.com/docs/troubleshoot/authentication-issues/troubleshoot-mfa-issues)
