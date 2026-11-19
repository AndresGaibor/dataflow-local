---
source: https://qlik.dev/embed/reports/qlik-api-export-data/
last_updated: 2025-12-08T16:58:54+01:00
---

# Export data from an embedded chart

## Introduction

This tutorial shows you how to use qlik-api to export data from a chart embedded in a web application with qlik-embed
web components.

## What you'll learn

In this tutorial, you'll learn how to:

- Embed a Qlik chart using `qlik-embed` web components
- Set up OAuth2 authentication for secure access
- Export chart data to Excel using qlik-api
- Implement asynchronous report generation and polling
- Handle file downloads in the browser

## Prerequisites

To complete this tutorial, you need the following:

- HTML and JavaScript experience
- A Qlik Cloud tenant
- A Qlik Analytics app
- A Qlik Analytics app ID and object ID to export data
- An [OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-spa)
  configured in your Qlik Cloud tenant
- A web server to host your application

## Step 1: Set up the embedded chart

### Configure the qlik-embed connection script

When you use `qlik-embed`, you need a host configuration (`hostConfig`) to load
the library and connect it to your Qlik Cloud tenant.

Add the host configuration as a child of the `head` element in your web page.

```html
<script
  crossorigin="anonymous"
  type="application/javascript"
  src="https://cdn.jsdelivr.net/npm/@qlik/embed-web-components@1/dist/index.min.js"
  data-host="https://<tenant>.<region>.qlikcloud.com"
  data-client-id="<clientId>"
  data-redirect-uri="https://your-web-application.example.com/oauth-callback.html"
  data-access-token-storage="session"
></script>
```

> **Note:** This tutorial uses an OAuth2 SPA host configuration which requires an OAuth callback page.
> For more ways to connect qlik-embed to your tenant, see [Connect qlik-embed](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed).

### Add the qlik-embed element

In the HTML body of your web application, add a `qlik-embed` element with an
`analytics/chart` ui.

```html
<qlik-embed
  id="visualization"
  ui="analytics/chart"
  app-id="a51a902d-76a9-4c53-85d2-066b44240146"
  object-id="ZxDKp"
  disable-cell-padding="true"
></qlik-embed>
```

1. Replace the app ID `a51a902d-76a9-4c53-85d2-066b44240146` with your actual app ID in the `app-id` property.
2. Replace the object ID `ZxDKp` with your actual chart object ID in the `object-id` property.

### Add the export button

Add the export button to the HTML page. Also, add a loader `div` element
to show a loading icon when the data export is generating.

```html
<div>
  <button id="exportData">Export data</button>
</div>
<div id="loader" class="loader" style="display:none;"></div>
```

## Step 2: Set up the export logic

Exporting data from an embedded chart uses qlik-api, the companion library to qlik-embed.
qlik-api provides TypeScript interfaces to Qlik Cloud's REST APIs and the Qlik Analytics Engine (also called `qix`).

Add a script element to your web application and set the type to module.

```html
<script type="module">
  //Add javascript here...
</script>
```

### Import libraries

Add the `auth`, `reports`, and `tempContents` modules from qlik-api using the
`import` command.

The `fileSaver` library assists with downloading the export file to your computer or
device.

```javascript
import { auth, reports, tempContents } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.min.js";
import fileSaver from 'https://cdn.jsdelivr.net/npm/file-saver@2.0.5/+esm'
```

### Configure the qlik-api connection

When you use qlik-embed and qlik-api together, they can share the same
authenticated session. However, you must set the host configuration for
qlik-api to connect to your Qlik Cloud tenant.

Using the `auth.setDefaultHostConfig` method, configure the qlik-api connection.
The parameters to use are similar to those found in the qlik-embed script with
slightly different syntax.

```javascript
auth.setDefaultHostConfig({
  host: "<tenant>.<region>.qlikcloud.com",
  authType: "Oauth2",
  clientId: "<clientId>",
  redirectUri: "https://your-web-application.example.com/oauth-callback.html",
  accessTokenStorage: "session",
  autoRedirect: true,
});
```

### Get reference to your qlik-embed object

When you add a `qlik-embed` object to a web application, you can obtain
access to the source analytics application's composition and data model.

Access the object from the DOM using the `getElementById` method. Once you have
a reference to the object, you can access the `qlik-embed` API reference.

```javascript
const vizEl = document.getElementById("visualization");
const appId = vizEl.getAttribute("app-id");
const refApi = await vizEl.getRefApi();
```

The `refApi` variable represents a connection to the analytics session. You can
now make a `getDoc` call to access the complete analytics application model,
or make a `getObject` call to access the genericObject defining the embedded
visualization.

Create references to both the `doc` and the object. Then, create a reference to the
layout of the object:

```javascript
const doc = await refApi.getDoc();
const theObject = await refApi.getObject();
const objLayout = await theObject.getLayout();
```

## Step 3: Create and submit the export request

### Create temporary bookmark

Temporary bookmarks make it easier to send the current selection state of the
analytics application to the reporting services API. The reporting API generates
the requested output based upon the temporary bookmark.

