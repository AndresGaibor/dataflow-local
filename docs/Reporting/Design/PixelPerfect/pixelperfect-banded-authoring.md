---
title: "Banded report authoring"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-banded-authoring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Getting started with PixelPerfect report templates"]
---

# Banded report authoring

PixelPerfect report templates are constructed using a banded design. Content in the report is structured as a series of horizontal (and sometimes vertical) bands. Some bands can be connected to specific data for looping of content (with [levels](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/pixelperfect-work-with-levels.htm)). Bands can be arranged in hierarchical structures.

Bands are used to arrange content in the way it is intended to appear in output. Bands can be nested within other bands. Bands allow you to compose dynamic reports that alternate between varied and repeated content. With bands, you also have maximum control over the printed output of your reports, with a number of bands being used mainly to prepare your report to be printed.

In your report template, the bands are shown on the side of the design surface.

Bands in a PixelPerfect report template

![Image showing the bands in the PixelPerfect template as they appear in the design surface, such as TopMargin1,Detail1, and so on](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-bands.png "Click to view full size")

## Types of bands

There are multiple types of bands that can appear in a PixelPerfect report template. Every PixelPerfect template contains a TopMargin, Detail, and BottomMargin band. These bands cannot be removed from the template.

The TopMargin and BottomMargin bands help you organize content so that it is consistent in where it starts and ends. These bands help produce content that is ready to be printed. If desired, you can add repeatable objects in these bands (such as page numbers or logos), or you can use the PageHeader and PageFooter bands for this purpose.

Every template also has a Detail band that cannot be removed. If you are creating a detailed report filled with varied content and levels, you will probably need to create additional DetailReport bands to arrange the report data. When creating simple reports, the default Detail band is useful for adding non-repeated content.

The following sections outline the most commonly used bands, and what you can do with them.

### DetailReport

Create DetailReport bands in your template to organize the presentation of data. DetailReport bands can be bound to application data, creating levels. You can nest DetailReport bands within other DetailReport bands to achieve a complex design that allows granular, filtered analysis.

### PageHeader and PageFooter

PageHeader and PageFooter bands appear at the start and end of every page. These bands are useful for:

- Adding fixed images such as logos
- Adding repeated title information
- Adding page numbers

### ReportHeader and ReportFooter

Add report headers and footers with ReportHeader and ReportFooter bands. The ReportHeader band appears once, at the start of the report. The ReportFooter band appears once, at the end of the report. These bands are useful for:

- Adding a report cover.
- Adding an interactive table of contents.

  [*Adding a table of contents*](pixelperfect-toc-bookmarks.htm)
- Adding summary information, and descriptions that do not need to be repeated.

### Vertical bands

Vertical bands can be used to organize report data in vertical columns. These bands allow you to create alternatively structured tables, and they work particularly well for briefly summarizing detailed source data. For more information and an example, see:

- [*Working with vertical bands in PixelPerfect reporting*](pixelperfect-vertical-bands.htm)
- [*Example - Creating a profit and loss table with vertical bands*](pixelperfect-vertical-bands-example.htm)

### Sub-bands

Sub-bands allow you to create multiple versions of the same report band to display different content based on conditions. For more information and an example, see:

- [*Working with sub-bands in PixelPerfect reporting*](pixelperfect-sub-bands.htm)
- [*Example - Highly formatted table with sub-bands*](pixelperfect-sub-bands-example.htm)

## Bands and levels

Bands are used to arrange content in the way it is intended to appear in output. Bands can be nested within other bands. As you add content to your template, you can connect some bands to a data binding so that it is repeated in output, with each iteration of the content filtering the application data for a different dimension or chart value. When you perform this action, you are creating a level.

For more information about levels, see [*Working with levels*](pixelperfect-work-with-levels.htm) and [*Using a level to loop over application data*](pixelperfect-create-level.htm).

## Working with bands

As you build your template, you can create and delete bands, and rearrange them on the design surface.

### Creating a new band

Do the following:

1. In the PixelPerfect designer, right-click in or outside the design surface.

   Where you right-click affects whether or not the new band is created within other bands. If you right-click on an area with an existing band, the new band is created within that band.
2. Do one of the following:

   - Move your cursor over Insert Band, and then select an option from the list. This creates a horizontal band.
   - Move your cursor over Insert Vertical Band, and select an option from the list. This creates a vertical band.

### Resizing a band

You can resize bands in the template by hovering your cursor over the color-coded block where the band's name is shown, and then clicking and dragging.

To resize a band to exact dimensions, you can configure the band's properties.

Do the following:

1. Select the band.
2. Click ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) in the right side panel to open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu.
3. Under Layout > Size, set a width and height.

### Deleting bands

Some bands cannot be deleted (see [*Types of bands*](#Types)). For a band that you can delete, remove it by selecting the band and then clicking the Delete key on your keyboard. Alternatively, select the band and then click the ![Cross mark](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) icon in the toolbar at the top of the designer.

## Additional band types

There are additional band types that can be used for advanced report authoring. For examples, see:

- Sub-bands: [*Example - Highly formatted table with sub-bands*](pixelperfect-sub-bands-example.htm)
- Vertical bands: [*Example - Creating a profit and loss table with vertical bands*](pixelperfect-vertical-bands-example.htm)

## Viewing and arranging bands

The Report Explorer offers an alternative view of the structure of your report, laying out the report elements in a hierarchical structure. In this structure, you can view all bands in the template and their positions in the hierarchy. You can rearrange bands that can be moved, by clicking and dragging them to new positions in the structure.

[*Using the Report Explorer*](pixelperfect-arrange-content.htm#ReportExp)
