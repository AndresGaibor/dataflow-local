---
title: "Working with the next-gen script editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/next-gen-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Working with the next-gen script editor

[Feature in Preview](../Introduction/feature-preview-program-overview.htm)

In the Data load editor and Script, Next-gen editor provides settings for an enhanced script editing experience. This new experience includes dark mode, code folding, an embedded Command Palette, hover-based help, enhanced code refactoring and navigation, and a refreshed look and feel.

## Turning on next-gen editor features

The next-gen editor is turned off by default. When you turn one or more of these features on, they are activated for you in the Data load editor for all applications, and in the Editor for all scripts.

Do the following:

1. Open the Data load editor in an application, or the Editor in Script.
2. In the toolbar, click the Next-gen editor drop down.
3. Turn on Enable new code editor experience.

   Enable new code editor experience turned on in the Data load editor.

   ![New code editing experience turned on the Data load editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_script-editing_new-editor_preview.png "Click to view full size")
4. If desired, turn on Dark mode. This feature is only available when you have Enable new code editor experience turned on.

   Dark mode turned on in the Data load editor.

   ![Dark mode turned on the Data load editor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_script-editing_dark-mode_preview.png "Click to view full size")

## Enhancements in new code editing experience

This section outlines the new features that are available when you turn on Enable new code editor experience.

### Code assistance

Improved hover help

Hover over text as you edit the script for additional information and links to help documentation.

For more information, see [*Hovering over keywords*](../LoadData/edit-data-load-script.htm#Hovering).

Improved autocomplete

Autocomplete has been improved with a new drop down menu for suggestions. Additionally, parentheses and other enclosures automatically self-close while typing.

### Code navigation

Code navigation has been enhanced with several new features.

Definition and reference linking

New options are available—both from the right-click and menu and via keyboard shortcuts—to navigate between recognized Qlik script constructs:

- Go to Definition (Ctrl + F12): Go to the location where a script construct is defined.
- Go to References (Ctrl + F12): Go to the location where a script construct is referenced. If multiple references exist, you can choose which reference to go to.
- Peek options (Alt + F12): View definitions and references as pop-ups below the code you are currently inspecting.

For more information, see [*Definition and reference links*](../LoadData/edit-data-load-script.htm#DefinitionLink).

Code folding

You can collapse and expand blocks of code by clicking ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) and ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg).

For more information, see [*Code folding*](../LoadData/edit-data-load-script.htm#Folding).

Minimap

The minimap is shown in the top right, offering a fast way to preview the current script section without scrolling through it. This is especially helpful for long script sections.

For more information, see [*Minimap*](../LoadData/edit-data-load-script.htm#MiniMap).

### Code editing

Enhanced find-and-replace

Use the Change All Occurences option from the right-click menu (or keyboard shortcut Ctrl + F2) to find and replace selected code in the current section.

For more information, see [*Editing load scripts*](../LoadData/edit-data-load-script.htm#Searchin).

Enhanced multi-cursor selection

It is now easier to select and edit multiple script lines at a time for advanced and efficient editing.

For more information, see [*Multi-cursor selection*](../LoadData/edit-data-load-script.htm#Multi-cu).

Command Palette

The Command Palette is accessible both from the right-click menu and keyboard shortcuts. The Command Palette offers many advanced operations to support efficient writing of script.

Do one of the following:

- In the editor, right-click and select Command Palette....
- Use the keyboard shortcut Ctrl + Shift + P.

For some actions, you might have to select the text on which to perform the operation. For others, this is not needed.

After opening the Command Palette, you can search for available commands and view keyboard shortcuts for these commands.

For more information, see [*Command Palette*](../LoadData/edit-data-load-script.htm#CommandPalette).

### Code refactoring

The editor now supports refactoring of known Qlik script constructs, such as the names of tables and variables.

To refactor code, use the Rename Symbol option from the right-click menu (or use the keyboard shortcut F2).

For more information, see [*Code refactoring*](../LoadData/edit-data-load-script.htm#Refactor).

## Dark mode

With Dark mode, the script editor switches to a different color scheme with a dark background. Text and other elements appear in light colors, maintaining high contrast and readability.

[*Turning on next-gen editor features*](#TurningOn)

## Limitations

- Some interface elements, such as right-click options, Command Palette, and hover help, are not translated in Swedish or Dutch.
- Dark mode does not cover the entire user interface when activated. For example, the Qlik Cloud navigation bar and left panels, as well as some dialogs for data load and connections, do not appear in dark mode.

## Learn more

- [*Editing load scripts*](../LoadData/edit-data-load-script.htm)
- [*Keyboard shortcuts in Data load editor and Script*](../LoadData/DLE-keyboard-shortcut.htm)
- [*Using Data load editor*](../LoadData/use-data-load-editor.htm)
- [*Navigating scripts in catalog*](navigating-scripts.htm)
