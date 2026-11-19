---
source: https://qlik.dev/apis/javascript/sn-network-chart/
last_updated: 2026-10-23T15:23:57Z
---

# Nebula Network chart

`Version: 1.3.0` | _stable_

Network chart generic object definition

## Table of Contents

### Entries

- [properties](#properties-object)

## Entries

### properties `object`

extends `GenericObjectProperties`

#### Properties

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `version` | string | Yes | - | Current version of this generic object definition |
| `qHyperCubeDef` | object | Yes | - | Extends `HyperCubeDef`, see Engine API: `HyperCubeDef`. |
| `components` | object[] | Yes | - |  |
| `showTitles` | boolean | No | false |  |
| `title` | string | No | "" |  |
| `subtitle` | string | No | "" |  |
| `footnote` | string | No | "" |  |
| `showDetails` | boolean | No | true |  |
| `showDetailsExpression` | boolean | No | false |  |
| `edgeType` | 'dynamic' \| 'continuous' \| 'discrete' \| 'diagonalCross' \| 'straightCross' \| 'horizontal' \| 'vertical' \| 'curvedCW' \| 'curvedCCW' \| 'cubicBezier' | No | "dynamic" |  |
| `displayEdgeLabel` | boolean | No | false |  |
| `posEdgeLabel` | 'top' \| 'middle' \| 'bottom' \| 'horizontal' | No | "top" |  |
| `nodeShape` | 'dot' \| 'square' \| 'star' \| 'triangle' \| 'triangleDown' \| 'diamond' | No | "dot" |  |
| `shadowMode` | boolean | No | false |  |

---
