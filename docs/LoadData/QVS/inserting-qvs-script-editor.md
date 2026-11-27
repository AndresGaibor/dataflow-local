---
title: "Inserting other scripts into load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/QVS/inserting-qvs-script-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Inserting other scripts into load scripts

You can insert scripts, both other scripts created in Qlik Cloud and QVS files, into load scripts in Data load editor and Script. This allows you to reuse scripting content across multiple scripts.

You insert other scripts into your load script from Data sources in your script editor. Inserting the script adds the system variable Must\_Include with the definition of the script ID in the case of other scripts or the path to the QVS file. For example, $(Must\_Include=lib://DataFiles/test.qvs). For more information on Must\_Include, see [*Include*](../../Scripting/SystemVariables/Include.htm).

## Viewing included scripts

Under Included scripts, you can view scripts or QVS files you have inserted that have been successfully included during the last run of Preview data, Load data, or Export data. You can select a script or QVS file to preview the inserted load script.

Included scripts in Script

![Script editor showing a QVS script selected in Included scripts.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Scripting/ui_script-editor-qvs-preview.png "Click to view full size")

In the load script, you can click </> after an inserted script to view a preview of the inserted script.

Preview of an inserted QVS script in Script

![Preview of an inserted QVS script in Script editor. The preview shows the QVS script with an option to Open the script.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Scripting/ui_script-qvs-preview-load-scripts.png "Click to view full size")

## Inserting scripts from Data catalog

Do the following:

1. In Data sources,click Include script.
2. Select the script and click Next.
3. Click Insert.

## Inserting QVS from Data connections

Do the following:

1. In Data source, under Data connections do one of the following:

   - For uploaded QVS files, under DataFiles, click ![Select script](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_script_ok_outline.svg).
   - For QVS files in web storage, under the corresponding web storage connection, click ![Select script](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_script_ok_outline.svg).
2. Select the script and click Next.
3. Click Insert script.

## Permissions

When inserting a different script into your load script, you need to have certain permissions for the space containing the inserted script. For more information, see [*Permissions for inserting scripts*](../../Scripting/SystemVariables/Include.htm#Permissions).
