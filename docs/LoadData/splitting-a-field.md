---
title: "Splitting a field in a table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/splitting-a-field.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Splitting a field in a table

The Split card enables you to create new fields using data from an existing [field](#glossary-0 "Glossary term").

You could, for example, split a field that contains an address to create a new field that contains only a zip or postal code. This lets you to quickly create new fields containing segments of existing data. The Split card can create new fields from table fields that meet the following requirements:

- Fields must be set as dimensions in the Summary card.

Tip note

Table fields containing date and time information are automatically split into date fields when their tables are prepared in [Data manager](#glossary-1 "Glossary term") and do not require the Split card.

The Split card consists of an input field containing a template value and a preview of the new fields with their values. By default, the template value is the first value in numerical order from a field, but you can select other values from the source field to use as the template. You should select a value that is representative of all values in the table. Splitting using an outlier value as a template may impact the quality of the new fields.

Fields are split by inserting split markers into the template value where you want to split the field. Split markers are added by selecting a point in the sample field where you want to add a split marker, adjusting your selection, and then selecting to split by instance or position. The Split card may automatically add recommended split markers to your template value.

Instances are occurrences of a selected delimiter, such as the character @ or a space between words. Positions of instance split markers are relative to either:

- The start of the value, such as the first instance of @ in a value.
- Their position to the right of another instance or position split marker, such as the first instance of . after @.

If you remove the instance to which another instance is relative, the other instance's position adjusts to the same position relative to the next instance of a different delimiter set as a split marker or the start of the value. You can split a field on up to 9 delimiters.

Information note

The Split card splits values using the characters specified as the split markers. If the data has variances in how these characters are composed, such as accented characters, those variances will not be included in the split.

Positions are locations in the field value, such as after the first four characters. Positions are relative to either:

- The start of the value.
- Their position to the right of an instance split marker, such as the second character after an instance split marker.

If you removed an instance that has a position to its right, the position moves to the same position relative to the start of the value or the first next instance split marker to the left or the start of the value.

The field preview updates as you add split markers , showing the new fields and their data. You can rename the new fields in the field preview. You can also select to include or exclude split fields from your table before you apply the split. When you apply a split, the fields you selected in the field preview are added to your table.

A field can be split multiple times.

To split a field into new fields, do the following:

1. Access the Split card.
2. Set split markers in the input field.
3. You can also perform these optional tasks:
   - Remove split markers.
   - Select which new fields you want to be added to the table.
   - Rename the new fields.
4. Create the new fields.

## Accessing the Splitting card

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Select a dimension field.
3. In the data profiling card, click the Split tab.

## Inserting split markers

You insert split markers by clicking positions in the sample value and selecting the kind of split you want to apply.

Tip note

You can change the sample value displayed in the input field by clicking ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_triangle_bottom.svg) and selecting a different value.

Do the following:

1. In the Split card, click the position in the sample value where you want to add split markers.

   Clicking selects all of the template value up to any other split markers.

   Double-clicking selects the insert point of your cursor in the template value.
2. Adjust your selection by clicking and dragging the selection tabs or highlighting the section you want to select.
3. Click the button that corresponds to the kind of split you want applied:

   - This instance: The field splits by the selected instance of the delimiter.
   - All instances: The field splits by all instances of the delimiter.
   - These positions: The field splits on either side of the selection.
   - This position: The field splits at this position.

The split marker is inserted into the template value.

## Removing split markers

Do the following:

- In the Split card, do one of the following:

  - To remove a single split marker, click ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg) above the split marker you want to remove.
  - To remove all split marker, click Reset.

    Recommended split markers will not be removed and any removed recommended split markers will be added back to the template. You must remove these individually.

## Selecting the fields to add to your table

You can select which fields created by the Split card to include or exclude from your table. By default, all split fields are included.

Do the following:

- In the Split card, in the field preview, do one of the following:

  - To include a field, select the field column checkbox.
  - To exclude a field, clear the field column checkbox.

## Renaming new fields

Do the following:

- In the Split card, in a field header in the field preview, enter a new field name.

## Creating new fields

Do the following:

- In the Split card, click Split.

Related learning:

- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
- [How do I split data fields?](/lnk/How_split_data_fields)
