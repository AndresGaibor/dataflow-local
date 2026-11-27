---
title: "Transformations at export"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/TransformationAtExport.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with OpenAPI Specification and RAML definitions", "Exporting a definition"]
---

# Transformations at export

When exporting a definition designed with API Contracts features in a format that does not support them, the definition is modified to fit the target format. Some expressivity is lost in the process.

The table below describes the modifications made to your API definition when exporting in one of the following specifications:

- OAS/Swagger 2.0
- Availability-note[Deprecated](https://help.talend.com/r/en-US/Cloud/labels-on-talend-help-center/availability-deprecated)

  This content is deprecated.

  Swagger 1.2
- RAML 1.0

| Unsupported feature | Transformation |
| --- | --- |
| Components | The component is copied in every place where it is used. |
| Response ranges and default responses | The response is removed. |
| Bearer authentication and OpenID Connect | The security scheme is removed. |
| allOf combinations | The combination is replaced with an object containing all the properties of all the types used. |
| anyOf and oneOf combinations | The combination is replaced with an empty object. |
| Multiple endpoints | The first published endpoint is included in the definition, the others are ignored. |

OpenAPI Specification 3.0 only supports URLs in the Terms of service field. When exporting a definition in OAS 3.0, this field is exported only if it contains a URL. If it does not, the Terms of service field is ignored to ensure the validity of the definition.
