---
title: "Dates processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-dates.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Dates processor

Performs date related operations.

The Dates processor allows you to apply various functions to fields related to dates, times and timestamps. Available functions can be used to calculate, cleanse, modify or convert dates.

## Usage

The Dates processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to work on dates.

Information noteThe properties listed in this section are the default properties for most of the functions of this processor. Additional properties may need to be defined depending on the function you have selected.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Convert to timestamp: Interprets a string as a timestamp using a format that can be selected from a list or specified manually. If you select Auto as input format, the function will try to detect the format from a set of the most common ones. If it fails to be interpreted as a timestamp, it will be set to Null. - Convert to date: Interprets a string as a date using a format that can be selected from a list or specified manually. If you select Auto as input format, the function will try to detect the format from a set of the most common ones. If it fails to be interpreted as a date, it will be set to Null. - Convert to time: Interprets a string as time using a format that can be selected from a list or specified manually. If you select Auto as input format, the function will try to detect the format from a set of the most common ones. If it fails to be interpreted as time, it will be set to Null. - Create timestamp from parts: Creates a new timestamp field by concatenating numeric parts from other fields or constant values. - Create date from parts: Creates a new date field by concatenating numeric parts from other fields or constant values. - Create time from parts: Creates a new time field by concatenating numeric parts from other fields or constant values. - Format date: Changes the date format to use in a date field. - Calculate date difference: For a given time part unit, calculates the time between the dates in your field and the date of your choice. The calculation is done by first truncating the dates to the specified date or time part, and then returning the difference between them as an integer. - Add duration: Adds a specific amount of time to a date. - Compare dates: Compares this field to another field or a constant - Extract date parts: Creates fields with year, month, quarter, day, hour, minute, second, etc. - Truncate date: Removes part of a date. |
| Fields to process | Select the field or fields on which you want to apply a function in the list. |
| Create new field | Enable this option to create a new field after applying the function. If you do not enable this option, the existing field will be kept and modified. |
| Rename new field | Give a custom name to the newly created field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.

## Additional information on how to work with dates

There are three distinct date related formats that are commonly referred to as dates:

- Time, that marks a time of day
- Date, that marks a particular day
- Timestamp, made from a date and a time

Dates are in most cases identified automatically in a data flow. However, in the following cases you should use one of the Convert to functions to properly introduce the dates into the system:

- Your dates are formatted in a way that can not be automatically identified.
- You want to put them in the same date format as the data flow, based on the localization of the user that created the data flow.
- You want to make sure they set in a particular format. Otherwise, date formats that are not recognized are set to Null.

## Limitations

- In some cases, formatting of dates will not work because of engine limitations. This applies to the Format function and the Convert to functions. This will only happen when updating the original input field and not when a new field is created.
- Due to an engine limitation, when a date is loaded from a format that natively supports dates, such as Excel, it is not always possible to set the format of that date.

## Predefined date formats

This table lists the different formats that are predefined in Data flow, but other formats are also supported when entered manually. For more information on what manually defined formats should look like, see [Descriptions for number and time formats](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/conventions-number-time-formats.htm#anchor-3).

| Format | Type | Example |
| --- | --- | --- |
| YYYY-MM-DD | Date | 1999-03-22 |
| YYYYMMDD | Date | 19990322 |
| M/D/YYYY | Date | 3/22/1999 |
| M/D/YY | Date | 3/22/99 |
| MM/DD/YY | Date | 03/22/99 |
| MMM D, YYYY | Date | Mar 22, 1999 |
| MMMM D, YYYY | Date | March 22, 1999 |
| YYYY-MM-DD hh:mm | Timestamp | 1999-03-22 05:06 |
| YYYY-MM-DD hh:mm:ss | Timestamp | 1999-03-22 05:06:07 |
| YYYY-MM-DDThh:mm | Timestamp | 1999-03-22T05:06 |
| YYYY-MM-DDThh:mm:ss | Timestamp | 1999-03-22T05:06:07 |
| M/D/YYYY hh:mm tt | Timestamp | 3/22/1999 05:06 AM |
| M/D/YY hh:mm tt | Timestamp | 3/22/99 05:06 AM |
| MM/DD/YY hh:mm tt | Timestamp | 03/22/99 05:06 AM |
| M/D/YYYY hh:mm:ss tt | Timestamp | 3/22/1999 05:06:07 AM |
| M/D/YY hh:mm:ss tt | Timestamp | 3/22/99 05:06:07 AM |
| MM/DD/YY HH:mm:ss tt | Timestamp | 03/22/99 05:06:07 AM |
| MMM D, YYYY h:mm:ss tt | Timestamp | Mar 22, 1999 5:06:07 AM |
| WWWW, MMMM D, YYYY h:mm:ss tt | Timestamp | Monday, March 22, 1999 5:06:07 AM |
| hh:mm | Time | 05:06 |
| hh:mm:ss | Time | 05:06:07 |
| hh:mm tt | Time | 05:06 AM |
| hh:mm:ss tt | Time | 05:06:07 AM |

## Example: Converting and working with dates

This scenario shows how to prepare a dataset with information on prospects, to train an ML experiment with the purpose of identifying which prospects could become customers. Among the information available, we have a couple of fields containing dates, such as FirstContactDate, and TrialDate.

![A dataset with information on prospects, including dates](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dates_convert_example_1.png)

The first step will be to make sure the two date fields use a common format. Use a first Dates processor with the Convert to date function on the FirstContactDate and TrialDate fields. The two fields now use the same D/MM/YYYY format.

With a second Dates processor, use the Calculate date difference to display the number of days between a first contact and the start of a trial.

After that a Fork processor is used to generate a first output from the resulting data, while the second branch will use a third Dates processor. With the Extract date parts function, you are able to keep only the year and month information of the FirstContactDate field, making it easier to read and work with in your future ML experiment.

After an aggregation operation, the data flow can be run to train your model, and the final data flow looks like the following:

![A data flow where dates are properly formatted](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dates_convert_example_2.png)

## Example: Calculating a date difference

The data used as source in this example contains a reference of orders including their date of order and date of shipping.

![Dataset containing orders and shipment dates](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dates_example_1.png)

To gain some insight on the delay necessary to ship orders, you can use the Dates processor to calculate the time between order placement and order shipping.

In the processor properties, select Calculate date difference as function and Day as time unit. Select Order Date as field to process and choose Ship Date as other field to calculate the time difference. Enter a name for the new field to create, set a target and run the data flow.

![A dates processor to calculate a time difference](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dates_example_2.png)

The target of this data flow will include a new column with the number of days it took to ship orders that you can use in your analytics.

## Video summary
