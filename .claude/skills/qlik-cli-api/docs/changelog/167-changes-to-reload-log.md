---
source: https://qlik.dev/changelog/167-changes-to-reload-log/
last_updated: 2026-01-28T10:46:46Z
---

# The reload log payload is changing

> **Note:** Updated on January 28, 2026: Changed the target release date to February 4, 2026.
>
> Updated on December 15, 2025: Changed the target release date to January 28, 2026.
>
> Updated on November 7, 2025: Changed the target release date to December 15, 2025 from November 4, 2025.

The payload returned from the
[`/api/v1/reloads/{reloadId}` endpoint](https://qlik.dev/apis/rest/reloads/#get-api-v1-reloads-reloadId)
will change **on or after February 4, 2026**.
The existing `log` attribute will now provide a **summarized reload outcome**
instead of a partial script progress listing.

This change makes it easier to interpret reload success, failure, and row counts
directly from the API response, without parsing verbose log excerpts.
Full detailed logs remain available for download once the reload completes.

## Log script changes

### Current (successful reload)

```text
ReloadID: 68540644ea9e47432cff0827
Started loading data
(A detailed script progress log can be downloaded when the reload is finished)
Characters << AUTOGENERATE(26) 26 Lines fetched
ASCII << AUTOGENERATE(255) 191 Lines fetched

Transactions << AUTOGENERATE(1000) 1,996 Lines fetched

App saved Finished successfully
```

### Future (successful reload)

This is the proposed format and may change slightly prior to release.

```text
ReloadID: 68540644ea9e47432cff0827
Reload finished successfully
In total 13456 rows read from sources.
In total 5000 rows stored.
```

### Current (failed reload)

```text
ReloadID: 6866892543db4e9ecdaca12a
Started loading data
(A detailed script progress log can be downloaded when the reload is finished)
The following error occurred:
Connection not found: DataFiles2 (connection not found)
The engine error code: Connector error:11024
The error occurred here:
LOAD
AId,
AConstant,
ADate
FROM [lib://DataFiles2/T1.qvd]
(qvd)
```

### New (failed reload)

This is the proposed format and may change slightly prior to release.

```text
ReloadID: 6866892543db4e9ecdaca12a
Reload finished with error
The following error(s) occurred:
Connection not found
The error occurred at line 45
```

## Additional updates

- **History**: The last 100 script logs are now retained (`MaxInAppScriptLogs`
  configuration).
- **Incomplete reloads**: If the engine crashes, logs will be recovered once the
  engine restarts, ensuring better visibility of failed reloads.

This update provides clearer, more actionable reload information while reducing
noise in the `log` output.
