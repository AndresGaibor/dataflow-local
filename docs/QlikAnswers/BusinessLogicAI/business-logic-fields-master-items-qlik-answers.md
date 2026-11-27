---
title: "Defining fields and master items for Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/business-logic-fields-master-items-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic"]
---

# Defining fields and master items for Qlik Answers

Fields, master items, and groups are the primary components of logical models in business logic. By defining the groups to which your fields and master items belong, you can define how Qlik Answers should use them.

You define how business logic should handle fields and master items in the Fields and master items section of AI optimization. Fields and master items can be grouped together to indicate a relationship in Qlik Answers analysis. For each item in a group, you can define how Qlik Answers should treat it in analysis.

Groups enable you to organize fields and master items into related conceptual groupings. For example, you can group all the fields related to customers in a single group, regardless of which tables in the data model from which they are loaded. Qlik Answers can use this information to determine which fields to show together in [visualizations](#glossary-0 "Glossary term"). There are three kinds of groups:

- Dimension: A dimension group commonly consists of fields that are classified as dimensions. Dimension groups can also contain fields classified as [measures](#glossary-1 "Glossary term") or dates.
- Measure: A measure group consists of related measure fields. Only measures can belong to a measure group.
- Calendar: A calendar group contains a time dimension in your logical model. Calendar groups can only contain dimensions and are expected to have at least one temporal fields (such as date, timestamp, or year). Calendar groups are useful if you have separate fields defining your calendar, such as year, month, and day. If you can also group other data-related fields, such as fiscal quarter or fiscal year.

Fields and master items that are not in any group are Excluded. Qlik Answers does not use excluded fields and master items. Fields that are new to the data model are excluded until you add them to a group.

By default, fields and master items are ordered by group. If you turn off Order by group, a Type column is added to the table. Type shows the type of the group to which each item belongs.

In addition to defining groups, you can also define the properties of individual fields and master items belonging to your groups.

## Creating groups

Once you create a group, the group type cannot be changed. You can rename the group and add or remove fields from the group. Groups can also be deleted. Deleting a group ungroups all items in the group.

To edit an existing group, click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg) in the group row or after the group name in the Group column.

Do the following:

1. Click Create group.
2. Enter a group name.
3. Select a group type.
4. Add fields to the group from Available fields.
5. Click Create.

## Defining fields and master items

Fields and master items consists of a table containing fields and master items from your application, along with the groups to which they belong. You can edit the properties of your fields and master items by adjusting the column value in that item's row. For additional options, you can click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the row. You can:

- Move item: Move the item to a different group.
- Ungroup: Remove the item from its current group. The item becomes Excluded and is not used by Qlik Answers. Ungrouping can also be used to remove old fields that were removed from the data model, but are still present in the semantic model.

You can also select multiple rows using the row checkboxes to make the same changes to multiple items. When selected in this way, properties settings and options are available above the table.

### Field and master item properties

The table contains the following columns:

- Name: The name of the field or master item.
- Group: The group to which the item belongs.
- Visibility: Whether the item is available in Qlik Answers.

### Visibility

Visibility controls if an item is available in Qlik Answers. There are two possible values:

- Visible: The item is available for use in Qlik Answers.
- Hidden: The item is not available for use in Qlik Answers.

Tip noteVisibility is one of the strongest tools for improving answer quality. More fields can create noise, so hiding fields that are not necessary for analysis helps Qlik Answers focus on the right information and make better field selection decisions during evaluation and runtime.
