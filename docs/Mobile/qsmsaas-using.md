---
title: "Using the Qlik Analytics mobile app"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Mobile/qsmsaas-using.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Analytics mobile app"]
---

# Using the Qlik Analytics mobile app

Use the Qlik Analytics mobile app to access and consume Qlik Sense applications that are available to you on a Qlik Cloud [tenant](#glossary-1 "Glossary term"). Download applications to your device to use them offline.

Typically, Qlik Sense applications are shared with you in your collections for you to download and use offline. Applications that you download and open offline are available for interaction. You can make [selections](#glossary-2 "Glossary term") in the data, but the applications cannot be developed further or saved.

Information noteThe Qlik Analytics mobile app will use Wi-Fi when it is available. If Wi-Fi is not available, the app will attempt to use cellular data. If you do not want the app to use cellular data, disable cellular data on your device.

## Switching between subscriptions

If you are subscribing to more than one tenant, you can switch between your tenants without having to log out.

Do the following:

1. In the Mobile Collection, tap the tenant name to open the subscriptions list.

   Switch between Qlik Cloud subscriptions

   ![Switch between Qlik Sense Mobile SaaS subscriptions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qsmsaas-switch-between-subscriptions.png "Click to view full size")
2. In the subscriptions list, tap the tenant you want to switch to.

## Open Qlik Sense applications

The applications you see in the Qlik Analytics mobile app are apps that belong to your Mobile collection. If you do not see the application you want to explore, you can search for it and then click the Add to collection icon to add it to your Mobile collection.

Do the following:

- In the Mobile Collection, tap the Qlik Sense app icon to open the application.

  If you are offline, and if you have downloaded the application, the offline version opens, otherwise the online version is opened. Downloaded applications have a ![downloaded](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download_success.svg) badge.

## Consuming offline versions of applications

You can download applications to your tablet or phone for offline use. You can select to open the online version or the offline version of applications you have downloaded.

If a newer version of the downloaded application exist, you can download the updated version or continue consuming your offline version.

### Download applications for offline use

Qlik Sense applications that can be downloaded have a ![download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) badge in the Qlik Analytics mobile app.

Do the following:

1. In the Mobile Collection, tap the download button ![download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) for the application you want to download.
2. Tap Confirm.

   The application is downloaded to your mobile device. Downloaded apps have a ![downloaded](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download_success.svg) badge.

### Opening offline version of an application

If you are online, Qlik Analytics opens the online version by default. If you want to open the offline version, do the following:

1. Make sure the Qlik Sense application has been downloaded for offline use. Downloaded applications have a ![downloaded](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download_success.svg) badge.
2. Tap ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the Qlik Sense application. The details window opens.
3. Tap Open offline version. The offline version of the app opens.

### Updating offline version of an application

If the application has been updated, for example data has been reloaded, an Update button indicates that there is a newer version of the application available.

Do the following:

- In the Mobile Collection, tap Update and confirm to download the latest version of the application.

### Deleting offline versions of applications

You can delete offline versions of applications from your mobile device.

Do the following:

1. Tap ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the Qlik Sense application. The details window opens.
2. Tap Delete offline version.
3. Tap Confirm.

   The offline version of the application is deleted.

### Security considerations

The Qlik Analytics mobile client incorporates additional defense-in-depth security features that help ensure mobile devices meet various compliance standards. If the operating environment is found to deviate from these standards, access may be restricted, local QVF and cached files are removed, and an alert is issued. Please ensure that your organization’s mobile OS and network configurations are maintained in line with industry best security practices.

## Monitoring visualizations in the Qlik Analytics mobile app

You can monitor [visualizations](#glossary-3 "Glossary term") in the Qlik Analytics mobile app, allowing you to view [charts](#glossary-4 "Glossary term") without opening any apps.

When consuming monitored visualizations in the Qlik Analytics mobile app, you can see all the related metadata, such as when it was created, and the last time it was reloaded. Tap ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then select Chart details to view the metadata.

When you open a chart in the Qlik Analytics mobile app, the chart shows the latest version of the chart from the last reload of data in the source application. You can view the chart, the chart details, and the history.

You cannot make selections in the chart, but you can view the chart in the source app by tapping View in app. For example, you may want to apply [bookmarks](#glossary-5 "Glossary term") or see how the chart changes based on new selections. View in app opens the source app to the visualization with selections applied.

For more information about monitoring visualizations in your [activity center](#glossary-6 "Glossary term"), see [*Monitoring visualizations*](../Hub/monitor-charts-hub.htm).

### Adding visualizations to monitor from the Qlik Analytics mobile app

You can add visualizations to monitor from the Qlik Analytics mobile app.

Do the following:

1. Tap ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the visualization you want to monitor.
2. Tap Monitor in activity centers. The Monitor in hub dialog opens.
3. Give the visualization a name.
4. Tap Create.

The visualization can now be monitored from the Qlik Sense Mobile SaaS hub.

### Adding visualizations to monitor from Qlik Cloud

You can add visualizations to monitor from Qlik Cloud.

Do the following:

1. Add the visualization to the Mobile Content collection in Qlik Cloud to make it available in the Qlik Analytics mobile app.
2. When in the Qlik Analytics mobile app, you can search for any visualization you have added to your personal space.
3. Click the Add to collection button to add it to your Mobile collection.

## Push notifications

Push notifications are managed in your personal settings. You can access the settings from the Qlik Cloud navigation bar in a web browser.

Push notifications are encrypted with an auto-generated personal key.

### Managing push notifications

Do the following:

1. Open your user profile menu in the activity center and select Settings.
2. Select Notifications.
3. Enable push notifications for activities related to spaces, apps, and alerts.

The push notifications are connected to web notifications. When you enable push notification for an activity, web notifications are automatically also enabled for that activity. The difference between the two is that web notifications are consumed in your activity center and push notifications are consumed in the Qlik Analytics mobile app.

### Reading notifications in the Qlik Analytics mobile app

You can read and remove notifications in the Qlik Analytics mobile app. The notifications can be found by tapping the ![notifications](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bell_dark.svg) badge.

You only receive notifications from the tenant you are logged onto.

On iOS devices, you may see a number next to the Qlik Analytics mobile app icon. This is the total notification count for all tenants you have set up in the Qlik Analytics mobile app.

## Viewing alerts

Switch to the Alerts tab to view all alerts that you own, and alerts that have been shared with you. To only see your own alerts, change the filter to Owned by you.

Information noteThe Alerts tab is not available:

- When data alerts have been disabled in the tenant, see [Managing alerts](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-managing-alerts.htm).
- When you are connected to Qlik Sense Business or Qlik Cloud Analytics Standard tenants.

Tap an alert to see more details. The following actions are available for alerts that have been shared with you.

- History: when the alert was triggered.
- Details: description, status, alert details, and notification preferences.
- Conditions: measures, dimensions, selections, and conditions used in the alert.
- Recipients: recipients of the alert.

For more information about data alerts, see [*Monitoring data with alerts*](../Alerting/monitoring-changes-with-alerts.htm).

## Logging out all mobile devices

You can be signed in to the Qlik Analytics mobile app on up to five mobile devices at the same time.

Do the following to log out of all your mobile devices:

1. In the activity center, open your profile menu and select Settings.
2. Select Qlik Sense Mobile.
3. Click Log out all devices to log out all devices listed on the page.
4. Confirm the log out.

## Setting your preferred language for the Qlik Analytics mobile app

By default, the Qlik Analytics mobile app uses the language you selected for your mobile device.

The Qlik Analytics mobile app defaults to English if the language you selected for your mobile device is not supported by Qlik Cloud.

On iOS devices, you can set your preferred language for the Qlik Analytics mobile app. This overrules the language from your mobile device.

Do the following:

1. On your iOS device, open Settings and select Qlik Sense.
2. Under Preferred language, select your language.

For more information about changing languages in Qlik Sense, see [*Changing language in Qlik Cloud*](../UserInterface/Languages.htm).
