---
title: "Grouping measure data into ranges"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Grouping-measure-data-into-ranges.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Grouping measure data into ranges

Measures can provide additional insight for analysis when grouped into ranges and used as [dimensions](#glossary-0 "Glossary term") in [visualizations](#glossary-1 "Glossary term").

For example, if a [field](#glossary-2 "Glossary term") had customer ages, you could group values into age ranges. The Bucket data profiling card enables the grouping of field data into ranges, creating a new field with the specified groupings. You access the Bucket card by editing a table in [Data manager](#glossary-3 "Glossary term") and selecting a table field that is set as a [measure](#glossary-4 "Glossary term") in the Summary card.

## Requirements

You can group measures into ranges with fields that meet the following requirements:

- Fields must be classified as a measure in the Summary card
- Fields must contain at least 10 distinct values.

  The Bucket card is not recommended with fields containing a low range of values, but you can choose to use the Bucket card with non-recommended fields.
- Values in the field cannot contain more than 20% mixed types.

  The Bucket card is not recommended with fields containing mixed types of values, but you can choose to use the Bucket card with non-recommended fields.

Information note

Bucket fields created by the Bucket card are categorized as dimensions in the Summary card. Bucket fields cannot have a custom order applied to them using the Order card, however. Bucket fields cannot be used in calculated fields.

## Overview

The Bucket card provides a suggested number of groupings, a preview of the groupings, and a slider bar containing your groupings that enables modifying each bucket's name and value range. You can modify the suggested number of groupings by entering a new number into the Bucket field. Qlik Sense supports a maximum of 20 buckets and a minimum of 2 buckets. New buckets are added to the right of your bucket range while buckets are removed from right to left. If you have not modified any individual buckets, each bucket's range is adjusted to fit evenly within the value range of the field. If you change the number of buckets after having modified an individual bucket, new buckets are added to the right of your bucket range and are given a range of values equal to the size of the second rightmost bucket.

The Preview of data buckets bar chart gives overview of the data in your buckets, with a count of the number of distinct values in each bucket. The chart is updated as you alter your buckets. If a bucket has no values in it, it will have no bar in the chart.

The Bucket slider bar enables you to edit your buckets. By clicking a bucket segment, you can set that bucket's range, change the bucket's name, or remove the bucket entirely. Hovering your cursor over the bucket brings up the bucket’s name and range of values. By default, buckets are named with the bucket's value range expressed as an interval notation. Buckets ranges include values between the starting value and up to but excluding the ending value.

When you adjust a single bucket’s value range, Qlik Sense shifts the values of all buckets, ensuring there are no gaps and overlaps while respecting the existing quantitative ranges of the other buckets as much as possible. The leftmost bucket always has no lower boundary and the rightmost bucket has no upper boundary. This allows them to capture any values that might fall outside the set ranges of all your buckets. Modifying the lower range of a bucket will alter the ranges of the buckets to the right, modifying the upper range of a bucket will modify the buckets to the left.

When you create buckets from a field, a new field is generated containing all the buckets assigned to the rows with their corresponding measure values from the source field. By default, it will be named <field> (Bucketed). This field can be renamed, associated, sorted, and deleted like other table fields. You can edit the bucketing in the generated bucket field by selecting the field in the table and modifying the bucketing options. You can create multiple bucket fields from the same source measure field.

## Grouping measures

To group measure values into ranges, do the following:

1. Access the Bucket card.
2. Optionally, change the number of buckets.
3. Optionally, modify individual buckets.
4. Optionally, reset the manual adjustments to buckets to the default settings.
5. Create the bucketed field.

## Accessing the Buckets card

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. If you are creating new groups of value ranges, select a field.
3. If you are editing an existing buckets field, select a buckets field

## Changing the number of buckets

Changing the number of buckets adds buckets to or removes buckets from the end of the range.

Do the following:

- In the Bucket card, enter a new number before Buckets.

## Modifying a bucket

You can rename a bucket, adjust a bucket’s value range, or delete a bucket.

Tip note

If you are modifying buckets, it is recommended to modify buckets in order from the leftmost bucket segment to the rightmost bucket segment.

### Renaming a bucket

Do the following:

1. In the Bucket card, click the bucket segment.
2. In the name field, enter a new name.
3. To apply your changes, click anywhere outside the bucket segment.

### Adjusting a bucket's range of values

Information note

If you are trying to use decimal values, you must enter them manually in the From and Up To fields.

Do the following:

1. In the Bucket card, click the bucket segment.
2. Do one of the following:
   - After From and Up To, enter new values to set the range of the bucket.

     A bucket includes the values between the value in From and up to but excluding the value in Up To.
   - Adjust the segment's sliders to set the range of the bucket.
3. To apply your changes ,click anywhere outside the bucket segment.

### Deleting a bucket

Do the following:

1. In the Bucket card, click the bucket’s segment.
2. Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg).

## Resetting a field's buckets

Resetting buckets enables you to restore the bucket card settings to their default state. If this is a measure field, the default state is the Qlik Sense recommended bucketing. If this is a bucket field, the default state is the field’s state after the last time Create buckets was clicked.

Do the following:

- In the Bucket card, click Reset to default.

## Creating a bucket field

Do the following:

1. In the Bucket card, click Create buckets.
2. Click OK.

The new field containing your data grouping is added to your table.

Related learning:

- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
