---
title: "Deploying an API definition to AWS API Gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/DeployingApiDefinitionToAwsApiGateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API Contracts Examples"]
---

# Deploying an API definition to AWS API Gateway

Use the API Contracts public
API to automatically update your API to AWS API Gateway.

This example explains how to import a new API definition or update an existing
one in AWS API Gateway from API Contracts.

![Diagram of the process where the API definition is fetched by the CI/CD pipeline from Qlik Talend Cloud and then pushed to the AWS API Gateway.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/amazon_api_gateway_6.png)

To do this, you must first fetch your API from Qlik Talend Cloud, then you
need to deploy it to AWS API Gateway using a command line script or a CI/CD pipeline.

The following procedures use AWS CLI, but you can also use the AWS API Gateway REST API.

For more information, see the following resources:

- [*Fetching an API definition for AWS API Gateway*](FetchingApiDefinitionForAwsApiGateway.htm)
- [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/index.html)
- [AWS API Gateway Developer Guide](https://docs.aws.amazon.com/en_en/apigateway/latest/developerguide/index.html)
- [AWS API Gateway REST API Reference](https://docs.aws.amazon.com/apigateway/api-reference/)
