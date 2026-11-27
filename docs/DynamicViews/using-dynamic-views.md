---
title: "Using dynamic views and charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DynamicViews/using-dynamic-views.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Managing data with dynamic views"]
---

# Using dynamic views and charts

Dynamic charts can be interacted with like other Qlik Sense [visualizations](#glossary-0 "Glossary term"). Users can also directly control when to refresh data in [dynamic views](#glossary-1 "Glossary term"). If a dynamic view’s template application uses bind expressions in its [load script](#glossary-3 "Glossary term"), the query that refreshes the dynamic view’s data will usually include filter conditions that use values selected in the selection state of the base application. When a user refreshes a dynamic view, all dynamic charts associated with the view are updated with the new data.

To access a context menu for [chart](#glossary-4 "Glossary term") options, such as for taking [snapshots](#glossary-5 "Glossary term") and opening the exploration menu, right-click on the [chart](#glossary-6 "Glossary term") and select Dynamic chart.

You can interact with the dynamic view through the dynamic charts. By right-clicking a dynamic chart and selecting Dynamic view, you can refresh the charts, view constraints, and view the values of the dynamic view’s binding fields used on the last refresh of the dynamic view.

## Selections in dynamic views

Dynamic charts use the same associative selection model as standard Qlik Sense charts. Selections made in dynamic charts do not impact the [selections](#glossary-7 "Glossary term") in the base application and do not appear in the base application selection bar. You can clear the selections you have made within a dynamic view by right-clicking a dynamic chart from that view, selecting Dynamic view and then selecting Clear selections.

If bind expressions are in the dynamic view’s template application, selections made in the base application impact the data loaded into a dynamic view when it is next refreshed. Qlik Sense keeps track of the selection state that existed on the last refresh of each dynamic view. The data in the dynamic view is considered stale whenever selections change the values used by any of the bound fields in the dynamic view from when the dynamic view was last refreshed. A stale data icon displays on all of the charts of a dynamic view whenever data is stale. Refreshing a stale chart refreshes all charts from dynamic view using the updated selected value sets for each of the view’s bound fields. If you want to restore the base application’s selection state to match what it was when the dynamic view was last refreshed instead of refreshing it, use the context menu on any of the charts from that dynamic view and select Dynamic View, Show last selections, and click Apply.

Dynamic chart with stale data notification

![Dynamic chart with stale data notification](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_chart_stale_data.png "Click to view full size")

If any of the constraints have not been met for a dynamic view, such as if the current selections result in a number of rows that exceeds the maximum row count, no data will be shown for any of that view’s charts. It is not be possible to refresh the dynamic view until the selection state of the base application changes so that all constraints are met.

Dynamic chart with selections exceeding the constraints

![Dynamic chart with selections exceeding the constraints](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_chart_constraints.png "Click to view full size")

## Viewing dynamic view details

You can view the refresh history, constraints, and selections used with dynamic view in Dynamic view details. You can access the details by clicking the Dynamic view details icon in the corner of a dynamic chart.

Refresh shows the last time the data in the dynamic view was refreshed.

Refresh details in Dynamic view details

![Refresh details](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_chart_refresh.png "Click to view full size")

Constraints shows the [field](#glossary-8 "Glossary term") and row constraints applied for generating content from the dynamic view.

Current constraints in Dynamic view details

![Current constrains](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_view_dialog.png "Click to view full size")

Selections shows the selections that were applied to generate data for this view. If you make new selections that would change the data in the dynamic view and have not refreshed your dynamic view, you can click Apply to restore the original selections of the dynamic view.

Current selections in Dynamic view details

![Current selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_chart_selections.png "Click to view full size")

## Refreshing dynamic views

You can refresh the data in your dynamic view by selecting a dynamic chart from that view and clicking ![Reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg). Using the refresh option on a dynamic chart will refresh all charts from the same dynamic view. Refreshing removes any selections you have made within the dynamic charts of the dynamic view.
