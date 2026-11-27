---
title: "JOIN_ARRAYS"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/join_arrays.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# JOIN\_ARRAYS

Joins any number of arrays by index using a MessageFormat pattern.

## Syntax

```
JOIN_ARRAYS(formatString, inputs1[, inputs2, ..., inputsN])
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
| '{0} {1} is {2} years old' | array['John', 'Jane'] | array['Smith', 'Johnson'] | array[35, 32] | [`John Smith is 35 years old`, `Jane Johnson is 32 years old`] |
| '{0}:{1}' | array['red', 'green', 'blue', 'luminosity'] | array[255, 255, 0] |  | [`red:255`, `green:255`, `blue:0`, `luminosity:`] |
