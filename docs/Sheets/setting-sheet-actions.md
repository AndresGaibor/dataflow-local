---
title: "Adding actions to sheets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/setting-sheet-actions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with sheets"]
---

# Adding actions to sheets

You can set actions to [sheets](#glossary-0 "Glossary term") that trigger when users navigate to the sheet. Sheet actions are useful when you want to assist application users with predefined selection or selection controls when they navigate to a sheet. For example, a sheet could automatically apply a [bookmark](#glossary-2 "Glossary term") or clear all [selections](#glossary-3 "Glossary term") when users navigate to the sheet.

Sheet actions can be configured in the properties panel.
You can add multiple actions to a sheet. The actions are performed in the order they are listed under Actions. You can change the order of an action by dragging it.

For a visual demo about adding actions to sheets, see [Adding actions to sheets](https://share.vidyard.com/watch/P2LTiTvmDTMcbkDuSxqVtG?).

Information note

All expressions used in sheet actions are evaluated before the actions are performed. For example, you could not use an expression in an action that selects results from a previous action as the expression evaluates before the selection is made by the action.

Sheet actions are not triggered if the sheet is an embedded sheet or in a mashup.

Do the following:

1. In sheet view, click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click Actions in the properties panel of the sheet.
3. Click Add action.
4. Select the action you want to use.

   For some actions you need to provide details for the action. For example, for the Select values in a field action, you need to select a field, and which value to select in the field.
5. Optionally, after Label, enter a name for the action.

## Available sheet actions

You can add one or more actions to be performed when users navigate to the sheet. For some actions, you need to provide details for the action.

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

### Select excluded

Select all excluded values in a field that you specify. You can optionally overwrite locked selections.

### Select possible values in a field

Select all possible values in a field that you specify. You can optionally overwrite locked selections.

### Toggle field selection

You can set the button to toggle between the current selection, and a selection that adds selections defined by a search string. You can use wild cards in the search string. If you want to define a list of values you need to use the format (A|B), where A and B are values to select.

### Set variable value

You can assign a value to a variable.
