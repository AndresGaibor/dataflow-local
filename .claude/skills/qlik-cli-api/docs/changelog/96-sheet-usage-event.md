---
source: https://qlik.dev/changelog/96-sheet-usage-event/
last_updated: 2025-07-08T16:09:30Z
---

# Qlik Sense sheet usage event added to audit

Qlik has added the `com.qlik.v1.analytics.analytics-app-client.sheet-view.opened`
event to the audit service in Qlik Cloud. This event is triggered whenever a sheet is
displayed in Qlik Sense, allowing for detailed analysis of how many times a sheet
in an app has been viewed and by which user.

The audit entry structure is as follows:

```json

{
  "id": "auditEntryId",
  "data": {
    "appId": "appId",
    "sheetId": "sheetId",
    "sheetState": "analysis|edit|simpleEdit"
  },
  "eventId": "eventId",
  "eventTime": "2024-05-01T01:13:16.000Z",
  "eventType": "com.qlik.v1.analytics.analytics-app-client.sheet-view.opened",
  "source": "com.qlik/analytics",
  "tenantId": "tenantId",
  "userId": "userId"
}
```

A view will be recorded each time the sheet is navigated to by users
accessing via the Qlik Sense client, via iFrame, or via the `classic/app`
interface with qlik-embed. Events are not generated for any other embedding approaches.
Actions such as toggling between edit and view mode without changing sheet will
not register as additional views of the sheet.

The value of `sheetState` details the consumption mode active when the user
opened the sheet:

- `analysis` when in view only mode.
- `simpleEdit` when in [edit mode](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/navigating-sheets.htm).
- `edit` when in the [advanced options edit mode](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/navigating-sheets.htm#anchor-4).

This event is available via the [Audits API](https://qlik.dev/apis/rest/audits/) and
can also be viewed in the Events section of the Management Console.
