---
title: "Defining a security scheme compatible with AWS API Gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/DefiningSecuritySchemeForAwsApiGateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with API gateways"]
---

# Defining a security scheme compatible with AWS API Gateway

When exporting a definition from API Contracts and
importing it into AWS API Gateway, your security can be propagated if it is defined
properly.

1. Open your API and go to the general information page.
2. Go to the Security schemes section and click
   Add.
3. Enter a name.
4. In the Type drop-down list, select Custom / API
   key.
5. Click Add header in the Headers
   section.
6. In the Name field, enter
   `x-api-key`.
7. In the Type field, select
   string.
8. Click Add.

You have defined a security scheme which is compatible with AWS API Gateway. You can
use it globally or on the resource or operation level.![Security scheme example called AWS API Gateway, with the type Custom / API key and a string header.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_how_to_define_a_security_scheme_compatible_with_AWS_API_Gateway.png)
