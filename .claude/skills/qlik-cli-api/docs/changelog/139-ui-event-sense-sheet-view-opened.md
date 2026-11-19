---
source: https://qlik.dev/changelog/139-ui-event-sense-sheet-view-opened/
last_updated: 2025-10-31T14:06:52+01:00
---

# New UI event - Sense Sheet View Opened

A new UI event, Sense Sheet View Opened, is now available.
This event is triggered by the client (browser) each time a sheet change is recorded, whether in the native Qlik Sense
experience or when using qlik-embed with the `classic/app` UI.

The event is not emitted when switching between sheet modes (such as View to Edit) or in non-sheet UIs (like Stories or
Reporting).

For more information, refer to:

- the [Qlik Cloud UI events overview](https://qlik.dev/apis/ui-event/).
- the [reference documentation](https://qlik.dev/apis/ui-event/analytics/#com-qlik-v1-analytics-analytics-app-client-sheet-view-opened).
