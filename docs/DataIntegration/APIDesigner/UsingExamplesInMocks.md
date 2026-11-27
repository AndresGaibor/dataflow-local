---
title: "Using examples"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/UsingExamplesInMocks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API mocks", "Response generation with API mocks"]
---

# Using examples

Add sample data in example fields throughout your API.

In API Contracts, you can add example values for various elements
of your API. Once you have defined an example, it is used when making API calls to your
mock.

In the following example, a data type was created using an example.

![Screenshot of the Character data type that was generated from a JSON example.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_a_example_used_in_a_data_type.png)

This data type is then used as a response body for an operation.

![The Character data type is returned for the method called Get a Star Wars character by ID.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_a_data_type_used_in_an_operation_response.png)

You can define examples in different parts of your API, and some might override the others when
making calls to your mock. Here, the example from the data type is used, but you can
also define an example for the operation's response.

![A new example is defined for the response. Here the character is Leia Organa.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_an_operation_response_using_a_data_type_and_an_added_example.png)

External examples are not supported.
