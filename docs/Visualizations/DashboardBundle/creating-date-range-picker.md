---
title: "Creating date range pickers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/DashboardBundle/creating-date-range-picker.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating date range pickers

The date range picker (Date picker) lets you select a single date or a range of dates from a calendar. It is included in Dashboard bundle. For more information, see [*Dashboard bundle*](dashboard-bundle.htm).

You can create a date range picker on the [sheet](#glossary-0 "Glossary term") you are editing.

Do the following:

1. In the assets panel, open Charts.
2. Under Dashboard objects, drag a Date picker object to the sheet.
3. Select the date [field](#glossary-1 "Glossary term") to use as filter in Date field.

   The list contains only fields that are recognized as a date field by Qlik Sense.

   Tip noteIf you want to use a timestamp field, you need to convert it to a date. Use the expression =date(floor(myTimeStamp\_Field)) instead of myTimeStamp\_Field.
4. Select if you want to be able to pick a single date or a date interval in Single date / interval.

   Date interval lets you pick a range of dates.

   Single date lets you pick a single date only.

When you have created the date range picker, you may want to adjust its appearance and other settings.

## Setting the available date range

You can set the range of dates available to pick by setting the option Advanced setup to On. You can use expressions or explicit date values. The expressions used below refer to a field named DateField.

- Set the first date of the calendar with Min date.

  Default value is =Min( {1} [DateField]). This expression returns the first date in DateField in the full data set.
- Set the last date of the calendar with Max date.

  Default value is =Max( {1} [DateField]). This expression returns the last date in DateField in the full data set.
- Set the date to show when the date range picker is opened with Start date.

  Default value is =Min([DateField]). This expression returns the first date in DateField in the current selection.

## Setting locale of the calendar

You can set the locale of the calendar to get local names for days and months. Change the setting Locale under Calendar Settings > Language and labels to the two-letter code of the locale you want to use. For example, you can change the default value of en for English to de for German.

## Using predefined ranges

In date interval mode there are a number of predefined ranges available to pick if Show predefined ranges is set to On. You can customize the text labels for the predefined range selections with the settings under Calendar Settings > Predefined ranges:

- Custom Range represents the option where you select a date interval freely from the calendar. Default value is Range.
- Today represents the date value of today. Default value is Today.
- Yesterday represents the date value of yesterday. Default value is Yesterday.
- Last $ days represents the two options for showing the last 7 or 30 days. $ is replaced by 7 or 30 in the string. Default value is Last $ days.
- This represents the current period. By default Month is selected. You can select:
  - Day
  - Month
  - Quarter
  - Year
  - None
- Last represents the previous period. By default Month is selected. You can select:

  - Day
  - Month
  - Quarter
  - Year
  - None

  You can specify how many of the previous periods to include in Last number of.

  You can include the current period by selecting Include current.

## Customizing text labels

You can customize the text labels that are shown when the date range picker is used.

You change the text prompt shown when the date range picker is minimized with the setting Default Text under Calendar Settings > Language and labels. The default setting is 'Select date range'.

## Customizing styling

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, turn off Show titles.

The visibility of the different labels on the chart depends on chart-specific settings and label display options. These can be configured in the properties panel.

You can style the text that appears in the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote

### Customizing the background

You can customize the background of the chart. The background can be set by color and image.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the origin must be added to the allowlist in your tenant's Content Security Policy. Add the origin with the img-src directive. This is done in the Administration activity center by an administrator.

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

### Customizing the border and shadow

You can customize the border and shadow of the chart.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Limitations

The date range picker cannot filter date ranges greater than 28 years or that contain 10,000 or more values. If your date range contains a large number of dates, use another object such as a line chart.

For information about general limitations, see [*Limitations*](dashboard-bundle.htm#Limitati).

### Date format limitations

Dates in the format YYYYMMDD cannot be used in the date range picker. If your application has date values in this format, change the date format in the load script. Examples are shown below.

Examples: Transforming dates for compatibility with date range picker

For the example script below, consider the following:

- original\_date is the original date field in YYYYMMDD format.
- new\_date1, new\_date2, and new\_date3 are updated date fields that will be in compatible date formats.
- original\_table is the table in which the original\_date field was loaded (not shown). For the purposes of the example showing a complete LOAD statement, we perform the transformation on this existing field by using a RESIDENT load. However, your own data can be loaded in many different ways depending on your use case.

```
SET DateFormat='M/D/YYYY';

Load
Date(Date#(original_date, 'YYYYMMDD'),'YYYY/MM/DD') as new_date1,
Date(Date#(original_date, 'YYYYMMDD')) as new_date2,
Date(Date#(original_date, 'YYYYMMDD'),'YYYY-MM-DD') as new_date3
RESIDENT original_table;
```

Related learning:

- [How do I configure a Dashboard Bundle Date picker object?](/lnk/How_configure_Dashboard_Bundle_Date_picker_object)
