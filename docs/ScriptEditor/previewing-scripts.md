---
title: "Previewing data in load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/previewing-scripts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Previewing data in load scripts

You can preview the results of your load script without fully running the load script. When you preview data, you limit the rows of data loaded for each table and ignore any Store statements in your load script.

You can view previewed data and profiling information in the Preview section in the bottom panel.

Preview of the data

![Preview of the loaded data, showing the table Sales in table view of Preview.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DLE_Preview.png "Click to view full size")

## Previewing data

Do the following:

- Click Preview data.

  Tip noteIf you are working in Script, you can alternatively click Preview data at the bottom of the Editor.

By default, 100 rows for each table are loaded during preview. Store statements in your load script are skipped. You can change settings by clicking ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) in ![Run script without exporting data using store statements](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_run_preview.svg) Preview data and changing the preview settings.

## Previewing previously loaded data

You can preview data that has been previously loaded or previewed within an application.

If you are instead working in Script, click Preview data anywhere in the Editor to regenerate a preview of the data. See [*Previewing data*](#Previewing).

Do the following:

1. In the bottom panel, select Preview if not already selected.
2. Click Show preview.
