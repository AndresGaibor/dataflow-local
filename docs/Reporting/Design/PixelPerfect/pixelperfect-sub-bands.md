---
title: "Working with sub-bands in PixelPerfect reporting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-sub-bands.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Getting started with PixelPerfect report templates", "Banded report authoring"]
---

# Working with sub-bands in PixelPerfect reporting

Sub-bands allow you to create multiple versions of the same report band to display different content based on conditions. You can create advanced, dynamic output that is tailored to any number of scenarios, such as specific field values, aggregated totals, and more.

## Creating sub-bands

Do the following:

1. Create one or more bands that support sub-bands in your PixelPerfect template. For a highly formatted table, this can be the GroupHeader band.

   Typically, the parent band is connected to a data binding, rather than the sub-bands themselves.
2. Right-click the band, and select Insert Sub-Band. Add as many sub-bands as desired.

After you have created sub-bands, you can customize them with conditional logic. For example, to show sub-band data conditionally:

1. Select a sub-band.
2. Click ![Formula](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) on the right side panel to expand the Expressions menu.
3. In the menu, click the three-dot icon next to Visible.

   The Expression Editor opens.
4. Define the conditional expression—for example, an Iif expression.
5. Repeat the process for each sub-band.

## Uses

You can use sub-bands to:

- Dynamically include or exclude data from reports using a condition—for example, use this to filter for an individual field value or hide elements unless an aggregation has a large enough value.
- Style report content dynamically.

## Example

For an example of using sub-bands to create a highly formatted table, see [*Example - Highly formatted table with sub-bands*](pixelperfect-sub-bands-example.htm).
