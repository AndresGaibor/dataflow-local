---
source: https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-offline-snapshots/
last_updated: 2026-09-22T19:15:49Z
---

# Offline analytics snapshot embedding with qlik-embed

In this quick start, you'll:

- Retrieve a snapshot of a chart from a Qlik Sense app in JSON format.
- Embed it into an HTML page using qlik-embed and the `analytics/snapshot` UI.
- Render it with no authentication or connection to a Qlik Cloud tenant.

## Prerequisites

If you just want to try embedding a snapshot offline:

1. Copy the [sample snapshot JSON](#sample-snapshot-json) file provided at the end of this quick start.
2. Save it as `snapshot.json`.
3. Skip to [Create a simple HTML file to embed the snapshot](#create-an-html-file-to-embed-the-snapshot).

If you want to generate and embed your own snapshot JSON file, you need:

- Access to a Qlik Cloud tenant.
- A Qlik Sense app with a chart.
- A snapshot already created for that chart.
- [An access token](https://qlik.dev/authenticate/) to call the [Sharing tasks API](https://qlik.dev/apis/rest/sharing-tasks/).

If you need help creating a snapshot, see [Monitoring visualizations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Hub/monitor-charts-hub.htm).
When you start monitoring a visualization, a sharing task is created.
The sharing task generates snapshots at regular intervals.

## Retrieve the snapshot JSON

To embed a snapshot offline, you first need to export it from Qlik Cloud.
You'll use the Sharing tasks API to list your snapshots and download the JSON payload from the latest execution.

> **Before you begin:** [Monitor a visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Hub/monitor-charts-hub.htm)
> to create a snapshot of a chart in your Qlik Sense app.
> When you start monitoring, a sharing task is created and generates snapshots at regular intervals.

> **Monitoring charts are disabled after 90 days of inactivity:** If a monitoring chart is not viewed or accessed for 90 consecutive days, it is disabled and no longer
> updated. To keep your monitoring task active, ensure it is regularly accessed (viewed) at least once
> every 90 days. See [Keep monitoring charts active](#keep-monitoring-charts-active) for strategies to
> maintain active charts through automation.

1. List sharing tasks using the Sharing tasks API:
   ```bash
   curl -X GET "https://<QLIK_TENANT_URL>/api/v1/sharing-tasks" \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
   ```

The response contains an array of tasks.

<details>
  <summary>
    Example response
  </summary>

  ```json
  "sharingTasks": [
    {
      "appId": "178ebc50-db69-4dc8-98e5-8a52180c7377",
      "appName": "qlik-dev-exec-dashboard",
      "createdBy": "66cd95575011929d135e71ef",
      "dateCreated": "2025-09-09T10:17:13Z",
      "emailContent": null,
      "enabledBySystem": true,
      "enabledByUser": true,
      "executeOnCreation": true,
      "id": "68bffea8a928af5200418eb1",
      "insightDirectURL": "https://<QLIK_TENANT_URL>/share/45104064-a2a6-4996-91aa-0f3b0d455871",
      "insightFallbackURL": "https://<QLIK_TENANT_URL>/sense/app/178ebc50-db69-4dc8-98e5-8a52180c7377/sheet/PfKsJK/state/analysis/insight/95e3820f-d871-4b96-ae2b-7b966b085f97",
      "insightID": "95e3820f-d871-4b96-ae2b-7b966b085f97",
      "lastExecutionDate": "2025-09-09T10:17:23Z",
      "lastRun": "2025-09-09T10:17:23Z",
      "lastUpdated": "2025-09-09T10:17:42Z",
      "lastViewed": "2025-09-09T10:17:12Z",
      "multiInsightURLs": null,
      "name": "Revenue Trend",
      ...}
  ```
</details>

2. Look for the sharing task that matches your Qlik Sense app name (`appName`) and chart's `name`.
   Copy the sharing task `id`, you will use it in the next API call.

3. Fetch the snapshot JSON from the latest execution of the sharing task:
   Replace `<TASK_ID>` with the sharing task `id` you noted earlier:
   ```bash
   curl -X GET "https://<QLIK_TENANT_URL>/api/v1/sharing-tasks/<TASK_ID>/executions/latest/files/snapshot" \
     -H "Authorization: Bearer <ACCESS_TOKEN>"
   ```

The response contains the snapshot in JSON format.

4. Save the response to a file named `snapshot.json`.

## Create an HTML file to embed the snapshot

Now that you have the snapshot JSON file, you can build an HTML page that uses qlik-embed to render the snapshot offline
with `data-auth-type="noauth"`.

Using `data-auth-type="noauth"`, qlik-embed doesn't connect to your tenant.
Instead, it renders an offline snapshot JSON you provide.
This means that no authentication is needed, and no data is fetched from Qlik Cloud.

1. Open your text editor and create a new file named `index.html` in the same folder as your `snapshot.json` file.
2. Add the following HTML code to the file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Offline snapshot embedding with analytics/snapshot via qlik/embed-web-components</title>
    <!-- Load qlik-embed-web-components with no authentication -->
    <script
      crossorigin="anonymous"
      src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1.4.1/dist/index.min.js"
      data-auth-type="noauth"
    ></script>
    <style>
      #qlik-container {
        height: 420px;
      }
      qlik-embed {
        display: block;
        min-height: 380px;
      }
    </style>
  </head>
  <body>
    <h1>Offline snapshot embedding with analytics/snapshot via qlik/embed-web-components</h1>
    <div id="qlik-container"></div>

    <script type="application/javascript">
      window.addEventListener("DOMContentLoaded", async function () {
        const snapshotContainer = document.getElementById("qlik-container");
        snapshotContainer.innerHTML = "";

        try {
          // Load the snapshot JSON from the local file
          const r = await fetch("./snapshot.json", { cache: "no-store" });
          if (!r.ok) throw new Error(`HTTP ${r.status}`);
          const snapshotData = await r.json();

          // Create a <qlik-embed> element
          const snapshotEmbed = document.createElement("qlik-embed");
          snapshotEmbed.id = "snapshot";
          snapshotEmbed.setAttribute("ui", "analytics/snapshot");

          // 3. Attach the snapshot JSON payload
          snapshotEmbed.setAttribute("data___json", JSON.stringify(snapshotData));

          // 4. Add the <qlik-embed> element into the container
          snapshotContainer.appendChild(snapshotEmbed);
        } catch (err) {
          // If the snapshot.json cannot be loaded or parsed, show an error
          console.error("Failed to load snapshot.json:", err);
          snapshotContainer.textContent =
            "Could not load snapshot.json. Make sure index.html and snapshot.json are in the same folder and served over http://";
        }
      });
    </script>
  </body>
</html>

```

3. Save the `index.html` file.

## Run a local server

To view the `index.html` file in your browser, you need to serve it using a local web server.

1. Make sure both `index.html` and `snapshot.json` are in the same folder.
2. From the folder containing `index.html` and `snapshot.json`, start a local server.
   For example, using Node.js with `http-server`, run:
   ```bash
   npx http-server -p 8080
   ```
3. Open your web browser and navigate to `http://localhost:8080`.

You should see the chart snapshot rendered in the browser.

## Summary

- The `<script>` tag loads the `qlik-embed-web-components` bundle.
- With `data-auth-type="noauth"`, qlik-embed never calls Qlik APIs. It only renders the snapshot JSON provided.
- The snapshot JSON is loaded from the `snapshot.json` file in the same folder as the `index.html` file.
- `<qlik-embed ui="analytics/snapshot">` renders the chart based on that JSON.

## Keep monitoring charts active

Monitoring charts are disabled after 90 days of inactivity. To keep your charts continuously
refreshed with the latest data, use the `isViewChart` parameter when you fetch snapshots. This parameter updates the
`lastViewed` timestamp, resetting the inactivity timer.

### Using Qlik Automate or your tooling

Set up scheduled automation using [Qlik Automate](https://qlik.dev/toolkits/no-code/), cron jobs, cloud functions, or
other workflow tools to periodically fetch snapshots from your monitoring tasks.

**Example: Fetch the latest snapshot with the `isViewChart` parameter**

```bash
# Run this on a schedule (e.g., every 30 days)
curl -X GET "https://<QLIK_TENANT_URL>/api/v1/sharing-tasks/<TASK_ID>?isViewChart=true" \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

The `isViewChart=true` parameter updates the monitoring task's `lastViewed` property to the current time, which
determines whether the sharing task is still in use. This prevents the task from being disabled after 90 days.

### Recommended frequency

To be safe, schedule this API call at least once every 60 days. This leaves a 30-day buffer before the 90-day
expiration window.

## Next steps

- Experiment with different types of visualizations and snapshots in your Qlik Sense app.
- Customize the styling and layout of your HTML page to better fit your needs.
- Keep your monitoring charts active using automation: Use [Qlik Automate](https://qlik.dev/automate) or your
  preferred workflow tool (cron jobs, cloud functions, etc.) to schedule regular API calls with the `isViewChart=true`
  parameter. This resets the inactivity timer and prevents the 90-day expiration. See [Keep monitoring charts active](#keep-monitoring-charts-active)
  for implementation details.
- Follow the [Offline analytics snapshot embedding with qlik-embed and OAuth M2M](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-offline-snapshots-m2m-tutorial)
  to learn how to configure and run a web app that fetches snapshots from Qlik Cloud using OAuth M2M and displays them
  offline.

<details>
  <summary>
    ## Sample snapshot JSON
  </summary>

  ```json
  {
    "permissions": {
        "update": false,
        "publish": false,
        "export": false,
        "exportData": false,
        "changeOwner": false,
        "remove": false
    },
    "qInfo": {
        "qId": "Njbgg",
        "qType": "linechart"
    },
    "qMeta": {
        "privileges": [
            "read"
        ]
    },
    "qSelectionInfo": {},
    "qHyperCube": {
        "qSize": {
            "qcx": 2,
            "qcy": 12
        },
        "qDimensionInfo": [
            {
                "qFallbackTitle": "Month",
                "qApprMaxGlyphCount": 3,
                "qCardinal": 12,
                "qSortIndicator": "A",
                "qGroupFallbackTitles": [
                    "Month"
                ],
                "qGroupPos": 0,
                "qStateCounts": {
                    "qLocked": 0,
                    "qSelected": 0,
                    "qOption": 12,
                    "qDeselected": 0,
                    "qAlternative": 0,
                    "qExcluded": 0,
                    "qSelectedExcluded": 0,
                    "qLockedExcluded": 0
                },
                "qTags": [
                    "$numeric",
                    "$integer"
                ],
                "qDimensionType": "N",
                "qGrouping": "N",
                "qNumFormat": {
                    "qType": "U",
                    "qnDec": 0,
                    "qUseThou": 0
                },
                "qIsAutoFormat": true,
                "qGroupFieldDefs": [
                    "FiscalMonth"
                ],
                "qMin": 1,
                "qMax": 12,
                "qContinuousAxes": true,
                "qAttrExprInfo": [],
                "qAttrDimInfo": [],
                "qCardinalities": {
                    "qCardinal": 12,
                    "qHypercubeCardinal": 12,
                    "qAllValuesCardinal": -1
                },
                "qLibraryId": "dyCEjG",
                "qEffectiveDimensionName": "FiscalMonth",
                "title": "Month",
                "autoSort": true,
                "cId": "eMyDDxz",
                "othersLabel": "Others"
            }
        ],
        "qMeasureInfo": [
            {
                "qFallbackTitle": "Revenue",
                "qApprMaxGlyphCount": 10,
                "qCardinal": 0,
                "qSortIndicator": "D",
                "qNumFormat": {
                    "qType": "R",
                    "qnDec": 0,
                    "qUseThou": 0,
                    "qFmt": "##############",
                    "qDec": ".",
                    "qThou": ","
                },
                "qMin": 4746104.510000003,
                "qMax": 7150293.280000015,
                "qIsAutoFormat": true,
                "qAttrExprInfo": [],
                "qAttrDimInfo": [],
                "qLibraryId": "NPPsJt",
                "qTrendLines": [],
                "autoSort": true,
                "cId": "mcwb"
            }
        ],
        "qEffectiveInterColumnSortOrder": [
            0,
            1
        ],
        "qGrandTotalRow": [
            {
                "qText": "67119290.3",
                "qNum": 67119290.30000018,
                "qElemNumber": -1,
                "qState": "X",
                "qIsTotalCell": true
            }
        ],
        "qDataPages": [
            {
                "qMatrix": [
                    [
                        {
                            "qText": "Jan",
                            "qNum": 1,
                            "qElemNumber": 0,
                            "qState": "O"
                        },
                        {
                            "qText": "7042004.98",
                            "qNum": 7042004.979999991,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Feb",
                            "qNum": 2,
                            "qElemNumber": 1,
                            "qState": "O"
                        },
                        {
                            "qText": "5744335.85",
                            "qNum": 5744335.850000021,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Mar",
                            "qNum": 3,
                            "qElemNumber": 2,
                            "qState": "O"
                        },
                        {
                            "qText": "5601834.42",
                            "qNum": 5601834.420000011,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Apr",
                            "qNum": 4,
                            "qElemNumber": 3,
                            "qState": "O"
                        },
                        {
                            "qText": "7150293.28",
                            "qNum": 7150293.280000015,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "May",
                            "qNum": 5,
                            "qElemNumber": 4,
                            "qState": "O"
                        },
                        {
                            "qText": "6113696.6",
                            "qNum": 6113696.600000017,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Jun",
                            "qNum": 6,
                            "qElemNumber": 5,
                            "qState": "O"
                        },
                        {
                            "qText": "4882635.06",
                            "qNum": 4882635.059999999,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Jul",
                            "qNum": 7,
                            "qElemNumber": 6,
                            "qState": "O"
                        },
                        {
                            "qText": "4963275.18",
                            "qNum": 4963275.1799999885,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Aug",
                            "qNum": 8,
                            "qElemNumber": 7,
                            "qState": "O"
                        },
                        {
                            "qText": "4746104.51",
                            "qNum": 4746104.510000003,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Sep",
                            "qNum": 9,
                            "qElemNumber": 8,
                            "qState": "O"
                        },
                        {
                            "qText": "5453025.44",
                            "qNum": 5453025.439999999,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Oct",
                            "qNum": 10,
                            "qElemNumber": 9,
                            "qState": "O"
                        },
                        {
                            "qText": "4758358.02",
                            "qNum": 4758358.020000007,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Nov",
                            "qNum": 11,
                            "qElemNumber": 10,
                            "qState": "O"
                        },
                        {
                            "qText": "5252527.06",
                            "qNum": 5252527.060000019,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Dec",
                            "qNum": 12,
                            "qElemNumber": 11,
                            "qState": "O"
                        },
                        {
                            "qText": "5411199.9",
                            "qNum": 5411199.900000001,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ]
                ],
                "qTails": [
                    {
                        "qUp": 0,
                        "qDown": 0
                    }
                ],
                "qArea": {
                    "qLeft": 0,
                    "qTop": 0,
                    "qWidth": 2,
                    "qHeight": 12
                }
            }
        ],
        "qPivotDataPages": [],
        "qStackedDataPages": [],
        "qMode": "S",
        "qNoOfLeftDims": -1,
        "qTreeNodesOnDim": [],
        "qColumnOrder": []
    },
    "refLine": {
        "refLines": []
    },
    "showTitles": true,
    "title": "Revenue Trend",
    "subtitle": "",
    "footnote": "",
    "lineType": "line",
    "stackedArea": false,
    "separateStacking": true,
    "nullMode": "gap",
    "dataPoint": {
        "show": false,
        "showLabels": true
    },
    "gridLine": {
        "auto": true,
        "spacing": 2
    },
    "color": {
        "auto": true,
        "mode": "primary",
        "singleColor": "#4477aa",
        "persistent": false,
        "measureScheme": "sg",
        "reverseScheme": false,
        "dimensionScheme": "12"
    },
    "legend": {
        "show": false,
        "dock": "auto",
        "showTitle": true
    },
    "dimensionAxis": {
        "show": "labels",
        "label": "auto",
        "dock": "bottom"
    },
    "measureAxis": {
        "show": "labels",
        "label": "horizontal",
        "dock": "left",
        "spacing": 0.75,
        "autoMinMax": true,
        "minMax": "min",
        "min": 0,
        "max": 10
    },
    "visualization": "linechart",
    "snapshotData": {
        "object": {
            "size": {
                "w": 462,
                "h": 200,
                "boundingClientWidth": 461.8497314453125,
                "boundingClientHeight": 200.3115997314453
            }
        },
        "rtl": false,
        "appLocaleInfo": {
            "qDecimalSep": ".",
            "qThousandSep": ",",
            "qListSep": ",",
            "qMoneyDecimalSep": ".",
            "qMoneyThousandSep": ",",
            "qCurrentYear": 2011,
            "qMoneyFmt": "$#,##0.00;($#,##0.00)",
            "qTimeFmt": "h:mm:ss TT",
            "qDateFmt": "M/D/YYYY",
            "qTimestampFmt": "M/D/YYYY h:mm:ss[.fff] TT",
            "qCalendarStrings": {
                "qDayNames": [
                    "Mon",
                    "Tue",
                    "Wed",
                    "Thu",
                    "Fri",
                    "Sat",
                    "Sun"
                ],
                "qMonthNames": [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "Jun",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec"
                ],
                "qLongDayNames": [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday"
                ],
                "qLongMonthNames": [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]
            },
            "qFirstWeekDay": 0,
            "qReferenceDay": 0,
            "qFirstMonthOfYear": 0
        },
        "content": {
            "size": {
                "w": 461.8497314453125,
                "h": 170.6602325439453
            },
            "chartData": {
                "scrollOffset": {
                    "start": 0,
                    "end": 12
                }
            }
        },
        "parent": {
            "h": 202,
            "w": 462
        }
    },
    "reducedHyperCube": {
        "qDataPages": [
            {
                "qMatrix": [
                    [
                        {
                            "qText": "Jan",
                            "qNum": 1,
                            "qElemNumber": 0,
                            "qState": "O"
                        },
                        {
                            "qText": "7042004.98",
                            "qNum": 7042004.979999991,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Feb",
                            "qNum": 2,
                            "qElemNumber": 1,
                            "qState": "O"
                        },
                        {
                            "qText": "5744335.85",
                            "qNum": 5744335.850000021,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Mar",
                            "qNum": 3,
                            "qElemNumber": 2,
                            "qState": "O"
                        },
                        {
                            "qText": "5601834.42",
                            "qNum": 5601834.420000011,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Apr",
                            "qNum": 4,
                            "qElemNumber": 3,
                            "qState": "O"
                        },
                        {
                            "qText": "7150293.28",
                            "qNum": 7150293.280000015,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "May",
                            "qNum": 5,
                            "qElemNumber": 4,
                            "qState": "O"
                        },
                        {
                            "qText": "6113696.6",
                            "qNum": 6113696.600000017,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Jun",
                            "qNum": 6,
                            "qElemNumber": 5,
                            "qState": "O"
                        },
                        {
                            "qText": "4882635.06",
                            "qNum": 4882635.059999999,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Jul",
                            "qNum": 7,
                            "qElemNumber": 6,
                            "qState": "O"
                        },
                        {
                            "qText": "4963275.18",
                            "qNum": 4963275.1799999885,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Aug",
                            "qNum": 8,
                            "qElemNumber": 7,
                            "qState": "O"
                        },
                        {
                            "qText": "4746104.51",
                            "qNum": 4746104.510000003,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Sep",
                            "qNum": 9,
                            "qElemNumber": 8,
                            "qState": "O"
                        },
                        {
                            "qText": "5453025.44",
                            "qNum": 5453025.439999999,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Oct",
                            "qNum": 10,
                            "qElemNumber": 9,
                            "qState": "O"
                        },
                        {
                            "qText": "4758358.02",
                            "qNum": 4758358.020000007,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Nov",
                            "qNum": 11,
                            "qElemNumber": 10,
                            "qState": "O"
                        },
                        {
                            "qText": "5252527.06",
                            "qNum": 5252527.060000019,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ],
                    [
                        {
                            "qText": "Dec",
                            "qNum": 12,
                            "qElemNumber": 11,
                            "qState": "O"
                        },
                        {
                            "qText": "5411199.9",
                            "qNum": 5411199.900000001,
                            "qElemNumber": 0,
                            "qState": "L"
                        }
                    ]
                ],
                "qTails": [
                    {
                        "qUp": 0,
                        "qDown": 0
                    }
                ],
                "qArea": {
                    "qLeft": 0,
                    "qTop": 0,
                    "qWidth": 2,
                    "qHeight": 12
                }
            }
        ],
        "qDimensionInfo": [
            {
                "qFallbackTitle": "Month",
                "qApprMaxGlyphCount": 3,
                "qCardinal": 12,
                "qSortIndicator": "A",
                "qGroupFallbackTitles": [
                    "Month"
                ],
                "qGroupPos": 0,
                "qStateCounts": {
                    "qLocked": 0,
                    "qSelected": 0,
                    "qOption": 12,
                    "qDeselected": 0,
                    "qAlternative": 0,
                    "qExcluded": 0,
                    "qSelectedExcluded": 0,
                    "qLockedExcluded": 0
                },
                "qTags": [
                    "$numeric",
                    "$integer"
                ],
                "qDimensionType": "N",
                "qGrouping": "N",
                "qNumFormat": {
                    "qType": "U",
                    "qnDec": 0,
                    "qUseThou": 0
                },
                "qIsAutoFormat": true,
                "qGroupFieldDefs": [
                    "FiscalMonth"
                ],
                "qMin": 1,
                "qMax": 12,
                "qContinuousAxes": true,
                "qAttrExprInfo": [],
                "qAttrDimInfo": [],
                "qCardinalities": {
                    "qCardinal": 12,
                    "qHypercubeCardinal": 12,
                    "qAllValuesCardinal": -1
                },
                "qLibraryId": "dyCEjG",
                "qEffectiveDimensionName": "FiscalMonth",
                "title": "Month",
                "autoSort": true,
                "cId": "eMyDDxz",
                "othersLabel": "Others"
            }
        ],
        "qEffectiveInterColumnSortOrder": [
            1,
            0
        ],
        "qMeasureInfo": [
            {
                "qFallbackTitle": "Revenue",
                "qApprMaxGlyphCount": 10,
                "qCardinal": 0,
                "qSortIndicator": "D",
                "qNumFormat": {
                    "qType": "R",
                    "qnDec": 0,
                    "qUseThou": 0,
                    "qFmt": "##############",
                    "qDec": ".",
                    "qThou": ","
                },
                "qMin": 4746104.510000003,
                "qMax": 7150293.280000015,
                "qIsAutoFormat": true,
                "qAttrExprInfo": [],
                "qAttrDimInfo": [],
                "qLibraryId": "NPPsJt",
                "qTrendLines": [],
                "autoSort": true,
                "cId": "mcwb"
            }
        ],
        "qStackedDataPages": [],
        "qMode": "S",
        "qSize": {
            "qcx": 2,
            "qcy": 12
        },
        "qColumnOrder": []
    },
    "visualizationType": "linechart",
    "sourceObjectId": "GJxgd",
    "sheetId": "",
    "timestamp": 1757413043398,
    "isClone": false,
    "qMetaDef": {
        "title": "Revenue Trend"
    },
    "supportExport": true
  }
  ```
</details>
