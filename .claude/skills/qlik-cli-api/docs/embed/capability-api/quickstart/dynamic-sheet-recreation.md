---
source: https://qlik.dev/embed/capability-api/quickstart/dynamic-sheet-recreation/
last_updated: 2025-07-03T16:05:11+02:00
---

# Embed a Qlik Sense sheet using the Capability API

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> To do something similar with qlik-embed, refer
> to [qlik-embed web components](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-sheet).

Contributed by Daniel Pilla.

## Overview

In this tutorial, you are going to learn how to embed a sheet from a Qlik Sense
application using the Capability API instead of embedding the sheet using an
iframe. While an iframe is an easy mechanism for embedding content, there may be
circumstances related to security, responsive design, and more, where rendering
the sheet with JavaScript is a better fit.

A sheet in a Qlik Sense application is a container for one-to-many
visualizations, and the sheet's layout is accessible metadata in JSON that you
can read to recreate the sheet programmatically. The benefit of this approach is
that the layout of the sheet is created dynamically in the client and propagated
to your web application without using an iframe.

## Prerequisites

To use the example page in this tutorial, ensure that you have the following:

- An existing application ID and sheet ID to embed.
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
| `<SHEET_ID>`           | The unique identifier of the sheet.                                                       |
| `<IDENTITY>`           | An arbitrary string to establish a separate session state.                                |

> **Note:** The `<IDENTITY>` [parameter](https://qlik.dev/apis/javascript/single-integration/) can be used across iframes or
> other methods of embedding to tie and/or separate sessions accordingly.
> It is an optional parameter included in this example for illustrative purposes.

## Sequence

The code example in this tutorial provides a basic, fully functional web page that executes
the following sequence:

1. Handles logging into Qlik.
2. Loads the Capability API resources.
3. Connects to the application.
4. Gets the layout of the sheet.
5. Sets a target div with a CSS grid that matches the sheet's layout.
6. Iterates over each object within the sheet layout creating a div for each and
   setting it with the same grid position as in the layout. This process also
   sets the `id` of each div to the `objectId` of the Qlik object.
7. Iterates over each div and injects each Qlik object whose `objectId` matches
   the corresponding `id`.

## Sample code

The sample code uses jQuery to showcase sheet rendering with the Capability API,
however, it's not a required component for the solution. In addition, the following
code includes sample handling for lack of browser support for third-party
cookies.

```html
<html>

<head>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"
        integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4=" crossorigin="anonymous"></script>
</head>

<body>

    <div id="sheet" style="height:800px;">

    </div>

    <script>

        //    CONFIGURATION

        const TENANT = '<TENANT>';
        const WEBINTEGRATIONID = '<WEB_INTEGRATION_ID>;
        const APPID = '<APP_ID>';
        const SHEETID = '<SHEET_ID>';
        const IDENTITY = '<IDENTITY>';

        //    DEFAULT PLACEMENT CONFIGURATION

        const qlikDivSelector = '#sheet';
        const qlikObjectClass = 'qlikObject';

        //    MAIN

        (async function main() {
            const isLoggedIn = await qlikLogin();
            const loadedCapabilitiesAssets = await loadCapabilitiesAssets();
            const app = await doCapabilities(APPID, qlikDivSelector, qlikObjectClass);
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

        // CREATE GRID

        function createGrid(querySelector, columns, rows) {
            const gridContainer = document.querySelector(querySelector);
            gridContainer.style.display = 'grid';
            gridContainer.style.gridTemplateRows = `repeat(${rows}, minmax(0, 1fr)`;
            gridContainer.style.gridTemplateColumns = `repeat(${columns}, minmax(0, 1fr))`;

            return gridContainer;
        }

        // CONSTRUCT SHEET

        function constructSheet(sheetLayout, querySelector, addClass) {
            const gridContainer = createGrid(querySelector, sheetLayout.columns, sheetLayout.rows);
            (sheetLayout.cells).forEach(function (object) {
                const objectId = object.name;
                const colStart = object.col + 1;
                const rowStart = object.row + 1;
                const colSpan = object.colspan;
                const rowSpan = object.rowspan;
                const objectDiv = document.createElement('div');
                objectDiv.id = objectId;
                objectDiv.style["grid-column"] = `${colStart} / span ${colSpan}`;
                objectDiv.style["grid-row"] = `${rowStart} / span ${rowSpan}`;
                objectDiv.style.border = '2px solid #0000';
                objectDiv.style.margin = '5px';
                objectDiv.classList.add(addClass);
                gridContainer.appendChild(objectDiv);
            })
            return true;
        }

        // LOAD & RENDER CAPABILITIES


        async function loadCapabilitiesAssets() {
            const cssUrl = `https://${TENANT}/resources/autogenerated/qlik-styles.css`;
            const requireUrl = `https://${TENANT}/resources/assets/external/requirejs/require.js`;
            return $.when(
                $('head').append(`<link rel="stylesheet" type="text/css" href="${cssUrl}">`),
                $.getScript(requireUrl)
            );
        }

        async function doCapabilities(appId, qlikDivSelector, objectClass) {
            var config = {
                host: TENANT,
                prefix: "/",
                port: 443,
                isSecure: true,
                webIntegrationId: WEBINTEGRATIONID,
                identity: IDENTITY
            };

            require.config({
                config: {
                    text: { useXhr: function (url, protocol, hostname, port) { return true; } }
                },
                baseUrl: 'https://' + config.host + (config.port ? ':' + config.port : '') + config.prefix + 'resources',
                webIntegrationId: WEBINTEGRATIONID
            });

            requirejs(["js/qlik"], (qlik) => {
                const app = qlik.openApp(appId, config);
                const sheetObject = app.getObject(SHEETID)
                    .then((sheetObject) => {
                        const sheetLayout = sheetObject.getLayout()
                            .then((sheetLayout) => {
                                constructSheet(sheetLayout, qlikDivSelector, objectClass);
                                $(`.${objectClass}`).each(function () {
                                    var chartId = $(this).attr("id");
                                    app.getObject(this, chartId);
                                });
                            })
                    })
            })
        }


    </script>

</body>

</html>
```
