---
title: "now Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions", "measure"]
---
Expand/Collapse all

# now Script and chart function

In Qlik Cloud, this function returns a timestamp in UTC format. The function returns values in the TimeStamp system variable format. The default timer\_mode value is 1.

> **Tip:** In Qlik Cloud, now() uses UTC. If you need to return timestamps in other time zones, consider the following alternatives:
>
> - Wrap the now() function in an expression that uses the converttolocaltime() function. For example: `converttolocaltime(now(), 'Stockholm')`
> - Use the localtime() function as a standalone expression. For example: `LocalTime('Stockholm')`

Syntax:

now([
timer\_mode])

Return data type:  dual

The `now()` function can be used either in the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-0 "Glossary term") or in [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-1 "Glossary term") objects.

Arguments

| Argument | Description |
| --- | --- |
| timer\_mode | Can have the following values:  0 (time at last finished data load) 1 (time at function call) 2 (time when the application was opened)  **Note:** If you use the function in a data load script, timer\_mode=0 will result in the time of the last finished data load, while timer\_mode=1 will give the time of the function call in the current data load. |

> **Tip:** The `now()` function has a high-performance impact, which might result in scrolling issues if the function is used within tables' expressions. Whenever its use is not strictly necessary, we recommend using the `today()` function instead. If the use of `now()` is required in a layout, we recommend using the non-default settings `now(0)` or `now(2)` when possible, as they do not require constant recalculations.

## When to use now

The `now()` function is commonly used as a component within an expression. For example, it can be used to calculate the time remaining in a product's lifecycle. The `now()` function would be used instead of the `today()` function when the expression requires the use of a fraction of a day.

The following table provides an explanation of the result returned by the `now()` function, given different values for the `timer_mode` argument:

Function examples

| timer\_mode value | Result if used in load script | Result if used in chart object |
| --- | --- | --- |
| 0 | Returns a timestamp, in the `TimeStamp` system [variable](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-3 "Glossary term") format, of the last successful data reload prior to the latest data reload. | Returns a timestamp, in the `TimeStamp` system variable format, for the latest data reload. |
| 1 | Returns a timestamp, in the `TimeStamp` system variable format, for the latest data reload. | Returns a timestamp, in the `TimeStamp` system variable format, of the function call. |
| 2 | Returns a timestamp, in the `TimeStamp` system variable format, for when the user’s session in the application began. This will not be updated unless the user reloads the script. | Returns the timestamp, in the `TimeStamp` system variable format, for when the user’s session in the application began. This will be refreshed once a new session begins or the data in the application is reloaded. |

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the `SET DateFormat` statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Example 1 – Generation of objects using load script

Load script and results

Overview

Open the [Data load editor](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-4 "Glossary term") and add the load script below to a new tab.

This example creates three [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-5 "Glossary term") using the `now()` function. Each variable uses one of the `timer_mode` options to demonstrate their effect.

For the variables to demonstrate their purpose, reload the script and then, after a short period of time, reload the script a second time. This will result in the `now(0)` and `now(1)` variables showing different values, thereby correctly demonstrating their purpose.

Load script

```
LET vPreviousDataLoad = now(0);
LET vCurrentDataLoad = now(1);
LET vApplicationOpened = now(2);
```

Results

Once the data has been loaded for a second time, create three textboxes using the directions below.

First, create a textbox for the data which has previously been loaded.

Do the following:

1. Using the **Text & Image** chart object, create a textbox.
2. Add the following measure to the object:

   `=vPreviousDataLoad`
3. Under **Appearance**, select Show titles and add the title 'Previous Reload Time' to the object.

Next, create a textbox for the data which is currently being loaded.

Do the following:

1. Using the **Text & Image** chart object, create a textbox.
2. Add the following measure to the object:

   `=vCurrentDataLoad`
3. Under **Appearance**, select Show titles and add the title 'Current Reload Time' to the object.

Create a final textbox to show when the user's session in the application was started.

Do the following:

1. Using the **Text & Image** chart object, create a textbox.
2. Add the following measure to the object:

   `=vApplicationOpened`
3. Under **Appearance**, select Show titles and add the title 'User Session Started' to the object.

`now()` load script variables

![Diagram showing what each of the three generated textboxes could look like after using the now() function to load the variables via the load script.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-now-example-load-script.png)

The above image shows example values for each of the created variables. For example, the values could be as follows:

- Previous Reload Time: 6/22/2022 8:54:03 AM
- Current Reload Time: 6/22/2022 9:02:08 AM
- User Session Began: 6/22/2022 8:40:40 AM

## Example 2 – Generation of objects without load script

Load script and chart expression

Overview

In this example, you will create three chart objects using the `now()` function, without loading any variables or data into the application. Each chart object uses one of the `timer_mode` options to demonstrate their effect.

There is no load script for this example.

Do the following:

