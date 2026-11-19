---
source: https://qlik.dev/embed/nebula/customize/session-apps/first-session-app/
last_updated: 2026-10-26T15:10:16Z
---

# Making your first session app using enigma.js

> **Note:** Where possible, use [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

## Overview

In this tutorial, you are going to learn how to use session apps in Qlik Sense
SaaS. Are you new to the concept of session apps? Read more about [session apps](https://qlik.dev/apis/json-rpc/qix#session-apps)
before continuing.

If you're just interested in the code produced in this tutorial, skip to the
[Summary](#summary) section.

<details open>
  <summary>
    ## Requirements
  </summary>

  - An access token or API key. For more information, see [Authentication](/authenticate).
  - [Node.js](https://nodejs.org/en/download) (version 10 or newer)
  - A terminal (for example [Git Bash on Windows](https://gitforwindows.org/),
    or Terminal.app on Mac)
  - A text editor or IDE of your choice, for example, Visual Studio Code
</details>

<details>
  <summary>
    ## Define your load script
  </summary>

  <Aside type="note">
    Since session apps are created on the fly and require a data reload, they benefit from small data models.
    For an optimal experience, make sure your load script doesn't load too much data or the end-user experience may suffer.
  </Aside>

  If you already have a load script in mind, feel free to skip this section. Otherwise,
  here's one that doesn't require any external data source.

  `embed:./snippets/first-session-app/first-session-app.js#L12-16`
</details>

<details>
  <summary>
    ## Opening a session
  </summary>

  Move into a new empty folder in your terminal, and run `npm install enigma.js ws`.
  This installs the npm dependencies needed for this tutorial.

  After dependencies are installed, create a new file in the same folder using your
  IDE and call it `session-app.js`.

  In the file, start by loading the npm dependencies:

  `embed:./snippets/first-session-app/first-session-app.js#L1-4`

  <Aside type="note">
    In Qlik Cloud, the methods [CreateSessionApp](/apis/json-rpc/qix/global/#createsessionapp)
    and [CreateSessionAppFromApp](/apis/json-rpc/qix/global/#createsessionappfromapp)
    aren't used, instead the API is URL-based.
  </Aside>

  Next up is to make the WebSocket URL, which is an important
  step when working with session apps. The app ID needs to be prefixed
  with `SessionApp_`. It also needs to contain a unique identifier.

  Place and update these variables at the end of your file:

  `embed:./snippets/first-session-app/first-session-app.js#L5-17,44`

  <Aside type="note">
    The `(async () => {})();` piece is just so that you can use the `async`
    and `await` syntax directly inside the file without calling a function.
  </Aside>

  The script so far has imported all dependencies and defined all the
  variables you need to actually open a WebSocket connection and start
  working with the session app.

  The snippet below shows how to:

  - [open the session](/apis/javascript/enigma-js/#definitions-session-entries-open),
  - [get a reference to the app object](/apis/json-rpc/qix/global/#getactivedoc),
  - [set the load script](/apis/json-rpc/qix/doc/#setscript), and
  - [load data into the in-memory data model](/apis/json-rpc/qix/doc/#doreload).

  Add this at the end of your script, preceding the `})();` line:

  `embed:./snippets/first-session-app/first-session-app.js#L19-32,39-43`

  Great, you now have a session app all ready to evaluate expressions,
  build hypercubes, and much more. If you don't want to close the session, omit
  the last line. In this next code piece, you'll evaluate an expression just
  to verify that the data was loaded successfully.

  After the `app.doReload()` line, add this:

  `embed:./snippets/first-session-app/first-session-app.js#L33-38`

  If you haven't done so already, try running the complete script in your
  terminal:

  ```bash
  node session-app.js
  ```
</details>

<details open>
  <summary>
    ## Summary
  </summary>

  This is a short tutorial that shows you how to create a script using enigma.js
  to:

  - open a session app
  - set a load script and load data in-memory
  - evaluate a simple expression

  You can continue working on this script and do more complex things like using
  listobjects and hypercubes. You can find more examples to get you started in
  the [enigma.js git repository](https://github.com/qlik-oss/enigma.js/tree/master/examples/data).

  `session-app.js`

  `embed:./snippets/first-session-app/first-session-app.js`
</details>
