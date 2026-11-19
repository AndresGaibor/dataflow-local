---
source: https://qlik.dev/changelog/216-webhooks-legacy-fields-removal/
last_updated: 2026-10-02T10:20:50Z
---

# Deprecation notice - Webhooks legacy event fields will be removed on December 10, 2026

> **Timeline update - October 2, 2026:** The removal date for legacy webhook event fields has been extended from October 6, 2026, to December 10, 2026.

> **Deprecation notice:** Legacy fields in Qlik Cloud webhook event payloads will be removed on December 10, 2026.

Following the [initial announcement on September 2, 2025](https://community.qlik.com/t5/Official-Support-Articles/Qlik-Cloud-Webhooks-Migration-to-new-event-formats-is-coming/ta-p/2528660),
Qlik Cloud webhook events have been emitting hybrid payloads containing both legacy and CloudEvent fields since
November 3, 2025.

On **December 10, 2026**, hybrid events will be replaced by
CloudEvent-only payloads. Any integrations relying on legacy fields such as `eventId`, `eventTime`, `eventType`,
`cloudEventsVersion`, `contentType`, or `extensions` properties must migrate to their CloudEvent equivalents before
this date.
