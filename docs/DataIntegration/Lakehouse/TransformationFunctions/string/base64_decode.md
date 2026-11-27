---
title: "BASE64_DECODE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/base64_decode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# BASE64\_DECODE

Decodes a base 64 string into a string.

## Syntax

```
BASE64_DECODE(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | string |  |  |

## Returns

Returns a `string` value.

---

## Examples

| value | Output |
| --- | --- |
| "SGVsbG8gV29ybGQ=" | `Hello World` |
| "###" | null |
