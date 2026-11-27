---
title: "Saving the load script"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/save-load-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Saving the load script

When you save the [load script](#glossary-0 "Glossary term") in Data load editor or Script, the entire application or script is saved, but data is not automatically reloaded.

When the load script is saved, the application or script will still contain old data from the previous reload, which is indicated in the toolbar. If you want to update the application or script:

- In Data load editor, click ![load data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_play_2_outline.svg) Load data to fully load application data or click ![Run script without exporting data using store statements](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_preview.svg) Preview data to load a limited number of rows.
- In Script, click ![Run script without exporting data using store statements](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_preview.svg) Preview data in Script to load the load script with a limited number of rows or click ![load data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_play_2_outline.svg) Export data to run the load script in full.

The script is automatically saved when data is loaded, previewed, or exported.

Data load editor and Script save your work automatically as you make changes to your load script. You can force a save by pressing CTRL+S.

Information noteThe load script is not saved automatically in Qlik Sense Desktop. You need to save the script manually.

When you save a script, it is automatically checked for syntax errors. Syntax errors are highlighted in the code, and all script sections containing syntax errors are indicated with ![warning](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_warning.svg) next to the section label.
