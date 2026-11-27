---
title: "Designing API security"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ApiSecurity.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# Designing API security

As part of the API design process, you need to specify which consumers can access
your API (authentication) and what they are allowed to do (authorization).

You may want to simply define a common security for your entire API, or choose a finer
policy with a specific security for a critical resource.

You may also want to specify that certain operations are freely accessible without
authentication.

API Contracts
can handle all these cases with the main security types:

- Basic authentication
- Bearer authentication
- Digest authentication
- OAuth 1.0
- OAuth 2.0
- OpenID Connect
- Custom / API key
- Pass through

Cookie authentication is not supported.

## Creating a security scheme

Create a security scheme to be used globally in your API version or in individual
elements.

1. Go to the general information page of your API.
2. Scroll down to the Security schemes section, and click
   Add to create a new scheme.
3. Enter a Name and select a Type in
   the drop-down list.
4. Optional: Enter a Description.
5. Enter other parameters specific to the selected type.

   ![Security scheme definition example.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_OAuth2_security_scheme.png)

Your security scheme is now created, you can use it in your API's global settings
or in specific resources and operations.

## Defining your API security

Define security schemes for your API, resources, and operations.

1. Go to the general information page of your API.
2. In the Global securitysection, add your security schemes
   and select the ones that you want to apply globally to your API version.

   ![In this example, the Petstore API is secured by petstore_auth with the scope write:pets.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_security.png)
3. Select a resource and choose the security schemes your want to apply to all of
   your resource's operations.

   Alternatively, you can select an operation to define its specific security. ![In this example, the Find Pets by tags method is secured using petstore_auth.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_security_2.png)
