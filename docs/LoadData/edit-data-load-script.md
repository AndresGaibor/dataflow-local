---
title: "Editing load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/edit-data-load-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Editing load scripts

Expand/Collapse all

# Editing load scripts

You write the script in the text editor of the [Data load editor](#glossary-0 "Glossary term") or Script.
Here you can make manual changes to the LOAD or SELECT statements you have generated when selecting data, and type new script.

The script, which must be written using Qlik script syntax, is color coded to make it easy to distinguish the different elements. Each script line is numbered.

There are a number of functions available in the editor to assist you in developing the [load script](#glossary-1 "Glossary term"), and they are described in this section.

## Code assistance

### Accessing syntax help for commands and functions

There are several ways to access syntax help for a Qlik syntax keyword.

#### Hovering over keywords

You can hover over script functions and keywords in the script to learn more about formatting syntax, and to access help resources.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

#### Accessing the help portal

You can access detailed help in the help portal in the following ways:

- Click ![Help](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_help_outline.svg) in the toolbar to enter syntax help mode.
  In syntax help mode you can click on a syntax keyword (marked in blue and underlined) to access syntax help.
- Place the cursor inside or at the end of the keyword and press Ctrl+H.
- If you have Enable new code editor experience activated, hover over a keyword and click the help link if available. See [*Hovering over keywords*](#Hovering).

Information noteYou cannot edit the script in syntax help mode.

#### Using the auto-complete function

If you start to type a Qlik script keyword, you get an auto-complete list of matching keywords to select from. The list is narrowed down as you continue to type, and you can select from templates with suggested syntax and parameters. A tooltip displays the syntax of the function, including parameters and additional statements, as well as a link to the help portal description of the statement or function.

Tip note

You can also use the keyboard shortcut Ctrl+Space to show the keyword list, and Ctrl+Shift+Space to show a tooltip.

## Code navigation

### Accessing syntax help for commands and functions

There are several ways to access syntax help for a Qlik syntax keyword.

#### Hovering over keywords

You can hover over script functions and keywords in the script to learn more about formatting syntax, and to access help resources.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

#### Accessing the help portal

You can access detailed help in the help portal in the following ways:

- Click ![Help](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_help_outline.svg) in the toolbar to enter syntax help mode.
  In syntax help mode you can click on a syntax keyword (marked in blue and underlined) to access syntax help.
- Place the cursor inside or at the end of the keyword and press Ctrl+H.
- If you have Enable new code editor experience activated, hover over a keyword and click the help link if available. See [*Hovering over keywords*](#Hovering).

Information noteYou cannot edit the script in syntax help mode.

### Definition and reference links

You can use the right-click menu or keyboard shortcuts to navigate between related script elements (such as specific tables or variables).

The following options are available:

- Go to Definition (Ctrl + F12): Go to the location where a script construct is defined.
- Go to References (Ctrl + F12): Go to the location where a script construct is referenced. If multiple references exist, you can choose which reference to go to.
- Peek options (Alt + F12): View definitions and references as pop-ups below the code you are currently inspecting.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

### Code folding

You can expand and collapse blocks of script code, improving flexibility and readability during editing.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

To fold code blocks, hover in the margin next to a block that supports folding and click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg). You can unfold code by clicking ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) on collapsed blocks.

The Command Palette also offers advanced options for code folding. See [*Command Palette*](#CommandPalette).

### Minimap

The minimap offers a visual representation of the current script section. It is located beside the editor, offering a view of the entire section at a glance. The minimap is interactive—you can use it to scroll through the section to find specific code.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

## Code editing

### Inserting a prepared test script

You can insert a prepared test script that will load a set of inline data fields. You can use this to quickly create a data set for test purposes.

Do the following:

- Press Ctrl + 00.

The test script code is inserted into the script.

### Indenting code

You can indent the code to increase readability.

Do the following:

1. Select one or several lines to change indentation.
2. Click ![Indent](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_indent_outline.svg) to indent the text (increase indentation) or, click ![Undent](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_undent_outline.svg) to outdent the text (decrease indentation).

Tip note

You can also use keyboard shortcuts:

Tab (indent)

Shift+Tab (outdent)

### Searching and replacing text

You can search and replace text throughout script sections.

#### Searching for text

 Do the following:

1. Click ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg) in the toolbar.

   The search drop-down dialog is displayed.
2. In the search box, type the text you want to find.

   The search results are highlighted in the current section of the script code. Also, the number of text instances found is indicated next to the section label.
3. You can browse through the results by clicking ![Previous](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) and ![Next](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg).
4. Click ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg) in the toolbar to close the search dialog.

Tip noteAlso, you can select Search in all sections to search in all script sections. The number of text instances found is indicated next to each section label. You can select Match case to make case sensitive searches.

#### Replacing text

Do the following:

1. Click ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg) in the toolbar.

   The search drop-down dialog is displayed.
