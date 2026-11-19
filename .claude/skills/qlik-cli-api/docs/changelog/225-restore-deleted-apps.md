---
source: https://qlik.dev/changelog/225-restore-deleted-apps/
last_updated: 2026-06-18T10:08:14+01:00
---

# App deletion lifecycle events and soft-delete recovery

> **Warning:** App restoration is a disaster recovery pattern, not a recycle bin. The core app is
> recovered, but associated content such as collections, tags, data alerts, subscriptions,
> and notes is permanently lost and cannot be restored.

Analytics apps now provide granular deletion lifecycle visibility and recovery
capabilities. Apps deleted after their first 45 minutes of life enter a soft-delete
state with a 14-day recovery window, while apps deleted within the first 45 minutes
are hard-deleted immediately.

### New deletion lifecycle events \{#225-deletion-events}

The [Apps event API](https://qlik.dev/apis/event/apps/) now publishes three deletion-related events,
enabling you to track app deletion state, automate recovery workflows, and audit
hard-deletions for compliance.

- `com.qlik.app.deleted`: An existing event, published when an app deletion is
  initiated. The event now includes a `deleteType` field indicating whether
  deletion is `SOFT` (recoverable) or `HARD` (permanent).
- `com.qlik.app.softdeleted`: Published when an app enters the recovery window.
  Includes the `purgeAt` date after which permanent deletion can occur.
- `com.qlik.app.harddeleted`: Published when an app is permanently deleted and can
  no longer be recovered.

### New app recovery REST endpoint \{#225-restore-endpoint}

The [Apps REST API](https://qlik.dev/apis/rest/apps/) now includes a restore endpoint for recovering
soft-deleted apps:

- `POST /api/analytics/apps/{appId}/actions/restore`: Restores a soft-deleted app to its state at
  the point of deletion. Available to tenant administrators and app owners (if the
  original space exists and they retain delete permission).

### Recovery workflow \{#225-recovery-workflow}

Use the deletion events to determine app state and the restore endpoint to recover
apps within the 14-day window. For a full walkthrough including event queries and
recovery examples, see
[Restore a deleted analytics app](https://qlik.dev/manage/analytics-applications/restore-deleted-app).