Create the temporary bookmark using the `doc` object, supplying the chart object
ID from the object layout.

```javascript
const tempB = await doc.createTemporaryBookmark(
  {
    qOptions: {
      qIncludeAllPatches: true,
      qIncludeVariables: true,
      qSaveVariableExpressions: true
    },
    qObjectIdsToPatch: [ 
      objLayout.qInfo.qId
    ]
  }
);
```

The function will return the ID for the bookmark so it can be supplied to the
data extract request.

### Build the request payload

Create the report payload object using values from the previous steps:

> **Note:** The code uses the following variables from earlier steps:
>
> - `appId`: The Qlik Analytics application ID to specify the object source.
> - `id`: The ID of the object present in the object layout variable.
> - `temporaryBookmarkV2.id`: The temporary bookmark ID obtained in the [Create temporary bookmark](#create-temporary-bookmark) section.

```javascript
const reportPayload = {
  type: "sense-data-1.0",
  meta: {
    exportDeadline:"P0Y0M0DT0H8M0S",
    tags:["qlik-embed-download"]
  },
  senseDataTemplate: {
    appId: appId,
    id: objLayout.qInfo.qId,
    selectionType: "temporaryBookmarkV2",
    temporaryBookmarkV2: {
      id: tempB
    }
  },
  output: {
    outputId: "Chart_excel",
    type:"xlsx"}
}
```

For all available payload properties, see the ["Queue a new report request generation" endpoint documentation](https://qlik.dev/apis/rest/reports/#post-api-v1-reports).

### Submit and monitor the request using helper functions

When a user makes a report request, the export process is asynchronous and requires polling.
In the example code for this tutorial, the helper functions manage the report request lifecycle:

- `showLoader`: Makes visible the DOM element with `id="loader"`.
- `hideLoader`: Makes hidden the DOM element with `id="loader"`.
- `extractReportId`: Obtains the report request ID from the report status URL.
- `waitUntil`: Evaluates the report request status on an interval, stopping when
  the report generation completes.
- `getDownloadId`: Obtains the data extract output ID so the file can be
  downloaded.
- `createFileName`: Formats the name of the downloadable file to guarantee uniqueness.

> **Note:** These helper functions are part of this example to help provide an
> end-to-end experience. They are not required to execute a report request or
> download the resulting file.

### Handle the download

Use a try-catch code block to perform the report request. Inside the try block,
add a `reports.createReport` call including the report payload from the [Build the request payload](#build-the-request-payload) section.

Obtain the status URL to monitor the reporting task from the `content-location`
header returned from the `createReport` call. Then get the report ID from the
status URL.

Use the `waitUntil` function to monitor the report request using the report ID.
When the report generation completes, get the download ID.

The download ID is the reference to the downloadable file's temporary storage
location.

Use the `tempContents.downloadTempFile` function with the download ID to retrieve the
file. Use the `fileSaver.saveAs` function to open the browser's save dialog.

```javascript
try {
      showLoader();
      const reportReq = await reports.createReport(reportPayload);
      let statusURL = reportReq.headers.get("content-location");
      const reportId = extractReportId(statusURL);
      if (!reportId) {
        throw new Error("Invalid report ID");
      }
      // Set interval to check status every 5 seconds
      const wait = await waitUntil(reportId);
      const downloadId = getDownloadId(wait.location);
      let dle = await tempContents.downloadTempFile(downloadId, {inline: 1});
      hideLoader();
      fileSaver.saveAs(dle.data, `${createFileName(wait.filename)}.xlsx`);
    } catch (err) {
        console.log(err);
    }
```

## Step 4: Connect the button to export

Now that you have the export logic in place, you need to trigger it when users click the button.
Add this event listener to the same module script from [Step 2](#step-2-set-up-the-export-logic):

```javascript
document.getElementById("exportData").addEventListener("click", async function() {
    exportData(doc, objLayout);
  });  
```

When users click the export button, the flow is:

1. Event listener triggers `exportData()`
2. A temporary bookmark captures the current selection state
3. Report request is submitted to the API
4. Loader appears while the report generates
5. Status is polled every 5 seconds
6. When complete, the file is downloaded and loader disappears

## Putting it all together

Combine all code from Steps 2-4 into a single `<script type="module">` block in your HTML file in the following order:

1. [Imports](#import-libraries)
2. [Configuration](#configure-the-qlik-api-connection)
3. [Export request logic](#step-3-create-and-submit-the-export-request)
4. [Helper functions](#submit-and-monitor-the-request-using-helper-functions)
5. [Event listener](#step-4-connect-the-button-to-export)

The [Full code](#full-code) section includes a complete working example with all pieces assembled.

## Full code

<details>
  <summary>
    ### qlik-embed HTML and export button
  </summary>

  ```html
    <div id="analytics-chart" class="container">
      <div class="sub-container">
        <div>
          <button id="exportData">Export data</button>
        </div>
        <div id="loader" class="loader" style="display:none;"></div>
      </div>
      <div class="sub-container">
        <div class="viz">
          <qlik-embed
            id="visualization"
            ui="analytics/chart"
            app-id="<app-id>"
            object-id="<object-id>"
            disable-cell-padding="true"
          ></qlik-embed>
        </div>
      </div>
    </div>
  ```
</details>

<details>
  <summary>
    ### exportData function
  </summary>

  ```html
    <script type="module">
    import { auth, reports, tempContents } from "https://cdn.jsdelivr.net/npm/@qlik/api@2/index.min.js";
    import fileSaver from 'https://cdn.jsdelivr.net/npm/file-saver@2.0.5/+esm'

    const vizEl = document.getElementById("visualization");
    const appId = vizEl.getAttribute("app-id");
    const refApi = await vizEl.getRefApi();
    const doc = await refApi.getDoc();
    const theObject = await refApi.getObject();
    const objLayout = await theObject.getLayout();

    auth.setDefaultHostConfig({
      host: "<tenant>.<region>.qlikcloud.com",
      authType: "Oauth2",
      clientId: "<clientId>",
      redirectUri: "https://your-web-application.example.com/oauth-callback.html",
      accessTokenStorage: "session",
      autoRedirect: true,
    });

    document.getElementById("exportData")
      .addEventListener("click", async function() {
        exportData(doc, objLayout);
      });
    
    async function exportData(doc, objLayout) {
      
      const tempB = await doc.createTemporaryBookmark(
        {
          qOptions: {
            qIncludeAllPatches: true,
            qIncludeVariables: true,
            qSaveVariableExpressions: true
          },
          qObjectIdsToPatch: [ 
            objLayout.qInfo.qId
          ]
        }
      );

      const reportPayload = {
        type: "sense-data-1.0",
        meta: {
          exportDeadline:"P0Y0M0DT0H8M0S",
          tags:["qlik-embed-download"]
        },
        senseDataTemplate: {
          appId: appId,
          id: objLayout.qInfo.qId,
          selectionType: "temporaryBookmarkV2",
          temporaryBookmarkV2: {
            id: tempB
          }
        },
        output: {
          outputId: "Chart_excel",
          type:"xlsx"}
      }
      
      try {
        showLoader();
        const reportReq = await reports.createReport(reportPayload);
        let statusURL = reportReq.headers.get("content-location");
        const reportId = extractReportId(statusURL);
        if (!reportId) {
          throw new Error("Invalid report ID");
        }
        // Set interval to check status every 5 seconds
        const wait = await waitUntil(reportId);
        const downloadId = getDownloadId(wait.location);
        let dle = await tempContents.downloadTempFile(downloadId, {inline: 1});
        hideLoader();
        fileSaver.saveAs(dle.data, `${createFileName(wait.filename)}.xlsx`);       
      } catch (err) {
          console.log(err);
      }
    }

    function showLoader() {
      document.getElementById("loader").style.display = "block";
    }

    function hideLoader() {
      document.getElementById("loader").style.display = "none";
    }
    // Function to create a filename
    function createFileName(additionalInfo) {
      const currentDateTime = new Date().toISOString();
      return `${additionalInfo}-${currentDateTime}`;
    }

    async function waitUntil(reportId) {
      return await new Promise(resolve => {
        const interval = setInterval(() => {
          return reports.getReportStatus(reportId).
            then((status) => {
              console.log(status);
              console.log(`Current status: ${status.data.status}`);
              if (status.data.status === "done") {
                console.log(status);
                let result = { 
                  location: status.data.results[0].location,
                  filename: status.data.results[0].outputId,
                };
                clearInterval(interval);
                resolve(result);
                
              };
            });
          
        }, 5000);
      });
    }
    
    function extractReportId(url) {
      const regex = /reports\/(.*?)\/status/;
      const match = url.match(regex);
      if (match && match[1]) {
        return match[1];
      }
      return null;
    }

    function getDownloadId(url) {
      // Define a regular expression to match the last part of the path
      const regex = /\/([^\/?#]+)(?:[?#]|$)/;

      // Execute the regular expression on the URL
      const matches = url.match(regex);
      // Return the matched string, or null if no match is found
      return matches ? matches[1] : null;
    }

  </script>
  ```
</details>

<details>
  <summary>
    ### Supporting CSS for HTML
  </summary>

  ```css
  .viz {
    height: 600px;
    width: 100%;
    padding: 16px;
    border: 1px solid #bbb;
    border-radius: 3px;
    box-shadow: 1px 1px 10px rgba(0, 0, 0, 0.2);
    position:relative;
  }

  .container {
    padding: 8px;
    gap: 8px;
    position: relative;
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    margin-top: 50px;
    padding-top: 50px;
  }

  .sub-container {
    display: flex;
    flex: 1 0 auto;
    flex-direction: row;
    align-content: stretch;
    gap: 10px;
  }

  .loader {
    border: 4px solid #a9a9a9; /* Light grey */
    border-top: 4px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 16px;
    height: 16px;
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  ```
</details>
