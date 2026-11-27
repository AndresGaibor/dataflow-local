---
title: "Qlik Reporting Service specifications and limitations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Reporting-service-specifications-limitations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics"]
---

# Qlik Reporting Service specifications and limitations

Expand/Collapse all

# Qlik Reporting Service specifications and limitations

This help topic lists the capacities and limitations that apply to reporting in Qlik Cloud Analytics, both in the user interface and via the Qlik Reporting Service API. It specifically notes limitations that apply to using the value-add subscription options available with the Qlik Reporting Service.

The Qlik Reporting Service is a value-add set of services within a Qlik Cloud subscription that provides enterprise-level reporting capabilities from Qlik Cloud. With the Qlik Reporting Service, the following capabilities are available:

- In-application reporting
- Reporting with Qlik Automate
- Direct usage of the Qlik Reporting Service API. See: [Reports](https://qlik.dev/apis/rest/reports)

For more information about reporting in Qlik Cloud Analytics, see [*Reporting from Qlik Cloud Analytics*](SaaS-reporting-intro.htm).

This page lists limitations for the value-add capabilities noted above. The following information is provided:

- Qlik Reporting Service consumption limitations
- Limitations and specifications for each of the value-add capabilities within the Qlik Reporting Service

The information on this page does not necessarily apply to other reporting capabilities in Qlik Cloud (for example, subscription reports). For limitations specific to those capabilities, refer to their associated help topics.

## Consumption limitations for Qlik Reporting Service value-add capabilities

The following consumption-related limitations apply to all Qlik Cloud licenses, unless otherwise stated. The capacities listed on this page are a metered combination representing the combined usage across each of the included Qlik Reporting Service capabilities in the subscription.

For the consumption limits and capacities specific to your Qlik Cloud subscription, check with your [service account owner](#glossary-0 "Glossary term") and refer to the terms of service for the Qlik Cloud subscription you are using.

The maximum number of reports per month varies depending on your Qlik Cloud license, with add-on packs available for purchase. If you need additional reports, contact your [tenant admin](#glossary-1 "Glossary term").

For detailed information about your license metrics, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description. Administrators can view license information and monitor the number of generated reports and automation runs in the Administration activity center. For more information, see [*Monitoring resource consumption*](../Admin/mc-monitor-consumption.htm).

More detailed information about your personal automations is available through Automations in the Analytics [activity center](#glossary-2 "Glossary term"). Tenant admins can view consumption metrics on the Home tab of the Administration activity center.

## System and software requirements — Qlik add-ins for Microsoft Office

See [*System and software requirements*](Install/reporting-install-add-ins.htm#SystemReqsAddIns).

## Limitations for in-application reporting

These limitations apply to the in-application reporting capability in Qlik Cloud. For information about this capability, see [*In-application reporting with Qlik Cloud Analytics*](InAppGeneral/cloud-in-app-reports-intro.htm).

Platform and product availability

- In-application reporting is supported in Qlik Cloud Government and Qlik Cloud Government - DoD. Qlik add-ins for Microsoft Office are supported for developing report templates against applications in Qlik Cloud Government or Qlik Cloud Government - DoD tenants.
- In-application reporting is not available for applications published or distributed from Client-Managed Qlik Sense (including multi-cloud deployments) to Qlik Cloud. To use in-application reporting with these applications, migrate the application using the [Qlik Analytics Migration Tool](/en-US/migration/Subsystems/AnalyticsMigrationTool/Content/Qlik-Analytics-Migration-Tool-Overview.htm), or manually export the application and re-upload it into Qlik Cloud.
- Reporting capabilities, including the Qlik Reporting Service value-add features and subscription reports, are not supported in Direct Query applications.

Fonts and application styling

- When using a custom font in your application, it is assumed you have the required license to use that font in output from Qlik Sense. To ensure your fonts are licensed, make use of the multiple open-source fonts available in Qlik Sense for styling application content.

  If you have the required licenses for a font that is not available in the default Qlik Sense themes, see [Create themes with custom fonts](https://qlik.dev/extend/create-custom-themes/custom-themes-fontfamily-examples) to learn about adding the font to a custom theme.
- When using a custom, third-party, and/or proprietary font in your report, it is assumed you have the required license to use that font in output from the Qlik Reporting Service. For optimal print output, it is recommended to use an open-source font.
- When characters that are unsupported in the selected font are used in application content, these characters will be rendered in output with a font in which they are supported. Different behavior might be noticed if a custom font is used.
- Custom CSS styling applied to sheets is not included in reports.
- Shadows applied to chart objects in the application are not shown in the generated report.

Technical guardrails for application content

The following limitations apply to sharing visualizations, with respect to in-application reporting. If these limits are exceeded, your report will fail. If this issue occurs, contact a user with Can edit permission in the application.

The specific limitations are listed below:

- Maximum image size: 4,000 x 4,000 pixels
- Minimum image size: 5 x 5 pixels for charts and 20 x 20 pixels for sheets

Limitations specific to in-application task configuration

- A [report task](#glossary-3 "Glossary term") can generate a maximum of 500 unique reports. This limit is evaluated across all templates added to the task, rather than per template in the task. This limit also applies to all report tasks regardless of whether or not one or mores cycles are applied.
- You can select a maximum of three fields to cycle for a report task.
- The maximum execution time for a report task is four hours.
- In a Qlik Cloud tenant, a maximum of 1000 report tasks can be created by the same user. A user can free up report tasks by deleting existing tasks they created.
- You can add a maximum of 1000 recipients and 1000 groups to the [distribution list](#glossary-4 "Glossary term") of an application. The number of total recipients, whether in groups or not, cannot be higher than 1000.
- Report delivery via Microsoft SharePoint distribution folder is not available if the application uses section access.
- External email clients often enforce size limits for email attachments. Check with your email provider to find out what your limit is.

  Reports delivered to cloud [storage](#glossary-5 "Glossary term") connectors have no file size limit.
- [Report filters](#glossary-6 "Glossary term") are not compatible with Star statements. If an application contains this statement in the script, reports with filters might show unexpected results.
- When configuring a report filter using the Search selection method, certain search methods are not supported. For more information, see [*Report filter limitations*](Generate/cloud-in-app-reports-filters.htm#Report).
- Hidden and system fields are not visible in the list of fields to use in a report filter.
- If an application contains one or more fields configured with the Always one selected value property, you need to configure your report filters so that the filters select exactly one value for each of these fields. These report filters need to be applied to the report task.

  If a filter doesn't contain a value for these fields, or no filters are associated at all to the task, the report task will fail.
- You can add up to five report template instances to a report task, including copies of the same template. For example, if you add an Excel template twice to a task, with one .xlsx and one PDF output, this counts as two templates added to the task.

Limitations by report type—templates and in-application task configuration

These limitations are relevant for both template creation and configuration of report generation.

All template types

- Generally, when creating report templates, if an entity from the application is not available in a node in the template editor (for example, Charts, Levels, or Tables), this means that the entity, or something within the entity, is not supported in the selected node in the editor. For example, a pivot table from the application cannot be added in the Levels node but it can be added in the Images node.
- The following objects are not supported in report templates:

  - Filter panes
  - Maps
  - Charts with these hypercubes types: Tree, Pivot, or Stacked
- You can nest a maximum of five levels deep in your report template.
- The maximum number of generated images in a report is 1,000.
- A generated report can contain a maximum of 50,000 objects. Consider the following:

  - A single chart, variable value, level value, or expression value counts as one object.
  - For tables, 500 generated cells count as one object.
- The maximum number of object instances you can add to a report template is 200.
- Hidden and system fields are not visible in the list of fields to use for levels and pages.
- Using a calculated dimension as a level is not supported. Specifically, the following use cases are not supported:

  - Adding a calculated dimension as a master item, adding this master item to a chart, and then using the chart as a level.
  - Adding a calculated dimension expression to a chart, and then using the chart as a level.

  You can, however, include tabular data consisting of calculated dimension columns inside a level.
- When using master dimensions inside a level, you can only use master dimensions with the Single type. Drill-down master dimensions are not supported inside levels.
- Master dimensions with the Cyclic type will show always the first dimension when charts are inserted into templates and reports are scheduled with tasks.
- For report content based on a chart column that has a Show column if condition, the column will not visible in the add-in or designer window. You need to remove the condition from the column prior to adding it to the template, and then readd the condition as needed.
- Semantic load prefixes in load scripts are not supported. For information about semantic loads, see [*Semantic*](../Scripting/ScriptPrefixes/Semantic.htm).
- Third-party extensions are not supported.

Tabular reporting

This section lists limitations that apply when using the Qlik add-in for Microsoft Excel, as well as to reports generated from Excel report templates.

- The use of custom fonts in the Excel template file is not supported. If your template contains fonts that are unavailable for report generation, elements using these fonts will instead use a default Excel font in generated reports.
- Macros and scripting are not supported in Microsoft Excel report templates.
- Microsoft Excel imposes certain constraints on what is contained within an Excel workbook file. These limitations apply to both Excel report templates and the output they generate. This includes the maximum number of rows, columns, and characters in a single .xlsx file. Refer to the official Microsoft documentation to learn about these external limits.
- An Analysis object can only be added to an Excel report template as a chart image. To add an Analysis to the template as tabular data, convert it to a chart in the application.
- Sensitivity labels or Azure Information Protection (AIP) labels are not supported in Excel report template files. That is, if your template contains any of these labels, the data restriction they provide is ignored, report generation proceeds as usual, and generated reports will not contain any of sensitivity or AIP labels. If sensitivity or AIP labels are required for output, you can add them manually to the reports after they are generated.
- Tabular (Excel) report templates can have a maximum file size of 10 MB.
- Excel report templates cannot contain the following content:

  - Excel formula functions that call external services, such as *WEBSERVICE*, *FILTERXML*, *RTD*, *CALL*, *REGISTER*, *REGISTER.ID*, *IMAGE*, and *IMPORTTEXT*, or that invoke HTTP URLs.
  - External resources included through external links, such as data connections (for example, Power Query, ODBC, OLEDB, or web queries), external links in document properties, pivot tables sourcing data from external sources, or linked images. Embedded images are allowed.
  - OLE or ActiveX objects.

  Report templates containing any of these disallowed objects cannot be uploaded to Qlik Cloud. Previewing a template that contains a disallowed object fails, and any existing scheduled tasks based on such a template fail when they run. These restrictions apply to both Qlik Cloud’s user interface and public APIs.

PixelPerfect reporting

- An Analysis object cannot be added to a PixelPerfect report template. To add an Analysis to the template as an image, convert it to a chart in the application.

  For more information about Analysis objects, see [*Creating and editing analyses*](../Analyses/creating-analyses.htm).
- Custom fonts are not supported for PixelPerfect reporting in Qlik Cloud Analytics.
- PixelPerfect report templates can have a maximum file size of 10 MB.

HTML reporting

- You cannot set an HTML report template to generate as an embedded email message if a cycle has been applied to the report task.
- Recipient tags are only supported when the HTML template is used as an embedded email body. These tags are not replaced in any other scenarios, including:

  - Report preview
  - Reports generated as email attachments
  - Reports generated for folder distribution (Microsoft SharePoint)
  - Direct use of the Qlik Reporting Service API
  - Reports generated from Qlik Automate
- HTML report templates can have a maximum file size of 10 MB.

PowerPoint reporting

- Qlik’s integration testing of PowerPoint APIs show that the Qlik add-in for Microsoft PowerPoint can be unstable and/or slow at times. Qlik’s investigation with Microsoft have understood that this is a known state and that some APIs on web, when compared to desktop, can result in different behaviors. If report developers are having difficulty with the online Microsoft PowerPoint add-in, please contact [Qlik Support](https://community.qlik.com/t5/Support/ct-p/qlikSupport) to report the case—however, please pursue your report development with the desktop version of PowerPoint. This will allow the Qlik team to investigate the integration while the report developer can continue with report development.
- PowerPoint report templates can have a maximum file size of 30 MB.
- PowerPoint report templates cannot contain linked audio, linked video, linked pictures, or linked OLE objects. Report templates containing any of these disallowed objects cannot be uploaded to Qlik Cloud. Previewing a template that contains a disallowed object fails, and any existing scheduled tasks based on such a template fail when they run. These restrictions apply to both Qlik Cloud’s user interface and public APIs.

Word reporting

This section lists limitations that apply when using the Qlik add-in for Microsoft Word, as well as to reports generated from Word report templates.

- An Analysis object can only be added to a Word report template as a chart image. To add an Analysis to the template as tabular data, convert it to a chart in the application.
- Word templates have the following limitations for chart images that are added as [floating images](https://www.microsoft.com/en-us/microsoft-365/blog/2011/05/19/understanding-images-part-1-the-basics/):

  - Using desktop versions of Word, you cannot refresh these chart images.
  - Using web versions of Word, you cannot refresh these chart images. Also, you cannot have the properties open automatically when you select it, nor will the object be selected in the Word document when you open its properties via the add-in.
- Word report templates can have a maximum file size of 30 MB.
- Word report templates cannot contain the following content:

  - A template (.dotx or .dotm) attached and linked to the document.
  - Fields that include external content, such as *INCLUDETEXT*, *INCLUDE*, *INCLUDEPICTURE*, *RD* (RefDoc), *LINK*, *IMPORT*, or *DATABASE*, as well as DDE fields (*DDE*, *DDEAUTO*) and EMBED, HTML ActiveX, or OCX fields.
  - Linked images, OLE or ActiveX objects, or mail merge.

  Report templates containing any of these disallowed objects cannot be uploaded to Qlik Cloud. Previewing a template that contains a disallowed object fails, and any existing scheduled tasks based on such a template fail when they run. These restrictions apply to both Qlik Cloud’s user interface and public APIs.

## Limitations for reporting with Qlik Automate

Technical limitations

The following limitations apply to reporting with Qlik Automate. If these limits are exceeded, your report will fail. If this issue occurs, contact a user with Can edit permission in the application.

The specific limitations are listed below:

- Maximum number of fields in the selections: 125
- Maximum number of field values in the selections: 150,000 total field values across one or many fields
- Maximum number of alternate states: 125

  [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm)
- Maximum number of patches: 100

  Patches are properties or styling applied in the application. For example: Adding a sort to a table column.
- Maximum number of variables: 1,100

  [*Using variables in expressions*](../Variables/work-with-variables.htm)
- Maximum image size: 4,000 x 4,000 pixels
- Minimum image size: 5 x 5 pixels for charts and 20 x 20 pixels for sheets
- Maximum number of pages in a report: 200

Other specifications and limitations

- If you create PDF or PowerPoint reports, the resolution will be 300 DPI.
- External email clients often enforce size limits for email attachments. Check with your email provider to find out what your limit is.

  Reports delivered to cloud [storage](#glossary-7 "Glossary term") connectors have no file size limit.
- Portrait layout is not supported for sheets that will be outputted to automations in PowerPoint format. Sheets set to portrait layout will be converted to landscape. However, you can use portrait layout if you are using the Qlik Reporting Service API. For more information about using the API to create reports, see the [Developer Portal documentation](https://qlik.dev/apis/rest/reports).
- When using a custom font in your application, it is assumed you have the required license to use that font in output from Qlik Sense. To ensure your fonts are licensed, make use of the multiple open-source fonts available in Qlik Sense for styling application content.

  If you have the required licenses for a font that is not available in the default Qlik Sense themes, see [Create themes with custom fonts](https://qlik.dev/extend/create-custom-themes/custom-themes-fontfamily-examples) to learn about adding the font to a custom theme.
- When characters that are unsupported in the selected font are used in application content, these characters will be rendered in output with a font in which they are supported. Different behavior might be noticed if a custom font is used.
- If you use a custom theme in your application to define font use (for example, adding a font file directly to the theme), fonts rendered in various outputs might not be the same fonts you have used in your application.
- Shadows applied to chart objects in the application are not shown in the generated report.
- Third-party extensions are not supported.
- Reporting capabilities, including the Qlik Reporting Service value-add features and subscription reports, are not supported in Direct Query applications.
- Analyses cannot be individually added to reports in Qlik Automate using Add chart to report. Sheets with analyses can be added to reports with Add sheet to report or Add selection to report.
- Sheet titles are not included in exported reports generated with Qlik Automate. This is by design and applies to .xlsx, .pptx, HTML, and PixelPerfect output.
- Custom CSS styling applied to sheets is not included in reports.

More detailed information about your personal automations is available through Automations in the Analytics activity center. Tenant admins can view consumption metrics on the Home tab of the Administration activity center.
