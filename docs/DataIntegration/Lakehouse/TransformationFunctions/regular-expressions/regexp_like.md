---
title: "REGEXP_LIKE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regexp_like.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Regular Expressions"]
---

# REGEXP\_LIKE

Evaluates a regular expression pattern and determines if it is contained within the given string.

This function is similar to the `LIKE` operator, except that the pattern only needs to be contained within the string, rather than needing to match all of the string. In other words, this performs a *contains* operation rather than a *match* operation. You can match the entire string by anchoring the pattern using `^` and `$`.

## Syntax

```
REGEXP_LIKE(STRING, PATTERN)
```

## Arguments

#### `STRING`

Type: `string`

A sequence of characters.

#### `PATTERN`

Type: `string`

A regular expression pattern.

This pattern must be a Java regular expression. String literals are unescaped. For example, to match `'\abc'`, a regular expression would be `'^\\abc$'`.

See the [RegEx pattern table](regular-expressions.htm#regular-expression-patterns) for more information.

## Returns

Type: `Boolean`

A Boolean value indicating whether or not `PATTERN` is contained with `STRING`.

---

## Examples

| STRING | PATTERN | Output |
| --- | --- | --- |
| "1a 2b 14m" | "\d+b" | `true` |
| "1a 2b 14m" | "^1" | `true` |
| "ab abc abcc bac" | "ab\*" | `true` |
| "ab a1bc ab1cc bac" | "a1\*" | `true` |
| "2 a1bc ab11cc 311" | "a1(2)" | `true` |
| "2 a1bc ab11cc 311" | "a1(2)sdag" | `false` |
| `null` | "\d+" | `null` |
