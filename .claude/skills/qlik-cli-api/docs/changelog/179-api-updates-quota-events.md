---
source: https://qlik.dev/changelog/179-api-updates-quota-events/
last_updated: 2025-11-20T14:13:46Z
---

# Updated API - New quota event specifications have been published

New quota event specifications have been published, following the subscription of the event in the Audits service
earlier this year. The events are available via the [Audits API](https://qlik.dev/apis/rest/audits/) for customers who have
subscribed to [Large App support](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/large-app-support.htm),
and are visualized in the [App Analyzer monitoring app](https://github.com/qlik-oss/qlik-cloud-app-analyzer).

Three events are available:

- `com.qlik.v1.quota.consumed` - emitted when an app requiring large app support is opened. Documents the quota consumed
  by this action.
- `com.qlik.v1.quota.released` - emitted when an app requiring large app support is unloaded from memory. Documents
  the quota released, which is then immediately made available for use by other apps.
- `com.qlik.v1.quota.allocation-failed` - emitted when an app requiring large app support cannot be opened due to
  insufficient available quota. Documents the requested quota, quota in use at the time of the failure, and the quota
  boundary.

Each event indicates which license quota is being consumed in the `quota` field; either `appSizeTotalDefault`
for interactive consumption, or `appSizeTotalReloads` for reload consumption and app evaluations.

For more information, see the [Quota event specifications](https://qlik.dev/apis/event/quotas/).
