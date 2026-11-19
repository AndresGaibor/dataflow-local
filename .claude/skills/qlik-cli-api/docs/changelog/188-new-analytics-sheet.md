---
source: https://qlik.dev/changelog/188-new-analytics-sheet/
last_updated: 2025-12-12T09:12:17Z
---

# Preview attribute added to \`analytics/sheet\` and \`analytics/chart\`

A new `preview="true"` attribute has been added to the `analytics/sheet` and `analytics/chart` web component.
The analytics sheet and chart exploration are lightweight components designed to bring the primary Qlik
Sense experience to users.
Setting `preview="true"` enables the preview mode, which includes the following enhancements:

- Support for non-Nebula charts (legacy charts such as the Text and Image object)
- Improved theme support to match the native Qlik Sense client
- Support for visualization extensions

Example:

```html
<qlik-embed
    ui="analytics/sheet"
    app-id="<APP_ID_FROM_QLIK_ANALYTICS>"
    theme="<NAME_OF_THEME>"
    object-id="<SHEET_ID_FROM_APP>"
    preview="true"
></qlik-embed>
```

To learn more about `analytics/sheet` and `analytics/chart`, see [UI parameters](https://qlik.dev/embed/qlik-embed/parameters/).
