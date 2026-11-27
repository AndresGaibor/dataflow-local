---
title: "In-application reporting in managed spaces"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/InAppGeneral/cloud-in-app-reports-managed-space.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation"]
---

# In-application reporting in managed spaces

You can configure in-application reports for applications requiring strict data governance. With the same principles that you use for developing application data models for use in managed spaces, you can prepare your application for in-application reporting capabilities. This is achieved using space-aware syntax in the load script.

When developing an application in preparation to be published to a managed space, consider the following:

- The [templates](#glossary-0 "Glossary term") can be developed before or after publishing the application. If you create the template before publishing, change the connected application after publishing.
- A [distribution list](#glossary-1 "Glossary term") must be added to the application before publishing the application. During development, this can consist of mock data sources, rather than the actual data sources. The sources in the distribution list are referenced in the load script, so the script must be written in preparation for publishing, using space-aware syntax. This syntax is automatically used by default if you upload a distribution list as a source file.
- After publishing, the reporting assets – template, [filters](#glossary-2 "Glossary term"), and [report tasks](#glossary-3 "Glossary term") – can be recreated as desired, based on the reporting use case for the published application. The real data sources used in the distribution list should be added to the managed space.

## Existing report configurations

If you created a reporting configuration and distribution list before March 26, 2024, you need to be aware of changes to the file upload process for distribution lists.

For applications created before March 26, 2024, a distribution list source file uploaded in the Reporting section was automatically renamed and added to the space. The reference to this renamed file was then automatically added to the load script. The uploaded source file is now no longer renamed when added to the space.

To continue using existing report configurations when publishing these applications, follow the corresponding section below, depending on your distribution list sources. Alternatively, re-create your reporting configuration from scratch, using the guides shown later on this page.

### If you uploaded a source file

Open Data load editor and look at the file name references in the Distribution List script section. Adjust the syntax so that they use a space-aware reference pointing to the current space, rather than any specific space. For example, a file reference might look like:

```
FROM "lib://DataFiles/reporting_source_your_app_ID.xlsx"
```

Change this to:

```
FROM "lib://:DataFiles/reporting_source_your_app_ID.xlsx"
```

You can see that the application ID of the source application is contained in the file name. If you want this exact script to run when you publish the application, add your actual distribution list file to the managed space, with this exact name.

Alternatively, you can rename the source file in the development space, update the load script, and then publish. Finally, add the actual distribution list file, with the updated name.

### If you used remote data sources manually in the script

If you instead manually configured the load script to rely on other data sources for the distribution list, you simply need to adjust the load script to contain relative, space-aware references to the data sources (if this is not already done).

For more information and specific examples, see [*Data sources for applications in managed spaces*](../../Spaces/app-data-managed-spaces.htm).

## Workflow

Follow the sequence below to work with in-application reporting in a managed space.

### Application development

Develop the application in your development space (personal or shared space), as you normally would, in preparation for publishing it to the managed space.

### Develop the templates and filters

If desired, you can build the report templates and filters before publishing the application. This can be helpful as a stage in application development, but templates and filters added to the source application are not retained in the published copy.

If you create the templates before publishing and want to use them for the published application, change the connected Qlik Sense application for the templates. For Excel, PowerPoint, and Word templates, you can perform this action in the add-in. Alternatively, perform this action in the Qlik Sense application as you upload the templates into the published application. See [*Change the connected Qlik Sense application*](#Change).

### Prepare the distribution list reference

When you add a distribution list to an application, the application's load script is changed. The load script of an application is not accessible in a published application. Therefore, you need to add a distribution list to the application before publishing it.

At this stage, the distribution list simply needs to be a placeholder for the actual file or other sources that you will use for the distribution list in the managed space.

The procedure is slightly different, depending on whether your distribution list is a source file or a remote data source added manually in the script. However, the underlying concepts are the same. For a full guide outlining how to use space-aware syntax in the load script, see [*Data sources for applications in managed spaces*](../../Spaces/app-data-managed-spaces.htm).

#### Option 1: Direct upload of source file

Follow the regular procedure for uploading a source file as the distribution list: [*Adding the distribution list by uploading a source file*](../Generate/cloud-in-app-reports-distribution.htm#Adding).

Instead of adding the finalized recipient details, you can insert any desired placeholders. The important thing here is that you upload a file, and that this file is then automatically added to the development space and referenced in the script.

You can check that the Distribution List section in the load script contains a space-aware reference to the file, and does not directly reference any particular space. This is done automatically when you upload a source file as a distribution list in the Reporting section of the application. It should look something like this:

```
FROM "lib://:DataFiles/My_App_Distribution_List.xlsx"
```

This example is a space-aware reference that points to the current space in which the application is located. The extra colon before DataFiles provides the required relative reference.

Later, when you publish the application to the managed space, upload the actual distribution list file to the managed space. The actual distribution list must have the same file name as the file referenced in the script.

#### Option 2: Manual reference to data sources in the script

Follow the regular procedure for connecting to remote distribution list sources manually in your script: [*Defining the distribution list manually in the load script*](../Generate/cloud-in-app-reports-distribution.htm#Defining).

When writing the script to connect to the required data sources for your distribution list, you can use mock references to the files and connections as needed. In your script, the data sources simply need to have the same names as they will have in the managed space, and the references to these sources need to use relative, space-aware syntax.

### Publish the application

After you have prepared the load script and distribution list, the application is ready to be published to the managed space. For more information about publishing an application, see [*Publishing applications*](../../Apps/publish-app-cloud-hub.htm).

### Create object-level filters

If your template uses filters on individual report objects (see [*Using object-level filters in report templates*](../Generate/cloud-in-app-reports-filters.htm#ObjectLevel)), you must create the corresponding report filters in the published application before you upload any template that uses these filters. The report filters you create need to have names that match those in the source application.

### Change the connected Qlik Sense application

If you have created a report template before publishing the application, you need to update the template to reference the correct application ID. A published copy of an application will have a different application ID than the source application.

This process can be completed automatically in Qlik Sense as you upload a template. For Microsoft Office-based template formats—Excel, PowerPoint, or Word—this can also be done in the corresponding add-in. Before starting, you can create a separate copy of the template to distinguish it from the template for the source application.

For full instructions, see:

- From Qlik Sense: [*Changing the connected Qlik Sense application*](../Generate/cloud-in-app-reports-templates.htm#ChangeApp)
- From Qlik add-ins for Microsoft Office: [*Changing the connected Qlik Sense app*](../Design/OfficeCommon/add-in-get-started.htm#Changing)

Tip noteA best practice is to develop the template on a source application located in a shared space. When you need to publish the application to a managed space, download the template directly from the source application and upload it into the published application. As the application and its reporting needs change over time, you can follow this workflow when uploading new versions of the template.

It is always possible to develop and update your templates in the managed space directly.

### Add the actual distribution list sources

In the managed space, create the required files and connections needed to load your distribution list, as referenced in the load script. This step can be completed at any time.

The data sources providing the distribution list must contain the same parameter names (names of connections, files, and fields) as the distribution list sources used in the source application's load script.

When the connected sources are added to the space, you should be able to reload the application.

### Create the new reporting assets

You can now add reporting assets to the application. This could consist of the templates, [filters](#glossary-4 "Glossary term"), and [report tasks](#glossary-5 "Glossary term").

## Permissions

To work with in-application reporting for applications in managed spaces, you need:

- Permissions assigned to you by a tenant administrator. For more information, an administrator can refer to [*Setting permissions for metered reporting features*](../../Admin/mc-permissions-reporting.htm).
- One of the following space roles in the managed space:

  - Owner
  - Can manage
  - Can operate

  Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

For more information about space permissions for reporting, see [*Qlik Reporting Service permissions*](../reporting-permissions.htm).

## Limitations

In-application reporting is not available for applications published or distributed from Client-Managed Qlik Sense (including multi-cloud deployments) to Qlik Cloud. To use in-application reporting with these applications, migrate the application using the [Qlik Analytics Migration Tool](/en-US/migration/Subsystems/AnalyticsMigrationTool/Content/Qlik-Analytics-Migration-Tool-Overview.htm), or manually export the application and re-upload it into Qlik Cloud.

For more information, see [*In-application reporting with exported or migrated applications*](../Generate/cloud-in-app-reports-exported-migrated.htm).
