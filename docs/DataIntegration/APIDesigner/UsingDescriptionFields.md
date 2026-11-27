---
title: "Using description fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/UsingDescriptionFields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with OpenAPI Specification and RAML definitions", "OpenAPI Specification 3.0 support"]
---

# Using description fields

Use description fields as a workaround for unsupported OAS 3.0 features.

While there are some OAS 3.0 features which are not supported in API Contracts, description fields can be used
instead.

For example, parameter serialization is not supported, but you can describe how and why a
query parameter should be serialized in its description field.![Description example.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_how_to_use_description_field_to_explain_query_parameter_serialization.png)
