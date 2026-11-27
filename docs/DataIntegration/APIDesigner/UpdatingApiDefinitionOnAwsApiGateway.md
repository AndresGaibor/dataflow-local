---
title: "Updating an API definition on AWS API Gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/UpdatingApiDefinitionOnAwsApiGateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API Contracts Examples", "Deploying an API definition to AWS API Gateway"]
---

# Updating an API definition on AWS API Gateway

Import a JSON file to AWS API Gateway to update an existing
definition.

- You have access to AWS API Gateway.
- You have installed AWS CLI. For more information, see [Installing the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).
- You have exported your API definition as a JSON file.
- You have uploaded a previous version of the API definition to AWS API
  Gateway.

1. Open a command line and enter the following command to upload the file:

   ```
   aws apigateway put-rest-api --rest-api-id {api-id} --mode {mode} --body 'file://{yourfile}.json'
   ```
2. Add the correct parameters:

   | Parameter | Description |
   | --- | --- |
   | {api-id} | AWS API Gateway ID of the API to update. |
   | {mode} | Behavior at import. The value can be either overwrite to replace the previous version of the API with the new one, or merge to merge the two versions. |
   | {yourfile} | Path and file name of the API definition you exported. |
3. Execute the command.

Your API definition is merged or overwritten, depending on the mode you defined. You can check
your update on the AWS API Gateway console.

In this example, a first version of the API definition containing only the
/contacts resource and its operations was uploaded. Then, a
second version with the /companies resource was uploaded and merged
with the previous version.

![Screenshot of the merged API definition.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/aws_2.png)

For more information about the put-rest-api command, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-rest-api.html).
