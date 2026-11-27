---
title: "Managing installation manifests for Qlik add-ins for Microsoft Office"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-add-in.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations", "Administering reporting and subscriptions"]
---

# Managing installation manifests for Qlik add-ins for Microsoft Office

Qlik add-ins for Microsoft Office are installed in Microsoft environments using a manifest XML file. A [tenant admin](#glossary-0 "Glossary term") generates the link to the manifest file, and can download the file itself, from the Administration activity center. The manifest file can be used to install Qlik add-ins for Microsoft Excel, Microsoft PowerPoint, and Microsoft Word.

Information note
The manifest file, and the link to it, must be obtained in the Administration activity center after completing the OAuth client configuration.
For the full workflow, see [*Prepare and obtain the add-in manifest*](../Reporting/Install/reporting-install-add-ins.htm#Manifest).

## Obtaining the manifest link

A link to the manifest file is most likely required for the Microsoft 365 administrator to centrally deploy Qlik add-ins for Microsoft Office.

Do the following:

1. Create an OAuth client to use in your organization's deployment of the add-in. See: [*Create an OAuth client*](../Reporting/Install/reporting-install-add-ins.htm#Creating)
2. In the Administration activity center, go to the Settings page, then select the Email and reports tab.
3. Go to Qlik add-ins for Microsoft Office.
4. In the drop down menu, select the OAuth client configuration you have set up for activating OAuth in the add-in.

   Qlik Cloud Government note

   If you are using a Qlik Cloud Government or Qlik Cloud Government - DoD tenant, you can also select your Microsoft Office version. You can choose between:

   - Office 365 Commercial version
   - Office 365 Government Community Cloud (GCC) version
   - Office 365 Government Community Cloud High (GCCH) version

   For more information about installing add-ins for Qlik Cloud Government, see [Qlik Cloud Government — Creating analytics and visualizing data](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg.htm#Creating) and [Qlik Cloud Government - DoD — Creating analytics and visualizing data](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg-dod.htm#Creating).
5. Click Copy.

The link to the manifest is copied to your clipboard.

## Downloading the manifest file directly

If you are sideloading the add-in, or installing with a network share, you will need the manifest file for direct import. Access it through the manifest link (see above), or by using the download dialog.

Do the following:

1. Create an OAuth client to use in your organization's deployment of the add-in. See: [*Create an OAuth client*](../Reporting/Install/reporting-install-add-ins.htm#Creating)
2. In the Administration activity center, go to the Settings page, then select the Email and reports tab.
3. Go to Qlik add-ins for Microsoft Office.
4. In the drop down menu, select the OAuth client configuration you have set up for activating OAuth in the add-in.

   Qlik Cloud Government note

   If you are using a Qlik Cloud Government or Qlik Cloud Government - DoD tenant, you can also select your Microsoft Office version. You can choose between:

   - Office 365 Commercial version
   - Office 365 Government Community Cloud (GCC) version
   - Office 365 Government Community Cloud High (GCCH) version

   For more information about installing add-ins for Qlik Cloud Government, see [Qlik Cloud Government — Creating analytics and visualizing data](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg.htm#Creating) and [Qlik Cloud Government - DoD — Creating analytics and visualizing data](/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/HelpSites/about-qcg-dod.htm#Creating).
5. Click Download.

## Learn more

- [*Designing report templates with Qlik add-ins for Microsoft Office*](../Reporting/Design/OfficeCommon/reporting-add-ins.htm)
- [*Deploying and installing Qlik add-ins for Microsoft Office*](../Reporting/Install/reporting-install-add-ins.htm)
- [*Designing tabular report templates*](../Reporting/Design/Excel/design-tabular-report-templates.htm)
- [*Designing PowerPoint report templates*](../Reporting/Design/PowerPoint/powerpoint-report-template.htm)
- [*Designing Word report templates*](../Reporting/Design/Word/word-report-template.htm)
