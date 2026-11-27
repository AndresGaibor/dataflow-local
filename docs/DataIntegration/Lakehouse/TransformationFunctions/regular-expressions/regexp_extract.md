---
title: "REGEXP_EXTRACT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regexp_extract.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Regular Expressions"]
---

# REGEXP\_EXTRACT

Finds the first match of the regular expression pattern in string and returns the capturing group number requested.

## Syntax

```
REGEXP_EXTRACT(string, pattern, group)
```

## Arguments

| Name | Type |
| --- | --- |
| string | string |
| pattern | string |
| group | numeric |

## Returns

When the group argument is excluded, this function returns the first substring matched by the regular expression pattern in the string.

If the group argument is included, the function finds the first occurrence of the regular expression pattern in the string and returns the capturing group number group.

---

## Examples

| string | pattern | group | output |
| --- | --- | --- | --- |
| '1a 2b 14m' | '\d+' |  | '1' |
| 'document.pdf' | '.([^.]+)$' |  | '.pdf' |
| 'john.doe@example.com' | '(?<=@).+$' |  | 'example.com' |
| '1a 2b 14m' | '' |  | '' |
| '1a 2b 14m' | 'c' |  | NULL |
| '1a 2b 14m' | '(1a' |  | NULL |
| '1a 2b 14m' | '(\d+)([a-z]+)' | '2' | 'a' |
| '1a 2b 14m' | '(\d+)([a-z]+)' | '1' | '1' |
| '1a 2b 14m' | '(\d+)([a-z]+)' | '0' | '1a' |
