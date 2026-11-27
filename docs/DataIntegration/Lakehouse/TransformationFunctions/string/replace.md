---
title: "REPLACE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/replace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# REPLACE

Replaces or removes a substring within the given string.

## Syntax

```
REPLACE(STRING, SEARCH [, REPLACE])
```

## Arguments

#### **`STRING`**

Type: `string`

The string to search.

#### **`SEARCH`**

Type: `string`

The substring to search for in `STRING`.

If this is an empty string, then `REPLACE` is inserted in front of every character and at the end of the `STRING`.

#### **`REPLACE`**

Type: `string`

Default: `''`

(Optional) The string used to replace all found instances of `SEARCH`.

If omitted, all instances of `SEARCH` are removed from `STRING`.

## Returns

Type: `string`

A substring of the input `STRING`.

---

## Examples

| STRING | SEARCH | REPLACE | Output |
| --- | --- | --- | --- |
| string | g |  | strin |
| a | a |  | `''` |
| a | a | b | b |
| 123 | 1 |  | 23 |
| word | word | bird | bird |
| word | bird | thing | word |
| word | or |  | wd |
| word | `null` |  | `null` |
| `null` | bird |  | `null` |
