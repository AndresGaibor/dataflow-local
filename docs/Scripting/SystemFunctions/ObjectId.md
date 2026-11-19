---
title: "ObjectId  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "System functions", "properties"]
---
Expand/Collapse all

# ObjectId - chart function

The ObjectId() chart function returns the ID of the object in which the expression is evaluated. The function takes an optional argument specifying which type of object the function concerns. The object can be a sheet or a visualization. This function is only available in chart expressions.

Syntax:

ObjectId([object\_type\_str])

Return data type: string

The function's only argument, object\_type\_str, is optional and refers to a string value representing the type of the object.

Arguments

| Argument | Description |
| --- | --- |
| object\_type\_str | A string value representing the type of the object being evaluated. |

If no argument is specified in the function expression, ObjectId() returns the ID of the object in which the expression is used. To return the ID of the [sheet](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm#glossary-0 "Glossary term") object within which the [visualization](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm#glossary-1 "Glossary term") appears, use ObjectId('sheet').

In the case of visualization objects nested within other visualization objects, specify the desired object type in the function argument for different results. For example, for a **Text & image** [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm#glossary-2 "Glossary term") within a container, use 'text-image' to return the **Text & image** object and 'container' to return the ID of the container.

You can use the **Embed** menu to obtain object IDs.

Do the following:

1. In analysis mode, right-click a visualization or sheet, and then click ![Forward](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg) **Share** > ![Embed](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_code_outline.svg) **Embed**.
2. Copy the object or sheet ID.

Limitations:

This function can give unexpected results when invoked in an object (for example, a button) inside a container which is a master item. This limitation also applies to filter pane master items, which are containers for a number of listboxes. This is because of how master items use the object hierarchy.

The chart expression ObjectId('sheet') will return an empty string in those cases, whereas ObjectId('masterobject') will show the identifier of the owning [master item](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm#glossary-3 "Glossary term").

ObjectId() is often used in combination with the following functions:

Related functions

| Function | Interaction |
| --- | --- |
| [*if Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ConditionalFunctions/if.htm) | The **if** and **ObjectId** functions can be used together to create conditional expressions. For example, [visualizations](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm#glossary-4 "Glossary term") might achieve conditional coloring through expressions using these functions. |
| [*InObject - chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/InObject.htm) | Similar to **if**, **InObject** is also used with **ObjectId** to create conditional expressions. |

## Example 1 – Return chart object ID

Chart expression and results

The following basic example demonstrates how to return the ID of a visualization.

Do the following:

1. Open a new sheet and in the **Assets** panel, open **Charts**.
2. Under **Legacy**, drag a **Text & image**chart onto the sheet.
3. In the [properties](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/ObjectId.htm#glossary-5 "Glossary term") panel, click **Add measure**.
4. Click ![Expression](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
5. Paste the following expression into the dialog:

   ```
   =ObjectId()
   ```
6. Click **Apply**.

The ID of the **Text & image** object is displayed in the visualization.

The same result can be achieved with the following expression:

=ObjectId('text-image')

## Example 2 – Return sheet ID

Chart expression and results

The following basic example demonstrates how to return the ID of the sheet in which a visualization appears.

Do the following:

1. Open a new sheet and in the **Assets** panel, open **Charts**.
2. Under **Legacy**, drag a **Text & image**chart onto the sheet.
3. In the properties panel, click **Add measure**.
4. Click ![Expression](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
5. Paste the following expression into the dialog:

   ```
   =ObjectId('sheet')
   ```
6. Click **Apply**.

The ID of the sheet is displayed in the visualization.

## Example 3 – Nested expression

Chart expression and results

The following example shows how the **ObjectId()** function can be nested inside other expressions.

Do the following:

1. Open a new sheet and in the **Assets** panel, open **Charts**.
2. Under **Legacy**, drag a **Text & image**chart onto the sheet.
3. In the properties panel, click **Add measure**.
4. Click ![Expression](../../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) to open the expression editor.
5. Paste the following expression into the dialog:

   =if(InObject(ObjectId('text-image')), 'In Text & image', 'Not in Text & image')
6. Click **Apply**.

The text In Text & image appears in the chart, indicating that the object referenced in the expression is a **Text & image** chart.

For a more detailed example using conditional coloring, see the example on [*InObject - chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/InObject.htm).
