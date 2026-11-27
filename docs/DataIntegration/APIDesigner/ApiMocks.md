---
title: "API mocks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ApiMocks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# API mocks

There are two main use cases for API mocks in API Contracts:
prototyping, and parallel frontend and backend implementation.

## API prototyping

The first use case for API mocks is API prototyping.
The idea here is that once you have completed an iteration of your API design, you want to get
feedback from different stakeholders in the API project: team members, developers who will consume
the API, product owners, etc.

If stakeholders can actually interact with the API design, you are
more likely to obtain better feedback and faster, as the experience of reviewing the API is more immersive
and realistic.

## Parallel frontend and backend implementation

In many projects, once the API
design phase is complete, there will be both backend code that needs to be written to implement the API,
and frontend code that will consume the API.

Once the API contract is settled upon, there is no
real reason for the frontend developers to wait until backend developers are finished before starting.
Proceeding in such a linear fashion will increase time to market and slow down feedback cycles between
backend and frontend teams during development.

Having an API mock that is up to date with the latest API contract design enables frontend and
backend teams to work in parallel.

## Content negotiation

The only dynamism provided by the mocks is content negotiation. If you have multiple bodies
defined in the API, and you make a request with a compatible media type in your
Accept header, the mock uses this body to create the response.

## Testing a mock

You can test your mock using any API client, such as API Tester, Postman, or cURL, by sending requests to the mock endpoint URL displayed in API Contracts.
