---
title: "Working with API gateways"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/WorkingWithApiGateways.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# Working with API gateways

Export your API definition to use it with an API gateway.

After designing your API, you may need to publish it to an API gateway in order to handle
issues such as authentication, monitoring, and logging. To do so, you can export your API
definition and import it into any API gateway.

For AWS API Gateway and Azure API Management, API Contracts offers
an API gateway compatibility mode which helps you avoid compatibility issues.

Information noteTip: You can also export your API definition for other API gateways using the
Standard OAS export. This export should be compatible with
many API gateways, such as Apigee.

If you export your API in one of the compatibility modes, API Contracts informs you of the elements in your
API that might not be supported in the gateway. There are three possible levels of messages:

- Information: there is a compatibility issue but the definition is exported without
  alterations and you will be able to import it to the gateway.
- Warning: there is a compatibility issue and the definition is modified in order to be
  imported successfully to the gateway.
- Error: there is a compatibility issue which will prevent you from importing the
  definition to the gateway.

The messages are displayed in the bottom right corner of the window.![Message examples.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/api_gateway_compatibility_messages.png)

For more information about AWS API Gateway limitations, see [AWS API Gateway Known Issues](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-known-issues.html).

For more information about Azure API Management restrictions, see the [API import restrictions and known issues](https://docs.microsoft.com/en-us/azure/api-management/api-management-api-import-restrictions).
