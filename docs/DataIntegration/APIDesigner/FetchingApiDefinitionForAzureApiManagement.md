---
title: "Fetching an API definition for Azure API Management"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/FetchingApiDefinitionForAzureApiManagement.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API Contracts Examples", "Deploying an API definition to Azure API Management"]
---

# Fetching an API definition for Azure API Management

Export an API definition as a JSON file compatible with Azure API Management from
API Contracts.

- You have installed cURL. For more information, see the [cURL documentation](https://curl.haxx.se/docs/).
- You have created an API in API Contracts.

1. Open a command line and enter the following command to export
   your API definition:

   ```
   curl --header "Authorization:Bearer {userToken}" -X GET -o {outFile}.json https://apid.{region}.cloud.talend.com/api/v1/api-definitions/{api-id}?format=Swagger20Azure
   ```
2. Add the correct parameters:

   | Parameter | Description |
   | --- | --- |
   | {userToken} | Token generated from Qlik Talend Cloud. |
   | {outFile} | Path and filename of your API definition. For example: contactsapi.json |
   | {region} | Region for your Qlik Talend Cloud account. The value can be: - us-west - us - eu - ap - au For more information, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-windows/Cloud/talend-cloud-application-url). |
   | {api-id} | ID of the API version to fetch. To get it, open your API in API Contracts and go to Settings > MANAGEMENT API or use the GET method on the /api-definitions endpoint to get a list of API definitions with their IDs. |
3. Execute the command.

Your API definition is exported as a JSON
file compatible with Azure API Management and saved in the selected directory.
