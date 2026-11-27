---
title: "Creating an operation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/CreatingOperation.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design"]
---

# Creating an operation

An operation is the action that can be performed on your resources.

1. Click Create new in the top-right corner.

   Information noteTip: If you want to create your operation directly in a previously
   created section, you can do so by clicking the + button to
   the right of the section name. If you have already created a resource, you can
   click the + button to the right of the resource path to
   create an operation for this resource.

   ![Create new menu expanded.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_the_menu_to_create_definition_elements_and_components.png)
2. Click Operation, or click the type of operation, for
   example GET if you are creating it in an existing
   resource.

   If you create an operation in an existing resource, the method
   and the path of the operation are filled automatically.
3. Enter a Name for your operation, `Get list of
   contacts` for example.
4. Select the Method and enter a
   Path.

   If you enter a path that does not match an existing resource, a new resource will
   be created.![Example of creating a GET method called "Get list of contacts" with the /contacts/ path.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/creating_operation_01.png)
5. Optional: Enter a Description.
6. Optional: Enter Tags and an Id.
7. If you want to add a different security scheme than the whole API, in the
   Security section, select Customize security for
   this resource.
8. Select your security scheme(s).

   Information noteNote: Security schemes are defined in the
   Security section of your API.
9. Optional: Add Request and Responses
   parameters.

   Reusable request bodies are not supported.