2. Type the text you want to find in the search box.
3. Type the replacement text in the replace box and click Replace.
4. Click ![Next](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to find next instance of search text and do one of the following:

   - Click Replace to replace text.
   - Click ![Next](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to find next.
5. Click ![Search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg) in the toolbar to close the search dialog.

Tip noteYou can also click Replace all in section to replace all instances of the search text in the current script section. The replace function is case sensitive, and replaced text will have the case given in the replace [field](#glossary-2 "Glossary term"). A message is shown with information about how many instances that were replaced.

#### Alternative methods

You can also use other methods to search and replace text.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

The following other methods are available:

- Change All Occurrences: Available from the right-click menu and via keyboard shortcut Ctrl + F2. This finds and replaces all matching text in the current script section.
- Command Palette: You can perform find-and-replace actions using the embedded Command Palette. See [*Command Palette*](#CommandPalette).

### Commenting in the script

You can insert comments in the script code, or deactivate parts of the script code by using comment marks. All text on a line that follows to the right of // (two forward slashes) will be considered a comment and will not be executed when the script is run.

The toolbar contains a shortcut for commenting or uncommenting code. The function works as a toggle. That is, if the selected code is commented out it will be commented, and vice versa.

#### Commenting

Do the following:

1. Select one or more lines of code that are not commented out, or place the cursor at the beginning of a line.
2. Click ![Comment / Uncomment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_comment_outline.svg), or press Ctrl + K.

   Information noteIf you have Enable new code editor experience turned on, you can also use Ctrl + /.

The selected code is now commented out.

#### Uncommenting

Do the following:

1. Select one or more lines of code that are commented out, or place the cursor at the beginning of a commented line.
2. Click ![Comment / Uncomment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_comment_outline.svg), or press Ctrl + K.

   Information noteIf you have Enable new code editor experience turned on, you can also use Ctrl + /.

The selected code will now be executed with the rest of the script.

Tip note

There are more ways to insert comments in the script code:

- Using the Rem statement.
- Enclosing a section of code with /\* and \*/.

Example:

```
Rem This is a comment ;
/* This is a comment
   that spans two lines */
// This is a comment as well
```

For more information about Rem, see [*Rem*](../Scripting/ScriptRegularStatements/Rem.htm).

### Selecting all code

You can select all code in the current script section.

Do the following:

- Press Ctrl + A.

All script code in the current section is selected.

### Multi-cursor selection

With multi-cursor selection, you can select code from multiple different script lines at a time.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

Do one of the following:

- Press Ctrl + Alt + arrow up/down to select multiple parallel lines vertically at once.
- Press Alt + Shift and then drag your cursor in any direction to select adjacent code together.

### Command Palette

The Command Palette is embedded into the script editor, making it easier to perform advanced operations on script code. The Command Palette also supports several options for enhancing the look and feel of the editor.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

Examples of uses for the Command Palette include:

- Find and replace
- Advanced code folding
- Code indentation
- Advanced text processing
- Customizing editor interface, such as font size, word wrapping, and more

For examples of specific workflows, see [*Example workflows: Command Palette*](#Examples).

Do one of the following:

- In the editor, right-click and select Command Palette....
- Use the keyboard shortcut Ctrl + Shift + P.

For some actions, you might have to select the text on which to perform the operation. For others, this is not needed.

After opening the Command Palette, you can search for available commands and view keyboard shortcuts for these commands.

#### Example workflows: Command Palette

Find and replace text with the Command Palette

Do the following:

1. Open a script section.
2. Select the text you want to find and replace.
3. Right-click anywhere in the editor, and select Command Palette....
4. Select Replace.
5. Enter the text to find.
6. Enter the text to replace the found text.
7. Select to replace all instances or one instance at a time.

Collapse (fold) code

Do the following:

1. Open a script section with tables, loops, subroutines, or other content that support folding.
2. Right-click anywhere in the editor, and select Command Palette....

   The Command Palette opens.
3. Select Fold All.
4. To unfold all folded code, open the Command Palette again and select Unfold All.

Turning on word wrap

Do the following:

1. Open a script section.
2. Right-click anywhere in the editor, and select Command Palette....
3. Select View: Toggle Word Wrap or enter Alt+Z on the keyboard.

Word wrap is activated for the script section.

## Code refactoring

With Enable new code editor experience turned on, you can refactor recognized Qlik script constructs. For example, you can rename all instances of a table in the script.

Information note

You need to turn on Enable new code editor experience. See [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm).

Do the following:

1. Place your cursor on a script construct that you want to rename, or highlight the construct in full.
2. Right-click and select Rename Symbol, or use the keyboard shortcut F2.

The construct is renamed across the script.

## Limitations

With Enable new code editor experience turned on, some interface elements, such as right-click options, Command Palette, and hover help, are not translated in Swedish and Dutch.

Related learning:

- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)

## Learn more

- [*Working with the next-gen script editor*](../ScriptEditor/next-gen-editor.htm)
- [*Keyboard shortcuts in Data load editor and Script*](DLE-keyboard-shortcut.htm)
- [*Using Data load editor*](use-data-load-editor.htm)
- [*Navigating scripts in catalog*](../ScriptEditor/navigating-scripts.htm)
- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)
