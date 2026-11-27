---
title: "REGEXP_EXTRACT_ALL"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regexp_extract_all.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Regular Expressions"]
---

# REGEXP\_EXTRACT\_ALL

Matches the regular expression on the input string. Returns the escape groups if any exists or the original string if none exists.

## Syntax

```
REGEXP_EXTRACT_ALL(first, second)
```

## Arguments

| Name | Type |
| --- | --- |
| first | string |
| second | string |

## Returns

Returns the substrings(s) matched by the regular expression.

---

## Examples

| first | second | Output |
| --- | --- | --- |
| "abcdefabc" | "abc" | [`abc`, `abc`] |
| "1a2b3" | "\d+" | [`1`, `2`, `3`] |
| "Word" | "^((((((((((..)?.)?.)?.)?.)?.)?.)?.)?.)?.)?" | [`Word`, `Wor`, `Wo`, `W`] |
| "abab" | "abc" | null |
| null::string | "abc" | null |
| "abc" | '' | [`,` , `,` ] |
| array["ab1", "a2a", "345"] | "\d" | [`1`, `2`, `3`, `4`, `5`] |
| array["ab1", "a2a", "345"] | array['\d', "a"] | [`1`, `a`, `2`, `a`, `a`, `3`, `4`, `5`] |
| "abc" | null::string | null |
