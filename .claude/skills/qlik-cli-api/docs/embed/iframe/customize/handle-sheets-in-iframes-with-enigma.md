---
source: https://qlik.dev/embed/iframe/customize/handle-sheets-in-iframes-with-enigma/
last_updated: 2026-01-19T14:21:00Z
---

# Handle sheets in iframes with enigma.js

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> To do something similar with qlik-embed, refer
> to [embedding Qlik using qlik-embed web components](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart/)
> for the core web app, and add sheet retrieval based on [get sheets from an app](https://qlik.dev/embed/qlik-embed/examples/sheetlist-dropdown-example/).

Contributed by Daniel Pilla

## Overview

In this tutorial, you are going to learn how to dynamically embed a sheet within
an iframe, without having to hard code URLs and sheet IDs. This tutorial
uses [enigma.js](https://qlik.dev/toolkits/enigma-js) to dynamically fetch, categorize, and sort a list of all sheets within an
analytics application.
With enigma.js, you can create custom drop-downs, navigation controls, provide sheet
metadata type information, that is, whether the sheet is a "Base" or "Community"
sheet, and more. If you are only looking to embed a single sheet, or the number
of sheets is static and you are fine with hardcoding sheet IDs to buttons, then
this approach is not necessary, however, this is frequently not the case. There
are many scenarios where a custom UI is desired, but iframes are preferred due
to their ease of use and portability.

## Prerequisites

To use the example page in this tutorial, ensure that you have the following:

- An existing application ID to embed.
- A [web
  integration](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
  configured that contains the location of the web page that will be embedding
  the Qlik Cloud application.
- A [content security
  policy](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)
  entry with the `frame-ancestors` directive added for the location of the web
  page that will be embedding the Qlik Cloud application.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables that appear in the sample code.

| Variable               | Description                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `<TENANT>`             | The domain for the tenant you are accessing. Equivalent to `tenant.region.qlikcloud.com`. |
| `<WEB_INTEGRATION_ID>` | The unique identifier of the web integration.                                             |
| `<APP_ID>`             | The unique identifier of the application.                                                 |
| `<IDENTITY>`           | An arbitrary string to establish a separate session state.                                |

> **Note:** The `IDENTITY` [parameter](https://qlik.dev/apis/javascript/single-integration/) can be used across iframes or other methods of
> embedding to tie and/or separate sessions accordingly.
> It is an optional parameter included in this example for illustrative purposes.

## Pseudocode

The code example in this tutorial provides a basic, fully functional web page that executes
the following sequence:

1. Handles logging into Qlik.
2. Fetches the CSRF token so that a WebSocket connection can be made to the
   Engine.
3. Connects to the application using enigma.js.
4. Establishes listeners on the WebSocket session `closed` and `suspended`
   events.
5. Fetches the active theme of the application (this is purely bonus code
   showing the power of the Engine).
6. Fetches the space ID of the application.
7. Fetches the space type that the application resides in.
8. Gets a list of all sheets within the application.
9. Categorizes each sheet by type: Base, Community, or Private, and sorts
   them by their type and subsequently by their rank (order displayed in the
   client.)
10. The sheets are logged to the console.
11. The iframe is rendered with the first sorted sheet in the sorted array.

The intent here is that you take the sheets array and build it into any
type of navigation-oriented UI that you would like.

## Sheet type and sorting

This code sample includes an algorithm to categorize and sort sheets. The
matrices below document the criteria required for the categorization.

Applications in Managed Spaces:

|           | Published | Approved |
| --------- | --------- | -------- |
| Base      | True      | True     |
| Community | True      | False    |
| Private   | False     | False    |

Applications in Shared Spaces:

|         | Published | Approved |
| ------- | --------- | -------- |
| Base    | True      | False    |
| Private | False     | False    |

The sorting is determined by the sheet's `rank` property, which is sorted
secondary to its sheet type. The sheet type sorting in this sample code is first
sorted by Base, then Community, and finally Private.

Given this sample code's categorization and sorting, the output resembles the
following ordering (with the full sheet objects in JSON):

| SheetType | SheetName         |
| --------- | ----------------- |
| Base      | Base Sheet 1      |
| Base      | Base Sheet 2      |
| Community | Community Sheet 1 |
| Community | Community Sheet 2 |
| Private   | Private Sheet 1   |
| Private   | Private Sheet 2   |

There are two custom attributes that this sample code adds to each sheet's
JSON object. They are:

| Attribute     | Definition                                                                      |
| ------------- | ------------------------------------------------------------------------------- |
| sheetType     | "Base", "Community", or "Private"                                               |
| sheetTypeEnum | Integer representation, where 1 == "Base", 2 == "Community", and 3 == "Private" |

## Sample code

The sample code showcases a few capabilities in one example, providing a
boilerplate you can modify. Here are some of the features:

- Catch session events, such as displaying a custom modal dialog or redirecting
  to another web page.

- Handles browser support for third-party cookies. For more information, see
  [Third-party cookie handling with embedded content](https://qlik.dev/embed/iframe/authenticate/third-party-cookie-handling-with-embedded-content).

```html
  <html>

  <head>
      <script src="https://unpkg.com/enigma.js/enigma.min.js"></script>
  </head>

  <body>

      <div id="main">
          <div id="message"></div>
          <iframe id='qlik_frame' style='border:none;width:100%;height:900px;'></iframe>
      </div>

      <script>

          //    CONFIGURATION

          const TENANT = '<TENANT>';
          const WEBINTEGRATIONID = '<WEB_INTEGRATION_ID>';
          const APPID = '<APP_ID>';
          const IDENTITY = '<IDENTITY>';

          //    MAIN

          (async function main() {
              const isLoggedIn = await qlikLogin();
              const qcsHeaders = await getQCSHeaders();
              const [session, enigmaApp] = await connectEnigma(qcsHeaders, APPID, IDENTITY);
              handleDisconnect(session);
              const theme = await getTheme(enigmaApp);
              const spaceId = (await getApp(APPID)).spaceId;
              const spaceType = await getSpaceType(spaceId);
              const sheets = await getSheetList(enigmaApp, spaceType);
              console.log(sheets);
              renderSingleIframe('qlik_frame', APPID, sheets[0].qInfo.qId, theme, IDENTITY);
          })();

          //    LOGIN

          async function qlikLogin() {
              const loggedIn = await fetch(`https://${TENANT}/api/v1/users/me`, {
                  mode: 'cors',
                  credentials: 'include',
                  headers: {
                      'qlik-web-integration-id': WEBINTEGRATIONID,
                  },
              })
              if (loggedIn.status !== 200) {
                  if (sessionStorage.getItem('tryQlikAuth') === null) {
                      sessionStorage.setItem('tryQlikAuth', 1);
                      window.location = `https://${TENANT}/login?qlik-web-integration-id=${WEBINTEGRATIONID}&returnto=${location.href}`;
                      return await new Promise(resolve => setTimeout(resolve, 10000)); // prevents further code execution
                  } else {
                      sessionStorage.removeItem('tryQlikAuth');
                      const message = 'Third-party cookies are not enabled in your browser settings and/or browser mode.';
                      alert(message);
                      throw new Error(message);
                  }
              }
              sessionStorage.removeItem('tryQlikAuth');
              console.log('Logged in!');
              return true;
          }

          async function getQCSHeaders() {
              const response = await fetch(`https://${TENANT}/api/v1/csrf-token`, {
                  mode: 'cors',
                  credentials: 'include',
                  headers: {
                      'qlik-web-integration-id': WEBINTEGRATIONID
                  },
              })

              const csrfToken = new Map(response.headers).get('qlik-csrf-token');
              return {
                  'qlik-web-integration-id': WEBINTEGRATIONID,
                  'qlik-csrf-token': csrfToken,
              };
          }


          //    ENIGMA ENGINE CONNECTION

          async function connectEnigma(qcsHeaders, appId, identity) {
              const [session, app] = await getEnigmaSessionAndApp(appId, qcsHeaders, identity);
              return [session, app];
          }

          async function getEnigmaSessionAndApp(appId, headers, identity) {
              const params = Object.keys(headers)
                  .map((key) => `${key}=${headers[key]}`)
                  .join('&');

              return (async () => {
                  const schema = await (await fetch('https://unpkg.com/enigma.js@2.7.0/schemas/12.612.0.json')).json();

                  try {
                      return await createEnigmaAppSession(schema, appId, identity, params);
                  }
                  catch {
                      // If the socket is closed immediately following the connection this
                      // could be due to an edge-case race condition where the newly created
                      // user does not yet have access to the app due to access control propagation.
                      // This bit of code will make another attempt after a 1.5 seconds.
                      const waitSecond = await new Promise(resolve => setTimeout(resolve, 1500));
                      try {
                          return await createEnigmaAppSession(schema, appId, identity, params);
                      }
                      catch (e) {
                          throw new Error(e);
                      }
                  }
              })();
          }

          async function createEnigmaAppSession(schema, appId, identity, params) {
              const session = enigma.create({
                  schema,
                  url: `wss://${TENANT}/app/${appId}/identity/${identity}?${params}`
              });
              const enigmaGlobal = await session.open();
              const enigmaApp = await enigmaGlobal.openDoc(appId);
              return [session, enigmaApp];
          }

          //    HANDLE ENGINE SESSION CLOSURE

          function handleDisconnect(session) {
              session.on('closed', () => {
                  console.log('Due to inactivity or loss of connection, this session has ended.');
              });

              session.on('suspended', () => {
                  console.log('Due to loss of connection, this session has been suspended.');
              });

            window.addEventListener('offline', () => {
                session.close();
            });
          }

          //    GET QLIK APP (FOR SPACE ID)

          async function getApp(appId) {
              var url = new URL(`https://${TENANT}/api/v1/items?resourceType=app&resourceId=${appId}`);
              const response = await fetch(url, {
                  method: 'GET',
                  mode: 'cors',
                  credentials: 'include',
                  headers: {
                      'Content-Type': 'application/json',
                      'qlik-web-integration-id': WEBINTEGRATIONID,
                  },
              })
              responseJson = await response.json();
              return responseJson.data[0];
          }

          //    GET SPACE (FOR SPACE TYPE)

          async function getSpaceType(spaceId) {
              var url = new URL(`https://${TENANT}/api/v1/spaces/${spaceId}`);
              const response = await fetch(url, {
                  method: 'GET',
                  mode: 'cors',
                  credentials: 'include',
                  headers: {
                      'Content-Type': 'application/json',
                      'qlik-web-integration-id': WEBINTEGRATIONID,
                  },
              })
              responseJson = await response.json();
              return responseJson.type;
          }

          //    GET THEME
          async function getTheme(enigmaApp) {
              const createAppProps = await enigmaApp.createSessionObject({
                  qInfo: {
                      qId: "AppPropsList",
                      qType: "AppPropsList"
                  },
                  qAppObjectListDef: {
                      qType: "appprops",
                      qData: {
                          theme: "/theme"
                      }
                  }
              });
              const appProps = await enigmaApp.getObject('AppPropsList');
              const appPropsLayout = await appProps.getLayout();
              const theme = appPropsLayout.qAppObjectList.qItems[0].qData.theme;
              return theme;
          }

          //    GET SHEETS (WITH TYPE ADDED, E.G., BASE, COMMUNITY, PRIVATE)

          async function getSheetList(app, spaceType) {
              var sheets = await app.getObjects(
                  {
                      "qOptions": {
                          "qTypes": [
                              "sheet"
                          ],
                          "qIncludeSessionObjects": false,
                          "qData": {}
                      }
                  }
              )
              sheetsIncludingType = [];
              for await (const sheet of sheets) {
                  var pushSheet = true;
                  const sheetObject = await app.getObject(sheet.qInfo.qId);
                  const sheetLayout = await sheetObject.getLayout();
                  var isManaged = spaceType === 'managed';
                  var sheetTypeEnum = 1;
                  var approved = sheet.qMeta.approved;
                  var published = sheet.qMeta.published;
                  const sheetTypeEnums = {
                      1: "Base",
                      2: "Community",
                      3: "Private"
                  };
                  if (!approved && !published) {
                      sheetTypeEnum = 3;
                  }
                  else if (!approved && published) {
                      if (isManaged) {
                          sheetTypeEnum = 2;
                      }
                  }
                  const sheetTypeObject = {
                      "sheetType": sheetTypeEnums[sheetTypeEnum],
                      "sheetTypeEnum": sheetTypeEnum
                  };
                  const mergedObject = {
                      ...sheetLayout,
                      ...sheetTypeObject
                  };
                  sheetsIncludingType.push(mergedObject)
              }
              sheetsIncludingType.sort((a, b) => (a.sheetTypeEnum - b.sheetTypeEnum || a.rank - b.rank))
              return sheetsIncludingType;
          }

          //    HELPER FUNCTION TO GENERATE IFRAME

          function renderSingleIframe(frameId, appId, sheetId, theme, identity) {
              const frameUrl = `https://${TENANT}/single/?appid=${appId}&sheet=${sheetId}&theme=${theme}&identity=${identity}&opt=ctxmenu,currsel`;
              document.getElementById(frameId).setAttribute('src', frameUrl);
          }


      </script>

  </body>

  </html>
```
