---
title: "Dates processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-dates.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Dates processor

The Dates processor allows you to perform different operations on columns with date or timestamp data in a transformation flow.

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.

For information about patterns to use for date and time input, please check the vendor documentation for the data platform that you are using in the project.

## Compare dates

You can compare a date value in a column with the value in another date column or a specified date. The output value is a boolean representation of the comparison.

1. Select Compare dates in Function name.
2. Select which operator to use when comparing the dates, for example, equals or before, in Compare mode.
3. Select which column to use when comparing dates in Column to process.
4. Select what to compare with in Use with.

   - Value lets you compare with a fixed value.

     Set the date and time to compare with in Value. The input format is: yyyy-MM-DD HH:mm:ss, or if you want to include fractions of a second, yyyy-MM-DD HH:mm:ss.F(f). You can specify fractions up to 9 digits with f, for example, F(9).
   - Column compares with the value of another column in the dataset.

     Set the column to compare with in Column.
5. Enter the name of the new column in New column name.
6. Click Apply.

## Convert to date

If you have a column with a data type other than date, but that contains date values, you can convert it to a date.

1. Select Convert to date in Function name.
2. Select which column to convert in Column to process.
3. Set the format of the input date in Input format.

   - Auto will attempt to recognize the date format automatically.
   - Custom lets you set the format pattern of the input date.

     Set the pattern in Input date pattern.
4. Select Create new column if you want to store the results in a new column. Otherwise the results are stored in the same column.

   Enter the name of the new column in New column name.
5. Click Apply.

## Convert to datetime

If you have a column with a data type other than datetime, but that contains datetime values, you can convert it to a datetime.

1. Select Convert to datetime in Function name.
2. Select which column to convert in Column to process.
3. Set the format of the input datetime in Input format.

   - Auto will attempt to recognize the datetime format automatically.
   - Custom lets you set the format pattern of the input datetime.

     Set the pattern in Input date pattern.

   You can also set the precision in Precision.
4. Select Create new column if you want to store the results in a new column. Otherwise the results are stored in the same column.

   Enter the name of the new column in New column name.
5. Click Apply.

## Convert to time

If you have a column with a data type other than time, but that contains time values, you can convert it to a time.

1. Select Convert to time in Function name.
2. Select which column to convert in Column to process.
3. Set the format of the input timestamp in Input format.

   - Auto will attempt to recognize the timestamp format automatically.
   - Custom lets you set the format pattern of the input timestamp.

     Set the pattern in Input date pattern.
4. Select Create new column if you want to store the results in a new column. Otherwise the results are stored in the same column.

   Enter the name of the new column in New column name.
5. Click Apply.

## Create date from parts

You can create a date from parts that can either be a set value, or a column value. The date is stored in a new column.

1. Select Create date from parts in Function name.
2. Set the year part.

   Select if you want to set a fixed value, or a column value in Year.

   - If you selected Value, enter a year value in Year value.
   - If you selected Column, select which column to use in Year column.
3. Set the month part.

   Select if you want to set a fixed value, or a column value in Month.

   - If you selected Value, enter a month value in Month value.
   - If you selected Column, select which column to use in Month column.
4. Set the day part.

   Select if you want to set a fixed value, or a column value in Day.

   - If you selected Value, enter a day value in Day value.
   - If you selected Column, select which column to use in Day column.
5. Enter the name of the new column in New column name.
6. Click Apply.

## Create time from parts

You can create a time from parts that can either be a set value, or a column value. The time is stored in a new column.

1. Select Create time from parts in Function name.
2. Set the hours part.

   Select if you want to set a fixed value, or a column value in Hours.

   - If you selected Value, enter an hours value in Hours value.
   - If you selected Column, select which column to use in Hours.
3. Set the minutes part.

   Select if you want to set a fixed value, or a column value in Minutes.

   - If you selected Value, enter a minutes value in Minutes value.
   - If you selected Column, select which column to use in Minutes column.
4. Set the seconds part.

   Select if you want to set a fixed value, or a column value in Seconds.

   - If you selected Value, enter a seconds value in Seconds value.
   - If you selected Column, select which column to use in Seconds column.
5. Set the milliseconds part.

   Select if you want to set a fixed value, or a column value in Milliseconds.

   - If you selected Value, enter a milliseconds value in Milliseconds value.
   - If you selected Column, select which column to use in Milliseconds column.
