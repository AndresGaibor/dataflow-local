---
source: https://qlik.dev/changelog/260-automations-run-ended-event-is-properties-deprecation/
last_updated: 2026-10-15T16:04:40Z
---

# Deprecation notice - isTestRun and isArchived properties in the Automations run ended event

The `isTestRun` and `isArchived` properties in the data payload of the `com.qlik.v1.automation.run.ended` event are
deprecated and will be removed on or after May 30, 2027.

Use the following replacement properties, which have the same type and meaning:

| Deprecated property | Replacement property |
| ------------------- | -------------------- |
| `isTestRun`         | `testRun`            |
| `isArchived`        | `archived`           |

Until the deprecated properties are removed, the event includes both the deprecated and the replacement properties.
Update any code that reads `isTestRun` or `isArchived` from this event to read `testRun` and `archived` instead.

For more information about the event, see the
[Automations events API](https://qlik.dev/apis/event/automations/#com-qlik-v1-automation-run-ended).
