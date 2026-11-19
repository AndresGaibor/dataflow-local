---
source: https://qlik.dev/changelog/264-geo-operations-geocoding-event/
last_updated: 2026-11-06T17:51:56+01:00
---

# New Geo-operations event API for geocoding lookups

The Geo-operations event API is now available, allowing you to track geocoding lookups performed in Qlik Cloud.

The following event is available:

- **Geocoding performed** (`com.qlik.analytics.geocoding.executed`): Published when a geocoding lookup is executed.
  The event payload includes the request ID, the number of rows sent for geocoding, the operation type
  (`pointtoaddresslookup` or `addresspointlookup`), and the application ID when available.

Use this event to monitor geocoding activity and track lookup volumes.

For more information, see the [Geo-operations event API reference documentation](https://qlik.dev/apis/event/analytics/geocodings/).
