---
title: "Setting up the Qlik Analytics mobile app"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Mobile/qsmsaas-setup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Analytics mobile app"]
---

# Setting up the Qlik Analytics mobile app

When you start the Qlik Analytics mobile app for the first time, you must connect and authenticate to a Qlik Cloud [tenant](#glossary-1 "Glossary term") before you can consume Qlik Sense applications on your mobile device.

After you have connected once, you can open the mobile app when you are offline, and view Qlik Sense applications that you have downloaded.

## Technical and security considerations

### OS support

For information about operating system support for the Qlik Analytics mobile app, refer to:

- Apple: [Qlik Analytics (Apple Store)](https://apps.apple.com/us/app/qlik-sense-saas/id1523006591)
- Android: [Qlik Analytics (Google Play Store)](https://play.google.com/store/apps/details?id=com.qlik.qsm)

### Number of concurrent devices

Each user can be logged on to the Qlik Analytics mobile app on five concurrent mobile devices per tenant.

If you delete the Qlik Analytics mobile app from your device without having logged out first, a second device license will be consumed when you reinstall the app.

### Qlik Analytics login longevity

The OAuth protocol and refresh-token architecture used by the Qlik Analytics mobile app to communicate with Qlik Cloud means that most Qlik Analytics mobile users do not have to log in each time they open their mobile app.

Users are automatically logged out if:

- The user is inactive for 7 days without using the app.
- The identity provider application configuration is incomplete.
- The administrator explicitly revokes the user's access.

### Developing applications for the Qlik Analytics mobile app

Consider the size and complexity of your application when placing objects on the same sheet or page. The Qlik Analytics mobile app runs on a device with much lower CPU performance and available memory compared with a computer using a web browser to connect to Qlik Cloud.

We recommend that you test the Qlik Sense application carefully in the Qlik Analytics mobile app before you make it available for consumers. Perform tests on a device with system specifications that match those of your application consumer. Tests should include the following:

- Open the Qlik Sense application
- Make selections in the data
- Test offline behavior

### On-demand applications

On-demand applications may not work as expected in the Qlik Analytics mobile app.

### Direct Query applications

Direct Query applications are not supported in the Qlik Analytics mobile app.

### Security

The Qlik Analytics mobile app is protected by a Qlik Sense password when you connect to a Qlik Cloud tenant. For additional security, especially when working offline, you can turn on app lock to use PIN or biometric authentication to unlock the Qlik Analytics mobile app. See  [*Unlocking the app with a PIN or biometric*](#TouchFaceID).

The Qlik Analytics mobile client incorporates additional defense-in-depth security features that help ensure mobile devices meet various compliance standards. If the operating environment is found to deviate from these standards, access may be restricted, local QVF and cached files are removed, and an alert is issued. Please ensure that your organization’s mobile OS and network configurations are maintained in line with industry best security practices.

#### Mobile device management with Microsoft Intune

If your organization uses Microsoft Intune to manage mobile devices, administrators can automate app setup and apply protection policies for the Qlik Analytics mobile app. See [*Securing and configuring the Qlik Analytics mobile app with Microsoft Intune*](../Admin/configure-mobile-app.htm).

Tip noteProtect your data by ensuring that your device is protected with a password or biometric. Lock the device when not in use or log out from the Qlik Analytics mobile app.

Information noteThe tablet or phone must have a password or screen locking enabled to install and run the Qlik Analytics mobile app.

### Object rendering

Visualizations in the Qlik Analytics mobile app can be rendered natively or in an embedded WebView.

Natively rendered visualizations have better performance compared to visualizations rendered in WebView. Natively rendered visualizations are:

- Button
- Filter pane
- KPI
- Table (Retired) (as accessed from Charts > Legacy)
- Text & image
- Treemap

If a natively rendered visualization is wrapped inside a Container object, it will be rendered in an embedded WebView.

While natively rendered visualizations have greater performance, they do not support the full breadth of object styling (general styling or theme-based styling) when viewed in the Qlik Analytics mobile app. If styling of objects is important for mobile analysis, the application developer can place the object inside a Tab container, Container, or Layout container. This forces the WebView presentation and preserves styling.

Natively rendered visualizations do not support CSS styles in custom themes.

## Connecting to a Qlik Cloud subscription

After you have downloaded the Qlik Analytics mobile app, you create a connection to your Qlik Cloud [subscription](#glossary-2 "Glossary term"). You can have more than one connection.

Do the following:

1. On the start page, tap +.

   If this is the first connection, tap Login.
2. Define the Qlik Cloud URL, in the following form: tenant.qlikcloud.com. Add a friendly name for the tenant. Tap Add.

## Logging in to Qlik Cloud

After you have added the connection to your Qlik Cloud subscription, you must log in using your Qlik Cloud credentials.

Do the following:

1. On the start page, tap the Qlik Cloud subscription. The login page is displayed.
2. Enter your username and password and tap Login.

Information noteOffline login is possible until 7 days after the last login.

## Unlocking the app with a PIN or biometric

For added security, you can turn on app lock to use your device authentication method (PIN, fingerprint, or face) with the Qlik Analytics mobile app. Protecting the app with a PIN or biometric helps to prevent unauthorized users from accessing the app. When turned on, you must unlock the app using either a PIN or biometric when opening or switching to the app. Unlocking the app is required whether you are connected to the tenant or working offline. You must set up fingerprint or face authentication for your device to use app lock with the Qlik Analytics mobile app.

Do the following:

1. Tap your profile icon in the mobile app to open the Settings page.

You can also tap ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel.svg) on the start page.

2. Under App lock, turn on Unlock with PIN, fingerprint, or face authentication.

Information noteIf fingerprint or face authentication does not unlock the app, you can enter your PIN.

## Using the Qlik Analytics mobile app while offline

If enabled in your Qlik Cloud tenant, you can still open the Qlik Analytics mobile app and view the Qlik Sense apps you have downloaded while being disconnected or offline.

Offline functionality is enabled by the tenant admin in the Administration activity center, see [*Setting access to the Qlik Analytics mobile app*](../Admin/mobile-set-access.htm).

You must log in to the tenant at least once before you can open Qlik Analytics offline. Offline login is then allowed for 7 days since the last online login.

Do the following:

1. Download an app to your mobile device.
2. Turn on Airplane mode on your device, or disconnect from the server.
3. Test the app to ensure that the app works as expected.

## Logging out

1. Tap your profile icon in the mobile app. The Settings page opens.
2. Tap Log out. You are logged out, and the start page opens.

## Editing a subscription connection

Do the following:

1. On the start page, long-touch and swipe left on the connection you want to edit.
2. Tap ![update](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg). The Update server page opens.
3. Update the URL and the friendly name as required. Tap Update.

## Removing a subscription connection from the list

When you delete an existing connection from your Qlik Analytics mobile app, any locally downloaded apps from this tenant will be deleted as well.

1. On the start page, long-touch and swipe left on the tenant connection you want to remove.
2. Tap ![delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg).
3. Tap Confirm. The Qlik Cloud tenant connection is deleted from your Qlik Analytics mobile app.
