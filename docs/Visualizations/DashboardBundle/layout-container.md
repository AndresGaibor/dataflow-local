---
title: "Layout container"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/layout-container.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects"]
---

# Layout container

Layout containers (Layout container) allow you to add [visualizations](#glossary-0 "Glossary term") in a limited space. You can also show or hide the visualizations inside the layout container based on conditions.

Information noteLayout container is included as a part of the Dashboard bundle. Dashboard bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

Layout container

![A layout container with a bar chart, line chart, and map. The bar chart is in the upper left, the line chart on the upper right, and the map chart across the bottom.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_layoutcontainer.png "Click to view full size")

Information noteContainers can only be added in the advanced edit mode.

A layout container can hold a range of visualizations while occupying a small amount of space on a sheet. When expanded to full sheet, each chart expands as well.

## When to use the layout container

The layout container is useful when you want to build a custom display containing multiple charts as a single unit. Unlike the container, which uses tabs to cycle through charts, the layout container is a space where you are free to customize your own layout of the charts in the layout container. As the layout container offers sheet-like arrangement of visualizations, you can functionally store multiple sheets within a sheet that can be expanded for more detail.

You can place visualizations on top of one another. You can use conditions in the layout container to control which visualizations display. For example, you could show visualizations based on:

- Which user is accessing the chart.
- The value of a variable.

As a best practice, be aware the more visualizations that are added to a container, the longer it can take to display visualizations. Too may objects in a layout container might overwhelm the user and make the application slower to render visualizations.

## Limitations

Layout containers have the following limitations:

- You cannot create a chart inside a layout container by dropping measures or dimensions on the container.
- You cannot add a tab container, trellis container, or layout container inside a layout container.
- Keyboard shortcuts are not supported for copying and pasting charts in a layout container.
- The visualization exploration menu is not available for charts that are located inside a tab container, layout container, or legacy container object.
- You cannot add a master visualization to a layout container by dragging it onto an existing object in the layout container. Instead, use the properties panel to add the master visualization to the layout container, or drag the master visualization onto a blank layout container.
- Visualizations within a layout container cannot be expanded to full screen individually.

## Learn more

- [*How I made this: Dynamic analysis with the layout container*](layout-container-example.htm)
