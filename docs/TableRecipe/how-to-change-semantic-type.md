---
title: "How to change the data type of a column"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/how-to-change-semantic-type.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Working with table recipes"]
---

# How to change the data type of a column

When you add a dataset and create a table recipe, each column is automatically assigned a data type based on the data it contains.

The data type corresponds to the category (names, emails, phone numbers, etc) of the data. If the data type that has been applied on a column is not the desired one, you have the possibility to manually change it to one of the other predefined types or even a custom one, based on your own experience.

Let's take the example of a dataset containing client data, including the job title of your customers. You can see in the header of the Occupation column that the data type has only been recognized as Text (string). You are going to change the data type of the column so that it more accurately reflects the data

![A column with the text native type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_change_data_type_1.png)

To change the data type assigned to a column:

1. In the table, right-click the header of the Occupation column or click ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) to open the column menu.
2. Click Change type....
3. To change the type:

   - Start typing the name of the type that you think would be appropriate in the Search field.

     As you type, an auto-completion feature will suggest a list of available types for your data.
   - Select one of the suggestions, based on the matching percentage with your column.

   ![Selecting a semantic type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_change_data_type_2.png)
4. Click the Job Title type from the suggestions in this case.

   According to the statistics, this data type corresponds most closely to the values contained in the column.
5. Click Apply.

The column type is updated to Job Title, as you can see in the header of the Occupation column.

Every time that the data type of a column is modified, the column quality is calculated again

For more information on data types in Qlik Cloud, and how to manage and create custom types, see [Managing semantic types](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Managing-semantic-types.htm).
