---
title: "Mocks behavior"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/MocksBehavior.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API mocks"]
---

# Mocks behavior

This section describes how mocks handle the various API definition
elements available in API Contracts.

Mocks provide mostly static answers to requests that correspond to the API
contract. They respond to requests without concern for any security defined on the API,
request payload or request headers (except the Accept header
which is used for content negotiation).

When a request is made, the mock creates a response either based on what the
user provided (example, default value, enum value), or using a built-in example value.

For example, if the request returns an object, the example of the object is
used if one is provided. If not, the examples on each of the properties are used and a JSON
object is created from that. This also works for response headers.

## Responses

- If your operation only has a response range, the first status in the
  range is returned. For example, an operation with a 2XX response range
  returns a 200 response.
- If your operation has a specific response code and response ranges or
  a default response, the defined code is returned. For example, an operation with a 201 response and a 3XX
  response range returns the 201 response.
- If your operation has several response ranges and no defined response
  status, the first status of the first range is returned. For example an operation with a
  4XX and a 5XX response
  range returns a 400 response.
- If your operation only has a default response, the response returned
  depends on the operation method:
  - If the method used is POST, then a
    201 response is returned.
  - For other methods, a 204 response
    is returned if no response body is defined and a 200
    response is returned if a response body is defined.
- If your operation has no defined response, a 200 response is returned.
- 1XX responses are not supported by mocks. If an operation has the
  1XX response range or a defined response code in this range, a
  404 response is returned.

## Combinations

- All of: if an example is
  defined, it is returned. If no example is defined for the data type, the properties of the
  types are merged and the examples defined at the property level are used or example values
  are generated. If a property is defined twice in different types, only the last value is
  preserved. Primitive types are discarded, only objects are returned.
- Any of or One of: if an example is defined, it is returned. If no
  example is defined, a response is generated from the first type in the list.

## Restrictions

- Available in request only: the
  property is excluded from the generated example.
- Available in response only: the property is included in the
  generated example.
- Available in request and response: the property is included in
  the generated example.

Examples provided at the data type level take precedence over properties.
If a property defined as Available in request only is
included in the example, it is returned in the response. If a property defined as Available in response only or Available in request and response is not included in the example, it is not
returned in the response.
