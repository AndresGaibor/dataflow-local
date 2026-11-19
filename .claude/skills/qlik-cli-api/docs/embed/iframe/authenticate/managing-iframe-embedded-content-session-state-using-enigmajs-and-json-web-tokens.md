---
source: https://qlik.dev/embed/iframe/authenticate/managing-iframe-embedded-content-session-state-using-enigmajs-and-json-web-tokens/
last_updated: 2026-06-29T09:07:47+02:00
---

# Manage iframe Embedded Content Session State using enigma.js and JSON web tokens

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
session state when using JSON web tokens (JWTs) for authorization to Qlik Cloud.

> **Note:** This tutorial contains sample code using JWTs for authorization.
> If you are using OpenID Connect (OIDC), refer to the [Manage iframe-embedded content session state using enigma.js tutorial](https://qlik.dev/embed/iframe/authenticate/managing-iframe-session-with-enigma).

## Context

- You are embedding Qlik content using iframes and need to display custom
  modals, add private labels to dialogs, or control messages when a user's
  session disconnects.
- You've embedded Qlik content into a portal and you want to keep the portal open for
  the duration of the user's session.

Monitoring iframe content from Qlik uses [enigma.js](https://qlik.dev/toolkits/enigma-js),
a JavaScript library with access to Qlik Sense session state information.

## Prerequisites

This code example uses JWTs to authorize users to Qlik Cloud.
Ensure you have [configured a JWT identity provider](https://qlik.dev/authenticate/jwt/create-signed-tokens-for-jwt-authorization)
before proceeding. This article illustrates how to configure a
JWT identity provider on Qlik Cloud and it includes sample code for generating
a JWT. In addition, the example code in this tutorial utilizes backend code
to ensure secure generation and signing of the token. You may choose to generate
JWTs using a language a tech stack you prefer. The preceding referenced guide is
written in NodeJS, and there is another example using Python to generate JSON
web tokens.

> **Note:** The backend code configured to generate the JWT uses a REST endpoint to
>
> `GET` request and return a JWT with a response payload like this:

> `{"body":{"<token>"}}`.

To use the example page in this tutorial, ensure you also have the following:

- An existing application ID and sheet ID to embed.
- A [web
  integration](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm)
  configured which contains the location of the web page that will be embedding
  the Qlik Cloud application.
- A [content security
  policy](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-content-security-policy.htm)
  entry with the `frame-ancestors` directive added for the location of the web
  page that will be embedding the Qlik Cloud application.
- A method of generating and fetching the JWT from your backend.

## Variable substitution and vocabulary

Throughout this tutorial, variables will be used to communicate value placement.
The variable substitution format is `<VARIABLE_NAME>`. Here is a list of
variables that appear in the sample code.

| Variable               | Description                                                                               |
| ---------------------- | ----------------------------------------------------------------------------------------- |
| `<TENANT>`             | The domain for the tenant you are accessing. Equivalent to `tenant.region.qlikcloud.com`. |
| `<JWT_ENDPOINT>`       | RESTful endpoint to retrieve JWT.                                                         |
| `<WEB_INTEGRATION_ID>` | The unique identifier of the web integration.                                             |
| `<APP_ID>`             | The unique identifier of the application.                                                 |
| `<SHEET_ID>`           | The unique identifier of the sheet.                                                       |
| `<IDENTITY>`           | An arbitrary string to establish a separate session state.                                |

> **Note:** The `IDENTITY` [parameter](https://qlik.dev/apis/javascript/single-integration/) can be
> used across iframes or other methods of embedding to tie and/or separate sessions accordingly.

> It is an optional parameter included in this example for illustrative purposes.

## Pseudocode

The code in this sample does the following:

1. Handles logging into Qlik.
2. Fetches the CSRF token so that a WebSocket connection can be made to the
   engine.
3. Connects to the application leveraging enigma.js.
4. Establishes listeners on the WebSocket session `closed` and `suspended` and
   events.
5. Fetches the active theme of the application to style the embedded
   visualization consistently across user interfaces.
6. Renders the iframe.
7. A timer is set to automatically close the engine WebSocket session in 10
   seconds.
8. The Engine WebSocket session is closed, which triggers the listener on the
   `closed` event, illustrating the catch.
9. The iframe is hidden and a custom message is displayed.

## Sample code

The code example in this tutorial provides a basic, fully functional web page
after successfully logging in to Qlik Cloud with JWT. It showcases a few capabilities
in one example, providing a boilerplate you can modify. Here are some of the features:

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

        const TENANT = '<TENANT>';
        const JWTENDPOINT = '<JWT_ENDPOINT>';
        const WEBINTEGRATIONID = '<WEB_INTEGRATION_ID>';
        const APPID = '<APP_ID>';
        const SHEETID = '<SHEET_ID>';
        const IDENTITY = '<IDENTITY>';

        //    MAIN

        (async function main() {
            const isLoggedIn = await qlikLogin();
            const qcsHeaders = await getQCSHeaders();
            const [session, enigmaApp] = await connectEnigma(qcsHeaders, APPID, IDENTITY);
            handleDisconnect(session);
            const theme = await getTheme(enigmaApp);
            renderSingleIframe('qlik_frame', APPID, SHEETID, theme, IDENTITY);
            const message = 'Session will be automatically closed in 10 seconds to showcase the handling.';
            document.getElementById('message').innerHTML = message;
            setTimeout(() => { // remove this after testing
                session.close();
            }, "10000")
        })();

        //    LOGIN

        async function qlikLogin() {
            const loggedIn = await checkLoggedIn();
            if (loggedIn.status !== 200) {
                const tokenRes = await (await getJWTToken(JWTENDPOINT)).json();
                const loginRes = await jwtLogin(tokenRes.body);
                if (loginRes.status != 200) {
                    const message = 'Something went wrong while logging in.';
                    alert(message);
                    throw new Error(message);
                }
                const recheckLoggedIn = await checkLoggedIn();
                if (recheckLoggedIn.status !== 200) {
                    const message = 'Third-party cookies are not enabled in your browser settings and/or browser mode.';
                    alert(message);
                    throw new Error(message);
                }
            }
            console.log('Logged in!');
            return true;
        }

        async function checkLoggedIn() {
            return await fetch(`https://${TENANT}/api/v1/users/me`, {
                mode: 'cors',
                credentials: 'include',
                headers: {
                    'qlik-web-integration-id': WEBINTEGRATIONID
                },
            })
        }

        //    Get the JWT and use it to obtain Qlik Cloud session cookie.

        async function getJWTToken(jwtEndpoint) {
            return await fetch(jwtEndpoint, {
                mode: 'cors',
                method: 'GET'
            })
        }

        async function jwtLogin(token) {
            const authHeader = `Bearer ${token}`;
            return await fetch(`https://${TENANT}/login/jwt-session?qlik-web-integration-id=${WEBINTEGRATIONID}`, {
                credentials: 'include',
                mode: 'cors',
                method: 'POST',
                headers: {
                    'Authorization': authHeader,
                    'qlik-web-integration-id': WEBINTEGRATIONID
                },
            })
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
            const [session, app] = await getEnigmaSessionAndApp(qcsHeaders, appId, identity);
            return [session, app];
        }

        async function getEnigmaSessionAndApp(headers, appId, identity) {
            const params = Object.keys(headers)
                .map((key) => `${key}=${headers[key]}`)
                .join('&');

            return (async () => {
                const schema = await (await fetch('https://unpkg.com/enigma.js@2.7.0/schemas/12.612.0.json')).json();

                try {
                    return await createEnigmaAppSession(schema, appId, identity, params);
                }
                catch {
                    // Handle race condition with new users who do not have permissions to access the application. The code makes another attempt after a 1.5 seconds.
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
                document.getElementById('message').innerHTML = message;
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
            document.getElementById(frameId).setAttribute('src', frameUrl);
        }


    </script>

</body>

</html>
```
