---
title: "QlikView applications in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikViewInCloud/using-QV-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data"]
---

# QlikView applications in Qlik Cloud

You can upload and access QlikView applications in Qlik Cloud. You can also share QlikView applications with other users by publishing them in spaces.

QlikView applications are compatible with Qlik Cloud. QlikView users that want to use QlikView applications in a cloud environment must have a unified license. The unified license became available with the April 2019 releases of QlikView and Qlik Sense.

For more information on licensing for QlikView, see [Licensing QlikView](/en-US/qlikview/September2026/Subsystems/Server/Content/QV_Server/QlikView-Server/QVSRM_Licensing.htm).

You can add QlikView applications to Qlik Cloud in the following ways:

- Publish them from the QlikView Publisher: [*Publishing QlikView applications and links*](#Publishi)
- Uploading them directly in the Analytics [activity center](#glossary-0 "Glossary term"): [*QlikView applications in Qlik Cloud*](#Uploadin)

Information noteIn Qlik Sense Business, you can only upload QlikView documents.

## Publishing QlikView applications and links

QlikView applications have the same purpose as Qlik Sense applications, but have a different interface and different available features. In the cloud environment, QlikView applications are view-only. You can explore the visualizations in the application, but you cannot edit the application or add your own sheets to the application. You can share QlikView applications with other users by adding them to managed and shared spaces.

Qlik Cloud members with administrators rights for a QlikView Server environment can distribute QlikView documents, and links to documents, to Qlik Cloud. QlikView documents open directly in the activity center.
Applications distributed to Qlik Cloud can only be distributed to managed spaces.

You can publish documents and links in Qlik Cloud.

Links that are published in Qlik Cloud redirect you outside the cloud environment, into the QlikView AccessPoint where the QlikView document is opened.
The user must be able to access the QlikView Server.

[*Publishing QlikView documents and links in Qlik Cloud*](QMC_Documents_DistributeToCloud.htm)

Qlik Cloud members can also upload QlikView applications to personal spaces in the Analytics activity center, and publish them in managed or shared spaces. To learn how to upload a QlikView application in the Qlik Cloud, see [*QlikView applications in Qlik Cloud*](#Uploadin).

### QlikView applications and QlikView documents

In a QlikView environment, QlikView files are called documents and are in .qvf format or .qvw format. In a cloud environment QlikView files are called applications and are in .qvf format. When a QlikView document in .qvw format is uploaded to Qlik Cloud, the file is automatically converted from .qvw to .qvf to make it compatible with the cloud environment.

Converting a QlikView document into a QlikView application allows Qlik Cloud members to open and interact with the QlikView content in the cloud environment.
This conversion, however, brings some feature limitations. To learn more about QlikView application supported and unsupported functionality, see: [*Working with QlikView applications in Qlik Cloud Analytics*](#Working)

## Uploading and sharing a QlikView application in Qlik Cloud

You can manually upload a QlikView file (.qvf or .qvw) to Qlik Cloud from the QlikView publisher folder or any other preferred location in your Windows environment. Once uploaded, the application resides in your personal space. You can then share it to shared spaces, and publish it to managed spaces for which you have “Can publish” permission.

Information note

If you want QlikView applications uploaded to Qlik Cloud to include filters in Excel exports, before uploaded the QlikView application in Document Properties > Variables, under Setting for Selected Variable, you must select Include in bookmarks.

Do the following:

1. Select a QlikView file (.qvf or .qvw) that you want to upload to Qlik Cloud.

Tip noteQlikView files can be uploaded from any local or remote location. If you are uploading a QlikView file from the publisher folder in a QlikView Server environment, it is good practice to first reload the file from the QlikView Management Console, to make sure it is updated to the latest version.

2. In Qlik Cloud, upload the QlikView file to your personal space. In Analytics, go to the Create page of the Analytics activity center and select Upload.
3. Share the QlikView application with other members
   by publishing it in managed spaces or by sharing it in shared spaces.
   - Choose one or more managed spaces where you want to publish the QlikView application. Managed spaces are created by the tenant or analytics administrator, or by users with the ManagedSpaceCreator role.
      For detailed documentation, see
     [Working in managed spaces.](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-managed-spaces.htm)
   - Choose a shared space where you want to share the QlikView application. For detailed documentation, see [Working in shared spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/working-in-shared-spaces.htm).

## Working with QlikView applications in Qlik Cloud Analytics

From the Qlik Cloud Analytics activity centers, you can interact with QlikView applications in the same way as Qlik Sense applications. QlikView applications can be added to collections. Unlike Qlik Sense applications, QlikView applications in the Qlik Cloud are view only.
QlikView applications can be shared with other users using shared spaces. Community or shared content cannot be added to them by other users.

Information noteOpening QlikView applications in Qlik Cloud establishes a connection over the WSS (WebSocket Secure) protocol. Therefore, make sure that your firewall and proxy server (if you intend to use one) are set up to allow outbound WSS connections.

Each application in Qlik Cloud displays the application name, description, owner, and the modification date.
You can click on the application to open it. You can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view more options for the application including:

- Share

  Copy a link to the QlikView application.
- Details

  Details provides an overview of application information. It shows the dates of application creation, and last modification. Details also shows the tags applied to the application and who can access the application. You can also view the managed spaces to which the application has been published. You can also view the application ID and unique application views.
- Manage

  Management options for the QlikView application. The following options are available:

  - Favorite

    Add the QlikView application to your Favorites.
  - Add to collection

    You can add the QlikView application to a collection.

    [*Collections*](../QlikCloudNavigation/Analytics-activity-center.htm#Collecti)
  - Edit details

    You can change the application name, description, tags, and space.

    [Editing application details](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/edit-app-cloud-hub.htm)
  - Publish to space

    You can publish applications from a personal or shared space. You must have Can publish permission in the managed spaces to which you are publishing.

    [Publishing applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/publish-app-cloud-hub.htm)
  - Published copies

    View and manage published copies of the application.
  - Move to space

    You can move the application to another space.

    [Moving applications](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/move-apps-cloud-hub.htm)
  - Duplicate

    You can duplicate the application.
- Delete

  You can delete any application you own in your activity center.
  If you have permission in a space, you can also delete the application from the space.

  [Deleting an application](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/delete-app-cloud-hub.htm)
- Open app in IE plugin

  Information noteThe QlikView IE Plug-in for Qlik Cloud has been deprecated.

  Only available from Microsoft Edge in IE mode.

  The QlikView IE Plug-in installation file is downloaded from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads), see [Downloading installation files](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/Download_install_files.htm).

  The QlikView IE Plug-in is an application installed to your Microsoft Edge. If the plug-in has been installed, it opens the application in the plug-in, and displays the content of the QlikView application in as close a format as possible to the original qvw file.

  The URL of your tenant must be added as a trusted site in Microsoft Edge (Internet Options > Security). You can omit the https:// part of the URL and enable the Display mixed content setting found in the Custom Level... settings for Trusted Sites.

  For more information, see support article [QlikView on Qlik Cloud Services: open documents using the IE-plugin via Edge Chromium](https://community.qlik.com/t5/Knowledge-Base/QlikView-on-Qlik-Cloud-Services-open-documents-using-the-IE/ta-p/1806839).

You cannot reload QlikView applications in Qlik Cloud.
For applications that were uploaded manually to Qlik Cloud, you can upload the application again with the updated data.

### Supported functionality

Here is a list of supported actions when opening a QlikView application in Qlik Cloud.
Standard usage with all objects and all expressions is supported.

- Select, Select possible, Select excluded, Select all
- Section access
- Actions and triggers
- Back, forward
- Pivot
- Sorting
- Drill-down
- Search
- Lock
- Switching sheets
- Detach, Attach
- Minimize, Maximize
- Clear, Clear All, Clear other fields
- Set reference
- Alternate states
- Set analysis
- Document chaining
- Document Bookmarks
- Server Bookmarks (create, delete, share, mail as link)

  Permissions to use server bookmarks in QlikView applications in spaces are the same as for private Qlik Sense bookmarks.

  For information about permissions, see [Managing permissions in shared spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-shared-spaces.htm) and [Managing permissions in managed spaces](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/managing-managed-spaces.htm).
- Repository (read-only)

  Supported for bookmarks only.
- Accessibility and GeoAnalytics extensions
- Send to Excel (Sort order and documents with triggers are not supported).

  If your QlikView application contain sheet objects with fields with show conditions depending on variables, make sure Include in Bookmarks is selected before uploading the application to Qlik Cloud. If not, these objects will not be exported correctly. Include in Bookmarks is available in QlikView Desktop, Document Properties > Variables.
- Input fields
- Alerts

### Unsupported functionality

Here is the list of currently unsupported actions:

- Functions based on Shared file persistence in Windows are not supported. For example: Server objects, create new application, add sheet, new sheet objects. Server bookmarks can be migrated from your on-premise QlikView installation to QlikView applications in Qlik Cloud.
- You cannot reload QlikView applications in Qlik Cloud.
- You cannot download data (for example Export to Excel) from QlikView documents with Triggers.
- QlikView applications in a cloud environment are read-only. Script features are not available.
- AJAX client is supported, but the following are not: Open in Server, and Small device version (Mobile Clients - Small device and Mobile application).
- It is not possible to replace an existing application with a new upload. With each new upload a new copy of the application is added and the previous one is not removed even if the two applications have the same name.
- Notes
- Filter AccessPoint Document List Based on Section Access document property will not work in Qlik Cloud.
- Last document state
- Session collaboration
- Macros
- Print (HTML)
- Image export, subscriptions, Qlik Reporting Service, and On-Demand printing (Qlik NPrinting) are not supported.
- Copy cell value to clipboard only works in the AJAX client.
- Share Object
- Reload, both full or partial
- Repository (read-only)

  Supported for bookmarks only.
- Properties (read-only)
- Advanced Analytics (Server-side extensions)
- [Direct Discovery](/en-US/qlikview/September2026/Subsystems/Client/Content/QV_QlikView/DirectDiscovery/direct-discovery-introduction.htm)
- Dynamic update
- Export
- Accessibility and GeoAnalytics extensions are supported but no other Client-side Extensions (third-party extensions)
- Bundling (mostly used for pictures)
- Multiple languages are supported, but language management is different from QlikView AccessPoint, see [Changing language in Qlik Sense](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/languages.htm).
- Images where the path is a URL are not supported. As a workaround, you can load images into the document using a Bundle Info LOAD statement, referencing a CSV file containing your image URLs. To use an image by URL in your document, specify the image in a QMEM path.

  See:

  - [Bundle](/en-US/qlikview/September2026/Subsystems/Client/Content/QV_QlikView/Scripting/ScriptPrefixes/Bundle.htm)
  - [Internal files](/en-US/qlikview/September2026/Subsystems/Client/Content/QV_QlikView/Internal_Files.htm)
- Include Input Field Values is not available for bookmarks in QlikView applications.
