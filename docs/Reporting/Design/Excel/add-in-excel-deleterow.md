---
title: "Removing rows with the Deleterow tag"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/Excel/add-in-excel-deleterow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing report templates with Qlik add-ins for Microsoft Office", "Designing tabular report templates"]
---

# Removing rows with the Deleterow tag

Using the Deleterow tag in a [report template](#glossary-0 "Glossary term") provides an easy way to remove a row that you do not need included in your report output, but is required to be included in your template to make it function correctly.

When you create native Excel tables in your report template, your table must include a blank row at the bottom. This ensures that the Qlik add-in for Microsoft Excel propagates any native Excel formulas on every row of the table. If you do not include a blank row and you add Excel calculated columns or row totals, the formula will only be applied to the row where you defined it, not the entire table.

Insert a <deleterow> tag in this blank row if you do not want a blank row to appear in the generated report.

If your report template has blank rows that you do not want to appear in the generated report, use the <deleterow> tag. This is often done to remove the gap between table data and totals. Deleterow tags are not mandatory. If you do not add one to the empty row, you will simply have a table with a blank row at the end.

You can also add <deleterow> tags below standard tabular data added from a Qlik Sense chart, or in any row in the template file. This performs the same function, removing the row the tag is inserted on.

## Applies to

This content applies to designing [tabular report](#glossary-1 "Glossary term") templates using the Qlik add-in for Microsoft Excel. See [*Qlik add-in for Microsoft Excel*](../OfficeCommon/reporting-add-ins.htm#Excel).

## Example

Let's say you have created a native Excel table, and want the last, blank row (which is required to generate the proper report output) to be removed in the generated report. Add the <deleterow> tag according to the image below.

Required use of <deleterow> tag to remove last row in Excel table

![Deleterow tag inserted at the bottom of a native Excel table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_deleterowInput.png "Click to view full size")

In the generated report, the table will appear like the image below.

Generated report output after using <deleterow> tag in template

![Output generated from use of Deleterow at bottom of native Excel table. The bottom, blank row is removed from the output](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ExcelAddIn_deleterowOutput.png "Click to view full size")
