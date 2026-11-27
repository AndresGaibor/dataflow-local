---
title: "Getting started with using Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/OfficeCommon/add-in-get-started.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office"]
---

# Getting started with using Qlik add-ins for Microsoft Office

Get started with your Qlik add-in for Microsoft Office by activating and opening it, and then using it to connect to content from your analytics app.

For information about adding content to your [template](#glossary-0 "Glossary term"), see [*Adding content to report templates with Qlik add-ins for Microsoft Office*](add-in-content.htm) and related topics.

Information noteAdd-ins must be installed before you can work with them. For information, see [*Deploying and installing Qlik add-ins for Microsoft Office*](../../Install/reporting-install-add-ins.htm).

## Applies to

This content applies to the following types of Qlik Cloud report templates:

- Excel

  [*Qlik add-in for Microsoft Excel*](reporting-add-ins.htm#Excel)
- PowerPoint

  [*Qlik add-in for Microsoft PowerPoint*](reporting-add-ins.htm#PowerPoint)
- Word

  [*Qlik add-in for Microsoft Word*](reporting-add-ins.htm#Word)

## Requirements for using add-ins

To work with Qlik add-ins for Microsoft Office, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../../Admin/mc-permissions-reporting.htm).
- [*Space permissions*](#Space)

  For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../../reporting-permissions.htm).

### Space permissions

To connect to apps in add-ins, you need certain space roles. The requirements depend on the type of space in which your app is located.

To use an add-in to generate a report template for a Qlik Sense app in a shared space, you must have, at minimum, Can edit permissions in that space.

To use an add-in to generate a report template for a Qlik Sense app in a managed space, you must have, at minimum, Can contribute or Can operate permissions in that space.

Warning noteWhile you only need Can contribute or Can operate permissions access to the app's space to connect to the app in add-ins, any report task that uses your created template will run based on the access of the report task owner. Therefore the template creator should not create a template using content located on an app sheet that they do not intend to make visible to other space members in the future (namely, a sheet that is private to them). See [*Requirements for a report task to run successfully*](../../Generate/cloud-in-app-reports-tasks.htm#Requirem2) for more information.

For more information, see [*Qlik Reporting Service permissions*](../../reporting-permissions.htm).

### Other requirements

If you are working with a Microsoft 365 web version of Excel, Microsoft PowerPoint, or Word, you need to allow pop-ups in your browser settings. However, keep the navigation history and cookies stored. Otherwise, you will need to install the add-in again every time you open the applicable Microsoft Office application.

## Activating add-ins

After a Microsoft administrator has installed a Qlik add-in for your organization, you can activate and use it if you have been given access to it.

Depending on the version of your Microsoft Office application, these steps might be slightly different. Refer to the official Microsoft documentation for full details.

Do the following:

1. Open a desktop or web version of Excel, PowerPoint, or Word.
2. Go to Home > Add-ins > Get Add-ins.
3. In the ADMIN MANAGED tab of the dialog, select the Qlik add-in.

The Qlik add-in icon is added to your ribbon bar.

[View, manage, and install add-ins for Excel, PowerPoint, and Word](https://support.microsoft.com/en-gb/office/view-manage-and-install-add-ins-for-excel-powerpoint-and-word-16278816-1948-4028-91e5-76dca5380f8d)

Information noteIf you have instead installed the add-in using sideloading or a network share, activating the add-in requires a different procedure. See [*Workflows 2-4: Self-managed installation options*](../../Install/reporting-install-add-ins.htm#Sideload).

## Opening add-ins

To open an add-in, click the Qlik icon in the ribbon bar under the Home tab.

Open the Qlik add-in by clicking the Qlik icon in the ribbon bar

![Ribbon bar in Microsoft Excel showing the Qlik add-in icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_QlikIconInRibbon.png "Click to view full size")

## Connecting to the tenant and logging in

When you open an add-in, you are prompted to connect to the Qlik Cloud[tenant](#glossary-1 "Glossary term") that the add-in was installed for. Remember that a single add-in installation configures the add-in for one specific tenant. Click Connect.

An OAuth client configuration is required to install the add-in.

You are asked to log in the first time you connect, or if the connection is closed on the server side. When using a web version of Excel, you might be required to log in again at some later point if you do not keep navigation history and cookies stored.

Do the following:

1. When prompted to log in, follow the login procedure for your Qlik account, using your tenant's identity provider configuration as applicable.
2. In the app authorization dialog, authorize the app with the OAuth client by clicking Approve. You only have to do this after your first login to the tenant.

## Selecting the Qlik Sense app for the template

After you log in, you must select the Qlik Sense space and app you want to use as source for the [template](#glossary-3 "Glossary term") you are creating. A report template uses a single app. You will only be able to add objects from one Qlik Sense app to each template file.

Do the following:

1. Under Space, select the Qlik Cloud Analytics space.
2. Under App, select the Qlik Sense app from the space.
3. Click Save.

After the app has been loaded and its metadata is populated into the file, you can click ![Open external file or application](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_goto.svg) to open the source app in Qlik Cloud.

After the template is connected to a source app, you can return to the ![Home](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) tab in the add-in to change the app. For more information, see [*Changing the connected Qlik Sense app*](#Changing).

## Availability of sheets in the app

When you log into a Qlik add-in for Microsoft Office, you will only see content you have access to in the source Qlik Sense app. For example, for an app in your [personal space](#glossary-4 "Glossary term"), you can access all content. For an app in a shared space, you can only see and use content which is public in the app or private to you. Content from another user's private [sheet](#glossary-5 "Glossary term") in a shared space app cannot be seen or used.

## Previewing the report

When developing a [template](#glossary-6 "Glossary term"), you will likely need to check that the output it will create is what you want. Preview the report to see what it will look like without configuring report tasks and emailing them to yourself.

To preview your report, click on the ![Download](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) icon in the top right toolbar of the add-in. Depending on which Microsoft Office application you are using, you have the following options:

- Preview as Excel
  (.xlsx)
- Preview as PowerPoint
  (.pptx)
- Preview as Word
  (.docx)
- Preview as
  PDF

When opening a report preview in PDF format, the report uses the current language from your Excel settings to apply regional formatting (for dates, numbers, and so on).

Depending on your browser configuration, your report will either appear in a browser window, or download to your computer. If you do not see a report, verify that you have allowed pop-ups in your browser.

Open the generated file to check the results.

## Preparing for PDF and printed output

If your report will be generated in PDF format or printed, you might need to adjust the print settings in your template. Use the native features in your Microsoft Office application to prepare the template.

Some of these page setup configurations might include:

- Paper size
- Page orientation
- Selected print area
- Page breaks

The navigation experience for configuring print area and page setup may depend on:

- Whether you are working with Excel, PowerPoint, or Word
- Your operating system
- Your web browser

Later, when you configure report output, you can define the locale for region-dependent formatting in the reports. This includes formatting of dates, numbers, and other information. Where you configure this setting will depend on your use case:

- Task-based reports: Regional format settings when configuring a report task.

  [*Part 3: Configure the output*](../../Generate/cloud-in-app-reports-tasks.htm#ConfigureOutput)
- Generation of on-demand reports: Preferred language setting in your personal settings (to configure these settings, click your user profile icon and select Settings.).

  [*Region-dependent formatting*](../../OnDemand/reports-on-demand-create.htm#Localiza)
- When opening a report preview in PDF format, the report uses the current language from your Excel settings to apply regional formatting (for dates, numbers, and so on).

## Opening the source object in Qlik Sense

You can inspect the source object for report content by opening it in the Qlik Sense app.

Do the following:

1. In the add-in window, click the ![Home](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) tab in the toolbar.
2. Under Source app, click ![Open external file or application](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_goto.svg).

If the source object is a chart, you are brought to the Qlik Sense app to view the corresponding sheet. You might need to log in to Qlik Cloud again for the app to open.

## Saving your work

Save the Excel, PowerPoint, or Word file as you normally would. You can re-open the file as usual and you will see your template.

## Finding the add-in version and connected server address

You can find the add-in version and the Qlik Cloud[tenant](#glossary-7 "Glossary term") (server) address.

Do the following:

1. In the add-in window, click the ![Home](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) tab in the toolbar.
2. Next to Source app, click ![More](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Click About.
4. View the tenant URL and Office Add-in version, as well as the Qlik Sense app's space and name.

## Synchronizing the add-in with the Qlik Cloud tenant

If there are changes in the connected Qlik Cloud tenant, the Excel, PowerPoint, or Word file that uses the add-in is not updated automatically. For example, you might need to refresh:

- The list of available spaces you can work with.
- The list of available apps you can work with.
- The list of available entities in the selected Qlik Sense app.
- The chart images you have used in the template. For example, if you have made selections in the source Qlik Sense app, you might want your chart images to reflect the selections in the image placeholders.
- The status of images and tables you have used in the template (for example, because they were deleted or their titles have changed).

Follow the steps below to refresh the connection metadata.

Do the following:

1. In the add-in window, click the ![Home](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) tab in the toolbar.
2. Next to Source app, click ![More](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Click Refresh all images.

This applies a global refresh. You can also perform refreshes of some individual entities and objects in the other tabs in the add-in. The ![Reload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) icon is present when these are available.

The data and objects in a template will not update when the Qlik Sense app is edited, unless a refresh is applied.

## Sharing report template files

[Template](#glossary-8 "Glossary term") files created with Qlik add-ins for Microsoft Office contain only tags and preview images. If another user wants to edit and preview the template, they must have:

- The Qlik add-in installed in their version of Excel, PowerPoint, or Word.
- Access to the Qlik Cloud tenant.
- If the app is in a [shared space](#glossary-9 "Glossary term"): Can view or higher space role in the space, or to the app (so they can connect to the app in the add-in, and access its data).
- If the app is in a [managed space](#glossary-10 "Glossary term"): Has restricted view or higher space role in the space, or to the app (so they can connect to the app in the add-in, and access its data).

However, a [report template](#glossary-11 "Glossary term") is a normal Excel, PowerPoint, or Word file that contains the data available when the preview was created. You can share the template file with anyone, but only users with access to the source app will be able to connect to it in the add-in and apply refreshes. For more information about global refreshes, see [*Synchronizing the add-in with the Qlik Cloud tenant*](#Synchron).

## Changing the connected Qlik Sense app

A report template can generate reports from a single Qlik Sense app. You can change the connected Qlik Sense app before or after adding content to the template.

For templates with content already added, the new app must contain the same object IDs as the app that the template is currently connected with. This workflow is intended for apps that are duplicated, moved between spaces or tenants, or published to a managed space.

Before you change the template connection, it is recommended that you create a backup copy of the template.

### Connecting to a different app in the tenant

Do the following:

1. In the add-in window, click the ![Home](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) tab in the toolbar.
2. Next to Source app, click ![More](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Click Edit source app.
4. Select the Space and App, and click Save.

### Changing the tenant and app

1. In the add-in window, click the ![Home](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) tab in the toolbar.
2. Next to Source app, click ![More](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Click Edit source app.
4. The current Qlik Cloud tenant is shown. Click Change tenant.
5. Enter the new Qlik Cloud tenant and Qlik Sense app IDs.

   Tip noteYou can copy and paste the app ID directly from the URL when you have the app open.
6. Click Save.
7. Close the add-in or refresh the page.

If you change the tenant, the manifest file for the new tenant must be installed to be able to edit the template.

### Changing the connected app in Qlik Sense

Alternatively, you can change the connected app within the Reporting section in the new Qlik Sense app. This is useful when you have created a new copy of the original Qlik Sense app. For example, you have published the app to a managed space, or duplicated, migrated, or transferred it.

For more information, see [*Uploading a report template*](../../Generate/cloud-in-app-reports-templates.htm#UploadTemplate).

## Searching for Qlik Sense objects in add-ins

You can find a specific Qlik Sense object by expanding and scrolling the list that appears on the right after clicking on the add button or you can insert a string in the search form. After pressing Enter, it will search for the string in the following fields of the inserted Qlik Sense app:

- Object ID
- Object name (Sheets included)
- Type of chart

To find the correct object quickly, it is important to use correct naming conventions while developing Qlik Sense apps.

## Accessing error messages

There are native error messages in Qlik add-ins for Microsoft Office. To assist in error reporting when contacting Qlik, check the error messages in your browser’s developer tools, in the JavaScript console and Network tabs.

## Best practices for app object naming

The way in which you name the objects in your Qlik Sense app can affect the effectiveness and usability of your report templates. For a list of best practices, see [*Best practices for in-application reporting*](../../InAppGeneral/reporting-best-practices.htm).
