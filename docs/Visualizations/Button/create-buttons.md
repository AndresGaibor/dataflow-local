---
title: "Creating buttons"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Button/create-buttons.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating buttons

You can use buttons to:

- Add quick links for easy selection and navigation in your application
- Reload data

You can create a button on the [sheet](#glossary-1 "Glossary term") you are editing. This shows how to create a button that makes a selection and then navigates to another sheet. It is also possible to create a button that just performs the action, or that navigates.

Do the following:

1. In the Assets panel , open Charts and under Dashboard objects, drag a Button object to the sheet.
2. Click Add action under Actions in the properties panel.
3. Select the action you want to use.

   For some actions you need to provide details for the action. For example, for the Select values in a field action, you need to select a field, and which value to select in the field.
4. Select which navigation option to use under Navigation. You can navigate to another sheet, a story or a website.
5. Set the label of the button in Label under General in the properties panel.

You will now have a button that makes a data selection and then navigates to the place in the application you selected.

## Setting the action

You can add one or more actions to be performed when the button is clicked. For some actions you need to provide details for the action.

The actions are performed in the order they are listed under Actions. You can change the order of an action by dragging it.

Toggle Runtime evaluation on or off to change when the expressions in the button are evaluated. If this setting is turned off, the expressions in the button (for example, the value expression for a [variable](#glossary-2 "Glossary term")) are evaluated independently of one another. With the setting turned on, the expressions for each action are evaluated at the action's runtime. This allows expression values set in an action to be carried forward for future actions in the chain.

Tip noteYou do not have to add an action if you just want the button to perform navigation.

### Related video content

Configuring an action for a button is similar to setting sheet actions. The main differences are:

- Sheet actions are configured under Actions in the properties panel when the sheet is the object in focus.
- Button actions are configured under Actions and navigation in the properties panel when the button is selected.
- There are some differences between which actions are available for buttons and sheets.

For video content describing the action configurations for sheets, see [*Adding actions to sheets*](../../Sheets/setting-sheet-actions.htm).

### Apply bookmark

You can apply the selection that is defined in a bookmark that you choose.

### Clear all selections

You can clear all selections in all states in the application. You can optionally overwrite locked selections.

### Clear selections in other fields

You can clear selections from all fields except the one you specify. You can optionally overwrite locked selections.

If no selections are made in the specified field, all values in this field will be selected.

### Move forwards in your selections

You can move one step forwards in your selection history.

### Move backwards in your selections

You can move one step backwards in your selection history.

### Clear selections in field

You can clear all selections from a field that you specify.

### Lock all selections

You can lock all selections in the application.

### Lock a specific field

You can lock selections in a field that you specify.

### Unlock all selections

You can unlock all selections in the application.

### Unlock a specific field

You can unlock selections in a field that you specify.

### Select all values in a field

You can select all values in a field that you specify. You can optionally overwrite locked selections.

### Select values in a field

You can select a list of values in a field that you specify. Separate the values to select with a semi colon. You can optionally overwrite locked selections.

Information noteIt is not possible to use fields with date, timestamp, or money data type.

Information noteThis button action does not select numeric values that are stored or classified as text. For this purpose, use the Select values matching search criteria action instead.

### Select values matching search criteria

You can select all values that match the search results from a search criteria that you specify. You need to specify the search criteria as a string. You can optionally overwrite locked selections.

- If you want to use an expression, you need to enclose it in single quotes, for example, ='=Sum([Sales Amount]) > 200000'.
- If you want to search for a partial string, you need to use wild cards (\*, ?,^). If you do not use wild cards, only strings that match exactly are selected.

### Select alternatives

Select all alternative values in a field that you specify. You can optionally overwrite locked selections.

### Step cyclic dimension

Cycle fields in a selected cyclic dimension forward or backward.

#### Limitations

Step cyclic dimension has the following limitations:

- In the Qlik Analytics mobile app, buttons with the action Step cyclic dimension will only cycle dimension if the button is in a container.
- In the Qlik Analytics mobile app, buttons with the action Step cyclic dimension do not cycle the dimension in offline mode.

### Set active field

Set the active field in a cyclic dimension.

#### Limitations

Set active field has the following limitations:

- Set active field uses the position of the selected field in the cyclic dimension. If the fields are reordered in the cyclic dimension, Set active field will use the field in the same position as the originally selected field. To resolve this, select the field again in the button properties.

### Select excluded

Select all excluded values in a field that you specify. You can optionally overwrite locked selections.

### Select possible values in a field

Select all possible values in a field that you specify. You can optionally overwrite locked selections.

### Toggle field selection

You can set the button to toggle between the current selection, and a selection that adds selections defined by a search string. You can use wild cards in the search string. If you want to define a list of values you need to use the format (A|B), where A and B are values to select.

### Set variable value

You can assign a value to a variable.

### Reload data

You can run the [load script](#glossary-3 "Glossary term") to reload data.

You can also select Partial reload. For more information, see [*Partial reload*](../../Scripting/ScriptPrefixes/PartialReload.htm).

### Refresh dynamic views

Refreshes the displays of all dynamic objects on the sheet based on the current selection.

### Execute automation

You can run automations created with Qlik Automate from a button on a sheet. You can include selections made in the application and pass additional input values to the automation. To learn more, see [Qlik Automate](https://alphahelp.qliktech.com/ld/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/introduction/home-automation.htm).

#### Recommended approach: shared space

Place the automation in a shared space and give users can-edit access. Users with can-edit access can execute automations without being able to modify them.

This approach has important advantages:

- Users authenticate with their own token, not a static execution token. This means they must be signed in to Qlik Cloud.
- The automation runs with the user's ID, so you can audit who triggered it.
- Only the automation owner can edit it, regardless of space role.

You can also:

- Select Include selections to pass current app selections to the automation.
- Add input parameters for automation-specific values by defining a key and a value for each parameter.
- Click Copy input block to copy the generated input structure into your automation.

#### Alternative approach: triggered mode

If a shared space setup does not fit your use case, you can use Run mode: triggered instead. With this mode, any user with access to the sheet can run the automation regardless of whether they have access to it directly.

Be aware of the following limitations and risks:

- Anyone with access to the sheet and button can run the automation.
- The execution token is visible in browser network traffic when the button is clicked.
- The automation runs using the owner's credentials rather than the user's.
- In apps using [section access](#glossary-4 "Glossary term"), this can expose data that the clicking user would not normally be allowed to access under section access rules.
- The token can be used to call the automation from outside Qlik Cloud.
- Variable automation IDs cannot be used, since an interactive user session in the editor is required to update the execution token in the button object definition.

#### Configuring Execute automation

Do the following:

1. Under Actions and navigation in the properties panel, click Add action.
2. Under Action, select Execute automation.
3. Under Automation, select the automation you want to trigger as an action.

   The automations that are available appear in the drop-down menu.
4. Select the Include selections box.

   When you select this option, the button creates a bookmark for the current selection. The following inputs are included:

   - App ID
   - Bookmark ID
   - Sheet ID
   - User ID
   - Space ID
   - Tenant ID
   - Time

   The application ID and bookmark ID are used as inputs to the automation, and they are used to apply data selections when executing the automation.
5. Optionally, if a shared space is not suitable and you want any user with access to the sheet to be able to run the automation, select Run mode: triggered.

   You must also be the owner of the automation to configure this option. See the security considerations above before using this mode.
6. If your automation requires parameters to execute, do the following:

   1. Click Add input parameter.
   2. Under Key, enter the parameter ID.
   3. Under Value, enter the value to use.
   4. Repeat for any other parameters required.
7. Optionally, to paste an Input block for your button in your automation, click Copy input block.

   When pasted into your automation, it passes button information through as an input block.

Learn how to connect a button to an automation with the [Active intelligence tutorial](https://help.qlik.com/en-US/cloud-services/Subsystems/ApplicationAutomation/Content/tutorials/active-intelligence.htm).

#### Execute automation limitations

Execute automation has the following limitations:

- A maximum of 100 automations can be displayed for selection under Automation. If you have access to more than 100 automations and cannot find the automation you want, you can use the automation ID. The automation ID is in the segment after /editor/ in the URL before /edit or /history.

  For example, in qlik.com/automations/editor/6c201b49-cz2e-00dc-8040-464ca41457b0/edit?resourceName=Active%20Intelligence, the automation ID is 6c201b49-cz2e-00dc-8040-464ca41457b0.
- Buttons using Execute automation are not supported in Qlik Sense Mobile.
- When using Execute automation to run an automation containing Qlik Reporting blocks, [selections](#glossary-5 "Glossary term") are not passed through to the report in the automation. The session state of Qlik Automate cannot be transferred to the report composition definition that is passed to the Qlik Reporting Service. As a result, report composition and data will not reflect the selections.

  Warning noteFor apps using [section access](#glossary-6 "Glossary term"), automated reports are run using the credentials of the automation owner instead of the user triggering the report. This can expose data that users would not have access to in application section access rules.
- The Execute automation is not supported for embedded buttons.
- If the automation triggered by the button takes longer than 10 minutes to run, no notification will be sent when the automation finishes.

## Navigation

You can choose to navigate to another sheet, a [story](#glossary-7 "Glossary term"), or a website when the button is clicked. You do not have to specify an action if you want to create a simple navigation button. A button can only have one navigation option at a time.

Information noteNavigation is not supported in stories.

### Go to next sheet

Navigate to the next sheet sequentially.

### Go to previous sheet

Navigate to the previous sheet sequentially.

### Go to last sheet

Navigate to the last sheet.

### Go to first sheet

Navigate to the first sheet.

### Go to a sheet

Navigate to a specific sheet, and optionally highlight a specific chart on the sheet.

Under Sheet, enter the name of the desired sheet or select it from the list. Under Chart ID, enter the object ID for the chart or select the desired chart from the list.

Tip note

You can obtain the object ID with either of the following methods:

- In analysis mode, right-click a visualization or sheet, and then click ![Forward](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg)Share > ![Embed](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_code_outline.svg) Embed. You can then find the object ID in the dialog.
- For certain chart types, you can use the ObjectId chart function. For example, add =ObjectId() as a dimension along with any measure. The chart ID is displayed and you can write it down for future reference. For more information, see [*ObjectId - chart function*](../../Scripting/SystemFunctions/ObjectId.htm).

Information noteIf you are using expressions, the expression should resolve to the sheet ID.

### Go to a sheet defined by sheet ID

Navigate to a specific sheet. Enter the sheet ID of the desired sheet.
You can find the ID of a sheet in the URL of the browser with the sheet open. The sheet ID follows after /sheet/ followed by /.

Example: Sheet URL

qlik.com/sense/app/8f8ffa0e-3fde-48a5-a127-59645923a1fc/sheet/7300b241-f221-43db-bb8b-8c8cc1887531/state/analysis

The ID of the sheet is 7300b241-f221-43db-bb8b-8c8cc1887531 in this example.

Information noteIf you are using expressions, the expression should resolve to the sheet ID.

### Go to a story

Navigate to a specific story. Enter the name of the desired story, or select it from the list.

### Open a website or email

Open a specified website or email client. Enter the URL to navigate to. Optionally, select Open in same window to have the website or email client open in the same window.

### Generate on-demand app

Creates an on-demand application based on the current selection. You must select an on-demand application navigation link (see [*Building an on-demand application*](../../LoadData/creating-OnDemand-app.htm)). The status of the application is displayed as the application is created.

### Application chaining

You can open another existing application with the current selection applied. Specify the application you want to open by application ID. Optionally, you can specify a sheet by sheet ID, and whether you want the new application to open in the same window.

Information noteApplications always open in the same window in the Qlik Analytics mobile application.

## Styling the button

You have a number of styling options available under Appearance in the properties panel.

Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling under Appearance > Presentation to further customize the styling of the chart. The styling panel contains various sections under the General and Chart tabs.

You can reset your styles by clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) next to each section. Clicking ![Reset](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/reset.svg) Reset all resets styles for all available tabs in the styling panel.

For general information about styling an individual visualization, see [*Applying custom styling to a visualization*](../style-visualization.htm).

### Adding an icon

You can add an icon to the button under Appearance > Icon. Choose from a number of preset options.

### Customizing the text

You can set the text for the title, subtitle, and footnote under Appearance > General. To hide these elements, switch the Show titles setting to off.

Additionally, you can set the text for the button Label.

You can style the text that appears in the chart.

Do the following:

1. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
2. On the General tab, set the font, emphasis style, font size, and color for the following text elements:

   - Title
   - Subtitle
   - Footnote
3. On the Chart tab, set the text properties for the button Label. Set the font, emphasis style, text alignment, font size, and color.

   You can also choose from a number of text layout options for this label under Layout behavior. The following options are available:

   - Responsive: You can adjust the font size of the Label, with additional text size adjustments applied based on button size and text length. Adjustments are made to fit all text content into the button.
   - Fluid: You can adjust the font size of the Label, with additional text size adjustments applied based on button size only. This re-scaling of the text is independent of text length. If the text is too long, an ellipsis is inserted at the end.
   - Fixed: You can adjust the font size of the Label in pixels. If the text is too long, an ellipsis is inserted at the end.

### Customizing the background

You can customize the general background, as well as the background of the button itself. The background of each can be set by color and image. Background options can be configured by expanding Appearance > Presentation in the properties panel, then clicking ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.

#### Setting the general background

The general background of the button includes the title area, as well as the chart itself, which is partially covered by the button itself.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the General tab of the styling panel, you can select a background color (single color or expression). You can also set the background to an image from your media library or from a URL.

   Information note

   To add a background image from a URL, the URL's origin needs to be added to the allowlist in your tenant's Content Security Policy. The origin must be added with the following Directive: img-src. This is done by a [tenant administrator](#glossary-8 "Glossary term").

   For more information, see [*Creating a CSP entry*](../../Admin/mc-administer-content-security-policy.htm#AddEntry).

   When using a background color, use the slider to adjust the opacity of the background.

   When using a background image, you can adjust image sizing and position.

#### Setting the background of the button

The background of the button includes the portion that the user can click to execute the action.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
3. On the Chart tab of the styling panel, you can select a background color (single color or expression), and also set the background to an image from your media library.

   When using a background image, you can adjust image sizing and position.

### Adjusting the border of the interactive portion of the button

You can adjust the border of the part of the button the user interacts with to perform intended action.

Do the following:

1. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
2. On the Chart tab, under Border, switch the border On to display it on the button.
3. Adjust the corner radius and width.
4. Set the color of the border, either a single color or with an expression.

### Customizing the border and shadow of the entire object

You can customize the border and shadow of the entire object in which the button is located. Note that you can also adjust the border of the clickable button itself.

Do the following:

1. In the properties panel, expand the Appearance section.
2. Under Appearance > Presentation, click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
3. On the General tab of the styling panel, under Border, adjust the Outline size to increase or decrease the border lines around the chart.
4. Select a color for the border.
5. Adjust the Corner radius to control the roundness of the border.
6. Under Shadow in the General tab, select a shadow size and color. Select None to remove the shadow.

## Disabling and enabling the button

You can set a calculation condition to enable the [chart](#glossary-9 "Glossary term") under Enable chart. If the condition is evaluated to 0, the button is disabled.

## Converting from the Button for navigation in the Dashboard bundle

You can convert an existing Button for navigation control into a button. There are some limitations when you do the conversion.

- The navigation option to switch to edit mode (Switch to edit mode) is not supported.
- The action to select a value and then lock the field (Select a value and lock field) is not supported. This will be converted into two consecutive actions, Select values in a field and Lock a specific field.
