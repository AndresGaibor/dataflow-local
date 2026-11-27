---
title: "Discovering your data with associative insights"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/associative-insights.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections"]
---

# Discovering your data with associative insights

Associative insights reveals relationships in your data. The Qlik cognitive engine searches your data model for excluded values in a subset of fields. It then highlights those values, so you can explore them.

You can compare the contributions of your selections and excluded values against your measures. In any data set, particularly in complex ones, this can help you uncover blind spots and reveal relationships that you may have missed.

For a visual demo and practical example about discovering your data with associative insights, see the following:

- [Discovering your data with associative insights](https://share.vidyard.com/watch/mAQMxC7TMASxeRYjngcCF4?)
- [Qlik associative insights - A simple yet practical example](https://share.vidyard.com/watch/dgVzf4SAqaAp351MhtK2Yx?)

## Limitations

Application consumers with the appropriate access rights for an application can use associative insights. They must connect to a Qlik Sense Enterprise or Qlik Core server. They cannot:

- Use the Alternate states feature. See: [*Using alternate states for comparative analysis*](../Visualizations/alternate-states-comparative-analysis.htm).
- Set Always one selected value for a field in an application. See: [*Always one selected value*](../DataSource/select-single-value.htm).
- Lock their selections. See: [*Locking and unlocking selections*](SelectionsToolbar/lock-unlock-selections.htm).

## Associative insights selections view

When generating insights, Qlik Sense looks at your selections and analyzes the excluded values in your data model. It then highlights data that may be of interest for further exploration. That data is displayed in cards, which can be clicked to provide a more detailed view.

Associative insights selections view.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_card_cloud-rev.png "Associative insights selections view ")

### Selections

Your currently applied selection or selections. The top list box shows data associated with your current selection. The other list boxes show data excluded from your current selection.

Selections card in associative insights.

![Selections pane in associative insights](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associative_insights_selections.png "Click to view full size")

### Application dimensions

The selections that are available to you. By default, only master items are displayed. Select Show fields to show all fields.

Application dimensions in associative insights.

![App dimensions in associative insights](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associative_insights_app_dimensions.png "Click to view full size")

### Measure

The measure that Qlik Sense has selected for insights. You can change the measure in the drop-down menu.

Application dimensions in associative insights.

![App dimensions in associative insights](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associative_insights_app_dimensions.png "Click to view full size")

### Included values

This card represents included values.

Values included in associative insights.

![Values included in associative insights](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associative_insights_incl_values.png "Click to view full size")

### Insights from excluded values

Insight cards show the impact of the excluded value on your measure. In this case, it shows that one employee (EmployeeName), who is not in Canada (CAN), contributed 37.8% of yearly sales (YearlySales). Purple indicates an insight. Click on a card to reveal the insights details view.

Insights from excluded values in associative insights.

![Insights from excluded values in associative insights](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_excl_values.png "Click to view full size")

### Add a dimension drop-down

You can use this drop-down to add cards to the Insights from excluded values section.

Add dimensions drop-down.

![Drop-down allowing user to add dimensions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associative_insights_add_dimension.png "Click to view full size")

## Insights card details view

Details view will display a detailed chart if you have a simple sum() measure.

Associative insights card details view.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_expanded-rev.png "Associative insights details view ")

### Details view

A detailed view of the currently selected card. Click the chart to see the data in a table. Purple indicates an insight.

Details view for currently selected card.

![Card view in associative insights.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_card.png "Click to view full size")

### Measure and included values

You can use the drop-down to change the current measure. The card beneath it represents included values.

Measure selection and included values.

![Measure selection and included values.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_measure_incl_values.png "Click to view full size")

### Insights from excluded values

These cards represent excluded values. You can click them to change the chart in details view.

Add dimensions drop-down.

![Card view in associative insights.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_measure_incl_values.png "Click to view full size")

### Currently selected dimension card

The dimension you have currently selected will have a dark border around it.

The currently selected card.

![Currently selected card, with border around it.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_currently_selected.png "Click to view full size")

### Analyzed - no insights

These values have been analyzed, but have no interesting insights.

List of cards with no available insights.

![List of items with no insights available.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_no_insights.png "Click to view full size")

### Add a dimension drop-down

You can use this drop-down to add cards to the Insights from excluded values section.

Drop-down menu for adding dimension.

