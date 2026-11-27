---
title: "Using combinations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/UsingCombinations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design", "Creating a data type"]
---

# Using combinations

Create a data type based on a combination of other data types.

1. Click Create new in the top-right corner.

   ![Create new menu expanded.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_the_menu_to_create_definition_elements_and_components.png)
2. Click Data type.
3. Enter a Name for your data type, `Dog`
   for example.
4. To add your properties manually, click Edit next to your
   newly created data type.
5. In Type, select one of the available combinations:
   allOf, oneOf, or anyOf.

   The not combination is not supported.
6. In Data types, add as many data types as necessary.
7. Optional: You can add examples and other properties.
8. Click Save.

   In this example, the `Dog` data types contains all the
   properties contained in the `Pet` data type, as well as some
   properties specific to dogs. ![The Dog data type is of type allOf with the value Pet, and it also has the bark and breed properties that are specific to dogs.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_a_data_type_using_all_of_combination.png)
