---
title: "Adding recipient placeholder tags"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-recipient-tags.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates", "Adding content to your HTML report template"]
---

# Adding recipient placeholder tags

You can add recipient tags to HTML templates that will be delivered as embedded email messages. The tags consist of placeholder text that is replaced by details specific to the generated email, including the recipient name and email, the groups that the recipient belongs to, and the [filter](#glossary-0 "Glossary term") applied to their report.

Adding recipient tags to your template allows you to personalize and enrich report elements such as salutation, header content, and section titles.

## Adding a recipient tag

Do the following:

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the recipient tag.
2. In the designer toolbar, click ![Tag](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tag_2.svg).
3. Select one the following tag types:

   - Name: Will be replaced by the name of the recipient as it has been entered in the [distribution list](#glossary-1 "Glossary term").
   - Email: Will be replaced by the email address of the recipient.
   - Groups: Will be replaced by a comma-separated list of all groups to which the recipient has been linked in the distribution list.
   - Filters: Will be replaced by the name of the recipient-level report filter that applies to the specific report being generated.

   The recipient tag is added.

When you create a report task that delivers the template output in an embedded email, you can see the results.

## Example

This is a basic example of HTML template code that makes use of the recipient tag types.

```
<html><head>
<title>Report - Sales Monthly</title>
  </head>
  <body>
    <div><p>Key details about this report:</p>
    <ul><li>Recipient: [recipient_name]</li>
    <li>Email: [recipient_email]</li>
    <li>Applicable Distributions: [recipient_groups]</li>
    <li>Department: [recipient_filters]</li>

<p>Dear [recipient_name],</p>
<p>This email contains the [recipient_filters] department's monthly performance. See below for details.</p>
<p>Regards,</p>
<p>- Management</p>

</body></html>
```

## Limitations

- Recipient tags are only supported when the HTML template is used as an embedded email body. These tags are not replaced in any other scenarios, including:

  - Report preview
  - Reports generated as email attachments
  - Reports generated for folder distribution (Microsoft SharePoint)
  - Direct use of the Qlik Reporting Service API
  - Reports generated from Qlik Automate

## Learn more

- [*Creating a distribution list for your report*](../../Generate/cloud-in-app-reports-distribution.htm)
