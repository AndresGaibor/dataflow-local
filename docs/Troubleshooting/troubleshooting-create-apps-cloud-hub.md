---
title: "Troubleshooting - Creating applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Troubleshooting/troubleshooting-create-apps-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Troubleshooting - Creating applications

## There are no data sources in the application I uploaded to Qlik Cloud Analytics

I uploaded an application to Qlik Cloud Analytics, but all the attached files and data connections have been removed from the application.

Possible cause

Exporting and uploading an application removes the attached files and data connections from an application.

Proposed action

Reattach these files and reconfigure the data connections for the application.

## Error message: The visualization failed to render

When I uploaded my application, the error message The visualization failed to render displayed on one or more [visualization](#glossary-0 "Glossary term") objects in my sheets.

Possible cause

Your application may be from an unsupported version of Qlik Sense. Applications must be from Qlik Sense 3.1 or later.

Proposed action

Update the application to a more recent version of Qlik Sense by updating the Qlik Sense deployment. You can also import the application into a more recent version of Qlik Sense and then export the application again.

## Error message: Invalid visualization. The extension is not available in the cloud

When I uploaded my application, the error message Invalid visualization. This visualization was not found. The extension is not available in the cloud displayed on one or more of my extensions.

Possible cause

You uploaded an application that contained an unsupported extension.

Proposed action

Remove the invalid extensions from your application. To find out which extensions are valid, see [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm).

## My application failed to export

When I tried to export my application, it failed.

Possible cause

Your application may use section access for security in the data load script.

Proposed action

For security reasons, exporting applications that use section access is not permitted.

## Thumbnails are not included when copying a sheet

Possible cause

You have copied a sheet from another application. Thumbnails are stored as application resources and are not included when you copy a sheet. Copying sheets within an application works fine.

Proposed action

You can copy an entire application and use that as starting point. This will include all resources, such as images.

## Right-to-left reading order works for some visualizations, but not others

Possible cause

You might notice some visualizations in Qlik Sense can display right-to-left languages such as Arabic or Hebrew without right-to-left reading order being activated in the application. However, to guarantee that the right-to-left reading order is applied correctly at all times and to all visualizations in the application, you need to activate this setting in the application.

Proposed action

Activate right-to-left reading order in the application to ensure the setting is applied to all visualizations in the application.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then click ![Settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Settings.
2. In the menu, switch to the Appearance tab.
3. Turn Right-to-left on or off.

Information noteIf a visualization is shared using Qlik Sense Charts, changing the reading order in the application will also affect the reading order in the shared chart. For more information, see  [*The reading order is incorrect in my shared chart*](troubleshooting-navigate-interact.htm#Right-to).
