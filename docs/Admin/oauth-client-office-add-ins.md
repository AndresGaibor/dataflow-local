---
title: "Creating OAuth clients for Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-client-office-add-ins.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Creating OAuth clients for Qlik add-ins for Microsoft Office

A tenant admin must create an OAuth client before report developers can install the Qlik add-ins for Microsoft Office.

An OAuth client configuration is required to install Qlik add-ins for Microsoft Office. Add-ins are used by report developers to prepare [report templates](#glossary-0 "Glossary term") for in-application reporting with Qlik Cloud.

For OAuth to work in the add-ins, the OAuth client needs to be configured with the exact configuration shown below.

Do the following:

1. In Qlik Cloud, click ![Open Navigation menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_menu.svg) in the top left corner.
2. Select Administration.
3. Go to OAuth.
4. Click Create new.
5. In the Client type dropdown menu, select Single-page app. More fields will appear.
6. Insert a Name. The Description is optional.
7. At minimum, select the checkbox to include the user\_default scope. You can include other scopes in the configuration, but without user\_default, installation will not work.

   See [*Available OAuth scopes*](oauth-scopes.htm#Availabl) for a full description of each available scope.
8. In the Add redirect URLs field, insert the URL of the Qlik Cloud tenant, followed by this fixed string: /office-add-ins/oAuthLoginSuccess.html

   The result should look like this: https://<tenant or alias hostname>.<region>.qlikcloud.com/office-add-ins/oAuthLoginSuccess.html. For example: http://example-company-123.us.qlikcloud.com/office-add-ins/oAuthLoginSuccess.html
9. Click Add.
10. In the Add allowed origins field, insert your tenant URL and click Add.
11. Click Create.
12. The Copy your Client ID window appears. You can choose to copy the Client ID to clipboard, or click Done to close the window.

After creating the OAuth client, get the updated manifest XML link from the Administration activity center. Go to the Settings page and select the Email and reports tab. In the Qlik add-ins for Microsoft Office section, retrieve the link you can use to deploy and install the add-in.

For more information about generating the manifest file, as well as deploying and installing an add-in, see:

- [*Deploying and installing Qlik add-ins for Microsoft Office*](../Reporting/Install/reporting-install-add-ins.htm)
- [*Managing installation manifests for Qlik add-ins for Microsoft Office*](mc-administer-add-in.htm)
