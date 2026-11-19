---
source: https://qlik.dev/changelog/203-api-updates-apps-placement/
last_updated: 2026-04-20T13:34:03+01:00
---

# New Apps API endpoints for managing analytics application engine sizes

The Apps API now includes three new endpoints that give you self-service control over application engine placement:

- `PUT /v1/apps/{appId}/placement`: Set a minimum engine size override for an app
- `GET /v1/apps/{appId}/placement`: Retrieve the current engine size override for an app
- `DELETE /v1/apps/{appId}/placement`: Remove the engine size override and revert to automatic placement

## Why this matters

While Qlik Cloud automatically places applications on the best available engine, you can now override this placement by
setting a minimum engine size.
This self-service capability eliminates operational overhead and enables faster response to evolving app performance
needs.

Set a minimum engine size to help maintain consistent CPU and memory resources for:

- Complex visualizations and large chart objects that generate hypercubes
- Performance-critical business applications
- Apps requiring predictable performance characteristics

You can specify engine sizes from 40 GB to 200 GB, or set to 0 to return to automatic placement.

## Capacity considerations

Pinned applications consume large app capacity.
When you override placement, you control the minimum compute resources
available for interactive consumption.
Track this consumption through [quota events](https://qlik.dev/apis/event/quotas/).

For guidance on determining the appropriate engine size for your apps, see
[Pin applications to engine sizes](https://qlik.dev/manage/analytics-applications/analytics-engine-size-override).

For complete API reference details, see the [Apps API reference documentation](https://qlik.dev/apis/rest/apps/).
