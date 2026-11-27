---
title: "Accessing view and usage metrics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/viewing-usage-metrics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Cloud Analytics activity centers", "Navigating analytic content"]
---

# Accessing view and usage metrics

Viewer and usage metrics allow you to quantify the value of your content at-a-glance by showing both the number and trend of unique viewers in the last 28 days (Viewed by) as well as the number of applications that are currently using a particular item (Used in).

Usage metrics are turned on by default in a tenant and can be turned off by a tenant administrator. If you do not see these statistics in your tenant, it is likely they are turned off. For more information, see [*Displaying content usage metrics*](../Admin/mc-usage-metrics.htm).

## Content viewer metric

The viewer metric for content shows a count of how many unique users have accessed content in the last 28 days.

Viewer metrics on an application

![Viewer metric on an app showing one unique viewer in the last 28 days](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_viewer-metric-app.png "Click to view full size")

An item's view count over the last 28 days is a good indication of its popularity. Knowing how many times an item has been viewed recently also helps content owners gain valuable insights into their work. For instance, an item that has been viewed by a relatively small number of users might indicate that the item is no longer useful or needs to be improved to increase its popularity.

Information noteThe number of views is calculated according to the number of unique viewers that have viewed the item.

### Viewer metric limitations

The viewer metric is not available for automations.

## Understanding metrics icons

The table below describes the icons that are used to display viewer and item usage metrics in Grid view. Hover over an icon to bring up a tooltip with more information. Note that the arrowhead icon used to indicate viewer trends is also shown in List view.

Metrics icons

| Details | Description |
| --- | --- |
| Unique viewers icon. Hover over it to see a tooltip with more information. | The number of unique viewers over the last 28 days. |

## Metrics locations

Viewer and usage metrics are available in the locations listed below:

- Catalog Grid view
- Catalog List view
- Dataset Overview tab
- Content Details

### Grid view

Below the content tile in Grid view:

Metrics on a data asset tile

![One of the places where viewer metrics icons are located (below the data asset tile in Grid view).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_viewer-metric-app.png "Click to view full size")

Hovering over the viewer metrics icons will show a tooltip with more information.

### List view

For any item, hovering over the Viewed by number will show a tooltip with more information.

![One of the places where viewer metrics icons are located (in List view).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/metrics-icon-list.png)

### Dataset Overview tab

In the Overview tab of datasets, you can view the metrics in the details side panel.

![One of the places where metrics icons are located (in the dataset Overview tab, in the details side panel).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/metrics-icon-overview.png)

### Content Details

Viewer metrics can be viewed in Details for content types with these metrics. On the content in catalog, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Details. In Details, the viewer metrics are displayed below the file name and content type. Hovering over the ![icon info](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) icon will show a tooltip with more information.

Information note

Viewer metrics are not available for scripts.

Details panel for a dataset when viewed in Analytics activity center, showing the viewer metrics

![Details for an app, showing the viewer metrics.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_catalog_metrics_details.png "Click to view full size")
