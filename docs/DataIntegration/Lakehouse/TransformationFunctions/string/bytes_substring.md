---
title: "BYTES_SUBSTRING"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/bytes_substring.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# BYTES\_SUBSTRING

Returns a substring of the input value, using the offsets in bytes of the UTF-8 encoded byte representation. Partial characters and invalid UTF-8 code points are removed from the result.

## Syntax

Use the following syntax to include the `BYTES_SUBSTRING` function in your query:

```
BYTES_SUBSTRING(value, startIndex, endIndex)
```

## Arguments

The `BYTES_SUBSTRING` function requires the following arguments:

- `value` input is the string upon which you want to perform the substring function.
- `startIndex` begins at `1` and includes the first character in your string.
- `endIndex` counts from the first character in the string, not from the `startIndex` position.

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | string | The input value to perform the substring function on |  |
| startIndex | int | The inclusive start index in bytes |  |
| endIndex | int | The exclusive end index in bytes |  |

## Returns

Returns a `string` value.

---

## Examples

The following example shows how the `startIndex` and `endIndex` arguments affect the `Output` value. Here, the `endIndex` value demonstrates that regardless of the `startIndex` value, the `endIndex` works from position **1** in the string to include **10** characters.

| value | startIndex | endIndex | Output |
| --- | --- | --- | --- |
| 'Hello World' | 1 | 10 | `Hello Worl` |
| 'Hello World' | 2 | 10 | `ello Worl` |
| '⻤Hello Wor⻤' | 2 | 10 | `Hello W` |
| '⻤Hello Wor⻤' | 1 | 10 | `⻤Hello W` |
| 'Hello' | 1 | 10 | `Hello` |