![Drop-down for adding a dimension.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_dimension_dropdown.png "Click to view full size")

## Insights card KPI view

Details view will display a KPI chart under two conditions:

- Measure aggregation is other than sum().
- Measure aggregation is sum(), but the data model is not appropriate for standard stacked charts.

Associative insights card details KPI layout.

![Insight advisor card KPI view ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_kpi_view-rev.png "Click to view full size")

## Generating insights

Do the following:

1. In a sheet in your application, click Selections. The Selections window opens. The window contains the Associative insights panel.
2. Select a value in App dimensions.

   By default, only master items are displayed. Select Show fields to show all fields. You can then select a value from the fields that are shown. For more information, see [*Using the selections tool*](use-selection-tool.htm).
3. Click Generate insights.
4. Cards are shown in the right hand panel. The cards show the effect of your selection on dimensions and measures in your data.
5. You can change which measure is assessed. Choose a new measure from the Measure drop-down menu.
6. Click a card to see more information about your associative insight.

You can make or change you selections in the Associative insights window at any time. Make your selections and then click Refresh. The cards will be updated based on your new selections.

## Associative insights example: No data left behind

In this example, we use a simple data set to uncover an insight.

[Sample data - Associative insights](/en-US/cloud-services/tutorials/AssociativeInsightsData.zip)

Do the following:

1. Here is a view of our application with the Selections window open. We have selected CAN in the Country field. US is colored light gray because it is an alternate selection. The values in the EmployeeID, EmployeeName, and YearlySales fields are white because they are possible values. In other words, they are associated with our selection of CAN.

   Associative insights with Generate insights button

   ![The Generate insights button.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_generate-rev.png "Click to view full size")
2. When we click Generate insights, Qlik Sense selects interesting data to show in the associative insights cards. We see that CAN contributes 62.2% to our yearly sales. We also see in the bottom card that one of our employees (or 5% of all EmployeName) is excluded from this selection. This employee contributes 37.8% to our yearly sales. Purple indicates an insight.

   Associative insights with one selection

   ![Associative insights with one selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_cards-rev.png "Click to view full size")
3. When we click on card, Qlik Sense shows us a detailed view of the data. It shows how much this excluded employee contributed to yearly sales. Who is this employee? We know they are excluded from our selection of CAN. Click Reveal data for the excluded values.

   Associative insights with detailed view

   ![Associative insights card detailed view.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_detailed-rev.png "Click to view full size")
4. We now see a table showing information about Kasie, the excluded value from the EmployeeName field. Click Select excluded to apply Kasie as a selection.

   Associative insights with detailed view of excluded values

   ![Associative insights card detailed view after clicking Reveal data for the excluded values.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_detailed_excl-rev.png "Click to view full size")
5. We are brought back to the Selections window. Kasie is selected. Values in our former selection of CAN are colored dark gray, because they are now excluded.

   Click Explore selections, and then Generate insights.

   Associative insights with previously excluded values included

   ![Associative insights with previously excluded values included.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_associate_insights_kasie-rev.png "Click to view full size")
6. Click the EmployeeName card, and you will see an updated insight card details view.

   Associative insights with Kasie as selected value

   ![Detailed view showing Kasie as selected value.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_insights_card_selected-rev.png "Click to view full size")

## Disabling associative insights in an application

Associative insights can be disabled in an application by adding a variable and then refreshing the application.

Do the following:

1. In the sheet edit mode, in the assets panel, click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg).
2. Click Create new.
3. In Name, type DISABLE\_SELECTION\_INSIGHTS.
4. In Definition, type any value.
5. Click Close.
6. Refresh the application.

## Troubleshooting associative insights

### I cannot see associative insights

Possible cause

A script variable is disabling this feature.

Proposed action

Contact your administrator.

### Insights are not available

Possible cause

Qlik Sense is offline or not connected to a Qlik Sense server.

Proposed action

Verify that you are online. Log into your Qlik Sense server and try again. If this does not solve the problem, there might be an issue with engine.

### I am missing fields under My dimensions

Possible cause

You can only see master dimensions, because Show fields is not selected

Proposed action

On the Selections screen, select Show fields.

## Learn more

- [*The associative selection model*](associative-selection-model.htm)
- [*Using the selections tool*](use-selection-tool.htm)
- [*Exploring with selections*](SelectionsToolbar/work-with-selections.htm)
