---
source: https://qlik.dev/changelog/91-qlik-embed-classic-chart/
last_updated: 2026-06-02T18:15:45+01:00
---

# New classic/chart UI for qlik-embed

## Introducing classic/chart

`classic/chart` is a new UI for [qlik-embed](https://qlik.dev/embed/qlik-embed/why-qlik-embed/).
`classic/chart` renders visualizations that have not been converted
to [nebula.js](https://qlik.dev/extend/extensions/nebula-js/quickstart/first-extension/) or use
the [classic extension API](https://qlik.dev/extend/extensions/extension-api/create-with-extension-api/extension-get-started/).

## Using classic/chart

Like other UIs available through qlik-embed, when you want to use `classic/chart`
in an embedded analytics context, set the `ui` property to `classic/chart`. If you use
qlik-embed web-components it will look something like this:

```html
<qlik-embed
    ui="classic/chart"
    app-id="<appId>"
    object-id="<objectId>"
></qlik-embed>
```

## classic/chart compatibility

`classic/chart` will render supported visualizations from Qlik Sense applications.
For a full support matrix, refer to
the [supported charts](https://qlik.dev/embed/foundational-knowledge/visualizations/) page.

## Third-party extensions

Third-party extensions may not render correctly within embedded contexts compared
to the native Qlik Sense experience if the extension manipulates private code
such as CSS. Manipulating CSS in the native experience is not supported by Qlik,
therefore, it's not supported in qlik-embed.

Additionally, for best compatibility, it is suggested to enable iframe mode when
working with extensions:

```html
<qlik-embed
    ui="classic/chart"
    app-id="<appId>"
    object-id="<objectId>"
    iframe="true"
></qlik-embed>
```

To learn more about third-party extension compatibility with qlik-embed,
please contact the extension author.

## Limitations

`classic/chart` does not support the following features:

- Right-click context menu
- Export data

You can learn more about qlik-embed
on the [Why qlik-embed](https://qlik.dev/embed/qlik-embed/why-qlik-embed/) page,
or review the [classic/chart example](https://qlik.dev/embed/qlik-embed/parameters/#classicchart).
