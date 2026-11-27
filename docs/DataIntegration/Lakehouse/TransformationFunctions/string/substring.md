---
title: "SUBSTRING"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/substring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# SUBSTRING

Extracts a substring starting from a specified point within the given string.

This is an alias for the [`SUBSTR`](substr.htm) function.

## Syntax

```
SUBSTRING(STRING, START [, LENGTH])
```

## Arguments

#### **`STRING`**

Type: `string`

The string to extract a substring from.

#### **`START`**

Type: `integer`

The starting index of the substring.

Positions start with `1`. A negative starting position is interpreted as being relative to the end of the string.

#### **`LENGTH`**

Type: `integer`

(Optional) The length of the substring.

If omitted, the rest of the string after the starting position `START` is returned.

## Returns

Type: `string`

Returns a substring from `STRING` of length `LENGTH` from the starting position `START`.

---

## Examples

| STRING | START | LENGTH | Output |
| --- | --- | --- | --- |
| Hello World | 1 | 5 | Hello |
| Hello World | 0 | 4 | `''` |
| Hello World | -5 | 5 | World |
| Hello World | 12 | 4 | `''` |
| Hello World | -12 | 4 | `''` |
| Hello World | 2 | 3 | ell |
| Hello World | 3 | -2 | `''` |
| Hello World | 2 | 14 | ello World |
| Hello World | 2 |  | ello World |
| Hello World | -3 | 2 | rl |
| `null` | -3 | 2 | `null` |
