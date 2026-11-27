---
title: "Deploying and installing Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Install/reporting-install-add-ins.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office"]
---

# Deploying and installing Qlik add-ins for Microsoft Office

Expand/Collapse all

# Deploying and installing Qlik add-ins for Microsoft Office

Deploy and install Qlik add-ins for Microsoft Office to allow users in your organization to create [report templates](#glossary-0 "Glossary term"). Upload report templates created with the add-ins into the Qlik Cloud application to generate report output from [report tasks](#glossary-1 "Glossary term").

Qlik add-ins for Microsoft Office can be deployed and installed for compatible web and desktop versions of Excel, PowerPoint, and Word within Microsoft 365.

Add-ins are installed using a manifest file. This manifest file is required for the Microsoft 365 administrator (or possibly a user, in certain installation methods) to deploy and install add-ins for themselves or users in their organization. A manifest file allows installation of add-ins for a single Qlik Cloud [tenant](#glossary-2 "Glossary term").

Information noteAn OAuth client configuration is required to generate a manifest file and link. For instructions, see [*Prepare and obtain the add-in manifest*](#Manifest).

## What are Qlik add-ins for Microsoft Office?

Qlik add-ins for Microsoft Office are:

- Qlik add-in for Microsoft Excel
- Qlik add-in for Microsoft PowerPoint
- Qlik add-in for Microsoft Word

Functionality is similar across the add-ins. In the add-in window, you can add application content in the form of tables, images, variables, and expressions. After adding content using the add-ins, you have several options for formatting and styling it using the default Microsoft Office functionality.

## Choose an installation workflow

After you obtain the manifest file or URL, choose the workflow that matches how you want to deploy the add-in:

- Workflow 1: Centralized deployment for managed distribution by a Microsoft 365 administrator. See [*Workflow 1: Centralized deployment*](#Centrali).
- Workflow 2: Sideloading on the web for quick testing without centralized deployment. See [*Workflow 2: Sideload an add-in on the web*](#Workflow2Web).
- Workflow 3: Installation on desktop Microsoft Office applications through a Windows network share. See [*Workflow 3: Install an add-in on desktop Microsoft Office applications using a Windows network share*](#Workflow3Windows).
- Workflow 4: Sideloading on desktop macOS applications. See [*Workflow 4: Sideload an add-in on desktop macOS applications*](#Workflow4Mac).

Workflow 1 is the recommended option for production deployments. Workflows 2 through 4 are best for testing, trial use, or isolated user setups.

Qlik add-in button shown in a web version of Microsoft Excel

![Ribbon bar in Microsoft Excel showing the Qlik add-in icon to indicate the add-in has been activated](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_QlikIconInRibbon.png "Click to view full size")

For more information, see [*Designing report templates with Qlik add-ins for Microsoft Office*](../Design/OfficeCommon/reporting-add-ins.htm).

## Before you start

These steps apply to all installation workflows.

- Ensure you and your users meet the system and software requirements.

  [*System and software requirements*](#SystemReqsAddIns)
- Create an OAuth client in Qlik Cloud.

  [*Create an OAuth client*](#Creating)
- Obtain the manifest file or link.

  [*Prepare and obtain the add-in manifest*](#Manifest)

### Requirement 1: Meet system and software requirements

System and software requirements

Qlik Cloud Government note

Qlik add-ins for Microsoft Office are supported for developing report templates against applications in Qlik Cloud Government or Qlik Cloud Government - DoD tenants.

To install and use Qlik add-ins, users must meet the following requirements.

#### Qlik add-in for Microsoft Excel

For Windows installations:

- Windows 10 v.1903 or higher
- Microsoft 365 v.16.0.11629 or higher

For macOS installations:

- macOS v.14 or higher
- Microsoft 365 v.16.83 or higher

Also, to run the Qlik add-in for Microsoft Excel, you must have a Microsoft Excel installation with ExcelAPI 1.9 or newer. To check if your Excel installation is compliant, refer to the official Microsoft documentation at [Excel JavaScript API requirement sets](https://learn.microsoft.com/en-us/javascript/api/requirement-sets/excel/excel-api-requirement-sets?view=common-js-preview).

If your ExcelAPI is lower than the minimum required version, an error is shown indicating that the Qlik add-in requires a newer version of Microsoft Excel.

Example of an error message during installation of the add-in

![Error message during Qlik Excel add-in installation showing that user's Microsoft Excel version is too old to support the add-in](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_ExcelVersionError.png "Click to view full size")

You may need to click on the white area on the right in Microsoft Excel and press F5 to update the page to see the error.

If you see this error, upgrade your Microsoft Excel installation.

#### Qlik add-in for Microsoft PowerPoint

For Windows installations:

- Windows 10 v.1903 or higher
- Microsoft 365 version 2504 (build 18730.20030) or higher

For macOS installations:

- macOS v.14 or higher
- Microsoft 365 v.16.96 or higher

#### Qlik add-in for Microsoft Word

For Windows installations:

- Windows 10 v.1903 or higher
- Microsoft 365 version 2208 (build 15601.20148) or higher

For macOS installations:

- macOS v.14 or higher
- Microsoft 365 v.16.64 or higher

### Requirement 2: Create an OAuth client

Create an OAuth client

An OAuth client configuration is required to install Qlik add-ins for Microsoft Office. Add-ins are used by report developers to prepare [report templates](#glossary-3 "Glossary term") for in-application reporting with Qlik Cloud.

For OAuth to work in the add-ins, the OAuth client needs to be configured with the exact configuration shown below.

Do the following:

1. In Qlik Cloud, click ![Open Navigation menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg) in the top left corner.
2. Select Administration.
3. Go to OAuth.
4. Click Create new.
5. In the Client type dropdown menu, select Single-page app. More fields will appear.
6. Insert a Name. The Description is optional.
7. At minimum, select the checkbox to include the user\_default scope. You can include other scopes in the configuration, but without user\_default, installation will not work.

   See [*Available OAuth scopes*](../../Admin/oauth-scopes.htm#Availabl) for a full description of each available scope.
8. In the Add redirect URLs field, insert the URL of the Qlik Cloud tenant, followed by this fixed string: /office-add-ins/oAuthLoginSuccess.html

   The result should look like this: https://<tenant or alias hostname>.<region>.qlikcloud.com/office-add-ins/oAuthLoginSuccess.html. For example: http://example-company-123.us.qlikcloud.com/office-add-ins/oAuthLoginSuccess.html
9. Click Add.
10. In the Add allowed origins field, insert your tenant URL and click Add.
11. Click Create.
12. The Copy your Client ID window appears. You can choose to copy the Client ID to clipboard, or click Done to close the window.

After creating the OAuth client, get the updated manifest XML link from the Administration activity center. Go to the Settings page and select the Email and reports tab. In the Qlik add-ins for Microsoft Office section, retrieve the link you can use to deploy and install the add-in.

### Requirement 3: Prepare and obtain the add-in manifest

Prepare and obtain the add-in manifest

You install Qlik add-ins for Microsoft Office in the Microsoft environment using a manifest XML file, or a link to it.

- For centralized deployment, the manifest often needs to be provided in the form of a URL.
- For self-managed installations, the manifest is often provided in the form of a file.

A manifest file is specific to a single Qlik Cloud [tenant](#glossary-4 "Glossary term"). You use the same manifest file to install the add-ins for Excel, PowerPoint, and Word.

An OAuth client configuration is required to install the add-in. After you have configured the OAuth client, obtain the manifest file link, as well as the manifest file itself, from the Administration activity center.

Do the following:

1. Create the OAuth client in the Qlik Cloud tenant using the required configuration. For full instructions, see [*Create an OAuth client*](#Creating).
2. In Qlik Cloud, click ![Open Navigation menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg) in the top left corner.
3. Select Administration.
4. Go to Settings.
5. In the Sharing and reports section, go to Qlik add-ins for Microsoft Office.
6. In the drop down menu, select the OAuth client configuration you have set up for activating OAuth in the add-in.
7. Click Download to download the manifest, or Copy to copy the link to it.

## Workflow 1: Centralized deployment

It is recommended that Qlik add-ins for Microsoft Office are made available with centralized deployment and installation. Centralized deployment requires action from a Microsoft 365 administrator in your organization.

With centralized deployment, the add-in manifest is loaded into your organization’s Microsoft 365 admin center and distributed to users as a pre-configured installation. Distribution can be restricted to members of specific security groups.

Information noteWith centralized deployment, add-ins are installed for Excel, PowerPoint, and Word. There is no option to install add-ins individually.

Use this workflow when:

- You want the add-ins to be permanently installed for members of your organization
- You want to manage distribution to your organization members

Warning noteDeployment of Qlik add-ins for Microsoft Office is not tied to access to the Qlik Cloud tenant. If you distribute add-ins to users who do not have access to Qlik Cloud, they will be able to view and start the add-ins. However, the add-ins will prompt the user to log into Qlik Cloud. Functionality will be blocked if login is not successful.

Complete the following sections in order.

### Deploy and install with the Microsoft 365 admin center

Centralized deployment is completed by a Microsoft 365 system administrator.

Do the following:

1. Obtain the add-in manifest file or manifest URL after creating an OAuth client. See [*Prepare and obtain the add-in manifest*](#Manifest).
2. Distribute the add-in according to the official Microsoft documentation: [Deploy and publish Office Add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/publish/publish). Note that distribution through centralized deployment is only possible by using the Microsoft 365 admin center.

With the above procedure, the add-ins are installed for users who are given access to them. Users then activate add-ins in their version of Excel, PowerPoint, or Word.

### Activate an add-in after centralized deployment

After a Microsoft administrator has installed a Qlik add-in for your organization, you can activate and use it if you have been given access to it.

Depending on the version of your Microsoft Office application, these steps might be slightly different. Refer to the official Microsoft documentation for full details.

Do the following:

1. Open a desktop or web version of Excel, PowerPoint, or Word.
2. Go to Home > Add-ins > Get Add-ins.
3. In the ADMIN MANAGED tab of the dialog, select the Qlik add-in.

The Qlik add-in icon is added to your ribbon bar.

[View, manage, and install add-ins for Excel, PowerPoint, and Word](https://support.microsoft.com/en-gb/office/view-manage-and-install-add-ins-for-excel-powerpoint-and-word-16278816-1948-4028-91e5-76dca5380f8d)

### Remove an add-in

If your installation uses a centralized deployment, you might not be able to uninstall the add-in. This depends on the policy used by your Microsoft 365 administrator.

## Workflows 2-4: Self-managed installation options

Sideloading and network share installation are suitable ways to quickly obtain access to add-ins for testing or trial purposes. They are not suitable methods for deploying add-ins for production and enterprise-scale use cases.

Warning noteTo self-install add-ins using sideloading or network share, you may need permissions from your organization and on your local machine. These permissions may be managed by your organization or Microsoft 365 administrator. If you are unable to self-install an add-in, consult [the official Microsoft documentation for Office add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/), or contact your system administrator.

Warning noteDownloading the manifest and sideloading add-ins is possible without restrictions. It is possible to install the manifest even if you do not have access to Qlik Cloud. However, you are immediately prompted to log into Qlik Cloud after installation. Add-ins will not work if you are not logged in.

Qlik Cloud Government note

In Office 365 Government Community Cloud High (GCCH), Qlik add-ins for Microsoft Office can only be installed via [centralized deployment](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Install/reporting-install-add-ins.htm#Centrali). Installing via sideloading or network share is not supported.

Depending on your version of Excel, PowerPoint, or Word, as well as other factors, add-ins loaded with these methods might eventually be removed from your ribbon bar. When this happens, re-upload the manifest into the Microsoft Office application.

### Workflow 2: Sideload an add-in on the web

Workflow 2: Sideload an add-in on the web

To sideload an add-in using Excel, PowerPoint, or Word on the web, the user uploads the manifest file to their browser.

Sideloading is supported by Microsoft 365 web versions of Excel, PowerPoint, or Word.

Use this workflow when:

- You need to access the add-in quickly.
- You want to test add-in functionality in isolation.
- You want to test the add-in without requiring intervention from a Microsoft 365 administrator.

Do the following:

1. Prepare and download the manifest file. See [*Prepare and obtain the add-in manifest*](#Manifest).
2. Open Microsoft Office on the web at <https://office.live.com/>.
3. Open a new Excel, PowerPoint, or Word document.
4. In the Home tab, click Add-ins.
5. Click Advanced... or Office Add-ins.
6. In the Office Add-ins dialog, click Upload My Add-in.
7. Browse to the add-in manifest file, and then select Upload.
8. If required, sign into your Qlik Cloud account.

#### Removing a sideloaded add-in

To remove a sideloaded add-in, clear the cache of the web browser with which you are using the add-in.

### Workflow 3: Install an add-in on desktop Microsoft Office applications using a Windows network share

Workflow 3: Install an add-in on desktop Microsoft Office applications using a Windows network share

To install add-ins on a desktop version of Excel, PowerPoint, or Word without centralized deployment, you can set up a network share and load the manifest into it. This can only be done on a Windows operating system.

Follow the guidelines below to sideload add-ins via network share. The instructions are adapted from the official Microsoft documentation. See [Sideload Office Add-ins for testing from a network share](https://learn.microsoft.com/en-us/office/dev/add-ins/testing/create-a-network-shared-folder-catalog-for-task-pane-and-content-add-ins) or other Microsoft resources for more information.

#### Step 1: Create and share a folder

Do the following:

1. Create a folder to host the Qlik add-in. For example: C:\Qlik Office add-ins
2. In the Windows File Explorer, go to the parent folder, or drive letter, of the folder you want to use as your shared folder catalog. For example: C:\
3. Right-click the folder and select Properties.
4. Open the Sharing tab and then click the Share... button.

   Share... button

   !['Share...' button in dialog when configuring Windows network share](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SideloadNetworkShare_Share.png "Click to view full size")
5. In the dialog window, add yourself and any other users and/or groups with whom you want to share your add-in. You will need at least Read/Write permission to the folder. After you have finished choosing people to share with, click Share.
6. When you see confirmation that your folder has been shared, make note of the full network path that is displayed immediately following the folder name. Click Done to close the dialog window.

   Confirmation of successfully shared folder with full network path

   ![Network access dialog confirmation of successfully shared folder with full network path](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SideloadNetworkShare_ShareConfirmation.png "Click to view full size")
7. Click Close to close the Properties dialog window.

#### Step 2: Manually configure the shared folder as a trusted catalog

Do the following:

1. Open a new blank workbook in the desktop version of Excel, PowerPoint, or Word.
2. Click the File tab, and then click Options in the bottom left corner.
3. Click Trust Center, and then click the Trust Center Settings... button.

   Trust Center Settings... button

   !['Trust Center Settings...' button in Microsoft Excel options](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SideloadNetworkShare_TrustCenterSettings.png "Click to view full size")
4. Click Trusted Add-in Catalogs.

   Trusted Add-in Catalogs tab

   !['Trusted Add-in Catalogs' button in Microsoft Excel Trust Center](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SideloadNetworkShare_TrustedCatalogs.png "Click to view full size")
5. In the Catalog Url box, enter the full network path to the folder that you shared previously.
6. Click Add catalog.
7. Check the Show in Menu checkbox for the newly added item, and then click OK to close the Trust Center dialog window.

   Trusted Add-in Catalogs tab in Trust Center dialog, with newly added catalog path

   !['Trusted Add-in Catalogs' tab with newly added catalog URL](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_SideloadNetworkShare_CatalogURL.png "Click to view full size")
8. Click OK to close the dialog window.
9. Close and re-open the application so your changes take effect.

#### Step 3: Sideload the add-in

Do the following:

1. Add the add-in manifest XML file to the shared folder.
2. In ExcelPowerPoint, or Word, click Add-ins on the Home tab of the ribbon.
3. Click More Add-ins.
4. Click SHARED FOLDER at the top of the Office Add-ins dialog box.
5. Select Qlik to insert the add-in.
6. You might see a dialog window that says something like the following: Qlik wants to display a new window. Click Allow.

#### Removing an add-in installed through network share

Do the following:

1. If you have Excel, PowerPoint, or Word open, close it.
2. Delete the contents of this folder: %LOCALAPPDATA%\Microsoft\Office\16.0\Wef\

### Workflow 4: Sideload an add-in on desktop macOS applications

Workflow 4: Sideload an add-in on desktop macOS applications

For macOS, add-ins can be installed on Microsoft 365 desktop versions of Excel, PowerPoint, or Word. For the system and software requirements, see [*System and software requirements*](#SystemReqsAddIns).

Follow the guidelines below. The instructions are adapted from the official Microsoft documentation. For full instructions, refer to the official Microsoft documentation: [Sideload an add-in in Office on Mac](https://learn.microsoft.com/en-us/office/dev/add-ins/testing/sideload-an-office-add-in-on-mac#sideload-an-add-in-in-office-on-mac)

Do the following:

1. Open the Finder application on your computer.
2. Enter the following keyboard combination: Command+Shift+G

   The Go to folder menu opens.
3. Enter one of the following paths depending on the Microsoft Office application:

   - Excel: /Users/<username>/Library/Containers/com.microsoft.Excel/Data/Documents/wef
   - PowerPoint: /Users/<username>/Library/Containers/com.microsoft.Powerpoint/Data/Documents/wef
   - Word: /Users/<username>/Library/Containers/com.microsoft.Word/Data/Documents/wef

   It could happen that the wef folder does not exist on your computer yet. If so, create it in this location.
4. In the wef folder, add a copy of the XML manifest file.
5. Open Excel, PowerPoint, or Word. If you already have it open, you will need to restart it.
6. In the ribbon bar, navigate to Home > Add-ins.
7. Select the Qlik add-in.

The Qlik add-in should now be available in your ribbon bar.

#### Removing a sideloaded add-in from desktop macOS applications

To remove the Qlik add-in, you need to clear the Office cache on your computer. For more information, see:

- [Remove a sideloaded add-in](https://learn.microsoft.com/en-us/office/dev/add-ins/testing/sideload-an-office-add-in-on-mac#remove-a-sideloaded-add-in)
- [Clear the Office cache](https://learn.microsoft.com/en-us/office/dev/add-ins/testing/clear-cache)

## Adding multiple Qlik add-ins to Excel, PowerPoint, or Word

Each added Qlik add-in allows use of the add-in for a single Qlik Cloud [tenant](#glossary-5 "Glossary term").

Behavior and limitations are as follows:

- In your Excel, PowerPoint, or Word application, only one add-in (connected to a single Qlik Cloud tenant) is supported for use at a single time.
- If you need to work with add-ins for multiple Qlik Cloud tenants, you must switch between tenants by deploying or installing the add-in you want to use directly before you start to use it. If your add-in is still connecting to the previously selected tenant, restart your Office application or reload the browser page.
- Having a Qlik add-in [centrally deployed](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Install/reporting-install-add-ins.htm#Centrali) for one Qlik Cloud tenant may prevent your ability to sideload the add-in for different tenants.
- Depending on your version of Microsoft Excel, PowerPoint, or Word, and the browser in use, when multiple add-ins are loaded, the ribbon bar might show icons for each of them, or only one icon holding the latest deployed instance. The former can happen, for example, when using older versions of Microsoft Excel, PowerPoint, or Word.
- In Office 365 Government Community Cloud High (GCCH), Qlik add-ins for Microsoft Office can only be installed via [centralized deployment](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Install/reporting-install-add-ins.htm#Centrali). Installing via sideloading or network share is not supported. Office 365 GCC and GCCH support working with a single Qlik Cloud Government or Qlik Cloud Government - DoD tenant at a time.

## Troubleshooting

This section provides tips for resolving common deployment and installation issues.

For additional troubleshooting tips, see [*Troubleshooting - In-application reporting*](../../Troubleshooting/troubleshooting-reporting.htm).

Blank dialog shown during authentication after deployment of a Qlik add-in for Microsoft Office

When a user tries to authenticate to a reporting add-in for Microsoft Excel, Microsoft PowerPoint, or Microsoft Word, their authentication pop-up dialog might be blank. Alternatively, the user could instead see an error in the dialog (particularly, 12006).

For a user to work with a Qlik add-in for Microsoft Office, the authentication flow requires a redirect between your [tenant](#glossary-6 "Glossary term") and the identity provider hosted in a different domain. Your identity provider is setting a Cross-Origin-Opener-Policy with restrictive settings. As a result, the cross-domain communication part of the authentication flow is blocked, preventing login information to be correctly returned to the add-in.

Proposed action

The following resolution should be performed by a network administrator who is responsible for setting up identity providers.

Do the following:

- Set the response header from your IDP to your dialog to:

  Cross-Origin-Opener-Policy: unsafe-none

For more information, refer to the official Microsoft documentation: [Best practices and rules for the Office Dialog API](https://learn.microsoft.com/en-us/office/dev/add-ins/develop/dialog-best-practices)

Pop-ups not allowed when first opening a Qlik add-in for Microsoft Office

You might see the following error message when you first open the Qlik add-in for Microsoft Office after activating it:

The security settings in your browser prevent us from creating a dialog box.

Possible cause

Your web browser is blocking the add-in authentication dialog from opening as a pop-up.

Proposed action

If you are using a web version of the Microsoft Office application, you need to allow the browser to open pop-ups. This depends on your browser and version, but possible solutions include:

- Selecting an option in the web address bar to allow the pop-ups.
- Opening the browser settings and selecting the option to allow pop-ups.

## Learn more

- [*Creating and managing OAuth clients*](../../Admin/mc-create-oauth-client.htm)
