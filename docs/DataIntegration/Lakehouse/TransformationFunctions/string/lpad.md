---
title: "LPAD"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/lpad.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# LPAD

Uses a given padstring to left pad a string to a certain size.

## Syntax

```
LPAD(STRING, SIZE, PADSTRING)
```

## Arguments

#### **`STRING`**

Type: `string`

The string to be padded.

#### **`SIZE`**

Type: `bigint`

A non-negative integer specifying the length of the result string.

#### **`PADSTRING`**

Type: `string`

The string to use for padding. This must be non-empty.

## Returns

Type: `string`

`STRING` left padded to `SIZE` with `PADSTRING`.

If `SIZE` is less than the length of `STRING`, the result is truncated to `SIZE` characters.

---

## Examples

| STRING | SIZE | PADSTRING | Output |
| --- | --- | --- | --- |
| Call me Ishmael. Some years ago | 7 |  | Call me |
| drizzly November | 16 | . | drizzly November |
| right | 1 |  | r |
| what | 9 | ?! | ?!?!?what |
| `null` | 9 | `''` | `null` |
| hi | 5 | five | fivhi |
| hi | 10 | five | fivefivehi |
