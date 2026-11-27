---
title: "Getting started with HTML reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-get-started.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates"]
---

# Getting started with HTML reports

HTML [report templates](#glossary-0 "Glossary term") are developed with the HTML designer. This designer is available directly within an analytics application.

## Interface overview

For an overview of the HTML designer, see [*Navigating the HTML designer*](html-report-designer.htm).

## Creating a new HTML template

Do the following:

1. In your application, use the drop down menu in the navigation bar and select Reporting.
2. Switch to the Templates tab.
3. In the top right, click Create new > HTML template.
4. Enter a Name for the template.

The HTML designer opens.

## Editing a template

You can edit existing HTML templates that have already been added in the application. When you edit a template, the HTML designer opens directly in the application, where you can make changes to the existing template.

Do the following:

1. In the Reporting section of an application, switch to the Templates tab.
2. Click ![Three-dot icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to an HTML template, and click ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit.

The HTML designer opens.

## Saving your work

Autosave is turned on by default in the HTML designer. Changes are automatically saved every 30 seconds. You can also manually save your work more frequently if needed—for example, if you are done editing and would like to close your browser. To manually save, click Save template in the top right corner.

Autosave can also be turned off if needed. To turn off this feature, switch Autosave off in the top right corner.

Your template cannot be saved (including with autosave) if you add HTML content that is not allowed in the template. When prohibited content is present in the template, you must first sanitize the contents, either automatically or by manually removing non-compliant code, before saving. For more information about sanitization and a list of allowed HTML code, see [*Allowlist for code in HTML templates*](html-report-allowed-code.htm).

## Previewing your work

As you add content to your report template, it is helpful to preview the output in its current form. You can easily export a copy of the generated report when working in the HTML designer.

Do the following:

- When editing a template, click Preview template in the top right corner of the interface.

You can continue working on your template while the preview is being generated.

## Exporting an HTML template

You can export a copy of the template to your local machine. The template is exported in .qhtml format.

Do the following:

1. In the Reporting section of an application, switch to the Templates tab.
2. Click ![Three-dot menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a template.
3. Click ![Download](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) Download.

After exporting the template, you can upload it into the same application—or a copy of the application—to create new variations or add the template to a published application. See [*Uploading an existing HTML template*](#Uploading).

## Uploading an existing HTML template

You can upload an existing HTML template file (in .qhtml format) into the application. This action is common when you have developed a template against a copy of the application in a development space, and need to re-upload the template after the application has been published to a managed space.

To upload the template into an application, any Qlik Sense objects referenced in the template must also exist in the application.

Do the following:

1. Before starting, export the HTML template you want to use. See [*Exporting an HTML template*](#Exporting).
2. In the Reporting section of an application, switch to the Templates tab.
3. In the top right, click Upload template.
4. Click Browse, and select a compatible .qhtml file from your computer.

## Other actions

For an HTML template listed in the Templates tab, click ![Three-dot menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to access the following additional options:

- ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg)
  Rename: Change the name of a template within the application.
- ![Upload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_upload.svg) Upload new version: Update the template with a new version, in .qhtml format. There are requirements for the application objects in the template. The action is blocked if the new template version is not compatible with the current application.
- ![Trash can](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin2.svg)
  Delete: Delete the template.

  Information noteDeleted templates cannot be recovered.
- ![Report](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_report_outline.svg)
  On-demand: Change the on-demand reporting settings for the template. See: [*Configuring on-demand reporting*](../../OnDemand/reports-on-demand-configure.htm)

For more information about template management in the application, see [*Managing report templates*](../../Generate/cloud-in-app-reports-templates.htm).

## Permissions

Working with HTML templates includes:

- Viewing templates
- Creating, editing, and deleting templates
- Uploading and downloading templates
- Configuring on-demand reporting for the templates

To work with HTML templates, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../../Admin/mc-permissions-reporting.htm).
- [*Space permissions*](#Space)

  For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../../reporting-permissions.htm).

### Space permissions

To perform the above actions with HTML templates in an application located in a [shared space](#glossary-2 "Glossary term"), you need one of the following space roles in the space:

- Owner (of space)
- Can manage
- Can edit data in applications
- Can edit

To perform the above actions with HTML templates in an application located in a [managed space](#glossary-3 "Glossary term"), you need one of the following space roles in the space:

- Owner (of space)
- Can manage
- Can operate

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

If you are working with an application in your [personal space](#glossary-4 "Glossary term"), you need the Private Analytics Content Creator security role in the tenant to perform these actions.
