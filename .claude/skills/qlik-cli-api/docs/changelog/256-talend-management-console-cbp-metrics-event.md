---
source: https://qlik.dev/changelog/256-talend-management-console-cbp-metrics-event/
last_updated: 2026-10-09T16:39:41+02:00
---

# Talend Management Console Capacity-Based Pricing metrics event now available

The [Talend Management Console event API](https://qlik.dev/apis/event/talend-management-consoles/) now publishes Capacity-Based Pricing
(CBP) metrics for managed and unmanaged task executions.

The following event is available:

- **CBP execution metrics aggregated** (`com.qlik.talend-management-console.cbp-execution-metrics.aggregated`):
  Published when CBP metrics are aggregated for a task execution. Includes the execution ID, job ID, batch number, and
  CBP metrics such as input volume, event count, and duration, depending on the execution type.

Use this event to track consumption relative to your
[Qlik Talend Cloud subscription](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-QTC.htm),
or use the metrics in your own usage reporting.

For more information, see the [reference documentation](https://qlik.dev/apis/event/talend-management-consoles/).
