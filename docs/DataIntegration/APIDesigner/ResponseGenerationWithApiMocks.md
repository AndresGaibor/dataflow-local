---
title: "Response generation with API mocks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ResponseGenerationWithApiMocks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API mocks"]
---

# Response generation with API mocks

Once you have enabled an API mock, it is immediately available for use.

API mocks respond as realistically as possible to any calls they receive.
When generating a response body, a mock will give priority to user-provided data by looking for an example
field, then a default value, then an enum field. If one is found, it will be used as an example, otherwise a
JSON example will be generated based on the data type returned by the operation being called.

As an example, consider the Company data type definition shown below. It does not contain any user-provided examples.

![The Company data type definition with no examples.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/datatype.png)

When mocking is activated, a GET call made to the /company/{companyId} resource will return
an automatically generated JSON response based on the structure of the data type.

The mock has done a number of interesting things, including generating values for custom
response headers (e.g. x-my-custom-header), identifying arrays and creating appropriate
examples (e.g. tags property), and also identifying nested structures and generating values
for those too (e.g. address property).

API Contracts mocks support content
negotiation, so you can use the Accept request header to select which body should be returned
among several options (each potentially has its own example), therefore changing the examples
returned by the mock.

![Contact example.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/content-nego-example.png)

Information noteNote: The case of response header
names may be changed when calling an API mock. This should not break anything, since HTTP
header names are case-insensitive.
