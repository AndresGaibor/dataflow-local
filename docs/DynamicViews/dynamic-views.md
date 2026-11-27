---
title: "Managing data with dynamic views"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DynamicViews/dynamic-views.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data"]
---

# Managing data with dynamic views

Dynamic views offer users the ability to directly control both the analytic sources they want to explore and when data is refreshed in [visualizations](#glossary-0 "Glossary term").

Dynamic views enable you to query and view relevant subsets of large data sets in [charts](#glossary-1 "Glossary term") that can be dynamically refreshed as [selections](#glossary-2 "Glossary term") are made. This enables up-to-date visualizations for high data volume or fast-changing data scenarios.

## Dynamic views overview

Dynamic views enable you to connect a base application to another application. Master visualizations from that application can then be used in the base application. This enables application creators to use master visualizations from the template application as dynamic charts in other applications. There is no limit to the number of dynamic views you can add to your base application.

Sheet view with dynamic view and dynamic charts

![A sheet with a dynamic view displaying four dynamic charts](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_view_rev.png "Click to view full size")

Dynamic views are made from three main components:

- Dynamic views: A mechanism added to base applications that connect to template applications and enable application creators to add master visualizations from the template application to the base application.
- Dynamic view template applications: A Qlik Sense application containing [connections](#glossary-4 "Glossary term") to data sources, such as cloud databases.
- Dynamic charts: Master visualizations in the dynamic view template application that can be added to base applications and that can be manually refreshed by users.

The template application and the base application do not need to use the same data. If you have a data set covering customer purchases, you could add a dynamic view to a template application containing weather data to look at any correlations.

If the data queried from the template application’s source can be filtered using values in your base application, you can use binding expressions in the template application’s script. This enables the dynamic view to only query a subset of data specifically related to the selections in the base application from the data sources of the template application. For example, you could bind the [field](#glossary-5 "Glossary term") SalesDate in the base application to the field DailyTemperatureReadingDate in the template application.

This subset capability is useful if your base application contains aggregated data and the dynamic view data is from the same source but is more granular than the base application data (e.g. the base application contains sales by month and product brand while the template application contains sales by day and product name). For more information on adding binding expressions to template applications, see [*Binding expressions in on-demand template applications*](../LoadData/bind-expressions-OnDemand-template-app.htm).

Dynamic views can be used with any kind of data. Dynamic views are particularly useful when dealing with large volumes of data or fast changing data scenarios, where it is better to perform data aggregations on the database. This helps avoid latency in data transfers from the data source.

Dynamic views are accessible from the Assets panel in sheet edit mode.
Dynamic views are enabled by tenant administrators in the Administration activity center.
For information about enabling dynamic views, see [*Accessing the Administration activity center*](../Admin/management-console.htm).

Dynamic views are similar to on-demand application generation. Both use template applications to offer on-demand data, but dynamic views allow you to use individual charts in sheets rather than generating whole on-demand applications. If you are also using on-demand applications, you can create dynamic views using your on-demand template applications. For more information about generating on-demand applications, see [*Managing big data with on-demand applications*](../DataSource/Manage-big-data.htm).

### Dynamic views

When you create a dynamic view, you select a template application and optionally apply a row limit expression to control how much data the dynamic view will access. Once the dynamic view is created, you can then add master visualizations from the template application to your [sheets](#glossary-7 "Glossary term").

Multiple dynamic views can use the same template application. Each dynamic view is refreshed individually. If bind expressions are used in a dynamic view’s template application script, selections made in the base application can control which data is loaded into each dynamic view that uses that template application. Two dynamic views using the same template can be used to compare side-by-side charts of two separate subsets of granular data. For example, you have two dynamic views using the same template application. You could select Jan 1, 2018 from the base application SaledDate field and refresh one dynamic view. You could then change the selection to Jan 1, 2019, refresh the other dynamic view, and then compare the dynamic charts.

For information on creating and editing dynamic views, see [*Managing data with dynamic views*](#).

For information on using dynamic views, see [*Using dynamic views and charts*](using-dynamic-views.htm).

### Dynamic view template applications

A dynamic view template application is a Qlik Sense application used to supply dynamic views with data and master visualizations.

Dynamic view templates can have a [load script](#glossary-8 "Glossary term") that contains data binding expressions used to formulate queries made on the data sources based on selections made in the base application. Binding expressions are usually created by users with experience writing Qlik Sense load scripts. Template applications can have query filter conditions that are based on input parameters supplied during the activation of dynamic charts.

Once the data model of a dynamic view template application is complete, master visualizations can be added to the template application. These master visualizations can then be accessed through dynamic views and added as dynamic charts in other applications.

For information on creating template applications, see [*Creating an on-demand template application*](../LoadData/creating-OnDemand-template-app.htm).

### Dynamic charts

Dynamic charts are derived from the master charts of a dynamic view’s template application. Dynamic charts can be added to the sheets of other applications using dynamic views. Unlike other Qlik Sense charts, users can control when the source data in a dynamic view is refreshed using a refresh option in the charts. When a dynamic view’s data is controlled by bind expressions, Qlik Sense tracks the base application selection state. A stale data icon appears on each chart of a dynamic view whenever the base application's selection state changes so that the new value sets for and off the dynamic view's bound fields no longer match the values used for the view's last refresh.

For information about using dynamic charts, see [*Using dynamic views and charts*](using-dynamic-views.htm).

## Dynamic views limitations

Dynamics views have the following limitations:

- Dynamic views are not supported with [stories](#glossary-9 "Glossary term"). You can add [snapshots](#glossary-10 "Glossary term") of dynamic charts to stories, but cannot use go to source with a dynamic chart.
- Dynamic views are not supported with Qlik NPrinting.
- Dynamic views support the Dashboard bundle and Visualization bundle extensions. No other extensions are supported.
- Dynamic view ownership does not change with application ownership.
- Dynamic views cannot be created in applications in a [managed space](#glossary-11 "Glossary term").
- Dynamic views are not supported in Qlik Sense Desktop.
- Dynamic views are not supported in the Qlik Analytics mobile app.
- Dynamic charts cannot be placed in a container.
- Trellis containers and containers are not supported as master charts in dynamic views.
- Write tables cannot be defined as dynamic views.

## Spaces and dynamic views

You can create dynamic views using your own applications in your [personal space](#glossary-12 "Glossary term") as template applications. Other users with access to your application with dynamic charts are able to see and refresh the dynamic charts.

You can create dynamic views using applications created by other users in [shared spaces](#glossary-13 "Glossary term"). You must have Can edit, Can edit data in applications, Can manage, or Owner permission in the shared space containing the template applications. If you want to edit a dynamic chart in the source template application, you must be the owner of that template application.

Only application owners can add new dynamic views to an application. Users with access to the application can use any dynamic view added to the application, however.

You cannot create dynamic views in applications in managed spaces. You cannot use applications in managed spaces as template applications. Dynamic charts in applications published to managed spaces can still be refreshed and users can make selections in the dynamic charts.
