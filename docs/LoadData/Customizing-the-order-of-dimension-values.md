---
title: "Customizing the order of dimension values"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Customizing-the-order-of-dimension-values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Customizing the order of dimension values

Custom ordering enables you to set the order of [dimension](#glossary-0 "Glossary term") values in [visualizations](#glossary-1 "Glossary term").

While alphabetical or numerical order may work for many visualizations, in some instances, an alternative order is useful. For example, in a field containing cities, you could set a custom order so that in your charts cities are listed in order of east to west. You can define custom ordering for fields that meet the following requirements:

- Fields must be set as dimensions in the Summary card.
- Fields must contain up to a maximum of 5,000 distinct values.

  It is recommended that your [field](#glossary-2 "Glossary term") have up to a maximum of 25 values, but you can choose to use the Order card with fields containing up to 5,000 distinct values.

The Order card consist of two sections: Current Order and Preview of order. Current Order displays all the distinct values from the dimension. By default, the distinct values are organized by load order. You set your custom order by dragging the values in Current Order into the desired order. Preview of order is a bar chart that displays a count of values in each distinct value, organized by the current order.

A custom order overrides all other sorting options available in Qlik Sense visualizations except for sorting by load order. If you require alphabetical or numeric ordering for this field, you must remove the custom order by resetting the order.

## Changing the order of values in a dimension field

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Select a dimension field.
3. In the data profiling card, click the Order tab.
4. Click and drag the values into the new order.
5. If you want to cancel your current ordering, click Cancel.

   Information note

   Cancel is only available to new custom orders. To cancel your changes if you are changing the order of values in an existing custom order, select a different field in the table and then select this field again.
6. Click Reorder.

## Resetting the order of values in a dimension field

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Select a reordered dimension field.
3. In the data profiling card, click the Order tab.
4. Click Reset.
5. Click OK.

Related learning:

- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
- [How do I create custom sort orders?](/lnk/How_create_custom_sort_orders)
