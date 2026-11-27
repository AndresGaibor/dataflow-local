---
title: "URL_DECODE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/url/url_decode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "URL"]
---

# URL\_DECODE

Unescapes the given URL encoded value.

This function is the inverse of [`URL_ENCODE`](url_encode.htm).

url\_decode(*value*) → varchar

Unescapes the URL encoded `value`. This function is the inverse of [`url_encode()`](url_encode.htm).

## Syntax

```
URL_DECODE(VALUE)
```

## Arguments

#### `VALUE`

Type: `string`

A URL encoded value.

## Returns

Type: `string`

The decoded `VALUE`.

---

## Examples

```
SELECT url_decode("The+quick+brown+fox") = "The quick brown fox" AND url_decode("Comment+%235") = "Comment #5" AND url_decode('%26%24%23_line_%21123') = "&$#line!123" AND url_decode('') = '' AND url_decode("word%2Bword++word") = "word+word word""
```

| VALUE | Output |
| --- | --- |
| The+quick+brown+fox | The quick brown fox |
| Comment+%235 | Comment #5 |
| %26%24%23\_line\_%21123 | &$#\_line\_!123 |
| `''` | `''` |
| word%2Bword++word | word+word word |
