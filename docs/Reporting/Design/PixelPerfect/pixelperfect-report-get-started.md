---
title: "Getting started with PixelPerfect report templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-report-get-started.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates"]
---

# Getting started with PixelPerfect report templates

PixelPerfect [report templates](#glossary-0 "Glossary term") are developed with the PixelPerfect designer. This designer is available directly within a Qlik Sense application.

## Concepts

Before you start working with PixelPerfect reports, it is helpful to understand the underlying concepts behind template creation. The following concepts are essential for understanding how report content is generated from a template:

- Banded authoring
- Data binding

### Banded report authoring

The PixelPerfect designer is a banded report authoring tool. The structure of the report template contains a series of bands that contain report objects. Typically, report objects are added on the bands, with or without data bindings. These data bindings connect to data sources from your Qlik Sense application.

For more information about banded report creation, see [*Banded report authoring*](pixelperfect-banded-authoring.htm).

### Data binding

To populate your reports with application data, you need to add specific data sources from your Qlik Sense application to the designer, and then link them to bands and objects in your template. A data source that has been made available in the PixelPerfect designer is known as a data binding.

Data binding is performed with the following general workflow:

1. Add the data binding using the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, available in the right side panel.
2. Add objects, bands, and other elements to the template, and then connect them to the data source in the element's properties.

For more information about data binding, see [*Data binding*](pixelperfect-data-binding.htm).

## Interface overview

For an overview of the PixelPerfect designer, see [*Navigating the PixelPerfect designer*](pixelperfect-designer.htm).

## Creating a template

Do the following:

1. In your application, use the drop down menu in the navigation bar and select Reporting.
2. Switch to the Templates tab.
3. In the top right, click Create new > PixelPerfect template.
4. Enter a Name for the template.

The PixelPerfect designer opens.

## Editing a template

You can edit existing PixelPerfect templates that have already been added in the application. When you edit a template, the PixelPerfect designer opens directly in the application, where you can make changes to the existing template.

Do the following:

1. In the Reporting section of an application, switch to the Templates tab.
2. Click ![Three-dot icon](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a PixelPerfect template, and click ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit.

The PixelPerfect designer opens.

## Saving your work

Autosave is turned on by default in the PixelPerfect designer. Changes are automatically saved every 30 seconds. You can also manually save your work more frequently if needed—for example, if you are done editing and would like to close your browser. To manually save, click Save template in the top right corner.

Autosave can also be turned off if needed. To turn off this feature, switch Autosave off in the top right corner.

## Previewing your work

As you add content to your report template, it is helpful to preview the output in its current form. You can easily export a copy of the generated report when working in the PixelPerfect designer.

Do the following:

1. When editing a template, click Preview template in the top right corner of the interface.
2. Click Preview as PDF, and save the file to your computer.

You can continue working on your template while the preview is being generated.

## Exporting a PixelPerfect template

You can export a copy of the template to your local machine. The template is exported in .qpxp format.

Do the following:

1. In the Reporting section of an application, switch to the Templates tab.
2. Click ![Three-dot menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a template.
3. Click ![Download](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) Download.

After exporting the template, you can upload it into the same application—or a copy of the application—to create new variations or add the template to a published application. See [*Getting started with PixelPerfect report templates*](#).

## Uploading an existing PixelPerfect template

You can upload an existing PixelPerfect template file (in .qpxp format) into the application. This action is common when you have developed a template against a copy of the application in a development space, and need to re-upload the template after the application has been published to a managed space.

To upload the template into an application, any Qlik Sense objects referenced in the template must also exist in the application.

Do the following:

1. Before starting, export the PixelPerfect template you want to use. See [*Exporting a PixelPerfect template*](#Exporting).
2. In the Reporting section of an application, switch to the Templates tab.
3. In the top right, click Upload PixelPerfect template.
4. Click Browse, and select a compatible .qpxp file from your computer.

## Other actions

For a PixelPerfect template listed in the Templates tab, click the ![Three-dot menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) icon to access the following additional options:

- ![Edit](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg)
  Rename: Change the name of a template within the application.
- ![Upload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_upload.svg) Upload new version: Update the template with a new version, in .qpxpformat. There are requirements for the application objects in the template. The action is blocked if the new template version is not compatible with the current application.
- ![Trash can](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin2.svg)
  Delete: Delete the template.
- ![Report](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_report_outline.svg)
  On-demand: Change the on-demand reporting settings for the template. See: [*Configuring on-demand reporting*](../../OnDemand/reports-on-demand-configure.htm)

For more information about template management in the application, see [*Managing report templates*](../../Generate/cloud-in-app-reports-templates.htm).

## Permissions

Working with PixelPerfect templates includes:

- Viewing templates
- Creating, editing, and deleting templates

  Information noteDeleted templates cannot be recovered.
- Uploading and downloading templates
- Configuring on-demand reporting for the templates

To work with PixelPerfect templates, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../../Admin/mc-permissions-reporting.htm).
- [*Space permissions*](#Space)

  For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../../reporting-permissions.htm).

### Space permissions

You require specific space roles. The requirements depend on the type of space in which your application is located.

To perform the above actions with PixelPerfect templates in an application located in a [shared space](#glossary-2 "Glossary term"), you need one of the following space roles in the space:

- Owner (of space)
- Can manage
- Can edit data in applications
- Can edit

To perform the above actions with PixelPerfect templates in an application located in a [managed space](#glossary-3 "Glossary term"), you need one of the following space roles in the space:

- Owner (of space)
- Can manage
- Can operate

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

If you are working with an application in your [personal space](#glossary-4 "Glossary term"), you need the Private Analytics Content Creator security role in the tenant to perform these actions.
