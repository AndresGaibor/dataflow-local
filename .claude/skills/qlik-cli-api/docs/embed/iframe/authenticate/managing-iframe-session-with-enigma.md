---
source: https://qlik.dev/embed/iframe/authenticate/managing-iframe-session-with-enigma/
last_updated: 2026-03-18T16:49:43Z
---

# Manage iframe-embedded content session state using enigma.js

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> A similar concept can be leveraged with [supported auth providers](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/)
> in qlik-embed if needed.

Contributed by Daniel Pilla

## Overview

In this tutorial, you are going to learn how to embed an iframe and monitor its
session state with Qlik.

## Context

- You are embedding Qlik content using iframes and need to display custom
  modals, add private labels to dialogs, or control messages when a user's
  session disconnects.
- You've embedded Qlik into a portal and you want to keep the portal open for
  the duration of the user's session.

Monitoring iframe content from Qlik uses [enigma.js](https://qlik.dev/toolkits/enigma-js), a JavaScript library with access to
Qlik Sense session state information.

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
4. Establishes listeners on the WebSocket session `closed` and `suspended`
   events.
5. Fetches the active theme of the application (this is purely bonus code
   showing the power of the engine).
6. Renders the iframe.
7. A timer is set to automatically close the engine WebSocket session in 10
   seconds.
8. The engine WebSocket session is closed, triggering the listener receive the
   `closed` event and illustrating the catch.
9. The iframe is hidden and a custom message is displayed.

## Sample code

The code example in this tutorial provides a basic, fully functional web page. It
showcases a few capabilities in one example, providing a boilerplate you can modify.
Here are some of the features:

- Automatically hides the iframe and displays a message inline.

- Catches session events, such as, displaying a custom modal dialog or redirecting
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

        const TENANT = '<tenant>.<region>.qlikcloud.com';
        const WEBINTEGRATIONID = '<web-integration-id>';
        const APPID = '<app-id>';
        const SHEETID = '<sheet-id>';
        const IDENTITY = '<identity>';

        //    MAIN

        (async function main() {
            const isLoggedIn = await qlikLogin();
            const qcsHeaders = await getQCSHeaders();
            const [session, enigmaApp] = await connectEnigma(qcsHeaders, APPID, IDENTITY);
            handleDisconnect(session);
            const theme = await getTheme(enigmaApp);
            renderSingleIframe('qlik_frame', APPID, SHEETID, theme, IDENTITY);
            const message = 'Session will be automatically closed in 10 seconds to showcase the handling.';
            document.getElementById('message').innerHTML = message; // remove this after testing
            setTimeout(() => { // remove this after testing
                session.close();
            }, "10000")
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

        //    BONUS! DYNAMICALLY FETCH THEME

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

        //    HANDLE ENGINE SESSION CLOSURE

        function handleDisconnect(session) {
            session.on('closed', () => {
                const message = '<Your text here> Due to inactivity or loss of connection, this session has ended.';
                document.getElementById('qlik_frame').style.display = "none";
                document.getElementById('message').innerHTML = message; // replace with own handling
            });

            session.on('suspended', () => {
                const message = '<Your text here> Due to loss of connection, this session has been suspended.';
                document.getElementById('qlik_frame').style.display = "none";
                document.getElementById('message').innerHTML = message;
            });

            window.addEventListener('offline', () => {
                session.close();
            });
        }

        //    HELPER FUNCTION TO GENERATE IFRAME

        function renderSingleIframe(frameId, appId, sheetId, theme, identity) {
            const frameUrl = `https://${TENANT}/single/?appid=${appId}&sheet=${sheetId}&theme=${theme}&identity=${identity}&opt=ctxmenu,currsel`;
            document.getElementById(frameId).setAttribute('src', frameUrl); // replace with own handling
        }


    </script>

</body>

</html>
```
