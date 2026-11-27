---
title: "Managing Data Movement gateway in the Administration activity center"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Gateways/dm-gateway-managing-console.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Qlik Data Gateway - Data Movement"]
---

# Managing Data Movement gateway in the Administration activity center

This topic describes how to manage your Data Movement gateways.

## Editing the Data Movement gateway properties

Information noteIf you need to update the registration key, follow the procedure described in [*Managing the Data Movement gateway server*](dm-gateway-managing.htm#Updating).

1. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways.
2. Click the ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the row, and select Edit.

   The Edit data gateway dialog opens.
3. Update the properties as needed, and then click Save.

## Enabling and disabling Data Movement gateway

1. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways.
2. Do one of the following:

   - Select the check box at the beginning of the row and click the Enable or Disable toolbar button.
   - Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the row, and select Enable or Disable.
3. Confirm the action.

Warning noteAfter enabling the Data Movement gateway, you must restart the gateway service. For details, see [*Data Movement gateway service commands*](dm-gateway-managing.htm#Restarti)..

## Deleting Data Movement gateway

1. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways.
2. Do one of the following:

   - Select the check box at the beginning of the row, and click the Delete toolbar button.
   - Click the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button at the end of the row, and select Delete.
3. Confirm the deletion.

## Setting notifications for a Data Movement gateway

### Notifications for a specific Data Movement gateway

You can set notifications to be alerted at changes in the operation of your data gateway. You can get a notification in your browser, by email, or a push message to the Qlik Analytics mobile app.

1. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways.
2. Click ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a data gateway, and select Notifications.
3. Select which events to receive a notification for.

   Notifications are available for the following events:

   - Data gateway state has changed
   - Data gateway version requires an update

     Information noteThis notification will only be sent in the rare case of Qlik forcibly deactivating the gateway (usually due to a critical issue).
4. Click Done.

You can view and edit gateway-specific notifications in your settings. You can find them under Settings > Notifications > Custom notifications > Data gateways.

### Notification for a new Data Movement gateway version

Click your profile icon in the top right. Then, go to Settings > Notifications > Data gateways, where you will be able to set the following additional notification:

- New data gateway version is available

When enabled, the notification will be sent to the data gateway creator only, whenever a new Data Movement gateway version becomes available for download.

## Executing a task run after a missed schedule

Sometimes a network issue might result in the connection to Data Movement gateway being lost. If the connection to Data Movement gateway is not restored before the next scheduled run, the data task will not be able to run as scheduled. In such cases, you can choose whether or not to execute a run immediately after the connection is restored.

To do this

1. Select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways.
2. In the toolbar above the Data gateways list, click Data Movement gateway settings.
3. Choose one of the following Run missed scheduled tasks options:

   - As soon as possible and then as scheduled if it's important to run a task before the next scheduled instance
   - As scheduled to run the task at the next scheduled instance
4. Save your settings.

## Data Movement gateway properties

To access the Data gateways table, select Administration from the launcher menu (![Launcher menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg)), and then select Data gateways. The Data gateways table shows basic information about each data gateway.

Data gateway properties

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DMgateways-table.png "Click to view full size")

The table columns are as follows:

- Name – The name specified when the data gateway was created.
- Type – Should be Data Movement gateway.
- Version - The current version. For more information, see [*Upgrading and uninstalling Data Movement gateway*](dm-gateway-upgrading.htm).
- Description – The description provided when the data gateway was created.
- Data gateway ID – A unique identifier, which might be useful for troubleshooting purposes.
- State – Can be one of the following:

  - Connected
    - Indicates that the data gateway service has established a connection with Qlik Cloud.
  - Disconnected
     - If the status is Disconnected, start the data gateway service as described above.
  - Disabled
    - The data gateway is disabled in the Administration activity center.
  - Establishing session - Shown when the data gateway establishes a connection to the data source.
- Space - The space with which the data gateway is associated.
- Date created – When the data gateway was created.
