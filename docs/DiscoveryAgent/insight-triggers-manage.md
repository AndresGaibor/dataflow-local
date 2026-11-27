---
title: "Managing insight triggers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/insight-triggers-manage.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Discovery Agent", "Working with Discovery Agent insight triggers"]
---

# Managing insight triggers

In sheet view in an application, you can manage insight triggers in the assets panel.

## Editing an insight trigger group

If the group contains no active insight triggers yet, click Continue editing.

You can also edit and rename insight triggers and their groups, doing any of the following:

- Adding and removing insight triggers in the group
- Modifying group and insight trigger properties
- Activating and deactivating insight triggers

Do the following:

1. Open ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Insight triggers in the Assets panel.
2. Click ![Bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a group or active insight trigger.
3. Select Edit, Rename, or Rename group.

   Editing an insight trigger group

   ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-insight-triggers-edit.png "Click to view full size")
4. Update the properties for the insight trigger or insight trigger group. For information about these properties, see [*Creating an insight trigger*](insight-triggers-create.htm#CreateInsightTrigger).

## Deleting an insight trigger

You can delete insight triggers or groups of insight triggers.

When you delete an insight trigger, insights related to that trigger will be removed from feeds.

Do the following:

1. Open ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Insight triggers in the Assets panel.
2. Next to an insight trigger group or active insight trigger, click ![Bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Delete group or Delete.

To delete an inactive insight trigger, [edit the insight trigger](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/insight-triggers-manage.htm#Edit) and then click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin2.svg) next to it.

## Duplicating an insight trigger group

Do the following:

1. Open ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Insight triggers in the Assets panel.
2. Next to an insight trigger group, click ![Bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Duplicate.

## Viewing insight trigger details

You can view details about an active insight trigger, such as owner, time periods, and a visualization of its current data, by opening Details.

Do the following:

1. Open ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Insight triggers in the Assets panel.
2. Next to an insight trigger, click ![Bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Details.

## Monitoring insight calculations from a trigger

Insight triggers are evaluated whenever data changes (see [*When are insights generated?*](insight-triggers.htm#Generate)). When editing an insight trigger, you can view the status of its last evaluation.

You will need permissions to edit the insight trigger to view this information. See [*Discovery Agent permissions*](discovery-agent-admin.htm#Permissions).

Do the following:

1. Open ![Insight triggers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_metrics_outline.svg) Insight triggers in the Assets panel.
2. Next to an insight trigger or group, click ![Bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Edit.
3. In the dialog, under General, inspect the Status column. You can see whether the trigger is active or inactive, as well as the following icons. Hover over the icon for more details about the evaluation.

   - ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_minus_outline.svg): The insight trigger has never been evaluated.
   - ![Checkbox](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_success_outline.svg): The last evaluation was successful.
   - ![Errors box](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning.svg): The last evaluation failed.

Checking the status of the last evaluation for an insight trigger.

![Monitoring the status of an insight trigger](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-insight-triggers-status.png "Click to view full size")

## Permissions

For more information about permissions for managing insight triggers, see [*Discovery Agent permissions*](discovery-agent-admin.htm#Permissions).

## Learn more

- [*Creating insight triggers*](insight-triggers-create.htm)
- [*Working with Discovery Agent insight triggers*](insight-triggers.htm)
- [*Sheet view*](../Sheets/sheet-view.htm)
- [*Analyzing Discovery Agent feeds*](feeds.htm)
- [*Navigating insights in feeds*](feeds-navigate.htm)
