---
title: "Designing HTML report templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/design-html-reports.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates"]
---

# Designing HTML report templates

You can design HTML reports that can be embedded into emails and web pages. HTML reporting offers a code-based report development experience that is available directly within your analytics application. When configuring output from HTML templates, you can automatically embed the content into a pre-configured email, deliver the output as an HTML file, or both.

HTML report delivered as an embedded email message

![An HTML report embedded into an email message](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/reports_html-example.png "Click to view full size")

## Use cases

HTML reporting make it easy to deliver insights to stakeholders without the need for opening file attachments. With report content embedded directly within emails, key metrics and details are more easily found, simplifying consumption and accessibility of content.

Because they are in HTML format, these reports are also easy to embed into web pages and applications.

## Report generation

You can configure your HTML reports to be embedded directly within email messages. This action is completed in the Distribute tab when configuring a task.

Additional options are also available for generating reports from your HTML template. These options can be used in combination with, as alternatives to, embedded email body reports:

- Select to send the report as an attachment, or deliver to SharePoint. This is the standard way in which report templates in other formats are sent through the task configuration process.
- On-demand reporting is also available for application consumers. When an HTML report is generated on-demand, it is downloaded from the browser as an HTML file.

For full details, see [*Embedding report content in an email message*](../../Generate/html-report-as-email.htm).

## Considerations

During HTML template development, it is common to preview the template often to ensure that template code results in intended output. Due to variations in how email clients and devices render HTML content, there can be differences between previewed reports and what recipients actually see when HTML templates are embedded into email messages. Consider a trial-and-error approach involving tests from one or more email clients and devices to ensure optimum quality in your HTML reports.

Third-party tools are also available to simulate how the same HTML code will be rendered in different clients. These tools can help you to:

- Decide between having a single, optimized template or to create different templates for various consumption scenarios.
- Optimize the HTML code for a specific client.
- Control the rendering of the HTML code across different clients.

## Limitations

- You cannot set an HTML report template to generate as an embedded email message if a cycle has been applied to the report task.
- Recipient tags are only supported when the HTML template is used as an embedded email body. These tags are not replaced in any other scenarios, including:

  - Report preview
  - Reports generated as email attachments
  - Reports generated for folder distribution (Microsoft SharePoint)
  - Direct use of the Qlik Reporting Service API
  - Reports generated from Qlik Automate
