---
title: "BASE64_TO_HEX"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/base64_to_hex.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# BASE64\_TO\_HEX

Converts a base 64 string into a hex string.

## Syntax

```
BASE64_TO_HEX(value)
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
| "AAAAAAAAAP8=" | `00000000000000ff` |
| "/w==" | `ff` |
| "QWxsIHlvdXIgYmFzZQ==" | `416c6c20796f75722062617365` |
| "###" | null |
