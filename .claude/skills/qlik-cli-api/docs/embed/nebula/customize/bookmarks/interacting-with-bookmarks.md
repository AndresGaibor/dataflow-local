---
source: https://qlik.dev/embed/nebula/customize/bookmarks/interacting-with-bookmarks/
last_updated: 2026-10-26T15:10:16Z
---

# Interact with bookmarks

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.
>
> To learn how to manage bookmarks using qlik-embed, refer to [Working with Qlik Sense bookmarks](https://qlik.dev/embed/qlik-embed/customize/qlik-embed-bookmark-interface)

> **Third-party cookies:** This tutorial leverages cookies for auth, which are blocked by some browser vendors.
> Please use an OAuth solution where possible, which doesn't leverage cookies.

In this tutorial, you are going to learn with sample code how to interact with
bookmarks through APIs using `enigma.js`, by building a simple bookmark
manager.

If you're just interested in the code produced in this tutorial, skip to the
[Summary](#summary) section.

## Prerequisites

General Qlik Sense knowledge about bookmarks and selections plus basic HTML
and JavaScript experience would be preferable.

What you need:

- [Node.js](https://nodejs.org/en/download) (version 12 or newer)
- A terminal (for example [Git Bash on Windows](https://gitforwindows.org/),
  or Terminal.app on Mac)
- A modern web browser, for example Google Chrome
- A text editor or IDE of your choice, for example Visual Studio Code
- An existing
  [web integration](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-adminster-web-integrations.htm),
  or possibility to get one created in your tenant

## Project structure and setup

For this project, you are going to use:

- [enigma.js](https://qlik.dev/toolkits/enigma-js) to communicate with the Qlik
  Associative Engine
- [parceljs](https://parceljs.org/) to start a development server and bundle the application
- [bootstrap](https://getbootstrap.com/docs/3.4/javascript/) as a CSS framework

With your preferred terminal, create the project folder, initialize with `npm init`,
and install the required dependencies:

```bash
# new folder to contain the project files:
mkdir bookmark-manager
cd bookmark-manager

# initialize the project without having it ask any questions
# this creates a `package.json` in the root of your directory
npm init -y

# install the required dependencies
npm i -S enigma.js
npm i -D parcel@next
```

In the `scripts` property of the newly generated `package.json` file, add a
new script entry allowing you to start a development server. Next, add a new property called
`browserlist` for `parceljs` to correctly set the browser configuration for the
app bundle (see [parceljs#browserlist](https://github.com/parcel-bundler/parcel#packagejsonbrowserslist)
for more details)

`embed:./snippets/interacting-with-bookmarks/package.json#L6-8,15-17`

- Create an `index.html` file using your favorite editor and save the file in
  the project folder.

`embed:./snippets/interacting-with-bookmarks/index.html`

> **Note:** In the HTML file, you have a `<table>` element that contains a predefined
> header (`<thead>` tag) for labeling the columns for the bookmark list.

Next, create the communication module required for client authentication
and for creating an `enigma.js` session.

- Create a new JavaScript file and call it `comm.js`. This file
  contains the necessary configuration and method helpers for doing
  requests against your tenant.

Add the configuration object:

`embed:./snippets/interacting-with-bookmarks/comm.js#L4-8`

Then add request helper method that has mode CORS, credentials set to true,
and `qlik-web-integration-id` configured in the headers.

`embed:./snippets/interacting-with-bookmarks/comm.js#L10-19`

Next, add a sign-in helper method that uses the previously created `request`
method for fetching the `/api/v1/users/me` endpoint. Note that the full `Users`.

`embed:./snippets/interacting-with-bookmarks/comm.js#L21-38`

> **Note:** For more information, see the [Users API reference](https://qlik.dev/apis/rest/users).

Finally, add the method that creates an enigma session, connects to your
tenant's WebSocket, and opens the app:

- import `enigma.js` and its schema at the beginning of the file
  `embed:./snippets/interacting-with-bookmarks/comm.js#L1-2`
- add the `getApp` method
  `embed:./snippets/interacting-with-bookmarks/comm.js#L40-56`
- expose `login` and `getApp` by adding at the end of the file:
  `embed:./snippets/interacting-with-bookmarks/comm.js#L58-61`

## Building the app

Now that the project structure is set up including all the required
dependencies, you can start building the bookmark manager.

### Ensure that the user is signed in and open the app

- Create the main JavaScript file and call it `app.js`. Add
  an asynchronous init function, and then invoke the function.

`embed:./snippets/interacting-with-bookmarks/app.js#L99,118-120`

- import `login` and `getApp` functions from the communication module by
  adding at the beginning of the file:

`embed:./snippets/interacting-with-bookmarks/app.js#L2`

- Add the sign in authentication redirect logic and open the app in
  the `init` function

`embed:./snippets/interacting-with-bookmarks/app.js#L99-103`

### Fetch your app's bookmarks

There are two ways of fetching bookmarks in the Qlik Associative Engine:

- By using the [GetBookmarks](https://qlik.dev/apis/json-rpc/qix/doc/#getbookmarks) method example:

```javascript
app.getBookmarks({
  qOptions: {
    qTypes: ["bookmark"],
    qData: {
      title: "/qMetaDef/title",
      description: "/qMetaDef/description",
      sheetId: "/sheetId",
      selectionFields: "/selectionFields",
      creationDate: "/creationDate",
    },
  },
});
```

- By creating a [GenericObject](https://qlik.dev/apis/json-rpc/qix/genericobject/)
  with the [CreateSessionObject](https://qlik.dev/apis/json-rpc/qix/doc/#createsessionobject):

```javascript
app.createSessionObject({
  qInfo: {
    qId: "BookmarkList",
    qType: "BookmarkList",
  },
  qBookmarkListDef: {
    qType: "bookmark",
    qData: {
      // dynamic data stored by the Qlik Sense client
      title: "/qMetaDef/title",
      description: "/qMetaDef/description",
      sheetId: "/sheetId",
      selectionFields: "/selectionFields",
      creationDate: "/creationDate",
    },
  },
});
```

In this use case, the advantage of using
the [Generic object model](https://qlik.dev/embed/foundational-knowledge/app-anatomy/generic-object-model) is that it allows binding to
certain events, and the event of interest here is `changed`.
The event is triggered by the Qlik Associative Engine when the state changes from valid to invalid,
allowing rendering updates in the front-end.

Both methods require sending a [BookmarkList definition](https://qlik.dev/apis/json-rpc/qix/schemas/#bookmarklistdef)
as a parameter and in Qlik Sense, bookmarks contain
an extra set of data that should be included in the definition (ex: `sheetId`,
`creationDate`, etc.) to retrieve them.

- Declare a constant called `bookmarkListProps` that contains the definition:

`embed:./snippets/interacting-with-bookmarks/app.js#L4-20`

- Create a session object with the previously declared `bookmarkListProps` definition,
  and bind an `update` function that triggers when the model gets invalidated.

`embed:./snippets/interacting-with-bookmarks/app.js#L105-107,109,113,115-117`

### Render the table

In the previous sections, you created a generic object containing the bookmark list
definition and the callback method `update` triggered by the `changed` event.

- In the `update` function, add:

`embed:./snippets/interacting-with-bookmarks/app.js#L109-113`

The [getLayout](https://qlik.dev/apis/json-rpc/qix/genericobject/#getlayout) method evaluates
an object and returns its properties, in this case, the bookmark list.

The returned layout from the `getLayout` method should be similar to below.

```json
{
  "qInfo": {},
  "qMeta": {
    "privileges": []
  },
  "qSelectionInfo": {},
  "qBookmarkList": {
    "qItems": []
  }
}
```

- Create a top level function called `renderTableContent`

`embed:./snippets/interacting-with-bookmarks/app.js#L22`

- In that function, get HTML element references for the `<table>` and `<tbody>`
  elements, create a new `<tbody>` element for replacing the old one, and then extract
  the data from the layout (for now, you only need the `qItems` array).

`embed:./snippets/interacting-with-bookmarks/app.js#L22-30`

- Now add a forEach loop that creates cells and fills them with the bookmark
  list data.

`embed:./snippets/interacting-with-bookmarks/app.js#L32-41`

> Note the added attribute called `bookmark-id` on row element `<tr>`
> containing the bookmarkId as value, the `<input>` element for the
> title value, and the `<textarea>` element for the description.
> These are later used to change the bookmark title and description,
> but more on this later.

#### Action buttons

- In the last cell, create buttons with actions for applying, cloning, removing,
  and publishing the bookmarks.

`embed:./snippets/interacting-with-bookmarks/app.js#L43-73`

- Finally, add the buttons to the cell and, after the forEach loop, replace the
  current body with the newly created one.

`embed:./snippets/interacting-with-bookmarks/app.js#L45-80,95-96`

Quick summary of the methods used:

- [ApplyBookmark](https://qlik.dev/apis/json-rpc/qix/doc/#applybookmark)
  (alternatively you can use [GenericBookmark Apply](https://qlik.dev/apis/json-rpc/qix/genericbookmark/#apply))
- [CloneBookmark](https://qlik.dev/apis/json-rpc/qix/doc/#clonebookmark) for duplicating a bookmark
- [DestroyBookmark](https://qlik.dev/apis/json-rpc/qix/doc/#destroybookmark) for removing a bookmark
- [GenericBookmark Publish](https://qlik.dev/apis/json-rpc/qix/genericbookmark/#publish) for
  publishing a bookmark

The `published` state used for "toggling" the publish button of the bookmark
can be found nested in the `qItem.qMeta` object.

#### Update the title and description of a bookmark

Do you remember the `<input>` and `<textarea>` elements added earlier to the title
and description cells? It's time to add `change` event listeners with logic that
updates the bookmark's titles and descriptions.

- Before `tableEl.replaceChild(tbody, oldTbody);`, add a query selector for all `<input>`
  and `<textarea>` elements. Then in a `forEach` loop, add the event listener `change`,
  which triggers each time the text changes.

`embed:./snippets/interacting-with-bookmarks/app.js#L80-82,93-96`

- Now you get the bookmark ID and model, by adding in the `addEventListener` callback:

`embed:./snippets/interacting-with-bookmarks/app.js#L82-86`

> **Note:** You can retrieve the `bookmarkId` stored in the `<tr bookmark-id="">` element as the `bookmark-id` attribute.

- You can update the bookmark properties with the
  [SetProperties](https://qlik.dev/apis/json-rpc/qix/genericbookmark/#setproperties) method,
  but since `setProperties` overwrites all the properties, you first need to fetch the bookmark properties with the
  [GetProperties](https://qlik.dev/apis/json-rpc/qix/genericbookmark/#getproperties) method.

The title and description are stored under `qMetaDef/title` and
`qMetaDef/description`, respectively and since you know that titles
use `input` element and descriptions uses `textarea`, you can use a
conditional ternary operator for setting the value:

`embed:./snippets/interacting-with-bookmarks/app.js#L87-92`

Save your files and give it a try by running the start script in your terminal:

```bash
npm start
```

## Summary

This tutorial hopefully taught you how to interact with bookmarks using `enigma.js`.

The following files have been created as part of this tutorial.

`index.html`

`embed:./snippets/interacting-with-bookmarks/index.html`

`comm.js`

`embed:./snippets/interacting-with-bookmarks/comm.js`

`app.js`

`embed:./snippets/interacting-with-bookmarks/app.js`

`package.json`

`embed:./snippets/interacting-with-bookmarks/package.json`
