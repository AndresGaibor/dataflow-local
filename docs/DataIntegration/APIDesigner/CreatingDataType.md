---
title: "Creating a data type"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/CreatingDataType.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design"]
---

# Creating a data type

A data type is a description of the data that is exchanged over the
network. It can be reused throughout the API version.

1. Click Create new in the top-right corner.

   ![Create new menu expanded.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/shows_the_menu_to_create_definition_elements_and_components.png)
2. Click Data type.
3. Enter a Name for your data type,
   `Contact` for example.

   The type is object by default.
4. Optional: Enter a Description and select the
   Section in which you want to include the data type.
5. Click Edit next to your newly created data type to edit the
   type or add a description and examples.

   ![Screenshot of the object type.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/creating_data_type_2.png)

   Information noteNote: Only the object type supports properties. Types such
   as string or integer do not support
   adding properties.
6. Click Save.
7. Optional: If the type is object, click Add
   property.
   1. Enter a Name and select a Type
      for your property.
   2. Fill in the fields that appear. The available fields depend on the selected
      type.
   3. Click Add.

   Define the `firstName` property as a required property of
   type `string`, described as `Customer's first
   name`.![Example of how to define the firstName property, which is a required property of type String and described as "Customer's first name".](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/creating_data_type_03.png)

   You can add as many properties as needed to an object
   data type.
