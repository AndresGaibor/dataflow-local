---
title: "REGEXP_REPLACE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/regular-expressions/regexp_replace.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Regular Expressions"]
---

# REGEXP\_REPLACE

Replaces every instance of the substring matched by a regular expression pattern in the given string with a specified replacement.

## Syntax

```
REGEXP_REPLACE(STRING, PATTERN, REPLACEMENT)
```

## Arguments

#### `STRING`

Type: `string`

The string that is searched for a `PATTERN` match.

#### `PATTERN`

Type: `string`

A regular expression pattern.

This pattern must be a Java regular expression. String literals are unescaped. For example, to match `'\abc'`, a regular expression would be `'^\\abc$'`.

See the [RegEx pattern table](regular-expressions.htm#regular-expression-patterns) for more information.

#### `REPLACEMENT`

Type: `string`

The string used to replace instances of `PATTERN` found in `STRING`.

[Capturing groups](http://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html#cg) can be referenced in `REPLACEMENT` using `$g` for a numbered group or `${name}` for a named group. A dollar sign (`$`) may be included in the replacement by escaping it with a backslash (`\$`):

## Returns

Type: `string`

`STRING` with every instance of the substring matched by the regular expression `PATTERN` replaced with `REPLACEMENT`.

---

## Examples

| STRING | PATTERN | REPLACEMENT | Output |
| --- | --- | --- | --- |
| Hello world | w | W | Hello World |
| Hello World | o | 0 | Hell0 World |
| Bond, James | (\w+)\W+(\w+) | The names $1. $2 $1. | The names Bond. James Bond. |
| Hello World! | ! | `''` | Hello World |
| Hello xxWorld | x | `''` | Hello World |
| Hellol World | l(?= ) | `''` | Hello World |
| Hellol World | l(?![lod]) | `''` | Hello World |
| Helloo World | (?<=o)o | `''` | Hello World |
| Hello WorldW | (?<! )W | `''` | Hello World |
| `null` | '(?<! )W | `''` | `null` |
