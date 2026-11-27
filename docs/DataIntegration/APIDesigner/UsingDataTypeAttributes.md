---
title: "Using data type attributes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/UsingDataTypeAttributes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design", "Creating a data type"]
---

# Using data type attributes

The following tables describe the attributes that can be defined for
different data types.

## General attributes

These attributes are available for all data types.

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Name | Name of the data type or property. | Root element for the data type or property definition. |
| Description | Description of the property. | description |
| Required | Boolean, defines whether a property is required or optional. | - OAS 3.0 and Swagger 2.0: Required properties are listed   in a required element at the object   level. - RAML: required |
| Restrictions | Defines whether the property is available in the request, response or both. | - OAS 3.0: Properties can have a writeOnly or readOnly   element with a boolean value. - No corresponding element in Swagger 2.0 or RAML 1.0. |
| Examples | Sample values for the property. They can be returned when using an API mock. | - OAS 3.0 and Swagger 2.0: The first value is used in the   example element. Other values are   ignored. Information noteNote: The OAS 3.0 specification includes an   examples element, but it is not supported by   API Contracts. - RAML: examples |

## Object attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Additional properties | Boolean, defines whether the object accepts properties not included in the data type definition. This is enabled by default. | additionalProperties |

## Array attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Min items and Max items | Minimum and maximum number of items in an array. | minItems and maxItems |
| Unique items | Boolean, defines whether each item in an array must be unique. | - OAS 3.0 and RAML 1.0: uniqueItems - No corresponding element in Swagger 2.0. |

## String attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Enum | Possible values for the property. | enum |
| Min length and Max length | Minimum and maximum number of bytes in the value. | minLength and maxLength |
| Pattern | Regular expression that the value should match. | pattern |
| Default | Value to use if a value is not provided. | default |

## Number and integer attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Enum | Possible values for the property. | enum |
| Format | Format to use for a number or integer. | format |
| Minimum and Maximum | Minimum and maximum value of a number or integer. | minimum and maximum |
| Default | Value to use if a value is not provided. | default |

## Date and time attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Enum | Possible values for the property. | enum |
| Default | Value to use if a value is not provided. | default |

## Datetime attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Enum | Possible values for the property. | enum |
| Format | Format to use for a datetime. | - RAML 1.0: format - OAS 3.0: Datetime properties in OAS 3.0 are defined   as strings with the format date-time. The default   datetime format used is RFC3339, but if `rfc2616`   is selected, a custom format date-time-rfc2616 is   used. - Swagger 2.0: Datetime properties are defined in the   same way as in OAS 3.0, but Swagger 2.0 does not support custom formats.   They will be interpreted as RFC3339, regardless of the format   selected. |

## File attributes

| Field | Description | Corresponding OAS/Swagger and RAML element |
| --- | --- | --- |
| Min length and Max length | Minimum and maximum number of bytes in the value. | minLength and maxLength |
| File types | Type of file to use, in the format \*/\*. For example: image/png | - RAML 1.0: fileTypes |
