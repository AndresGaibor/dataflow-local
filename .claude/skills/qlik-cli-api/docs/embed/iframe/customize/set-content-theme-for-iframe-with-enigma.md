---
source: https://qlik.dev/embed/iframe/customize/set-content-theme-for-iframe-with-enigma/
last_updated: 2026-03-18T16:49:43Z
---

# Set the theme for embedded iframe content with enigma.js

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> To do something similar with qlik-embed, refer
> to [qlik-embed UIs and parameters](https://qlik.dev/embed/qlik-embed/parameters/),
> in particular the `classic/app` UI.

Contributed by Daniel Pilla

## Overview

In this tutorial, you are going to learn how to fetch the current theme of a
Qlik Sense application using [enigma.js](https://qlik.dev/toolkits/enigma-js) so it can be applied to embedded content dynamically.

## Prerequisites

To use this example page, ensure you have the following:

- An existing Qlik Sense application ID and sheet ID to embed.
- A [web integration
  id](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
  to prevent cross-site request attacks.
- A [content security
  policy](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)
  entry with the `frame-ancestors` directive added for the location of the web
  page that will be embedding the content.

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

> **Note:** The `IDENTITY` [parameter](https://qlik.dev/apis/javascript/single-integration/) can be used across iframes or other methods of
> embedding to tie and/or separate sessions accordingly.
> It is an optional parameter included in this example for illustrative purposes.

## Pseudocode

The code in this sample does the following:

1. Handles logging into Qlik.
2. Fetches the CSRF token so that a WebSocket connection can be made to the
   engine.
3. Connects to the application leveraging enigma.js.
4. Fetches the active theme of the application (this is purely bonus code
   showing the power of the engine).
5. Renders the iframe.

## Sample code

The code example in this tutorial provides a basic, fully functional web page.
It showcases a few capabilities in one example, providing a boilerplate you can modify.
Here are some of the features:

- Catches session events, such as, displaying a custom modal dialog or redirecting
  to another web page.

Handles browser support for third-party cookies. For more information, see
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
        const SHEETID = '<SHEET_ID>';
        const IDENTITY = '<IDENTITY>';

        //    MAIN

        (async function main() {
            const isLoggedIn = await qlikLogin();
            const qcsHeaders = await getQCSHeaders();
            const [session, enigmaApp] = await connectEnigma(qcsHeaders, APPID, IDENTITY);
            const theme = await getTheme(enigmaApp);
            renderSingleIframe('qlik_frame', APPID, SHEETID, theme, IDENTITY);
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

        //    DYNAMICALLY FETCH THE THEME

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

        //    HELPER FUNCTION TO GENERATE IFRAME

        function renderSingleIframe(frameId, appId, sheetId, theme, identity) {
            const frameUrl = `https://${TENANT}/single/?appid=${appId}&sheet=${sheetId}&theme=${theme}&identity=${identity}&opt=ctxmenu,currsel`;
            document.getElementById(frameId).setAttribute('src', frameUrl);
        }


    </script>

</body>

</html>
```
