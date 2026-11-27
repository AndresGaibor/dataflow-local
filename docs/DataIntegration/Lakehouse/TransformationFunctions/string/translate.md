---
title: "TRANSLATE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/string/translate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "String"]
---

# TRANSLATE

Translates the given value using a given dictionary.

## Syntax

```
TRANSLATE(dictionary, keepValuesWithoutTranslation, emptyAsNull, input)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| dictionary | string |  |  |
| keepValuesWithoutTranslation | boolean | Whether to keep values that have that are not mapped to a value in the feature |  |
| emptyAsNull | boolean | If set, empty values will be treated as null |  |
| input | string/numeric |  |  |

## Returns

Returns a `string` value.

---

## Examples

| dictionary | keepValuesWithoutTranslation | emptyAsNull | input | Output |
| --- | --- | --- | --- | --- |
| 'a,Antman |  |  |  |  |
| b,Batman |  |  |  |  |
| d,' | false | false | 'a' | `Antman` |
| 'a,Antman |  |  |  |  |
| b,Batman |  |  |  |  |
| d,' | false | false | 'b' | `Batman` |
| 'a,Antman |  |  |  |  |
| b,Batman |  |  |  |  |
| d,' | false | false | 'c' | null |
| 'a,Antman |  |  |  |  |
| b,Batman |  |  |  |  |
| d,' | true | false | 'c' | `c` |
| 'a,Antman |  |  |  |  |
| b,Batman |  |  |  |  |
| d,' | true | true | 'd' | null |
| 'a,Antman |  |  |  |  |
| b,Batman |  |  |  |  |
| d,' | true | false | 'd' | `` |
| '1234.0,good' | false | false | 1234 | `good` |
| '1234.0,good' | false | false | 1234 | `good` |
| '0.0,good' | false | false | 0 | `good` |
| '-0.0,good' | false | false | 0 | `good` |
| '-0.0,good' | false | false | 0 | `good` |
| '1.23456e17,good' | false | false | 123456000000000000 | `good` |
| '6.000000000000001,good' | false | false | 6 | null |
