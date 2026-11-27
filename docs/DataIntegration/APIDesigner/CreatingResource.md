---
title: "Creating a resource"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/CreatingResource.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design"]
---

# Creating a resource

A resource is an element that your consumers interact with through your
API.

1. Click Create new in the top-right corner.

   ![Create new menu expanded.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_the_menu_to_create_definition_elements_and_components.png)
2. Click Resource.
3. Enter a Path for your resource,
   `/contacts/` for example, and add a
   Name.

   Overriding servers at the resource level is not supported.
4. Optional: Select a Section and enter a
   Description
5. If you want to add a different security scheme than the whole API, in the
   Security section, select Customize security for
   this resource.
6. Select your security scheme(s).

   Information noteNote: Security schemes are defined in the
   Security section of your API.
