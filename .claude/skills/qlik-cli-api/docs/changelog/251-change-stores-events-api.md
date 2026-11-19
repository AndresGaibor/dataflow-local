---
source: https://qlik.dev/changelog/251-change-stores-events-api/
last_updated: 2026-10-01T15:03:30+02:00
---

# Change stores event API now available

The Change stores event API is now available, letting you react when users save changes to a
[change store](https://qlik.dev/apis/rest/analytics/change-stores/). Change stores track modifications made through the
[Write table](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/WriteTable/Analyze/write-table.htm)
visualization.

The following event is available:

- **Changes saved** (`com.qlik.analytics.change-store.changes.saved`): Published when a user commits changes in a
  change store. Includes the change store ID, the space ID for shared-space stores or owner ID for personal-space
  stores, the user who saved the changes, and the commit timestamp.

Use this event to trigger downstream pipelines, sync external systems, or record modifications to change stores,
instead of polling the [Change stores API](https://qlik.dev/apis/rest/analytics/change-stores/) for updates.

For more information, see the [reference documentation](https://qlik.dev/apis/event/analytics/change-stores/).
