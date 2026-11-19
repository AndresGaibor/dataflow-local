---
source: https://qlik.dev/embed/iframe/authenticate/third-party-cookie-handling-with-embedded-content/
last_updated: 2025-07-08T16:09:30Z
---

# Third-party cookie handling with embedded content

> **Use qlik-embed for new integrations:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
>
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.
>
> Third-party cookie handling is not required when using [qlik-embed with OAuth](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/).

Contributed by Daniel Pilla

## Overview

> **Note:** This tutorial provides sample code that uses OpenID Connect [OIDC](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/OIDC-intro.htm)
> for authentication.
> If you are using JWT authorization, refer to [Manage iframe Embedded Content Session State using enigma.js and JSON web tokens](https://qlik.dev/embed/iframe/authenticate/managing-iframe-embedded-content-session-state-using-enigmajs-and-json-web-tokens).

In this tutorial, you are going to learn how to configure your Qlik embedded
project to handle scenarios where your client's browser does not support
third-party cookies. Given that a Qlik Cloud tenant resides at
`*.*.qlikcloud.com`, and your web page will not reside on that same domain (for
example it might reside at `analytics.company.com`), this means that inherently,
any embedded content from Qlik Cloud must handle third-party cookies, as Qlik
Cloud relies on cookies for authentication.

Some browsers, by default, block third-party cookies. Furthermore, select
browser modes (such as Chrome's Incognito mode) and certain browser
configurations also turn off support for third-party cookies. This sample code
handles whether the user's browser supports third-party cookies,
which enables you to display a message (for example a nice modal) that the
user will either have to modify their browser settings or try another browser to
view the embedded Qlik content. Without this, the accessing user may perceive
Qlik to be malfunctioning, as the embedded content will not render.

If you're not familiar with third-party cookies, [here's a great blog to learn
more](https://cookie-script.com/all-you-need-to-know-about-third-party-cookies.html).

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

> **Note:** The `IDENTITY` [parameter](https://qlik.dev/apis/javascript/single-integration/) can be used across iframes or other
> methods of embedding to tie and/or separate sessions accordingly.
> It is an optional parameter included in this example for illustrative purposes.

## Sample code

The code example in this tutorial provides a basic, fully functional web page
that places an iframe into a div after successfully logging in to Qlik Cloud.
It showcases how to implement a custom message to alert the user if
their browser does not support third-party cookies. Be sure to test your final
customized message code in third-party cookie supported and unsupported modes to
ensure the message appears when you expect it.

```html
<html>

<body>
    <iframe id='qlik_frame' style='border:none;width:100%;height:800px;'></iframe>
    <script>
        const TENANT = '<tenant>.<region>.qlikcloud.com';
        const WEBINTEGRATIONID = '<web-integration-id>';
        const APPID = '<app-id>';
        const SHEETID = '<sheet-id>';
        const IDENTITY = '<identity>';

        (async function main() {
            const initQlikLogin = await qlikLogin();
            if (qlikLogin) {
                const frameSrc = `https://${TENANT}/single/?appid=${APPID}&sheet=${SHEETID}&identity=${IDENTITY}&opt=ctxmenu,currsel`;
                document.getElementById('qlik_frame').setAttribute('src', frameSrc);
            }

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
                        alert(message); // replace alert with modal or otherwise
                        throw new Error(message);
                    }
                }
                sessionStorage.removeItem('tryQlikAuth');
                console.log('Logged in!');
                return true;
            }
        })()
    </script>
</body>

</html>
```
