---
title: "Organizing load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/organize-script-code.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Organizing load scripts

You can divide your [load script](#glossary-0 "Glossary term") into sections to organize the structure. The script is executed in the order of the sections from top to bottom. A load script must contain at least one section.

Sections Main, Dictionary and Calendar in Data load editor

![Sections in the Data load editor.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_organize_script_code_cloud-rev.png "Click to view full size")

If you have added data using Add data, you will have a data [load script](#glossary-1 "Glossary term") section named Auto-generated section that contains the script code required to load the data.

To learn more about editing data load script, see [*Editing load scripts*](edit-data-load-script.htm).

## Working with script sections

There are several ways to organize scripting sections:

- Click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to insert new script sections to organize your code. The new section is inserted after the currently selected section.
- Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg)
  next to the section tab to delete it. You need to confirm the deletion.

  Information noteDeleting a script section cannot be undone.
- Click on the section name and type to edit the name. Press Enter or click outside the section when you are finished.
- Put the cursor on ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/LUIicons_draggable.svg) and drag the section to rearrange the order.

Related learning:

- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)
