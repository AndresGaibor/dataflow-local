---
title: "InObject  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/InObject.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "System functions"]
---

# InObject  - chart function

Expand/Collapse all

# InObject - chart function

The InObject() chart function evaluates whether or not the current object is contained inside another object with the ID specified in the function argument. The object can be a sheet or a visualization.

This function can be used to show the hierarchy of objects in a [sheet](#glossary-0 "Glossary term"), from the top-level sheet object to [visualizations](#glossary-1 "Glossary term") nested within other visualizations. This function can be used alongside the if and ObjectId functions to create custom navigation in your applications.

Syntax:

InObject(id\_str)

Return data type: Boolean

In Qlik Sense, the Boolean true value is represented by -1, and the false value is represented by 0.

Arguments

| Argument | Description |
| --- | --- |
| id\_str | A string value representing the ID of the object being evaluated. |

You can use the Embed menu to obtain object IDs.

Do the following:

1. In analysis mode, right-click a visualization or sheet, and then click ![Forward](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg) Share > ![Embed](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_code_outline.svg) Embed.
2. Copy the object or sheet ID.

Limitations:

This function can give unexpected results when invoked in an object (for example, a button) inside a container which is a master item. This limitation also applies to filter pane master items, which are containers for a number of listboxes. This is because of how master items use the object hierarchy.

InObject() is often used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*if Script and chart function*](../ConditionalFunctions/if.htm) | The if and ObjectId functions can be used together to create conditional expressions. For example, visualizations might achieve conditional coloring through expressions using these functions. |
| [*ObjectId - chart function*](ObjectId.htm) | Similar to if, ObjectId is also used with InObject to create conditional expressions. |

## Example 1 – Basic functionality

Chart expression and results

The following basic example demonstrates how to determine whether an object is contained inside another object. In this case, we will be checking if a Text & image object resides in a sheet object using the ID of the sheet as an argument.

Do the following:

1. Open a new sheet and in the Assets panel, open Charts.
2. Under Legacy, drag a Text & image[chart](#glossary-2 "Glossary term") onto the sheet.
3. In the [properties](#glossary-3 "Glossary term") panel, click Add measure.
4. Click ![Expression](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
5. Paste the following expression into the dialog:

   ```
   =InObject()
   ```
6. Modify the expression to include the ID of your sheet as a string between the parentheses.

   For example, for a sheet with ID 1234-5678, you would use the following:

   =InObject('1234-5678')
7. Click Apply.

The value -1 is displayed in the chart, indicating that the expression was evaluated to be true.

## Example 2 – Objects with conditional colors

Chart expression and results

Overview

The following example demonstrates how to create custom navigation buttons showing different coloring to indicate the sheet that is currently open.

Start by creating a new application and opening the [Data load editor](#glossary-4 "Glossary term"). Paste the following [load script](#glossary-5 "Glossary term") into a new tab. Note that the data itself is a placeholder and will not be used in the example content.

Load script

```
Transactions:

Load
*
Inline
[
id,date,amount
8188,'1/19/2022',37.23
8189,'1/7/2022',17.17
8190,'2/28/2022',88.27
8191,'2/5/2022',57.42
8192,'3/16/2022',53.80
8193,'4/1/2022',82.06
8194,'4/7/2022',40.39
8195,'5/16/2022',87.21
8196,'6/15/2022',95.93
8197,'7/26/2022',45.89
8198,'8/9/2022',36.23
8199,'9/22/2022',25.66
8200,'11/23/2022',82.77
8201,'12/27/2022',69.98
8202,'1/1/2023',76.11
8203,'2/8/2022',25.12
8204,'3/19/2022',46.23
8205,'6/26/2022',84.21
8206,'9/14/2022',96.24
8207,'11/29/2022',67.67
];
```

Creating the visualizations

Load the data and create two new sheets. Title them Sales 2022 and Sales 2023 respectively.

In the Sales 2022 sheet, toggle on the advanced options. Next, build two button objects that will be used to navigate between the two sheets.

Do the following:

1. Add two Button objects to the sheet.
2. Under Appearance > General, set the Label of each button to Sales 2022 and Sales 2023, respectively.
3. Arrange the buttons to match the following image.

   Sales 2022 sheet arrangement with two navigation buttons

   ![Sales 2022 sheet with two buttons, labelled 'Sales 2022' and 'Sales 2023' respectively. The buttons are arranged in a thin horizontal arrangement at hte top of the otherwise blank sheet.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ObjectId_ConditionalColorButtonsArrangement.png "Click to view full size")
4. Select the Sales 2022 button, and expand Actions and navigation in the properties panel.
5. Click Add action and under Navigation, select Go to a sheet.
6. Under Sheet, select Sales 2022.
7. Repeat this button action setup to link the Sales 2023 button to the Sales 2023 sheet.
8. Convert the buttons to master items by right-clicking them and selecting ![Linked Object](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Add to master items.

You can now copy each button and paste it in the Sales 2023 sheet, using the same size and arrangement on the sheet.

Creating conditional colors

Next, configure the buttons so that they will be blue if they are linked to the currently open sheet, and light gray if linked to the sheet that is not open.

Do the following:

1. Open the Sales 2022 sheet and obtain the sheet ID from the URL. Keep the Sales 2022 sheet open.
2. Click the Sales 2022 button [master item](#glossary-6 "Glossary term") and select Edit in the properties panel.
3. Under Appearance > Background, select to color the button By expression.
4. In Expression, paste the following text:

   =if(InObject(''), Blue(), LightGray())
5. Between the parentheses in the above expression, paste the sheet ID for the Sales 2022 sheet.

The button is now configured to turn blue when the Sales 2022 sheet is open, and light gray when it is not open.

Repeat the above instructions for the Sales 2023 sheet, linking the Sales 2023 button master item to the Sales 2023 sheet ID.

Each sheet should now have two buttons indicating the currently open sheet with the color blue.

Sales 2022 sheet with blue coloring to indicate that Sales 2022 is currently displayed

![Analysis mode for Sales 2022 sheet with two buttons, labelled 'Sales 2022' and 'Sales 2023' respectively. The buttons are now configured to blue when open and light gray when not open .](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ObjectId_ConditionalColorButtonsSales2022.png "Click to view full size")