6. Enter the name of the new column in New column name.
7. Click Apply.

## Create datetime from parts

You can create a datetime from parts that can either be a set value, or a column value. The datetime is stored in a new column.

1. Select Create datetime from parts in Function name.
2. Set the year part.

   Select if you want to set a fixed value, or a column value in Year.

   - If you selected Value, enter a year value in Year value.
   - If you selected Column, select which column to use in Year column.
3. Set the month part.

   Select if you want to set a fixed value, or a column value in Month.

   - If you selected Value, enter a month value in Month value.
   - If you selected Column, select which column to use in Month column.
4. Set the day part.

   Select if you want to set a fixed value, or a column value in Day.

   - If you selected Value, enter a day value in Day value.
   - If you selected Column, select which column to use in Day column.
5. Set the hours part.

   Select if you want to set a fixed value, or a column value in Hours.

   - If you selected Value, enter an hours value in Hours value.
   - If you selected Column, select which column to use in Hours column.
6. Set the minutes part.

   Select if you want to set a fixed value, or a column value in Minutes.

   - If you selected Value, enter a minutes value in Minutes value.
   - If you selected Column, select which column to use in Minutes column.
7. Set the seconds part.

   Select if you want to set a fixed value, or a column value in Seconds.

   - If you selected Value, enter a seconds value in Seconds value.
   - If you selected Column, select which column to use in Seconds column.
8. Set the milliseconds part.

   Select if you want to set a fixed value, or a column value in Milliseconds.

   - If you selected Value, enter a milliseconds value in Milliseconds value.
   - If you selected Column, select which column to use in Milliseconds column.
9. Set the microseconds part.

   Select if you want to set a fixed value, or a column value in Microseconds.

   - If you selected Value, enter a microseconds value in Microseconds value.
   - If you selected Column, select which column to use in Microseconds column.
10. Set the nanoseconds part.

    Select if you want to set a fixed value, or a column value in Nanoseconds.

    - If you selected Value, enter a nanoseconds value in Nanoseconds value.
    - If you selected Column, select which column to use in Nanoseconds column.
11. Enter the name of the new column in New column name.
12. Click Apply.

## Truncate date

You can truncate date field to exclude a date or time part.

1. Select Truncate date in Function name.
2. Select which date column to truncate in Column to process.
3. Select which date or time part to truncate in Date or time part.
4. Select Create new column if you want to store the results in a new column. Otherwise the results are stored in the same column.

   Enter the name of the new column in New column name.
5. Click Apply.

## Add duration

You can add a duration of time to column values. The duration can be a fixed value, or from another column.

1. Select Add duration in Function name.
2. Select which date column to add duration to in Column to process.
3. Select which date or time part to add in Date or time part.
4. Select if you want to set a fixed value, or a column value in Duration. The duration added will be according to what you selected in Date or time part.

   - If you selected Value, enter the duration in Duration value.
   - If you selected Column, select which column to use in Duration column.
5. Select Create new column if you want to store the results in a new column. Otherwise the results are stored in the same column.

   Enter the name of the new column in New column name.
6. Click Apply.

## Calculate date difference

You can calculate the difference between the date in a column and either now. a specific date, or a date in another column. The result is stored in a new column.

1. Select Calculate date difference in Function name.
2. Select which date column to add duration to in Column to process.
3. Optionally, you can select which unit to calculate the difference in Date or time part.
4. Select if you want to compare with now. a specific date, or a date in another column in Until.

   - If you selected Specific date, enter the date in This date. The input format is: yyyy-MM-DD HH:mm:ss or if you want to include fractions of a second, yyyy-MM-DD HH:mm:ss.F(f). You can specify fractions up to 9 digits with f, for example, F(9).
   - If you selected Column, select which column to use in Column.
5. Enter the name of the new column in New column name.
6. Click Apply.

## Extract date parts

You can extract parts of a date, time or datetime, and store the parts in individual columns.

1. Select Extract date parts in Function name.
2. Select which date column to extract date parts from in Column to process.
3. Select which parts to extract.
4. Enter a column prefix in New columns prefix. The columns that are created will be named starting with the prefix, followed by the part, separated with underscore.
5. Click Apply.
