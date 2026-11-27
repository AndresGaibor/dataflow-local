---
title: "JSON_PATH"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/structural/json_path.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "Structural"]
---

# JSON\_PATH

Extracts data from JSON objects.

## Syntax

```
JSON_PATH(path, JSON)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| path | string | JSON Path Expression |  |
| JSON | string | A string that contains JSON Document |  |

## Examples

| path | JSON | Output |
| --- | --- | --- |
| `"$[*].author.name"` | `"[{"name": "The Great Gatsby", "author": {"name": "F. Scott Fitzgerald"}}, {"name": "Nineteen Eighty-Four", "author": {"name": "George Orwell"}}]` | `[F. Scott Fitzgerald, George Orwell]` |
| `"net_id"` | `"{ "net_id": 41 }"` | `41` |
| `"net_id"` | `"{ "net_id": [41, 42] }"` | `[41,42]` |
| `"net_id[*]"` | `"{ "net_id": [41, 42] }"` | [`41`, `42`] |
| `"net_id.parent"` | `"{ "net_id": [41, 42] }"` | null |
| `"$[*]"` | `"[1,2,3]"` | [`1`, `2`, `3`] |
| `"$[*].author"` | `"[{"name":"The Great Gatsby", "author":{"name": "F. Scott Fitzgerald"}}, {"name":"Nineteen Eighty-Four", "author": {"name": "George Orwell"}}]` | `[{"name":"F. Scott Fitzgerald"}, {"name":"George Orwell"}]` |
