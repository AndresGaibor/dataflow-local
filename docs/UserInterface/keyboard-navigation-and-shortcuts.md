---
title: "Keyboard navigation and shortcuts in apps"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/keyboard-navigation-and-shortcuts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Interacting with the application interface"]
---

# Keyboard navigation and shortcuts in apps

Expand/Collapse all

# Keyboard navigation and shortcuts in apps

Qlik Sense supports keyboard accessibility. You can use a keyboard to navigate in your [activity centers](#glossary-0 "Glossary term"), the application overview, the toolbar, [sheets](#glossary-1 "Glossary term"), data, and [visualizations](#glossary-2 "Glossary term"). There is also a range of keyboard shortcuts.

When you navigate with the keyboard, the center of focus is highlighted.

Information noteKeyboard shortcuts are expressed assuming that you are working in Windows. For macOS, use Command instead of Ctrl.

For keyboard navigation in activity centers, see [*Keyboard navigation and shortcuts in Qlik Cloud*](../../Global_Common/HelpSites/keyboard-navigation-hub.htm).

## Application overview and toolbar

The Skip to content button is the first element when you navigate using a keyboard on the application overview page. Click Enter to skip navigation and land on Sheets on the toolbar. If you click Tab, you will open the global menu.

For more information on navigating the application overview page and the Qlik Sense toolbar, see [*Navigating in the application interface*](navigate-user-interface.htm).

How to navigate in the application overview and toolbar

Keyboard controls in the application overview and toolbar

| Keyboard navigation | Description |
| --- | --- |
| Tab | Moves focus forward. In an active menu, Tab will cycle between the menu options. If a sheet is open, Tab will also move focus to the sheet. |
| Shift + Tab | Moves focus back . In an active menu, Shift + Tab will cycle between the menu options. If a sheet is open, Tab will also move focus to the sheet. |
| Enter or Space | Opens current focus. |
| Esc | Closes an open menu. |
| Right arrow | Navigates to the next sheet or [story](#glossary-3 "Glossary term") on the application overview page. |
| Left arrow | Navigates to the previous sheet or story on the application overview page. |
| Up arrow | Navigates to the next [bookmark](#glossary-4 "Glossary term") on the application overview page. |
| Down arrow | Navigates to the previous bookmark on the application overview page. |
| Ctrl + G | Switches to grid layout. |
| Ctrl + Shift + L | Switches to list layout. |
| Ctrl + up | Navigates to first item in list. |
| Ctrl + down | Navigates to last item in list. |

## Sheet view

You can use keyboard navigation to interact with visualizations in your sheets, access options in visualization, context menus, and download visualization data.

For more information, see [*Sheet view*](../Sheets/sheet-view.htm).

How to navigate in sheet view

Keyboard controls in sheet view

| Keyboard navigation | Description |
| --- | --- |
| Tab | Moves focus forward between items in the toolbar and the visualizations in the sheet. In an active menu, Tab will cycle between the menu options. |
| Shift + Tab | Move focus backward between items in the toolbar and the visualizations in the sheet. In an active menu, Shift+Tab will cycle between the menu options. |
| Ctrl + Right arrow | Navigates to the next sheet. |
| Ctrl + Left arrow | Navigates to the previous sheet. |
| Ctrl + Home, Ctrl + Fn + Left (macOS) | Navigates to the first sheet of the application. |
| Ctrl + End, Ctrl + Fn + Right (macOS) | Navigates to the last sheet of the application. |
| Right arrow | Navigates to the next visualization in the row. |
| Left arrow | Navigates to the previous visualization object in the row. (Analysis mode) |
| Up arrow | Navigate to the visualization in the row above. (Analysis mode) |
| Down arrow | Navigate to the visualization in the row below. (Analysis mode) |
| Ctrl + up arrow | Navigate to the first visualization in the sheet. (Analysis mode) |
| Ctrl + down arrow | Navigate to the last visualization in the sheet. (Analysis mode) |
| Enter | Changes between the current visualization and View data mode. If visualization is a table, moves focus to the first data cell inside the table. |
| Shift + Enter or Space | Opens the current visualization in full screen. |
| Shift + F10, Fn + Shift + F10 (macOS) | Opens the context menu for the selected visualization. |
| Ctrl + E | Toggles sheet edit on and off. |

## Selections mode

When a user has focus on a table or [chart](#glossary-5 "Glossary term") and [selections](#glossary-6 "Glossary term") are made they are in selection mode. When cells or objects are actively selected, a selection menu displays on the top bar of the table or chart.

For more information, see [*Exploring with selections*](../Selections/SelectionsToolbar/work-with-selections.htm).

How to navigate in selections mode

### In selections menu

Keyboard controls in selections menu

| Keyboard navigation | Description |
| --- | --- |
| Shift + Tab | Moves focus from selections to the Confirm button (unless the search bar is visible in the listbox, then it moves focus there first and the next Shift + Tab moves focus to the Confirm button in the selections menu). Select Enter to Confirm selections and exit selections menu. |
| Left/Right arrow | Moves focus to ( ...) sub menu, Clear selection, Cancel selection, Confirm selection.  Information note (...) sub menu navigation: Enter sub menu and navigate with Up and Down arrows to selection options: Select all, Select possible, Select alternative, Select excluded. |
| Esc | Cancels the selection and returns focus to visualization. |
| Tab | Moves focus back to the visualization with selections retained. |

### In selections mode

Keyboard controls in selections mode

| Keyboard navigation | Description |
| --- | --- |
| Up arrow | Navigates to the row above. |
| Down arrow | Navigates to the row below. |
| Space bar | Selects value. |
| Shift + up/down arrows | Selects multiple values. |
| Enter | Confirms selections. |
| Esc | Cancels selections. |

### In current selection

Keyboard controls in current selection

| Keyboard navigation | Description |
| --- | --- |
| Tab | Navigates to next selection or Clear all fields button. |
| Enter/Space bar | If you press Enter/space bar on a current selection, it opens the list box pop-over. If you press Enter/space bar on Clear all fields, the selections are deleted. |

## List boxes

For more information, see [*Searching within selections or visualizations*](../Selections/SelectionsToolbar/search-selections.htm).

How to navigate in the list boxes

### Inside of list box

Keyboard controls in list boxes

| Keyboard navigation | Description |
| --- | --- |
| Space (on a selectable cell) | Enters Selections mode. |
| Shift + up/down arrows (on a selectable cell) | Selects multiple values. |
| Up arrow | Navigates to the cell in the row above. |
| Down arrow | Navigates to the cell in the row below. |
| Esc | Moves focus back to the object. |
| Ctrl + Space (while selecting) | Selects value and deselects all other values. |
| Ctrl + A | Selects all values. |
| Ctrl + F | Opens and focuses search form. |

### In selections mode

Keyboard controls in list boxes, in selections mode

| Keyboard navigation | Description |
| --- | --- |
| Up arrow | Navigates to the row above. |
| Down arrow | Navigates to the row below. |
| Space bar | Selects value. |
| Shift + up/down arrows | Selects multiple values. |
| Enter | Confirms selections.  When focus is on the search bar in the list box, selects whatever is in the current search. Any items currently selected that would be selected by this search are unselected. |
| Enter + Ctrl | When focus is on the search bar in the list box, clears the current selections then select the search result |
| Esc | Cancels selections. |

## Visualization context menus

The context or option menu is represented by ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).

For more information, see [*Options menu*](../Sheets/sheet-view.htm#Options2).

How to navigate in visualization context menus

Keyboard controls in visualization context menus

| Keyboard navigation | Description |
| --- | --- |
| Shift + F10, Fn + Shift + F10 (macOS) | Opens the context menu for the selected visualization. |
| Esc | Close the context menu. |
| Down arrow | Navigate the focus to the next item in the context menu. |
| Up arrow | Navigate the focus to the previous item in the context menu. |
| Right arrow | Open an item's sub-menu. |
| Left arrow | Close an item's sub-menu. |
| Enter | Performs the action for the focused item. |

## Filter panes

For more information, see [*Filter pane*](../Visualizations/FilterPane/filter-pane.htm).

How to navigate in filter panes

Keyboard controls in filter panes

| Keyboard navigation | Description |
| --- | --- |
| Space or Enter | Moves focus to the first listbox in the filter pane. Another key press brings the focus to the first value inside that listbox.  If the focus is on a collapsed listbox, press Enter to open the listbox in a pop-over. |
| Esc | Moves focus back one level (from the values to the listbox to the filter pane object). |
| Right arrow | If the focus is on an individual listbox within the filter pane, the right arrow key moves the focus to the next listbox on the right.  If the focus is on a value inside a listbox, the right arrow key moves to the next value in the listbox. |
| Left arrow | If the focus is on an individual listbox within the filter pane, the left arrow key moves the focus to the next listbox on the left.  If the focus is on a value inside a listbox, the left arrow keymoves to the previous value in the listbox. |
| Up arrow | If the focus is on an individual listbox within the filter pane, the up arrow key moves the focus to the previous listbox (to the left, or above, the current listbox).  If the focus is on a value inside a listbox, the up arrow key moves to the previous value in the listbox. |
| Down arrow | If the focus is on an individual listbox within the filter pane, the down arrow key moves the focus to the next listbox (to the right, or below, the current listbox).  If the focus is on a value inside a listbox, the down arrow key moves to the next value in the listbox. |

How to navigate in straight tables

### Outside of table

Keyboard controls in straight tables, outside of table

| Keyboard navigation | Description |
| --- | --- |
| Enter or Space | Enters View data mode. |
| Esc | Closes View data mode. |
| Shift + Enter or Space | Enters Full screen mode. |

### Inside of table

These commands work once focus is inside a cell in the table. Click the table cell to put it in focus.

Keyboard controls in straight tables, inside of table

| Keyboard navigation | Description |
| --- | --- |
| Enter or Space (on a selectable cell) | Enters Selections mode. |
| Shift + up/down arrows (on a selectable cell) | Selects multiple values. |
| Enter or Space (on header cell or other cell with an action) | Executes cell action. |
| Right arrow | Navigates to the next cell in the table. |
| Left arrow | Navigates to the previous cell in the table. |
| Up arrow | Navigates to the cell in the row above. |
| Down arrow | Navigates to the cell in the row below. |
| Esc | Moves focus back to the object. |
| Ctrl + Space (while selecting) | Selects value and deselects all other values. |

## Tables and View data mode

These keyboard controls apply to:

- Straight table visualizations.

  [*Straight table*](../Visualizations/StraightTable/sn-straight-table.htm)
- Legacy table visualizations.

  [*Table*](../Visualizations/Table/table.htm)
- Write table visualizations.

  [*Write table*](../Visualizations/WriteTable/Analyze/write-table.htm)
- View data mode for visualizations.

  [*Viewing data of visualizations*](../Visualizations/viewing-data-visualizations.htm)

Information note

Note the following:

- Pagination is always on in View data mode and write tables.
- Pagination is not available for legacy tables, but is on when you enter View data mode by putting focus on the object.
- Actions for editing cell values only apply to write tables.

How to navigate in tables and View data mode

### Outside of table or View data mode

Keyboard controls (outside of table or View data mode)

| Keyboard navigation | Description |
| --- | --- |
| Enter or Space | Enters View data mode, or puts table in focus. |
| Esc | Closes View data mode, or exits focus on table. |
| Shift + Enter or Space | Enters Full screen mode. |

### Inside of table or View data mode

These commands work once focus is inside a cell in the table. In legacy tables and View data mode, you can put the focus on a cell by pressing Enter a second time, or by clicking a cell.

Keyboard controls (inside of table or View data mode)

| Keyboard navigation | Description |
| --- | --- |
| Space (on a selectable cell) | Enters and exits Selections mode. |
| Enter | Confirms selection. |
| Shift + up/down arrows (on a selectable cell) | Selects multiple values. |
| Enter or Space (on header cell) | Expands and selects column options. |
| Right arrow | Navigates to the next cell in the table. |
| Left arrow | Navigates to the previous cell in the table. |
| Up arrow | Navigates to the cell in the row above, or between options if column options are expanded. |
| Down arrow | Navigates to the cell in the row below, or between options if column options are expanded. |
| Esc | Moves focus back to the object, changes the focus back to cell, or exits column header options. |
| Ctrl + Space (while selecting) | Selects value and deselects all other values. |
| Tab | Enters pagination footer. |
| F2 (write table only) | Edits editable column cell in focus mode. |

### In pagination and other controls

Pagination and functionality controls are at the bottom of the table. You can change how many rows are displayed, move between pages, and expand informative tooltips and legends.

Pagination footer controls (in table or View data mode)

| Keyboard navigation | Description |
| --- | --- |
| Tab | Goes to next pagination or other item. |
| Shift + Tab | Goes to previous pagination or other item. |
| Space or Enter | Selects pagination item, or opens the interactive element in focus. |
| Up arrow and down arrow (in dropdown) | Moves up and down the dropdown menu. |
| Shift + Tab or Esc | Exits pagination footer or interactive element. |

## View data mode

For more information, see [*Viewing data of visualizations*](../Visualizations/viewing-data-visualizations.htm).

How to navigate in view data mode

### In view data mode

Keyboard navigation in view data mode, inside of table

| Keyboard navigation | Description |
| --- | --- |
| Space (on a selectable cell) | Enters Selections mode. |
| Enter or Space (on header cell) | Changes the table sorting. |
| Right arrow | Navigates to the next cell in the table. |
| Left arrow | Navigates to the previous cell in the table. |
| Up arrow | Navigates to the cell in the row above. |
| Down arrow | Navigates to the cell in the row below. |
| Esc | Moves focus back to the visualization. |
| Ctrl + Shift + left arrow | Go to previous page. |
| Ctrl + Shift + right arrow | Go to next page. |
| Tab | Go to pagination controls at bottom of table. |

### In view data mode, in selections mode

Keyboard navigation in view data mode, in selections mode

| Keyboard navigation | Description |
| --- | --- |
| Enter | Confirms selection. |
| Space (on a selectable cell) | Selects or deselects a cell. |
| Up arrow | Navigates to the cell in the row above. |
| Down arrow | Navigates to the cell in the row below. |
| Esc | Cancels selections. |
| Ctrl + Shift + left arrow | Go to previous page. |
| Ctrl + Shift + right arrow | Go to next page. |
| Tab (while in table) | Go to pagination controls at bottom of table. |

### In pagination controls

Pagination controls are at the bottom of the data table. You can change how many rows are displayed and move between pages.

Keyboard navigation in data table pagination controls

| Keyboard navigation | Description |
| --- | --- |
| Tab | Go to next pagination item. |
| Shift + Tab | Go to previous pagination item. |
| Space or Enter | Select pagination item. |
| Space (when dropdown is in focus) | Opens dropdown where you can change the number of rows that are displayed. |
| Up arrow and down arrow (in dropdown) | Moves up and down the dropdown menu. |
| Shift + Tab | Leave pagination footer, go back to table. |

## Insight Advisor Search and Insight Advisor Analysis Types

For more information, see [*Creating visualizations with Insight Advisor*](../Insights/insight-advisor-create-visualizations.htm).

How to navigate in Insight Advisor Search and Insight Advisor Analysis Types

### In Insight Advisor results

Keyboard controls in Insight Advisor results

| Keyboard navigation | Description |
| --- | --- |
| Tab | Moves focus forward between items in the toolbar and the visualizations in the sheet. In an active menu, Tab will cycle between the menu options. |
| Shift + Tab | Move focus backward between items in the toolbar and the visualizations in the sheet. In an active menu, Shift + Tab will cycle between the menu options. |
| Right arrow | Navigates to the next visualization in the row. |
| Left arrow | Navigates to the previous visualization object in the row. |
| Up arrow | Navigate to the visualization in the row above. |
| Down arrow | Navigate to the visualization in the row below. |
| Ctrl + up arrow | Navigate to the first visualization in the sheet. |
| Ctrl + down arrow | Navigate to the last visualization in the sheet. |
| Enter | Enters View data mode. |
| Space or Shift + Enter | Opens the current visualization in full screen. |
| Esc | Closes the full screen mode. |
| Shift + F10, FN + Shift + F10 (macOS) | Opens the context menu for the selected visualization.  Information noteIf Shift + F10 does not work in your browser, use Alt + Shift + F10. |

### Insight Advisor assets panel

Keyboard controls in the Insight Advisor assets panel

| Keyboard navigation | Description |
| --- | --- |
| <letter key> | Navigate to the first item in the list that starts with this letter (if the item currently in focus starts with a different letter). Navigate to the next item in the list that starts with this letter (if the item currently in focus starts with the same letter). |
| Ctrl + up arrow | Navigate to the last item in the previous category. |
| Ctrl + down arrow | Navigate to the first item in the next category. |
| Up arrow | Navigate to the item immediately above the current one (asset or category). |
| Down arrow | Navigate to the item immediately below the current one (asset or category). |
| Left arrow | Navigates to the category holding the item with the current focus (when focus is on an asset). |
| Right arrow | Navigates to the first item of the selected category (when the focus is on a category). |
| Space or Enter | Selects the item that has focus. |

## Keyboard shortcuts

Some Qlik Sense features have specific shortcuts:

- [*Keyboard shortcuts in Data load editor and Script*](../LoadData/DLE-keyboard-shortcut.htm)
- [*Keyboard shortcuts used in smart search*](../Search/smart-search-keyboard.htm)

General keyboard shortcuts

Information noteThis topic does not list all available keyboard shortcuts. For example, many other keyboard shortcuts are available for the embedded Command Palette in the data load editor. See [*Command Palette*](../LoadData/edit-data-load-script.htm#CommandPalette).

Keyboard shortcuts in Qlik Sense

| Shortcut | Description |
| --- | --- |
| Ctrl + P | Prints the current view or active sheet/story. |
| Ctrl + C | Copies the selected item to the clipboard. |
| Ctrl + X | Cuts the selected item and copies it to the clipboard. When using the Google Chrome browser: if the cursor is put in front of a row in the [Data load editor](#glossary-7 "Glossary term") or in the expression editor, without selecting anything, the entire row is cut. |
| Ctrl + V | Pastes the most-recently copied item from the clipboard. |
| Ctrl + Z | Undo action. Repeat to undo earlier actions. |
| Ctrl + Y | Redo actions. |
| Ctrl + H | Opens online help in the context of the current function.  Information note Data load editor and expression editor only. |
| Ctrl + F | Opens smart search. |
| Ctrl + E | In sheet view, opens and closes the editing of the selected sheet. |
| Ctrl + S | Saves changes to the application.  Not supported in Qlik Sense, changes are automatically saved. Ctrl + S saves changes in the Data load editor |
| Ctrl + O | Opens an application file copied to the clipboard using Ctrl + C. Not supported in Qlik Sense. |
| Ctrl + A | Selects all code.  Information note Data load editor and expression editor only. |
| Ctrl + D | Deletes the content of the current line.  Information note Data load editor and expression editor only. In data load editor, Enable new code editor experience needs to be turned off. With this setting turned on, Ctrl + D selects all instances of the current symbol in the script section. |
| Ctrl + K | Comments or uncomments the selected lines in the data load editor. |
| Ctrl + 00 | Inserts a test script in the data load editor. |
| Tab | Indents code in the data load editor. |
| Shift + Tab | Outdents code in the data load editor. |
| F2 | Renames the selected symbol in the data load editor.  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Ctrl+F2 | In the data load editor, renames all occurrences of the selected symbol in the current script section.  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Ctrl+F12 | Goes to the definition or reference of the selected script element in the data load editor.  Tip noteYou can also use Ctrl + click.  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Ctrl + Shift + P | Opens the Command Palette in the data load editor.  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Ctrl + / | Comments or uncomments the selected lines.  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Alt+F12 | Peeks at the definition of the selected script element in the data load editor.  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| = | Selects multiple vertically parallel lines at one time in the data load editor (multi-cursor).  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Alt + Shift + cursor drag | Selects code from different lines at one time in the data load editor (multi-cursor).  Information note You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm). |
| Left arrow | Navigates to the previous slide in storytelling view. |
| Right arrow | Navigates to the next slide in storytelling view. |
| Up arrow | Scrolls up in a table. |
| Down arrow | Scrolls down in a table. |
| Ctrl + left arrow | Navigates to the previous sheet in sheet view. |
| Ctrl + right arrow | Navigates to the next sheet in sheet view. |
| Ctrl + Home, Cmd + Fn + Left (macOS) | Navigates to the first sheet of the application in sheet view. |
| Ctrl + End, Ctrl + Fn + Right (macOS) | Navigates to the last sheet of the application in sheet view. |
| Esc | Exits play mode in storytelling view. Deselects a visualization when editing in sheet view. Deselects an object. Undoes selections in a visualization. Closes a dialog or window. |
| Delete | Deletes selected item. |
| Backspace | Deletes selected item. |
| Enter | Performs the action for the active option or button (for example, in dialogs). |
| Ctrl + + | Zoom in. |
| Ctrl + - | Zoom out. |
| Ctrl + 0 | Reset zooming. |
| Shift | When held while dragging and dropping a field into a sheet, adds the field as a filter pane. |
| Alt + Shift + O, Option + Shift + O (macOS) | Opens the application overview. |
| Alt + Shift + S, Option + Shift + S (macOS) | Opens sheet view. |
| Alt + Shift + Y, Option + Shift + Y (macOS) | Opens storytelling view. |
| Alt + Shift + R, Option + Shift + R (macOS) | Opens Reporting section of the application. |
| Alt + Shift + D, Option + Shift + D (macOS) | Opens Data manager. |
| Alt + Shift + E, Option + Shift + E (macOS) | Opens Data load editor. |
| Alt + Shift + M, Option + Shift + M (macOS) | Opens Data model viewer. |
| Alt + Shift + G, Option + Shift + G (macOS) | Opens the logical model. |
| Alt + Shift + V, Option + Shift + V (macOS) | Opens the application vocabulary section. |