1. Open the Data load editor.
2. Without changing the existing load script, click **Load data**.
3. After a short period of time, load the script a second time.

Results

Once the data has been loaded for a second time, create three textboxes.

First, create a textbox for the latest data reload.

Do the following:

1. Using the **Text & Image** chart object, create a textbox.
2. Add the following [measure](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-6 "Glossary term").

   `=now(0)`
3. Under **Appearance**, select Show titles and add the title 'Latest Data Reload' to the object.

Next, create a textbox to show the current time.

Do the following:

1. Using the **Text & Image** chart object, create a textbox.
2. Add the following measure:

   `=now(1)`
3. Under **Appearance**, select Show titles and add the title 'Current Time' to the object.

Create a final textbox to show when the user's session in the application was started.

Do the following:

1. Using the **Text & Image** chart object, create a textbox.
2. Add the following measure:

   `=now(2)`
3. Under **Appearance**, select Show titles and add the title 'User Session Began' to the object.

`now()` chart object examples

![Diagram showing what each of the three generated textboxes could look like after using the now() function to create chart objects only, with no data loaded into the application.](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-now-example-no-data-loaded.png)

The above image shows example values for each of the created objects. For example, the values could be as follows:

- Latest Data Reload: 6/22/2022 9:02:08 AM
- Current Time: 6/22/2022 9:25:16 AM
- User Session Began: 6/22/2022 8:40:40 AM

The 'Latest Data Reload' chart object uses a `timer_mode` value of 0. This returns the timestamp for the last time the data was successfully reloaded.

The 'Current Time' chart object uses a `timer_mode` value of 1. This returns the current time according to the system clock. If the [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-7 "Glossary term") or object is refreshed, this value will be updated.

The 'User Session Began' chart object uses a `timer_mode` value of 2. This returns the timestamp for when the application was opened, and the user’s session began.

## Example 3 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-8 "Glossary term") consisting of inventory for a cryptocurrency mining operation, which is loaded into a table called `Inventory`.
- Data with the following fields: `id`, `purchase_date`, and `wph` (watts per hour).

The user would like a table that displays, by `id`, the total cost each mining rig has incurred in the month so far, in terms of power consumption.

This value should update whenever the chart object is refreshed. The current cost of electricity is $0.0678 per kWH.

Load script

```
SET DateFormat='MM/DD/YYYY';

Inventory:
Load
*
Inline 
[
id,purchase_date,wph
8188,1/7/2022,1123
8189,1/19/2022,1432
8190,2/28/2022,1227
8191,2/5/2022,1322
8192,3/16/2022,1273
8193,4/1/2022,1123
8194,5/7/2022,1342
8195,5/16/2022,2342
8196,6/15/2022,1231
8197,6/26/2022,1231
8198,7/9/2022,1123
8199,7/22/2022,1212
8200,7/23/2022,1223
8201,7/27/2022,1232
8202,8/2/2022,1232
8203,8/8/2022,1211
8204,8/19/2022,1243
8205,9/26/2022,1322
8206,10/14/2022,1133
8207,10/29/2022,1231
];
```

Results

Load the data and open a sheet. Create a new table and add this field as a dimension: `id`.

Create the following measure:

`=(now(1)-monthstart(now(1)))*24*wph/1000*0.0678`

If the chart object was refreshed at 6/22/2022 10:39:05 AM, it would return the following results:

Results table

| id | =(now(1)-monthstart(now(1)))\*24\*wph/1000\*0.0678 |
| --- | --- |
| 8188 | $39.18 |
| 8189 | $49.97 |
| 8190 | $42.81 |
| 8191 | $46.13 |
| 8192 | $44.42 |
| 8193 | $39.18 |
| 8194 | $46.83 |
| 8195 | $81.72 |
| 8196 | $42.95 |
| 8197 | $42.95 |
| 8198 | $39.18 |
| 8199 | $42.29 |
| 8200 | $42.67 |
| 8201 | $42.99 |
| 8202 | $42.99 |
| 8203 | $42.25 |
| 8204 | $43.37 |
| 8205 | $46.13 |
| 8206 | $39.53 |

The user would like the object results to refresh every time the object is refreshed. Therefore, the `timer_mode` argument of supplied for instances of the `now()` function in the expression. The timestamp for the start of the month, identified by using the `now()` function as the timestamp argument in the `monthstart()` function, is subtracted from the current time which is identified by the `now()` function. This provides the total amount of time that has elapsed so far this month, in days.

This value is multiplied by 24 (the number of hours in a day) and then by the value in the `wph` [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm#glossary-9 "Glossary term").

To convert from watts per hour to kilowatts per hour, the result is divided by 1000 before finally being multiplied by the kWH rate supplied.

## Learn more

- [*localtime Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/localtime.htm#Bar)
- [*converttolocaltime Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/converttolocaltime.htm#Bar)
