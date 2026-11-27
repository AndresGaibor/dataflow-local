---
title: "STRING_FORMAT"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/string_format.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# STRING\_FORMAT

Format any number of inputs into a string using the given format.

## Syntax

```
STRING_FORMAT(formatString, inputs1[, inputs2, ..., inputsN])
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| formatString | string | The format string where {n} prints the n'th input. For example, the pattern '{0}.{0}.{1}' on the inputs 'a' and 'b' will result in the string 'a.a.b' | null |
| inputs# | any |  |  |

## Returns

Returns a `string` value.

---

## Examples

| formatString | inputs1 | inputs2 | inputs3 | Output |
| --- | --- | --- | --- | --- |
| '{0} {1} {2}' | 'a' | 'b' | 'c' | `a b c` |
| '{0}' | 1.23 |  |  | `1.23` |
| '{0,number,percent}' | 0.5 |  |  | `50%` |
| '{0,number,#.###}' | 1.23456 |  |  | `1.235` |
| '{0,number,#.###}' | 1.2 |  |  | `1.2` |
| '{0,number,0.000}' | 1.23456 |  |  | `1.235` |
| '{0,number,0.000}' | 1.2 |  |  | `1.200` |
| '{0,number,###,###.###}' | 123456789.01235 |  |  | `123,456,789.012` |
| '{0,number,000,000.000}' | 123456789.01235 |  |  | `123,456,789.012` |
