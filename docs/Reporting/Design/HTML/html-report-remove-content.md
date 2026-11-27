---
title: "Removing content from an HTML report template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-remove-content.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates"]
---

# Removing content from an HTML report template

You can remove an object from the HTML report template, and from the list of available objects shown in the objects panel.

Do the following:

1. Select the HTML code where the object is added.

   The objects panel opens, with the configuration for the object.
2. Click Delete at the bottom of the object panel.

This removes all code in the template that uses the object, and also deletes the object from the applicable menu in the object panel.

If you instead manually remove code that uses an object, the instance of the object is not shown in the generated report. However, the object will still appear in the list of added objects. This means you can easily re-add the object to the template later.

## Removing table columns

For chart data added by column as a table, you can delete columns from the template. To do this, remove the reference to the object from any td elements (if added as multi-column table) or remove the column item (if added as single-column table).

Removing columns from the template does not remove the columns from the table object, so you can use the object panel to add back any columns as needed.
