---
title: "REGEX_MATCH_POSITION"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regex_match_position.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Regular Expressions"]
---

# REGEX\_MATCH\_POSITION

Matches the regular expression on the input string, and returns the index of the first match.

## Syntax

```
REGEX_MATCH_POSITION(pattern, value, startPosition)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| pattern | string | Pattern to search for |  |
| value | string |  |  |
| startPosition | numeric |  |  |

## Returns

Returns a `bigint` value.

---

## Examples

| pattern | value | startPosition | Output |
| --- | --- | --- | --- |
| ',' | '1,2,3' | 0 | 1 |
| '2,\d' | '1,2,3' | 2 | 2 |
| '2,\d' | '1,2,3' | 3 | null |
| ',' | '1,2,3' | -1 | null |
| ',' | '1,2,3' | -2 | 3 |
