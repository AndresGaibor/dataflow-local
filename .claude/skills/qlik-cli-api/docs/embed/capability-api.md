---
source: https://qlik.dev/embed/capability-api/
last_updated: 2025-11-13T09:33:53Z
---

# Capability APIs

> **qlik-embed:** For new integrations, use [qlik-embed](https://qlik.dev/embed/qlik-embed/)
> to safeguard against third-party cookie blocking and unlock future features.
> This tutorial remains available for those with existing implementations,
> but upgrading to qlik-embed ensures a robust, forward-looking solution.

## Capability APIs

The [Capability APIs](https://qlik.dev/apis/javascript/capability) are a collection of JavaScript APIs
that allow you to embed Qlik Sense content into a web app or portal. With just a few lines of code, you
can create a visualization that leverages the Qlik Sense visualization library. You can even
interact with the engine to return data and metadata from an application.
For an overview and examples, see [Capability APIs](https://qlik.dev/embed/capability-api/).

### Prerequisites for using Capability API

- JavaScript
- AngularJS 1.8 (Long term support ended December 12, 2021)
- require.js

### Considerations

The Capability APIs use AngularJS and RequireJS, which are both global libraries
with the potential to interact with the rest of your web app. jQuery is also
loaded with the Capability APIs. This means if you use another version of jQuery
in your web app, it may be overwritten by the copy of jQuery loaded
by the Capability APIs. CSS must also be loaded to use the Capability APIs,
which has the potential to overwrite your own web app styles. These factors
should be considered before using the Capability APIs. If any of these potential
conflicts are an issue, consider using the App Integration API or Single
Integration API. Both of these APIs use iFrames to embed Qlik Sense content into
your page, isolating your web app from library version conflicts.
You could also consider creating a mashup with the Capability APIs and embedding
the mashup in your web app in an iFrame to isolate it from the rest of your web app.

Additionally, some visualizations require UTF-8 encoding to render correctly.
For troubleshooting and workarounds, see [UTF-8 character encoding requirement](https://qlik.dev/embed/foundational-knowledge/visualizations/#utf-8-character-encoding-requirement).

See Using AngularJS in your mashup for more information on integrating the
Capability APIs into an existing AngularJS project.

### Limitations

The following capability API methods are not supported when used with Qlik Cloud.

| Capability API     | Methods                                                                                  |
| ------------------ | ---------------------------------------------------------------------------------------- |
| Global API         | getAppList()getProductVersion()getQTProduct()isPersonalMode()                            |
| Root API           | callRepository()getAppList()getExtensionList()getGlobal()sessionApp()sessionAppFromApp() |
| QVisualization API | exportData()exportImg()exportPdf()                                                       |

### Use cases best suited for Capability APIs

- When you want to customize the Qlik experience to match your user interface.
- When you want to customize the layout of Qlik objects without the overhead of multiple iFrames.
- When you want to interact with Qlik directly, that is, without going through visualizations.
- When you want to access the Qlik Sense client without using the Qlik Sense UI, that is,
  the selection model.

## APIs for mashups

Qlik Sense comes with a number of Capability APIs that can
be used for building mashups. Once your mashup is set up, you will have access
to the `qlik` namespace. The `qlik` namespace provides all of the methods of the
Root API. From there, you can use the `openApp` method to connect to a Qlik Sense
app and get an app object with which you can use all of the methods of the App
API. That is the general pattern of the Capability APIs.

| Capability API name | Namespace                 |
| ------------------- | ------------------------- |
| Root API            | `qlik`                    |
| App API             | `qlik.app`                |
| Bookmark API        | `qlik.app.bookmark`       |
| Field API           | `qlik.app.field`          |
| Global API          | `qlik.global`             |
| Table API           | `qlik.table`              |
| Selection API       | `qlik.app.selectionState` |
| Variable API        | `qlik.app.variable`       |
| Visualization API   | `qlik.app.visualization`  |
