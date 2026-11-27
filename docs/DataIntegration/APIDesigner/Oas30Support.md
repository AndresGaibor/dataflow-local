---
title: "OpenAPI Specification 3.0 support"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/Oas30Support.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with OpenAPI Specification and RAML definitions"]
---

# OpenAPI Specification 3.0 support

Design an API with OpenAPI Specification (OAS) 3.0 using API Contracts.

OpenAPI Specification 3.0 comes with new features, bringing more expressivity and
productivity to API designers.

For more information about OpenAPI, see the [Swagger
documentation](https://swagger.io/docs/specification/about/).

## Components

Components allow you to reuse various elements across an API. These elements can be:

- Path variables
- Query parameters
- Headers
- Responses

## Combinations

Combinations allow you to create a new data type by combining several
other data types. API Contracts supports two
types of combinations:

- Composition (allOf) allows you to aggregate schema properties from different
  schemas. For example, you can define a data type `Company` by
  reusing all the properties from the existing types `Contact`
  and `Error`. ![Example of a composition.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/all_of.png)
- Polymorphism (oneOf/anyOf) allows you to create an entity that can use the
  properties from different data types.
  - oneOf allows you to define a data type containing the
    properties of one of the selected types. For example, if you create an
    operation to get information about a service account, you can define the
    response using the oneOf combination to get either all the
    properties of `Error` or all the properties of
    `ServiceAccountCount`. ![Example of a polymorphism.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/oneof.png)
  - anyOf allows you to define a data type containing the
    properties of one or several of the selected types. For example, you can
    define a data type `nervousSystem` and a type
    `skeleton` containing different properties, and use
    the anyOf combination to create a data type containing any
    properties from either of these types.

    An anyOf
    combination is valid as long as it contains all the required parameters
    of at least one of the data types selected. The example below uses the
    brain\_weight property from the
    `nervousSystem` type and the
    skull\_height and `teeth`
    properties from `skeleton`.

    ![Example of a combination using the nervousSystem and skeleton data types.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/anyof.png)

For more information about composition and polymorphism, see [Inheritance and Polymorphism](https://swagger.io/docs/specification/data-models/inheritance-and-polymorphism/) and [Difference Between anyOf and oneOf](https://swagger.io/docs/specification/data-models/oneof-anyof-allof-not/#anyof-vs-oneof).

## Responses

OAS 3.0 allows you to define new types of responses for your operations:

- Response ranges: instead of defining a response such as `200`, you can set it as `2XX`, so that it includes responses from `200` to `299`.
- Default responses: you can define a default response to be returned
  when a specific or range response is not defined.

Responses defined with an explicit code take
precedence over response ranges and default responses, and response ranges take
precedence over default responses. In the following example:

- The `204` response is defined and takes precedence over the
  others.
- The `2XX` response applies to response codes 200 to 203 and
  205 to 299.
- The `default` response applies to all 1XX, 3XX, 4XX, and 5XX
  responses.

![Responses section.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/responses-headers-api.png)

## Security

OAS 3.0 brings new security schemes for your API:

- Bearer authentication
- OpenIdConnect

## Restrictions

OAS 3.0 allows you to indicate that some properties are read-only or
write-only.

This option is available in data types only and cannot be defined in
requests or responses at the operation level.

![Restriction example.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_restrictions.png)
