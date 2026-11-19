---
source: https://qlik.dev/embed/nebula/quickstart/build-a-simple-single-page-app/
last_updated: 2025-07-08T16:09:30Z
---

# Add visualizations to a single page application

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) rather than this framework.\
> For more information, see the [embedding Qlik Analytics using qlik-embed web components tutorial](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-webcomponent-quickstart).

This tutorial goes through all the steps necessary for you to create a simple
OAuth single page application from scratch that'll integrate with your Qlik
Cloud tenant. You'll learn about concepts such as:

- How to use [Public OAuth Clients (Redirect URL and CORS/domain allowlisting)](https://qlik.dev/authenticate/oauth/create/create-oauth-client).
- How to set up WebSockets towards the Qlik Associative Engine.
- How to do REST calls (headers, query parameters, and more).

> **Note:** You need access to a Qlik Cloud Analytics tenant, and either tenant administrator rights yourself, or the means to get
> a Single Page App (SPA) OAuth client.

## Requirements

This tutorial requires you to have the following things accessible:

- [Node.js](https://nodejs.org/en/download) (version 18 or newer)
- A terminal (for example [Git Bash on Windows](https://gitforwindows.org/),
  or Terminal.app on Mac).
- A modern web browser, for example, Google Chrome.
- A text editor or IDE of your choice, for example, Visual Studio Code.
- An existing [Single Page App (SPA) OAuth](https://qlik.dev/authenticate/oauth/create/create-oauth-client),
  or possibility to get one created in your tenant.

## Bootstrapping the project

You will work with HTML, JavaScript, and the [enigma.js](https://qlik.dev/toolkits/enigma-js) library, which simplifies communication
with the Qlik Associative Engine through WebSockets.

But before you can start writing any code, you need to prepare the project.
There are three steps:

- Create or retrieve a SPA OAuth client from your tenant.
- Create the necessary project (folders and files) structure.
- Start a local web server.

### Create SPA Public OAuth client

To allow third-party domains to communicate with your tenant, you need to
set up an [SPA Public OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client).
This process requires tenant administrator privileges.

You will need to add the app URL in the allowed list of redirect URLs
and origins. For this tutorial, the URL `http://localhost:8000` will be used
for the SPA app.

Once you've created the OAuth client, you should have everything
you need to start communicating with your tenant in your SPA app.

In the next section, you will create the project structure.

### Project structure

First of all, start your preferred terminal and create the project folder.

```bash
# move to a folder where you want to store the project:
cd ~

# new folder to contain the project files:
mkdir simple-spa
```

Next you will create the HTML index page and an app JavaScript file that
serves as the basis for the logic needed to communicate with your tenant.

Create an `index.html` file in the project folder with the following HTML
template.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Qlik Sense Single Page App</title>
  </head>
  <body>
  </body>
</html>
```

In the `head` tag, you will import the following Qlik JavaScript files
and the your `app.js`.

```html
<script type="module" src="https://unpkg.com/@qlik/sdk"></script>
<script src="https://unpkg.com/enigma.js"></script>
<script src="https://unpkg.com/@nebula.js/stardust"></script>
<script src="https://unpkg.com/@nebula.js/sn-pie-chart"></script>
<script type="module" src="/app.js"></script>
```

And define the following style for the page in the `head` tag.

```html
<style>
  #login {
    display: none;
  }
  .object {
    float: left;
    display: inline-block;
    height: 400px;
    width: 50%;
  }
  #loading {
    font-size: 40px;
    display: none;
  }
</style>
```

Finally, you will render a login button and a placeholder for a pie chart
visualization.

```html
<h1>Welcome to Qlik Nebula Demo</h1>
<h2>This demo is running with an OAuth public client and using WebSockets</h2>
<div id="login">
  You are not logged in.
  <button id="login_button">login with Qlik</button>
</div>

<div id="loading">Loading...</div>
<div class="toolbar"></div>

{/* a pie object will be rendered here */}
<div id="pie" class="object"></div>
```

Next, create the `app.js` file. with the following contents.

First, you will import Qlik SDK and define the OAuth client
configuration.

```javascript
import { Auth, AuthType } from "https://unpkg.com/@qlik/sdk";

const config = {
  authType: AuthType.OAuth2,
  host: "https://your-tenant.us.qlikcloud.com",
  clientId: "<clientId>",
  redirectUri: window.location.origin,
  scopes: ["user_default"]
};
```

Next, the script will verify if the user is authorized and if not
the user will be redirected to complete the login.

```javascript
(async () => {
  const auth = new Auth(config);
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get("code");
  if (code) {
    await auth.authorize(window.location.href); // exchanges the credentials for a token
    window.history.pushState({}, "", "/");
    await renderPieChart(auth);
  } else if (!(await auth.isAuthorized())) { {
    const { url } = await auth.generateAuthorizationUrl();
    window.location = url;
  }
})();
```

If the user is authorized, the script will render a pie chart using random data.

> **Note:** The user must have `Private Analytics Content Creator` role to create visualizations.

```javascript
async function renderPieChart(auth) {

  const script = `
    TempTable:
    Load
    RecNo() as Field1,
    Rand() as Field2,
    Rand() as Field3
    AutoGenerate 5
  `;
  const schema = await (await fetch('https://unpkg.com/enigma.js/schemas/12.936.0.json')).json();
  const randomId = Math.random().toString(32).substring(3);
  const appId = `SessionApp_${randomId}`;
  // WebSocket url for Enigma.js
  const wsUrl = await auth.generateWebsocketUrl(appId);
  const session = enigma.create({
    schema,
    createSocket: () => new WebSocket(wsUrl),
  });

  // opens the app
  const app = await (await session.open()).getActiveDoc();
  await app.setScript(script);
  await app.doReload();

  // create renderer
  const renderer = window.stardust.embed(app, {
    context: { theme: "light" },
    types: [
      {
        name: 'pie-chart',
        load: () => Promise.resolve(window['sn-pie-chart']),
      }
    ]
  });

  // renders toolbar
  (await renderer.selections()).mount(document.querySelector('.toolbar'));

  // renders a pie chart
  renderer.render({
    type: 'pie-chart',
    element: document.querySelector('#pie'),
    fields: ['Field1', 'Field2', '=Sum(Field3)'],
    properties: {
      title: 'Nebula Pie Chart example',
    },
  });
}
```

Next up, you will learn how to Make REST calls to your tenants SaaS environment.

### Making REST Calls

The following example shows a REST call to the `/users/me` endpoint.

```javascript
const response = await (await auth.rest('/users/me')).json();
console.log(response);
```

Next up, you will learn how to start the HTTP web server needed for communication
with your tenant.

### Starting the web server

To serve your web app locally, you'll need an HTTP web server. The web integration
that you'll set up later requires HTTPS, which means that you can't just open
up your web app files using the `file://` protocol.

Open up your terminal and enter the following commands. Ignore typing the lines
starting with `#` as they're just comments for each command. The `npx` command comes
as part of your npm installation and allows you to execute command-line tools available
on npm without having to install them globally.

```bash
# move to the folder created during the `Project structure` section:
cd ~/simple-spa

# start the HTTP server on port 8000
npx simple-server 8000
```

If these commands run successfully, you should now have an HTTP web server running
that you can test in your browser.

## Summary

This tutorial hopefully taught you how to create a basic single page app from
scratch that communicates with your tenant, and all the steps needed to
configure a SPA Public OAuth client, HTTP requests, and WebSockets.
