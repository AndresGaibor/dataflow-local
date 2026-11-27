---
title: "Monitoring visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Hub/monitor-charts-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Monitoring visualizations

You can monitor [visualizations](#glossary-0 "Glossary term") in [activity centers](#glossary-1 "Glossary term") and in the Qlik Analytics mobile app, enabling you to view [charts](#glossary-2 "Glossary term") without opening any applications.

You can select a visualization and monitor it from your [personal space](#glossary-3 "Glossary term") in your activity centers.
You can add visualizations from both [sheets](#glossary-4 "Glossary term") and from Insight Advisor. Visualizations you add this way can be found in Your charts on the Home section of Analytics and Insights activity centers or in Catalog or Browse. You can filter on Charts in Catalog. Any [selections](#glossary-5 "Glossary term") applied to the visualization are kept when it is added to your activity centers. The monitored visualization updates every time the source application reloads.

In shared or managed spaces, you can share a monitored visualization from an application in that space if you have the appropriate permissions. Adding visualizations to a shared space requires one of the following permissions:

- Owner
- Can manage
- Can edit
- Can edit data in applications

Adding visualizations to a managed space requires one of the following permissions:

- Owner
- Can manage

Tip noteAdd the visualization to the Mobile Content collection to make it available in the Qlik Analytics mobile app.

## Viewing monitored charts

When you open a monitored chart in an activity center, the chart shows the latest version of the chart from the last reload of data in the source application. You can view the chart, the chart details, and the history.

Visualization in an activity center

![A chart open in the hub with Details expanded](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Charts/ui_monitored-chart.png "Click to view full size")

Information noteIf you have added a visualization from an application to which you no longer have access, the last version of the visualization you had access to will display.

The top of the chart shows the chart history. You can select to view previous versions of the chart, or compare the current version to previous versions. New versions are added every day the source application reloads. If a version already exists for that date, the version is updated with the latest data from the application. You can view the previous 10 chart versions.

Chart history

![The history dropdown expanded, showing versions of the chart from August 6th and August 5th.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Charts/ui_monitored-chart-history.png "Click to view full size")

History comparison

![A side-by-side comparison of the August 6th and August 5th versions of the monitored chart.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Charts/ui_monitored-chart-history-comparison.png "Click to view full size")

Selections displays the selections that were applied to the chart when you added it to your activity centers. You cannot make selections in the chart.

Selections

![The selections of the monitored chart. In this chart, 4 selections have been applied.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Charts/ui_monitored-chart-selections.png "Click to view full size")

In the details, you can view:

- The source application.
- The chart owner.
- The space.
- The source application reload schedule.
- The date of the last source application reload.
- The date of the last update.
- The creation date.
- Any tags added to the chart.

You can edit the chart's title and tags by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) >Edit details.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Charts/ui_monitored-chart-history.png)

You can view the chart in the source application by clicking View in application, which opens the chart in the application with selections applied. For charts generated in Insight Advisor, View in application opens Insight Advisor in Sheet. You can optionally view additional charts from the same Insight Advisor search or analysis.

### Inactive charts

Charts that have not been viewed in more than 90 days will be deactivated and will no longer be updated with new versions from the application. Deactivated charts cannot be reactivated. If you still want to monitor that chart, click View in application in the deactivated chart and then create a new monitored chart.

## Monitoring visualizations in activity centers

Do the following:

1. Right-click a visualization and select Monitor in activity centers.
2. Optionally, select Store view state to lock the zoom and scroll position in the monitored chart to the current view.

   Information note

   As data changes, this option may make data points appear out of view.
3. Optionally, edit the name of the visualization.
4. Optionally, add tags to the visualization.
5. After Location, select the destination space for the monitored visualization.
6. Click Monitor.

Tip noteAdd the visualization to the Mobile Content collection to make it available in the Qlik Analytics mobile app.

## Sharing charts

Charts added to shared or managed spaces are shared with other members of those spaces. If you have permission in the space, you can also invite users to view the chart in the space.

Do the following:

1. In an open monitored chart, click Share > Invite.
2. Enter a name or email to find the members you want to share it with.
3. Select their permission level for the space and click Send.

## Copying and saving charts as images

You can copy monitored charts to your clipboard or save them as PNG images. This allows you to share chart snapshots in emails, presentations, or collaboration tools without requiring access to Qlik Cloud.

Do the following:

1. In an activity center, open a monitored chart.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Do one of the following:
   - Select Copy as image, then paste the image into your destination application.
   - Select Save as image. The chart is downloaded as a PNG file with the chart name and timestamp.

Information noteCopy as image and Save as image are not available if the chart is unavailable or has an error.

## Removing visualizations from activity centers

Do the following:

1. In an activity center, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a visualization, and select Delete.
2. Click Delete.

## Limitations

Monitoring visualizations has the following limitations:

- The following visualizations cannot be monitored:
  - Button
  - Filter pane
  - Word cloud chart extension
  - Multi-KPI extension
  - Trellis container extension
  - Dashboard bundle objects cannot be monitored, aside from the following objects:
    - Layout container
    - Line
    - Text

    These objects are monitored as images that cannot be interacted with like other monitored charts.
  - Custom extensions
- You can view data in tooltips when you hover over values in the chart for the following charts:
  - Bar chart
  - Box plot
  - Bullet chart
  - Combo chart
  - Distribution plot
  - Funnel chart extension
  - Histogram
  - KPI
  - Line chart
  - Mekko chart
  - Org chart
  - Pie chart
  - Sankey chart extension
  - Scatter plot
  - Waterfall chart
- Selections from dynamic bookmarks are not supported in monitored charts. The selections in the monitored visualization will be the selections that were applied in the visualization when it was added to your activity centers.
- Previous or next selections from [set analysis](#glossary-7 "Glossary term") expressions are not supported in monitored charts.
- Variable values in monitored charts are set and are not updated if they change in the source application.
- If the source application reloads within five minutes of the previous reload, a new chart history version is not created.
- Charts within custom tooltips will not be included in the tooltip when you are monitoring a visualization.
- Monitored visualizations using cyclic dimensions cannot cycle dimensions in the activity centers.
- If you apply a shadow to a chart in the application, the shadow is not shown when you monitor the chart in activity centers.
- You cannot monitor visualizations from an application using section access in a shared or managed space.
- Visualizations generated by Insight Advisor can only be shared in a shared or managed space if they are first added to a sheet and then selected to be monitored.

The following technical limitations apply when monitoring visualizations.
These limits are checked when you click Monitor in activity centers. If these limits are exceeded, you will see an error message. If this issue occurs, contact a user with Can edit permission in the application.

The specific limitations are listed below:

- Maximum number of fields in the selections: 125
- Maximum number of field values in the selections: 150,000 total field values across one or many fields
- Maximum number of alternate states: 125

  [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm)
- Maximum number of patches: 100

  Patches are properties or styling applied in the application. For example: Adding a sort to a table column.
- Maximum number of variables: 1,100

  [*Using variables in expressions*](../Variables/work-with-variables.htm)
- Maximum image size: 4,000 x 4,000 pixels
- Minimum image size: 5 x 5 pixels for charts and 20 x 20 pixels for sheets

Related learning:

- [How do I monitor a chart directly in the Qlik Cloud Analytics Hub?](/lnk/How_monitor_chart_cloudhub)
