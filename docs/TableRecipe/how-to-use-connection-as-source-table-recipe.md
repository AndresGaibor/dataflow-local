---
title: "How to use data from a connection as source for a table recipe"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/how-to-use-connection-as-source-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Working with table recipes"]
---

# How to use data from a connection as source for a table recipe

You can use file based datasets from your catalog as source for your table recipes. If your data is stored in a connection, you can still use it by using one of the two following methods.

## Creating a dataset from a connection

If your data is stored in a connection, you can use it to create new datasets. For information about adding datasets from files, see [*Adding datasets*](../DataSource/add-datasets.htm).

1. From the launcher menu, select Analytics > Create or Analytics > Prepare data.
2. Click Create new > Dataset.

   ![Creating a new dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_how_to_use data_from_connection_1.png)
3. In the menu that opens, select the connection where your data is stored and click Next.
4. Browse your connection, select one or more tables to import as datasets using the check boxes, and click Next.

   If you select multiple tables, each one will be turned into a different dataset.
5. Select the space in which to create the datasets, and click Create datasets.

Your new datasets, with data originating from a connection, are added to your catalog and can be easily selected when setting a source in your table recipe.

## Using a connection type source in a data flow

Another way to use table recipe to prepare data stored in a connection is to use the native support of connections as sources in a data flow, and then use the [*Table recipe processor*](../DataFlow/data-flow-processor-table-recipe.htm) in your flow. For more information on how to use Data flow, see [*Building a data flow*](../DataFlow/Creating-data-flow.htm).

1. Create a new data flow.
2. Use the connection where your data is stored as source for the flow.
3. Add a Table recipe to the canvas.
4. Add a target to configure the output of the recipe.
5. Link the different nodes together to create a flow.

   ![A flow to use a table recipe on data stored in a connection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_how_to_use data_from_connection_2.png)
6. Click the Table recipe processor and in the configuration panel on the right, select the Edit table recipe icon.

   The embedded version of Table recipe opens and you can start preparing your table.

   ![The embedded version of Table recipe in a data flow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TableRecipe/table_recipe_how_to_use data_from_connection_3.png)
7. When your recipe is ready, click Return to data flow.
8. Check that the flow is valid, and click Run flow to apply the recipe to the data and generate your output.
