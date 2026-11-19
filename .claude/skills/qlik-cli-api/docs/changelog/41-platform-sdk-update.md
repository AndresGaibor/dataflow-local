---
source: https://qlik.dev/changelog/41-platform-sdk-update/
last_updated: 2025-07-02T17:28:24+02:00
---

# Platform SDKs Update - May 2023

## v0.22.0: Sense Client Objects & Mixins

- feat: Sense Client Object Defaults support in the SDK

  Added support for [Sense Client Objects](https://qlik.dev/apis/javascript/sense-client-objects),
  users can now easily do operations like:

```ts
// fetch the list sheets
const sheetList = await app.getSheets();
// get individual sheet and do operation on it
const sheet =  await app.getSheet(sheetList[0].id);
await sheet.publish()
```

and more:

```ts
// fetch the list fields
const fieldList = await app.getFields();
// fetch fthe list of fields (including system fields)
const fieldList = await app.getFields({ qFieldListDef: { qShowSystem: true } });
// listen to current selections
const currentSelectionsObj = await app.getCurrentSelectionsObject();
await currentSelectionsObj.getLayout();
currentSelectionsObj.on('changed', () => {
  // selections have been toggled
});
// create masterObjects & publish
const createdMasterObject = await app.createMasterobject({ qMetaDef: { title, description } });
// configure app properties
await app.setAppProperties({sheetTitleBgColor: '#ffcf03', sheetTitleColor: '#ffcf03'});
// list bookmarks easily etc...
const bookmarkList = await app.getBookmarks();

```

- feat: enigma mixins are now enabled by default non raw rpc calls

```ts
// ex: to disable the bandwidth-reducing delta protocol you now need to set it to false
await app.open( { delta: false} );
```

## v0.21.1: Maintenance Release

- fix: Exclude nebula example from dep specs

  Excluding nebula example as it uses production non-approved dependencies: parcel and nebula/stardust

## v0.21.0: New Features and Bugfixes

- fix: Handle property number name

  Added leading underscore to property names starting with number
  This fixes the problem with groups blocking updating of specs

- fix: Throw engine message error
  Added a response error interceptor to throw a descriptive error message
  received from engine

- fix: Replaced Buffer to btoa in browser build

- chore: Refactor env_vars

- chore: Use `apiResponseInterceptor` and add nebula integration test

  added empty once function next to the on-listener function - this should be a proper once function
  set properties in the open function: id, handle, type, genericType
  use `apiResponseInterceptor` - to set properties on result
  throw error from `apiResponseInterceptor` similar to enigma, should this throw an enigma error?
  wrap constructor for loop in if-isArray because of a non array response - needs investigation
  add browser integration test for nebula app using cypress

- chore: Added once event listener
  Once event listeners are called only once on event and removed from listeners

```ts
hypercube.once('changed', () => {...});
```

- chore: Allow event listeners to be async

  Async functions can be added as event listeners

```ts
hypercube.on('changed', async () => {...});
```

- chore: Keep reserved keywords as class members (delete)

Language reserved words are modified only while using as formal parameters and
kept as it is in class members which allows parsing request body with reserved
words as keys to class object without losing any fields from request body
