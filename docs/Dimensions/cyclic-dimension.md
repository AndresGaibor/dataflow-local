---
title: "Cyclic dimensions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Dimensions/cyclic-dimension.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Data grouping with dimensions"]
---

# Cyclic dimensions

Group non-hierarchical fields together as a master dimension so they can be cycled through in a visualization.

Cyclic dimensions allow users to quickly change between fields displayed as dimensions in visualizations. Users can cycle through the fields in the cyclic dimension using a button. Unlike drill-down dimensions, fields grouped in a cyclic dimension do not need a hierarchical relationship. Their only relationship is that they are all of interest with similar measures in a chart.

When a cyclic dimension is used as a visualization dimension, the visualization will use the first dimension in the list. Users can switch to the next dimension in the order they appear in the cyclic dimension's list. If you are using a cyclic dimension in multiple visualizations, all the fields in each visualization using the cyclic dimension will change when you switch to the next field.

You can switch dimension by:

- Clicking ![Cycle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg) in the visualization.

  You can also select a specific field from the cyclic dimension by clicking on the field name label in the axis.
- Clicking a button with the action Step cyclic dimension.

  For more information, see [*Setting the action*](../Visualizations/Button/create-buttons.htm#Setting).

Chart using a cyclic dimension

![Visualization with cyclic dimension, displaying the first dimension in the cycle.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_cyclic_dimension.png "Click to view full size")

## Limitations

Cyclic dimensions have the following limitations:

- The cycle button (![Cycle](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg)) is only available in the following visualizations:

  - Bar charts
  - Bullet charts
  - Combo charts
  - Grid charts
  - Line charts
  - Pie charts
- The Qlik Analytics mobile app has the following limitations with cyclic dimensions:

  - Buttons with the action Step cyclic dimension will only cycle dimension if the button is in a container.
  - In offline mode, buttons with the action Step cyclic dimension do not cycle the dimension.
  - In offline mode, any visualization with a cyclic dimension will only display the first dimension in the cycle. The cyclic dimension cannot be cycled.
- Custom objects may not work with cyclic dimensions.
- Cyclic dimensions are not supported with the following Qlik Dashboard bundle objects:

  - Date picker
  - Line
  - Text
  - Variable input
  - Video player
- Cyclic dimensions are not supported with the following Qlik Visualization bundle objects:

  - Trellis container
- Cyclic dimensions do not support assigning colors to dimension values
- In the storytelling view, while snapshots display correctly, clicking Go to source will not apply the cyclic dimension state from the snapshot.
- If a field is removed from the data model but not from a cyclic dimension, the cyclic dimension will continue to work until it steps to the removed field.
- When navigating back to a visualization containing a cyclic dimension from charts monitored in [activity centers](#glossary-0 "Glossary term"), subscriptions, or data storytelling, the chart will use the default starting field in the cyclic dimension.

  If you already have the application open, then it will use the current field in the cyclic dimension.

## Learn more

- [*Creating a cyclic dimension*](create-cyclic-dimension.htm)
- [Creating cyclic dimensions](https://share.vidyard.com/watch/psEU44Jiau7KJXKx1jMJW6)
