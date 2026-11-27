---
title: "Defining fields and groups in Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-fields-groups.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Building logical models for Insight Advisor with Business logic"]
---

# Defining fields and groups in Insight Advisor

Fields and groups are the primary component of logical models in [business logic](#glossary-0 "Glossary term"). By defining the groups to which your fields and master items belong, you can define how [Insight Advisor](#glossary-1 "Glossary term") should use them.

You define how business logic should handle fields and groups in the Fields & groups section of Logical model. Fields and master items can be grouped together to indicate a relationship in Insight Advisor analysis. For each item in a group, you can define how Insight Advisor should treat it in analysis.

Groups enable you to organize fields and master items into related conceptual groupings. For example, you can group all the fields related to customers in a single group, regardless of which tables in the data model from which they are loaded. Insight Advisor uses this information to determine which fields to show together in [visualizations](#glossary-2 "Glossary term"). Groups can also be used to create packages, which limits scope for Insight Advisor to only use related groups together. There are three kinds of groups:

- Dimension: A dimension group commonly consists of fields that are classified as [dimensions](#glossary-3 "Glossary term"). Dimension groups can also contain fields classified as [measures](#glossary-4 "Glossary term") or dates.
- Measure: A measure group consists of related measure fields. Only measures can belong to a measure group.
- Calendar: A calendar group contains a time dimension in your [logical model](#glossary-5 "Glossary term"). Calendar groups can only contain dimensions and are expected to have at least one temporal fields (such as date, timestamp, or year). Calendar groups are useful if you have separate fields defining your calendar, such as year, month, and day. If you can also group other data-related fields, such as fiscal quarter or fiscal year.

By default, fields and master items are ordered by group. If you disable this, an additional column, In group, is added to the table.

In addition to defining groups, you can also define the properties of individual fields and master items belonging to your groups.

## Creating groups

Once you create a group, the group type cannot be changed. You can rename the group and add or remove fields from the group. Groups can also be deleted. Deleting a group ungroups all items in the group.

To edit an existing group, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit.svg) in the group row or after the group name in the In group column.

Do the following:

1. Click Create group.
2. Enter a group name.
3. Select a group type.
4. Add fields to the group from Available fields.
5. Click Create.

## Defining fields and master items

Fields & groups consists of a table containing fields and master items from your application, along with the groups to which they belong. You can edit the properties of your fields and master items by adjusting the column value in that item's row. For additional options, you can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the row. You can:

- Move item: Move the item to a different group.
- Create behavior: Create a behavior for the group to which the current item belongs.
- Ungroup: Remove the item from its current group. Ungrouped items are excluded from Insight Advisor.

You can also select multiple rows using the row checkboxes to make the same changes to multiple items. When selected in this way, properties settings and options are available above the table.

### Field and master item properties

The table is divided into the following columns:

- Name
- Group
- Visibility
- Classification
- Data value lookup
- Default aggregation
- Favorable trend
- Favorite
- Overall aggregation
- Default period grain

Name lists the field names. Group lists the group name to which the field belongs. The following section outlines the different values and settings of the other fields. You can set which columns display in the table by clicking ![Set columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_columns.svg).

#### Visibility

Visibility controls if an item is available in Insight Advisor. There are two possible values:

- Visible: The item is available for use in Insight Advisor.
- Hidden: The item is not available for use in Insight Advisor. Hidden fields should not be enabled for data value lookup.

You can hide all hidden items in Field & groups by selecting Show visible only.

#### Classification

Classification defines the default role that attribute can play in an analysis. The following types can be used to classify fields and groups:

- dimension: A field that is only to be used as a dimension
- measure: A field that is to only be used as a measure.
- boolean: A binary dimension.
- date: A temporal dimension containing dates.
- timestamp : A temporal field containing timestamps.
- year: A temporal dimension containing year data.
- week: A temporal dimension containing week data.
- quarter: A temporal dimension containing quarter data.
- month: A temporal dimension containing month data.
- weekDay: A temporal dimension containing data for the day of the week, either short form (Mon., Tues.), long form (Monday, Tuesday), or a number between 1-7.
- monthDay: A temporal dimension containing a number between 1-31 indicating the day of the month.
- yearDay: A temporal dimension containing a number for the day of the year (between 1-366).
- hour: A temporal dimension containing hour data.
- email: A dimension containing email addresses.
- address: A dimension containing addresses.
- country: A dimension containing country names.
- stateProvince: A dimension representing first-level administrative areas, such as states and provinces.
- city: A dimension representing cities.
- geoPoint: A dimension containing geographic point data.
- geoPolygon: A dimension containing geographic polygon data
- geographical: A dimension representing a geographic location, such as country or region.
- postalCode: A dimension containing postal codes.
- longitude: A dimension containing longitude data.
- latitude: A dimension containing latitude data.
- percentage: A measure field representing percentage values such as employment rate or inflation.
- monetary: A monetary measure such as revenue, cost, or salary.
- ordinal: A dimension whose values have inherent order.
- temporal: A time-related dimension.

You may have fields that might be considered a dimension in one question and a measure in another question. As a best practice, it is recommended to create a second field or [master item](#glossary-7 "Glossary term") for the alternate use case of the field.

#### Data value lookup

Data value lookup controls whether or not Insight Advisor can look up values from fields when a user asks a natural language question.

Reducing the number of fields that have data value lookup enabled can help you avoid false positive results and to reduce the time to generate results.
For example, you may have three fields containing names in your data model: First Name, Last Name, and Full Name. If Data value lookup was enabled for all three fields, users might get confusing results from all three fields if they search for `Drew`.

Information note

Data value lookup should be disabled for measures and hidden fields.

#### Default aggregation

Default aggregation sets the standard [aggregation](#glossary-8 "Glossary term") for measures in Insight Advisor. The following aggregations can be used:

- sum
- avg
- min
- max
- count
- countDistinct

When field has a default aggregation, Insight Advisor always applies that aggregation when using it as a measure.Users can edit [charts](#glossary-9 "Glossary term") to change the aggregation to a different type in Insight Advisor.

Default aggregations cannot be assigned to master items.

#### Favorable trend

Favorable trend sets whether the desired trend for a measure is to increase or decrease. By default, the favorable trend for measures is to increase. The following trends can be used:

- Up
- Down

The favored trend is used in visualizations created by Insight Advisor to ranking results.

#### Favorite

Favorite marks a measure as being of particular interest for Insight Advisor. Insight Advisor will use this measure more often when generating visualizations without user queries or [selections](#glossary-10 "Glossary term"), such as with Generate.

#### Overall aggregation

Overall aggregation indicates to Insight Advisor what aggregation should be used when Insight Advisor cannot determine for itself what aggregation to use in natural language insights for results involving master measures.
As some master measures use complex expressions, Insight Advisor may not know the aggregation to use when calculating the contribution of the master measure in the narratives. Setting an overall aggregation allows Insight Advisor to calculate narratives for these complex master measures.

You can only set overall aggregation for master measures.

#### Default period grain

You can set the default period grain, such as month or year, to be used with a date field in a calendar group when generating analyses in Insight Advisor. The grains are either derived from the autocalendar or you can pick a field containing a grain from the same calendar group.

You can use the default calendar setting with the default calendar period behavior. Default calendar properties set for fields and master items are overruled by default calendar period behaviors set for groups.
