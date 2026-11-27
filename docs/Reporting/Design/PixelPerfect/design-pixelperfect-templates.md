---
title: "Designing PixelPerfect report templates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/design-pixelperfect-templates.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates"]
---

# Designing PixelPerfect report templates

With PixelPerfect reporting, create professional, pixel-specific reports worthy of the most stringent customer, executive, or compliance reporting demands. PixelPerfect reports use Qlik data and visualizations, along with a library of print-specific charts.

Reports are generated in PDF format.

## Use cases

PixelPerfect reporting allows you to create dynamic reports, with an emphasis on precision of output. The embedded PixelPerfect designer makes it easy to control the exact layout of your content, making it easy to produce output that is formatted to specific proportions (for example, printed output).

## Report generation

As with Excel report templates, PixelPerfect report templates can be used to create task-based, burst report deliveries, or can be used by application consumers to generate on-demand reports.

For information about each of these distribution options, see:

- [*Configuring report generation*](../../Generate/configure-task-based.htm)
- [*Working with on-demand reporting*](../../OnDemand/reports-on-demand.htm)

## Concepts

The following concepts are important to understand when authoring PixelPerfect templates.

### Banded authoring

PixelPerfect reports are designed using a banded experience. This means that report content is structured as a series of horizontal (and vertical) bands. Bands are used for separating content, especially for the purposes of automating the repetition of content that needs to be filtered in different ways for granular analysis.

For more information, see [*Banded report authoring*](pixelperfect-banded-authoring.htm).

### Data binding

You add application data to your PixelPerfect report by binding it to specific objects in your template. At a high level, the process of adding application data to your report consists of creating a data binding (a reusable entity for specific data elements from the application), adding objects to the template, and then connecting these objects to the data bindings you have created.

For more information, see [*Data binding*](pixelperfect-data-binding.htm).

## Limitations

For a list of limitations that apply to PixelPerfect templates, see [*Qlik Reporting Service specifications and limitations*](../../Reporting-service-specifications-limitations.htm).

Related learning:

- [Qlik Reporting: Introduction to PixelPerfect Editor & Tabular Reporting](/lnk/Qlik_Reporting_PixelPerfect)
