---
title: "Working with dates"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/working-with-dates.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations"]
---

# Working with dates

This section shows how you work with dates in your automation using the convert date function.

To add a date formula, click Add formula > Date functions > Date in the input field.

Tip noteFor the complete list of date functions and formatting, see [date functions](date-functions.htm).

## Convert a date to a timestamp

Working with integers is easier than working with dates because they have a defined data type and Unix timestamps have a defined format. Unix timestamps represent a data as the number of seconds since 1-1-1970. You can convert dates to Unix timestamps by applying a data function formula. For example, this automation shows how to convert a Qlik Sense app creation date to a Unix timestamp.

Raw formula view of date function

![Automation timestamp showing a simple automation and the raw output with a data conversion formula](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-timestamp.png)

The Get App Information block returns information about a Qlik Sense app. The output block outputs the `createdDate` key from the field mapped output of the preceding block. A formula is applied to the field mapping to covert the date to a Unix time stamp. The `'U'` parameter in the formula specifies that the date value should be converted to a Unix timestamp.

Do the following to apply the formula in the Output block:

1. Drag the Output block and place it in the Editor.
2. In the Data to output filed, map the createdDate field from the Get App Information block.
3. Click on the field mapping and select Add formula.
4. Click on Date functions and search for Date in the search bar to select it.
5. Add output format as U. This converts the createdDate into a Unix timestamp.

The raw formula to convert the date looks like this:

`{date:{$.GetAppInformation.info.attributes.createdDate},'U'}`

## Compare two dates

Using the example from the previous section, we can easily compare dates once they are converted to a Unix timestamp. For example, this automation uses a condition block to determine if the app was created recently or whether it was created more than five days ago.

Raw formula view to compare dates

![Automation compare dates showing both condition dates as Unix timestamps](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-comparedate.png)

The condition block converts the `createdDate` to a Unix timestamp and adds the condition `greater than 5 days ago`, as a Unix timestamp. Since the condition dates are both timestamps, they can easily be compared.

Do the following to apply the formula in the Condition block:

1. In the Input filed, map the createdDate field from the Get App Information block.
2. Click on the field mapping and select Add formula.
3. Click on Date functions and search for Date in the search bar to select it.
4. Add output format as U. This converts the createdDate into a Unix timestamp.
5. Select is greater than in the drop-down menu.
6. Click on the Value field > Add formula > Date functions > Date.
7. Add the Date as now-5. This subtracts 5 days from today's date.
8. Add output format as U. This converts the createdDate into a Unix timestamp.

The raw formula to convert the second condition date looks like this:

`{date:'now - 5 days','U'}`

You can also add or subtract months, hours, minutes, or seconds. Modifying the date with these operators looks like this:

`{date:'now + 1 month','U'}`

`{date:'now + 5 hours','U'}`

`{date:'now - 120 minutes','U'}`

`{date:'now - 1500 seconds','U'}`

For more information, see [How to compare dates in an automation](https://community.qlik.com/t5/Official-Support-Articles/How-to-compare-dates-in-an-automation/ta-p/1817301).

## Calculate the difference between dates

Using the example from the first section, we can calculate the difference between two dates using a variable for the Unix timestamp. For example, this automation uses a variable to calculate the difference between the current date and the created date of the Qlik Sense app.

Inputs for variable block

![Simple automation showing a variable that calculates the difference of dates](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-calculatedates_1130x806.png)

The variable block is set to the current date using a date formula to get the timestamp from now. This formula looks like this:

`{date:'now','U'}`

The variable has two more operations: one to substract the `createdDate`, which is the same formula as in the previous examples, and another to divide the result by the number of second in a day, which is 86400. This must be done because Unix timestamps are expressed in seconds. Configure the output block to show the difference in days.

Raw formula for output block

![The output block configuration showing the string and variable that is output](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-showDate.png)

To access the list of parameters when you are working on your automations, click on Show more in the Edit Formula dialog.

Edit formula input

![Edit formula dialog box emphasizing the link to show the parameters that can be used when working with date functions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_edit-formula_489x418.png)
