---
source: https://qlik.dev/apis/javascript/listbox/
last_updated: 2026-11-03T10:49:46Z
---

# Nebula Listbox properties

`Version: 7.9.0` | _stable_

nebula listbox properties definition

## Table of Contents

### Definitions

- [ListboxProperties](#listboxproperties-object)
- [ListObjectDef](#listobjectdef-interface)
- [Representation](#representation-interface)
- [ValueExpression](#valueexpression-object)

## Definitions

### ListboxProperties `object`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoConfirm` | boolean | No | false | Automatically confirm selections when clicking outside a listbox, without showing the selections toolbar. |
| `checkboxes` | boolean | No | false | Show values as checkboxes instead of as fields. |
| `frequencyMax` | 'fetch' \| [ValueExpression](#valueexpression-object) | No | - | frequencyMax calculation needed for histogram when not using qListObjectDef.qFrequencyMode: 'P' use an expression in the form `Max(AGGR(Count([field]), [field]))` (when needed) or 'fetch' that triggers an extra engine call but needed for library dimension that could change field when using the object |
| `histogram` | boolean | No | false | Show histogram bar. also requires (qListObjectDef.qFrequencyMode 'V' and frequencyMax) or qListObjectDef.qFrequencyMode 'P' |
| `layoutOptions` | object | No | - | Layout settings. |
| `qListObjectDef` | [ListObjectDef](#listobjectdef-interface) | Yes | - |  |
| `representation` | [Representation](#representation-interface) | Yes | - |  |
| `searchEnabled` | boolean | No | true | Enables search. |
| `selectionMode` | 'add' \| 'replace' | No | "add" | Controls what a click does to the current selection. 'add' (default) adds/toggles the clicked value while keeping other selections (holding ctrl/cmd replaces the selection with just that value). 'replace' inverts this: a plain click replaces the selection with just the clicked value, while holding ctrl/cmd adds/toggles it into the current selection. |
| `showTitle` | boolean | No | true | Show title. |
| `title` | string | No | "" | Listbox title |
| `wildCardSearch` | boolean | No | false | Pre-fill search input field with wildcard characters. |

<details>
<summary>Properties of `layoutOptions`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dataLayout` | 'singleColumn' \| 'grid' | No | "singleColumn" | Layout mode. |
| `dense` | boolean | No | false | Dense mode. |
| `layoutOrder` | 'row' \| 'column' | No | "row" | Layout order. Only used when dataLayout is 'grid' |
| `maxVisibleColumns` | object | No | - | Max visible columns. Only used when dataLayout is 'grid' and layoutOrder is 'row' |
| `maxVisibleRows` | object | No | - | Max visible rows. Only used when dataLayout is 'grid' and layoutOrder is 'column' |

<details>
<summary>Properties of `maxVisibleColumns`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | No | true | Automatically fit as many columns as possible. Only used when dataLayout is 'grid' and layoutOrder is 'row' |
| `maxColumns` | number | No | 3 | Fixed number of max visible columns. Only used when dataLayout is 'grid' layoutOrder is 'row' and auto is false |

</details>

<details>
<summary>Properties of `maxVisibleRows`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `auto` | boolean | No | true | Automatically fits as many rows as possible. Only used when dataLayout is 'grid' and layoutOrder is 'column' |
| `maxRows` | number | No | 3 | Fixed number of max visible rows. Only used when dataLayout is 'grid' layoutOrder is 'column' and auto is false |

</details>

</details>

---

### ListObjectDef `interface`

extends `qix.ListObjectDef`

Extends `ListObjectDef`, see Engine API: `ListObjectDef`.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `frequencyEnabled` | boolean | No | false | Show frequency count. also requires qListObjectDef.qFrequencyMode to be set |

---

### Representation `interface`

Representation settings for the dimension values, set on the listbox object root `representation`
(a sibling of `qListObjectDef`, alongside `layoutOptions`).

Notes on image representation:
-   * When `type` is `'image'` the values are rendered as images. Image metadata is resolved from
list-object expressions (`qListObjectDef.qExpressions`) using their `qLabel` keys.

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `borderColor` | string | No | "#d9d9d9" | Cell border color. Only used when `type` is 'image' and `borderWidth` > 0. |
| `borderColorMode` | 'single' \| 'expression' \| 'selectionState' | No | "single" | Cell border color mode. Only used when `type` is 'image' and `borderWidth` > 0. |
| `borderWidth` | number | No | 0 | Cell border width in px. Only used when `type` is 'image'. |
| `cellBgColor` | string \| object \| [ValueExpression](#valueexpression-object) | No | - | Cell background color (hex string or color object when cellBgColorMode='single') or expression (when cellBgColorMode='expression'). Only used when `type` is 'image'. |
| `cellBgColorMode` | 'single' \| 'expression' \| 'selectionState' | No | "single" | Cell background color mode. Only used when `type` is 'image'. |
| `cornerRadius` | number | No | 4 | Corner radius of the image cell in pixels. Only used when `type` is 'image'. |
| `gridGap` | number | No | 1 | Spacing between image grid cells, as a percentage of the column width. Only used when `type` is 'image'. |
| `imageLabel` | [ValueExpression](#valueexpression-object) | No | - | Per-value image label expression. Only used when `type` is 'image' and `imageSetting` is 'label'. Stored in qExpressions with qLabel='imageLabel'. |
| `imagePosition` | string | No | "topCenter" | Image position within the cell. Only used when `type` is 'image' and `imageSize` is not 'stretch'. |
| `imageSetting` | 'url' \| 'label' | No | "label" | When `type` is 'image', choose whether the   per-value expression (qExpressions.qLabel='imageUrl'/'imageLabel') provides the image URL   (`'url'`) or the image label (`'label'`). |
| `imageSize` | 'alwaysFit' \| 'fitWidth' \| 'fitHeight' \| 'stretch' \| 'alwaysFill' | No | "alwaysFit" | Image sizing mode. Only used when `type` is 'image'. |
| `imageUrl` | [ValueExpression](#valueexpression-object) | No | - | Per-value image URL expression. Only used when `type` is 'image' and `imageSetting` is 'url'. Stored in qExpressions with qLabel='imageUrl'. |
| `showSelected` | boolean | No | true | When `type` is 'image', show only selected values once a selection is applied (while selecting, all values stay visible). Set to false to keep unselected values visible. |
| `subtitle` | [ValueExpression](#valueexpression-object) | No | - | Per-value subtitle expression. Only used when `type` is 'image' and `textOverlay` is not false. |
| `textOverlay` | boolean | No | true | Whether to render the title/subtitle overlay text. Only used when `type` is 'image'. |
| `titleBackground` | boolean | No | true | Draw a background behind the title text for legibility. Only used when `type` is 'image'. |
| `titlePosition` | string | No | "top-center" | Overlay text alignment as `{vertical}-{horizontal}` (e.g. 'top-left', 'center-center', 'bottom-right'). Only used when `type` is 'image'. |
| `tooltip` | [ValueExpression](#valueexpression-object) | No | - | Per-value tooltip expression. Only used when `type` is 'image'. |
| `type` | 'text' \| 'image' | No | "text" | How the dimension values are presented. |

---

### ValueExpression `object`

see: https://qlik.dev/apis/json-rpc/qix/schemas#%23%2Fdefinitions%2Fschemas%2Fentries%2FValueExpression

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qValueExpression` | object | Yes | - |  |

<details>
<summary>Properties of `qValueExpression`</summary>

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `qExpr` | string | Yes | - |  |

</details>

---
