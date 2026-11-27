---
title: "today Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/today.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# today Script and chart function

Expand/Collapse all

# today Script and chart function

This function returns the current date, evaluated as per UTC time. The function returns values in the DateFormat system variable format.

Syntax:

today([
timer\_mode])

Return data type:  dual

The today() function can be used either in the [load script](#glossary-0 "Glossary term") or in [chart](#glossary-1 "Glossary term") objects.

The default timer\_mode value is 1.

Arguments

| Argument | Description |
| --- | --- |
| timer\_mode | Can have the following values:  0 (day of last finished data load) 1 (day of function call) 2 (day when the application was opened)  Information noteIf you use the function in a load script, timer\_mode=0 will result in the day of the last finished data load, while timer\_mode=1 will give the day of the current data load. |

Function examples

| timer\_mode value | Result if used in load script | Result if used in chart object |
| --- | --- | --- |
| 0 | Returns a date, in the DateFormat system [variable](#glossary-3 "Glossary term") format, of the last successful data reload prior to the latest data reload. | Returns a date, in the DateFormat system variable format, for the latest data reload. |
| 1 | Returns a date, in the DateFormat system variable format, for the latest data reload. | Returns a date, in the DateFormat system variable format, of the function call. |
| 2 | Returns a date, in the DateFormat system variable format, for when the user’s session in the application began. This will not be updated unless the user reloads the script. | Returns the date, in the DateFormat system variable format, for when the user’s session in the application began. This will be refreshed once a new session begins or the data in the application is reloaded. |

## When to use today

The today() function is commonly used as a component within an expression. For example, it can be used to calculate the interest that has accumulated in a month up to the current date.

The following table provides an explanation of the result returned by the today() function, given different values for the timer\_mode argument:

## Regional settings

Unless otherwise specified, the examples in this topic use the following date format: MM/DD/YYYY. The date format is specified in the SET DateFormat statement in your data load script. The default date formatting may be different in your system, due to your regional settings and other factors. You can change the formats in the examples below to suit your requirements. Or you can change the formats in your load script to match these examples. For more information, see [*Modifying regional settings for applications and scripts*](../../Apps/regional-settings-in-apps.htm).

Default regional settings in applications are based on the user profile. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../../UserInterface/Languages.htm#Setting).

## Example 1 – Generation of objects using load script

Load script and results

Overview

The following example creates three variables using the today() function. Each variable uses one of the timer\_mode options to demonstrate their effect.

For the variables to demonstrate their purpose, reload the script and then, after 24 hours, reload the script a second time. This will result in the today(0) and today(1) variables showing different values, thereby correctly demonstrating their purpose.

Load script

```
LET vPreviousDataLoad = today(0);
LET vCurrentDataLoad = today(1);
LET vApplicationOpened = today(2);
```

Results

Once the data has been loaded for a second time, create three textboxes using the directions below.

First, create a textbox for the data which has previously been loaded.

Do the following:

1. Using the Text & Image chart object, create a textbox.
2. Add the following measure to the object:

   =vPreviousDataLoad
3. Under Appearance, select Show titles and add the title 'Previous Reload Time' to the object.

Next, create a textbox for the data which is currently being loaded.

Do the following:

1. Using the Text & Image chart object, create a textbox.
2. Add the following measure to the object:

   =vCurrentDataLoad
3. Under Appearance, select Show titles and add the title 'Current Reload Time' to the object.

Create a final textbox to show when the user's session in the application was started.

Do the following:

1. Using the Text & Image chart object, create a textbox.
2. Add the following measure to the object:

   =vApplicationOpened
3. Under Appearance, select Show titles and add the title 'User Session Started' to the object.

Diagram of variables created using today() function in load script

![Diagram showing what each of the three generated textboxes could look like after using the today() function to load the variables via the load script.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-today-example-variables-script.png "Click to view full size")

The above image shows example values for each of the created variables. For example, the values could be as follows:

- Previous Reload Time: 06/22/2022
- Current Reload Time: 06/23/2022
- User Session Began: 06/23/2022

## Example 2 – Generation of objects without load script

Load script and chart expression

Overview

The following example creates three chart objects using the today() function. Each chart object uses one of the timer\_mode options to demonstrate their effect.

There is no load script for this example.

Results

Once the data has been loaded for a second time, create three textboxes.

First, create a textbox for the latest data reload.

Do the following:

1. Using the Text & Image chart object, create a textbox.
2. Add the following [measure](#glossary-4 "Glossary term").

   =today(0)
3. Under Appearance, select Show titles and add the title 'Latest Data Reload' to the object.

Next, create a textbox to show the current time.

Do the following:

1. Using the Text & Image chart object, create a textbox.
2. Add the following measure:

   =today(1)
3. Under Appearance, select Show titles and add the title 'Current Time' to the object.

Create a final textbox to show when the user's session in the application was started.

Do the following:

1. Using the Text & Image chart object, create a textbox.
2. Add the following measure:

   =today(2)
3. Under Appearance, select Show titles and add the title 'User Session Began' to the object.

Diagram of objects created using today() function without load script

![Diagram showing what each of the three generated textboxes could look like after using the today() function to create chart objects only, with no data loaded into the application.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/scripting-functions-today-example-variables-chart.png "Click to view full size")

The above image shows example values for each of the created objects. For example, the values could be as follows:

- Latest Data Reload: 06/23/2022
- Current Time: 06/23/2022
- User Session Began: 06/23/2022

The 'Latest Data Reload' chart object uses a timer\_mode value of 0. This returns the timestamp for the last time the data was successfully reloaded.

The 'Current Time' chart object uses a timer\_mode value of 1. This returns the current time according to the system clock. If the [sheet](#glossary-5 "Glossary term") or object is refreshed, this value will be updated.

The 'User Session Began' chart object uses a timer\_mode value of 2. This returns the timestamp for when the application was opened, and the user’s session began.

## Example 3 – Scenario

Load script and chart expression

Overview

Open the Data load editor and add the load script below to a new section.

The load script contains:

- A [dataset](#glossary-6 "Glossary term") containing a set of loan balances, which is loaded into a table called Loans.
- Table data with fields for loan ID, balance at the start of the month, and the simple interest rate charged on each loan per annum.

The end user would like a chart object that displays, by loan ID, the current interest that has been accrued on each loan in the month to date. Although the application is only reloaded once per week, the user would like the results to be refreshed whenever the object or application is refreshed.

Load script

```
Loans:
Load
*
Inline
[
loan_id,start_balance,rate
8188,$10000.00,0.024
8189,$15000.00,0.057
8190,$17500.00,0.024
8191,$21000.00,0.034
8192,$90000.00,0.084
];
```

Results

Do the following:

1. Load the data and open a sheet. Create a new table.
2. Add the following fields as [dimensions](#glossary-7 "Glossary term").

   - loan\_id
   - start\_balance
3. Next, create a measure to calculate accumulated interest:

   =start\_balance\*(rate\*(today(1)-monthstart(today(1)))/365)
4. Set the measure's Number formatting to Money.

Results table

| loan\_id | start\_balance | =start\_balance\*(rate\*(today(1)-monthstart(today(1)))/365) |
| --- | --- | --- |
| 8188 | $10000.00 | $16.44 |
| 8189 | $15000.00 | $58.56 |
| 8190 | $17500.00 | $28.77 |
| 8191 | $21000.00 | $48.90 |
| 8192 | $90000.00 | $517.81 |

The monthstart() function, using the today() function to return today’s date as its only argument, returns the start date of the current month. By subtracting that result from the current date, again using the today() function, the expression returns the number of days that have elapsed so far this month.

This value is then multiplied by the interest rate and divided by 365 to return the effective interest rate incurred for this period. The result is then multiplied by the starting balance of the loan to return the interest that has been accrued so far this month.

Because the value of 1 is used as the timer\_mode argument in the today() functions inside the expression, each time the chart object is refreshed (by opening the application, refreshing the page, moving between sheets etc.), the date returned will be for the current date, and the results will be refreshed accordingly.
