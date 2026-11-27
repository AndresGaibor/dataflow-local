---
title: "Embedding report content in an email message"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Generate/html-report-as-email.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Configuring report generation", "Working with report tasks"]
---

# Embedding report content in an email message

The content of HTML [report templates](#glossary-0 "Glossary term") can be embedded directly into an email message. To configure embedded email output for your HTML template, create a report task and select the HTML report option in the Distribute > Email settings.

By embedding HTML reports directly into your email, you can simplify the process of delivering and summarizing key performance metrics for report stakeholders.

## High-level workflow

Do the following:

1. Create an HTML template containing your email message content.

   [*Designing HTML report templates*](../Design/HTML/design-html-reports.htm)
2. Add a distribution list to the application.

   [*Creating a distribution list for your report*](cloud-in-app-reports-distribution.htm)
3. Create a report task.

   [*Creating a report task*](cloud-in-app-reports-tasks.htm#Creating)
4. In the Template dialog tab, select the HTML template to use as the embedded email body, or click Upload new to upload it.
5. Add any additional templates to the task, and click Next.

   Tip note

   You can use a single HTML template to generate the email body and also generate it as an attached report. To do this, add the same HTML template twice — as two separate instances — to the report task. For more information, see [*Setting up multiple outputs for the same template*](cloud-in-app-reports-tasks.htm#MultiOutput).

   Across all template instances added to the task, consider:

   - All HTML template instances not used as the embedded email body will be added as attachments.
   - The HTML template instance used in the embedded email body will not be added as an attachment.
6. Configure Output settings for each template, and click Next.
7. In the Distribute dialog tab, configure the Recipients for the emails.
8. Still in the Distribute dialog tab, go to the Email section.
9. Under Format, select HTML report.
10. Click Select template and choose your HTML template.
11. Complete the configuration for the report task.

## Considerations

During HTML template development, it is common to preview the template often to ensure that template code results in intended output. Due to variations in how email clients and devices render HTML content, there can be differences between previewed reports and what recipients actually see when HTML templates are embedded into email messages. Consider a trial-and-error approach involving tests from one or more email clients and devices to ensure optimum quality in your HTML reports.

Third-party tools are also available to simulate how the same HTML code will be rendered in different clients. These tools can help you to:

- Decide between having a single, optimized template or to create different templates for various consumption scenarios.
- Optimize the HTML code for a specific client.
- Control the rendering of the HTML code across different clients.

## Limitations

- You cannot set an HTML report template to generate as an embedded email message if a cycle has been applied to the report task.

## Example

For an example, see [*Example - Creating an email report using an embedded HTML template*](../Design/HTML/html-report-example.htm).
