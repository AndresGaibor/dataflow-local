---
title: "Creating insight triggers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/insight-triggers-create.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Discovery Agent", "Working with Discovery Agent insight triggers"]
---

# Creating insight triggers

You can create an [insight trigger](#glossary-0 "Glossary term") when editing or analyzing a sheet.

## Creating an insight trigger

Do the following:

1. In sheet view in an application, do any of the following:

   - Expand the Assets panel and click ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Insight triggers, then click Create insight trigger group.
   - Right-click a visualization and select ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Create insight trigger.
   - Right-click a master measure in the Assets panel and select ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Create insight trigger.

   Information note

   You create groups of insight triggers to collect related metrics together. A group is created by default even if you are creating a single insight trigger.

   Creating insight triggers

   ![Creating insight triggers in the 'Create insight trigger group' dialog](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-insight-triggers-configure.png "Click to view full size")
2. Optionally, update the Group properties with a name and description.
3. As needed, expand Show shared properties to set other group properties. Insight triggers in the group will inherit these group properties, unless you change the individual insight trigger properties.

   - Time dimension: Select a dimension containing the date and time information on which you want to track data trends.
   - Time periods: Select one or more time periods on which the data is aggregated. The setting defaults to using all time periods.
   - Breakdown dimensions: Set specific fields and values to use when calculating insights.

     Follow these guidelines to add filters to a breakdown dimension:

     - Click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a filter, and select a field.
     - After adding a field, click it to select the values to use. To calculate insights individually for the first 50 values in the dimension, do not select any values.
     - Click ![Remove](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cross.svg) to remove filters.

   You can also configure these properties after adding insight triggers to the group.
4. Click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg)  Add insight trigger.
5. In the Measure drop down menu, select a master measure, or define a field-based aggregation, that contains the calculation you want to monitor.

   For example, Sum(Sales).
6. Configure the rest of the General settings:

   - Name: Define a custom name for the insight trigger.
   - Value going up is: Define the underlying meaning behind increasing values across the Measure.

     This depends on your application data and use case. For example, an increase to total sales is positive and an increase to total cost of sales is negative.
   - Time dimension: Select the date and time dimension on which you want to track trends.
   - Time periods: Select one or more time periods on which the data is aggregated.

     Use the Inherit from group option to use the setting defined in the Shared insight trigger properties.
   - Breakdown dimensions: Select a dimension containing the date and time information on which you want to track data updates.

     For more information, see [*Breakdown dimensions*](insight-triggers.htm#Breakdown).

   Tip noteAfter adjusting properties, you can click ![View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_view_outline.svg) to preview the current data in the application. This helps to understand whether you have configured your measure and dimensions as intended.
7. If desired, switch to Optional settings to configure some additional settings:

   - Offset: Specify a number of days by which to delay insight calculation. This can help if there are delays in your data collection process—for example, a database does not sync with the sales for a date until a processing period of one week.
   - Insight types: Select the insight types to evaluate. If you do not select anything, insights are calculated based on all insight types.

     For a description of each insight type, see [*Insight types*](insight-triggers.htm#Types).
   - Bookmarks: Specify a [bookmark](#glossary-1 "Glossary term") from the application to apply a [selection](#glossary-2 "Glossary term") state to the trigger before calculations are done. This allows custom, dynamic filtering of data used to calculate insights.
   - Link to sheet: Link to a [sheet](#glossary-3 "Glossary term") in the application.
8. When ready for insights to start being generated from the trigger, set the Status to Active.
9. Click Create.

After creating the insight trigger, you can manage it and change its properties. For more information, see [*Managing insight triggers*](insight-triggers-manage.htm).

## Permissions

For more information about permissions for creating insight triggers, see [*Discovery Agent permissions*](discovery-agent-admin.htm#Permissions).

## Learn more

- [*Working with Discovery Agent insight triggers*](insight-triggers.htm)
- [*Managing insight triggers*](insight-triggers-manage.htm)
- [*Analyzing Discovery Agent feeds*](feeds.htm)
- [*Navigating insights in feeds*](feeds-navigate.htm)
