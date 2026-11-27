---
title: "Changing field types"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/changing-date-time-format.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Changing field types

When data is added, Qlik Sense interprets the field type of each [field](#glossary-0 "Glossary term"). The following field types are currently supported:

- ![general](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) General
- ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) Date
- ![Time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_clock_3.svg) Timestamp
- ![Map](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_map_outline.svg) Geo data

If the data was not interpreted correctly, you can adjust the field type. You can also change the input and display format of a data or timestamp field.

To open the table editor, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) on the data table you want to edit.

It is not possible to change field type or display format of fields in some cases.

- The table is the result of concatenating two or more tables.
- The field is already recognized as a date or a timestamp.

## Making sure a date or timestamp field is recognized correctly

If a date or timestamp field is not recognized as a date or a timestamp, that is, it is marked with ![general](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) General, you can make sure it is interpreted correctly.

Do the following:

1. Click on ![general](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) above the field heading.

   The data format dialog opens.
2. Change Field type to Date or Timestamp.
3. Change the format string in Input format to interpret the date correctly. You can use a prepared format from the drop down list, or write your own format string.

   For more information, see [*Descriptions for number and time formats*](../Introduction/conventions-number-time-formats.htm).

   Information noteIt is not possible to use a single quote in the format string.
4. If you want to use a display format other than the default format in your application, write or select a format string in Display format.

   If you leave it empty, the application default display format is used.

## Changing the display format of a date or timestamp field

Each application has default display formats for date and timestamp fields. You can change the display format for an individual date or timestamp field.

Do the following:

1. Click on ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) or ![Time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_clock_3.svg) above the field heading.

   The data format dialog opens.
2. Change the format string in Display format. Either use a prepared format from the drop down list, or write your own format string..

   For more information, see [*Descriptions for number and time formats*](../Introduction/conventions-number-time-formats.htm).

## Changing a field type to geographical data

If a field with values such as city and country names or ISO symbols is not recognized as geographical data, you can change the field type to Geo data.

Do the following:

1. Click on ![general](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) above the field heading.

   The data format dialog opens.
2. Select Geo data from the Field type drop-down menu.
3. Select the type of geographical data from the Geo data drop-down menu.

   The options are City, Country, Country code ISO2, and Country code ISO3. ISO2 and ISO3 are from ISO 3166, the International Standards Organization's codes for countries. ISO2 contains two-character codes, and ISO3 contains three-character codes. For example, the codes for Sweden are SE and SWE.

   When assigning an ISO code, be sure that the values in the field match the code you assign. If you assign ISO3 to a field with two-character code values, location coordinates will not be assigned correctly.
4. For City data, select the related field in the table that contains geographical data for countries.

   There may be only one related country field, but it is possible to have multiple fields with geographical data for countries. For example, one field may have long names such as France and another field that designates countries by country codes such as ISO2. But the fields appear in the Associated country list only if they have been designated as Geo data.

   If no field has been designated as a Geo data country field, then the Associated country list does not appear when you designate a field as City.

When a field is assigned the Geo data field type, either by the user or automatically by Qlik Sense, a field containing geographical coordinates, either point or polygon data, is associated with it. The associated fields containing the coordinates are visible in the [Data model viewer](#glossary-2 "Glossary term"). These coordinates are required for applications that use Map objects.

Fields that contain geographical information in the form of names or codes, such as postal areas, cannot be used for mapping unless they are designated as Geo data fields.

The fields assigned the Geo data type continue to hold string values, such as Mexico and MX, but when they are used in a Map object, the mapping coordinates come from the fields containing the point or polygon data.
