---
title: "Finding deprecated charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/find-deprecated-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Monitoring system and resources", "Monitoring system events"]
---

# Finding deprecated charts

Tenant administrators can monitor system events to find where deprecated visualization objects are being used in a Qlik Cloud tenant.

Information note

More information about deprecated charts can be found on [Qlik Community](https://community.qlik.com/t5/Official-Support-Articles/About-the-deprecation-of-Qlik-Analytics-charts/ta-p/2543997).

## Overview

The Deprecated charts opened in sheet event is triggered each time a user in the tenant opens an application sheet that contains a deprecated object. With this event, tenant administrators can identify where deprecated objects are being used in analytics applications, making it easier to update and replace these objects with new functionalities. For more information about the event, see [Deprecated charts opened in sheet](https://qlik.dev/apis/ui-event/analytics/#com-qlik-v1-analytics-analytics-app-client-deprecated-charts-opened).

For more information about monitoring system events, see [*Monitoring system events*](../Admin/mc-administer-events.htm).

## Deprecated objects that are identified

The following deprecated objects are detected with the Deprecated charts opened in sheet system event:

- Bar & area chart (Visualization bundle)
- Bullet chart (Visualization bundle)
- Heatmap chart (Visualization bundle)
- Multi KPI (Visualization bundle)
- Container (Dashboard bundle)
- Share button control (Dashboard bundle)
- Show/hide container (Dashboard bundle)
- Tabbed container (Dashboard bundle)
- Navigation button (Dashboard bundle)

## Learn more

- [*Monitoring system events*](../Admin/mc-administer-events.htm)
- [*Visualization bundle*](VisualizationBundle/visualization-bundle.htm)
- [*Dashboard bundle*](DashboardBundle/dashboard-bundle.htm)
