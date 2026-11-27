---
title: "URL_ENCODE"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/url/url_encode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "URL"]
---

# URL\_ENCODE

This function escapes the given input value by encoding it so that it can be safely included in URL query parameter names and values:

- Alphanumeric characters are not encoded.
- The characters `.`, `-`, `*` and `_` are not encoded.
- The ASCII space character is encoded as `+`.
- All other characters are converted to UTF-8 and the bytes are encoded as the string `%XX` where `XX` is the uppercase hexadecimal value of the UTF-8 byte.

## Syntax

```
URL_ENCODE(VALUE)
```

## Arguments

#### `VALUE`

Type: `string`

The value to encode.

## Returns

Type: `string`

The encoded `VALUE`.

---

## Examples

| VALUE | Output |
| --- | --- |
| The quick brown fox | The+quick+brown+fox |
| Comment #5 | Comment+%235 |
| &$#\_line\_!123 | %26%24%23\_line\_%21123 |
| `''` | `''` |
| word+word word | word%2Bword++word |

### Example

#### SQL

```
//url_example1
        URL_ENCODE('word+word  word')
```

```
//url_example2
        URL_ENCODE('&$#_line_!123')
```

#### Query result

| url\_example1 | url\_example2 |
| --- | --- |
| word%2Bword++word | %26%24%23\_line\_%21123 |
