---
title: "TOP_PRIVATE_DOMAIN"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/url/top_private_domain.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions", "URL"]
---

# TOP\_PRIVATE\_DOMAIN

Get the top private domain from a domain name.

For example, for **www.example.com** will return **example.com**.

## Syntax

```
TOP_PRIVATE_DOMAIN(value)
```

## Arguments

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| value | string |  |  |

## Returns

Returns a `string` value.

---

## Examples

| value | Output |
| --- | --- |
| "www.example.com" | `example.com` |
| "www.example.co.uk" | `example.co.uk` |
| "www.example.uk.com" | `example.uk.com` |
