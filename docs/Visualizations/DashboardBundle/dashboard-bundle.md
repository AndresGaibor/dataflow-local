---
title: "Dashboard bundle"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/dashboard-bundle.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization"]
---

# Dashboard bundle

Dashboard bundle is a set of controls that you can use to enhance navigation and selection in your Qlik Sense application.

## Dashboard bundle controls

Dashboard controls are in the asset panel under Custom objects.

The following controls are included:

- [*Animator*](animator.htm)

  You can animate changes in your [visualizations](#glossary-1 "Glossary term") over a period of time.

  [*Creating animators*](creating-animator.htm)
- [*Date range picker*](date-range-picker.htm)

  You can select a single date or a range of dates from a calendar.

  [*Creating date range pickers*](creating-date-range-picker.htm)
- [*Layout container*](layout-container.htm)

  Add and arrange visualizations in a container.

  [*Creating layout containers*](creating-layout-container.htm)
- [*Line*](line.htm)

  Add vertical and horizontal lines to a [sheet](#glossary-2 "Glossary term").

  [*Creating lines*](creating-line.htm)
- [*Text*](text-object.htm)

  A text object allows application developers to create and format text.

  [*Creating Text objects*](creating-text-object.htm)
- [*Variable input control*](variable-input.htm)

  You can set the value of a variable.

  [*Creating variable input controls*](creating-variable-input.htm)
- [*Video player*](video-player.htm)

  You can add a video to your sheet.

  [*Creating video players*](creating-video-player.htm)

Information note
The On-Demand reporting control is not available in Qlik Cloud.

## Deprecated controls

These controls have been deprecated by the addition of a native control. New instances cannot be added. Most of these will be removed from your applications in May 2027, while others will remain but require migration to the native controls.

Tenant administrators can find deprecated Dashboard bundle controls with the Deprecated charts opened in sheet system event. This event is triggered whenever a user opens an application sheet containing a deprecated chart.

For more information, see [*Finding deprecated charts*](../find-deprecated-charts.htm).

Information note

More information about deprecated charts can be found on [Qlik Community](https://community.qlik.com/t5/Official-Support-Articles/About-the-deprecation-of-Qlik-Analytics-charts/ta-p/2543997).

### Deprecated controls that will be removed from user applications

Existing instances of these controls will be deleted in May 2027.

#### Container

Deprecated by Tab container. For more information, see [*Tab container*](../Container/container-object.htm).

You can convert a container to a tab container by dragging and dropping a tab container onto a container from the assets panel.

If you need to configure existing instances of this control, please refer to the last version of the help before deprecation. [Container - November 2024](https://help.qlik.com/en-US/sense/November2024/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/Container/container-object.htm).

#### Share button control

Deprecated by Make public. For more information see: [*Granting access to sheets, sheet groups, bookmarks, and stories*](../../Share/make-public-or-private.htm)

If you need to configure existing instances of this control, please refer to the last version of the help before deprecation. [Share button- May 2021](http://help.qlik.com/en-US/sense/May2021/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/share-button.htm)

#### Show/hide container

Deprecated by Container.  For more information see: [*Tab container*](../Container/container-object.htm)

If you need to configure existing instances of this control, please refer to the last version of the help before deprecation. [Show/hide container - June 2019](http://help.qlik.com/en-US/sense/June2019/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/show-hide-container.htm)

#### Tabbed container

Deprecated by Tab container.  For more information see: [*Tab container*](../Container/container-object.htm)

If you need to configure existing instances of this control, please refer to the last version of the help before deprecation. [Tabbed container - June 2019](http://help.qlik.com/en-US/sense/June2019/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/tabbed-container.htm)

#### Navigation button

Deprecated by Button.  For more information see: [*Button*](../Button/button.htm)

If you need to configure existing instances of this control, please refer to the last version of the help before deprecation. [Navigation button - February 2020](http://help.qlik.com/en-US/sense/February2020/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/navigation-button.htm)

### Other deprecated controls

#### NL Insights

Deprecated by native NL insights object. Existing instances may need to be migrated manually. See [*Migrating from the Dashboard bundle to native object*](../NLInsights/nl-insights.htm#Migratin).

For full details about the native object, see: [*NL insights*](../NLInsights/nl-insights.htm).

## Limitations

When you use objects from Dashboard bundle there are some limitations compared to built-in controls. The following limitations are valid for all controls from Dashboard bundle:

- The user interface of the visualization is not localized to the language that Qlik Sense is using.
- Right-to-left reading order is not supported.
- Accessibility features are not supported.
- It is not possible to edit objects from an object bundle supplied by Qlik with Dev Hub.

The following table shows which additional features are supported, or not supported, for all bundled objects:

- Download

  Downloading as image, PDF, or Excel.
- Storytelling

  Using a [snapshot](#glossary-3 "Glossary term") of a visualization created with an object in a [story](#glossary-4 "Glossary term").
- Alternate states

  Making different selections on the same [dimension](#glossary-5 "Glossary term") and comparing the selections in a single visualization or in two or more visualizations side by side.

Dashboard bundle capability support

| Control | Download | Storytelling | Alternate states | Monitor in activity centers |
| --- | --- | --- | --- | --- |
| Animator | Excel only | Not applicable | Yes | No |
| Date picker | Not applicable | Not applicable | Yes | No |
| Layout container | Image and PDF only | Yes | Yes | Yes |
| Line | Image and PDF only | Yes | Yes | Yes |
| Text | Yes | Yes | Yes | Yes |
| Variable input | Not applicable | Not applicable | Not applicable | No |
| Video player | Not applicable | Yes | Yes | No |
