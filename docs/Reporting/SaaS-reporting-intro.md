---
title: "Reporting from Qlik Cloud Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/SaaS-reporting-intro.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Reporting from Qlik Cloud Analytics

Qlik Cloud Analytics offers several reporting capabilities that allow business intelligence teams to reach stakeholders who need to consume file-based analytics.

## Reporting with subscriptions

Business users can create subscriptions of a single chart or up to 10 sheets, delivered as an email message with a PDF or PowerPoint attachment on a predefined schedule. These reports can be sent to other Qlik Cloud Analytics users in your system. This reporting option supports [section access](#glossary-0 "Glossary term").

For more information, see [*Scheduling reports with subscriptions*](Subscriptions/Subscription-reports.htm).

## Centralized report development and delivery

The Qlik Cloud platform and the value-add Qlik Reporting Service support common advanced report composition and burst distribution requirements typically managed by centralized report developers.

In-application reporting allows you to design, configure, and generate reports in a number of formats, allowing extensive customization options for content, distribution, and self-service reporting. Reports are generated from templates created in Microsoft Excel, Microsoft PowerPoint, or Microsoft Word, or with one of two designers (PixelPerfect or HTML) embedded directly into your application. Reports can be generated from both task-based configurations and on-demand by application consumers. For more information, see [*In-application reporting with Qlik Cloud Analytics*](InAppGeneral/cloud-in-app-reports-intro.htm).

Where existing dashboards are required for visual report composition, report developers can consider reporting using Qlik Automate. For more information, see [*Reporting from Qlik Cloud Analytics with Qlik Automate*](Automations/Reports-with-application-automations.htm).

System integrators can use the Qlik Reporting Service API for systematic integration and customer-specific report distribution. For more information about the API, see [Reports](https://qlik.dev/apis/rest/reports).

Check with your [service account owner](#glossary-1 "Glossary term") about your Qlik Cloud subscription's included capacities.

## In-application reporting

In-application reporting provides a flexible, dynamic experience for enterprise report design and distribution. You can design your reports in Excel, PowerPoint, or Word using Qlik add-ins, or directly within your application using one of the two available designers (PixelPerfect or HTML). When you have finished designing your templates, configure report generation directly within your application, using one or both of the following workflows:

- Task-based generation: Allow large-scale report generation with scheduled or manual distribution. You can send reports to users within and outside the Qlik Cloud tenant. Reports can be delivered by email, and to folders with Microsoft SharePoint connections. Reports can be filtered at the task level, or on a per-user basis, to leverage burst report delivery. You also have the option to embed your reports directly into email messages with HTML templates.
- On-demand reporting: Allow application consumers to generate reports as they analyze sheets in your application. Reports can be downloaded directly to users' computers.

For more information, see [*In-application reporting with Qlik Cloud Analytics*](InAppGeneral/cloud-in-app-reports-intro.htm).

### Tabular reporting

For tabular-style reporting requirements where large datasets need to be generated and processed, report developers should consider using Qlik Cloud's tabular reporting offering.

With tabular reporting, you develop Excel report templates using the Qlik add-in for Microsoft Excel. Upload the templates into your application and configure report generation using the task-based and on-demand reporting features. Generated reports can be in .xlsx or PDF format.

For more information about designing tabular report templates, see [*Designing tabular report templates*](Design/Excel/design-tabular-report-templates.htm).

### PixelPerfect reporting

PixelPerfect offers a highly versatile report development experience, with a multitude of options to support precision and extensive customization.

To create PixelPerfect templates, use the PixelPerfect designer that is embedded directly into your Qlik Sense application. After you have finished creating your template, configure report generation using the task-based and on-demand reporting features. Generated reports are in PDF format.

For more information about creating PixelPerfect templates, see [*Designing PixelPerfect report templates*](Design/PixelPerfect/design-pixelperfect-templates.htm).

### HTML reporting

HTML reports can be embedded directly within email messages, making it easier to share key insights with report consumers. HTML report templates can also generate output in file-based HTML format, allowing easy integration of reports within web pages.

To create HTML templates, use the HTML designer that is embedded directly into your analytics application. After you have finished creating your template, configure report generation using the task-based and on-demand reporting features. Reports can be embedded directly into email messages, generated as downloadable HTML files, or both.

For more information about creating HTML templates, see [*Designing HTML report templates*](Design/HTML/design-html-reports.htm).

### PowerPoint reporting

With PowerPoint reporting, you can present analytics in slideshow format, benefiting from the power of native Microsoft PowerPoint content formatting.

Develop PowerPoint report templates using the Qlik add-in for Microsoft PowerPoint. Upload the templates into your application and configure report generation using the task-based and on-demand reporting features. Generated reports can be in .pptx or PDF format.

For more information about designing PowerPoint report templates, see [*Designing PowerPoint report templates*](Design/PowerPoint/powerpoint-report-template.htm).

### Word reporting

Word reporting allows you to create reports for document-style consumption.

Develop Word report templates using the Qlik add-in for Microsoft Word. Upload the templates into your application and configure report generation using the task-based and on-demand reporting features. Generated reports can be in .docx or PDF format.

For more information about designing Word report templates, see [*Designing Word report templates*](Design/Word/word-report-template.htm).

## Reporting using Qlik Automate

Application and report developers can use the combination of the Qlik Reporting Service and Qlik Automate to deliver customized automated reports.

Reports of Qlik Sense sheets are delivered as PDF or PowerPoint files, and can be sent to other Qlik Cloud users in your system or recipients outside of your system.

You can create a multi-page report using an automation template or create your own fully custom report definition.

For more information, see [*Reporting from Qlik Cloud Analytics with Qlik Automate*](Automations/Reports-with-application-automations.htm).
