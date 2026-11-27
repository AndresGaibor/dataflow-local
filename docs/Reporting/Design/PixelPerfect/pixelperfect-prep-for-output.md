---
title: "Preparing your report template for output"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-prep-for-output.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template"]
---

# Preparing your report template for output

Whether you are printing your reports or distributing them as PDFs, it is important to know how you can prepare your report template for optimal output.

## Configuring page size, orientation, and margins

One of the most important considerations for your report output is the size of the page on which contents are added. You can set the page size, orientation, and margins in the global report properties.

Do the following:

1. In the designer, click in the blank space outside the design surface.
2. Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side of the designer. These are the properties for the entire report.
3. Expand Page Settings.
4. The default page orientation is portrait. To switch to landscape orientation, check the Landscape checkbox.
5. For Paper Kind, choose from one of the preset paper sizes.
6. Expand Margins. You can set the exact margins (left, right, top, and bottom) with exact values as per the configured Measure Units for the report (also configurable in the same properties menu).

## Adding page breaks

To add a manual page break, use the ![Page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_page_break_outline.svg) Page Break object. This object forces content below it to be split onto a new page.

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_page_break_outline.svg) Page Break object onto the design surface.
2. You can configure a number of settings for the page break by selecting the object and opening the  ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right panel.

## Page numbers

You can insert page numbers onto the report using the ![Page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_page_info_outline.svg) Page Info object.

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Page](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_page_info_outline.svg) Page Info object onto the design surface.
2. With the object selected, open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu from the right side panel.
3. Under Page Info Tasks > Page Information, use the drop down menu to select Page Number.
4. You can configure a number of other settings in the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu, such as the starting page number and appearance settings.

## Adding a report cover

You can add a report cover that appears once at the beginning of the report. To create a report cover, you need to insert a ReportHeader band. For specific instructions, see [*Creating a new band*](pixelperfect-banded-authoring.htm#Create).

## Adding a table of contents

Use the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list_outline.svg)Table of Contents object to add an interactive table of contents to the generated report. Tables of contents can be inserted in the report header or footer.

For full details, see [*Adding a table of contents*](pixelperfect-toc-bookmarks.htm).
