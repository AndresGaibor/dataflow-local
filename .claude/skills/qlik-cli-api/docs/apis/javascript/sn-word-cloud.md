---
source: https://qlik.dev/apis/javascript/sn-word-cloud/
last_updated: 2026-10-23T15:23:57Z
---

# Nebula Word Cloud

`Version: 1.1.0` | _stable_

Word cloud generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

### Definitions

- [PaletteColor](#palettecolor-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition |
| `showTitles` | boolean | No | false |  |
| `title` | string | No | "" |  |
| `subtitle` | string | No | "" |  |
| `footnote` | string | No | "" |  |
| `showDetails` | boolean | No | true |  |
| `showDetailsExpression` | boolean | No | false |  |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `components` | object[] | Yes | - |  |
| `ScaleColor` | string[] | Yes | - | Color scale to use |
| `Orientations` | number | Yes | 2 | Number of orientations to use |
| `MinSize` | number | Yes | 20 | Font size minimum |
| `MaxSize` | number | Yes | 100 | Font size maximun |
| `RadStart` | number | Yes | - | Rotation start in degrees |
| `RadEnd` | number | Yes | 90 | Rotation end in degrees |
| `Scale` | 'linear' \| 'log' | Yes | "linear" | Scale type, linear or logarithmic |
| `customRange` | boolean | No | false | Use of a custom range |
| `customRangeFrom` | [PaletteColor](#palettecolor-object) | Yes | - | Custom coloring from color |
| `customRangeTo` | [PaletteColor](#palettecolor-object) | Yes | - | Custom coloring to color |

---

## Definitions

### PaletteColor `object`

Color information structure. Holds the actual color and index in palette

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `color` | string | Yes | - | Color as hex string (mandatory if index: -1) |
| `index` | number | Yes | - | Index in palette |

---
