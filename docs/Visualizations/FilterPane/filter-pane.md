---
title: "Filter pane"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/FilterPane/filter-pane.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Filter pane

You can add a filter pane to control what data that is shown in the [visualizations](#glossary-0 "Glossary term") on a [sheet](#glossary-1 "Glossary term"). A filter pane can filter the data of several [dimensions](#glossary-2 "Glossary term") at once.

For example, if you have a [chart](#glossary-3 "Glossary term") of sales over time, you can use a filter pane to limit the data in the chart to only show sales from a selected time period, from certain product categories, and from a certain region.

When a dimension is added, it is placed to the right of the previous dimensions, or below, depending on the available space. As long as there is enough space, the dimensions are displayed as expanded lists. If there is not enough space, the dimensions that were added first are turned into filter panes.

Selections have been made in the dimensions Year, Quarter, and Month.

![Filter pane with selections made.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_FilterPaneSelections.png "Click to view full size")

## When to use the filter pane

With filter panes, you can easily make several [selections](#glossary-4 "Glossary term") to define your data set exactly like you want it. With your well-defined data set, you can explore data of particular interest.

By using the selection menu options in the filter panes (select possible, select alternative, and select excluded), you can make adjustments to the data set and compare the results with the previous selection.

### Advantages

Filter panes are good for making selections and defining data sets. But they also show the relationship between different values, the associations. The green, white, and gray colors reflect the data associations that exist - and that do not exist. And by analyzing those associations, you can make new discoveries, for example, that a sales representative has too many customers, or that a region lacks a sales representative.

### Disadvantages

When the dimensions contain a very large amount of values, it may be hard to manage the data.

## Selections in filter panes

During analysis, you make selections in a filter pane listbox. Click a collapsed filter pane dimension to open a selection listbox.

When you make a selection, it is reflected in the small bars at the bottom of each filter pane dimension. Four states can be displayed in the bars: selected (green), possible (white), alternative (light gray), and excluded (dark gray). Locked values are indicated by a lock icon. The details of the selections are displayed in the selections bar, above the sheet. You can click an item to see the details and change your selection.

You can customize the selection behavior for each individual listbox in a filter pane. For more information, see [*Changing selection behavior*](create-filter-panes.htm#Changing).

Fields are filtered out from each dimension to be shown in the visualizations on the sheet.

![Filter pane with selections made.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_FilterPaneSelections.png "Click to view full size")

### Making selections in filter pane lists

When there is space enough in a filter pane, the dimension values are displayed in a listbox. In listboxes, you can click to select a single value or draw to select several values. On a touch device, you can two-finger-tap in the listbox to select a range of values.

Germany, Japan, and Nordic selected in the Region filter pane.

![Filter pane with three values selected.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_FilterPaneSelectionList.png "Click to view full size")

### The selections tool

The selections tool offers an option to get an overview of the fields and dimensions in an application. In the selections tool you can make selections in all the fields and dimensions in the application, regardless of whether they are used in the application or not.

During analysis, click ![Selections tool](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg) to open selections view.

### Selection locking and unlocking

In a filter pane, locked selections are indicated by a lock icon. You can lock and unlock selections in the selections bar above the sheet.

## Display limitations

### Responsive design

The filter pane has a responsive design and renders as many dimensions as possible. When space is limited, this could involve reducing the size of each dimension so that all dimensions are displayed.

Example:

The following image shows a filter pane while it is being edited. Only three out of five dimensions are displayed. There is an additional item below the displayed dimensions. When this is clicked, the remaining dimensions are listed.

Filter pane in edit mode.

![Filter pane in edit view.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_FilterPane-EditMode.png "Click to view full size")

When you have finished editing the filter pane and enter analysis mode, you will see the filter pane with all the dimensions displayed. If all items cannot be shown due to lack of space, click ![Down arrow](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) below the displayed dimensions to view the remaining dimensions.

Filter pane in analysis mode, with expanded drop down list showing additional dimensions.

![Filter pane in analysis mode with five dimensions. Three of the dimensions are displayed, with the dropdown expanded to show additional two dimensions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_FilterPane-AnalysisMode.png "Click to view full size")

### Full screen view

In full screen view, the filter pane is maximized and displays as many dimensions as possible expanded. When not all dimensions can be displayed expanded, the priority order is that the most recently added dimensions are expanded to the right. You can change the priority order in the properties panel, under Dimensions. Drag the dimensions to change the order.

### Mobile limitations

In the Qlik Analytics mobile application, the filter pane is a natively rendered visualization. Natively rendered visualizations have better performance compared to visualizations rendered in WebView. If a natively rendered visualization is wrapped inside a Container object, it will be rendered in an embedded WebView.

While natively rendered visualizations have greater performance, they do not support the full breadth of object styling (general styling or theme-based styling) when viewed in the Qlik Analytics mobile app. If styling of objects is important for mobile analysis, the application developer can place the object inside a Tab container, Container, or Layout container. This forces the WebView presentation and preserves styling.

## Keyboard navigation

You can use your keyboard to navigate a filter pane. Use the arrow keys or the Tab key to alternate between the different objects on the sheet. Once you have moved the focus to the filter pane, use the Enter, Space and Esc keys to move the focus between the following levels:

- Entire filter pane
- Listboxes inside the filter pane
- Values inside each listbox

Keyboard controls in filter panes

| Keyboard navigation | Description |
| --- | --- |
| Space or Enter | Moves focus to the first listbox in the filter pane. Another key press brings the focus to the first value inside that listbox.  If the focus is on a collapsed listbox, press Enter to open the listbox in a pop-over. |
| Esc | Moves focus back one level (from the values to the listbox to the filter pane object). |
| Right arrow | If the focus is on an individual listbox within the filter pane, the right arrow key moves the focus to the next listbox on the right.  If the focus is on a value inside a listbox, the right arrow key moves to the next value in the listbox. |
| Left arrow | If the focus is on an individual listbox within the filter pane, the left arrow key moves the focus to the next listbox on the left.  If the focus is on a value inside a listbox, the left arrow keymoves to the previous value in the listbox. |
| Up arrow | If the focus is on an individual listbox within the filter pane, the up arrow key moves the focus to the previous listbox (to the left, or above, the current listbox).  If the focus is on a value inside a listbox, the up arrow key moves to the previous value in the listbox. |
| Down arrow | If the focus is on an individual listbox within the filter pane, the down arrow key moves the focus to the next listbox (to the right, or below, the current listbox).  If the focus is on a value inside a listbox, the down arrow key moves to the next value in the listbox. |

For more information about keyboard navigation, see [*Keyboard navigation and shortcuts in apps*](../../UserInterface/keyboard-navigation-and-shortcuts.htm).

## Learn more

- [*Creating filter panes*](create-filter-panes.htm)
- [*Exploring with selections*](../../Selections/SelectionsToolbar/work-with-selections.htm)
- [Interpreting Filter Panes](/lnk/Interpreting_filter_panes)

Related learning:

- [Interpreting Filter Panes](/lnk/Interpreting_filter_panes)
