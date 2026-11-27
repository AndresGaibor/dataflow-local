---
title: "Exporting a definition for an API gateway"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/ExportingApiDefinitionForApiGateway.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "Working with API gateways"]
---

# Exporting a definition for an API gateway

Export an API definition compatible with AWS API Gateway or Azure API Management.

1. Open the API version that you want to export.
2. Click Export.
3. Click OpenAPI Specification and select AWS API Gateway or Azure API Management.

   If you want to export your API for another gateway, Apigee for example, it is
   recommended to select Standard OAS.![Select a specification menu.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/api-definition-specification.png)
4. Select the OAS version and format.

   Since Talend
   extensions are not supported by API gateways, No extensions is
   selected by default and cannot be modified.![Customize menu.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/designer_export_gateway.png)
5. If you do not want to export your entire API, click Filter export and select the operations that you want to export.

   When you filter your export, all data types, components, and resources are
   exported, regardless of the operations you selected.

   Information noteNote:

   Resources are exported even if they contain no operations or if their operations are filtered out. For example, in the image below, all operations in the /contact/{contactid} resource are filtered out, but the path still appears in the exported file:

   ```
   "/contacts/{contactid}" : {
         "parameters" : [ {
           "$ref" : "#/components/parameters/contactid"
         } ]
       }
   ```

   AWS API Gateway shows a warning when importing a file containing paths with no operations, but it does not prevent the import.

   ![Select operations options.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/api-definition-operations.png)
6. Click Export.
