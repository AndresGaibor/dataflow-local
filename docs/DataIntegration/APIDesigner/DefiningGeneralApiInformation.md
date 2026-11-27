---
title: "Defining general API information"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/DefiningGeneralApiInformation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design"]
---

# Defining general API information

Edit general information about your API version and define its media types, server
URLs, and security schemes.

1. Access the general information page of your API.

   This page opens automatically after creating your API. You can also open it by
   clicking the name of your API at the top of the left panel.
2. In the General section, edit the version, description,
   contact information, license details, and terms of service for your API.

   Information noteNote: The name of your API can be changed from the API Contracts
   homepage. For more information, see [*Working with a new API*](WorkingWithNewApi.htm).

   ![General section of the Petstore API.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/defining_general_info_01_general.png)
3. Edit the Media types section to add or remove media
   types.

   The media types defined in this section are global, they are applied to the whole
   API version. They can also be defined at the operation level.
4. Add your server URLs in the Server URLs section.

   The server URLs defined in this section are global, they are applied to the whole
   API version. Once they are defined, your server URLs appear below the name of your
   API in the top of the left panel, along with the mock endpoint if it is enabled.

   Published server URLs are visible in the live documentation.
   Server URLs that are not
   published are only visible in API Contracts.
5. Define the security for the API in the Global security and
   Security schemes sections.

   The security defined in this section is global, it is applied to the entire API
   version. It can also be defined at the resource and operation levels.
