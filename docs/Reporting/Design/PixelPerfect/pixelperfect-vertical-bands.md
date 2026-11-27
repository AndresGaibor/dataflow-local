---
title: "Working with vertical bands in PixelPerfect reporting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-vertical-bands.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Getting started with PixelPerfect report templates", "Banded report authoring"]
---

# Working with vertical bands in PixelPerfect reporting

Vertical bands allow you to arrange report content differently than horizontal bands. Rather than a standard relational table, vertical bands form a structure where each column corresponds to a single value from a dimension in your application—for example, a year, month, or category dimension. Other columns of interest are organized as rows rather than columns. The classic example of vertical bands is the profit and loss report, where the profit and loss fields are listed as rows in the table, and each column in the table represents a single year, quarter, or month value.

There are three types of vertical bands: VerticalHeader, VerticalDetail, and VerticalTotal. You can add one or more of these bands to your report template. You can add vertical bands within various types of horizontal bands.

## Creating vertical bands

Do the following:

1. Right-click a compatible horizontal band in your PixelPerfect template.
2. Select Insert Vertical Band, and then select a type of vertical band:

   - VerticalHeader
   - VerticalDetail
   - VerticalTotal

Select Insert Vertical Band, and then select a type of vertical band:

## Uses

You can use vertical report bands to:

- Create summary tables that are organized vertically rather than horizontally—for example, a profit and loss statement.
- Organize charts in vertical columns.

## Example

For an example of using vertical bands to create a profit and loss statement, see [*Example - Creating a profit and loss table with vertical bands*](pixelperfect-vertical-bands-example.htm).
