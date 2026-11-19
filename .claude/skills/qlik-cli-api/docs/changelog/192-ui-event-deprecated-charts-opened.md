---
source: https://qlik.dev/changelog/192-ui-event-deprecated-charts-opened/
last_updated: 2025-12-17T15:19:38Z
---

# New UI event - Deprecated Charts Opened

A new UI event, Deprecated Charts Opened, is now available.

This event is triggered by the client (browser) when deprecated chart types are detected.
It's emitted when a user opens or navigates to a sheet in the native Qlik experience or when using qlik-embed with the
`classic/app` UI.

The event is not emitted when switching between sheet modes (such as View to Edit) or in non-sheet UIs
(like Stories or Reporting).

Use this event to identify which apps and sheets contain deprecated charts that need to be updated.

The event payload includes:

- `appId`: The identifier of the app related to this event
- `charts`: A list of deprecated charts, each containing:
  - `chartId`: The identifier of the chart
  - `chartType`: The type of the chart
  - `chartTitle`: The title of the chart
  - `inContainer`: Whether the chart is inside a container
- `ownerId`: The ID of the user currently owning the related resource
- `sheetApproved`: Whether the sheet has been approved
- `sheetId`: The identifier of the sheet
- `sheetPublished`: Whether the sheet has been published
- `sheetTitle`: The evaluated sheet title expression, or the sheet title

<details>

<summary>Example event payload</summary>

```json
{
  "id": "693a9c567f0ffe1ca7079a38",
  "contentType": "application/json",
  "data": {
    "appId": "8571ee64-1d04-4c48-83ab-4e9d521b1082",
    "charts": [
      {
        "chartId": "ce271b14-f827-4e1a-a70f-a693119af715",
        "chartTitle": "",
        "chartType": "qlik-multi-kpi",
        "inContainer": true
      }
    ],
    "clientTimeStamp": "2025-12-11T10:26:30.237Z",
    "ownerId": "637390ef6541614d3a88d6c3",
    "sheetApproved": true,
    "sheetId": "cb5f7caa-59a0-4e0f-9722-48c6bb5de6be",
    "sheetPublished": true,
    "sheetTitle": "Current Month Forecast",
    "timestamp": "2025-12-11T10:26:30.237Z"
  },
  "eventId": "3b61a51f-735d-4357-85cc-8cbfdd13e650",
  "eventTime": "2025-12-11T10:26:30Z",
  "eventType": "com.qlik.v1.analytics.analytics-app-client.deprecated-charts.opened",
  "extensions": {
    "actor": {},
    "updates": []
  },
  "source": "com.qlik/analytics",
  "tenantId": "BL4tTJ4S7xrHTcq0zQxQrJ5qB1_Q6cSo",
  "userId": "637390ef6541614d3a88d6c3",
  "sessionId": "CiaT1A8MbMTp8/4CZXQuvoNosqKVGm+oGEKVTgTT1ao=",
  "links": {
    "self": {
      "href": "https://orchestration.eu.qlikcloud.com/api/v1/audits?eventType=com.qlik.v1.analytics.analytics-app-client.deprecated-charts.opened"
    }
  }
}
```
</details>

For more information, refer to the [reference documentation](https://qlik.dev/apis/ui-event/analytics/#com-qlik-v1-analytics-analytics-app-client-deprecated-charts-opened).

For a list of the deprecated objects that are detected with the event, see [Find deprecated charts](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/find-deprecated-charts.htm)
on Qlik Help.
