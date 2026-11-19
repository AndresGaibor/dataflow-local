---
source: https://qlik.dev/changelog/122-reporting-events/
last_updated: 2025-07-08T16:09:30Z
---

# The com.qlik.v1.reporting-service.audit event is being replaced

Qlik Cloud leverages an event-driven architecture to communicate between the
services in the platform. As part of an ongoing project to standardize event formats,
the event `com.qlik.v1.reporting-service.audit` is being replaced
by `com.qlik.v1.report.finished`. Users who consume this event via the
[Audits API](https://qlik.dev/apis/rest/audits) should migrate to the new event immediately.

As of this changelog, both events will be emitted until **May 5, 2025**.
On or after this date, the `com.qlik.v1.reporting-service.audit` event will no longer
be captured. Events already stored by the Audits API will remain available.

The new event is identical to the existing event, with the exception of the
`eventType` field. The `eventType` field will be updated from
`com.qlik.v1.reporting-service.audit` to `com.qlik.v1.report.finished`.

> **Note:** The `com.qlik.v1.reporting-service.audit` event is experimental and unpublished.
> In general, Qlik does not post deprecation notices for experimental and/or unpublished
> events. An exception has been made in this case due to the external
> usage of this event. Qlik reserves the right to deprecate without notice experimental
> and/or unpublished events.

For more information, review the [Audits API](https://qlik.dev/apis/rest/audits) specification.
