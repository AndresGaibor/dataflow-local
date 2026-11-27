---
title: "API gateway compatibility mode"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ApiGatewayCompatibilityMode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with API gateways"]
---

# API gateway compatibility mode

API Contracts offers an
API gateway compatibility mode to help you import your definition into AWS API Gateway and
Azure API Management.

When exporting your API in a gateway compatibility mode, API Contracts may modify your definition so it can be
imported successfully into the selected gateway.

In some cases, there are no modifications but a message is displayed to inform you of the
compatibility issue that you may encounter with the definition you exported.

## Exporting an OAS 3.0 definition for AWS API Gateway

The following table describes how API Contracts handles the
features unsupported by AWS API Gateway when exporting a definition, and what happens in AWS
API Gateway when you import the definition.

| Unsupported OpenAPI feature | API Contracts behavior at export | AWS API Gateway behavior at import |
| --- | --- | --- |
| The example attribute is not supported. | The attribute is preserved. | The attribute is removed from the schema. |
| The readOnly attribute is not supported. | The attribute is preserved. | The attribute is removed from the schema. |
| The additionalProperties attribute is not supported. | The attribute is preserved and an information message is displayed. | A warning message is displayed but can be ignored and the definition can be imported successfully. |
| Security definition types:  - oauth2 is not supported, - http is not supported, - openIdConnect is not supported. | The security schemes are preserved and an information message is displayed. | A warning message is displayed but can be ignored and the definition can be imported successfully. |
| Primitive data types in responses are not supported. | The primitive type is wrapped into a component schema and a warning message is displayed. | The import succeeds. |
| Media-type ranges are not supported. | The request or response is preserved and an information message is displayed. | The import fails and a warning message is displayed. |
| Default response is not supported. | The response is preserved and an information message is displayed. | The import fails and a warning message is displayed. |
| Range responses are not supported. | The response is preserved and an information message is displayed. | The import fails and a warning message is displayed. |
| Path variables, query parameters and headers must have unique names. | The parameters are preserved and an error message is displayed. | The import fails. |

## Exporting an OAS/Swagger 2.0 definition for Azure API Management

The following table describes how API Contracts handles the
features unsupported by Azure API Management when exporting a definition, and what happens
in Azure API Management when you import the definition.

| Unsupported OpenAPI feature | API Contracts behavior at export | Azure API Management behavior at import |
| --- | --- | --- |
| Required parameters across both paths and queries must have unique names. | An error message is displayed. | The import fails. |
